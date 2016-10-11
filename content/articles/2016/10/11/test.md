Title: RBM Choice Models
Date: 2016-10-01 10:20:04


## Context
Modeling customers' choices is an important step towards understanding how purchase decisions are made as well as being able to quantify the magnitude of tradeoffs among product functions.

Traditional approaches to constructing choice models assume IIA (Independence of Irrelevant Alternatives) -- which include MLM, Conjoint Analysis, etc.  In reality, it is impractical to assume that every customer has equal exposure to all choices when making a decision.

As we continue to gather online engagement data, product browse/click tracking data gives us a direct signal to model a customer's decision behavior.  Essentailly, we can categorize each visit to the site as a customer trip, then add a binary label to the product being purchased versus the other products being viewed in the session.  Products being viewed are grouped into a "choice set" and the product being purchased is known as the "selection set".  While the maximum size of a choice set is limited to the number of products in an assortment, in reality, the size of the choice set on a per-customer bases will be significantly smaller (i.e. customers will normally consider only a few products when deciding to make a purchase).  In our use case, the average choice set contains approximately 15 products; this is the typical challenge under IIA assumption - the number of available products can sometimes be in the millions (i.e. Amazon) which create very sparse choice sets.

To tackle this unique problem, we studied several methods including lower bound non-parametric models, rank based EM models, and [RBM Human Choice].  These are the most recent emerging approaches to solve sparsity choice models with limited data.  The RBM approach is appealing in that we can also derive side-by-side complimentary, substituted, and attractive effects.

## Implementation
We implemented the solution using Python + Chainer on three Nvidia GeForce TITAN X GPUs.  The network is a binary RBM (visible and hidden) with adaptive weight decay.  To speed up the training, we adopt K-contrasive divergence learning, which essentially is a K-steps gibbs sampling method.  The weights are updated through reconstruction error on the visible layer via sigmoid cross entropy.

## Results

Use trained hidden-to-visible weights to calculate choice rate

$$\lambda(x|X)\equiv exp(b_{x})\displaystyle\prod_{k\in K} (1 + exp(T_{X}^{k} + U_x^{k}))$$

where $$x \in X$$ and $$T_X^{k} \equiv \displaystyle\sum_{Y \in X} T_Y^{k}$$

We can use these probabilities to compare two products in a choice set.

![alt text](/images/ysl_handbags.png "YSL")

![alt text](/images/ugly_handbag.png "Extreme Difference")


  - Take the most frequent pairs of products in our validation data
  - Calculate their choice rate
  - Calculate their choice rate from each choice set that they occur in in the validation data
  - Calculate the KL-Divergence between these two distributions and use this metric as the graph weight 

![alt test](/images/graph.png "KLD-Graph")


  - We can also calculate attraction effect.  If we have two products in a choice set, how does the addition of a third product affect customer choice?
  - The strength of the attraction effect of a product C on A is defined as

$$\psi_{A,C,X}^{(att)}\equiv\frac{p(A|X \cup \{C\})}{p(A|X)}$$

  - When this equation is greater than one there is an attraction effect.
  - Product B is prefered much more than product A

![alt text](/images/pre_attraction.png "Before addition of attraction")

  - After the addition of a product C, the probability of product A has increased almost 15 fold.

![alt text](/images/post_attraction.png "Post attraction")

  $$\frac{0.011424}{0.000762} = 14.987$$

![alt text](/images/attraction_graph.png "Attraction graph")

## Conclusion/Future Work






## References
[1] Osogami, Takayuki and Otsuka, Makoto.  Testricted Boltzmann Machines modeling human choice.  *IBM Research - Tokyo*.

[RBM Human Choice]: <http://papers.nips.cc/paper/5280-restricted-boltzmann-machines-modeling-human-choice.pdf>

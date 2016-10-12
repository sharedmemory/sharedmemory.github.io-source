Title: Customer Choice Model and Attraction Effect
Date: 2016-10-12 13:45:57

## Context
Modeling customers' choices is a key technique to analyze how purchase decisions are made and also allows us to quantify the magnitude of features tradeoffsacross product functions in customer’s decision process.

The basic idea of a choice model is to understand which product a customer would prefer to purchase when she is presented with a list of product choices. For example in fashion, we want to estimate the scale of preference towards buying a black Gucci wallet priced at $2,000 vs other options of designers/colors priced $1,500 to $3,000. Most of the time we are interested in much larger choice combinations (e.g. materials, promotion, shape).

Traditional approaches to choice models e.g. MLM assumes IIA(Independence of Irrelevant Alternatives), which cannot represent some key phenomena that we are interested in (as mentioned in [[2]]).  Several methods have been studied and proposed; as we continued to explore many of them, [[1]] proposed an interesting RBM variation that extends MLM to represent the scenario where choice options can vary among customers. It is also straightforward to implement.

##Problem Formulation
Our goal is to estimate the trade-off effect in purchases among a given choice set. Eventually, we want to apply the trade-off to all customers who we can observe such behavior. There are many types of source data that come to mind. Among them, website behavior is by far the richest; we can directly observe each visitor's choice options and her final selection. For each visitor to the website, we construct her choice set from products she viewed; the final selection is the product she purchases.  We consider this level of design as demand based choices.

In our experiments, we explored other forms of problem designs, and each one of them reflects very different types of choice phenomena.  For instance, we can treat visitors' purchases as our choice set, and then select the set that represents only those products she eventually kept and did not return.  This problem design reflects some subtle decisions related to actual fit, size, and quality. We call this problem design utility based choice.

There are many such designs that can be defined based on the business use cases. Here we share the experiment related to demand based choices.

In our experiment, the size of the choice set is 18,000 (total number of unique styles). The average choices (average number of unique styles per observation) is around 13. Following the design of [[1]], our RBM layers are:

$$$$

<INSERT PICTURE OF NETWORK>

$$$$

As we continue to gather online engagement data, product browse/click tracking data gives us a direct signal to model a customer's decision.  Essentially, we can categorize each visit to the site as a customer trip, then add a binary label to the product being purchased versus the other products being viewed in the session.  Products being viewed are grouped into a "choice set" and the purchased product is known as the "selection set".  While the maximum size of a choice set is limited to the number of products in an assortment, in reality, the size of the choice set on a per-customer bases will be significantly smaller (i.e. customers will normally consider only a few products when deciding to make a purchase). In our use case, the average choice set contains approximately 15 products; this is the typical challenge under IIA assumption - the number of available products can sometimes be in the millions (i.e. Amazon) which create very sparse choice sets.

To tackle this unique problem, we studied several methods including lower bound non-parametric models, rank based EM models, and [RBM Human Choice].  These are the most recent emerging approaches to solve sparsity choice models with limited data.  The RBM approach is appealing in that we canal so derive side-by-side complimentary, substituted, and attractive effects.

## RBM Network
We implemented the solution using Python + Chainer on three Nvidia GeForceTITAN X GPUs.  The network is a binary RBM (visible and hidden) with adaptive weight decay.  To speed up the training, we adopt K-contrastive divergence learning, which performs adaptive K-step Gibbs sampling.  The weights are updated through reconstruction error on the visible layer via sigmoid cross-entropy.

## Results
We used the trained hidden-to-visible weights to calculate choice rate, which is given by the formula:

$$\lambda(A|\mathcal{X}) = \displaystyle\sum_{h}exp(-E_{\theta}((\upsilon^{\mathcal{X}}, \omega^{A}), h)) = exp(b_{A})\displaystyle\prod_{k}\sum_{h_{k} \in \{0,1\}}exp((T_{\mathcal{X}}^k + U_{A}^k)h_{k})$$

We can use these probabilities to compare any two products in a choice set.

**Example**:

![alt text](/images/ysl_handbags.png "YSL")

![alt text](/images/ugly_handbag.png "Extreme Difference")


  - Take the most frequent pairs of products in our validation data.
  - Calculate their choice rate (this will be the "theoretical").
  - Calculate their choice rate from each choice set that they occur in in the validation data (this will be the "actual").
  - Calculate the KL-Divergence between these two distributions and use this metric as the graph weight.

![alt test](/images/graph.png "KLD-Graph")


  - We can also calculate attraction effect.  If we have two products in a choice set, how does the addition of a third product affect customer choice?
  - The strength of the attraction effect of a product C on A is defined as:

$$\psi_{A,C,\mathcal{X}}^{(att)}\equiv\frac{p(A|\mathcal{X} \cup \{C\})}{p(A|\mathcal{X})}$$

  - When this equation is greater than one there is an attraction effect.
  - Product B is preferred much more than product A.

![alt text](/images/pre_attraction.png "Before addition of attraction")

  - After the addition of a product C, the probability of product A has increased almost 15 fold.

![alt text](/images/post_attraction.png "Post attraction")

  $$\frac{0.011424}{0.000762} = 14.987$$

![alt text](/images/attraction_graph.png "Attraction graph")

## Next Steps

## References
1. Takayuki Osogami, Makoto Otsuka.  Restricted Boltzmann Machines Modeling Human Choice.  *IBM Research - Tokyo*

2. Garrett van Ryzin, Gustavo Vulcano.  An Expectation-Maximization Method to Estimate a Rank-based Choice Model of Demand.  *Operations Research*, 2016-08.

3. Takayuki Osogami, Makoto Otsuka.  A Deep Choice Model.  *Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence*, 21 February 2016.



[1]: http://papers.nips.cc/paper/5280-restricted-boltzmann-machines-modeling-human-choice.pdf
[2]: http://pages.stern.nyu.edu/~gvulcano/EMPrefListsRev4.pdf
[3]: http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/view/12098/11674

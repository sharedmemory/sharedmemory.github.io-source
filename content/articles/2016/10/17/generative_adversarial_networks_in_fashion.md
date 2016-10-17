Title: Adversarial Networks in Fashion
Date: 2016-10-11 11:35:56


Recent generative model research has developed a class of methods known as Generative Adversarial Networks (GANs).  These models adopt a game theoritc approach to training; to networks D (discriminator) and G (generator) "play a game" where D is trained to learn generated data from real data and G is trained to confuse D that the data it's generating is real.  Several variants of these networks [[1](https://arxiv.org/pdf/1511.05644v2.pdf), [2](http://arxiv.org/abs/1511.06434)] have produced unbelieveably accurate samples.


## Handbag Addition

This is a "fashion" edition of the results from [[2](http://arxiv.org/abs/1511.06434)] where the authors perform vector arithmetic in z-space.  The classic example is:

**with man-with-glasses - man-without-glasses + woman = woman-with-glasses**

In our case, using handbags, the transition is much more subtle and not obvious, and up to interpretation as to what features the final product extracts from each image.


![alt text](/images/handbag_addition.jpg  "Addition")


Taking 100 random points in z-space and varying the mean and standard deviation, we are able to generate what appears to be a transition from a handle-less clutch to much wider handbag with a handle.

![alt text](/images/handbag_transformation.jpg  "Z-Transformation")

## Thoughts
An interesting experiemnt could be taking products that a shopper has viewed or purchased and using these techniques, create new patters/shapes/styles tayolred specificlly to that individual.



## References
[1] Brendan Frey, Ian Goodfellow, Navdeep Jaitly, Alireza Maklhzani, and Jonathon Shlens.  Adversarial Autoencoders. *arXiv:1511.05644v2 [cs.LG]*, 25 May 2016.

[2] Soumith Chintala, Luke Metz, and Alec Radford.  Unsupervised Representation Learning
with Deep Convolutional Generative Adversarial Networks.  *arXiv:1511.06434v2*, 07 January 2016.

[3] Xi Chen, Viki Cheung, Ian Goodfellow, Alec Radford, Tim Salimans, Wojciech Zaremba.  Improved Techniques for Training GANs.  *arXivL1606.03498v1 [cs.LG]*, 10 June 2016.

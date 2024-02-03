# Team Process Mapping Take-Home Task: Matthew Burke.

Goal: In this pre-test, you will first read brief selections from two social science papers (Step 1). You will then go through an end-to-end implementation of a feature and apply it to a dataset of team conversations (Step 2). Finally, you will write a reflection on how well you think this feature extractor performed on the data, as well as how well it performs in operationalizing social science constructs (Step 3).

The idea behind this task is to give you a flavor of the scope of our work — to show how we take inspiration from social science, then apply these ideas in a computational way.

Please write your reflection in this README document.

## 1. High-Level Questions
1a. Which dataset did you choose?

While the analysis was run on both datasets, I chose the CSOPLI dataset because it is smaller, and the context is less specific.

1b. What method(s) did you choose? In 1-2 sentences each, describe your sentiment analysis method(s).

My method captures West's concept of Team Optimism by detecting emotional positivity, and Troth's concept of conflict regulation by detecting anger and disagreement.

I used the BERTweet transformer model, which is a RoBERTa model pretrained on twitter and fine-tuned for the task of sentiment analysis. I chose this model because it had the best performance on the TweetEval benchmark, which is a related problem where I expect transfer learning to be effective.

https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis
https://aclanthology.org/2020.emnlp-demos.2/
https://arxiv.org/abs/2005.10200v2

1c. Does your method capture any of the ideas from Troth et al. and West et al.? If so, which ones?

My method captures West's concept of Team Optimism by detecting emotional positivity, and Troth's concept of conflict regulation by detecting anger and disagreement.

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

One strength of my approach is that it does not rely on self evaluations, and it can be replicated or extended at a much lower cost, possibly leveraging existing conversational datasets, or even scraped chatlogs. One limitation of my approach is that it relies entirely on dialogue, and that the positivity it captures is narrower in scope. While Team Optimism is directly captured, Team Resilience and Team Efficacy are only captured insofar as they impact emotional positivity. Another limitation is that BERTweet is pretrained on Twitter, and may fail to generalize in some contexts. While task-specific data is given, it is unlabeled, and thus cannot be easily used to fine-tune the model. 

## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

Visual inspection shows that BERTweet seems to get approximately 75% of the examples correct. Errors are often low confidence or are due to domain specific vocabulary ("asshole" is a lot less emotionally charged on r/AITA). Fine tuning on hand labeled data would likely improve results further, especially for the jury dataset.

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

I would use the Mean Squared Error as my evaluation metric. Although this is a classification task, labels are best treated as a scalar in range [-1, 1], so that, when the true value is positive, a neutral prediction is penalized less harshly than a negative one.

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

I would take the dot product of each prediction and [-1 0 1] to get a scalar. Then I'd compute the Mean Squared Error of the predicted scalars and some human labels.

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

One challenge is that the dataset provided does not include labels. While hand labeling the entire dataset might be too expensive, labeling a smaller subset (100 examples) would not be cost-prohibitive.

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

Completing the actual task took 6 hours, most of which was spent on lit review, hand labeling and the writeup. The code was pretty straight forward, though it took a while to finish running on my laptop. If you include the time I spent on the rabbit hole of weak supervision and self training, you can probably more than double those numbers (maybe triple once I spend the time needed to actually get it to work), though that is more of an potential extension. The project itself was reasonably scoped, but the open ended nature made it very easy to be much more ambitious than is actually neccessary. Using unlabeled data to fine tune the model is an admirable goal, but implementing a novel self-training method from a research paper is definitely far outside of the project scope, and would have taken too much time to actually complete.

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

I approached the task by first reviewing the provided papers, then by spending a coupke hours reviewing relevant papers and models so I had a good idea of what the task actually is, what tasks I'd expect to transfer well, and thus what needed to be implemented. In retrospect, this did result in me spending a lot of time on the problem of fine tuning a text classifier on unlabeled data, but other than that detour and the time initially spent on lit review, it went fairly smoothly. If I had more time, I would have implemented a self training optimization loop like that proposed in Sosea et al and Gera et al. I would also spend more time on optimization, as inference probably was slower than it needed to be.

https://arxiv.org/abs/2210.17541
https://aclanthology.org/2022.findings-emnlp.350.pdf

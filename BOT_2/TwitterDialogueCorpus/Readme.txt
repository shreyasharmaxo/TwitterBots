### Description

This directory contains the Twitter Dialogue Corpus, collected in the first half of 2011 using a procedure similar to one described by Ritter et al. (2010). The dataset is split into train, valid and test sets containing respectively 749,060, 93,633 and 10,000 dialogues.

Due to Twitter's terms of Service, we are not allowed to redistribute the actual corpus. Therefore, we provide instead the tweets in the following format. The train, valid and test set tweets are each contained in their own file, where each line corresponds to one dialogue. Each line conists of multiple tweets, which make up the dialogue chronologically:

<first tweet ID> \t <second tweet ID> \t <third tweet ID> \t ...

The tweet IDs can be used together with the Twitter API to create a dataset similar to the dataset used by Serban et al. (2016a) and Serban et al. (2016b).

### Benchmarking

It is not possible to reproduce the exact results in the literature due to differences in the generation process (including missing tweets, preprocessing steps etc.) and differences in the training procedure (model hyperparameter, hardware issues etc.). For benchmarking against the previous results, it is therefore strongly recommended that the LSTM, HRED and VHRED models be retrained and retested on the same corpus. 

Source code for baseline models is available here:

https://github.com/julianser/hed-dlg-truncated

However, for reference we provide the generated responses on the test sets for the LSTM, HRED, VHRED and MrRNN models.

### Notes

The MrRNN described by Serban et al. (2016b) were early stopped on a subset of the validation set (TweetIDs_Valid_Small.txt). All other models were early stopped on the full validation set.

### References

Unsupervised modeling of twitter conversations. Alan Ritter, Colin Cherry and Bill Dolan. 2010. NAACL, pages 172–180.

A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialoguesm. Iulian Vlad Serban, Alessandro Sordoni, Ryan Lowe, Laurent Charlin, Joelle Pineau, Aaron C. Courville and Yoshua Bengio. 2016a. http://arxiv.org/abs/1605.06069

Multiresolution Recurrent Neural Networks: An Application to Dialogue Response Generation. Iulian Vlad Serban, Tim Klinger, Gerald Tesauro, Kartik Talamadupula, Bowen Zhou, Yoshua Bengio, Aaron Courville. 2016b. http://arxiv.org/abs/1606.00776

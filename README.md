# NLP Final Project

## Project: Twiter Analyzer

## Wirter: Mengchen Fan & Zhengzhi Tan


  unsupervised: 

  In train model and preprocessing:
  
    - remove @xxx #xxx url and empty 
    
    - fine tuning elmo and get vectors
    
    - save vector 
    
  In cluster:
  
    - 1 First attempt:
    
      use kmean to cluster 
      
      or reduce dimension the cluster
      
    - 2 Second attempt:
    
      use classifers to classify data
      
    - 3 Third attempt:
    
      create two centers using all vectors
      
      calucuate distances with to center as polarity score

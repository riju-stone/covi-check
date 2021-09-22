## CoviCheck
A simple model to predict whether an individual is COVID-19 infected or not, given certain health parameters!

## Inspiration
All three of us are novices in the field of machine learning, and this being our first hackathon, we decided to take this opportunity to delve into its fascinating depths. We came up with the idea of creating a machine learning model shortly after the opening ceremony of HopHacks, while chatting in our Discord channel about the possible projects. 


## What it does
This is a very basic supervised machine learning model to predict whether an individual is infected with COVID-19 or not, given certain health parameters. It makes use of logistic regression to decide whether the person under observation is infected.


## How we built it
Having come up with a plausible idea, we debated over the algorithms that we should be using. Logistic regression is chosen unanimously, as the problem is a two-class classification problem. 
Next, we scoured the internet for a dataset and ended up with an appropriate one from Kaggle: [link]( https://www.kaggle.com/hemanthhari/symptoms-and-covid-presence)
One of us took up the responsibility to build the front-end, while the other two looked into the matter of building up the model. 
After completing the two separate parts, it’s time to integrate. We decided to use Flask to connect our model with the front-end, which has been made with dHTML. 


## Challenges we ran into
The first daunting task for us was to find an appropriate data-set. However, Kaggle saved us from much struggle, and we came across a pertinent data-set. 
Now, we looked into the making of the model. We had to split the data-set into training and testing sets, and trained our model. After encountering a few errors (including one about shape-mismatch), we could make our model give the expected outputs.  


## Accomplishments that we're proud of
We have never made a full-stack project in such a constrained time limit before. And we learned a lot while working with each other.


## What we learned
The best thing that we learnt is about working together in a team, complementing each other’s knowledge. Since this is our first hackathon together, we learnt a lot about how it is like participating in one. 


## What's next for CoviCheck
CoviCheck could be beneficial for decision making if there is a shortage of vaccine supplies, and medical professionals have to take a quick decision about who should be vaccinated on priority. This application could also be extended to generate a real-time heat map about the location of possibly infected people, hence helping the local authorities on taking decisions such as increasing the vaccine supplies, declaring a locality a containment zone, etc. 

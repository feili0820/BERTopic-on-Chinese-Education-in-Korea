# BERTopic on Chinese Language Education in South Korea
## Abstract
After a long-time intricate process of development, Chinese education in South Korea has gradually reached a new boom time in recent decades with the emergence of numerous private foreign language institutions. In order to fully understand the reasons and motivations behind this boom, this paper collected more than 10,000 pieces of Q&A records on Chinese learning and private language training institutions that have appeared on the NAVER knowledge-IN platform over the past decade, and presented an empirical study through a new topic classification model called "BERTopic" based on those data. After analyzing the difference in topics between the local and imported private educational institutions, this paper found that although the overall demand for Chinese language learning in Korean society was increasing, the difference in demand between different groups was also very obvious. Therefore, in order to achieve sustainable development of Chinese education in South Korea, the basic concept of “localizing development” should be taken into account.

## Experiment & Result
### Overview of the "BERTopic" workflow
![BERTopic Process](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/plots/bertopic%20process.png "BERTopic Process")
[BERTOPIC by Maarten Grootendorst](https://github.com/MaartenGr/BERTopic "For more details, click here.")

### Data preparation
* By using the double-restricted search method of “keyword  + catalogue index “ with the specific time range from 2011.01.01 to 2021.04.01, URLs of these targeted Q&A data are searched and collected on the "NAVER Knowledge-in" platform automatically;
* With URLs of total 10708 targets, the necessary information(including "title", "question description", "answer description", "question time", "cumulative page views", etc.) can be further extracted or summarized from the internet;
* The next step is to clean and reorganize all the texts. The specific cleaning process includes: deleting informal characters, spelling check on Korean expressions , merging valid paragraphs, and so on.
* Clean and reorganize all the text data parts. The specific cleaning process includes: deleting informal language characters, spelling and proofreading for Korean parts, merging valid paragraphs, and so on. 
* Finally, the cleaned data are resaved as a suitable dataset for model training, of which the individual text is separately documented with specific indexes based on “keyword(the name of private language training institutions)”.
</br>

Keyword|Numbers of questions|Numbers of page views|Category of Origin
:---:|:---:|:---:|:---:
Sisa (시사)|1408|1420551|Korean
Moon-Jeonga(문정아)|1798|1339087|Korean
Caihong(차이홍)|1575|1272821|Sino-Korean
HakSeupji(학습지)|2050|1222846|Korean
Hackers(해커스)|1765|1033599|Korean
Confucius Institute(공자학원/공자 아카데미) |673|537608|Sino-Korean
Pagoda(파고다)|506|453905|Korean
SiwonSchool(시원스쿨)|439|358808|Korean
YBM|268|315248|Korean
Gumon(구몬)|226|184430|Korean

### model training
*	__Two branches__：
    * Topic modelling for the whole dataset: a total of 10708(without the distinctions for keywords) are put into the “BERTopic” model for automatic topic classification.
    * Topic modelling for several sub-datasets: data with 4 representative keywords are extracted separately as 4 sub-datasets and are put into the “BERTopic” model one by one for automatic topic classification.
*	__Three steps__：
    * Parameter Tuning: Adjusting the local parameters used in training the topic models, including: Pre-trained language model for text embedding, topic merging method, minimum of topic size and range of representative keywords, etc.
    * Visualization: Mapping the trained topic models into the binary space to facilitate the further classifications and explanations with human subjective judgment.
    * Keywords extraction: after the training of the model, filtering out 15 most significantly related keywords of each subdivided topic and listing them for the follow-up analysis.
</br>

Stages|Main Functions|Key Parameters|values
:---:|:---:|:---:|:---:
Parameters setout|BERTopic() & fit_transform()|embedding_model|"distiluse-base-multilingual-cased-v1" 
Parameters setout| |nr_topics|"auto"
Parameters setout| |top_n_words|15
Parameters setout| |min_topic_size|50(total)/20(seperate)
Parameters setout| |n_gram_range|(1,1)
2 Topics Visualization|visualize_topics() & visualize_topics_over_time|top_n|numbers of all topics
2 Topics Visualization| |topics|depending on needs
3 keywords Extraction|get_topic_info() & get_topics()| 	　	

### visualization of results
* __topics of Total__ <br> <br>
![Total](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/total.PNG "Total") <br>
* __topics of Hackers__ <br> <br>
![Hackers](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/hackers.PNG "Hackers") <br>
* __topics of Moon-Jeonga__ <br> <br>
![Munza](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/munza.PNG "Munza") 
* __topics of Caihong__ <br> <br>
![Caihong](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/caihong.PNG "Caihong")
* __topics of Confucius Institute__ <br> <br>
![Kongzi](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/kongzi.PNG "Kongzi")
* __topics of Sisa__ <br> <br>
![Sisa](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/sisa.PNG "Sisa")
* __topics of HakSeupji__ <br> <br>
![Haksp](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/haksp.PNG "Haksp")
* __topics over time__ <br> <br>
![Topics Over Time](https://github.com/feili0820/BERTopic-on-Chinese-Education-in-Korea/blob/main/pictures/topics%20over%20time.PNG "Topics Over Time")
For more details, to see the plot list below. <br>

plot name|type|link
:---:|:---:|:---:
total(original)|"html"|[Total](./plots/SenMa_all.html "to Total")
Hackers(original)|"html"|[Hackers](./plots/figa_Hackers.html "Hackers")
Munza(original)|"html"|[Munza](./plots/figa_Munza.html "Munza")
Caihong(original)|"html"|[Caihong](./plots/figa_caihong.html "Caihong")
Kongzi(original)|"html"|[Kongzi](.plots/figa_kongzi.html "Kongzi")
Sisa(original)|"html"|[Sisa](./plots/figa_sisa.html "Sisa")
Haksp(original)|"html"|[Haksp](./plots/figa_Haksp.html "Haksp")

## Citation
Peng W. & Li F., (2021). A Practical Text-Mining Research on Representative Institutions of Chinese Education in South Korea with Naver Knowledge-in Q&A data Based on BERTopic.


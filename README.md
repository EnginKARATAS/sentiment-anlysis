# Twitter Data Analysis
1. Introduction
## This study aims to analyze and visualize sentiment analysis on two topic using the Twitter API
### Before/After of the Ukraine conflict emotion differentiation
### Emotional differences on Tweets using the Dollar exchange rate in the Turkish economy.

## 2. Methodology
### 2.1. Data collecting
Python programming language and Pandas library were used to perform sentiment analysis on tweets obtained using the Twitter API.

### 2.2. Using Secure Shell (SSH) and CURL
Tools such as SSH and CURL were used for data extraction. These operations were carried out in order to manage requests to the Twitter API and ensure secure communication.

### 2.3. Elastic Search and Kibana
Elastic Search and Kibana were used for data storage and visualization. These tools were chosen to analyze Twitter data and create various visualizations.

## 3. Elastic Search Operations
### 3.1. Adding Data
The PUT command was used to add data to Elastic Search. For example:


`
PUT dollar/_doc/1000
{
   "account_number": 1000,
   "balance": 65536,
   "firstname": "Engin",
   "lastname": "Karatas",
   "age": 23
}
`

### 3.2. Reading Process
Python ElasticSearch-Py library was used for search operations. Match_All property was used to fetch all data.


`
GET ukraine_crisis_topic/_search
{
   "query": {
     "match_all": {}
   }
}
`
### 3.3. Deletion Process
DELETE command was used for deletions. For example:


`
DELETE dollar/_doc/1
`

### 3.4. Update Process
Update operations are based on finding a specific record and replacing it with new data.

## 4. Index Export CSV Transaction
The index created on Elastic Search can be exported in CSV format with all its data. This process is accomplished by creating reports.

### 4.1. Creating a Report for Export Transaction
A relevant report must be created for the index export process. This is done in Analytics > Discover.

### 4.2. Report Viewing and Downloading Process
The generated reports are displayed and can be downloaded in Stack Management > Alerts and Insights > Reporting.

## 5. Monitoring, Analytics and Visualization via Kibana
For monitoring, analytics and visualization operations via Kibana, the relevant indexes must be defined as data views.

## 6. Sentiment Analysis and Visualization
Sentiment analysis was carried out on the obtained tweets. Tweets, which were converted into text items using the Python programming language, were divided into positive, negative and neutral categories. These analysis results are interpreted with various visualizations.

### 6.1. Visualization Models
Number of Records by Location
Total Number of Tweets
Positive and Negative Tweet Rates and Numbers
Average Mood
Sentiment Analysis by Countries and Locations
Location, Author, Messages According to Density Values
Scatter Plot of Density Values
Locations with the Highest Number of Followers
These visual models are created through Elastic Search and Kibana. Tweet data recorded on the graphs were examined simultaneously.

### 6.2. Ukraine War Analysis Results
In the examinations carried out between 3-4-5 May, 10-11-12 May, 17 June:

It has been observed that Turkey shares little about the Ukraine-Russia war.
More negative tweets were found in England and Spain than in other countries.
A serious density of tweets has been detected in all parts of Europe and especially in the UK.
In the African continent, especially in Togo, a high density of tweets was observed.
7. Extra Work
Extra studies carried out during the thesis study, other than the expected topics:

Elastic Search installation was done manually on the Linux system outside of elastic.co.
Jupyter Notebook was installed to test Python codes on Linux Server.
Different Elastic Search versions and migrations were made.
Dozens of errors encountered have been resolved and documented.
## 8. Results
Tweets were obtained by topic using Twitter's open source API.
According to the sentiment analysis results, various graphs were created and visualizations were made via Kibana.
The data obtained with Elastic Search and Kibana were examined on the world map and various analysis results were obtained.
## 9. Resources
### [1] “Number of Twitter users worldwide from 2019 to 2024,” statista.com/statistics/303681/twitter-users-worldwide/. (Accessed: 1 January 2022)

[2] "Pandas," en.wikipedia.org/wiki/Pandas. (Accessed: 17 June 2022)

[3] “Secure Shell (SSH),” en.wikipedia.org/wiki/G%C3%BCvenli_shell. (Accessed: 2 January 2022)

[4] “Secure Shell,” en.wikipedia.org/wiki/Secure_Shell. (Accessed: 20 January 2022)

[5] “Twitter Developer Documentation,” developer.twitter.com/en/docs.

[6] "Curl," tr.wikipedia.org/wiki/CURL. (Accessed: 17 June 2022)

[7] “Twitter Ads API - Accounts,” developer.twitter.com/en/docs/twitter-ads-api/campaign-management/api-reference/accounts. (Accessed: 20 January 2022)

[8] “Run Elasticsearch API requests,” elastic.co/guide/en/kibana/8.2/console-kibana.html#console-kibana. (Accessed: 17 June 2022)

[9] “Elasticsearch Geo-point,” elastic.co/guide/en/elasticsearch/reference/current/geo-point.html. (Accessed: 13 June 2022)

[10] “Execute CRUD Operations in Elasticsearch,” acloudguru.com/hands-on-labs/execute-crud-operations-in-elasticsearch. (Accessed: 13 June 2022)

[11] “Russia-Ukraine war: What happened today (June 17),” npr.org/2022/06/17/1105671092/russia-ukraine-war-what-happened-today-june-17. (Accessed: 18 June 2022)

[12] "U.S. House passes $40 billion Ukraine aid package; Ukraine economy predicted to contract 30%," cnbc.com/2022/05/10/russia-ukraine-live-updates.html.

[13] “NPR,” May 11, 2022, npr.org/2022/05/11/1098305702/russia-ukraine-war-what-happened-today-may-11.

[14] “NPR,” May 12, 2022, npr.org/2022/05/12/1098467785/russia-ukraine-war-what-happened-today-may-12.

[15] “NPR,” May 3, 2022, npr.org/2022/05/03/1096122593/russia-ukraine-war-what-happened-today-may-3.

[16] “NPR,” May 4, 2022, npr.org/2022/05/04/1096606111/russia-ukraine-war-what-happened-today-may-4.

[17] "Latitude and Longitude - Mapbox Docs," docs.mapbox.com/help/glossary/lat-lon/#:~:text=Latitude%20and%20longitude%20are%20a,180%20to%20180%20for% 20longitude. (Accessed: 13 June 2022)

[18] M. Bajer, “Building an IoT Data

Traffic Optimization with AWS IoT and Machine Learning
======================================================

Overview
--------

This project aims to optimize urban traffic flow by leveraging simulated IoT
data from traffic lights, vehicles, and environmental sensors. The system
collects real-time data using AWS IoT Core, performs analysis, and makes
predictions on traffic congestion and pollution using Amazon SageMaker. The
project provides actionable insights for optimal traffic signal adjustments,
focusing on sustainable urban planning.

Project Structure
-----------------

-   **src/**: Source code for training and deployment.

    -   **simulate-traffic-data.py**: Script for simulating IoT data for traffic
        lights and send it to AWS IoT Core.

    -   **lambda_function.py**: This file includes the complete Lambda function
        code along with explanations, making it easy to understand each part of
        the function.

    -   **train.py**: Script for training the model, saving it, and uploading it
        to S3.

    -   **athena_queries.sql**: This file contains all the necessary SQL queries
        to set up the database, create the table, and run analyses on the
        processed traffic data in S3.

    -   **inference.py**: Script for loading the model and making predictions at
        the SageMaker endpoint.

-   **requirements.txt**: Dependencies required to run the project.

Features
--------

-   **Data Collection**: Simulates IoT data for traffic conditions and
    environmental factors.

-   **Data Processing**: Real-time data processing using AWS Lambda and Kinesis.

-   **Predictive Modeling**: Model training using Amazon SageMaker to predict
    congestion and suggest traffic light timing adjustments.

-   **Real-Time Deployment**: Model deployment as a real-time SageMaker
    endpoint.

AWS Services Used
-----------------

-   **Amazon S3**: Storage for raw and processed data.

-   **AWS IoT Core**: Real-time streaming of IoT data.

-   **Amazon Kinesis**: Stream data processing.

-   **AWS Lambda**: Processes data in real-time.

-   **Amazon Athena:** Query data stored in S3 using SQL.

-   **Amazon SageMaker**: Model training and deployment as an endpoint.

Getting Started
---------------

### Prerequisites

-   An AWS account with permissions for SageMaker, IoT, Kinesis, Lambda, and S3.

-   Python 3.7 or higher.

-   Required packages listed in `requirements.txt`.

### Installation

1.  **Clone the repository**:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    bashCopy codegit clone https://github.com/dankends/traffic-optimization-AWS.git
    cd traffic-optimization-AWS
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.  **Install dependencies**:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    bashCopy codepip install -r requirements.txt
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.  **Set up AWS credentials** using the AWS CLI:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    bashCopy codeaws configure
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Running the Project

1.  **Simulate IoT Data**:

    -   Use the IoT data simulation script in `src/simulate-traffic-data.py` to
        send data to AWS IoT Core.

2.  **Data Processing with AWS Kinesis**

    -   AWS Kinesis Data Streams is used to collect and temporarily store
        real-time data from IoT devices. This enables us to continuously ingest
        high-velocity data and make it available for processing with AWS Lambda.

3.  **AWS Lambda**:

    -   AWS Lambda processes data from Kinesis in real-time. Each time new data
        arrives in the Kinesis stream, Lambda is triggered to perform tasks such
        as calculating additional metrics, flags high traffic levels, or
        processes CO2 levels. After processing, Lambda saves the transformed
        data to S3 for further analysis or model training. Use the script in
        `src/lambda_function.py` for help.

4.  **AWS Athena**:

    -   Enables SQL-based analysis on S3 data, perfect for quickly gaining
        insights from traffic metrics. With Athena, you can explore data
        patterns, such as average CO2 levels and high-traffic zones, directly
        from S3.

    -   Setup: Use `src/athena_queries.sql` to create a database and table in
        Athena. Run the provided queries to analyze traffic data stored in S3,
        extracting key insights like average vehicle speeds and congestion
        frequencies.

5.  **Train and Deploy the Model**:

    -   Use the `src/Traffic Data Predictor.ipynb` Jupyter notebook to train the
        model and save it to S3.

    -   Deploy the model to SageMaker using the instructions in the notebook.

6.  **Test the SageMaker Endpoint**:

    -   Run test data through the endpoint to get real-time predictions. You can
        use the`src/Endpoint.ipynb` to deploying your trained model as a
        real-time endpoint in Amazon SageMaker involves a few key steps. Here's
        a step-by-step guide:

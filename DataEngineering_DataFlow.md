# Overview

SERVERLESS DATA ANALYSIS with Dataflow

In this lab series, you learn how to load data into BigQuery and run complex queries. Next, you will execute a Dataflow pipeline that can carry out Map and Reduce operations, use side inputs and stream into BigQuery.

Objectives
In these labs you will perform the following tasks:

  * [Lab 1: A Simple Dataflow Pipeline (Python)](#lab1)
    * [Open Dataflow project](#lab1_1)
    * [Open Dataflow](#lab1_2)
    * [Pipeline filtering](#lab1_3)
    * [Execute the pipeline locally](#lab1_4)
    * [Execute the pipeline cloud](#lab1_5)
  * [Lab 2: MapReduce in Dataflow (Python)](#lab2)
    * [Identify Map and Reduce operations](#lab2_1)
    * [Execute the pipeline](#lab2_2)
    * [Use command line parameters](#lab2_3)
  * [Lab 3: Side Inputs (Python)](#lab3)
    * [Preparation](#lab3_1)
    * [Try using BigQuery](#lab3_2)
    * [Explore the pipeline](#lab3_3)
    * [Execute the pipeline](#lab3_4)


Note your lab credentials. You will use them to sign in to Cloud Platform Console.

Click Open Google Console.

Click Use another account if displayed.

Launch Google Cloud Shell Code Editor
Use the Google Cloud Shell Code Editor to easily create and edit directories and files in the Cloud Shell instance.

Once you activate the Google Cloud Shell , click the Launch the code editor button (looks like a pencil) to open the the Cloud Shell Code Editor.



The Launch the code editor button may be off screen to the right. You may need to click the Products & service button to close the menu to see the buttons.



You now have three interfaces available: 1) The Cloud Shell Code Editor, 2) the Cloud Shell Command Line, and 3) (By clicking on the tab) the Console. You can switch back and forth between the Console and Cloud Shell by clicking on the tab.



# <a name="lab1"></a> Lab 1: A Simple Dataflow Pipeline

In this lab, you learn how to write a simple Dataflow pipeline and run it both locally and on the cloud.

Setup a Python Dataflow project using Apache Beam
Write a simple pipeline in Python
Execute the query on the local machine
Execute the query on the cloud

## <a name="lab1_1"></a> Task 1. Preparation
For this lab you will need the training-data-analyst files and a Cloud Storage bucket.

Verify that the repository files are in Cloud Shell
Verify that the repository exists, and if not, clone it. Return to the browser tab containing the Cloud Shell code editor. Click on File > Refresh in the left navigator panel. You should see the training-data-analyst directory.
If the directory does not exist clone the repository from the Cloud Shell command line:

```
cd ~
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

Verify that you have a Cloud Storage bucket
You should have a bucket from the previous lab. If you don't you can follow these instructions to create a bucket.

In the Console, on the Products & services menu () click Home
Select and copy the Project ID. For simplicity you will use the Qwiklabs Project ID, which is already globally unique, as the bucket name.
In the Console, on the Products & services menu () click Storage > Browser.
Click Create Bucket.
Specify the following, and leave the remaining settings as their defaults:

|-----------|--------------------------------------------|
| Property  |                                            |
| Value     | (type value or select option as specified) |
| Name      | <your unique bucket name (Project ID)>     |
| Default storage class | [x] Regional                   |
| Multi-Regional location | <Your location>              |

Click Create.
Record the name of your bucket. You will need it in subsequent tasks.
In Cloud Shell enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command.
```
BUCKET="<your unique bucket name (Project ID)>"
echo $BUCKET
```

You can use $BUCKET in Cloud Shell commands. And if you need to enter the bucket name <your-bucket> in a text field in Console, you can quickly retrieve the name with "echo $BUCKET".

Verify that Google Cloud Dataflow API is enabled for this project
Return to the browser tab for Console. In the top search bar, enter Google Dataflow API. This will take you to the page, Products & Services > APIs & Services > Dashboard > Google Dataflow API. It will either show a status information or it will give you the option to Enable the API.
If necessary, Enable the API.


## <a name="lab1_2"></a> Task 2. Open Dataflow project

The goal of this lab is to become familiar with the structure of a Dataflow project and learn how to execute a Dataflow pipeline. You will need to update some files to install Apache Beam. Apache Beam is an open source platform for executing data processing workflows.

Return to the browser tab containing Cloud Shell. In Cloud Shell navigate to the directory for this lab:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```
Install the necessary dependencies for Python dataflow:
```
sudo ./install_packages.sh
```
Verify that you have the right version of pip. (It should be > 8.0):
```
pip -V
```
If not, open a new Cloud Shell tab and it should pick up the updated version of pip.

Use File > Refresh in Cloud Shell editor to view the local copy of the repository.
If at any time during the DataFlow labs you are logged out of Cloud Shell due to inactivity, when you login the in-memory elements of Apache Beam will be lost. So you will need to reissue these commands before proceeding:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
sudo ./install_packages.sh
```


## <a name="lab1_3"></a> Task 3. Pipeline filtering

In the Cloud Shell code editor navigate to the directory /training-data-analyst/courses/data_analysis/lab2/python and view the file grep.py Do not make any changes to the code.
Alternatively, you could view the file with nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano grep.py
```
Can you answer these questions about the file grep.py?

  - What files are being read?
  - What is the search term?
  - Where does the output go?

There are three transforms in the pipeline:

  - What does the transform do?
  - What does the second transform do?
  - Where does its input come from?
  - What does it do with this input?
  - What does it write to its output?
  - Where does the output go to?
  - What does the third transform do?


## <a name="label1_4"></a> Task 4. Execute the pipeline locally

In the Cloud Shell command line, locally execute grep.py
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
python grep.py
```
Note: if you see an error that says "No handlers could be found for logger "oauth2client.contrib.multistore_file", you may ignore it. The error is simply saying that logging from the oauth2 library will go to stderr.

The output file will be output.txt. If the output is large enough, it will be sharded into separate parts with names like: output-00000-of-00001. If necessary, you can locate the correct file by examining the file's time.
```
ls -al /tmp
```

Examine the output file. Replace "-\*" below with the appropriate suffix.
```
cat /tmp/output-*
```
Does the output seem logical?

## <a name="lab1_5"></a> Task 5. Execute the pipeline on the cloud

Copy some Java files to the cloud.
```
gsutil cp ../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/*.java gs://$BUCKET/javahelp
```
Edit the Dataflow pipeline in grepc.py. In the Cloud Shell code editor navigate to the directory /training-data-analyst/courses/data_analysis/lab2/python in and edit the file grepc.py
Replace PROJECT and BUCKET with your Project ID and Bucket name. Here are easy ways to retrieve the values:
echo $DEVSHELL_PROJECT_ID
echo $BUCKET
Example strings before:
```
PROJECT='cloud-training-demos'
BUCKET='cloud-training-demos'
```

Example strings after edit (use your values):
```
PROJECT='qwiklabs-gcp-your-value'
BUCKET='qwiklabs-gcp-your-value'
```

Submit the Dataflow job to the cloud:
```
python grepc.py
```
Because this is such a small job, running on the cloud will take significantly longer than running it locally (on the order of 2-3 minutes).

Return to the browser tab for Console. On the Products & services menu () click Dataflow and click on your job to monitor progress.
Example:

Wait for the job status to turn to Succeeded. At this point, your Cloud Shell will display a command-line prompt.
Examine the output in the Cloud Storage bucket. On the Products & services menu () click Storage > Browser and click on your bucket. Click the javahelp directory. This job will generate the file output.txt. If the file is large enough it will be sharded into multiple parts with names like: output-0000x-of-000y. You can identify the most recent file by name or by the Last modified field. Click on the file to view it.
Alternatively, you could download the file in Cloud Shell and view it:
```
gsutil cp gs://$BUCKET/javahelp/output.txt .
cat output.txt
```

# <a name="lab2"></a> Lab 2: MapReduce in Dataflow

## <a name="lab2_1"></a> Task 1. Review Preparations
These preparations should already be have been done:

Create Cloud Storage bucket
Clone github repository to Cloud Shell
Upgrade packages and install Apache Beam


## <a name="lab2_2"></a> Task 2. Identify Map and Reduce operations
In the Cloud Shell code editor navigate to the directory /training-data-analyst/courses/data_analysis/lab2/python and view the file is_popular.py Do not make any changes to the code.
Alternatively, you could view the file with nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano is_popular.py
```

Can you answer these questions about the file is_popular.py?
  - What custom arguments are defined?
  - What is the default output prefix?
  - How is the variable output_prefix in main() set?
  - How are the pipeline arguments such as --runner set?
  - What are the key steps in the pipeline?
  - Which of these steps happen in parallel?
  - Which of these steps are aggregations?

## <a name="lab2_3"></a> Task 3. Execute the pipeline

Run the pipeline locally:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
./is_popular.py
```

Note: if you see an error that says "No handlers could be found for logger "oauth2client.contrib.multistore_file", you may ignore it. The error is simply saying that logging from the oauth2 library will go to stderr.

Identify the output file. It should be output<suffix> and could be a sharded file.
```
ls -al /tmp
```

Examine the output file, replacing '-\*' with the appropriate suffix.
```
cat /tmp/output-*
```

## <a name="lab2_4"></a> Task 4. Use command line parameters

Change the output prefix from the default value:
```
./is_popular.py --output_prefix=/tmp/myoutput
```

What will be the name of the new file that is written out?
Note that we now have a new file in the /tmp directory:
```
ls -lrt /tmp/myoutput*
```

# <a name="lab3"></a> Lab 3: Side Inputs

In this lab, you learn how to use BigQuery as a data source into Dataflow, and how to use the results of a pipeline as a side input to another pipeline.

Read data from BigQuery into Dataflow
Use the output of a pipeline as a side-input to another pipeline

## <a name="lab3_1"></a> Task 1. Preparation
For this lab you will need the training-data-analyst files.

Verify that the repository files are in Cloud Shell
Verify that the repository exists, and if not, clone it. Return to the browser tab containing the Cloud Shell code editor. Click on File > Refresh in the left navigator panel. You should see the training-data-analyst directory.
If the directory does not exist clone the repository from the Cloud Shell command line:

```
cd ~
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

Verify that you have a Cloud Storage bucket
You should have a bucket from the previous lab and an environment variable containing the bucket name.

```
echo $BUCKET
```

If you don't have a bucket, you can follow these instructions to create a bucket.

In the Console, on the Products & services menu () click Home
Select and copy the Project ID. For simplicity you will use the Qwiklabs Project ID, which is already globally unique, as the bucket name.
In the Console, on the Products & services menu () click Storage > Browser.
Click Create Bucket.
Specify the following, and leave the remaining settings as their defaults:

|------------------|------------------------|
| Property         |                        |
| Value            | (type value or select option as specified) |
| Name             | <your unique bucket name (Project ID)> |
| Default storage class | [x] Regional |
| Multi-Regional location | <Your location> |
|-------------------------|------------------|

Click Create.
Record the name of your bucket. You will need it in subsequent tasks.
In Cloud Shell enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command.

```
BUCKET="<your unique bucket name (Project ID)>"
echo $BUCKET
```

You can use $BUCKET in Cloud Shell commands. And if you need to enter the bucket name <your-bucket> in a text field in Console, you can quickly retrieve the name with "echo $BUCKET".

Verify environment variable for your Project ID
Cloud Shell creates a default environment variable that contains the current Project ID.
```
echo $DEVSHELL_PROJECT_ID
```

Verify that Google Cloud Dataflow API is enabled for this project
Return to the browser tab for Console. In the top search bar, enter Google Dataflow API. This will take you to the page, Products & Services > APIs & Services > Dashboard > Google Dataflow API. It will either show a status information or it will give you the option to Enable the API.
If necessary, Enable the API.
Verify that Apache Beam is installed on Cloud Shell
Return to Cloud Shell. Verify that Apache Beam is installed on Cloud Shell. If the Cloud Shell has timed out and was reconnected, it may have lost the in-memory components of Apache Beam. There is no harm in reinstalling. It will take the necessary steps.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
sudo ./install_packages.sh
```

## <a name="lab3_2"></a> Task 2. Try using BigQuery query

Return to the BigQuery web UI. If it is not already open, open Console. On the Products & services menu () click BigQuery.
Compose a new query:
```
SELECT
  content
FROM
  [fh-bigquery:github_extracts.contents_java_2016]
LIMIT
  10
```

Before running the query, click on Show Options. Verify that Use Legacy SQL is checked. The click on Hide Options.
Click on Run Query.
What is being returned?

The BigQuery table fh-bigquery:github_extracts.contents_java_2016 contains the content (and some metadata) of all the Java files present in github in 2016.

To find out how many Java files this table has, type the following query and click Run Query:
```
SELECT
  COUNT(*)
FROM
  [fh-bigquery:github_extracts.contents_java_2016]
```

The reason zero bytes are processed is that this is table metadata.

How many files are there in this dataset?

Is this a dataset you want to process locally or on the cloud?

## <a name="lab3_3"></a> Task 3. Explore the pipeline code
In Cloud Shell editor, or in Cloud Shell, navigate to the lab directory:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```

View the pipeline code using Cloud Shell editor or nano. Do not make any changes to the code.
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano JavaProjectsThatNeedHelp.py
```

Refer to this diagram as you read the code. The pipeline looks like this:



Answer the following questions:
  - Looking at the class documentation at the very top, what is the purpose of this pipeline?
  - Where does the content come from?
  - What does the left side of the pipeline do?
  - What does the right side of the pipeline do?
  - What does ToLines do? (Hint: look at the content field of the BigQuery result)
  - Why is the result of ReadFromBQ stored in a named PCollection instead of being directly passed to another step?
  - What are the two actions carried out on the PCollection generated from ReadFromBQ?
  - If a file has 3 FIXMEs and 2 TODOs in its content (on different lines), how many calls for help are associated with it?
  - If a file is in the package com.google.devtools.build, what are the packages that it is associated with?
popular_packages and help_packages are both named PCollections and both used in the Scores (side inputs) step of the pipeline. Which one is the main input and which is the side input?
  - What is the method used in the Scores step?
  - What Python data type is the side input converted into in the Scores step?

The Java version of this program is slightly different from the Python version. The Java SDK supports AsMap and the Python SDK doesn't. It supports AsDict instead. In Java, the PCollection is converted into a View as a preparatory step before it is used. In Python the PCollection conversion occurs in the step where it is used.

## <a name="lab3_4"></a> Task 4. Execute the pipeline
Change into the directory:
```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
```

The program requires BUCKET and PROJECT values and choosing whether to run the pipeline locally using --DirectRunner or on the cloud using --DataFlowRunner
Execute the pipeline locally by typing the following into Cloud Shell.
```
python JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $DEVSHELL_PROJECT_ID --DirectRunner
```

Once the pipeline has finished executing, On the Products & services menu () click Storage > Browser and click on your bucket. You will find the results in the javahelp folder. Click on the Result object to examine the output.
Execute the pipeline on the cloud by typing the following into Cloud Shell.
```
python JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $DEVSHELL_PROJECT_ID --DataFlowRunner
```

Return to the browser tab for Console. On the Products & services menu () click Dataflow and click on your job to monitor progress.
Once the pipeline has finished executing, On the Products & services menu () click Storage > Browser and click on your bucket. You will find the results in the javahelp folder. Click on the Result object to examine the output.
Completion
Cleanup

In the Cloud Platform Console, sign out of the Google account.
Close the browser tab.
Last Updated: 2018-04-04

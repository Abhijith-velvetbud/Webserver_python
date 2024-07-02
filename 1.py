"""
This code sample shows Prebuilt ID Document operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

# code 
from flask import Flask, request 
# flask name module 
app = Flask(__name__) 


from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://aravttechocr.cognitiveservices.azure.com/"
key = "fd0ae204c12b4c92a9db689b20ef55b5"

# sample document
formUrl = "https://5.imimg.com/data5/AN/EO/NC/ANDROID-33737889/product-jpeg-500x500.jpeg"

document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-idDocument", formUrl)
id_documents = poller.result()

for idx, id_document in enumerate(id_documents.documents):
    print("--------Recognizing ID document #{}--------".format(idx + 1))
    first_name = id_document.fields.get("FirstName")
    if first_name:
        print(
            "First Name: {} has confidence: {}".format(
                first_name.value, first_name.confidence
            )
        )
    last_name = id_document.fields.get("LastName")
    if last_name:
        print(
            "Last Name: {} has confidence: {}".format(
                last_name.value, last_name.confidence
            )
        )
    document_number = id_document.fields.get("DocumentNumber")
    if document_number:
        print(
            "Document Number: {} has confidence: {}".format(
                document_number.value, document_number.confidence
            )
        )
    dob = id_document.fields.get("DateOfBirth")
    if dob:
        print(
            "Date of Birth: {} has confidence: {}".format(dob.value, dob.confidence)
        )
    doe = id_document.fields.get("DateOfExpiration")
    if doe:
        print(
            "Date of Expiration: {} has confidence: {}".format(
                doe.value, doe.confidence
            )
        )
    sex = id_document.fields.get("Sex")
    if sex:
        print("Sex: {} has confidence: {}".format(sex.value, sex.confidence))
    address = id_document.fields.get("Address")
    if address:
        print(
            "Address: {} has confidence: {}".format(
                address.value, address.confidence
            )
        )
    country_region = id_document.fields.get("CountryRegion")
    if country_region:
        print(
            "Country/Region: {} has confidence: {}".format(
                country_region.value, country_region.confidence
            )
        )
    region = id_document.fields.get("Region")
    if region:
        print(
            "Region: {} has confidence: {}".format(region.value, region.confidence)
        )




# create routes for call query example 
@app.route('/pan_details') 
def query_example(): 
	request 
	return '''<h1> The First Name is : {} </h1> 
              <h1> The Second Name is : {} </h1>
              <h1> The Date of Birth is : {} </h1> 
              <h1> The Document Number is : {}  </h1>'''.format(first_name.value,  
                                                        last_name.value,
                                                        dob.value,  
                                                        document_number.value)

if __name__ == "__main__": 
	app.run(debug=True)

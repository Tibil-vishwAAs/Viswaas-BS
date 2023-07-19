package api_Test;


import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.AssertJUnit;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.AssertJUnit;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.testng.Assert;
import org.testng.asserts.SoftAssert;

import api_endpoints.certificate;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
public class CertificateApiTest {
    private File file;
    private FileReader fr;
    private JSONTokener jr;
    private JSONObject data;
    public Logger logger;

    @BeforeClass
    public void setup() throws IOException 
    {
    	 Properties properties = new Properties();
         properties.load(new FileReader("config.properties"));

         // Retrieve the JSON file path
         String jsonFilePath = properties.getProperty("jsonCertificateFilePath");
         
        file = new File(jsonFilePath);
        fr = new FileReader(file);
        jr = new JSONTokener(fr);
        data = new JSONObject(jr);
        
        //Logs
        logger = LogManager.getLogger(this.getClass());
        
    }
    @Test
    public void testCertificate() 
    {
    	logger.info("*********************** Testing Started **********************************");

    	logger.info("*********************** Creating the certificate using valid Endpoints **********************************");

    	SoftAssert softAssert = new SoftAssert();

    	String jsonData = data.toString();

    	Response response = certificate.Create_user(jsonData);
    	response.then().log().all();

    	// Validate the response status code
    	int statusCode = response.getStatusCode();
    	softAssert.assertEquals(statusCode, 200, "Correct status code");


    	JsonPath jsonPath = response.jsonPath();
        String responseBody = response.getBody().asString();
       


        // Validate headers
        String contentTypeHeader = response.getHeader("Content-Type");
        Assert.assertEquals(contentTypeHeader, "application/json", "Correct Content-Type header");

    	// Validate response time
    	long responseTime = response.getTime();
    	System.out.println("Response Time: " + responseTime);
    	softAssert.assertTrue(responseTime >= 0, "Response time should be in milliseconds. Actual: " + responseTime + "ms");

 	String osid = jsonPath.getString("result.vishwaastest.osid");
    	 // Perform further validations using the 'osid' value
        if (osid != null && !osid.isEmpty()) {
            // Perform actions using 'osid' as the certificate was created successfully
            System.out.println("Certificate created. OSID: " + osid);
        } else {
            // Handle the case when the certificate creation failed
            String status = jsonPath.getString("status");
            if ("Certificate already exists".equals(status)) {
                // Certificate already exists, handle this case accordingly
                System.out.println("Certificate already exists");
            } else {
                // Other error cases or unexpected response format
                System.out.println("Certificate creation failed. Status: " + status);
            }
        }
    	   


    	softAssert.assertAll();
    	logger.info("*********************** certificate is Created using valid Endpoints **********************************");
    	logger.info("*********************** Testing Ended **********************************");


	}
	@Test
	public void certificateApiUsingInvalidEndpoint() 
	{
    	logger.info("*********************** Testing Started **********************************");

    	logger.info("*********************** Creating the certificate using Invalid Endpoints **********************************");

        SoftAssert softAssert = new SoftAssert();

        String jsonData = data.toString();
        Response response = certificate.Create_User_using_invalidEndpoints(jsonData);
        response.then().log().all();
//
//        ResponseBody responseBody = response.getBody();
//        System.out.println("Response Body: " + responseBody);
//        Assert.assertNotNull(responseBody, "Response body is not null");

        // Validate the response status code
        System.out.println(response.getStatusCode());
        Assert.assertEquals(response.getStatusCode(), 404, "Not Found");
//        System.out.println(response.body());

        // Validate headers
        String contentTypeHeader = response.getHeader("Content-Type");
        Assert.assertEquals(contentTypeHeader, "application/json", "Correct Content-Type header");

        long responseTime = response.getTime();
        System.out.println("Response Time: " + responseTime);
        Assert.assertTrue(responseTime >= 0, "Response time should be in milliseconds. Actual: " + responseTime + "ms");

        softAssert.assertAll();
    	logger.info("*********************** certificate is Not Created **********************************");

    	logger.info("*********************** Testing Ended **********************************");

       
    }
	
	
	
	

}

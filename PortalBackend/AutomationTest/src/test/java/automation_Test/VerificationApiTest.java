package api_Test;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.AssertJUnit;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.Assert;
import org.testng.asserts.SoftAssert;

import api_endpoints.VerificationApi;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;

public class VerificationApiTest
{
    public String osid;
    public Logger logger;
	@BeforeClass
	public void setup() throws FileNotFoundException, IOException
	{

		Properties properties = new Properties();
        FileInputStream file = new FileInputStream("config.properties");
        properties.load(file);
        file.close();

        // Get the osid value from the properties file
        osid = properties.getProperty("osid");
        
        //Logs
        logger = LogManager.getLogger(this.getClass());
	}
	@Test
	public void testVerificationApi()
	{
		
	     logger.info("*********************** Testing Started **********************************");
	     logger.info("*********************** Verify the certificate using valid Endpoints **********************************");
	        SoftAssert softAssert = new SoftAssert();
	        Response response = VerificationApi.getVerification(osid);
	        response.then().log().all();

	        // Validate the status code
	        int statusCode = response.getStatusCode();
	        Assert.assertEquals(statusCode, 200, "Correct status code");

	        String contentTypeHeader = response.getContentType();
	        Assert.assertNotNull(contentTypeHeader, "Content-Type header is not null");
	        Assert.assertTrue(contentTypeHeader.contains("application/json"), "Correct Content-Type header");

	        // Validate the "verified" field in the response JSON
	        boolean verified = response.jsonPath().getBoolean("verified");
	        Assert.assertTrue(verified, "Verified field is true");

	        // Extract and validate specific fields from the response JSON
	        String proofPurpose = response.jsonPath().getString("results[0].proof.proofPurpose");
	        Assert.assertEquals(proofPurpose, "assertionMethod", "Correct proofPurpose");

	        boolean valid = response.jsonPath().getBoolean("results[0].purposeResult.valid");
	        Assert.assertTrue(valid, "Valid field is true");

	        // Validate response time
	        long responseTime = response.getTime();
	        System.out.println("Response Time: " + responseTime);
	        Assert.assertTrue(responseTime >= 0, "Response time should be in milliseconds. Actual: " + responseTime + "ms");

	        logger.info("*********************** certificate is verified using valid Endpoints **********************************");
	        logger.info("*********************** Testing Ended **********************************");

	        softAssert.assertAll();
	    }

	@Test
	public void verificationApiUsingInvalidEndpoint()
	{
		 logger.info("*********************** Testing Started **********************************");
	     logger.info("*********************** Verify the certificate using Invalid Endpoints **********************************");
		
		 SoftAssert softAssert = new SoftAssert();

	        Response response = VerificationApi.getVerificationUsingInvalidEndpoints(osid);
	        response.then().log().all();

	        // Validate the status code
	        int statusCode = response.getStatusCode();
	        System.out.println(statusCode);
	        Assert.assertEquals(statusCode, 404, "Correct status code");

	        String contentTypeHeader = response.getContentType();
	        Assert.assertNotNull(contentTypeHeader, "Content-Type header is not null");
	        Assert.assertTrue(contentTypeHeader.contains("application/json"), "Correct Content-Type header");

	        // Validate response time
	        long responseTime = response.getTime();
	        System.out.println("Response Time: " + responseTime);
	        Assert.assertTrue(responseTime >= 0, "Response time should be in milliseconds. Actual: " + responseTime + "ms");

	        JsonPath jsonPath = response.jsonPath();

	        String timestamp = jsonPath.getString("timestamp");
	        AssertJUnit.assertNotNull(timestamp, "Timestamp field is not null");

	        int status = jsonPath.getInt("status");
	        Assert.assertEquals(status, 404, "Correct status code");

	        String error = jsonPath.getString("error");
	        Assert.assertEquals(error, "Not Found", "Correct error message");

	        String message = jsonPath.getString("message");
	        Assert.assertEquals(message, "No message available", "Correct message");

	        String path = jsonPath.getString("path");
	        Assert.assertEquals(path, "/api/v1/Verificationn/1-cd3704aa-65f9-4b0d-8218-03aa9e8a7ea3", "Correct path");

	        // You can also print the response body for debugging
	        System.out.println("Response Body: " + response.getBody().asString());

	        softAssert.assertAll();

	        logger.info("*********************** verified the certificate using in valid Endpoints**********************************");
	        logger.info("*********************** Testing Ended **********************************");

		
		
	}
	
	
	
	

}

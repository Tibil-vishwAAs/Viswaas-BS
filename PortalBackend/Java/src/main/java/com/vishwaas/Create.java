package com.vishwaas;

import java.util.Collections;
import java.util.logging.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.client.RestTemplate;

@Component
public class Create {
	//Parameter used to create certificate
    @Value("${baseURL}")
    private String baseURL;

    @Value("${rc.port}")
    private String port;

    @Value("${rc.Entity}")
    private String entity;

    @Autowired
    private Token tokenTest;
   
    @Autowired
    private CertificateData certificateData;
    private static final Logger logger = Logger.getLogger(Create.class.getName());

   //Create certificate API has been Called 
    public ResponseEntity<String> createCertificate(@RequestBody CertificateData certificatedata) {
        try {
            String certificateUrl = baseURL + ":" + port + entity;
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            headers.setBearerAuth(tokenTest.getToken());
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            RestTemplate restTemplate = new RestTemplate();
            HttpEntity<CertificateData> requestEntity = new HttpEntity<>(certificatedata, headers);
            ResponseEntity<String> response = restTemplate.exchange(
                    certificateUrl,
                    HttpMethod.POST,
                    requestEntity,
                    String.class
            );              
            if (response.getStatusCode() == HttpStatus.OK) {           
                return new ResponseEntity<String>(response.getBody(),HttpStatus.OK);               		              
            } else if (response.getStatusCode() == HttpStatus.NOT_FOUND) {
                logger.severe("Failed to create certificate. Status code: " + response.getStatusCode());
            }
        } catch (Exception e) {       	
           logger.warning("An error occurred while creating certificate: " + e.getMessage());
        }		
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Failed to create certificate");
    }
}
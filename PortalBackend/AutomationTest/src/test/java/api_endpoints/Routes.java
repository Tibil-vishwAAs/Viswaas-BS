package api_endpoints;

public class Routes {

	public static String base_URI = "http://localhost:8090";
	
	public static String Certificate_url = base_URI+"/api/v1/Certificates";
	public static String Invalid_url = base_URI+"/api/v1/Certificates1";
	
	public static String Verification_url = base_URI+"/api/v1/Verification/{Osid}";
			
	
	public static String Verification_invalid_url = base_URI+"/api/v1/Verificationn/{Osid}";
	
	
	public static String delete_url = base_URI+"";
	
	public static String update_url = base_URI+"";

	
}

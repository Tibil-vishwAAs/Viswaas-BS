package api_utilities;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

public class Utility 
{
	public static String getPropertyFileData(String Key) throws IOException
	{
		FileInputStream file =new FileInputStream("/home/priti/eclipse-workspace/Sahamati_Project/src/test/resources/properties.property");
		Properties property = new Properties();
		property.load(file);
		String value = property.getProperty(Key);
		return value;
	}
}

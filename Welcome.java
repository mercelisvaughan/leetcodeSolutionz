import java.util.*;

/* Keys to this problem is to split the string, and then split it again, add the split strings to the dictionary
 *  as a key and value
 * 
 * {
  "BloodPressure": "120/80",
  "Oxygen": 98,
  "Temperature": 36.6,
  "HeartRate": 72 }
 * 
 */


public class Welcome {
    public static void main(String[] args)
    {
        // Create a hashmap to store key value pairs
        Map<String, String> healthData = new Hashtable<>();

        // Split the string by the commas using .split() method
        String s = "BP:120/80,O2:98,Temp:36.6,HR:72";
        String[] entries = s.split(",");
        // BP:120/80 turns into 120/80
        for (String entry : entries) {
            String[] keyValue = entry.split(":");

            // Check if the split actually worked and has two parts
            if (keyValue.length == 2) {
                String key = keyValue[0];
                String value = keyValue[1];

                switch (key) {
                    case "BP":
                        key = "BloodPressure";
                        break;
                    case "O2":
                        key = "Oxygen";
                        break;
                    case "Temp":
                        key = "Temperature";
                        break;
                    case "HR":
                        key = "HeartRate";
                        break;
                }
                healthData.put(key, value);
            }
        }

        for (Map.Entry<String, String> pair : healthData.entrySet()) {
            System.out.println(pair.getKey() + ": " + pair.getValue());
        }

        String testString = "SensorID=9871|Time=2025-06-06T13:45:00Z|HR=75|BP=118/79|Temp=36.7|O2=97";
    Welcome main = new Welcome();

    HashMap<String, String> result = main.senser_formatter(testString);

    for (Map.Entry<String, String> entry : result.entrySet()) {
        System.out.println(entry.getKey() + ": " + entry.getValue());
    }

    }

    /*
     * 
     * ✅ Your task:
     * Sample string -> "SensorID=9871|Time=2025-06-06T13:45:00Z|HR=75|BP=118/79|Temp=36.7|O2=97"
    Extract each key-value pair.
    Store them in a map with the following friendly names:
        SensorID → Sensor
        Time → Timestamp
        HR → HeartRate
        BP → BloodPressure
        Temp → Temperature
        O2 → Oxygen
    Output the map.
🧪 Sample Output (Java Map or JSON-style):
{
  "Sensor": "9871",
  "Timestamp": "2025-06-06T13:45:00Z",
  "HeartRate": "75",
  "BloodPressure": "118/79",
  "Temperature": "36.7",
  "Oxygen": "97"
}


     * 
     * Step 1: Create a HashMap to store key value pairs
     * Create String[] by splitting input_String, this way we can loop over a list which is an iterable, string is not an iterable
     * Now that we split the input string, we are going to loop through the list we create called split_input, it is the input split
     * Now we are going to create another array call key value, that will hold our key value pairs
     */


    public HashMap<String, String> senser_formatter(String input_String) {
        HashMap<String, String> hm = new HashMap<>();
        String[] split_input = input_String.split("\\|");

        for (String string : split_input){
            String[] keyValue = string.split("=");

            if (keyValue.length == 2) {
                String key = keyValue[0];
                String value = keyValue[1];

                switch (key) {
                    case "SensorID":
                        key = "Sensor";
                        break;
                    case "Time":
                        key = "Timestamp";
                        break;
                    case "HR":
                        key = "HeartRate";
                        break;
                    case "BP":
                        key = "BloodPressure";
                        break;
                    case "Temp":
                        key = "Temperature";
                        break;
                    case "O2":
                        key = "Oxygen";
                        break;
                }
                hm.put(key, value);
        }

    }
        return hm;
}
}


/*
 * 
 * This is what a unit test would look like for this problem
 * public class WelcomeTest {

    @Test
    public void senser_formatterTest(){
        //Given
        Welcome main = new Welcome();
        // When
        String actual = "SensorID=9871|Time=2025-06-06T13:45:00Z|HR=75|BP=118/79|Temp=36.7|O2=97";
        HashMap<String, String> expected = new HashMap<>();
        expected.put("Sensor", "9871");
        expected.put("Timestamp", "2025-06-06T13:45:00Z");
        expected.put("HeartRate", "75");
        expected.put("BloodPressure", "118/79");
        expected.put("Temperature", "36.7");
        expected.put("Oxygen", "97");

        Assert.assertEquals(expected, expected);
    }
    
}
 * This is what would go in your pom.xml
 * 
 * <dependencies>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>
 * 
 * 
 * This question was generated from ChatGPT I told it I had an interview in 5 days.
 * 
 */
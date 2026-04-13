import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import java.util.Scanner;

import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    
    static String APIKEY = "71f3719d99aa37db801d62f3c6c22045";
    
    public static void main(String[] args) throws Exception{
        latFromCity();
    }


    public static void latFromCity() throws java.io.IOException, InterruptedException {

        Scanner scanner = new Scanner(System.in);
        Path outlet = Paths.get("response.JSON");

        System.out.print("Please enter a city (leave blank to close): ");
        String city = scanner.nextLine();

        boolean path = true;

        while (!city.equals("")){
            
            String Url = String.format("http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=1&appid=%s", city, APIKEY);
            HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create( Url ))
            .GET()
            .build();
            
            HttpClient client = HttpClient.newHttpClient();
            HttpResponse.BodyHandler<String> asString = HttpResponse.BodyHandlers.ofString();
            HttpResponse.BodyHandler<Path> asJSON = HttpResponse.BodyHandlers.ofFile(outlet);
            
            HttpResponse<String> response = client.send(request, asString);
            HttpResponse<Path> jresponse = client.send(request, asJSON);
            
            //        int statusCode = response.statusCode();
            //        System.out.printf("Status Code: %s%n", statusCode);
            
            
            System.out.println(jresponse.body());

            String[] shrimp = response.body().split("[\\{\\}]");
            String[] krill = shrimp[3].split(",");
            String lat = krill[1].split(":")[1];
            String lon = krill[2].split(":")[1];
            
//            System.out.println(lat);
//            System.out.println(lon);

            Url = String.format("https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s", lat, lon, APIKEY);
            request = HttpRequest.newBuilder()
                .uri(URI.create( Url ))
                .GET()
                .build();

            if (path) {
                response = client.send(request, asString);
                String[] fish = response.body().split(",");
    
    
                for (String bone : fish) {
                    if (bone.contains("description") || bone.contains("temp\"")) {
                        System.out.println(bone);
                    }
                }
            } else {
                jresponse = client.send(request, asJSON);
            }


            System.out.print("Please enter a city (leave blank to close): ");
            city = scanner.nextLine();
        }

        scanner.close();
    }
}


// class weatherResponse {
//     String name = "";
//     String local_names = "";
//     int lat = 0;
//     int lon = 0;
//     String country = "";
//     String state = "";
// }
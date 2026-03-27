import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import java.util.Scanner;



public class Main {
    
    static String APIKEY = "71f3719d99aa37db801d62f3c6c22045";
    
    public static void main(String[] args) throws Exception{
        latFromCity();
    }


    public static void latFromCity() throws java.io.IOException, InterruptedException {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Please enter a city (leave blank to close): ");
        String city = scanner.nextLine();

        while (!city.equals("")){
            
            String Url = String.format("http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=1&appid=%s", city, APIKEY);
            HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create( Url ))
            .GET()
            .build();
            
            var client = HttpClient.newHttpClient();
            HttpResponse.BodyHandler<String> asString = HttpResponse.BodyHandlers.ofString();
            HttpResponse<String> response = client.send(request, asString);
            
            //        int statusCode = response.statusCode();
            //        System.out.printf("Status Code: %s%n", statusCode);
            

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

            response = client.send(request, asString);
            System.out.println(response.body());


            System.out.print("Please enter a city (leave blank to close): ");
            city = scanner.nextLine();
        }

        scanner.close();
    }
}

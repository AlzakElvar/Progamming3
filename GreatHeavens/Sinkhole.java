
import java.util.Scanner;

public class Sinkhole {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);

        //Prompt user for input:
        //      Type of graph -> A
        System.out.println("Please enter the kind of graph you want:");
        System.out.println("""
                LineGraph
                ScatterPlot
                PieChart
                Histogram
                """);
        String A = scan.nextLine();

        //          case statement to switch:
        //              XY or otherwise

        //Repeat until interrupt:
        //  Prompt user for input:
        String B = "ello";
        while (!B.equals(""))
        {
            B = scan.nextLine();
        }
        //          Manual or File
        //              Prompt for file - autoassign labels
        //              Prompt with lables - autograb data
        //          Prompt for data

    }
}

class Constructor
{
    String a;
    public Constructor(String A)
    {
        a = A;
    }

    public void build()
    {
        System.out.print(a);
        //Switch between:
        //      Line Graph
        //      Scatter Plot
        //      PieChart
        //      Histograms
    }
}

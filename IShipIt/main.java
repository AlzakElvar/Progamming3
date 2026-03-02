import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Player Person1 = new Player();

        System.out.print("\033[H\033[2J");
        System.out.flush();

        CustomerService cs = new CustomerService();
        int[] lengths = {5, 4, 3, 3, 2};
        for (int i = 0; i < lengths.length; i++){
            Ship temp = new Ship(cs.Place(lengths[i]));
            Person1.ships[i] = temp;
        }
        Person1.printShips();

    }
}

class Player {
    Ship[] ships = new Ship[5];

    public void printShips() {
        for(Ship ship : ships){
            System.out.print(ship.length + " ");
        }
    }
}

class Ship {
    
    String[] parts = null;
    int length = 0;

    public Ship(String[] pieces) {
        parts = pieces;
        length = pieces.length;
    }

    public boolean Sunk() {
        for (int i = 0; i < length; i++){
            if (parts[i] != "HIT") {
                return false;
            }
        }
        
        return true;
    }
}


class Grid {
    
    char[][] grid = new char[10][10];
    char[] key = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'
    };

    public Grid(){
       
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                grid[i][j] = '0';
            }
        }
    }
    
    public void printGrid() {
        
        System.out.print("   ");
        for (int i = 0; i < 10; i++){
            System.out.print(i + "  ");
        }
        System.out.print("\n ");
        for (int i = 0; i < 30; i++){
            System.out.print("-");
        }
        System.out.print("\n");
        for (int i = 0; i < grid.length; i++) {
            System.out.print(key[i] + "| ");
            for (char col : grid[i]) {

                System.out.print(col + "  ");

                //     System.out.print("0  ")
                //     System.out.print("O  ");
                //     System.out.print("X  ");
                //     System.out.print("█  ");        //3 means ship (unhit)
                //     System.out.print("[ ");        //4 means ship (hit)
                
            }
        System.out.print("\n");
        }
    }

    public int getRow(char arg) {
        
        int answer = -1;
        
        for (int i = 0; i < key.length; i++ ) {
            if (arg == key[i]) {
                answer = i;
            }
        }
        
        return answer;
    }


    // Will take a String of XA: where X is any letter between A - J and A is any number between 1 - 10
    /**
     * Will take a String of XA: where X is any letter between A - J and A is any number between 1 - 10 
     * @param args - the position in XA
     * 
     * @return 'O' or '[' or 'X'. Depending on Miss, Hit, or other
     */
    public char plink(String args) {
        char a = args.charAt(0);
        int b = Integer.parseInt( Character.toString(args.charAt(1)) );
        
        int c = getRow(a);
        
        char temp = grid[c][b];
        if (temp == '0') {
            return 'O';
        } 
        else if (temp == '█'){
            return '[';
        } 
        else {
            return 'X';
        }
    }

    public String[] Set(String pos, int len, int rot){
        char a = pos.charAt(0);
        int b = Integer.parseInt( Character.toString(pos.charAt(1)) );
        int c = getRow(a);

        String[] parts = new String[len];

        for (int i = 0; i < len; i++){
            if(rot == 0){
                if (grid[c + i][b] != '█'){
                    grid[c + i][b] = '█';
                    parts[i]  = "" + (c + i) + b;
                } 
                else {
                    return null;
                }
            }
            else {
                if (grid[c][b + i] != '█'){
                    grid[c][b + i] = '█';
                    parts[i]  = "" + c + (i + b);
                }
                else {
                    return null;
                }
            }
        }
        return parts;
    }
}

class CustomerService {
    
    Grid panel1 = new Grid();
    Grid plank1 = new Grid();
    
    Grid panel2 = new Grid();
    Grid plank2 = new Grid();
    Scanner scanner = new Scanner(System.in);
    
    
    public void Plink() {
        Scanner scanner = new Scanner(System.in);
        panel1.printGrid();

        System.out.print("Please plink: ");
        String plonk = scanner.nextLine();
        panel1.plink(plonk);

        panel1.printGrid();
        scanner.close();
    }

    public String[] Place(int len) {
        ClearScreen.Clear();

        plank1.printGrid();
        System.out.print("Please Choose a postion for the " + len + "-len ship: ");
        String place = scanner.nextLine();
        System.out.print("Please select a rotation(0 or 90): ");
        String rot = scanner.nextLine();
        String[] temp = plank1.Set(place, len, Integer.parseInt(rot));    
        
        plank1.printGrid();

        return temp;
    }
}

class ClearScreen{
    public static void Clear(){
            System.out.print("\033[H\033[2J");
            System.out.flush();
    }
}
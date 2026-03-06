import java.util.Scanner;

class Main {
    static CustomerService cs = new CustomerService();
    static int turn = 1;
    public static void main(String[] args) {
        Player p1 = new Player();
        Player p2 = new Player();
        Player player = p1;
        Player s_player = p2;
        
        //Set up both boards
        for (int i = 0; i < 2; i ++){
            
            if (turn % 2 == 1){
                player = p1;
            }
            else {
                player = p2;
            }

            SetUp(player);
            Shift();
        }

        while (!p1.lost() || !p2.lost()){
            
            if (turn % 2 == 1){
                player = p1;
                s_player = p2;
            }
            else {
                player = p2;
                s_player = p1;
            }

            player.panel.printGrid();
            player.plank.printGrid();
            System.out.println(cs.Plink(s_player));
            cs.paktoc();
            Shift();
            
        }

    }

    public static void SetUp(Player player) {
        ClearScreen.Clear();
        
        int[] lengths = {5, 4, 3, 3, 2};
        for (int i = 0; i < lengths.length; i++){
            Ship temp = new Ship(cs.Place(lengths[i], player));
            player.ships[i] = temp;
        }
    }

    public static void Shift() {
        ClearScreen.Clear();
        System.out.println("TURN SHIFT");
        cs.paktoc();
        turn += 1;
    }
    
}

class Player {
    Ship[] ships = new Ship[5];
    Grid panel = new Grid();
    Grid plank = new Grid();

    public void printShips() {
        for(Ship ship : ships){
            System.out.print(ship.length + " ");
        }
    }

    public boolean lost() {
        for (Ship ship : ships){
            
            if (!ship.Sunk()) {
                return false;    
            }
        
        }
        return true;
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

    Scanner scanner = new Scanner(System.in);
    
    /**
     * Plink takes player input, then calls the plink() function from the board class 
     * 
     * @param player - Fexible for different turn orders
     */
    
    public char[] Plink(Player player) {
        player.panel.printGrid();

        System.out.print("Please plink: ");
        String plonk = scanner.nextLine();
        char temp = player.plank.plink(plonk);

        player.panel.printGrid();
        return new char[] {temp, plonk.charAt(0), plonk.charAt(1)};
    }

    public String[] Place(int len, Player player) {
        ClearScreen.Clear();

        player.plank.printGrid();
        System.out.print("Please Choose a postion for the " + len + "-len ship: ");
        String place = scanner.nextLine();
        System.out.print("Please select a rotation(0 or 90): ");
        String rot = scanner.nextLine();
        String[] temp = player.plank.Set(place, len, Integer.parseInt(rot));    
        
        player.plank.printGrid();

        return temp;
    }

    /**
     * Press Any Key TO Contiue
     */
    public void paktoc(){        
        System.out.print("Press any key continue:");
        String nothing = scanner.nextLine();
    }
}

class ClearScreen{
    public static void Clear(){
            System.out.print("\033[H\033[2J");
            System.out.flush();
    }
}
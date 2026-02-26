import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        CustomerService cs = new CustomerService();
        cs.Place(6);

    }
}
// panel1.printGrid();

// System.out.print("Please plink: ");
// String plonk = scanner.nextLine();
// panel1.plink(plonk);

// panel1.printGrid();

class Grid {
    
    char[][] grid = new char[10][10];

    public Grid(){
       
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                grid[i][j] = '0';
            }
        }
    }
    
    public void printGrid() {
        
        for (char[] row : grid) {
            for (char col : row) {

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

    public int getCollumn(char arg) {
        char[] key = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'
        };
        
        int answer = -1;
        
        for (int i = 0; i < key.length; i++ ) {
            if (arg == key[i]) {
                answer = i;
            }
        }
        
        return answer;
    }


    // Will take a String of XA: where X is any letter between A - J and A is any number between 1 - 10
    
    public char plink(String args) {
        char a = args.charAt(0);
        int b = Integer.parseInt( Character.toString(args.charAt(1)) );
        
        int c = getCollumn(a);
        
        char temp = grid[b][c];
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

    public Boolean Set(String pos, int len, int rot){
        char a = pos.charAt(0);
        int b = Integer.parseInt( Character.toString(pos.charAt(1)) );
        int c = getCollumn(a);

        for (int i = 0; i < len; i++){
            if(rot == 0){
                if (grid[b + i-1][c] != '█'){
                    grid[b + i-1][c] = '█';
                } 
                else {
                    return false;
                }
            }
            else {
                if (grid[b][c + i] != '█'){
                    grid[b][c + i] = '█';
                }
                else {
                    return false;
                }
            }
        }

        return true;
    }
}

class CustomerService {
    
    
    Grid panel1 = new Grid();
    Grid plank1 = new Grid();
    Grid panel2 = new Grid();
    Grid plank2 = new Grid();
    
    
    public void Plink() {
        Scanner scanner = new Scanner(System.in);
        panel1.printGrid();

        System.out.print("Please plink: ");
        String plonk = scanner.nextLine();
        panel1.plink(plonk);

        panel1.printGrid();
        scanner.close();
    }

    public void Place(int len) {
        Scanner scanner = new Scanner(System.in);

        plank1.printGrid();
        System.out.print("Please Choose a postion for the " + len + "-len ship: ");
        String place = scanner.nextLine();
        System.out.print("Please select a rotation(0 or 90): ");
        String rot = scanner.nextLine();
        plank1.Set(place, len, Integer.parseInt(rot));    
        
        plank1.printGrid();
        scanner.close();
    }
}
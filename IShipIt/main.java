import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Grid board = new Grid();
        board.printGrid();

        System.out.print("Please plink: ");
        String plonk = scanner.nextLine();
        board.plink(plonk);

        board.printGrid();

        scanner.close();
    }
}

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
    
    public void plink(String args) {
        char a = args.charAt(0);
        int b = Integer.parseInt( Character.toString(args.charAt(1)) );
        
        int c = getCollumn(a);
        
        grid[b][c] = 'O';
    }
}
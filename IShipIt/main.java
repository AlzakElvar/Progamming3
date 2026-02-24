class Test{
    public static void main(String[] args) {
        System.out.println("Hello World\n");
        Grid board = new Grid();
        board.printGrid();
    }
}

class Grid {
    
    int[][] grid = new int[10][10];
    
    public void printGrid() {
        
        for (int[] row : grid) {
            for (int col : row) {
        
                if (col == 0) {                     //0 means base state
                    System.out.print(col + "  ");
                } 
                else if (col == 1) {                //1 means miss
                    System.out.print("0  ");
                } 
                else if (col == 2){                 //2 means hit
                    System.out.print("X  ");
                } 
                else if (col == 3){
                    System.out.print("█  ");        //3 means ship (unhit)
                }
                else if (col == 4){
                    System.out.print("⍁ ");        //4 means ship (hit)
                }
                
            }
        System.out.print("\n");
        }
    }

    public int collumn(char arg) {
        char[] key = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j'
        };
        
        int answer = 0;
        
        for (int i = 0; i < key.length; i++ ) {
            answer = i;
        }
        
        return key[0];
    }

    public void plink(String args) {
        char a = args.charAt(0);
        int x = 0;
        
        if (a == 'a') {
            x = 0;
        }
        

        System.out.print(x);
    }
}
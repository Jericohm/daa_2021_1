import java.util.*;
import java.io.File;

public class BalanceoCodigo{

    char arr [] = new char[100];
    int Tope = 0;

    boolean is_empty(){
        return Tope == 0;
    }     
    
    char get_top(){
        return arr[Tope];
    }
    
    char pop(){
        if(Tope != 0){
            int Aux = Tope - 1;
            Tope--;
            return arr[Aux];
        }    
        else{
            System.out.println("Error de Balanceo");
            return ' ';
        }                    
    }
    
    void push(char caracter){        
        if(caracter == '('||caracter == '{'||caracter == '['){                       
            arr[Tope++] = '@';            
        }
    }
  
    public static void main(String[] args) {
        BalanceoCodigo Pila = new BalanceoCodigo();
        int tamaño = 200;
        int conta = 0;
        String [] Codigo = new String [tamaño];
        
        try{
            String file = "Tarea1Listas.txt";
            Scanner In = new Scanner(new File(file));
            
            while(In.hasNext()){
                Codigo[conta] = In.nextLine();
                conta++;            
            }
            System.out.println("-Carga de código exitosa-");
        }catch(Exception e){            
        }    
        
        

        for(int conta1 = 0;conta1 < conta; conta1++){
            for(int conta2 = 0;conta2 < Codigo[conta1].length(); conta2++){
                Pila.push(Codigo[conta1].charAt(conta2)); //Agregar código
                if(Codigo[conta1].charAt(conta2) == ')'||Codigo[conta1].charAt(conta2) == '}'||Codigo[conta1].charAt(conta2) == ']'){
                    Pila.pop();
                }
            } 
        } 

        if(Pila.Tope == 0){
            System.out.println("El código está balanceado");
        }else{
            System.out.print("El código está desbalanceado por: \""+ Pila.Tope+"\" ");
            if(Pila.Tope == 1)
                System.out.println("llave");
            else
                System.out.println("llaves");
        }
    }     
}
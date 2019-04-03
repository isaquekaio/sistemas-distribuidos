/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 20172014040034
 */
//public class server {}
import java.net.*;
import java.util.*;
import java.io.*;

public class server{
    private int porta;
    private ServerSocket ss;
    private Socket s;
    private OutputStream os;
    //Date d = new Date();
    /*/
    public server(int porta){
        this.porta = porta;
    }
    */
    public server(){
    
    }
    
    public server(int porta){
        this.porta = porta;
        try{
            ss = new ServerSocket(porta);
            System.out.println("Agrardando...");
            s = ss.accept();
       
        }catch(IOException ioe){
            ioe.printStackTrace();
        }
        
    }
    
    public void enviar() throws FileNotFoundException, IOException {
        FileOutputStream d = new FileOutputStream("d.txt");
        PrintWriter pr = new PrintWriter(d);
        pr.println("Isaque Kaio é bonitão!!!");
        pr.close();
        d.close();
        OutputStream os = s.getOutputStream();
        //ObjectInputStream os = new ObjectInputStream(s.getInputStream()); 
        os.write(d.toString().getBytes());//write
        os.close();
    }
    
    public static void main(String args[]){
        server s = new server();
    }
}
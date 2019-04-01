/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

/**
 *
 * @author 20172014040034
 */
//public class server {}
import java.net.*;
import java.util.*;
import java.io.*;

public class server{
    int porta = port;
    //Date d = new Date();
    public server(){
        try{
            ServerSocket ss = new ServerSocket(porta);
            System.out.println("Agrardando...");
            Socket s = ss.accept();
            FileOutputStream d = new FileOutputStream("d.txt");
            PrintWriter pr = new PrintWriter(d);
            pr.println("Isaque Kaio é bonitão!!!");
            pr.close();
            d.close();
            OutputStream os = s.getOutputStream();
            //ObjectInputStream os = new ObjectInputStream(s.getInputStream()); 
            os.write(d.toString().getBytes());//write
            os.close();
        }catch(IOException ioe){
            ioe.printStackTrace();
        }
    }
    public static void main(String args[]){
        
        server s = new server();
    }
}
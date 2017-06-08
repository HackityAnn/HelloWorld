/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package securesult.helloworldapi;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author root
 */
@WebService(serviceName = "HelloWorldAPI")
public class HelloWorldAPI {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "Hello")
    public String Hello(@WebParam(name = "Name") String Name) {
        //TODO write your implementation code here:
        return Name;
    }

    /**
     * Web service operation
     */

    /**
     * Web service operation
     */


    /**
     * This is a sample web service operation
     */

}

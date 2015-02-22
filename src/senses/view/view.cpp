/** view.cpp --- 
 *
 * Copyright (C) 2015 
 *
 * Author:  Steven QUINITO MASNADA
 *
 */

#include "view.hpp"

/**************************
 *
 *      Constructors
 *
 *************************/
View::View(){
    capture(0);
}
/**************************
 *
 *      Destructors
 *
 *************************/

/**************************
 *
 *       Methodes
 *
 *************************/
Mat getFrame(){
    Mat frame;
    return capture >> frame;
}

bool View::look(){
    // TODO revoir la gestion des erreurs
    if(!capture.isOpened()){
	cout << "Erreur lors de l'activation de la camera" << endl;
	return false;
    }
    else{
	return true;
    }
}

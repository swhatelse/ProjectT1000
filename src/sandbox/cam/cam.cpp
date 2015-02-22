#include <opencv2/opencv.hpp>
#include <highgui.h>
#include <iostream>

using namespace std;
using namespace cv;

int lowH = 70;
int lowS = 0;
int lowV = 0;
int highH = 140;
int highS = 40;
int highV = 66;


Mat detectEdge(Mat frame){
    Mat edges;
    cvtColor(frame, edges, CV_BGR2GRAY);
    GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
    Canny(edges, edges, 0, 30, 3);
    return edges;
}

Mat detectColor(Mat img){
    Mat binary;
    
    cvtColor(img, binary, CV_BGR2HSV);
    Scalar low(Scalar(lowH,lowS,lowV));
    Scalar high(Scalar(highH,highS,highV));
    GaussianBlur(binary, binary, Size(7,7), 1.5, 1.5);
    inRange(img, low, high, binary);
    return binary;
}

int main (int argc, char** argv){
    char key;
    VideoCapture capture(0);

    if(!capture.isOpened()){
	cout << "Erreur lors de l'activation de la camera" << endl;
	return -1;
    }

    namedWindow("Tuner", CV_WINDOW_AUTOSIZE);

    createTrackbar("LowH", "Tuner", &lowH, 359);
    createTrackbar("HighH", "Tuner", &highH, 359);
    createTrackbar("LowS", "Tuner", &lowS, 255);
    createTrackbar("HighS", "Tuner", &highS, 255);
    createTrackbar("LowV", "Tuner", &lowV, 255);
    createTrackbar("HighV", "Tuner", &highV, 255);


    Mat edges;
    Mat binary;
    namedWindow("edges",1);
    namedWindow("binary",1);
    namedWindow("original",1);

    while(key != 'q' && key != 'Q') {
	Mat frame;
        capture >> frame; // get a new frame from camera
	edges = detectEdge(frame);
	binary = detectColor(frame);

	imshow("binary", binary);
	imshow("original", frame);
	imshow("edges", edges);
	// On attend 10ms
	key = cvWaitKey(10);
    }
    
    return 0;
}

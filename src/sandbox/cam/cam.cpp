#include <opencv2/opencv.hpp>
#include <highgui.h>
#include <iostream>

using namespace std;
using namespace cv;

// int lowH = 70;
// int lowS = 0;
// int lowV = 0;
// int highH = 140;
// int highS = 40;
// int highV = 66;

// Blue
int lowH = 215;
int lowS = 0;
int lowV = 0;
int highH = 359;
int highS = 175;
int highV = 163;


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

Mat shot(VideoCapture cap){
    Mat s;
    cap >> s;
    return s;
}

void detectCircle(Mat src_gray, Mat src){
    /// Reduce the noise so we avoid false circle detection
    // GaussianBlur( src_gray, src_gray, Size(9, 9), 2, 2 );

    vector<Vec3f> circles;

    /// Apply the Hough Transform to find the circles
    HoughCircles(src_gray, circles, CV_HOUGH_GRADIENT, 1, src_gray.rows/8, 50, 25, 0, 0 );

    /// Draw the circles detected
    for( size_t i = 0; i < circles.size(); i++ )
    {
	Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
	int radius = cvRound(circles[i][2]);
	// circle center
	circle( src, center, 3, Scalar(0,0,255), -1, 8, 0 );
	// circle outline
	// circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
    }

    /// Show your results
    namedWindow( "Hough Circle Transform Demo", CV_WINDOW_AUTOSIZE );
    imshow( "Hough Circle Transform Demo", src );

    // waitKey(0);
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

    Mat pic;
    Mat picBin;

    bool pressed = false;

    image = imread("", CV_LOAD_IMAGE_COLOR);
    
    while(key != 'q' && key != 'Q') {
    	Mat frame;
        capture >> frame; // get a new frame from camera

    	binary = detectColor(frame);
    	edges = detectEdge(frame);

    	imshow("binary", binary);
    	imshow("original", frame);
    	imshow("edges", edges);
    	// On attend 10ms
    	key = cvWaitKey(30);
	// if(key == 's'|| key == 'S'){
	//     if(!pressed){
	// 	pressed = true;
	// 	pic = shot(capture);
	// 	picBin = detectColor(pic);
	// 	detectCircle(picBin, pic);
	// 	cout << "S pressed" << endl;
	//     }
	// }
	// else{
	//     pressed = false;
	// }

    }
    
    return 0;
}

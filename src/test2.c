#include <opencv/cv.hpp>
#include <opencv2/opencv.hpp>
#include <opencv/highgui.h>

int main(int argc, char** argv)
{
    cvNamedWindow("DisplayCamera", CV_WINDOW_AUTOSIZE);
    CvCapture* capture = cvCreateCameraCapture(0);
    IplImage* frame;

    const char filename[] = "video.avi";

//  int fourcc = CV_FOURCC('X','V','I','D');
//  int fourcc = CV_FOURCC('P','I','M','1');
    int fourcc = CV_FOURCC('M','J','P','G');
//  int fourcc = CV_FOURCC('M', 'P', '4', '2');
//  int fourcc = CV_FOURCC('D', 'I', 'V', '3');
//  int fourcc = CV_FOURCC('D', 'I', 'V', 'X');
//  int fourcc = CV_FOURCC('U', '2', '6', '3');
//  int fourcc = CV_FOURCC('I', '2', '6', '3');
//  int fourcc = CV_FOURCC('F', 'L', 'V', '1');
//  fourcc = -1;
//  int fourcc = 0;

//  printf("%d\n", fourcc);

    double fps = cvGetCaptureProperty(capture, CV_CAP_PROP_FPS);
    int width = (int) cvGetCaptureProperty( capture, CV_CAP_PROP_FRAME_WIDTH );
    int height = (int) cvGetCaptureProperty( capture, CV_CAP_PROP_FRAME_HEIGHT );
    CvSize size = cvSize( width , height );
    int isColor = 1;
    CvVideoWriter* writer = cvCreateVideoWriter(filename, fourcc, fps, size, isColor);

    while(1)
    {
        frame = cvQueryFrame( capture );
        if( !frame )
        {
            fprintf(stderr,"Frame error");
            break;
        }

        cvWriteFrame(writer , frame);
        cvShowImage("DisplayCamera", frame);

        char c = cvWaitKey( 30 );
        if( c == 27 ) break;    
    }

    cvReleaseVideoWriter(&writer);
    cvReleaseImage(&frame);
    cvReleaseCapture(&capture);
    cvDestroyWindow("DisplayCamera");
    return 0;
}

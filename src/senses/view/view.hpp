#ifndef View_hpp 1
#define View_hpp 1

#include <opencv2/opencv.hpp>

class View{
public:
    View();
    ~View();
    void look();
    Mat getFrame();
    
private:
    VideoCapture capture;
};

#endif // View_hpp

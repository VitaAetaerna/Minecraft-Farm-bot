#include "iostream"
#include "time.h"

using namespace std;

int StartBot(float time_line)
{
    time_t now = time(nullptr);
    tm* current_time = localtime(&now);

    int current_minute = current_time->tm_min;

    int defined_minute = current_minute + 1;

    while (current_minute < defined_minute)
    {
        current_minute = current_time->tm_min;
    }
}

int InputTime(){
    float time_line = NULL;
    cout << "Wedlcome to Hypixel Skyblock farmbot" << endl;
    cout << "Please enter the time you need for moving from one Line to another: ";
    cin >> time_line;
    StartBot(time_line);
}

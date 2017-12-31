// TypingTyrant.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <windows.h>
#include <winuser.h>

using namespace std;

long getTime()
{
	SYSTEMTIME time;
	GetSystemTime(&time);
	LONG time_ms = (time.wSecond * 1000) + time.wMilliseconds;
	return time_ms;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char i;
	long lastTime = 0;
	long nrChar = 0;
	double longRunningAvg = 0; // This is the goal
	double shortRunningAvg = 50; // This is the current

	while (1)  
	{
		for (i = 8; i <= 190; i++)
		{
			if (GetAsyncKeyState(i) == -32767)
			{
				if (i == 8)
				{
					
					// Compare to last time
					long timeDiff = getTime() - lastTime;

					// Run if less than thresshold
					if (timeDiff > 1000)
					{
						
						// Update running average 50/50
						longRunningAvg = longRunningAvg * 0.75 + nrChar * 0.25;
						shortRunningAvg = shortRunningAvg * 0.5 + nrChar * 0.5;

						// Print message
						//cout << "Backspace was pressed at " << getTime();
						cout << "Characters typed since last backspace: " << nrChar << " ";
						cout << "Long Running avg: " << longRunningAvg << " ";
						cout << "Short Running avg: " << shortRunningAvg << " ";
						cout << endl;

						// Reset nrChar
						nrChar = 0;
				
					}

					// Beep if running average gets low
					// if (runningAvg < 20)
					if (shortRunningAvg < longRunningAvg)
					{
						Beep(1000, 100);
					}

					// Update last time
					lastTime = getTime();
				} else {
					nrChar++;
				}
			}
		}
	}

	return 0;
}


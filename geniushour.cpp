#include <iostream>
using namespace std;

int main() {
	int room = 1;
	char choice = 'w';

	while (choice != 'q') {
		switch (room) {
		case 1:
			cout << "You're in a basement and its cold. You're alone the only sound you can hear is your breathing and droplets of water. Interested, you choose to explore. You can go (s)outh." << endl;
			cin >> choice;
			if (choice == 's' || choice == 'S')
				room = 2;
			else
				cout << "Sorry, not an option" << endl;
			break; 
		
		case 2:
			cout << "You walk into the next room. Yet, it looks like where you were before. Is this an endless loop? The only way to find out is to explore more! You can go (s)outh, (n)orth, or (w)est." << endl;
			cin >> choice;
			if (choice == 's' || choice == 'S')
				room = 4;
			else if (choice == 'n' || choice == 'N')
				room = 1;
			else if (choice == 'w' || choice == 'W')
				room = 3;
			else
				cout << "Sorry, not an option" << endl;
			break;

		case 3:
			cout << "You reached somewhat of a dead end, but it seems like its neverending. You look to your right. Another door, you can go (e)ast" << endl;
			cin >> choice;
			if (choice == 'e' || choice == 'E')
				room = 2;
			else
				cout << "Sorry, not an option" << endl;
			break;

		case 4:
			cout << "The walls surround you unless you turn back! Its the same scenery. It seems like you're trapped, you can only go (n)orth." << endl;
			cin >> choice;
			if (choice == 'n' || choice == 'N')
				room = 2;
			else
				cout << "Sorry, not an option" << endl;
			break;




		}//end switch

	}//end game loop

}// end of main

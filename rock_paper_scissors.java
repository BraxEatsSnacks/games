// BraxEatsSnacks

/**
	Program that allows user to play "Rock, Paper, Scissors" against computerized player
*/

import java.util.Scanner;

public class rock_paper_scissors {

	public static void display_menu() {
		/* Prints out menu to console */

		// menu
		System.out.println();
		System.out.println("****** RO-CHAM-BEAU LET'S GO! ******");
		System.out.println("* 0) ROCK");
		System.out.println("* 1) PAPER");
		System.out.println("* 2) SCISSORS");
		System.out.println("************************************");
		System.out.println();
		// instructions
		System.out.println("Remember to select your move based on number! (#)");
		System.out.println();
		System.out.println();
	}

	public static int computer_choice() {
		/* Randomly generates computer choice */

		double number = Math.random();
		int choice;

		if (number >= 0.00 && number < 0.33) {
			choice = 0;
		}

		else if (number >= 0.33 && number < 0.66) {
			choice = 1;
		}

		else {
			choice = 2;
		}

		return choice;
	}

	public static int user_choice() {
		/* Asks user for choice */

		Scanner input = new Scanner(System.in);

		System.out.print("Your turn! Enter your choice (#): ");
		int num = input.nextInt();

		// invalid choices
		while (num != 0 && num != 1 && num != 2) {
			System.out.print("That isn't a valid choice. Try again. ");
			num = input.nextInt();
		}

		return num;
	}

	public static Boolean beat(int user_choice, int computer_choice) {
		/* Did the user beat the computer? */

		// rock vs rock
		if (user_choice == 1 && computer_choice == 1) {
			 return false;
		}

		// rock vs paper
		else if (user_choice == 1 && computer_choice == 2) {
			return false;
		}

		// rock vs scissors
		else if (user_choice == 1 && computer_choice == 3) {
			return true;
		}

		// paper vs paper
		else if (user_choice == 2 && computer_choice == 2) {
			return false;
		}

		// paper vs scissors
		else if (user_choice == 2 && computer_choice == 3) {
			return false;
		}

		// paper vs rock;
		else if (user_choice == 2 && computer_choice == 1) {
			return true;
		}

		// scissors vs scissors
		else if (user_choice == 3 && computer_choice == 3) {
			return false;
		}

		// scissors vs rock
		else if (user_choice == 3 && computer_choice == 1) {
			return false;
		}

		// scissors vs paper
		else if (user_choice == 3 && computer_choice == 2) {
			return true;
		}

		// default
		return false;
	}

}
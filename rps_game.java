// BraxEatsSnacks

public class rps_game {

	public static void main(String[] args) {
		/* Game */

		rock_paper_scissors.display_menu(); // what it says
		int round = 1;

		int computer_score = 0; // score
		int user_score = 0; // score

		// MEAT & POTATOES

		// 10 rounds
		while (round <= 10) {

			// print round and scores
			System.out.println("Round: " + round);
			System.out.println();

			System.out.println("User: " + user_score);
			System.out.println("Computer " + computer_score);

			// computer choose
			int computer = rock_paper_scissors.computer_choice();
			System.out.println("Computer has chosen!");

			// user choose
			int user = rock_paper_scissors.user_choice();
			System.out.println();

			// not a tie
			if (user != computer) {
				round += 1;

				Boolean win = rock_paper_scissors.beat(user, computer);
				if (win) {
					System.out.println("HA! GOTEEEEEEEEEEEEM!");
					user_score += 1;
				}

				else {
					System.out.println("Nah G sorry. Computer won this one.");
					computer_score += 1;
				}
			}

			// tie
			else {
				System.out.println("Tie! This round is a do-over!");
				System.out.println();
				continue;
			}
		}

		// who won?
		// loser
		if (computer_score > user_score) {
			System.out.println("Sorry, you lose! Better luck next time!");
			System.out.println();
		}
		// winner
		else {
			System.out.println("AYEEE WIT IT! WINNER WINNER CHICKEN DINNER!");
			System.out.println();
		}
	}

}
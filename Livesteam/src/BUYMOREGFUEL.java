import java.util.Scanner;
import java.util.Random;


public class BUYMOREGFUEL {
	
	public static String[] append(String[] swears, String input) {
		int len = swears.length;
		
		String[] tempString = new String[len+1];
		for(int i=0;i<len;i++) {
			tempString[i] = swears[i];
		}
		
		tempString[tempString.length-1] = input;
		
		return tempString;
	}

	public static void main(String[] args) {
		boolean run = false;
		String[] swears = {"Fuck you", "Fuck off", "Piss off","No u","Cocksucker","motherfucker", "ass-tittie","fuckwad","dick magnet","cumsicle","ass-jabber",
				"homosexual","cunt","clitface","bastard","cockmuncher","cumtart","nut sack","nut smack","dick hole", "asshole","dick eater","fatass",
				"fart sniffer","fuck face","shit","n*glet","dick","dipshit","fag","faggot","dumbass","cock","fuck","pickledface anteater","roasted miscarriage",
				"you fapping to bob the builder looking nerd","jerk off", "dick-faggot","n*gger-faggot"};
		Scanner inputScanner = new Scanner(System.in);
		do {
			
			String input = inputScanner.nextLine();
			Random random = new Random();
			boolean hasSwear = false;
			
			
			for (int i = 0; i<swears.length;i++) {
				 if (input.toLowerCase().trim().equals(swears[i].toLowerCase().trim())) {
					 //choose a random swear from the array and tell that to the user
					 int num = random.nextInt(swears.length);
					 System.out.println(swears[num]);
					 hasSwear = true;
				 }
			}
			if (hasSwear == false && !input.equals("quit")) {
				System.out.println("Try a smarter insult bitch");
				swears = append(swears,input);
			} else if (input.equals("quit")) {
				run = true;
			}
			
		} while (run != true);
		inputScanner.close();
	}

}

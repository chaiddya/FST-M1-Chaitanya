package Activities;

import java.io.File;
import java.io.IOException;
import java.util.*;

public class Activity13 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<Integer>();
        Random indexGen = new Random();

        System.out.print("Enter integers please ");
        System.out.println("(EOF or non-integer to terminate): ");

        while(scan.hasNextInt()) {
            list.add(scan.nextInt());
        }

        Integer nums[] = list.toArray(new Integer[0]);
        int index = indexGen.nextInt(nums.length);
        System.out.println("Index value generated: " + index);
        System.out.println("Value in arary at generated index: " + nums[index]);

        scan.close();
    }

    public static class Activity14 {
        public static void main(String[] args) throws IOException {
            try {
                File file = new File("src/session4/newfile.txt");
                boolean fStatus = file.createNewFile();
                if(fStatus) {
                    System.out.println("File created successfully!");
                } else {
                    System.out.println("File already exists at this path.");
                }

                //get the file Object
                File fileUtil = FileUtils.getFile("src/session4/newfile.txt");
                //Read file
                System.out.println("Data in file: " + FileUtils.readFileToString(fileUtil, "UTF8"));

                //Create directory
                File destDir = new File("resources");
                //Copy file to directory
                FileUtils.copyFileToDirectory(file, destDir);

                //Get file from new directory
                File newFile = FileUtils.getFile(destDir, "newfile.txt");
                //Read data from file
                String newFileData = FileUtils.readFileToString(newFile, "UTF8");
                //Print it
                System.out.println("Data in new file: " + newFileData);
            } catch(IOException errMessage) {
                System.out.println(errMessage);
            }
        }
    }
}
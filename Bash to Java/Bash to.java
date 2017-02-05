import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Trollah
{
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException
	{
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Enter batch file name:");
		String datFilename = keyboard.nextLine();
		System.out.println("Enter java file name:");
		String java = keyboard.nextLine();
		Scanner file = new Scanner(new File(datFilename));
		PrintWriter writer = new PrintWriter(java + ".java", "UTF-8");
		writer.println("import java.io.File;");
		writer.println("import java.io.IOException;");
		writer.println("import java.io.PrintWriter;");
		writer.println(" ");
		writer.println("public class " + java.substring(0,1).toUpperCase() + java.substring(1));
		writer.println("{");
		writer.println("\t@SuppressWarnings(\"resource\")");
		writer.println("\tpublic static void main(String[] args) throws IOException");
		writer.println("\t{");
		writer.println("\t\tPrintWriter writer = new PrintWriter(\"" + datFilename + "\", \"UTF-8\");");
		String line = "";
		while (file.hasNextLine())
			line = file.nextLine();
			System.out.println("Found line " + line);
			writer.println("\t\twriter.println(\"" + line + "\");");
		writer.println("\t\twriter.close();");
		writer.println("\t\tRuntime.getRuntime().exec(\"cmd /c start " + datFilename + "\");");
		writer.println("\t}");
		writer.println("}");
		writer.close();
		System.out.println("Program generated :D");
	}
}
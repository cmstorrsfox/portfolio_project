import java.util.ArrayList;


public class RHUL {
  //static variables
  public static int totalStudents = 0;
  public static int totalTutors = 0;
  public static int totalClasses = 0;
  public static String[] cohorts = {"IFY", "IY1", "PMP"};
  public static ArrayList<TutorClass> classList = new ArrayList<TutorClass>();
  public static ArrayList<Tutor> tutorList = new ArrayList<Tutor>();
  public static ArrayList<Student> studentList = new ArrayList<Student>();


  public static void main(String[] args) {
  
    TutorClass SF06_AES = new TutorClass("SF06_AES");
    SF06_AES.assignTutor("Emmanuel Jones Sr.", "Academic English Skills", "Permanent", 48578);
    SF06_AES.addStudent("Paula Magoo", "IFY", "Arts & Social Sciences", 6.5, 7, 5.5, 6);
    SF06_AES.addStudent("Felicity Jones", "IFY", "Sciences B", 8, 7, 7, 6);


    TutorClass SF07_AES = new TutorClass("SF07_AES");
    SF07_AES.assignTutor("Paul McGinty", "Academic English Skills", "Permanent", 26822);
    SF07_AES.addStudent("Caroline Rushden", "IFY", "Arts & Social Sciences", 6.5, 7, 5.5, 6);
    SF07_AES.addStudent("John Stickly", "IFY", "Arts & Social Sciences", 8, 7, 7, 6);


    System.out.println("Students:");
    System.out.println("Total Students = "+RHUL.totalStudents);
    RHUL.studentList.forEach((std) -> System.out.println(std));
    
    System.out.println("Classes:");
    System.out.println("Total Classes = "+RHUL.totalClasses);
    RHUL.classList.forEach((cls) -> cls.printClassInfo());
    
    System.out.println("Tutors:");
    System.out.println("Total Tutors = "+RHUL.totalTutors);
    RHUL.tutorList.forEach((tut) -> System.out.println(tut));
    
  }


}
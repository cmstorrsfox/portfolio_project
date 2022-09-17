import java.util.ArrayList;

public class TutorClass {
  //instance variables
  String classCode;
  Tutor tutor;
  ArrayList<Student> studentList;

  public TutorClass(String classCode) {
    this.classCode = classCode;
    studentList = new ArrayList<Student>();
    RHUL.totalClasses += 1;
    RHUL.classList.add(this);
  }

  public void assignTutor(String name, String subject, String contractType, int salary) {
    this.tutor = new Tutor(name, subject, contractType, salary);
  }

  public void addStudent(String name, String course, String pathwayProgramme, double listening, double reading, double writing, double speaking) {
    Student student = new Student(name, course, pathwayProgramme, listening, reading, writing, speaking);
    studentList.add(student);

  }

  public void printClassInfo() {
    System.out.println("Class Information: \n\n"+
    "Class Code: "+classCode+"\n"+
    "Class Type: "+tutor.subject+"\n"+
    "Tutor Name: "+tutor.name+"\n"+
    "Students:\n");

    for (int i = 0; i < studentList.size(); i++) {
      System.out.println("Student #"+(i+1));
      System.out.println(studentList.get(i));
    }
  }


  
}

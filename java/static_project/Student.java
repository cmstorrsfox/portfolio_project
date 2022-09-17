public class Student {
  //instance variables
  public String name;
  public String course;
  public String pathwayProgramme;
  public InitialEnglish ieltsResults;


  public Student(String name, String course, String pathwayProgramme, double listening, double reading, double writing, double speaking) {
    this.name = name;
    this.course = course;
    this.pathwayProgramme = pathwayProgramme;
    this.ieltsResults = new InitialEnglish(listening, reading, writing, speaking);

    RHUL.totalStudents += 1;
    RHUL.studentList.add(this);
  }

  public String toString() {
    return "Name: "+name+"\n"+
           "Course: "+course+"\n"+
           "Pathway/Programme: "+pathwayProgramme+"\n"+
           ieltsResults+"\n";
  }
  
}

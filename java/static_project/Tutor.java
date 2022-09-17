public class Tutor {
  public String name;
  public String subject;
  private String contractType;
  private int salary;

  public Tutor(String name, String subject, String contractType, int salary) {
    this.name = name;
    this.subject = subject;
    this.contractType = contractType;
    this.salary = salary;

    RHUL.totalTutors += 1;
    RHUL.tutorList.add(this);
  }

  public String getContractType() {
    return this.contractType;
  }

  public int getSalary() {
    return this.salary;
  }

  public String toString() {
    return "name: "+this.name+"\n"+
           "subject: "+this.subject+"\n"+
           "contract type: "+this.contractType+"\n"+
           "salary "+this.salary+"\n";
  }

}

public class Person {
  int age;
  String fname;
  String lname;
  char gender;
  String fullName;
  ContactDetails contact;


  public Person(int currentAge, String firstName, String lastName, char sex) {
    age = currentAge;
    fname = firstName;
    lname =lastName;
    gender = sex;

    fullName = fname+" "+lname;
  }

  public int celebrateBirthday() {
    return age += 1; 
  }

  public void addContactInfo(String line1, String line2, String cityTown, String postalCode, String countryName, String telephone, String emailAddress) {
    
    ContactDetails details = new ContactDetails(line1, line2, cityTown, postalCode, countryName, telephone, emailAddress);

    contact = details;

  }

  public String toString() {
    return    "\tFirst Name: "+fname+"\n"+
              "\tLast Name: "+lname+"\n"+
              "\tFull Name: "+fullName+"\n"+
              "\tAge: "+age+"\n"+
              "\tGender: "+gender+"\n"+
              "\tContact: "+contact+"\n";
              
  }

}
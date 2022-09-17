public class ContactDetails {
  String addressFirst;
  String addressSecond;
  String city;
  String postcode;
  String country;
  String telNo;
  String email;

  public ContactDetails(String line1, String line2, String cityTown, String postalCode, String countryName, String telephone, String emailAddress) {
    addressFirst = line1;
    addressSecond = line2;
    city = cityTown;
    postcode = postalCode;
    country = countryName;
    telNo = telephone;
    email = emailAddress;
  }

  public String toString() {
    return addressFirst+"\n\t\t"+
           addressSecond+"\n\t\t"+
           city+"\n\t\t"+
           country+"\n\t\t"+
           telNo+"\n\t\t"+
           email+"\n";
  }
  
}

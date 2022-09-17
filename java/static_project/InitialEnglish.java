public class InitialEnglish {
  //instance variables
  double overall;
  double listening;
  double reading;
  double writing;
  double speaking;

  public InitialEnglish(double listening, double reading, double writing, double speaking) {
    this.listening = listening;
    this.reading = reading;
    this.writing = writing;
    this.speaking = speaking;  

    this.overall = Math.round((listening + reading + writing + speaking)/4);

  }

  public String toString() {
    return "Initial English Results:\n"+
           "Listening: "+listening+"\n"+
           "Reading: "+reading+"\n"+
           "Writing: "+writing+"\n"+
           "Speaking: "+speaking+"\n"+
           "Overall: "+overall+"\n";
  }

  public static void main(String[] args) {

  }
  
  
}

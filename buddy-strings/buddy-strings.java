class Solution {
    public boolean buddyStrings(String a, String b) {
        
        char[] ca = a.toCharArray();
    char[] cb = b.toCharArray();
    if (ca.length != cb.length) {
      return false;
    }
    if (a.equals(b)) {
      HashMap<Character, Integer> fr = new HashMap<>();
      for (int i=0; i<ca.length; i++) {
        if (fr.get(ca[i]) == null) {
          fr.put(ca[i], 1);
        } else {
          fr.merge(ca[i], 1, Integer::sum);
          return true;
        }
      }
      return false;
    }
    boolean swapTry = true;
    for (int i=0; i<cb.length; i++) {
      if (cb[i] != ca[i] && swapTry) {
        for (int j=i+1; j<ca.length; j++) {
          if (ca[j] == cb[i]) {
            char aux = ca[i];
            ca[i] = ca[j];
            ca[j] = aux;
            swapTry = false;
          }
        }
      }
    }
    for (int i=0; i<cb.length; i++) {
      if (ca[i] != cb[i]) {
        return false;
      }
    }
    return true;
        
// cbad  cbad
// -     -     
    }
}
import static java.lang.System.out;
import static java.lang.Math.pow;
import static java.lang.Math.ceil;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

import java.math.BigInteger;

class EulerProblem087 {

    private List<Integer> primesList;
    private Set<Integer> compList;
    final int N = 50000000;

    private void computePrimes() {
        final int M = (int) Math.ceil(Math.pow(N, .5));
        Boolean[] comp_nums = new Boolean[M];
        for (int k = 0; k < comp_nums.length; k++)
            comp_nums[k] = false;
        comp_nums[0] = true;

        for (int k = 3; k < comp_nums.length; k += 2)
            comp_nums[k] = true;

        int i = 1;
        while (2*i < M) {
            i += 2;
            if (comp_nums[i - 1])
                continue;
            for (int j = 2*i; j < M; j += i)
                comp_nums[j-1] = true;
        }

        for (int k = 0; k < comp_nums.length; k++)
            if (!comp_nums[k])
                primesList.add(k+1);
    }

    private void findCompNums() {
        for (int i = 0; i < primesList.size(); i++) {
            int foo = (int) Math.pow(primesList.get(i), 4);
            if (foo >= N)
                break;

            for (int j = 0; j < primesList.size(); j++) {
                int bar = foo + (int) Math.pow(primesList.get(j), 3);
                if (bar >= N)
                    break;

                for (int k = 0; k < primesList.size(); k++) {
                    int baz = bar + (int) Math.pow(primesList.get(k), 2);
                    if (baz >= N)
                        break;

                    compList.add(baz);
                }
            }
        }
        out.println("Answer: " + compList.size());
    }

    public EulerProblem087() {
        primesList = new ArrayList<Integer>();
        compList = new HashSet<Integer>();
        computePrimes();
        findCompNums();
    }

    Boolean[] comp_nums;

    public static void main(String[] args) {
        EulerProblem087 ep = new EulerProblem087();
    }
}

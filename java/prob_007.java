import static java.lang.System.out;

// Answer is prime below 104750, found by hand.

class EulerProblem007 {
    public static void main(String[] args)
    {
        while (true)
        {
            System.out.print("How high to go: ");
            int p = HowManyPrimes(Integer.parseInt(System.console().readLine().toString()));
            out.println(p);
        }
    }

    private static int HowManyPrimes(int n)
    {
        // final int n = 104750;
        int i = 2;

        Boolean[] comp_nums = new Boolean[n];
        for (int j = 0; j < comp_nums.length; j++)
            comp_nums[j] = false;

        while (2*i <= n)
        {
            if (!comp_nums[i - 1])
                for (int k = 2*i; k < n + 1; k += i)
                    comp_nums[k-1] = true;
            i++;
        }

        int prime_count = 0;
        for (int j = 0; j < comp_nums.length; j++)
            if (!comp_nums[j])
                prime_count++;

        return prime_count;
    }
}

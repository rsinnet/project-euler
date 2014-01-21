import static java.lang.System.out;
import java.util.List;
import java.util.ArrayList;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;

class EulerProblem080 {

    private static BigDecimal getSqrt(BigDecimal x) {
        BigDecimal x0 = BigDecimal.ZERO;
        BigDecimal x1 = BigDecimal.valueOf(Math.sqrt(Double.parseDouble(x.toString())));
        MathContext mc = new MathContext(110, RoundingMode.HALF_UP);

        while (!x1.setScale(101, RoundingMode.HALF_DOWN).equals(x0.setScale(101, RoundingMode.HALF_UP))) {
            x0 = x1;
            x1 = x0.subtract(x0.pow(2, mc).subtract(x, mc).divide(x0.multiply(BigDecimal.valueOf(2), mc),mc),mc);
        }

        return x0.setScale(100, RoundingMode.FLOOR);
    }

    private static int digitSum(BigDecimal bd) {
        char[] str = bd.toString().toCharArray();
        
        out.println(str.length);

        int cSum = 0;
        for (int i = 0; i < str.length - 1; i++)
            if (str[i] > 48 && str[i] <= 57)
                cSum += (int) str[i] - 48;

        return cSum;
    }

    public static void main(String[] args) {

        int cSum = 0;
        for (int i = 2; i < 100; i++) {
            if (i == 4 || i == 9 || i == 16 || i == 25 ||
                i == 36 || i == 49 || i == 64 || i == 81)
                continue;

            out.println(i + ": " + getSqrt(BigDecimal.valueOf(i)));            
            cSum += digitSum(getSqrt(BigDecimal.valueOf(i)));
        }

        out.println("Answer: " + cSum);

    }
}

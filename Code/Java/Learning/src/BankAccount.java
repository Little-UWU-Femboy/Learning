/**
 * A simple class representing a bank account.
 *
 * <p>This class demonstrates common Javadoc tags on classes, fields,
 * constructors, and methods.</p>
 *
 * @author Jane Doe
 * @version 1.0
 * @since 1.0
 */
public class BankAccount {

    /**
     * The name of the account holder. <p style="color:#FF0000;">Hello <strong>World</strong></p>
     * That was a good thing
     */
    public String ownerName;

    /**
     * The current balance of the account.
     */
    private double balance;

    /**
     * The unique account ID.
     */
    private final int accountId;

    /**
     * Creates a new BankAccount.
     *
     * @param ownerName the name of the account holder
     * @param initialBalance the starting balance (must be &gt;= 0)
     * @param accountId the unique account identifier
     * @throws IllegalArgumentException if initialBalance is negative
     */
    public BankAccount(String ownerName, double initialBalance, int accountId) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.ownerName = ownerName;
        this.balance = initialBalance;
        this.accountId = accountId;
    }

    /**
     * Deposits money into the account.
     *
     * <p>Example usage:
     * {@code account.deposit(100.0);}</p>
     *
     * @param amount the amount to deposit (must be positive)
     * @throws IllegalArgumentException if amount is not positive
     */
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
    }

    /**
     * Withdraws money from the account.
     *
     * @param amount the amount to withdraw (must be positive and &lt;= balance)
     * @return the new balance after withdrawal
     * @throws IllegalArgumentException if amount is invalid
     */
    public double withdraw(double amount) {
        if (amount <= 0 || amount > balance) {
            throw new IllegalArgumentException("Invalid withdrawal amount");
        }
        balance -= amount;
        return balance;
    }

    /**
     * Gets the current balance.
     *
     * @return the current account balance
     * @see #deposit(double)
     * @see #withdraw(double)
     */
    public double getBalance() {
        return balance;
    }

    /**
     * Gets the account owner's name.
     *
     * @return the owner's name
     */
    public String getOwnerName() {
        return ownerName;
    }

    /**
     * Gets the account ID.
     *
     * @return the account ID
     */
    public int getAccountId() {
        return accountId;
    }

    /**
     * Updates the account owner's name.
     *
     * @param newName the new owner name
     * @deprecated Use a verified profile update system instead.
     */
    @Deprecated
    public void setOwnerName(String newName) {
        this.ownerName = newName;
    }

    /**
     * Returns a string representation of the account.
     *
     * @return a string containing account details
     * <p><b>Implementation Note:</b> This implementation is simple and not secure for real systems.</p>
     */
    @Override
    public String toString() {
        return "BankAccount{" +
               "ownerName='" + ownerName + '\'' +
               ", balance=" + balance +
               ", accountId=" + accountId +
               '}';
    }
}

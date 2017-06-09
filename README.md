# CPE 101 Project 5
## File Matching


### Usage
To use this program, you must have a file named `oldMaster.dat` and `transactions.dat` file in the same directory as `fileMatching.py`.

To run the program, type:

```Sh
$ python3 fileMatching.py
```

### Authors
* **Dominic Gaiero**
* **Rusell Caletena**
### About the program
> In commercial data processing, it’s common to have several files in each system. In an
accounts receivable system, for example, there is generally a master file containing detailed
information about each customer such as the customer’s name, address, telephone number,
outstanding balance, credit limit, discount terms, contract arrangements and possibly a
condensed history of recent purchases and cash payments. In this program, we only stored the
customers’ account number, customers’ first and last name, customer’s balance, customers’
phone number, and customers’ city.

> As transactions occur (i.e., sales are made and cash payments arrive in the mail), they’re
entered into a file. At the end of each business period (i.e., a month for some companies, a week
for others and a day in some cases) the file of transactions (called "transaction.dat") is applied to
the master file (called "oldMaster.dat"), thus updating each account's record of purchases and
payments. After each of these updates, the master file is rewritten as a new file
("newMaster.dat"), which is then used at the end of the next business period to begin the
updating process again.

> File-matching programs must deal with certain problems that do not exist in single-file
programs. For example, a match does not always occur. A customer on the master file might not
have made any purchases or cash payments in the current business period, and therefore no
record for this customer will appear on the transaction file. Similarly, a customer who did make
some purchases or cash payments might have just moved to this community and the company
may not have had a chance to create a master record for this customer.

> Use the account number on each file as the record key for matching purposes. The
oldMaster.dat is not ordered. You need to read the file and generate a sequential file which issorted in increasing account number order. This sequential file will be sorted_oldMaster.dat. The
transaction.dat file has records of account numbers and value.

> When a match occurs (i.e., records with the same account number appear on both the master file
and the transaction file), add the dollar amount on the transaction file to the current balance on
the master file and write the "newMaster.dat" record. (Assume that purchases are indicated by
positive amounts on the transaction file, and that payments are indicated by negative amounts.)
When there is a master record for a particular account but no corresponding transaction record,
merely write the master record to "newMaster.dat". When there is a transaction record but no
corresponding master record, print the message "Unmatched transaction record for account
number ..." (fill in the account number from the transaction record)
For example:
> `Unmatched transaction record for account 900`

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

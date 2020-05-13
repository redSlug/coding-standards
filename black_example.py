gross_wages = 1
taxable_interest = 1
dividends = 1
qualified_dividends = 1
ira_deduction = 1
student_loan_interest = 1

# income = (gross_wages +
#           taxable_interest +
#           (dividends - qualified_dividends) -
#           ira_deduction -
#           student_loan_interest)

income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# def wonderful_function(x, y, z):
#
#     x += y ** z
#
#     x *= 3
#
#     return x


def wonderful_function(x, y, z):

    x += y ** z

    x *= 3

    return x


# spam( ham[ 1 ], { eggs: 2 } )

spam( ham[ 1 ], { eggs: 2 } )


# FILES = ['setup.cfg', 'tox.ini',]
# initialize(FILES, error=True,)

FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)

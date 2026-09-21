*** Settings ***
Documentation    Runs the generated rows in ages.csv and phones.csv against the two
...              functions they were written for, in the Robot repo's DataHelpers.
...              Every row is checked even if an earlier one fails, so one run shows
...              every disagreement.
...              Needs robot-framework-learning checked out next to qa-portfolio.
...              Run from this folder:  robot --outputdir results run.robot
Library          ${CURDIR}/../../../../robot-framework/libraries/DataHelpers.py


*** Test Cases ***
Every Age Row Gives Its Expected Result
    ${rows}=    Read CSV Rows    ${CURDIR}/ages.csv
    FOR    ${row}    IN    @{rows}
        Run Keyword And Continue On Failure    Check Age Row    ${row}
    END

Every Phone Row Gives Its Expected Result
    ${rows}=    Read CSV Rows    ${CURDIR}/phones.csv
    FOR    ${row}    IN    @{rows}
        Run Keyword And Continue On Failure    Check Phone Row    ${row}
    END


*** Keywords ***
Check Age Row
    [Arguments]    ${row}
    IF    $row['expected'] == 'error'
        # Not Run Keyword And Expect Error: its failure message cannot say which
        # row it was, and with a dozen rows in one loop that is the only thing
        # worth knowing.
        ${status}    ${result}=    Run Keyword And Ignore Error
        ...    Age On    ${row}[birthdate]    ${row}[on]
        Should Be Equal    ${status}    FAIL
        ...    msg=${row}[case] (${row}[source]): expected an error, got ${result}    values=False
    ELSE
        ${age}=    Age On    ${row}[birthdate]    ${row}[on]
        Should Be Equal As Integers    ${age}    ${row}[expected]
        ...    msg=${row}[case] (${row}[source]): expected ${row}[expected], got ${age}    values=False
    END

Check Phone Row
    [Arguments]    ${row}
    IF    $row['expected'] == 'error'
        ${status}    ${result}=    Run Keyword And Ignore Error
        ...    Normalize Phone Number    ${row}[input]
        Should Be Equal    ${status}    FAIL
        ...    msg=${row}[case] (${row}[source]): expected an error for '${row}[input]', got '${result}'    values=False
    ELSE
        ${clean}=    Normalize Phone Number    ${row}[input]
        Should Be Equal    ${clean}    ${row}[expected]
        ...    msg=${row}[case] (${row}[source]): expected '${row}[expected]', got '${clean}'    values=False
    END

<h1><u> Python Logon and Company Intranet Program</u></h1>

<h2><u>Classes</u></h2>
<p> <b>Employee:</b> Template class
representing an employee with username and password fields, as well as a terminal program
with an associated helper function.</p>
<p> <b> Admin: </b> Possesses full access rights and can
perform any function from the intranet portal.</p>
<p> <b> Engineer: </b> Possesses rights to their own timesheet
as well as project documents, but not management operations.</p>
<p> <b> Intern: </b> Possesses access rights only to their 
personal timesheet. </p>

<h2><u>Logon Portal and Intranet</u></h2>

<p><b> CSV File: </b> stores access privileges, usernames, and passwords 
in plaintext. On a single row, a role, username, and password corresponding to a single user
are comma separated. Used by the logon portal.</p>

<p> <b>Main program: </b> </p>
<ul>
    <li> The program proceeds by first giving a greeting to the
    user, and then asking them for their username; the user may also quit. </li>
    <li> Once a valid username is input, the program then asks for a password;
    the user may also quit. </li>
    <li> Upon correct password input, access to the company intranet terminal is given. </li>
        <ul>
            <li> Admins have full access. </li>
            <li> Engineers have access to project documents and their timesheet. </li>
            <li> Interns only have access to their timesheet. </li>
            <li> If a role is read other than the above, the program will abort. </li>
            <li> If a user with insufficient access rights attempts to open an
            unauthorized task, they will be rebuffed. </li>
            <li> The user is brought back to this main menu screen until they
            quit voluntarily. </li>
        </ul>
</ul>
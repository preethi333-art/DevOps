git rebase -i means interactive rebase.

The -i stands for interactive.

It opens an editor and lets you modify, combine, reorder, or delete commits before Git reapplies them.

Example

Suppose your history is:

A --- B --- C --- D (HEAD)

Run:

git rebase -i HEAD~3

Git opens something like:

pick abc123 C
pick def456 D
pick ghi789 E

Now you can change the commands:

1. Squash commits
pick abc123 C
squash def456 D
squash ghi789 E

Result:

A --- B --- X

Where X contains all changes from C, D, and E.

2. Reword a commit message
reword abc123 C
pick def456 D
pick ghi789 E

Git will ask you to edit the commit message for C.

3. Drop a commit
pick abc123 C
drop def456 D
pick ghi789 E

Commit D is removed.

4. Reorder commits
pick def456 D
pick abc123 C
pick ghi789 E

Git will replay them in that order.

Common interactive rebase commands
Command	Meaning
pick	Keep the commit
reword	Change commit message
edit	Stop and modify the commit
squash	Combine with previous commit
fixup	Combine with previous commit and discard message
drop	Remove the commit
Why use it?

Before creating a Pull Request, you might have:

Add login
Fix typo
Fix typo again
Debug print
Remove debug print

Using interactive rebase, you can clean it up into:

Add login feature

This gives a cleaner project history.

Important

Interactive rebase rewrites commit history.

So:

✅ Safe on your own local branch.
⚠️ Avoid on commits already pushed and used by others unless everyone agrees.
Interview answer

git rebase -i (interactive rebase) allows you to edit commit history by reordering, squashing, rewording, editing, or removing commits before they are reapplied. It is commonly used to clean up commit history before merging code.

git stash apply command
git stash apply

git stash apply restores the changes saved in a stash but keeps the stash entry in the stash list.

Example

You have uncommitted changes:

git stash

Git saves them:

stash@{0}: WIP on feature-login

View stashes:

git stash list

Output:

stash@{0}: WIP on feature-login

Now restore the changes:

git stash apply

✅ Changes are restored to your working directory.
✅ stash@{0} still exists.

Apply a specific stash
git stash apply stash@{1}
apply vs pop
Apply
git stash apply

Result:

Working directory: Changes restored
Stash list: Still contains the stash
Pop
git stash pop

Result:

Working directory: Changes restored
Stash list: Stash removed
Easy way to remember
apply = Copy the stash back, keep the original.
pop = Take the stash back and remove it from the stash stack.
Interview Answer

git stash apply restores stashed changes to the working directory without removing the stash from the stash list. Unlike git stash pop, it keeps the stash available for future use.

git diff
git show
git blame
git bisect

explain clearly

These are very important Git commands for debugging and understanding code history.

1. git diff
Purpose

Shows the differences between versions of files.

Example

You changed a file:

System.out.println("Hello");

to

System.out.println("Hello World");

Run:

git diff

Output:

- System.out.println("Hello");
+ System.out.println("Hello World");
Common uses

See unstaged changes

git diff

See staged changes

git diff --staged

Compare two commits

git diff commit1 commit2
2. git show
Purpose

Shows details of a commit.

Example
git show

Shows:

Commit ID
Author
Date
Commit message
Code changes

Example:

commit a1b2c3d
Author: Preethi

Added login page

+ LoginController.java
- OldLogin.java
Show a specific commit
git show a1b2c3d
When to use?

When someone gives you a commit ID and says:

"Check what changes were made in this commit."

3. git blame
Purpose

Shows who last modified each line of a file.

Example

File:

public class Test {
   String name;
   int age;
}

Run:

git blame Test.java

Output:

a1b2c3d (Preethi) String name;
e4f5g6h (Ravi)    int age;

Meaning:

name line was last modified by Preethi.
age line was last modified by Ravi.
Why use it?

Suppose you find a bug in line 200:

if(age < 0)

Run:

git blame User.java

You can identify:

Who changed it.
Which commit changed it.
When it was changed.
4. git bisect
Purpose

Finds the commit that introduced a bug.

Imagine:

A --- B --- C --- D --- E --- F
Commit A = works
Commit F = broken

You don't know which commit introduced the bug.

Step 1: Start bisect
git bisect start
Step 2: Mark bad commit
git bisect bad

(Current commit is broken.)

Step 3: Mark good commit
git bisect good A

Git automatically checks out a commit in the middle:

A --- B --- C --- D --- E --- F
          ↑
Step 4: Test

If the checked-out commit works:

git bisect good

If it is broken:

git bisect bad

Git keeps cutting the search space in half.

Example
A (good)
B (good)
C (good)
D (bad)
E (bad)
F (bad)

Git will quickly identify:

D

as the first bad commit.

Step 5: End bisect
git bisect reset

Returns you to your original branch.

Quick Interview Summary
Command	Purpose
git diff	Shows differences between files, commits, or staging area
git show	Displays details and changes of a commit
git blame	Shows who last modified each line of a file
git bisect	Uses binary search to find the commit that introduced a bug
Easy Memory Trick
diff → What changed?
show → Show me this commit.
blame → Who changed this line?
bisect → Which commit introduced the bug?

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - Entry point
*
* Description: Make a infinite loop
* Return: 0 on success
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Entry point
*
* Description: Make 5 zombie process
* Return: 0 on success, 1 on fail
*/
int main(void)
{
	pid_t pid0, pid1, pid2, pid3, pid4;

	pid0 = fork();
	if (pid0 > 0)
		printf("Zombie process created, PID: %i\n", pid0);
	else
		exit(1);

	pid1 = fork();
	if (pid1 > 0)
		printf("Zombie process created, PID: %i\n", pid1);
	else
		exit(1);

	pid2 = fork();
	if (pid2 > 0)
		printf("Zombie process created, PID: %i\n", pid2);
	else
		exit(1);

	pid3 = fork();
	if (pid3 > 0)
		printf("Zombie process created, PID: %i\n", pid3);
	else
		exit(1);

	pid4 = fork();
	if (pid4 > 0)
		printf("Zombie process created, PID: %i\n", pid4);
	else
		exit(1);

	infinite_while();
	return (0);
}

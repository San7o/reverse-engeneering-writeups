#include <fcntl.h>
#include <unistd.h>

int get_flag() {
    int fd = open("/home/orw/flag", O_RDONLY, 0);
    int buff[30];
    read(fd, &buff, 30);
    write(0, &buff, 30);
}

int main() {
    get_flag();
    return 0;
}


#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/thread/thread.hpp>
#include <iostreams>


int main() {
    std::cout << "Sleeping for 1 second...\n";
    boost::this_thread::sleep(boost::posix_time::seconds(1));
    std::cout << "Woken up!\n";
    return 0;
}

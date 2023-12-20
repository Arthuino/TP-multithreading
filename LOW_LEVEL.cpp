
#include <cpr/cpr.h>

#include <eigen3/Eigen/Dense>
#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

class Task {
 public:
  /**
   * @brief Construct a new Task object
   * @param identifier_ the identifier of the task (int)
   * @param a_ the matrix a (Eigen::MatrixXd)
   * @param b_ the matrix b (Eigen::MatrixXd)
   * @param x_ the matrix x (Eigen::MatrixXd)
   */
  Task(int identifier_, Eigen::MatrixXd a_, Eigen::MatrixXd b_,
       Eigen::MatrixXd x_) {
    identifier = identifier_;
    a = a_;
    b = b_;
    x = x_;
  }

  int identifier;
  Eigen::MatrixXd a;
  Eigen::MatrixXd b;
  Eigen::MatrixXd x;

  void work() { x = a.colPivHouseholderQr().solve(b); }
};

int main() {
  // infinite loop
  while (true) {
    // send a GET request to the server
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});
    // print the response
    std::cout << r.text << std::endl;

    if (r.status_code != 200) {
      // if the server is not running, exit the program
      std::cout << "Server is not running" << std::endl;
      return 0;
    }

    // check if response if empty
    if (r.text.empty()) {
      // if the response is empty, exit the program
      std::cout << "Response is empty" << std::endl;
      return 0;
    }

    // parse the response
    json data = json::parse(r.text);

    // print the data
    std::cout << data << std::endl;

    // sleep for 1 second
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

  return 0;
}

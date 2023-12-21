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
  Task(int identifier_, Eigen::MatrixXd a_, Eigen::MatrixXd b_) {
    identifier = identifier_;
    a = a_;
    b = b_;
  }

  int identifier;
  Eigen::MatrixXd a;
  Eigen::MatrixXd b;
  Eigen::MatrixXd x;

  void work() { x = a.lu().solve(b); }
};

namespace JsonParsing {
std::vector<std::vector<double>> convertDataToVector(json j) {
  return (j != nullptr) ? j.get<std::vector<std::vector<double>>>()
                        : std::vector<std::vector<double>>();
}

Eigen::MatrixXd convertVectToEigenMatrix(
    const std::vector<std::vector<double>>& vec) {
  Eigen::MatrixXd mat(vec.size(), vec[0].size());

  for (int i = 0; i < vec.size(); ++i) {
    for (int j = 0; j < vec[0].size(); ++j) {
      mat(i, j) = vec[i][j];
    }
  }
  return mat;
}

Eigen::MatrixXd convertDataToEigenMatrix(json j) {
  std::vector<std::vector<double>> vec = convertDataToVector(j);
  return convertVectToEigenMatrix(vec);
}

json convertEigenMatrixToJson(Eigen::MatrixXd mat) {
  std::vector<std::vector<double>> vec(mat.rows(),
                                       std::vector<double>(mat.cols()));

  for (int i = 0; i < mat.rows(); ++i) {
    for (int j = 0; j < mat.cols(); ++j) {
      vec[i][j] = mat(i, j);
    }
  }
  return vec;
}

}  // namespace JsonParsing

int main() {
  int n = 1;
  Eigen::setNbThreads(n);
  // infinite loop
  while (true) {
    // send a GET request to the server
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});

    // parse the response
    json data = json::parse(r.text);

    // print the data
    std::cout << data << "\n" << std::endl;

    int identifier = data["identifier"];
    Eigen::MatrixXd a_matrix = JsonParsing::convertDataToEigenMatrix(data["a"]);
    Eigen::MatrixXd b_matrix = JsonParsing::convertDataToEigenMatrix(data["b"]);

    // create a task
    Task task(identifier, a_matrix, b_matrix);

    // do the work
    task.work();

    std::cout << "Task " << identifier << " done!" << std::endl;
    std::cout << "x = " << std::endl;
    std::cout << task.x << std::endl;

    // check if a*x - b = 0
    std::cout << "a*x - b = " << std::endl;
    std::cout << task.a * task.x - task.b << std::endl;

    // concatenate the result with the identifier and a and b
    json result = {
        {"identifier", task.identifier},
        {"a", data["a"]},
        {"b", data["b"]},
        {"x", JsonParsing::convertEigenMatrixToJson(task.x)},
    };

    std::cout << "result = " << std::endl;
    std::cout << result << std::endl;

    // send a POST request to the server
    cpr::Response r2 =
        cpr::Post(cpr::Url{"http://localhost:8000/"}, cpr::Body{result.dump()});

    // sleep for 1 second
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

  return 0;
}

from conans import ConanFile

class StatsdClient(ConanFile):
    name = "statsdclient"
    version = "0.0.2"
    description = "Statsd Client from https://github.com/vthiery/cpp-statsd-client"
    license = "MIT"
    url = "https://github.com/vthiery/conan-statsd-client"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        self.run("git clone --recursive https://github.com/vthiery/cpp-statsd-client")

    def package(self):
        self.copy("*.hpp", dst="include")

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []

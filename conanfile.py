from conans import ConanFile, tools

class StatsdClientConan(ConanFile):
    name = "statsdclient"
    version = "0.0.4"
    description = "A header-only StatsD client implemented in C++ from https://github.com/vthiery/cpp-statsd-client"
    license = "MIT"
    url = "https://github.com/vthiery/conan-statsd-client"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        tools.download("https://github.com/vthiery/cpp-statsd-client/archive/%s.zip" % self.version, "cpp-statsd-client.zip")
        tools.unzip("cpp-statsd-client.zip")

    def package(self):
        zipname = "cpp-statsd-client-%s" % self.version
        self.copy("*.hpp", dst="include", src="%s/src" % zipname)
        self.copy("%s/LICENSE" % zipname)

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []

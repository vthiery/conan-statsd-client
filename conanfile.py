from conans import ConanFile, tools

class StatsdClientConan(ConanFile):
    name = "statsdclient"
    version = "1.0.1"
    description = "A header-only StatsD client implemented in C++ from https://github.com/vthiery/cpp-statsd-client"
    license = "MIT"
    url = "https://github.com/vthiery/conan-statsd-client"
    repo_url = "https://github.com/vthiery/cpp-statsd-client"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = "os"

    def source(self):
        tools.get("%s/archive/%s.zip" % (self.repo_url, self.version))

    def package(self):
        zipname = "cpp-statsd-client-%s" % self.version
        self.copy("*.hpp", dst="include", src="%s/include/cpp-statsd-client" % zipname)
        self.copy("%s/LICENSE.md" % zipname)

    def package_id(self):
        self.info.header_only()

    def configure(self):
        if self.settings.os == "Windows":
            raise Exception("This library only supports Unix like systems")
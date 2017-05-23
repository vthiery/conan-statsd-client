from conans import ConanFile

class StatsdClient(Conanfile):
    name = "statsd-client"
    version = "0.0.1"
    license = "MIT"
    url = "https://github.com/vthiery/conan-statsd-client"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = None

    def source(self):
        self.run("git clone --recursive https://github.com/vthiery/cpp-statsd-client")

    def build(self):
        def self
        # Do nothing - header only

    def package(self):
        header_dir = "include"
        if self.options.path != "":
            header_dir += "/" + str(self.options.path)
        self.copy("*.hpp", dst=header_dir)


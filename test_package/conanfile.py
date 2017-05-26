from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "vthiery")


class RxcppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "statsd-client/0.0.2@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(self, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build(self)

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
from conans import ConanFile, CMake, tools
import os


class SobjectizerConan(ConanFile):
    name = "so5extra"
    version = "1.4.1"

    license = ["GNU Affero GPL v3", "Commercial"]
    url = "https://github.com/Stiffstream/so5extra-conan"

    description = (
            "so_5_extra is a collection of tools built on top of SObjectizer"
    )

    settings = "os", "compiler", "build_type", "arch"

    requires = "sobjectizer/5.7.1@stiffstream/stable", "asio/1.12.2@bincrafters/stable"

    generators = "cmake"

    source_subfolder = "so5extra"

    def source(self):
        source_url = "https://github.com/Stiffstream/so5extra/archive"
        tools.get("{0}//v.{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "so5extra-v." + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['SO5EXTRA_INSTALL'] = True
        cmake.configure(source_folder = self.source_subfolder + "/dev/so_5_extra")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.hpp", dst="include/so_5_extra", src=self.source_subfolder + "/dev/so_5_extra")
        self.copy("license*", src=self.source_subfolder, dst="licenses",  ignore_case=True, keep_path=False)


# so5extra-conan
This is Conan package for [so_5_extra](https://stiffstream.com/en/products/so_5_extra.html) library.

# How To Use

## Installing Via Conan

To use so_5_extra via Conan it is necessary to do the following steps:

1. Add the corresponding remote to your conan:

```bash
conan remote add stiffstream https://api.bintray.com/conan/stiffstream/public
```
It can be also necessary to add _public-conan_ remote:
```bash
conan remote add public-conan https://api.bintray.com/conan/bincrafters/public-conan  
```

2. Add so_5_extra to `conanfile.txt` of your project:
```
[requires]
so5extra/1.2.1@stiffstream/testing
```
It also may be necessary to specify `shared` option for SObjectizer. For example, for build SObjectizer as a static library:
```
[options]
sobjectizer:shared=False
```

3. Install dependencies for your project:
```bash
conan install SOME_PATH --build=missing
```

## Adding so_5_extra To Your CMakeLists.txt

Please note that so_5_extra and SObjectizer should be added to your CMakeLists.txt via `find_package` command:
```cmake
...
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(sobjectizer CONFIG REQUIRED)
find_package(so5extra CONFIG REQUIRED)
...
target_link_libraries(your_target sobjectizer::SharedLib) # Or so_5_extra::StaticLib
target_link_libraries(your_target sobjectizer::so5extra)
```

# Some Notes
If you have any questions about SObjectizer feel free to ask us via `info at stiffstream dot com`.

If you have some problems with SObjectizer or this conan-recipe please open an [issue](https://github.com/Stiffstream/so5extra-conan/issues).


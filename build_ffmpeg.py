import os
import sys
from enum import Enum

# msys2: install toolchain for compile ffmpeg 
# run "msys2 mingw x64"
# pacman -S base-devel
# pacman -S mingw-w64-x86_64-toolchain

class AndroidPlatforms(Enum):
    Unknow = 0
    Arm = 1
    Arm64 = 2
    x86 = 3
    x64 = 4


class WindowsPlatforms(Enum):
    Unknow = 0
    x86 = 1
    x64 = 2
    Arm = 3


def build(ffmpeg_path: str, configure_option: str):
    print(ffmpeg_path)
    print(configure_option)
    os.chdir(ffmpeg_path)
    os.system("make clean")
    os.system("sh ./configure " + configure_option)
    os.system("make")
    os.system("make install")


def build_windows():
    configure_option_list = []

    prefix = "--prefix=/home/Sphinx/ffbuild/ffmepg_windows"
    cross_prefix = "--cross-prefix=x86_64-w64-mingw32-"
    arch = "--arch=x86_64"

    configure_option_list.append(prefix)
    configure_option_list.append(cross_prefix)
    configure_option_list.append(arch)

    configure_option_list.append("--pkg-config-flags=--static")
    configure_option_list.append("--pkg-config=pkg-config")
    configure_option_list.append("--target-os=mingw32")
    configure_option_list.append("--enable-gpl")
    configure_option_list.append("--enable-version3")
    configure_option_list.append("--disable-debug")
    configure_option_list.append("--enable-shared")
    configure_option_list.append("--disable-static")
    configure_option_list.append("--disable-w32threads")
    configure_option_list.append("--enable-pthreads")
    configure_option_list.append("--enable-iconv")
    configure_option_list.append("--enable-libxml2")
    configure_option_list.append("--enable-zlib")
    configure_option_list.append("--enable-libfreetype")
    configure_option_list.append("--enable-libfribidi")
    configure_option_list.append("--enable-gmp")
    configure_option_list.append("--enable-lzma")
    configure_option_list.append("--enable-fontconfig")
    configure_option_list.append("--enable-libvorbis")
    configure_option_list.append("--enable-opencl")
    configure_option_list.append("--disable-libpulse")
    configure_option_list.append("--enable-libvmaf")
    configure_option_list.append("--disable-libxcb")
    configure_option_list.append("--disable-xlib")
    configure_option_list.append("--enable-amf")
    configure_option_list.append("--enable-libaom")
    configure_option_list.append("--enable-avisynth")
    configure_option_list.append("--enable-libdav1d")
    configure_option_list.append("--enable-libdavs2")
    configure_option_list.append("--disable-libfdk-aac")
    configure_option_list.append("--enable-ffnvcodec")
    configure_option_list.append("--enable-cuda-llvm")
    configure_option_list.append("--enable-frei0r")
    configure_option_list.append("--enable-libgme")
    configure_option_list.append("--enable-libass")
    configure_option_list.append("--enable-libbluray")
    configure_option_list.append("--enable-libmp3lame")
    configure_option_list.append("--enable-libopus")
    configure_option_list.append("--enable-librist")
    configure_option_list.append("--enable-libtheora")
    configure_option_list.append("--enable-libvpx")
    configure_option_list.append("--enable-libwebp")
    configure_option_list.append("--enable-lv2")
    configure_option_list.append("--enable-libmfx")
    configure_option_list.append("--enable-libopencore-amrnb")
    configure_option_list.append("--enable-libopencore-amrwb")
    configure_option_list.append("--enable-libopenh264")
    configure_option_list.append("--enable-libopenjpeg")
    configure_option_list.append("--enable-libopenmpt")
    configure_option_list.append("--enable-librav1e")
    configure_option_list.append("--enable-librubberband")
    configure_option_list.append("--enable-schannel")
    configure_option_list.append("--enable-sdl2")
    configure_option_list.append("--enable-libsoxr")
    configure_option_list.append("--enable-libsrt")
    configure_option_list.append("--enable-libsvtav1")
    configure_option_list.append("--enable-libtwolame")
    configure_option_list.append("--enable-libuavs3d")
    configure_option_list.append("--disable-libdrm")
    configure_option_list.append("--disable-vaapi")
    configure_option_list.append("--enable-libvidstab")
    configure_option_list.append("--enable-vulkan")
    configure_option_list.append("--enable-libshaderc")
    configure_option_list.append("--enable-libplacebo")
    configure_option_list.append("--enable-libx264")
    configure_option_list.append("--enable-libx265")
    configure_option_list.append("--enable-libxavs2")
    configure_option_list.append("--enable-libxvid")
    configure_option_list.append("--enable-libzimg")
    configure_option_list.append("--enable-libzvbi")
    configure_option_list.append("--extra-cflags=-DLIBTWOLAME_STATIC")
    configure_option_list.append("--extra-cxxflags=")
    configure_option_list.append("--extra-ldflags=-pthread")
    configure_option_list.append("--extra-ldexeflags=")
    configure_option_list.append("--extra-libs=-lgomp")
    configure_option_list.append("--extra-version=20220129")


def build_android(ffmpeg_path: str, ndk_path: str, platform: AndroidPlatforms, api: int):
    configure_option_list = []

    NDK = ndk_path
    API = api
    SYSROOT = NDK + "/sysroot"
    TOOLCHAIN = NDK + "/toolchains/llvm/prebuilt/windows-x86_64/bin"
    CROSS = ""
    ARCH = ""
    CPU = ""
    TARGET = ""

    if platform == AndroidPlatforms.Arm:
        CROSS = TOOLCHAIN + "/arm-linux-androideabi-"
        ARCH = "arm"
        TARGET = "armv7a-linux-androideabi"
        CPU = "armeabi-v7a"
    elif platform == AndroidPlatforms.Arm64:
        # aarch64-linux-android-    arm-linux-androideabi- i686-linux-android- x86_64-linux-android-
        CROSS = TOOLCHAIN + "/aarch64-linux-android-"
        ARCH = "aarch64"  # arm aarch64 i686 x86_64
        TARGET = "aarch64-linux-android"  # armv7a-linux-androideabi aarch64-linux-android
        CPU = "arm64-v8a"  # armv8-a armv7-a x86_64 x86
    elif platform == AndroidPlatforms.x86:
        CROSS = TOOLCHAIN + "/i686-linux-android-"
        ARCH = "i686"
        TARGET = "i686-linux-android"
        CPU = "x86"
    elif platform == AndroidPlatforms.x64:
        CROSS = TOOLCHAIN + "/x86_64-linux-android-"
        ARCH = "x86_64"
        TARGET = "x86_64-linux-android"
        CPU = "x86_64"
    else:
        pass

    CC = TOOLCHAIN + "/" + TARGET + str(API) + "-clang"
    CXX = TOOLCHAIN + "/" + TARGET + str(API) + "-clang++"
    CFLAG = "\"-D__ANDROID_API__=" + \
        str(API) + " -U_FILE_OFFSET_BITS -DBIONIC_IOCTL_NO_SIGNEDNESS_OVERLOAD -Os -fPIC -DANDROID -D__thumb__ -mthumb -Wfatal-errors -Wno-deprecated -mfloat-abi=softfp -marm\""

    prefix = "--prefix=/home/Sphinx/ffbuild/ffmepg_android/" + CPU
    cross_prefix = "--cross-prefix=" + CROSS
    arch = "--arch=" + ARCH

    configure_option_list.append(prefix)
    configure_option_list.append(cross_prefix)
    configure_option_list.append(arch)
    # configure_option_list.append("--cpu="+CPU)
    # configure_option_list.append("--sysroot=" + SYSROOT)
    configure_option_list.append("--cc="+CC)
    configure_option_list.append("--cxx="+CXX)
    configure_option_list.append("--ld="+CC)
    configure_option_list.append("--extra-cflags="+CFLAG)
    configure_option_list.append("--extra-ldflags=\"-marm\"")
    configure_option_list.append("--target-os=android")
    configure_option_list.append("--enable-cross-compile")
    configure_option_list.append("--disable-x86asm")
    configure_option_list.append("--disable-asm")
    configure_option_list.append("--disable-bsfs")
    configure_option_list.append("--disable-ffmpeg")
    configure_option_list.append("--disable-ffplay")
    configure_option_list.append("--disable-ffprobe")
    configure_option_list.append("--enable-runtime-cpudetect")
    configure_option_list.append("--enable-jni")

    configure_option_list.append("--enable-mediacodec")

    configure_option_list.append("--disable-doc")
    configure_option_list.append("--disable-htmlpages")
    configure_option_list.append("--disable-manpages")
    configure_option_list.append("--disable-podpages")
    configure_option_list.append("--disable-txtpages")

    configure_option_list.append("--pkg-config-flags=--static")
    configure_option_list.append("--pkg-config=pkg-config")
    configure_option_list.append("--enable-gpl")
    configure_option_list.append("--enable-version3")
    configure_option_list.append("--disable-debug")
    configure_option_list.append("--enable-shared")
    configure_option_list.append("--disable-static")
    configure_option_list.append("--disable-w32threads")
    configure_option_list.append("--enable-pthreads")
    # configure_option_list.append("--enable-iconv")
    # configure_option_list.append("--enable-libxml2")
    # configure_option_list.append("--enable-zlib")
    # configure_option_list.append("--enable-libfreetype")
    # configure_option_list.append("--enable-libfribidi")
    # configure_option_list.append("--enable-gmp")
    # configure_option_list.append("--enable-lzma")
    # configure_option_list.append("--enable-fontconfig")
    # configure_option_list.append("--enable-libvorbis")
    # configure_option_list.append("--enable-opencl")
    # configure_option_list.append("--disable-libpulse")
    # configure_option_list.append("--enable-libvmaf")
    # configure_option_list.append("--disable-libxcb")
    # configure_option_list.append("--disable-xlib")
    ### configure_option_list.append("--enable-amf")
    # configure_option_list.append("--enable-libaom")
    # configure_option_list.append("--enable-avisynth")
    # configure_option_list.append("--enable-libdav1d")
    # configure_option_list.append("--enable-libdavs2")
    # configure_option_list.append("--disable-libfdk-aac")
    ### configure_option_list.append("--enable-ffnvcodec")
    ### configure_option_list.append("--enable-cuda-llvm")
    # configure_option_list.append("--enable-frei0r")
    # configure_option_list.append("--enable-libgme")
    # configure_option_list.append("--enable-libass")
    # configure_option_list.append("--enable-libbluray")
    # configure_option_list.append("--enable-libmp3lame")
    # configure_option_list.append("--enable-libopus")
    # configure_option_list.append("--enable-librist")
    # configure_option_list.append("--enable-libtheora")
    # configure_option_list.append("--enable-libvpx")
    # configure_option_list.append("--enable-libwebp")
    # configure_option_list.append("--enable-lv2")
    # configure_option_list.append("--enable-libmfx")
    # configure_option_list.append("--enable-libopencore-amrnb")
    # configure_option_list.append("--enable-libopencore-amrwb")
    # configure_option_list.append("--enable-libopenh264")
    # configure_option_list.append("--enable-libopenjpeg")
    # configure_option_list.append("--enable-libopenmpt")
    # configure_option_list.append("--enable-librav1e")
    # configure_option_list.append("--enable-librubberband")
    # configure_option_list.append("--enable-schannel")
    ### configure_option_list.append("--enable-sdl2")
    # configure_option_list.append("--enable-libsoxr")
    # configure_option_list.append("--enable-libsrt")
    # configure_option_list.append("--enable-libsvtav1")
    # configure_option_list.append("--enable-libtwolame")
    # configure_option_list.append("--enable-libuavs3d")
    # configure_option_list.append("--disable-libdrm")
    # configure_option_list.append("--disable-vaapi")
    # configure_option_list.append("--enable-libvidstab")
    # configure_option_list.append("--enable-vulkan")
    # configure_option_list.append("--enable-libshaderc")
    # configure_option_list.append("--enable-libplacebo")
    # configure_option_list.append("--enable-libx264")
    # configure_option_list.append("--enable-libx265")
    # configure_option_list.append("--enable-libxavs2")
    # configure_option_list.append("--enable-libxvid")
    # configure_option_list.append("--enable-libzimg")
    # configure_option_list.append("--enable-libzvbi")
    # configure_option_list.append("--extra-cxxflags=")
    # configure_option_list.append("--extra-ldexeflags=")
    # configure_option_list.append("--extra-libs=-lgomp")
    configure_option_list.append("--extra-version=20220129")

    build(ffmpeg_path, " ".join(configure_option_list))


if __name__ == "__main__":
    if sys.argv[1] == "windows":
        build_windows()
    elif sys.argv[1] == "android":
        build_android("D:/Development/msys64/home/Sphinx/FFmpeg",
                      "D:/Development/Android/Sdk/ndk/21.4.7075529", AndroidPlatforms.Arm64, 21)
        build_android("D:/Development/msys64/home/Sphinx/FFmpeg",
                      "D:/Development/Android/Sdk/ndk/21.4.7075529", AndroidPlatforms.Arm, 21)
        build_android("D:/Development/msys64/home/Sphinx/FFmpeg",
                      "D:/Development/Android/Sdk/ndk/21.4.7075529", AndroidPlatforms.x64, 21)
        build_android("D:/Development/msys64/home/Sphinx/FFmpeg",
                      "D:/Development/Android/Sdk/ndk/21.4.7075529", AndroidPlatforms.x86, 21)
    else:
        print("build_ffmpeg.py [android]")

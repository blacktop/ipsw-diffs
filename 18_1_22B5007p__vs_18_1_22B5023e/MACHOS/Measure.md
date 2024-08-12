## Measure

> `/private/var/staged_system_apps/Measure.app/Measure`

```diff

-175.0.4.0.0
-  __TEXT.__text: 0x3e56f0
-  __TEXT.__auth_stubs: 0x40f0
+175.0.6.0.0
+  __TEXT.__text: 0x3e54a8
+  __TEXT.__auth_stubs: 0x4160
   __TEXT.__objc_stubs: 0x1220
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x2380
-  __TEXT.__const: 0x1777c
+  __TEXT.__const: 0x1778c
   __TEXT.__objc_classname: 0x431
-  __TEXT.__objc_methname: 0xb3a4
-  __TEXT.__objc_methtype: 0x407b
+  __TEXT.__objc_methname: 0xb3f6
+  __TEXT.__objc_methtype: 0x40b9
   __TEXT.__cstring: 0x225ac
   __TEXT.__gcc_except_tab: 0xff9c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x64c8
-  __TEXT.__swift5_typeref: 0x5c24
+  __TEXT.__swift5_typeref: 0x5c2e
   __TEXT.__swift5_builtin: 0x348
   __TEXT.__swift5_reflstr: 0xa564
   __TEXT.__swift5_fieldmd: 0x7ee4
   __TEXT.__swift5_assocty: 0xce0
-  __TEXT.__swift5_proto: 0x6d4
+  __TEXT.__swift5_proto: 0x6d8
   __TEXT.__swift5_types: 0x5d8
-  __TEXT.__swift5_capture: 0x2304
+  __TEXT.__swift5_capture: 0x2314
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x378
-  __TEXT.__unwind_info: 0xa2a8
+  __TEXT.__unwind_info: 0xa2b0
   __TEXT.__eh_frame: 0x2c48
-  __DATA_CONST.__auth_got: 0x2088
-  __DATA_CONST.__got: 0xf98
-  __DATA_CONST.__auth_ptr: 0x2008
-  __DATA_CONST.__const: 0x17630
+  __DATA_CONST.__auth_got: 0x20c0
+  __DATA_CONST.__got: 0xfa0
+  __DATA_CONST.__auth_ptr: 0x2038
+  __DATA_CONST.__const: 0x176f0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x88

   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x176a0
+  __DATA.__objc_const: 0x176c0
   __DATA.__objc_selrefs: 0x25c0
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x89d8

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11746
-  Symbols:   1892
-  CStrings:  6292
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 11748
+  Symbols:   1908
+  CStrings:  6294
 
Symbols:
+ _$sSS10FoundationE17LocalizationValueV19StringInterpolationV06appendE0_9specifieryx_SStAA18_FormatSpecifiableRzlF
+ _$sSS10FoundationE17LocalizationValueV19StringInterpolationV13appendLiteralyySSF
+ _$sSS10FoundationE17LocalizationValueV19StringInterpolationV15literalCapacity18interpolationCountAESi_SitcfC
+ _$sSS10FoundationE17LocalizationValueV19StringInterpolationVMa
+ _$sSS10FoundationE17LocalizationValueV19stringInterpolationA2C06StringE0V_tcfC
+ _$sSS10FoundationE17LocalizationValueVMa
+ _$sSS10FoundationE9localized5table6bundle6locale7commentS2SAAE17LocalizationValueV_SSSgSo8NSBundleCSgAA6LocaleVs12StaticStringVSgtcfC
+ _$sSi10Foundation18_FormatSpecifiableAAWP
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\nGeneral configuration for OpenCV 3.4.0 =====================================\n  Version control:               unknown\n\n  Platform:\n    Timestamp:                   2024-08-03T20:39:36Z\n    Host:                        Darwin 10.0 x86_64\n    Target:                      Darwin 16.0.0 arm\n    CMake:                       3.26.3\n    CMake generator:             Xcode\n    CMake build tool:            /AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild\n    Xcode:                       16.0\n\n  CPU/HW features:\n    Baseline:                    NEON NEON\n      requested:                 DETECT\n      required:                  NEON\n      disabled:                  VFPV3\n\n  C/C++:\n    Built as dynamic libs?:      NO\n    C++11:                       YES\n    C++ Compiler:                /AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Toolchains/iOS18.1.xctoolchain/usr/bin/clang++  (ver 16.0.0.16000025)\n    C++ flags (Release):         -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG\n    C++ flags (Debug):           -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG\n    C Compiler:                  /AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Toolchains/iOS18.1.xctoolchain/usr/bin/clang\n    C flags (Release):           -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG\n    C flags (Debug):             -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG\n    Linker flags (Release):\n    Linker flags (Debug):\n    ccache:                      NO\n    Precompiled headers:         NO\n    Extra dependencies:          /AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libz.tbd -framework Accelerate -framework CoreGraphics -framework QuartzCore -framework AssetsLibrary -framework UIKit\n    3rdparty dependencies:       libjpeg libpng\n\n  OpenCV modules:\n    To be built:                 core imgcodecs imgproc\n    Disabled:                    -\n    Disabled by dependency:      -\n    Unavailable:                 -\n    Applications:                -\n    Documentation:               NO\n    Non-free algorithms:         NO\n\n  GUI: \n    Cocoa:                       YES\n\n  Media I/O: \n    ZLib:                        /AppleInternal/Library/BuildRoots/18d7d782-50ae-11ef-bff7-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libz.tbd (ver 1.2.12)\n    JPEG:                        build (ver 90)\n    PNG:                         build (ver 1.6.34)\n\n  Video I/O:\n    AVFoundation:                YES\n\n  Parallel framework:            GCD\n\n  Trace:                         YES (built-in)\n\n  Other third-party libraries:\n    Custom HAL:                  NO\n\n  Python (for build):            NO\n\n  Install to:                    /Library/Caches/com.apple.xbs/Binaries/Measure/install/TempContent/Objects/opencv/build/build-iphoneos/install\n-----------------------------------------------------------------\n\n"
+ "@\"NSArray\"40@0:8@\"UITabBarController\"16@\"UITab\"24@\"NSArray\"32"
+ "localizedStringWithFormat:"
+ "tabBarController:displayedViewControllersForTab:proposedViewControllers:"
- "\nGeneral configuration for OpenCV 3.4.0 =====================================\n  Version control:               unknown\n\n  Platform:\n    Timestamp:                   2024-07-13T04:33:10Z\n    Host:                        Darwin 10.0 x86_64\n    Target:                      Darwin 16.0.0 arm\n    CMake:                       3.26.3\n    CMake generator:             Xcode\n    CMake build tool:            /AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild\n    Xcode:                       16.0\n\n  CPU/HW features:\n    Baseline:                    NEON NEON\n      requested:                 DETECT\n      required:                  NEON\n      disabled:                  VFPV3\n\n  C/C++:\n    Built as dynamic libs?:      NO\n    C++11:                       YES\n    C++ Compiler:                /AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Toolchains/iOS18.1.xctoolchain/usr/bin/clang++  (ver 16.0.0.16000022)\n    C++ flags (Release):         -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG\n    C++ flags (Debug):           -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG\n    C Compiler:                  /AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Toolchains/iOS18.1.xctoolchain/usr/bin/clang\n    C flags (Release):           -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG\n    C flags (Debug):             -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks' -isysroot'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk' -F'/AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks'   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -Qunused-arguments -Wno-semicolon-before-method-body  -mfpu=neon -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG\n    Linker flags (Release):\n    Linker flags (Debug):\n    ccache:                      NO\n    Precompiled headers:         NO\n    Extra dependencies:          /AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libz.tbd -framework Accelerate -framework CoreGraphics -framework QuartzCore -framework AssetsLibrary -framework UIKit\n    3rdparty dependencies:       libjpeg libpng\n\n  OpenCV modules:\n    To be built:                 core imgcodecs imgproc\n    Disabled:                    -\n    Disabled by dependency:      -\n    Unavailable:                 -\n    Applications:                -\n    Documentation:               NO\n    Non-free algorithms:         NO\n\n  GUI: \n    Cocoa:                       YES\n\n  Media I/O: \n    ZLib:                        /AppleInternal/Library/BuildRoots/8808857c-3f9c-11ef-8de3-b60714381f84/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libz.tbd (ver 1.2.12)\n    JPEG:                        build (ver 90)\n    PNG:                         build (ver 1.6.34)\n\n  Video I/O:\n    AVFoundation:                YES\n\n  Parallel framework:            GCD\n\n  Trace:                         YES (built-in)\n\n  Other third-party libraries:\n    Custom HAL:                  NO\n\n  Python (for build):            NO\n\n  Install to:                    /Library/Caches/com.apple.xbs/Binaries/Measure/install/TempContent/Objects/opencv/build/build-iphoneos/install\n-----------------------------------------------------------------\n\n"
- "stringWithFormat:"

```

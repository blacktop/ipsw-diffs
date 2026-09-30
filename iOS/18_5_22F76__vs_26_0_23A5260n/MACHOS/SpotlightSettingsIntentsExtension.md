## SpotlightSettingsIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightSettingsIntentsExtension.appex/SpotlightSettingsIntentsExtension`

```diff

-120.4.6.0.0
-  __TEXT.__text: 0x39d4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0x96a
+163.1.0.0.0
+  __TEXT.__text: 0x39d0
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__const: 0x9d8
   __TEXT.__cstring: 0x229
   __TEXT.__swift5_typeref: 0x349
   __TEXT.__swift5_reflstr: 0xa4

   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x480
-  __DATA_CONST.__const: 0x2f8
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__eh_frame: 0x218
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x488
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x188
   __DATA.__common: 0x30
   __DATA.__bss: 0x1008
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E964B8A2-5C6A-3F27-BFE0-9DEAB4D69687
+  UUID: 09D4278F-AF6C-3603-B6D2-8FF2A9B099C6
   Functions: 158
-  Symbols:   52
+  Symbols:   51
   CStrings:  16
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_100001488 -> sub_100001438 : 100 -> 64
~ sub_100002fd0 -> sub_100002f5c : 92 -> 116
~ sub_1000033c4 -> sub_100003368 : 204 -> 4
~ sub_100003490 -> sub_10000336c : 264 -> 204
~ sub_100003598 -> sub_100003438 : 40 -> 264
~ sub_1000035c0 -> sub_100003540 : 60 -> 40
~ sub_1000035fc -> sub_100003568 : 16 -> 60
~ sub_10000363c -> sub_1000035d4 : 4 -> 16
~ sub_100003644 -> sub_1000035e8 : 80 -> 4
~ sub_100003694 -> sub_1000035ec : 124 -> 80
~ sub_100003710 -> sub_10000363c : 16 -> 124
~ sub_100003720 -> sub_1000036b8 : 40 -> 16
~ sub_100003770 -> sub_1000036f0 : 232 -> 40
~ sub_100003858 -> sub_100003718 : 28 -> 232
~ sub_100003874 -> sub_100003800 : 280 -> 28
~ sub_10000398c -> sub_10000381c : 188 -> 312
~ sub_100003a68 -> sub_100003974 : 292 -> 388
~ sub_100003ba8 -> sub_100003b14 : 128 -> 192
CStrings:
+ "com.apple.Spotlight"
- "com.apple.graphic-icon.search"

```

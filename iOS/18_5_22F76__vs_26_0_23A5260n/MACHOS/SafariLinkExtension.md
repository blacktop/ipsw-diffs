## SafariLinkExtension

> `/private/var/staged_system_apps/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension`

```diff

-7621.2.5.10.10
+7622.1.14.10.4
   __TEXT.__text: 0x1b8
   __TEXT.__auth_stubs: 0x60
   __TEXT.__swift5_typeref: 0x46

   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x100

   - /System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
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
-  UUID: E7157245-D282-32EF-AC39-CA75A49A3478
+  UUID: 8DF0E6A2-1B51-32F4-A190-08B77836E9F2
   Functions: 8
-  Symbols:   29
+  Symbols:   27
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```

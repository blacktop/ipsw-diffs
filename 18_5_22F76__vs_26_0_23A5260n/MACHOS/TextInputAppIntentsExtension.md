## TextInputAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension`

```diff

-3479.503.100.0.0
+3504.100.0.0.0
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

   - /System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore
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
-  UUID: 77CB0E1F-F04D-3655-AFFD-14F456D4CBD9
+  UUID: 46074177-8D6D-3C99-BCD5-5D394863908E
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

## GamePolicy

> `/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`

```diff

-2.0.23.0.0
+2.0.25.0.0
   __TEXT.__text: 0x1968c
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_methlist: 0x784

   __TEXT.__objc_methtype: 0x5f
   __TEXT.__objc_stubs: 0x340
   __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x17e0
   __AUTH.__data: 0x5c0
   __DATA.__data: 0x538
-  __DATA.__bss: 0x1000
+  __DATA.__bss: 0xff0
   __DATA.__common: 0x200
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 913
-  Symbols:   199
+  Symbols:   207
   CStrings:  263
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```

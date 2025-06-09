## ControlCenterAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ControlCenterAppIntentsExtension.appex/ControlCenterAppIntentsExtension`

```diff

-600.5.3.100.0
-  __TEXT.__text: 0x31dc
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x2ac
+645.102.0.0.0
+  __TEXT.__text: 0x3208
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__const: 0x718
+  __TEXT.__cstring: 0x2bc
   __TEXT.__swift5_typeref: 0x320
   __TEXT.__swift5_reflstr: 0xb3
   __TEXT.__swift5_assocty: 0xc0

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x1c8
   __TEXT.__eh_frame: 0x78
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0x3c0
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x190
+  __DATA.__data: 0x180
   __DATA.__common: 0x50
   __DATA.__bss: 0xc10
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
-  UUID: 16D9254E-A431-3526-B73E-372DDA52181C
+  UUID: A1783B4C-9707-39B3-A5EF-94061F3BAE56
   Functions: 123
-  Symbols:   49
+  Symbols:   51
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_arrayDestroy
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "com.apple.graphic-icon.control-center"
- "Settings → Control Center"

```

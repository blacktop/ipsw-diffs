## soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

-340.138.0.0.0
+400.178.0.0.0
   __TEXT.__text: 0x400
   __TEXT.__auth_stubs: 0xa0
-  __TEXT.__const: 0x42
+  __TEXT.__const: 0x52
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8

   __TEXT.__eh_frame: 0x40
   __DATA_CONST.__auth_got: 0x50
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

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
-  UUID: 5DBBFECA-EE64-3DCC-BE51-4D03B61B224D
+  UUID: C07C6B65-40CC-3BE9-8616-1326873E541F
   Functions: 8
-  Symbols:   35
+  Symbols:   33
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftMLCompute
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

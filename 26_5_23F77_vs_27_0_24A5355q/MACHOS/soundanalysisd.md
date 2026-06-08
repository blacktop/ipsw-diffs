## soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

-440.51.0.0.0
+500.151.0.0.0
   __TEXT.__text: 0x484
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__const: 0x52
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x8
   __TEXT.__unwind_info: 0x70
   __TEXT.__eh_frame: 0x40
+  __DATA_CONST.__const: 0x80
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x88
-  __DATA_CONST.__objc_imageinfo: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 466F78FB-B229-3450-98EC-AF6574724A0A
+  UUID: 65A18F06-1BBE-3CE4-8071-85AAA99BF4D5
   Functions: 8
-  Symbols:   31
+  Symbols:   30
   CStrings:  0
 
Symbols:
+ _swift_release_x8
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _swift_release

```

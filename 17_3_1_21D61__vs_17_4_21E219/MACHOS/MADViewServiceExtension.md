## MADViewServiceExtension

> `/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension`

```diff

-1.2.22.0.0
-  __TEXT.__text: 0x648c
-  __TEXT.__auth_stubs: 0x890
+1.4.3.0.0
+  __TEXT.__text: 0x6668
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x344
   __TEXT.__constg_swiftt: 0x170

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x18
-  __TEXT.__cstring: 0x173
+  __TEXT.__cstring: 0x403
   __TEXT.__objc_methname: 0xd3
-  __TEXT.__unwind_info: 0x1e4
+  __TEXT.__unwind_info: 0x1f0
   __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x30
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x60
-  __DATA.__objc_classrefs: 0x30
   __DATA.__data: 0x330
   __DATA.__bss: 0x320
   __DATA.__common: 0x30

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 493136B9-F34E-3166-90EC-5742C323BB62
-  Functions: 127
-  Symbols:   96
-  CStrings:  18
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 49D400DE-9CE7-38CD-A93A-DC6192EDD279
+  Functions: 128
+  Symbols:   99
+  CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_release_x19
+ _objc_retain_x26
- _objc_retain_x21
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```

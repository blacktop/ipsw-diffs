## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-677.3.6.0.0
-  __TEXT.__text: 0x1935c
-  __TEXT.__auth_stubs: 0xe40
+677.4.10.0.0
+  __TEXT.__text: 0x198ac
+  __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0xec
-  __TEXT.__cstring: 0xb29
-  __TEXT.__objc_methname: 0x5a8
+  __TEXT.__cstring: 0xe49
+  __TEXT.__objc_methname: 0x5bc
   __TEXT.__objc_classname: 0x45
   __TEXT.__objc_methtype: 0xce
   __TEXT.__const: 0x7f8

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_capture: 0x268
   __TEXT.__swift5_proto: 0x18
-  __TEXT.__unwind_info: 0x4d4
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__eh_frame: 0x98
-  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xf18

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x58
   __DATA.__objc_const: 0x970
   __DATA.__objc_selrefs: 0x1c8
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x58
   __DATA.__objc_data: 0x368
-  __DATA.__data: 0xe70
+  __DATA.__data: 0xd30
   __DATA.__common: 0x28
   __DATA.__bss: 0x400
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7717A679-ADDE-366F-9625-7C8237878B53
-  Functions: 483
+  UUID: 0DB84964-919E-322A-AD16-C926638191FB
+  Functions: 489
   Symbols:   135
-  CStrings:  195
+  CStrings:  213
 
Symbols:
+ _objc_retain_x2
+ _swift_initStackObject
- _objc_retain_x22
- _swift_release_n
CStrings:
+ "Can't construct Array with count < 0"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```

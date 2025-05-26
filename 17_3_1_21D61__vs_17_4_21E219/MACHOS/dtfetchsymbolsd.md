## dtfetchsymbolsd

> `/usr/libexec/dtfetchsymbolsd`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0x5cb8
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__const: 0x1ee
-  __TEXT.__cstring: 0x299
+33.0.0.0.0
+  __TEXT.__text: 0x6458
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__const: 0x1fe
+  __TEXT.__cstring: 0x530
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x68

   __TEXT.__swift5_reflstr: 0x16
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x16c
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_classrefs: 0x8
-  __DATA.__data: 0x148
-  __DATA.__common: 0x70
-  __DATA.__bss: 0x3b0
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA.__data: 0xc0
+  __DATA.__common: 0xc0
+  __DATA.__bss: 0x3e0
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Mercury.framework/Mercury
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 115
-  Symbols:   181
-  CStrings:  19
+  Functions: 125
+  Symbols:   185
+  CStrings:  33
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _objc_release_x26
+ _swift_initStackObject
+ _swift_once
- _objc_release_x25
- _swift_initStaticObject
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

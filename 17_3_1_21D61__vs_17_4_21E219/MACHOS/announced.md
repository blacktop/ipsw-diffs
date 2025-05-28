## announced

> `/usr/libexec/announced`

```diff

-217.30.3.0.0
-  __TEXT.__text: 0xf58
-  __TEXT.__auth_stubs: 0x350
+217.40.9.0.0
+  __TEXT.__text: 0x122c
+  __TEXT.__auth_stubs: 0x380
   __TEXT.__const: 0x42
-  __TEXT.__cstring: 0x1b4
+  __TEXT.__cstring: 0x450
   __TEXT.__objc_methname: 0x77
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x1a8
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x18
   __DATA.__objc_selrefs: 0x38
-  __DATA.__objc_classrefs: 0x18
   __DATA.__data: 0x18
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Announce.framework/Announce

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20
-  Symbols:   96
-  CStrings:  18
+  Functions: 21
+  Symbols:   99
+  CStrings:  32
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _objc_retain_x19
- _objc_retain_x8
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

## appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

-23.2.0.0.0
-  __TEXT.__text: 0xa180
-  __TEXT.__auth_stubs: 0x8c0
+23.4.0.0.0
+  __TEXT.__text: 0xa700
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_methlist: 0xcc
   __TEXT.__const: 0x2f4
-  __TEXT.__objc_methname: 0x487
-  __TEXT.__cstring: 0xb05
+  __TEXT.__cstring: 0xe05
+  __TEXT.__objc_methname: 0x49a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1c4
   __TEXT.__swift5_typeref: 0x218

   __TEXT.__objc_methtype: 0x19e
   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __TEXT.__eh_frame: 0x9c0
-  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x540

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x58
   __DATA.__objc_const: 0xa60
   __DATA.__objc_selrefs: 0x110
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x58
   __DATA.__objc_data: 0x290
   __DATA.__data: 0x530
   __DATA.__bss: 0x300

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 412CF084-6BF2-37B7-BDF0-8710645EF7B2
-  Functions: 207
-  Symbols:   240
-  CStrings:  144
+  UUID: 66667688-DA54-393E-B46B-216E03631064
+  Functions: 208
+  Symbols:   243
+  CStrings:  160
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _objc_retain_x2
- _objc_release_x28
CStrings:
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```

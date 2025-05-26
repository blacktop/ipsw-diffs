## icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

-2023.4.1.0.0
-  __TEXT.__text: 0x22ec0
-  __TEXT.__auth_stubs: 0xed0
+2023.5.3.0.0
+  __TEXT.__text: 0x24a10
+  __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x358
-  __TEXT.__const: 0x5fa
+  __TEXT.__const: 0x60a
   __TEXT.__oslogstring: 0x46
-  __TEXT.__cstring: 0x285d
-  __TEXT.__swift5_typeref: 0x5de
-  __TEXT.__objc_methname: 0xfbb
+  __TEXT.__cstring: 0x2c30
+  __TEXT.__swift5_typeref: 0x5d4
+  __TEXT.__objc_methname: 0xfcf
   __TEXT.__constg_swiftt: 0x604
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x44

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__objc_classname: 0x36
   __TEXT.__objc_methtype: 0x2dd
-  __TEXT.__unwind_info: 0x678
-  __TEXT.__eh_frame: 0x8d0
-  __DATA_CONST.__auth_got: 0x770
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__eh_frame: 0x8f8
+  __DATA_CONST.__auth_got: 0x780
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0xc58
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0xc8
   __DATA.__objc_const: 0xc88
   __DATA.__objc_selrefs: 0x418
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xc8
   __DATA.__objc_data: 0xa88
-  __DATA.__data: 0x940
+  __DATA.__data: 0x990
+  __DATA.__common: 0x150
   __DATA.__bss: 0x480
-  __DATA.__common: 0x70
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 515
-  Symbols:   396
-  CStrings:  416
+  Functions: 554
+  Symbols:   399
+  CStrings:  437
 
Symbols:
+ _$sSs8UTF8ViewVys5UInt8VSS5IndexVcig
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ __swift_FORCE_LOAD_$_swiftAccelerate
- _objc_retain_x10
- _objc_retain_x11
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Integers.swift"
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
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```

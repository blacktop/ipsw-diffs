## NewsKit

> `/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit`

```diff

-5325.6.0.0.0
-  __TEXT.__text: 0x1c204
-  __TEXT.__auth_stubs: 0x1210
+5345.2.0.0.0
+  __TEXT.__text: 0x1c4e4
+  __TEXT.__auth_stubs: 0x1200
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0x17cc
-  __TEXT.__cstring: 0x9ff
+  __TEXT.__const: 0x18bc
+  __TEXT.__cstring: 0xd1f
   __TEXT.__constg_swiftt: 0x900
   __TEXT.__swift5_typeref: 0x434
   __TEXT.__swift5_fieldmd: 0x628

   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8c4
+  __TEXT.__unwind_info: 0x898
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x2b14
+  __TEXT.__objc_methname: 0x2c0d
   __TEXT.__objc_methtype: 0x120d
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4d30
   __DATA_CONST.__objc_selrefs: 0x2f8
-  __AUTH_CONST.__const: 0x1358
+  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_classrefs: 0xd0
+  __AUTH_CONST.__const: 0x1350
   __AUTH_CONST.__auth_ptr: 0x78
   __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__auth_got: 0x900
   __AUTH.__data: 0x710
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0xd0
   __DATA.__data: 0xce0
   __DATA.__bss: 0x2200
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftShazamKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVision.dylib
   - /usr/lib/swift/libswiftWebKit.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 829
-  Symbols:   589
-  CStrings:  720
+  Functions: 835
+  Symbols:   587
+  CStrings:  749
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftShazamKit
+ __swift_FORCE_LOAD_$_swiftShazamKit_$_NewsKit
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x1
- _objc_retain_x27
CStrings:
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<FCChannelProviding>\",?,R,C,N"
+ "T@\"<FCHeadlineMetadata>\",?,R,C,N"
+ "T@\"<FCHeadlineStocksFields>\",?,R,N"
+ "T@\"<FCNewsAppConfiguration>\",?,R,N"
+ "T@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\",?,R,N"
+ "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\",?,R,N"
+ "T@\"FCArticleAudioTrack\",?,R,N"
+ "T@\"FCAssetHandle\",?,R,N"
+ "T@\"FCColor\",?,R,N"
+ "T@\"FCHeadlineExperimentalTitleMetadata\",?,R,C,N"
+ "T@\"FCIssue\",?,R,C,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSData\",?,R,N"
+ "T@\"NSDate\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisBundlePaid"
+ "TB,?,R,N,GisIssueOnly"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "Tq,?,R,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
- "T@\"<FCHeadlineMetadata>\",R,C,N"
- "T@\"<FCHeadlineStocksFields>\",R,N"
- "T@\"<FCNewsAppConfiguration><FCJSONEncodableObjectProviding>\",R,N"
- "T@\"COMAPPLEFELDSPARPROTOCOLLIVERPOOLArticleContentExpiration\",R,N"
- "T@\"FCArticleAudioTrack\",R,N"
- "T@\"FCColor\",R,N"
- "T@\"FCHeadlineExperimentalTitleMetadata\",R,C,N"
- "T@\"FCIssue\",R,C,N"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",R,N"
- "TB,R,N,GisBundlePaid"
- "TB,R,N,GisIssueOnly"

```

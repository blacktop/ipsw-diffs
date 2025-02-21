## TrustKit

> `/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit`

```diff

-9.3.0.0.0
-  __TEXT.__text: 0xe2d0
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__const: 0x89c
-  __TEXT.__constg_swiftt: 0x470
-  __TEXT.__swift5_typeref: 0x2a0
+12.6.0.0.0
+  __TEXT.__text: 0x13980
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__const: 0xd48
+  __TEXT.__cstring: 0x132c
+  __TEXT.__constg_swiftt: 0x570
+  __TEXT.__swift5_typeref: 0x38c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_reflstr: 0x234
-  __TEXT.__swift5_fieldmd: 0x314
-  __TEXT.__swift5_proto: 0x58
-  __TEXT.__swift5_types: 0x50
-  __TEXT.__cstring: 0x125c
-  __TEXT.__swift5_capture: 0x2c
+  __TEXT.__swift5_reflstr: 0x2d4
+  __TEXT.__swift5_fieldmd: 0x410
+  __TEXT.__swift5_proto: 0x88
+  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift5_capture: 0x54
+  __TEXT.__swift5_assocty: 0x18
   __TEXT.__oslogstring: 0x13
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__eh_frame: 0x5c8
-  __TEXT.__objc_methname: 0x78
-  __DATA_CONST.__got: 0x160
+  __TEXT.__unwind_info: 0x580
+  __TEXT.__eh_frame: 0xaa0
+  __TEXT.__objc_methname: 0xbc
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x80
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__auth_ptr: 0x258
-  __AUTH_CONST.__const: 0x6b8
-  __AUTH_CONST.__objc_const: 0x4d8
-  __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0x4c0
-  __DATA.__data: 0x418
-  __DATA.__bss: 0x880
-  __DATA.__common: 0x120
+  __DATA_CONST.__objc_selrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_ptr: 0x250
+  __AUTH_CONST.__const: 0xa48
+  __AUTH_CONST.__objc_const: 0x618
+  __AUTH.__objc_data: 0x2d0
+  __AUTH.__data: 0x618
+  __DATA.__data: 0x460
+  __DATA.__bss: 0xd80
+  __DATA.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 319
-  Symbols:   164
-  CStrings:  111
+  Functions: 410
+  Symbols:   182
+  CStrings:  117
 
Symbols:
+ _DeviceIdentityCreateHostSignatureWithCompletion
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_isVirtualDevice
+ _OBJC_CLASS_$_NSJSONSerialization
+ __swiftImmortalRefCount
+ _objc_retain_x22
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _objc_retain_x28
- _swift_setDeallocating
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Interfaces/TKReportService.swift"
+ "/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportOperation.swift"
+ "Attestation is not supported."
+ "Created report for encoding. { encodingReport="
+ "Device not supported."
+ "Failed to create host signature, attestation manager not available."
+ "Failed to generate host signature."
+ "Failed to generate host signature. { error="
+ "Invalid key in report. { expectedKey=[spam-messages, spamMessages] }"
+ "Invalid type and content."
+ "JSONObjectWithData:options:error:"
+ "Submitted report. { type="
+ "_TtC8TrustKit15ReportOperation"
+ "_TtC8TrustKit15TKReportService"
+ "baaCertChain"
+ "dataWithJSONObject:options:error:"
+ "hostSignature(for:)"
+ "https://concernreports-qa.g.apple.com/v2/report/report_junk"
+ "https://concernreports.apple.com/v2/report/report_junk"
+ "report"
+ "reportNetworkManager"
+ "v32@?0@\"NSData\"8@\"NSArray\"16@\"NSError\"24"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```

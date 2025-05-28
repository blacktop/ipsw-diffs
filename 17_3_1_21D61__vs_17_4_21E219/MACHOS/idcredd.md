## idcredd

> `/usr/libexec/idcredd`

```diff

-6.300.0.0.0
-  __TEXT.__text: 0xdea0c
-  __TEXT.__auth_stubs: 0x3010
+6.406.0.0.0
+  __TEXT.__text: 0xe4670
+  __TEXT.__auth_stubs: 0x3060
   __TEXT.__objc_methlist: 0x358
-  __TEXT.__const: 0x1b50
-  __TEXT.__cstring: 0x11071
-  __TEXT.__objc_methname: 0x1b78
+  __TEXT.__const: 0x1b40
+  __TEXT.__cstring: 0x114f1
+  __TEXT.__objc_methname: 0x1bdb
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1e88
-  __TEXT.__swift5_typeref: 0x1220
+  __TEXT.__constg_swiftt: 0x1e98
+  __TEXT.__swift5_typeref: 0x1264
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xd63
+  __TEXT.__swift5_reflstr: 0xd73
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_fieldmd: 0xd48
   __TEXT.__swift5_proto: 0xd8

   __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methtype: 0x9d9
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_capture: 0x764
-  __TEXT.__unwind_info: 0x1b90
-  __TEXT.__eh_frame: 0x5190
-  __DATA_CONST.__auth_got: 0x1808
+  __TEXT.__swift5_capture: 0x768
+  __TEXT.__unwind_info: 0x1ba4
+  __TEXT.__eh_frame: 0x51b8
+  __DATA_CONST.__auth_got: 0x1830
   __DATA_CONST.__got: 0xd18
-  __DATA_CONST.__auth_ptr: 0x1a0
-  __DATA_CONST.__const: 0x2248
+  __DATA_CONST.__auth_ptr: 0x1a8
+  __DATA_CONST.__const: 0x2230
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x130
+  __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_const: 0x2a30
-  __DATA.__objc_selrefs: 0x7d8
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x128
+  __DATA.__objc_selrefs: 0x7e8
   __DATA.__objc_data: 0xa20
-  __DATA.__data: 0x3c88
-  __DATA.__common: 0xb8
+  __DATA.__data: 0x3bb8
+  __DATA.__common: 0x90
   __DATA.__bss: 0x1510
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred
   - /System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1859
-  Symbols:   1333
-  CStrings:  1583
+  Functions: 1878
+  Symbols:   1336
+  CStrings:  1609
 
Symbols:
+ _$s13CoreIDVShared13IDCSAnalyticsC28sendPayloadPortraitSizeEvent7docType6issuer08portraitG5BytesySS_SSSgSitFZ
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _OBJC_CLASS_$_DCPresentmentProposalReaderAnalytics
+ _SecCertificateCreateWithData
+ __linkguard_init
+ _objc_retain_x2
- _$sSK17_StringProcessingSs11SubSequenceRtzrlE7matches2ofSayAA5RegexV5MatchVyqd___GGqd_0__t0G6OutputQyd_0_Rsd__AA0G9ComponentRd_0_r0_lF
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftUIKit
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CoreIDV/idcredd/crypto/CertificateSubjectDistinguishedNames.swift"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Extracted reader analytics from certificate: "
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
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
+ "buildProposal(for:itemsRequest:requiredPublicKeyIdentifier:sessionReaderAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:context:knownIssuer:)"
+ "findProposals(itemsRequest:requiredPublicKeyIdentifier:readerAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:knownIssuer:)"
+ "init(certificate:)"
+ "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:"
+ "initWithUntrustedIdentifier:untrustedOrganization:"
+ "invalid Collection: less than 'count' elements in collection"
+ "organization"
- "buildProposal(for:itemsRequest:requiredPublicKeyIdentifier:sessionReaderAuthenticationPolicy:readerAuthCertificateData:readerMetadata:context:knownIssuer:)"
- "extractSubjectDistinguishedNames(from:)"
- "findProposals(itemsRequest:requiredPublicKeyIdentifier:readerAuthenticationPolicy:readerAuthCertificateData:readerMetadata:knownIssuer:)"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:"

```

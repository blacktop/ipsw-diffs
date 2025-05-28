## CoreIDV

> `/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV`

```diff

-6.300.0.0.0
-  __TEXT.__text: 0x8cd24
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x1f60
-  __TEXT.__const: 0x8688
+6.406.0.0.0
+  __TEXT.__text: 0x8c7a0
+  __TEXT.__auth_stubs: 0x11d0
+  __TEXT.__objc_methlist: 0x1f78
+  __TEXT.__const: 0x8698
   __TEXT.__oslogstring: 0x454
-  __TEXT.__cstring: 0x3a4f
+  __TEXT.__cstring: 0x3d1f
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__ustring: 0x8
   __TEXT.__swift5_typeref: 0x23ac
   __TEXT.__constg_swiftt: 0x1afc
-  __TEXT.__swift5_reflstr: 0xc62
+  __TEXT.__swift5_reflstr: 0xc72
   __TEXT.__swift5_fieldmd: 0x1a30
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x1c8

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_capture: 0x544
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x35fc
-  __TEXT.__eh_frame: 0x4318
+  __TEXT.__unwind_info: 0x3488
+  __TEXT.__eh_frame: 0x41e8
   __TEXT.__objc_classname: 0x377
-  __TEXT.__objc_methname: 0x3622
+  __TEXT.__objc_methname: 0x36a2
   __TEXT.__objc_methtype: 0x610
   __TEXT.__objc_stubs: 0x14e0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x6b0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3898
-  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_const: 0x38c8
+  __DATA_CONST.__objc_selrefs: 0xcc0
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__const: 0x27d0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__const: 0x2770
   __AUTH_CONST.__auth_ptr: 0xc8
-  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_got: 0x8f8
   __AUTH.__data: 0x158
   __AUTH.__objc_data: 0x180
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x188
-  __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x230
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x2470
+  __DATA.__data: 0x2370
   __DATA.__bss: 0x10fa0
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__const: 0x29d8
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__const: 0x2990
   __DATA_DIRTY.__objc_const: 0x14d0
   __DATA_DIRTY.__objc_data: 0x17d8
-  __DATA_DIRTY.__data: 0xdf0
+  __DATA_DIRTY.__data: 0xe00
   __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4913
-  Symbols:   3201
-  CStrings:  1270
+  Functions: 4867
+  Symbols:   3205
+  CStrings:  1289
 
Symbols:
+ -[DIIdentityRequest merchantNameOverride]
+ -[DIIdentityRequest setMerchantNameOverride:]
+ _OBJC_IVAR_$_DIIdentityRequest._merchantNameOverride
+ __PROTOCOLS__TtC7CoreIDV13XPCAuditToken.44
+ __PROTOCOLS__TtC7CoreIDV30XPCMobileDocumentReaderRequest.26
+ __PROTOCOLS__TtC7CoreIDV31XPCMobileDocumentReaderMerchant.20
+ __PROTOCOLS__TtC7CoreIDV31XPCMobileDocumentReaderResponse.38
+ __PROTOCOLS__TtC7CoreIDV35XPCMobileDocumentReaderSessionState.2
+ __PROTOCOLS__TtC7CoreIDV36XPCMobileDocumentReaderConfiguration.8
+ __PROTOCOLS__TtC7CoreIDV41XPCMobileDocumentReaderCertificateRequest.56
+ __PROTOCOLS__TtC7CoreIDV41XPCMobileDocumentReaderIdentityKeyRequest.50
+ __PROTOCOLS__TtC7CoreIDV42XPCMobileDocumentReaderCertificateResponse.68
+ __PROTOCOLS__TtC7CoreIDV42XPCMobileDocumentReaderIdentityKeyResponse.62
+ __PROTOCOLS__TtC7CoreIDV43XPCMobileDocumentReaderDeviceEngagementType.32
+ __PROTOCOLS__TtC7CoreIDV44XPCMobileDocumentReaderConfigurationResponse.14
+ __PROTOCOLS__TtC7CoreIDV48XPCMobileDocumentReaderIssuerRootCertificateList.74
+ ___17-[DIVClient init]_block_invoke.82
+ ___17-[DIVClient init]_block_invoke.82.cold.1
+ ___block_literal_global.112
+ ___block_literal_global.116
+ ___block_literal_global.85
- __PROTOCOLS__TtC7CoreIDV13XPCAuditToken.92
- __PROTOCOLS__TtC7CoreIDV30XPCMobileDocumentReaderRequest.70
- __PROTOCOLS__TtC7CoreIDV31XPCMobileDocumentReaderMerchant.63
- __PROTOCOLS__TtC7CoreIDV31XPCMobileDocumentReaderResponse.84
- __PROTOCOLS__TtC7CoreIDV35XPCMobileDocumentReaderSessionState.40
- __PROTOCOLS__TtC7CoreIDV36XPCMobileDocumentReaderConfiguration.48
- __PROTOCOLS__TtC7CoreIDV41XPCMobileDocumentReaderCertificateRequest.107
- __PROTOCOLS__TtC7CoreIDV41XPCMobileDocumentReaderIdentityKeyRequest.99
- __PROTOCOLS__TtC7CoreIDV42XPCMobileDocumentReaderCertificateResponse.122
- __PROTOCOLS__TtC7CoreIDV42XPCMobileDocumentReaderIdentityKeyResponse.115
- __PROTOCOLS__TtC7CoreIDV43XPCMobileDocumentReaderDeviceEngagementType.77
- __PROTOCOLS__TtC7CoreIDV44XPCMobileDocumentReaderConfigurationResponse.55
- __PROTOCOLS__TtC7CoreIDV48XPCMobileDocumentReaderIssuerRootCertificateList.129
- ___17-[DIVClient init]_block_invoke.81
- ___17-[DIVClient init]_block_invoke.81.cold.1
- ___block_literal_global.111
- ___block_literal_global.115
- ___block_literal_global.84
- _objc_retain_x28
CStrings:
+ "\x05"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_merchantNameOverride"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_merchantNameOverride"
+ "invalid Collection: less than 'count' elements in collection"
+ "merchantNameOverride"
+ "setMerchantNameOverride:"
- "\x04"

```

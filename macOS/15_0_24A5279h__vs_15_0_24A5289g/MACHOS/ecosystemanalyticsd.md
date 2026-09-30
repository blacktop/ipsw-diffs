## ecosystemanalyticsd

> `/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0x77e8
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__const: 0x1be
+26.0.0.0.0
+  __TEXT.__text: 0x6ecc
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__const: 0x104
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x1223
-  __TEXT.__constg_swiftt: 0x16c
-  __TEXT.__swift5_typeref: 0x139
+  __TEXT.__cstring: 0x1383
+  __TEXT.__constg_swiftt: 0x160
+  __TEXT.__swift5_typeref: 0x10c
   __TEXT.__swift5_reflstr: 0xe4
   __TEXT.__swift5_fieldmd: 0x8c
-  __TEXT.__oslogstring: 0x286
+  __TEXT.__oslogstring: 0x246
   __TEXT.__swift5_capture: 0x10c
   __TEXT.__objc_methname: 0x196
-  __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methtype: 0xad
   __TEXT.__info_plist: 0x43b
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0xa8
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__eh_frame: 0x40
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x460
   __DATA.__objc_selrefs: 0x28
-  __DATA.__data: 0x3a0
-  __DATA.__bss: 0x180
-  __DATA.__common: 0x50
+  __DATA.__data: 0x370
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 117
-  Symbols:   223
-  CStrings:  84
+  Functions: 102
+  Symbols:   202
+  CStrings:  90
 
Symbols:
+ _$s3XPC11XPCListenerC22IncomingSessionRequestC20withUnsafeAuditTokenyxxSo13audit_token_taKXEKlF
+ _$s3XPC11XPCListenerC22IncomingSessionRequestC6reject6reasonAE8DecisionVSS_tFTj
+ _$s3XPC11XPCListenerC22IncomingSessionRequestC8DecisionVMa
+ _$ss9UnmanagedVMn
+ _$syXlN
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _swift_dynamicCast
- _$s10Foundation13__DataStorageC5bytes6lengthACSVSg_Sitcfc
- _$s10Foundation13__DataStorageCMa
- _$s10Foundation4DataV14RangeReferenceCMa
- _$s10Foundation4DataVN
- _$s14CoreFoundation9_CFObjectMp
- _$s14CoreFoundation9_CFObjectPAAE2eeoiySbx_xtFZ
- _$s14CoreFoundation9_CFObjectPAAE4hash4intoys6HasherVz_tF
- _$s14CoreFoundation9_CFObjectPAAE9hashValueSivg
- _$s14CoreFoundation9_CFObjectPSHTb
- _$s3XPC13XPCDictionaryV10auditTokenSo0C8_token_tavg
- _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
- _$sSH13_rawHashValue4seedS2i_tFTq
- _$sSH4hash4intoys6HasherVz_tFTq
- _$sSH9hashValueSivgTq
- _$sSHMp
- _$sSHSQTb
- _$sSQ2eeoiySbx_xtFZTq
- _$sSQMp
- _$sSW10Foundation15ContiguousBytesAAWP
- _$sSWN
- _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
- _$ss18_DictionaryStorageCMn
- _SecCodeCheckValidity
- _SecCodeCopyGuestWithAttributes
- _SecRequirementCreateWithString
- __swiftEmptyDictionarySingleton
- _kSecGuestAttributeAudit
- _kSecGuestAttributeDynamicCode
- _swift_initStackObject
CStrings:
+ "com.apple.private.ecosystemanalytics.rosetta"
+ "ecosystemanalyticsd: XPCListener: calling performRosettaAnalysis"
+ "ecosystemanalyticsd: XPCListener: failed to get SecTask object for session auditToken"
+ "ecosystemanalyticsd: XPCListener: sender is not entitled"
+ "ecosystemanalyticsd: isEntitled: %!@(MISSING)"
+ "ecosystemanalyticsd: isEntitled: SecTaskCopyValueForEntitlement returned nil"
+ "ecosystemanalyticsd: isEntitled: returning %!@(MISSING)"
+ "ecosystemanalyticsd: isEntitled: value returned is not a Bool"
+ "sender is not entitled"
- "ecosystemanalyticsd: XPCListener: failed to get SecCode object for message audit token"
- "ecosystemanalyticsd: XPCListener: sender is not Apple signed"
- "ecosystemanalyticsd: calling performRosettaAnalysis"

```

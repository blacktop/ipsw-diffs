## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-659.120.3.0.0
-  __TEXT.__text: 0x4cf14
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_stubs: 0x3020
-  __TEXT.__objc_methlist: 0x13ac
+659.120.7.0.3
+  __TEXT.__text: 0x4c614
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0x132c
   __TEXT.__const: 0x3f28
-  __TEXT.__cstring: 0x2b30
-  __TEXT.__objc_methname: 0x3c06
-  __TEXT.__objc_classname: 0x331
-  __TEXT.__objc_methtype: 0xa39
-  __TEXT.__oslogstring: 0x12b7
-  __TEXT.__gcc_except_tab: 0x238
+  __TEXT.__cstring: 0x2a90
+  __TEXT.__objc_methname: 0x3b1d
+  __TEXT.__objc_classname: 0x31a
+  __TEXT.__objc_methtype: 0xa1a
+  __TEXT.__oslogstring: 0x127e
+  __TEXT.__gcc_except_tab: 0x234
   __TEXT.__swift5_typeref: 0x88e
   __TEXT.__swift5_fieldmd: 0x1490
   __TEXT.__constg_swiftt: 0xd88

   __TEXT.__swift5_assocty: 0x5b8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1c70
+  __TEXT.__unwind_info: 0x1c50
   __TEXT.__eh_frame: 0x4158
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x2e18
-  __DATA_CONST.__cfstring: 0x17a0
+  __DATA_CONST.__const: 0x2df8
+  __DATA_CONST.__cfstring: 0x1720
   __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x25a0
-  __DATA.__objc_selrefs: 0xe60
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_const: 0x2500
+  __DATA.__objc_selrefs: 0xe38
+  __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0xe78
   __DATA.__data: 0x23d0
-  __DATA.__bss: 0x59d0
+  __DATA.__bss: 0x59c0
   __DATA.__common: 0x140
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2287
-  Symbols:   365
-  CStrings:  1161
+  Functions: 2275
+  Symbols:   361
+  CStrings:  1144
 
Symbols:
- __DPMetadataIsV2
- _kDPMetadataDediscoTaskConfigFeatures
- _kDPMetadataDediscoTaskConfigFeaturesOHTTP
- _kDPMetadataDediscoTaskConfigFeaturesPAT
CStrings:
+ "%@_%@.pat"
+ "Fetched %lu tokens"
+ "Missing issue URL. Skipping token fetching"
+ "No file found in path %@ to retrieve token"
+ "Token count: %lu; %@"
+ "donateTokenCountToBitacoraForDirPath:"
+ "fetchMultipleChallengeTokenPair"
+ "initWithIssuer:redemptionContext:"
+ "randomFile"
+ "randomToken"
+ "saveTokens:toFileInPath:"
+ "tokensFilePrefix"
- "\x011"
- "  aggregators: %@\n"
- "%@Tokens_%@.pat"
- "B40@0:8@16@24@32"
- "DPSubmissionService"
- "Fetched %lu tokens for aggregator %@."
- "Incorrect data type for %@.%@ - expect dictionary"
- "Incorrect data type for %@.%@.%@ - expect boolean"
- "Missing aggregator list or issue URL. Skipping token fetching"
- "No file found in path %@ to retrieve token for aggregator %@."
- "Origin info length exceeds 64KB."
- "Q32@0:8@16@24"
- "T@\"NSArray\",R,C,N,V_aggregators"
- "T@\"NSString\",R,C,N,V_origin"
- "Token count for %@: %lu; %@"
- "_aggregators"
- "_origin"
- "aggregators"
- "allKeys"
- "defaultValueForKey:"
- "donateTokenCountToBitacoraForAggregator:dirPath:"
- "fetchMultipleChallengeTokenPairForAggregator:"
- "getHelperServerName"
- "initWithIssuer:origin:redemptionContext:"
- "isFeatureEnabled:withError:"
- "origin"
- "randomFileForAggregator:"
- "randomTokenForAggregator:"
- "saveTokens:toFileInPath:forAggregator:"

```

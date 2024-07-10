## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Versions/A/Transparency`

```diff

-1218.0.57.0.2
-  __TEXT.__text: 0x43840
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x2df4
-  __TEXT.__cstring: 0x218f
-  __TEXT.__const: 0x94e
+1218.0.79.0.0
+  __TEXT.__text: 0x440d8
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x2e74
+  __TEXT.__cstring: 0x21ba
+  __TEXT.__const: 0x97e
   __TEXT.__gcc_except_tab: 0x560
-  __TEXT.__oslogstring: 0x16cf
+  __TEXT.__oslogstring: 0x1698
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__swift5_typeref: 0x19d
-  __TEXT.__swift5_reflstr: 0xa0
+  __TEXT.__swift5_reflstr: 0xaf
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x158
-  __TEXT.__swift5_fieldmd: 0x1f8
+  __TEXT.__swift5_fieldmd: 0x210
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x1460
+  __TEXT.__unwind_info: 0x1480
   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x627
-  __TEXT.__objc_methname: 0x6445
-  __TEXT.__objc_methtype: 0x19bb
-  __TEXT.__objc_stubs: 0x4d20
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x630
+  __TEXT.__objc_methname: 0x6555
+  __TEXT.__objc_methtype: 0x1a0b
+  __TEXT.__objc_stubs: 0x4dc0
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1920
+  __DATA_CONST.__objc_selrefs: 0x1960
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__auth_ptr: 0x138
-  __AUTH_CONST.__const: 0x2f00
-  __AUTH_CONST.__cfstring: 0x32e0
-  __AUTH_CONST.__objc_const: 0x6fe8
+  __AUTH_CONST.__const: 0x2f40
+  __AUTH_CONST.__cfstring: 0x3340
+  __AUTH_CONST.__objc_const: 0x7018
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0xff0
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x730
   __DATA.__bss: 0x12b0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 1761
-  Symbols:   3733
-  CStrings:  448
+  Functions: 1772
+  Symbols:   3754
+  CStrings:  451
 
Symbols:
+ +[SoftwareTransparency retryable:]
+ +[SoftwareTransparency tooManyRetries]
+ -[SoftwareTransparency proxyCreating]
+ -[SoftwareTransparency remoteObjectProxyWithErrorHandler:]
+ -[SoftwareTransparency setDebugProxyCreating:]
+ -[SoftwareTransparency setProxyCreating:]
+ -[SoftwareTransparency sysdiagnoseInfo:completion:]
+ -[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]
+ -[SoftwareTransparency verifyProofs:for:counter:completion:]
+ -[TransparencyAnalytics manateeStatusForReporting]
+ GCC_except_table32
+ OBJC_IVAR_$_SoftwareTransparency._proxyCreating
+ _PCSReportManateeStatus
+ __24-[KTAccountKey rollKey:]_block_invoke.46
+ __24-[KTAccountKey rollKey:]_block_invoke.49
+ __24-[KTAccountKey rollKey:]_block_invoke_2.50
+ __24-[KTAccountKey rollKey:]_block_invoke_2.61
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.34
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.37
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke_2.39
+ __46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.148
+ __60-[SoftwareTransparency verifyProofs:for:counter:completion:]_block_invoke.43
+ __OBJC_$_CLASS_METHODS_SoftwareTransparency
+ ___51-[SoftwareTransparency sysdiagnoseInfo:completion:]_block_invoke
+ ___60-[SoftwareTransparency verifyProofs:for:counter:completion:]_block_invoke
+ ___68-[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]_block_invoke
+ ___block_descriptor_52_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_68_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ __block_literal_global.130
+ __block_literal_global.147
+ __block_literal_global.33
+ __block_literal_global.41
+ __block_literal_global.45
+ __block_literal_global.63
+ _ktPeerValidateSuccessDays
+ _ktReliabilityAnalyticsVersion
+ _ktSelfValidateSuccessDays
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$proxyCreating
+ _objc_msgSend$retryable:
+ _objc_msgSend$setProxyCreating:
+ _objc_msgSend$sysdiagnoseInfo:completion:
+ _objc_msgSend$tooManyRetries
+ _objc_msgSend$verifyExpiringProofs:for:counter:completion:
+ _objc_msgSend$verifyProofs:for:counter:completion:
+ _reliabilityKey
+ _reliabilityVersionKey
- +[TransparencySettings allowsInternalSecurityPolicies]
- GCC_except_table33
- _OBJC_CLASS_$_NSUserDefaults
- __24-[KTAccountKey rollKey:]_block_invoke.56
- __24-[KTAccountKey rollKey:]_block_invoke.67
- __24-[KTAccountKey rollKey:]_block_invoke_2.57
- __24-[KTAccountKey rollKey:]_block_invoke_2.68
- __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.41
- __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.44
- __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.45
- __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke_2.46
- __46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.142
- __52-[SoftwareTransparency verifyProofs:for:completion:]_block_invoke.42
- ___52-[SoftwareTransparency verifyProofs:for:completion:]_block_invoke
- ___54-[SoftwareTransparency sysdiagnoseInfoWithCompletion:]_block_invoke
- ___60-[SoftwareTransparency verifyExpiringProofs:for:completion:]_block_invoke
- __block_literal_global.141
- __block_literal_global.40
- __block_literal_global.62
- __block_literal_global.70
- _objc_msgSend$allowsInternalSecurityPolicies
- _objc_msgSend$boolForKey:
- _objc_msgSend$standardUserDefaults
CStrings:
+ "Manatee"
+ "SelfHard"
+ "ktHasReachedReliability"
+ "ktHasReachedReliabilityVersion"
- "disableTransparencySignature"

```

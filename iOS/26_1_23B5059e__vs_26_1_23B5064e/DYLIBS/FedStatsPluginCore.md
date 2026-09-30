## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x102bc
+60.0.0.0.0
+  __TEXT.__text: 0x1035c
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xc3c
+  __TEXT.__objc_methlist: 0xc44
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x2130
+  __TEXT.__cstring: 0x2140
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x11c1
+  __TEXT.__oslogstring: 0x1201
   __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x3ef
-  __TEXT.__objc_methname: 0x25d5
+  __TEXT.__objc_methname: 0x25ef
   __TEXT.__objc_methtype: 0x37a
-  __TEXT.__objc_stubs: 0x20e0
-  __DATA_CONST.__got: 0x290
+  __TEXT.__objc_stubs: 0x2120
+  __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x998
+  __DATA_CONST.__objc_selrefs: 0x9a8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x138
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x27a0
+  __AUTH_CONST.__cfstring: 0x27c0
   __AUTH_CONST.__objc_const: 0x1f68
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D6A5267-ADB2-3D96-81E5-B73FD1D168A5
-  Functions: 309
-  Symbols:   1383
-  CStrings:  1236
+  UUID: 686001DF-DA8D-32CE-9670-086E63EF6539
+  Functions: 311
+  Symbols:   1390
+  CStrings:  1241
 
Symbols:
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.8
+ +[FedStatsPluginCoreConsentCheckHelper checkCommSafety]
+ _OBJC_CLASS_$_SCAnalyticsConsent
+ _objc_msgSend$checkCommSafety
+ _objc_msgSend$isEnabled
Functions:
+ +[FedStatsPluginCoreConsentCheckHelper checkCommSafety]
~ ___48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke : 1056 -> 1064
~ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:] : 692 -> 780
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:].cold.1
CStrings:
+ "Comm Safety consent is required for this use-case but not given"
+ "checkCommSafety"
+ "isEnabled"
+ "needsCommSafety"

```

## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.0.68.2.3
-  __TEXT.__text: 0x8270c
+12.1.6.0.0
+  __TEXT.__text: 0x829cc
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xabc4
+  __TEXT.__objc_methlist: 0xabcc
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x532b
+  __TEXT.__cstring: 0x532d
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x26
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__oslogstring: 0x4720
-  __TEXT.__gcc_except_tab: 0x1044
-  __TEXT.__unwind_info: 0x2718
+  __TEXT.__gcc_except_tab: 0x1048
+  __TEXT.__unwind_info: 0x2728
   __TEXT.__objc_classname: 0x18ac
-  __TEXT.__objc_methname: 0x143eb
-  __TEXT.__objc_methtype: 0x348f
-  __TEXT.__objc_stubs: 0x86a0
+  __TEXT.__objc_methname: 0x1457c
+  __TEXT.__objc_methtype: 0x34f0
+  __TEXT.__objc_stubs: 0x8700
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x2768
+  __DATA_CONST.__const: 0x2788
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43d8
+  __DATA_CONST.__objc_selrefs: 0x43f0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x810
   __AUTH_CONST.__cfstring: 0x67e0
-  __AUTH_CONST.__objc_const: 0x156f8
+  __AUTH_CONST.__objc_const: 0x156e0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95B45DA0-8A7B-3149-972E-1AA377FCD108
-  Functions: 4331
-  Symbols:   13209
-  CStrings:  6336
+  UUID: 2F21EA1B-A00C-328E-96FC-8C61F559372A
+  Functions: 4333
+  Symbols:   13215
+  CStrings:  6340
 
Symbols:
+ +[ASDBackgroundAssets didReachAssetPackTerminalPhaseForStoreItemIdentifier:bundleIdentifier:assetPackIdentifier:assetPackVersion:internalBeta:terminalPhase:error:completionHandler:]
+ -[ASDInstallationEventProofOfPurchase initWithItemID:timestampString:isRedownload:privateInput:certificate:finalizedToken:]
+ -[ASDServiceBroker getBackgroundAssetsServiceWithCompletionHandler:]
+ GCC_except_table19
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table86
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table97
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._certificate
+ ___181+[ASDBackgroundAssets didReachAssetPackTerminalPhaseForStoreItemIdentifier:bundleIdentifier:assetPackIdentifier:assetPackVersion:internalBeta:terminalPhase:error:completionHandler:]_block_invoke
+ ___68-[ASDServiceBroker getBackgroundAssetsServiceWithCompletionHandler:]_block_invoke
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e78_v24?0"<ASDBackgroundAssetsServiceProtocol><NSXPCProxyCreating>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$didReachAssetPackTerminalPhaseForStoreItemIdentifier:bundleIdentifier:assetPackIdentifier:assetPackVersion:internalBeta:terminalPhase:error:replyHandler:
+ _objc_msgSend$getBackgroundAssetsServiceWithCompletionHandler:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithItemID:timestampString:isRedownload:privateInput:certificate:finalizedToken:
- -[ASDInstallationEventProofOfPurchase initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:]
- -[ASDInstallationEventProofOfPurchase nonce]
- -[ASDInstallationEventProofOfPurchase timestamp]
- GCC_except_table16
- GCC_except_table27
- GCC_except_table35
- GCC_except_table40
- GCC_except_table45
- GCC_except_table54
- GCC_except_table68
- GCC_except_table73
- GCC_except_table84
- GCC_except_table89
- GCC_except_table92
- GCC_except_table95
- _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._publicKey
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_AppStoreDaemon
- _objc_msgSend$initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:
CStrings:
+ "T@\"NSString\",R,V_certificate"
+ "_certificate"
+ "didReachAssetPackTerminalPhaseForStoreItemIdentifier:bundleIdentifier:assetPackIdentifier:assetPackVersion:internalBeta:terminalPhase:error:completionHandler:"
+ "didReachAssetPackTerminalPhaseForStoreItemIdentifier:bundleIdentifier:assetPackIdentifier:assetPackVersion:internalBeta:terminalPhase:error:replyHandler:"
+ "getBackgroundAssetsServiceWithCompletionHandler:"
+ "initWithBase64EncodedString:options:"
+ "initWithItemID:timestampString:isRedownload:privateInput:certificate:finalizedToken:"
+ "v76@0:8@\"NSNumber\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40B48q52@\"NSError\"60@?<v@?@\"NSError\">68"
- "T@\"NSData\",R,V_publicKey"
- "_publicKey"
- "initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:"
- "nonce"

```

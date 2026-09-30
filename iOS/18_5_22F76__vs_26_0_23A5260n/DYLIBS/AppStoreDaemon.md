## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-11.5.4.0.0
-  __TEXT.__text: 0x7fda0
+12.0.41.2.1
+  __TEXT.__text: 0x81a68
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xa7dc
+  __TEXT.__objc_methlist: 0xab54
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x51a9
+  __TEXT.__cstring: 0x52a5
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x26
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__oslogstring: 0x468e
-  __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__unwind_info: 0x2658
-  __TEXT.__objc_classname: 0x188e
-  __TEXT.__objc_methname: 0x13804
-  __TEXT.__objc_methtype: 0x337f
-  __TEXT.__objc_stubs: 0x8460
-  __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x2680
-  __DATA_CONST.__objc_classlist: 0x5d0
+  __TEXT.__oslogstring: 0x46ac
+  __TEXT.__gcc_except_tab: 0x1044
+  __TEXT.__unwind_info: 0x26c0
+  __TEXT.__objc_classname: 0x18bb
+  __TEXT.__objc_methname: 0x14043
+  __TEXT.__objc_methtype: 0x34b5
+  __TEXT.__objc_stubs: 0x8600
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x2760
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4228
-  __DATA_CONST.__objc_protorefs: 0x150
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_selrefs: 0x4368
+  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6580
-  __AUTH_CONST.__objc_const: 0x14f70
+  __AUTH_CONST.__cfstring: 0x66c0
+  __AUTH_CONST.__objc_const: 0x15670
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc98
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0xd0c
   __DATA.__data: 0x1958
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_ivar: 0x19c
-  __DATA_DIRTY.__objc_data: 0x3890
+  __DATA_DIRTY.__objc_data: 0x2350
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x290
   __DATA_DIRTY.__common: 0x168

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6173E4F2-5B6B-3C4E-B7CA-F7440AB1F854
-  Functions: 4233
-  Symbols:   12964
-  CStrings:  6180
+  UUID: A989CB17-3394-38F0-810F-9A707BA62A25
+  Functions: 4312
+  Symbols:   13177
+  CStrings:  6291
 
Symbols:
+ +[ASDBackgroundAssets interface]
+ +[ASDBackgroundAssets testFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:error:]
+ +[ASDInstallationEventProofOfPurchase supportsSecureCoding]
+ -[ASDAppReviewAppMetadata chunkSize]
+ -[ASDAppReviewAppMetadata clearHashes]
+ -[ASDAppReviewAppMetadata cryptHashes]
+ -[ASDAppReviewAppMetadata hashType]
+ -[ASDAppReviewAppMetadata packageFormat]
+ -[ASDAppReviewAppMetadata packageSize]
+ -[ASDAppReviewAppMetadata setChunkSize:]
+ -[ASDAppReviewAppMetadata setClearHashes:]
+ -[ASDAppReviewAppMetadata setCryptHashes:]
+ -[ASDAppReviewAppMetadata setHashType:]
+ -[ASDAppReviewAppMetadata setPackageFormat:]
+ -[ASDAppReviewAppMetadata setPackageSize:]
+ -[ASDAppReviewAppMetadata setSoftwarePlatform:]
+ -[ASDAppReviewAppMetadata softwarePlatform]
+ -[ASDBetaAppLaunchInfo iconNeedsMask]
+ -[ASDBetaAppLaunchInfo setIconNeedsMask:]
+ -[ASDCellularSettings initWithIdentity:]
+ -[ASDInstallationEvent initWithPhase:commerceTimestamp:purchase:terminalPhase:bundleID:itemID:appType:source:installType:]
+ -[ASDInstallationEvent purchase]
+ -[ASDInstallationEventProofOfPurchase .cxx_destruct]
+ -[ASDInstallationEventProofOfPurchase certificate]
+ -[ASDInstallationEventProofOfPurchase copyWithZone:]
+ -[ASDInstallationEventProofOfPurchase encodeWithCoder:]
+ -[ASDInstallationEventProofOfPurchase finalizedToken]
+ -[ASDInstallationEventProofOfPurchase initWithCoder:]
+ -[ASDInstallationEventProofOfPurchase initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:]
+ -[ASDInstallationEventProofOfPurchase isRedownload]
+ -[ASDInstallationEventProofOfPurchase itemID]
+ -[ASDInstallationEventProofOfPurchase nonce]
+ -[ASDInstallationEventProofOfPurchase privateInput]
+ -[ASDInstallationEventProofOfPurchase publicKey]
+ -[ASDInstallationEventProofOfPurchase timestampString]
+ -[ASDInstallationEventProofOfPurchase timestamp]
+ -[ASDManifestRequest setSoftwarePlatform:]
+ -[ASDManifestRequest softwarePlatform]
+ -[ASDPurchase ageRatingValue]
+ -[ASDPurchase packageOverride]
+ -[ASDPurchase packaging]
+ -[ASDPurchase setAgeRatingValue:]
+ -[ASDPurchase setPackageOverride:]
+ -[ASDPurchase setPackaging:]
+ -[ASDPurchase setShouldAskForRatingException:]
+ -[ASDPurchase shouldAskForRatingException]
+ -[ASDPurchaseHistoryApp appIconArtworkToken]
+ -[ASDPurchaseHistoryApp appIconArtworkURLString]
+ -[ASDPurchaseHistoryApp circularAppIconArtworkToken]
+ -[ASDPurchaseHistoryApp circularAppIconArtworkURLString]
+ -[ASDPurchaseHistoryApp isEligibleForGamesApp]
+ -[ASDPurchaseHistoryApp setAppIconArtworkToken:]
+ -[ASDPurchaseHistoryApp setAppIconArtworkURLString:]
+ -[ASDPurchaseHistoryApp setCircularAppIconArtworkToken:]
+ -[ASDPurchaseHistoryApp setCircularAppIconArtworkURLString:]
+ -[ASDPurchaseHistoryApp setIsEligibleForGamesApp:]
+ -[ASDPurchaseHistoryQuery isEligibleForGamesApp]
+ -[ASDPurchaseHistoryQuery setIsEligibleForGamesApp:]
+ -[ASDServiceBroker getBackgroundAssetsServiceWithError:]
+ -[ASDTestFlightAppMetadata betaTesterType]
+ -[ASDTestFlightAppMetadata hashType]
+ -[ASDTestFlightAppMetadata packageFormat]
+ -[ASDTestFlightAppMetadata setBetaTesterType:]
+ -[ASDTestFlightAppMetadata setHashType:]
+ -[ASDTestFlightAppMetadata setPackageFormat:]
+ -[ASDTestFlightServiceExtension didReachAssetPackTerminalPhaseForStoreItemID:bundleID:assetPackID:assetPackVersion:isInternalBeta:terminalPhase:error:reply:]
+ -[ASDTestFlightServiceExtension fetchBAManifestRequestForStoreItemID:bundleID:reply:]
+ -[ASDTestFlightServiceExtensionRemoteContext didReachAssetPackTerminalPhaseForStoreItemID:bundleID:assetPackID:assetPackVersion:isInternalBeta:terminalPhase:error:reply:]
+ -[ASDTestFlightServiceExtensionRemoteContext fetchBAManifestRequestForStoreItemID:bundleID:reply:]
+ -[ASDVPPRequest setSoftwarePlatform:]
+ -[ASDVPPRequest softwarePlatform]
+ GCC_except_table16
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table54
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table84
+ GCC_except_table95
+ _OBJC_CLASS_$_AMSMediaResponseDecoder
+ _OBJC_CLASS_$_ASDBackgroundAssets
+ _OBJC_CLASS_$_ASDInstallationEventProofOfPurchase
+ _OBJC_CLASS_$_NSURLRequest
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._chunkSize
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._clearHashes
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._cryptHashes
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._hashType
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._packageFormat
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._packageSize
+ _OBJC_IVAR_$_ASDAppReviewAppMetadata._softwarePlatform
+ _OBJC_IVAR_$_ASDBetaAppLaunchInfo._iconNeedsMask
+ _OBJC_IVAR_$_ASDInstallationEvent._purchase
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._finalizedToken
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._isRedownload
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._itemID
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._privateInput
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._publicKey
+ _OBJC_IVAR_$_ASDInstallationEventProofOfPurchase._timestampString
+ _OBJC_IVAR_$_ASDManifestRequest._softwarePlatform
+ _OBJC_IVAR_$_ASDPurchase._ageRatingValue
+ _OBJC_IVAR_$_ASDPurchase._packageOverride
+ _OBJC_IVAR_$_ASDPurchase._packaging
+ _OBJC_IVAR_$_ASDPurchase._shouldAskForRatingException
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._appIconArtworkToken
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._appIconArtworkURLString
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._circularAppIconArtworkToken
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._circularAppIconArtworkURLString
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._isEligibleForGamesApp
+ _OBJC_IVAR_$_ASDPurchaseHistoryQuery._isEligibleForGamesApp
+ _OBJC_IVAR_$_ASDTestFlightAppMetadata._betaTesterType
+ _OBJC_IVAR_$_ASDTestFlightAppMetadata._hashType
+ _OBJC_IVAR_$_ASDTestFlightAppMetadata._packageFormat
+ _OBJC_IVAR_$_ASDVPPRequest._softwarePlatform
+ _OBJC_METACLASS_$_ASDBackgroundAssets
+ _OBJC_METACLASS_$_ASDInstallationEventProofOfPurchase
+ __OBJC_$_CLASS_METHODS_ASDBackgroundAssets
+ __OBJC_$_CLASS_METHODS_ASDInstallationEventProofOfPurchase
+ __OBJC_$_CLASS_PROP_LIST_ASDCellularIdentity
+ __OBJC_$_CLASS_PROP_LIST_ASDInstallationEventProofOfPurchase
+ __OBJC_$_INSTANCE_METHODS_ASDInstallationEventProofOfPurchase
+ __OBJC_$_INSTANCE_VARIABLES_ASDInstallationEventProofOfPurchase
+ __OBJC_$_PROP_LIST_ASDBackgroundAssets
+ __OBJC_$_PROP_LIST_ASDInstallationEventProofOfPurchase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDBackgroundAssetsServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDBackgroundAssetsServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ASDBackgroundAssets
+ __OBJC_CLASS_PROTOCOLS_$_ASDInstallationEventProofOfPurchase
+ __OBJC_CLASS_RO_$_ASDBackgroundAssets
+ __OBJC_CLASS_RO_$_ASDInstallationEventProofOfPurchase
+ __OBJC_LABEL_PROTOCOL_$_ASDBackgroundAssetsServiceProtocol
+ __OBJC_METACLASS_RO_$_ASDBackgroundAssets
+ __OBJC_METACLASS_RO_$_ASDInstallationEventProofOfPurchase
+ __OBJC_PROTOCOL_$_ASDBackgroundAssetsServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDBackgroundAssetsServiceProtocol
+ ___102+[ASDBackgroundAssets testFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:error:]_block_invoke
+ ___102+[ASDBackgroundAssets testFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:error:]_block_invoke_2
+ ___170-[ASDTestFlightServiceExtensionRemoteContext didReachAssetPackTerminalPhaseForStoreItemID:bundleID:assetPackID:assetPackVersion:isInternalBeta:terminalPhase:error:reply:]_block_invoke
+ ___27-[ASDMediaClipTask perform]_block_invoke.11
+ ___27-[ASDMediaClipTask perform]_block_invoke.4
+ ___27-[ASDMediaClipTask perform]_block_invoke_2
+ ___56-[ASDServiceBroker getBackgroundAssetsServiceWithError:]_block_invoke
+ ___56-[ASDServiceBroker getBackgroundAssetsServiceWithError:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e35_"AMSPromise"16?0"AMSURLRequest"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSURLRequest"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e78_v24?0"<ASDBackgroundAssetsServiceProtocol><NSXPCProxyCreating>"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e37_"AMSPromise"16?0"NSURLComponents"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e34_v24?0"AMSURLResult"8"NSError"16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs_e39_v16?0"ASDTestFlightServiceExtension"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.175
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppStoreDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppStoreDaemon
+ _objc_msgSend$_setError
+ _objc_msgSend$appIconArtworkToken
+ _objc_msgSend$appIconArtworkURLString
+ _objc_msgSend$circularAppIconArtworkToken
+ _objc_msgSend$circularAppIconArtworkURLString
+ _objc_msgSend$data
+ _objc_msgSend$didReachAssetPackTerminalPhaseForStoreItemID:bundleID:assetPackID:assetPackVersion:isInternalBeta:terminalPhase:error:reply:
+ _objc_msgSend$fetchBAManifestRequestForStoreItemID:bundleID:reply:
+ _objc_msgSend$getBackgroundAssetsServiceWithError:
+ _objc_msgSend$getBackgroundAssetsServiceWithReplyHandler:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getTestFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:replyHandler:
+ _objc_msgSend$hasError
+ _objc_msgSend$iconNeedsMask
+ _objc_msgSend$initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:
+ _objc_msgSend$initWithPhase:commerceTimestamp:purchase:terminalPhase:bundleID:itemID:appType:source:installType:
+ _objc_msgSend$isEligibleForGamesApp
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$position
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$setPosition:
+ _objc_retain_x7
- -[ASDInstallationEvent initWithPhase:commerceTimestamp:terminalPhase:bundleID:itemID:appType:source:installType:]
- -[ASDMediaClipTaskResponseDecoder resultFromResult:error:]
- GCC_except_table37
- GCC_except_table42
- GCC_except_table51
- GCC_except_table65
- GCC_except_table70
- GCC_except_table81
- GCC_except_table86
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AMSError
- _OBJC_CLASS_$_AMSMediaResult
- _OBJC_CLASS_$_ASDMediaClipTaskResponseDecoder
- _OBJC_CLASS_$_NSHTTPURLResponse
- _OBJC_CLASS_$_NSIndexSet
- _OBJC_IVAR_$_ASDAppLibrary._notificationCenter
- _OBJC_METACLASS_$_ASDMediaClipTaskResponseDecoder
- __OBJC_$_INSTANCE_METHODS_ASDMediaClipTaskResponseDecoder
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSResponseDecoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_AMSResponseDecoding
- __OBJC_CLASS_PROTOCOLS_$_ASDMediaClipTaskResponseDecoder
- __OBJC_CLASS_RO_$_ASDMediaClipTaskResponseDecoder
- __OBJC_LABEL_PROTOCOL_$_AMSResponseDecoding
- __OBJC_METACLASS_RO_$_ASDMediaClipTaskResponseDecoder
- __OBJC_PROTOCOL_$_AMSResponseDecoding
- ___63-[ASDUpdatesService shouldUseModernUpdatesWithCompletionBlock:]_block_invoke
- ___63-[ASDUpdatesService shouldUseModernUpdatesWithCompletionBlock:]_block_invoke_2
- ___block_literal_global.170
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AppStoreDaemon
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AppStoreDaemon
- _objc_msgSend$containsIndex:
- _objc_msgSend$initWithIndexesInRange:
- _objc_msgSend$initWithPhase:commerceTimestamp:terminalPhase:bundleID:itemID:appType:source:installType:
- _objc_msgSend$initWithResult:
- _objc_msgSend$response
- _objc_msgSend$resultWithTimeout:error:
- _objc_msgSend$shouldUseModernUpdatesWithReplyHandler:
- _objc_msgSend$statusCode
CStrings:
+ "$"
+ "@\"AMSPromise\"16@?0@\"AMSURLRequest\"8"
+ "@\"AMSPromise\"16@?0@\"NSURLComponents\"8"
+ "@\"ASDInstallationEventProofOfPurchase\""
+ "@60@0:8Q16@24B32@36@44@52"
+ "@88@0:8q16@24@32q40@48@56q64q72q80"
+ "AB"
+ "AE"
+ "ASDBackgroundAssets"
+ "ASDBackgroundAssetsServiceProtocol"
+ "ASDInstallationEventProofOfPurchase"
+ "BT"
+ "HT"
+ "PF"
+ "SoftwarePlatform"
+ "T@\"ASDCellularIdentity\",R"
+ "T@\"ASDInstallationEventProofOfPurchase\",R,V_purchase"
+ "T@\"NSData\",R"
+ "T@\"NSData\",R,V_finalizedToken"
+ "T@\"NSData\",R,V_privateInput"
+ "T@\"NSData\",R,V_publicKey"
+ "T@\"NSString\",C,N,V_packageOverride"
+ "T@\"NSString\",C,V_appIconArtworkToken"
+ "T@\"NSString\",C,V_appIconArtworkURLString"
+ "T@\"NSString\",C,V_circularAppIconArtworkToken"
+ "T@\"NSString\",C,V_circularAppIconArtworkURLString"
+ "T@\"NSString\",R,V_timestampString"
+ "TB,N,V_shouldAskForRatingException"
+ "TB,R,V_isRedownload"
+ "TB,V_iconNeedsMask"
+ "TB,V_isEligibleForGamesApp"
+ "TQ,N,V_ageRatingValue"
+ "TQ,R,V_itemID"
+ "TQ,V_betaTesterType"
+ "This region does not have automatic update authorization"
+ "Timed out doing media lookup"
+ "Tq,N,V_packaging"
+ "Tq,V_hashType"
+ "Tq,V_isEligibleForGamesApp"
+ "Tq,V_packageFormat"
+ "_ageRatingValue"
+ "_appIconArtworkToken"
+ "_appIconArtworkURLString"
+ "_betaTesterType"
+ "_circularAppIconArtworkToken"
+ "_circularAppIconArtworkURLString"
+ "_finalizedToken"
+ "_iconNeedsMask"
+ "_isEligibleForGamesApp"
+ "_packageFormat"
+ "_packageOverride"
+ "_packaging"
+ "_privateInput"
+ "_publicKey"
+ "_setError"
+ "_shouldAskForRatingException"
+ "_timestampString"
+ "ageRatingValue"
+ "appIconArtworkToken"
+ "appIconArtworkURLString"
+ "betaTesterType"
+ "certificate"
+ "circularAppIconArtworkToken"
+ "circularAppIconArtworkURLString"
+ "data"
+ "didReachAssetPackTerminalPhaseForStoreItemID:bundleID:assetPackID:assetPackVersion:isInternalBeta:terminalPhase:error:reply:"
+ "fetchBAManifestRequestForStoreItemID:bundleID:reply:"
+ "finalizedToken"
+ "getBackgroundAssetsServiceWithError:"
+ "getBackgroundAssetsServiceWithReplyHandler:"
+ "getBytes:range:"
+ "getTestFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:replyHandler:"
+ "hasError"
+ "iconNeedsMask"
+ "initWithIdentity:"
+ "initWithItemID:timestampString:isRedownload:privateInput:publicKey:finalizedToken:"
+ "initWithPhase:commerceTimestamp:purchase:terminalPhase:bundleID:itemID:appType:source:installType:"
+ "isEligibleForGamesApp"
+ "jobManager:updatedStateOfJobs:"
+ "nonce"
+ "numberWithUnsignedLongLong:"
+ "packageFormat"
+ "packageOverride"
+ "packaging"
+ "position"
+ "privateInput"
+ "publicKey"
+ "resultWithCompletion:"
+ "setAgeRatingValue:"
+ "setAppIconArtworkToken:"
+ "setAppIconArtworkURLString:"
+ "setBetaTesterType:"
+ "setCircularAppIconArtworkToken:"
+ "setCircularAppIconArtworkURLString:"
+ "setIconNeedsMask:"
+ "setIsEligibleForGamesApp:"
+ "setPackageFormat:"
+ "setPackageOverride:"
+ "setPackaging:"
+ "setPosition:"
+ "setShouldAskForRatingException:"
+ "shouldAskForRatingException"
+ "testFlightDownloadManifestRequestForStoreItemIdentifier:bundleIdentifier:error:"
+ "timestampString"
+ "v24@0:8@?<v@?@\"<ASDBackgroundAssetsServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@?0@\"<ASDBackgroundAssetsServiceProtocol><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0@\"AMSURLResult\"8@\"NSError\"16"
+ "v24@?0@\"NSURLRequest\"8@\"NSError\"16"
+ "v40@0:8@\"NSNumber\"16@\"NSString\"24@?<v@?@\"NSURLRequest\"@\"NSError\">32"
+ "v76@0:8@\"NSNumber\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40B48q52@\"NSError\"60@?<v@?B@\"NSError\">68"
+ "v76@0:8@16@24@32@40B48q52@60@?68"
- "@\"AMSURLResult\"32@0:8@\"AMSURLResult\"16^@24"
- "@80@0:8q16@24q32@40@48q56q64q72"
- "AMSResponseDecoding"
- "ASDMediaClipTaskResponseDecoder"
- "Invalid Response"
- "Invalid Status Code"
- "Media resource not found."
- "Media token is expired."
- "Media token is invalid."
- "Response is not of type NSHTTPURLResponse."
- "Response status code is: %lu"
- "This region is unsupported"
- "containsIndex:"
- "initWithIndexesInRange:"
- "initWithPhase:commerceTimestamp:terminalPhase:bundleID:itemID:appType:source:installType:"
- "initWithResult:"
- "response"
- "resultFromResult:error:"
- "resultWithTimeout:error:"
- "statusCode"

```

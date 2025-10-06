## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5407.3.0.0.0
-  __TEXT.__text: 0x2e6f10
+5419.0.0.0.0
+  __TEXT.__text: 0x2e7848
   __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__objc_methlist: 0x2a658
-  __TEXT.__const: 0x15b8
+  __TEXT.__objc_methlist: 0x2a728
+  __TEXT.__const: 0x15c8
   __TEXT.__swift5_typeref: 0x1ac
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__cstring: 0x48723
+  __TEXT.__cstring: 0x48879
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_reflstr: 0xa7
   __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x10
-  __TEXT.__oslogstring: 0xfe71
+  __TEXT.__oslogstring: 0xff6b
   __TEXT.__gcc_except_tab: 0x38b0
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x14a
-  __TEXT.__unwind_info: 0xa32c
+  __TEXT.__unwind_info: 0xa344
   __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x6e46
-  __TEXT.__objc_methname: 0x7d303
-  __TEXT.__objc_methtype: 0xc08b
-  __TEXT.__objc_stubs: 0x323e0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x10630
+  __TEXT.__objc_classname: 0x6e4a
+  __TEXT.__objc_methname: 0x7d5ad
+  __TEXT.__objc_methtype: 0xc09d
+  __TEXT.__objc_stubs: 0x32420
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x10608
   __DATA_CONST.__objc_classlist: 0x1a10
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x708
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x65460
-  __DATA_CONST.__objc_selrefs: 0x12e40
+  __DATA_CONST.__objc_const: 0x656f8
+  __DATA_CONST.__objc_selrefs: 0x12eb8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_classrefs: 0x1f68
   __DATA_CONST.__objc_superrefs: 0x1468
   __DATA_CONST.__objc_arraydata: 0x1060
-  __AUTH_CONST.__const: 0x4e48
+  __AUTH_CONST.__const: 0x4e88
   __AUTH_CONST.__objc_const: 0x13028
-  __AUTH_CONST.__cfstring: 0x2ab40
+  __AUTH_CONST.__cfstring: 0x2aca0
   __AUTH_CONST.__objc_intobj: 0x1350
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xc58

   __AUTH_CONST.__auth_got: 0xb68
   __AUTH.__objc_data: 0x43b0
   __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x4060
-  __DATA.__data: 0x5568
+  __DATA.__objc_ivar: 0x406c
+  __DATA.__data: 0x5598
   __DATA.__common: 0x8
   __DATA.__bss: 0x218
-  __DATA_DIRTY.__objc_ivar: 0xf58
+  __DATA_DIRTY.__objc_ivar: 0xf5c
   __DATA_DIRTY.__objc_data: 0xc238
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x170
-  __DATA_DIRTY.__bss: 0xe30
+  __DATA_DIRTY.__bss: 0xe00
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 61F962C3-411C-38D9-8C2B-FBCC9153B4B8
-  Functions: 18665
-  Symbols:   60241
-  CStrings:  34037
+  UUID: 09E06BE7-8EC7-36F2-930C-687592892904
+  Functions: 18688
+  Symbols:   60293
+  CStrings:  34087
 
Symbols:
+ -[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]
+ -[FCAssetHandle fetchDataProviderWithPriority:flags:completion:]
+ -[FCBundleSubscriptionManager initWithPrivateDataDirectory:configurationManager:cloudContext:contentContext:appActivityMonitor:entitlementsProvider:]
+ -[FCBundleSubscriptionManager networkReachabilityDidChange:]
+ -[FCNewsAppConfig liveActivityScheduleDelay]
+ -[FCNewsAppConfig liveActivityScheduleRandomInitialDelay]
+ -[FCNewsAppConfig liveActivityScheduleRetryCountMax]
+ -[FCNewsAppConfig liveActivityScheduleRetryInterval]
+ -[FCNewsAppConfig liveActivityScheduleRetryTimeWindow]
+ -[FCNewsAppConfig liveActivityScheduleTimeWindow]
+ -[FCNewsAppConfig liveActivityScheduledAlertsThreshold]
+ -[FCOperation flags]
+ -[FCOperation setFlags:]
+ -[FCPaidBundleConfiguration appLaunchUpsellBehaviorFlags]
+ -[FCPresentationOperation handlerUID]
+ -[FCPresentationOperation ignoreAfterSuccessfulPresentation]
+ -[FCPresentationOperation maxRetries]
+ -[FCPresentationOperation operationUID]
+ -[FCPresentationOperation setHandlerUID:]
+ -[FCPresentationOperation setIgnoreAfterSuccessfulPresentation:]
+ -[FCPresentationOperation setMaxRetries:]
+ -[FCPresentationOperation setOperationUID:]
+ -[NSError(FCAdditions) fc_failedDueToTaskConstraints]
+ _FCOperationFlagsApplyToURLRequest
+ _NSURLErrorNetworkUnavailableReasonKey
+ _OBJC_IVAR_$_FCPresentationOperation._handlerUID
+ _OBJC_IVAR_$_FCPresentationOperation._ignoreAfterSuccessfulPresentation
+ _OBJC_IVAR_$_FCPresentationOperation._maxRetries
+ _OBJC_IVAR_$_FCPresentationOperation._operationUID
+ __MergedGlobals.88
+ __OBJC_$_PROP_LIST_FCNewsletterManager.308
+ ___24-[FCOperation setFlags:]_block_invoke
+ ___34-[FCNewsletterManager unsubscribe]_block_invoke
+ ___36-[FCNewsletterManager optIntoSports]_block_invoke.46
+ ___37-[FCNewsletterManager optOutOfIssues]_block_invoke.41
+ ___37-[FCNewsletterManager optOutOfSports]_block_invoke.49
+ ___53-[NSError(FCAdditions) fc_failedDueToTaskConstraints]_block_invoke
+ ___56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke.70
+ ___56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke_2.74
+ ___60-[FCBundleSubscriptionManager networkReachabilityDidChange:]_block_invoke
+ ___64-[FCAssetHandle fetchDataProviderWithPriority:flags:completion:]_block_invoke
+ ___69-[FCTelemetryBasedOfflineNetworkTransitionOperation logNetworkEvent:]_block_invoke.26
+ ___69-[FCTelemetryBasedOfflineNetworkTransitionOperation logNetworkEvent:]_block_invoke_3
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke.9
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_2
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_3
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_4
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_5
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_6
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_7
+ ___80-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke_8
+ ___80-[FCResourceArchiveFetchOperation _unzipResourcesFromArchiveFileURL:completion:]_block_invoke.28
+ ___block_descriptor_88_e8_32s40s48bs56r64r_e5_v8?0ls32l8r56l8r64l8s48l8s40l8
+ ___block_literal_global.1334
+ ___block_literal_global.1409
+ ___block_literal_global.1413
+ ___block_literal_global.1432
+ ___block_literal_global.1437
+ ___block_literal_global.1442
+ ___block_literal_global.1447
+ ___block_literal_global.427
+ ___block_literal_global.462
+ ___block_literal_global.479
+ ___block_literal_global.496
+ ___block_literal_global.513
+ ___block_literal_global.530
+ ___block_literal_global.541
+ ___block_literal_global.546
+ _objc_msgSend$fc_failedDueToTaskConstraints
+ _objc_msgSend$fetchDataProviderWithPriority:flags:completion:
+ _objc_msgSend$initWithPrivateDataDirectory:configurationManager:cloudContext:contentContext:appActivityMonitor:entitlementsProvider:
+ _objc_msgSend$setAllowsConstrainedNetworkAccess:
+ _objc_msgSend$setAllowsExpensiveNetworkAccess:
- -[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]
- -[FCAssetHandle fetchDataProviderWithPriority:completion:]
- -[FCBundleSubscriptionManager initWithPrivateDataDirectory:configurationManager:contentContext:appActivityMonitor:entitlementsProvider:]
- -[FCPresentationOperation setUid:]
- -[FCPresentationOperation uid]
- _OBJC_IVAR_$_FCPresentationOperation._uid
- __MergedGlobals.86
- __OBJC_$_PROP_LIST_FCNewsletterManager.306
- ___36-[FCNewsletterManager optIntoSports]_block_invoke.44
- ___37-[FCNewsletterManager optOutOfIssues]_block_invoke.39
- ___37-[FCNewsletterManager optOutOfSports]_block_invoke.47
- ___52-[FCBundleSubscription(Headlines) containsHeadline:]_block_invoke_3
- ___56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke.68
- ___56-[FCNewsletterManager saveToCloudKitSubscribedChannels:]_block_invoke_2.72
- ___58-[FCAssetHandle fetchDataProviderWithPriority:completion:]_block_invoke
- ___69-[FCTelemetryBasedOfflineNetworkTransitionOperation logNetworkEvent:]_block_invoke.24
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke.9
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_2
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_3
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_4
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_5
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_6
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_7
- ___74-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke_8
- ___80-[FCResourceArchiveFetchOperation _unzipResourcesFromArchiveFileURL:completion:]_block_invoke.27
- ___block_descriptor_40_e8_32s_e5_i8?0ls32l8
- ___block_descriptor_80_e8_32s40s48bs56r64r_e5_v8?0ls32l8r56l8r64l8s48l8s40l8
- ___block_literal_global.1313
- ___block_literal_global.1388
- ___block_literal_global.1390
- ___block_literal_global.1392
- ___block_literal_global.1400
- ___block_literal_global.1416
- ___block_literal_global.1426
- ___block_literal_global.424
- ___block_literal_global.442
- ___block_literal_global.459
- ___block_literal_global.476
- ___block_literal_global.493
- ___block_literal_global.510
- ___block_literal_global.527
- ___block_literal_global.538
- ___block_literal_global.543
- _objc_msgSend$downloadTaskWithURL:completionHandler:
- _objc_msgSend$fetchDataProviderWithPriority:completion:
- _objc_msgSend$initWithPrivateDataDirectory:configurationManager:contentContext:appActivityMonitor:entitlementsProvider:
CStrings:
+ "\x11B\x16"
+ "\x12\x12\x11"
+ "-[FCAssetHandle _downloadIfNeededWithPriority:flags:completionQueue:completion:]_block_invoke"
+ "-[FCBundleSubscriptionManager initWithPrivateDataDirectory:configurationManager:cloudContext:contentContext:appActivityMonitor:entitlementsProvider:]"
+ "@40@0:8q16q24@?32"
+ "FCNewsletterManager: Already unsubscribed. Skipping operation."
+ "Successfully downloaded bundleChannelIDs list"
+ "T@\"NSNumber\",&,N,V_maxRetries"
+ "T@\"NSString\",C,N,V_handlerUID"
+ "T@\"NSString\",C,N,V_operationUID"
+ "TB,N,V_ignoreAfterSuccessfulPresentation"
+ "Tq,N,V_flags"
+ "_flags"
+ "_handlerUID"
+ "_ignoreAfterSuccessfulPresentation"
+ "_maxRetries"
+ "_operationUID"
+ "appLaunchUpsellBehaviorFlags"
+ "bundleChannelIDs list found empty.Initiating download for bundle channelIds list"
+ "disregarding event, since it failed due to task constraints"
+ "fc_failedDueToTaskConstraints"
+ "fetchDataProviderWithPriority:flags:completion:"
+ "handlerUID"
+ "ignoreAfterSuccessfulPresentation"
+ "initWithPrivateDataDirectory:configurationManager:cloudContext:contentContext:appActivityMonitor:entitlementsProvider:"
+ "launchPresentationConfigV2"
+ "liveActivityScheduleDelay"
+ "liveActivityScheduleRandomInitialDelay"
+ "liveActivityScheduleRetryCountMax"
+ "liveActivityScheduleRetryInterval"
+ "liveActivityScheduleRetryTimeWindow"
+ "liveActivityScheduleTimeWindow"
+ "liveActivityScheduledAlertsThreshold"
+ "operationUID"
+ "setAllowsConstrainedNetworkAccess:"
+ "setAllowsExpensiveNetworkAccess:"
+ "setHandlerUID:"
+ "setIgnoreAfterSuccessfulPresentation:"
+ "setMaxRetries:"
+ "setOperationUID:"
+ "widgetTelemetrySamplingRate2"
- "\x112\x16"
- "-[FCAssetHandle _downloadIfNeededWithPriority:completionQueue:completion:]_block_invoke"
- "-[FCBundleSubscriptionManager initWithPrivateDataDirectory:configurationManager:contentContext:appActivityMonitor:entitlementsProvider:]"
- "T@\"NSString\",C,N,V_uid"
- "_uid"
- "downloadTaskWithURL:completionHandler:"
- "fetchDataProviderWithPriority:completion:"
- "initWithPrivateDataDirectory:configurationManager:contentContext:appActivityMonitor:entitlementsProvider:"
- "setUid:"
- "uid"

```

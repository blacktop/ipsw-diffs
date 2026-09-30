## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3500.101.1.0.0
-  __TEXT.__text: 0x6fb14
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x34b8
-  __TEXT.__const: 0x110
+3505.9.2.0.0
+  __TEXT.__text: 0x768a8
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_methlist: 0x35a0
+  __TEXT.__const: 0x170
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__gcc_except_tab: 0x14a8
-  __TEXT.__cstring: 0xab86
-  __TEXT.__oslogstring: 0xd2de
-  __TEXT.__unwind_info: 0x1250
+  __TEXT.__cstring: 0xb0ec
+  __TEXT.__constg_swiftt: 0x48
+  __TEXT.__swift5_typeref: 0x67
+  __TEXT.__swift5_reflstr: 0x9
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__oslogstring: 0xd92b
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0x1510
+  __TEXT.__unwind_info: 0x1360
   __TEXT.__objc_classname: 0x45d
-  __TEXT.__objc_methname: 0x9afd
-  __TEXT.__objc_methtype: 0x1091
-  __TEXT.__objc_stubs: 0x7ce0
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1c60
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__objc_methname: 0x9d8c
+  __TEXT.__objc_methtype: 0x10c8
+  __TEXT.__objc_stubs: 0x7f00
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x1e00
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2588
+  __DATA_CONST.__objc_selrefs: 0x2618
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x4620
-  __AUTH_CONST.__objc_const: 0x4270
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0x628
+  __AUTH_CONST.__cfstring: 0x48c0
+  __AUTH_CONST.__objc_const: 0x4370
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x340
+  __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0x324
-  __DATA.__data: 0x238
-  __DATA.__bss: 0x20
+  __DATA.__data: 0x288
+  __DATA.__bss: 0x50
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x2d0
+  __DATA_DIRTY.__bss: 0x2e0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2EDB6CCE-AA81-3FC0-BB42-78D69FDA6A4B
-  Functions: 1442
-  Symbols:   5305
-  CStrings:  4290
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 2CCBA417-3268-335D-A780-8682B67ED95D
+  Functions: 1513
+  Symbols:   5501
+  CStrings:  4404
 
Symbols:
+ +[UAFAutoAssetManager assetSetComplete:]
+ +[UAFAutoAssetManager assetSetEmpty:]
+ +[UAFAutoAssetManager cacheAssetSetCompleteness:autoAssetSetStatus:]
+ +[UAFAutoAssetManager cacheAssetSetCompleteness:complete:]
+ +[UAFAutoAssetManager completedAtomicInstance:]
+ +[UAFAutoAssetManager completedAtomicInstances]
+ +[UAFAutoAssetManager getDownloadStatusForAssetSet:configurationManager:]
+ +[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:config:]
+ +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]
+ +[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]
+ +[UAFCommonUtilities deviceIsAudioAccessory]
+ +[UAFInstrumentationProvider _assetSetsComplete:assetSetCompleteness:]
+ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:]
+ +[UAFInstrumentationProvider _emitSubscriptionComplete:subscriber:user:assetSets:]
+ +[UAFInstrumentationProvider _emitSubscriptionCompleteForAssetSet:]
+ +[UAFInstrumentationProvider _getAssetSpecifiersForAssetSets:]
+ +[UAFInstrumentationProvider logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:]
+ +[UAFInstrumentationProvider logSubscriptionCompleteForSubscriptions:subscriber:user:]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:]
+ +[UAFPlatform platformAssetVersion:]
+ +[UAFUser uidForUser:error:]
+ GCC_except_table105
+ GCC_except_table128
+ GCC_except_table19
+ GCC_except_table38
+ GCC_except_table56
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table89
+ GCC_except_table93
+ _MGGetSInt32Answer
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_UAFAppleIntelligenceReporting
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_UAFAppleIntelligenceReporting
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __CLASS_METHODS_UAFAppleIntelligenceReporting
+ __DATA_UAFAppleIntelligenceReporting
+ __DATA__TtC21UnifiedAssetFramework19UAFAIREventReporter
+ __INSTANCE_METHODS_UAFAppleIntelligenceReporting
+ __IVARS__TtC21UnifiedAssetFramework19UAFAIREventReporter
+ __METACLASS_DATA_UAFAppleIntelligenceReporting
+ __METACLASS_DATA__TtC21UnifiedAssetFramework19UAFAIREventReporter
+ ___100-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:]_block_invoke
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.327
+ ___108-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:detailedProgress:completion:]_block_invoke
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.450
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.451
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.462
+ ___29+[UAFUserManager removeUser:]_block_invoke.293
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.302
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.308
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.309
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.310
+ ___37-[UAFAssetSetManager removeObserver:]_block_invoke
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.411
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.395
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.350
+ ___47+[UAFAutoAssetManager completedAtomicInstances]_block_invoke
+ ___49-[UAFAssetSetManager subscriptionsForSubscriber:]_block_invoke
+ ___50-[UAFAssetSetManager subscribedUsagesForAssetSet:]_block_invoke
+ ___51-[UAFAssetSetManager downloadStatusForSubscribers:]_block_invoke
+ ___51-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke_2
+ ___53+[UAFManagedSubscriptions managePlatformSubscription]_block_invoke_2
+ ___55-[UAFAssetSetManager knownUsagesForAssetSet:usageType:]_block_invoke
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.289
+ ___58-[UAFAssetSetManager diskSpaceNeededForSubscribers:error:]_block_invoke
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.419
+ ___61-[UAFAssetSetManager observeAssetSet:policies:queue:handler:]_block_invoke
+ ___63-[UAFAssetSetManager retrieveAssetSet:usages:consistencyToken:]_block_invoke
+ ___63-[UAFAssetSetManager retrieveAssetSet:usages:queue:completion:]_block_invoke
+ ___63-[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke
+ ___64+[UAFManagedSubscriptions manageAssistantSubscription:withMode:]_block_invoke
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.407
+ ___69-[UAFAssetSetManager retrieveAssetSet:usages:disableExperimentation:]_block_invoke
+ ___69-[UAFAssetSetManager unsubscribe:subscriptionNames:queue:completion:]_block_invoke
+ ___75+[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]_block_invoke
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.404
+ ___84-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.425
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.405
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.435
+ ___92-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:detailedProgress:completion:]_block_invoke
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.463
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8r72l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.340
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.391
+ ___block_literal_global.395
+ ___block_literal_global.398
+ ___block_literal_global.408
+ ___block_literal_global.410
+ ___block_literal_global.415
+ ___block_literal_global.418
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __os_activity_create
+ __os_activity_current
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_UnifiedAssetFramework
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _kUAFAIRUseCaseIdentifier
+ _kUAFEmbeddedUserUID
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_assetSetsComplete:assetSetCompleteness:
+ _objc_msgSend$_emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:
+ _objc_msgSend$_emitSubscriptionComplete:subscriber:user:assetSets:
+ _objc_msgSend$_emitSubscriptionCompleteForAssetSet:
+ _objc_msgSend$_getAssetSpecifiersForAssetSets:
+ _objc_msgSend$_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:
+ _objc_msgSend$assetSetComplete:
+ _objc_msgSend$assetSetEmpty:
+ _objc_msgSend$cacheAssetSetCompleteness:autoAssetSetStatus:
+ _objc_msgSend$cacheAssetSetCompleteness:complete:
+ _objc_msgSend$completedAtomicInstance:
+ _objc_msgSend$completedAtomicInstances
+ _objc_msgSend$getDownloadStatusForAssetSet:configurationManager:
+ _objc_msgSend$getDownloadStatusFromMAAutoAssetSetStatus:config:
+ _objc_msgSend$logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:
+ _objc_msgSend$logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:
+ _objc_msgSend$logSubscriptionCompleteForSubscriptions:subscriber:user:
+ _objc_msgSend$logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:
+ _objc_msgSend$platformAssetVersion:
+ _objc_msgSend$reason
+ _objc_msgSend$recordEvent:::
+ _objc_msgSend$uidForUser:error:
+ _objc_opt_self
+ _objc_retain_x7
+ _os_activity_apply
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic SaySSG
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 21UnifiedAssetFramework19UAFAIREventReporterC
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg 26AppleIntelligenceReporting0aB18AssetDeliveryEventV20UAFSubscriptionStateV14DownloadStatusO
+ _symbolic _____Sg 26AppleIntelligenceReporting0aB18AssetDeliveryEventV20UAFSubscriptionStateV18SubscriptionStatusO
+ _symbolic _____Sg 26AppleIntelligenceReporting0aB7UseCaseV
+ _symbolic _____Sg 26AppleIntelligenceReporting13EventReporterC
+ _symbolic ______p s5ErrorP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- +[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:]
- +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]
- +[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]
- +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetArrived:]
- GCC_except_table111
- GCC_except_table18
- GCC_except_table58
- GCC_except_table65
- GCC_except_table67
- GCC_except_table69
- GCC_except_table73
- GCC_except_table80
- GCC_except_table85
- GCC_except_table90
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.326
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.448
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.449
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.459
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.460
- ___29+[UAFUserManager removeUser:]_block_invoke.288
- ___36+[UAFUserManager performUserCleanup]_block_invoke.298
- ___36+[UAFUserManager performUserCleanup]_block_invoke.300
- ___36+[UAFUserManager performUserCleanup]_block_invoke.305
- ___36+[UAFUserManager performUserCleanup]_block_invoke.306
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.407
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.392
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.349
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.417
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.406
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.401
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.424
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.404
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.433
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.461
- ___block_descriptor_56_e8_32s40s48s_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.367
- ___block_literal_global.385
- ___block_literal_global.389
- ___block_literal_global.397
- ___block_literal_global.405
- ___block_literal_global.409
- ___block_literal_global.413
- ___block_literal_global.416
- _objc_msgSend$_emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:
- _objc_msgSend$_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:
- _objc_msgSend$getDownloadStatusFromMAAutoAssetSetStatus:
- _objc_msgSend$logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:
- _objc_msgSend$logUAFAssetSetDailyStatus:entries:assetSetArrived:
CStrings:
+ "%s Cannot update last seen time for nil user"
+ "%s Could not get configuration for for asset set %{public}@ to cache set completeness"
+ "%s Could use asset set experiment at %@: experiment id is nil"
+ "%s Emitting GMS Siri subscription change AIR event"
+ "%s Emitting Siri subscription change AIR event"
+ "%s Error %{public}@ occurred while fetching the user, so not emitting subscription complete AIR event"
+ "%s NSJSONSerialization crashed with exception: %{public}@"
+ "%s Platform asset missing from asset set id %@"
+ "%s Platform asset version missing from platform's asset metadata"
+ "%s Platform asset's metadata missing"
+ "%s Received maskable error from invalidate, suppressing error for token '%{public}@'.  Suppressed error: '%{public}@'"
+ "%s Sent Siri subscription state to AIR"
+ "%s Staging completed for %lu targets"
+ "%s Staging with platform asset version %@"
+ "%s Subscription %{public}@ for subscriber %{public}@ for user %{public}@ complete"
+ "%s Subscription %{public}@ for subscriber %{public}@ for user %{public}@ not yet complete"
+ "%s Writing Siri subscription state to AIR for user: %u. SubscriptionStatus: %{public}@"
+ "+[UAFAutoAssetManager cacheAssetSetCompleteness:autoAssetSetStatus:]"
+ "+[UAFAutoAssetManager getDownloadStatusForAssetSet:configurationManager:]"
+ "+[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:config:]"
+ "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke"
+ "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider _emitSubscriptionComplete:subscriber:user:assetSets:]"
+ "+[UAFInstrumentationProvider _emitSubscriptionCompleteForAssetSet:]"
+ "+[UAFInstrumentationProvider logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:]"
+ "+[UAFInstrumentationProvider logSubscriptionCompleteForSubscriptions:subscriber:user:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:]"
+ "+[UAFManagedSubscriptions manageAssistantSubscription:withMode:]"
+ "+[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]"
+ "+[UAFPlatform platformAssetVersion:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:]_block_invoke"
+ "-[UAFAssetSetManager knownUsagesForAssetSet:usageType:]_block_invoke"
+ "-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke_2"
+ "-[UAFAssetSetManager observeAssetSet:policies:queue:handler:]_block_invoke"
+ "-[UAFAssetSetManager removeObserver:]_block_invoke"
+ "@60@0:8@16@24@32@40B48Q52"
+ "AppleIntelligenceReporting"
+ "Cannot update last seen time for nil user"
+ "DeviceClassNumber"
+ "Failed to create EventReporter: %@"
+ "JSON serialization failed with exception"
+ "Not emitting event: missing required parameter"
+ "Recording event of type: %ld"
+ "Subscribed"
+ "UAF.diskSpaceNeededForSubscribers"
+ "UAF.downloadStatusForSubscriberAsync"
+ "UAF.downloadStatusForSubscribers"
+ "UAF.markAssetsExpired"
+ "UAF.observeAssetSet"
+ "UAF.removeObserver"
+ "UAF.retrieveAssetSetAsync"
+ "UAF.retrieveAssetSetWithDisableExperimentation"
+ "UAF.retrieveAssetSetWithToken"
+ "UAF.stagingDueToPlatformAssetUpdate"
+ "UAF.subscribe"
+ "UAF.subscribedUsagesForAssetSet"
+ "UAF.subscriptionsForSubscriber"
+ "UAF.unsubscribe"
+ "UAF.updateAssetsForSubscribers"
+ "UAFAppleIntelligenceReporting"
+ "Unknown exception"
+ "Unsubscribed"
+ "[%s] Emitting event: %s"
+ "[%s] Failed to emit event: %@"
+ "[%s] No event reporter"
+ "[%s] Successfully emitted event"
+ "_TtC21UnifiedAssetFramework19UAFAIREventReporter"
+ "_assetSetsComplete:assetSetCompleteness:"
+ "_emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:"
+ "_emitSubscriptionComplete:subscriber:user:assetSets:"
+ "_emitSubscriptionCompleteForAssetSet:"
+ "_getAssetSpecifiersForAssetSets:"
+ "_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:"
+ "action"
+ "assetSetComplete:"
+ "assetSetEmpty:"
+ "assetSetIdentifiers"
+ "batchIdentifier"
+ "cacheAssetSetCompleteness:autoAssetSetStatus:"
+ "cacheAssetSetCompleteness:complete:"
+ "com.apple.siri"
+ "completedAtomicInstance:"
+ "completedAtomicInstances"
+ "deviceIsAudioAccessory"
+ "emitAppleIntelligenceEvent(_:)"
+ "getDownloadStatusForAssetSet:configurationManager:"
+ "getDownloadStatusFromMAAutoAssetSetStatus:config:"
+ "locale"
+ "logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:"
+ "logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:"
+ "logSubscriptionCompleteForSubscriptions:subscriber:user:"
+ "logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:"
+ "mode"
+ "platformAssetVersion:"
+ "recordEvent:::"
+ "reporter"
+ "resourceSpecifiers"
+ "subscriberName"
+ "subscriptionName"
+ "subscriptionStatus"
+ "trigger"
+ "uidForUser:error:"
+ "useCaseIdentifier"
+ "userIdentifier"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16@24q32"
+ "v60@0:8@16@24@32@40B48Q52"
+ "v72@0:8@16@24I32@36@44@52q60B68"
- "%s Decoding of the asset set experiment id failed"
- "%s Received MAAutoAssetErrorSetAtomicInstanceUnknown from invalidate, suppressing error: '%{public}@'"
- "+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:]"
- "+[UAFAutoAssetManager getDownloadStatusFromMAAutoAssetSetStatus:]"
- "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:]"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetArrived:]"
- "-[UAFAssetSetExperiment initWithCoder:]"
- "-[UAFAssetSetManager downloadStatusForSubscribers:]"
- "-[UAFAssetSetManager knownUsagesForAssetSet:usageType:]"
- "-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke"
- "-[UAFAssetSetManager observeAssetSet:policies:queue:handler:]"
- "-[UAFAssetSetManager removeObserver:]"
- "_emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:"
- "_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:"
- "getDownloadStatusFromMAAutoAssetSetStatus:"
- "logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:"
- "logUAFAssetSetDailyStatus:entries:assetSetArrived:"
- "v40@0:8B16@20@28B36"
- "v56@0:8@16@24@32@40B48B52"

```

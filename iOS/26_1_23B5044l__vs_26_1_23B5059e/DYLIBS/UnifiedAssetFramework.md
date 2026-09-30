## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3505.9.2.0.0
-  __TEXT.__text: 0x768a8
+3505.15.1.0.0
+  __TEXT.__text: 0x79cdc
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x35a0
+  __TEXT.__objc_methlist: 0x3698
   __TEXT.__const: 0x170
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb0ec
+  __TEXT.__cstring: 0xb5d3
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xd92b
+  __TEXT.__oslogstring: 0xe315
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1510
-  __TEXT.__unwind_info: 0x1360
-  __TEXT.__objc_classname: 0x45d
-  __TEXT.__objc_methname: 0x9d8c
-  __TEXT.__objc_methtype: 0x10c8
-  __TEXT.__objc_stubs: 0x7f00
-  __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x1e00
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__gcc_except_tab: 0x1588
+  __TEXT.__unwind_info: 0x1390
+  __TEXT.__objc_classname: 0x472
+  __TEXT.__objc_methname: 0xa039
+  __TEXT.__objc_methtype: 0x10d1
+  __TEXT.__objc_stubs: 0x81c0
+  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__const: 0x1e90
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2618
+  __DATA_CONST.__objc_selrefs: 0x26c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x48c0
-  __AUTH_CONST.__objc_const: 0x4370
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__const: 0x648
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x4400
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x340
+  __AUTH.__objc_data: 0x390
   __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0x324
   __DATA.__data: 0x288
   __DATA.__bss: 0x50
-  __DATA.__common: 0x8
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__bss: 0x2f0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2CCBA417-3268-335D-A780-8682B67ED95D
-  Functions: 1513
-  Symbols:   5501
-  CStrings:  4404
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 607A9223-4277-3D83-B39B-FA74215A953A
+  Functions: 1535
+  Symbols:   5605
+  CStrings:  4528
 
Symbols:
+ +[UAFAutoAssetManager stageAssetSet:targets:platformAssetVersion:]
+ +[UAFCommonUtilities acquireClassAAssertion]
+ +[UAFCommonUtilities releaseClassAAssertion:]
+ +[UAFInstrumentationProvider _getAssetSpecifiersForSubscription:assetSetUsages:]
+ +[UAFInstrumentationProvider logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:]
+ +[UAFStagingLogManager createBuildVersionFile]
+ +[UAFStagingLogManager createLogEntryWithInfo:]
+ +[UAFStagingLogManager deleteItemAtURL:error:]
+ +[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]
+ +[UAFStagingLogManager findOrCreateDir:]
+ +[UAFStagingLogManager getBuildVersionFromStagingLogsDir]
+ +[UAFStagingLogManager getLastBuildStagingLogsDir]
+ +[UAFStagingLogManager getLatestStagingLogsDir]
+ +[UAFStagingLogManager getLogFileForTarget:andAssetSetName:]
+ +[UAFStagingLogManager getRootStagingLogsDir]
+ +[UAFStagingLogManager getSerialQueue]
+ +[UAFStagingLogManager logTargetSync:withAssetSetName:withPlatformAssetVersion:]
+ +[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]
+ +[UAFStagingLogManager moveItemAtURL:toURL:]
+ +[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]
+ +[UAFStagingLogManager serializeJSONObjectToData:]
+ +[UAFStagingLogManager writeToFile:content:]
+ +[UAFXPCActivity registerOnBootUAFActivityWithLockAssertion:]
+ _MKBDeviceLockAssertion
+ _OBJC_CLASS_$_UAFStagingLogManager
+ _OBJC_METACLASS_$_UAFStagingLogManager
+ _UAFLogContextStagingLogManager
+ _XPC_ACTIVITY_REQUIRES_CLASS_A
+ __OBJC_$_CLASS_METHODS_UAFStagingLogManager
+ __OBJC_CLASS_RO_$_UAFStagingLogManager
+ __OBJC_METACLASS_RO_$_UAFStagingLogManager
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.452
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.453
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.463
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.464
+ ___27-[UAFXPCService runUpdates]_block_invoke.377
+ ___27-[UAFXPCService runUpdates]_block_invoke.379
+ ___38+[UAFStagingLogManager getSerialQueue]_block_invoke
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.414
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.416
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.400
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.410
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.412
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.421
+ ___58+[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]_block_invoke
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.424
+ ___65+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]_block_invoke
+ ___77+[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]_block_invoke
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.437
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.465
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.320
+ ____RegisterXPCActivity_block_invoke.301
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.304
+ ___block_literal_global.401
+ ___block_literal_global.405
+ ___block_literal_global.413
+ ___block_literal_global.420
+ ___block_literal_global.423
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_UnifiedAssetFramework
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_UnifiedAssetFramework
+ _kUAFBuildVersion
+ _kUAFJSONExtension
+ _kUAFLastBuildVersionFilename
+ _kUAFLastStagingLogsFromLastBuild
+ _kUAFLatestStagingLogs
+ _kUAFRootStagingLogsDir
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$_getAssetSpecifiersForSubscription:assetSetUsages:
+ _objc_msgSend$acquireClassAAssertion
+ _objc_msgSend$createBuildVersionFile
+ _objc_msgSend$createLogEntryWithInfo:
+ _objc_msgSend$deleteItemAtURL:error:
+ _objc_msgSend$deleteLoggedTargetsForEliminatedAssetSet:
+ _objc_msgSend$findOrCreateDir:
+ _objc_msgSend$getBuildVersionFromStagingLogsDir
+ _objc_msgSend$getLastBuildStagingLogsDir
+ _objc_msgSend$getLatestStagingLogsDir
+ _objc_msgSend$getLogFileForTarget:andAssetSetName:
+ _objc_msgSend$getRootStagingLogsDir
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:
+ _objc_msgSend$logTargetSync:withAssetSetName:withPlatformAssetVersion:
+ _objc_msgSend$logTargets:withAssetSetName:withPlatformAssetVersion:
+ _objc_msgSend$moveItemAtURL:toURL:
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$registerOnBootUAFActivityWithLockAssertion:
+ _objc_msgSend$releaseClassAAssertion:
+ _objc_msgSend$rollStagingLogsUponNewBuildVersion
+ _objc_msgSend$serializeJSONObjectToData:
+ _objc_msgSend$stageAssetSet:targets:platformAssetVersion:
+ _objc_msgSend$writeToFile:content:
- +[UAFAutoAssetManager stageAssetSet:targets:]
- +[UAFInstrumentationProvider _getAssetSpecifiersForAssetSets:]
- +[UAFInstrumentationProvider logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:]
- __RegisterOnBootUAFActivity
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.450
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.451
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.462
- ___27-[UAFXPCService runUpdates]_block_invoke.376
- ___27-[UAFXPCService runUpdates]_block_invoke.378
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.409
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.411
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.395
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.409
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.411
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.420
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.419
- ___75+[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]_block_invoke
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.435
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.463
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.315
- ____RegisterXPCActivity_block_invoke.304
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.313
- ___block_literal_global.321
- ___block_literal_global.391
- ___block_literal_global.395
- ___block_literal_global.408
- ___block_literal_global.415
- ___block_literal_global.418
- _objc_msgSend$_getAssetSpecifiersForAssetSets:
- _objc_msgSend$logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:
- _objc_msgSend$stageAssetSet:targets:
- _objc_retain_x7
CStrings:
+ "%s %{public}@ does not contain a dictionary"
+ "%s %{public}@ does not contain valid eventInformation"
+ "%s Bad parameters passed: %{public}@"
+ "%s Cannot delete logs for nil or empty asset set name"
+ "%s Cannot find/create nil path"
+ "%s Cannot log target: invalid parameters (target: %{public}@, assetSetName: %{public}@)"
+ "%s Cannot log targets: invalid parameters (targets count: %lu, assetSetName: %{public}@)"
+ "%s Cannot serialize nil JSON object"
+ "%s Could not obtain device lock assertion: %{public}@"
+ "%s Could not stage asset set %{public}@ with error: %{public}@"
+ "%s Deleting %{public}@"
+ "%s Deleting directory that was found with the path of %{public}@"
+ "%s Deleting directory that was found with the path of the build version file %{public}@"
+ "%s Did not find %{public}@. Skip removing logs for eliminated assetSet %{public}@"
+ "%s Did not find %{public}@. Skipping rollover"
+ "%s Encountered device locked error, scheduling activity for class A unlock: %{public}@"
+ "%s Exception while parsing %{public}@: %{public}@"
+ "%s Failed to create directory at %{public}@ with error %{public}@"
+ "%s Failed to delete directory with the path of the build version file: %{public}@"
+ "%s Failed to delete existing item at %{public}@: %{public}@"
+ "%s Failed to delete item in %{public}@ with error: %{public}@"
+ "%s Failed to delete the directory: %{public}@"
+ "%s Failed to delete the old %{public}@: %{public}@. Skipping rollover"
+ "%s Failed to delete unexpected file at %{public}@: %{public}@"
+ "%s Failed to enumerate directory contents: %{public}@"
+ "%s Failed to get %{public}@"
+ "%s Failed to get default storage path"
+ "%s Failed to get log file for target %{public}@"
+ "%s Failed to get parent directory for %{public}@"
+ "%s Failed to get running build version"
+ "%s Failed to get the relevant staging directory URLs for rollover"
+ "%s Failed to move item from %{public}@ to %{public}@ with error %{public}@"
+ "%s Failed to parse %{public}@: %{public}@"
+ "%s Failed to read %{public}@: %{public}@"
+ "%s Failed to remove file %{public}@: %{public}@"
+ "%s Failed to rollover logs from %{public}@ to %{public}@"
+ "%s Failed to serialize JSON object: %{public}@"
+ "%s Failed to serialize data to json"
+ "%s Failed to write build version to %{public}@"
+ "%s Failed to write to %{public}@ with error %{public}@"
+ "%s Failed to write to log file %{public}@"
+ "%s Found unexpected file where directory should exist at %{public}@. Deleting file..."
+ "%s Invalid parameters for getLogFileForTarget: %@"
+ "%s Skipping rollover - build version %{public}@ has not changed"
+ "%s Staging with platform asset version %{public}@"
+ "%s Successfully removed log file %{public}@"
+ "%s Successfully rolled staging logs due to moving from build %{public}@ to %{public}@"
+ "%s Unable to determine the %{public}@ build version. Proceeding with rollover"
+ "+[UAFAutoAssetManager stageAssetSet:targets:platformAssetVersion:]"
+ "+[UAFCommonUtilities acquireClassAAssertion]"
+ "+[UAFInstrumentationProvider logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:]"
+ "+[UAFStagingLogManager createBuildVersionFile]"
+ "+[UAFStagingLogManager deleteItemAtURL:error:]"
+ "+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]"
+ "+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]_block_invoke"
+ "+[UAFStagingLogManager findOrCreateDir:]"
+ "+[UAFStagingLogManager getBuildVersionFromStagingLogsDir]"
+ "+[UAFStagingLogManager getLastBuildStagingLogsDir]"
+ "+[UAFStagingLogManager getLatestStagingLogsDir]"
+ "+[UAFStagingLogManager getLogFileForTarget:andAssetSetName:]"
+ "+[UAFStagingLogManager getRootStagingLogsDir]"
+ "+[UAFStagingLogManager logTargetSync:withAssetSetName:withPlatformAssetVersion:]"
+ "+[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]"
+ "+[UAFStagingLogManager moveItemAtURL:toURL:]"
+ "+[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]_block_invoke"
+ "+[UAFStagingLogManager serializeJSONObjectToData:]"
+ "+[UAFStagingLogManager writeToFile:content:]"
+ ".json"
+ "BuildVersion.json"
+ "Invalid URL path"
+ "LastStagingLogsFromLastBuildVersion"
+ "LatestStagingLogs"
+ "MKBAssertionKey"
+ "MKBAssertionTimeout"
+ "Missing assetSetName"
+ "Missing minTargetOSVersion"
+ "Other"
+ "Q24@0:8^@16"
+ "StagingLogs"
+ "UAFStagingLogManager"
+ "UAFStagingLogManager.Serial"
+ "URLByDeletingLastPathComponent"
+ "_getAssetSpecifiersForSubscription:assetSetUsages:"
+ "acquireClassAAssertion"
+ "createBuildVersionFile"
+ "createLogEntryWithInfo:"
+ "deleteItemAtURL:error:"
+ "deleteLoggedTargetsForEliminatedAssetSet:"
+ "empty content"
+ "eventInformation"
+ "findOrCreateDir:"
+ "getBuildVersionFromStagingLogsDir"
+ "getLastBuildStagingLogsDir"
+ "getLatestStagingLogsDir"
+ "getLogFileForTarget:andAssetSetName:"
+ "getRootStagingLogsDir"
+ "initWithCapacity:"
+ "logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:"
+ "logTargetSync:withAssetSetName:withPlatformAssetVersion:"
+ "logTargets:withAssetSetName:withPlatformAssetVersion:"
+ "moveItemAtURL:toURL:"
+ "moveItemAtURL:toURL:error:"
+ "nil filePath"
+ "platformAssetVersion"
+ "registerOnBootUAFActivityWithLockAssertion:"
+ "releaseClassAAssertion:"
+ "rollStagingLogsUponNewBuildVersion"
+ "running"
+ "serializeJSONObjectToData:"
+ "stageAssetSet:targets:platformAssetVersion:"
+ "stored"
+ "v24@0:8^v16"
+ "v32@0:8@16Q24"
+ "v36@0:8B16@20Q28"
+ "v64@0:8@16@24@32I40@44Q52B60"
+ "valid"
+ "writeToFile:content:"
- "%s Could get not stage asset set %{public}@ for other OS versions: %{public}@"
- "%s Emitting GMS Siri subscription change AIR event"
- "%s Staging with platform asset version %@"
- "+[UAFAutoAssetManager stageAssetSet:targets:]"
- "+[UAFInstrumentationProvider logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:]"
- "+[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]"
- "_getAssetSpecifiersForAssetSets:"
- "logSiriSubscription:subscriber:userId:assetSets:locale:countryCode:mode:unsubscribed:"
- "q24@0:8^@16"
- "stageAssetSet:targets:"
- "v32@0:8@16q24"
- "v36@0:8B16@20q28"
- "v72@0:8@16@24I32@36@44@52q60B68"

```

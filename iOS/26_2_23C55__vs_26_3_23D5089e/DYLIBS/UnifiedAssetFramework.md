## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3510.1.1.0.0
-  __TEXT.__text: 0x79dd4
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x3698
+3515.4.2.0.0
+  __TEXT.__text: 0x7be30
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x3748
   __TEXT.__const: 0x1c0
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb5d3
+  __TEXT.__cstring: 0xb791
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xe37a
+  __TEXT.__oslogstring: 0xeb1d
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1588
-  __TEXT.__unwind_info: 0x1390
-  __TEXT.__objc_classname: 0x472
-  __TEXT.__objc_methname: 0xa039
-  __TEXT.__objc_methtype: 0x10d1
-  __TEXT.__objc_stubs: 0x81c0
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x1e90
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__gcc_except_tab: 0x15d0
+  __TEXT.__unwind_info: 0x13e0
+  __TEXT.__objc_classname: 0x483
+  __TEXT.__objc_methname: 0xa297
+  __TEXT.__objc_methtype: 0x10dd
+  __TEXT.__objc_stubs: 0x8380
+  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__const: 0x1eb8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26c8
+  __DATA_CONST.__objc_selrefs: 0x2748
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0x648
-  __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x4400
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0xd8
+  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__const: 0x668
+  __AUTH_CONST.__cfstring: 0x4be0
+  __AUTH_CONST.__objc_const: 0x4540
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x390
+  __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x288
   __DATA.__bss: 0x50
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ABEEDEB5-D987-35E8-BC79-C9F0FBDEEDD2
-  Functions: 1535
-  Symbols:   5605
-  CStrings:  4529
+  UUID: 6F0CFC02-345A-32E7-8F19-A10AEFE3D45C
+  Functions: 1552
+  Symbols:   5674
+  CStrings:  4604
 
Symbols:
+ +[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]
+ +[UAFCommonUtilities bestSupportedSiriLanguage]
+ +[UAFInstrumentationProvider _deepestUnderlyingError:]
+ +[UAFPrestageConfiguration computePredicateKeys]
+ +[UAFPrestageConfiguration predicateMatch:predicateKeys:]
+ -[UAFConfigurationManager getPrestageSubscriptions]
+ -[UAFOSEligibility .cxx_destruct]
+ -[UAFOSEligibility _eligibilityCountryPolicyStringIsChina:]
+ -[UAFOSEligibility _updateCountryPolicy:]
+ -[UAFOSEligibility _updateDeviceLanguage:]
+ -[UAFOSEligibility _updateEligibilityData]
+ -[UAFOSEligibility _updateSiriLanguage:]
+ -[UAFOSEligibility gmsLanguage]
+ -[UAFOSEligibility init]
+ -[UAFOSEligibility siriLanguage]
+ -[UAFPrestageConfiguration identifier]
+ -[UAFPrestageConfiguration osVersionConfigMatch:]
+ -[UAFPrestageConfiguration setIdentifier:]
+ -[UAFPrestageConfiguration setSubscriptions:]
+ -[UAFPrestageConfiguration subscriptions:]
+ -[UAFPrestageConfiguration subscriptions]
+ -[UAFXPCService _updateShadowSiriLocale:]
+ -[UAFXPCService _updateShadowSiriLocaleIfNeeded]
+ GCC_except_table57
+ _OBJC_CLASS_$_UAFOSEligibility
+ _OBJC_IVAR_$_UAFOSEligibility._gmsLanguage
+ _OBJC_IVAR_$_UAFOSEligibility._siriLanguage
+ _OBJC_IVAR_$_UAFPrestageConfiguration._currentOSVersion
+ _OBJC_IVAR_$_UAFPrestageConfiguration._identifier
+ _OBJC_IVAR_$_UAFPrestageConfiguration._predicateKeys
+ _OBJC_IVAR_$_UAFPrestageConfiguration._subscriptions
+ _OBJC_METACLASS_$_UAFOSEligibility
+ __OBJC_$_INSTANCE_METHODS_UAFOSEligibility
+ __OBJC_$_INSTANCE_VARIABLES_UAFOSEligibility
+ __OBJC_$_PROP_LIST_UAFOSEligibility
+ __OBJC_CLASS_RO_$_UAFOSEligibility
+ __OBJC_METACLASS_RO_$_UAFOSEligibility
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.327
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.361
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.362
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.452
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.453
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.463
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.464
+ ___27-[UAFXPCService runUpdates]_block_invoke.375
+ ___27-[UAFXPCService runUpdates]_block_invoke.377
+ ___27-[UAFXPCService runUpdates]_block_invoke.379
+ ___29+[UAFUserManager removeUser:]_block_invoke.293
+ ___31-[UAFXPCConnection _connection]_block_invoke.291
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.302
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.304
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.308
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.309
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.310
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.310
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.414
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.416
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.299
+ ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke
+ ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.436
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.400
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.294
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.350
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.336
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.334
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.328
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.292
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.341
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.410
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.412
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.297
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.314
+ ___51-[UAFConfigurationManager getPrestageSubscriptions]_block_invoke
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.293
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.341
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.342
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.331
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.421
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.296
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.289
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.424
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.300
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.317
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.313
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.310
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.332
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.407
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.298
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.300
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.301
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.312
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.317
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.328
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.330
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.331
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.300
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.404
+ ___86+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]_block_invoke
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.425
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.405
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.437
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.465
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.319
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.320
+ ____RegisterXPCActivity_block_invoke.301
+ ___block_literal_global.289
+ ___block_literal_global.303
+ ___block_literal_global.304
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.310
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.326
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.368
+ ___block_literal_global.370
+ ___block_literal_global.373
+ ___block_literal_global.398
+ ___block_literal_global.401
+ ___block_literal_global.405
+ ___block_literal_global.413
+ ___block_literal_global.420
+ ___block_literal_global.423
+ _kUAFConfShadowSiriLocale
+ _kUAFIdentifier
+ _kUAFName
+ _kUAFPrestageFileVersion_1_1_0
+ _kUAFUsageAliases
+ _objc_msgSend$_deepestUnderlyingError:
+ _objc_msgSend$_updateCountryPolicy:
+ _objc_msgSend$_updateDeviceLanguage:
+ _objc_msgSend$_updateEligibilityData
+ _objc_msgSend$_updateShadowSiriLocale:
+ _objc_msgSend$_updateShadowSiriLocaleIfNeeded
+ _objc_msgSend$_updateSiriLanguage:
+ _objc_msgSend$bestSupportedLanguageCodeForLanguageCode:
+ _objc_msgSend$bestSupportedSiriLanguage
+ _objc_msgSend$computePredicateKeys
+ _objc_msgSend$firstObject
+ _objc_msgSend$getPrestageSubscriptions
+ _objc_msgSend$gmsLanguage
+ _objc_msgSend$initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:sourceOSBuild:promotedOSBuild:
+ _objc_msgSend$initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:fromFactory:
+ _objc_msgSend$initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:alteredAssetSets:eliminatedAssetSets:
+ _objc_msgSend$osVersionConfigMatch:
+ _objc_msgSend$predicateMatch:predicateKeys:
+ _objc_msgSend$siriLanguage
+ _objc_msgSend$stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:
+ _objc_msgSend$subscriptions
+ _objc_msgSend$subscriptions:
+ _os_eligibility_get_domain_answer
+ _xpc_array_get_count
+ _xpc_array_get_string
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_string
- +[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]
- +[UAFPrestageConfiguration predicateMatch:]
- -[UAFConfigurationManager getPrestage:]
- -[UAFPrestageConfiguration mergeAssetSetUsages:]
- -[UAFPrestageConfiguration name]
- -[UAFPrestageConfiguration setName:]
- -[UAFPrestageConfiguration setUsages:]
- -[UAFPrestageConfiguration usages:]
- -[UAFPrestageConfiguration usages]
- GCC_except_table56
- _NSFileType
- _NSFileTypeRegular
- _OBJC_IVAR_$_UAFPrestageConfiguration._name
- _OBJC_IVAR_$_UAFPrestageConfiguration._usages
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.336
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.370
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.371
- ___123+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.462
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.472
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.473
- ___27-[UAFXPCService runUpdates]_block_invoke.384
- ___27-[UAFXPCService runUpdates]_block_invoke.386
- ___27-[UAFXPCService runUpdates]_block_invoke.388
- ___29+[UAFUserManager removeUser:]_block_invoke.302
- ___31-[UAFXPCConnection _connection]_block_invoke.300
- ___36+[UAFUserManager performUserCleanup]_block_invoke.311
- ___36+[UAFUserManager performUserCleanup]_block_invoke.313
- ___36+[UAFUserManager performUserCleanup]_block_invoke.317
- ___36+[UAFUserManager performUserCleanup]_block_invoke.318
- ___36+[UAFUserManager performUserCleanup]_block_invoke.319
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.319
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.423
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.425
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.308
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.409
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.303
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.359
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.345
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.343
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.337
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.301
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.350
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.419
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.421
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.306
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.323
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.302
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.350
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.351
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.340
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.430
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.305
- ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.298
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.433
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.309
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.326
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.322
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.319
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.341
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.416
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.307
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.309
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.310
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.321
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.326
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.337
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.339
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.340
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.309
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.411
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.412
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.413
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.434
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.414
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.446
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.474
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.328
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.329
- ____RegisterXPCActivity_block_invoke.310
- ___block_literal_global.298
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.314
- ___block_literal_global.316
- ___block_literal_global.318
- ___block_literal_global.321
- ___block_literal_global.328
- ___block_literal_global.332
- ___block_literal_global.335
- ___block_literal_global.339
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.349
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.382
- ___block_literal_global.407
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.422
- ___block_literal_global.429
- ___block_literal_global.432
- _objc_msgSend$attributesOfItemAtPath:error:
- _objc_msgSend$getPrestage:
- _objc_msgSend$initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:
- _objc_msgSend$initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:
- _objc_msgSend$initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:
- _objc_msgSend$mergeAssetSetUsages:
- _objc_msgSend$stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:
- _objc_msgSend$usages:
CStrings:
+ "%s %{public}@: %{public}@ predicate does not match: %{public}@"
+ "%s %{public}@: %{public}@ predicate match: %{public}@"
+ "%s Adding prestage subscriptions from '%{public}@': %{public}@"
+ "%s Config identifier %{public}@, name %{public}@ does not match current OS version"
+ "%s Could not create subscription from prestaging identifier '%{public}@' with name '%{public}@'"
+ "%s Could not evaluate predicate string: %{public}@"
+ "%s Could not get OS_ELIGIBILITY_DOMAIN_GREYMATTER: %d: %s"
+ "%s Could not get Siri language"
+ "%s Could not init UAFPrestageConfiguration from %{public}@: %{public}@"
+ "%s Could not set potential siri locale to %{public}@: %{public}@"
+ "%s Device language array is empty"
+ "%s Eligibility returned no context.  error: %d, answer: %d source: %d"
+ "%s Evaluating predicate string: '%{public}@' with keys: %{public}@"
+ "%s Failed to configureAssetDelivery after updating Shadow Siri Locale: %{public}@"
+ "%s Failed to load UAFPrestageConfiguration dictionary from \"%@\": %@"
+ "%s Failed to validate UAFPrestageConfiguration dictionary from \"%@\""
+ "%s No device languages found"
+ "%s OS_ELIGIBILITY_DOMAIN_GREYMATTER is forced and will not produce configuration values.  Unset with `eligibility_util reset OS_ELIGIBILITY_DOMAIN_GREYMATTER`"
+ "%s One or both of Usages or UsageAliases must be specified in a ValidConfig"
+ "%s Set potential siri locale to %{public}@"
+ "%s Unable to retrieve preferred device language string"
+ "%s Underlying error: %u found while logging MA availableForUseError error for asset set %{public}@ with ID: %{public}@:"
+ "%s Underlying error: %u found while logging MA newerVersionError error for asset set %{public}@ with ID: %{public}@:"
+ "%s Usage for '%{public}@' is expected to be a string \"%{public}@\""
+ "%s Usage value for '%{public}@' is expected to be a dictionary \"%{public}@\""
+ "%s UsageAlias for '%{public}@' is expected to be a string \"%{public}@\""
+ "%s UsageAlias value for '%{public}@' is expected to be a string \"%{public}@\""
+ "%s UsageType for '%{public}@'/'%{public}@' is expected to be a string \"%{public}@\""
+ "%s UsageType value for ''%{public}@'/'%{public}@/'%{public}@' is expected to be a string \"%{public}@\""
+ "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]"
+ "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]_block_invoke"
+ "+[UAFPrestageConfiguration predicateMatch:predicateKeys:]"
+ "-[UAFConfigurationManager getPrestageSubscriptions]"
+ "-[UAFConfigurationManager getPrestageSubscriptions]_block_invoke"
+ "-[UAFOSEligibility _updateDeviceLanguage:]"
+ "-[UAFOSEligibility _updateEligibilityData]"
+ "-[UAFOSEligibility _updateSiriLanguage:]"
+ "-[UAFPrestageConfiguration subscriptions:]"
+ "-[UAFXPCService _updateShadowSiriLocale:]_block_invoke"
+ "1.1.0"
+ "B24@0:8r*16"
+ "CHN"
+ "CN"
+ "EligibleAppleIntelligenceDeviceLanguage"
+ "EligibleAppleIntelligenceSiriLanguage"
+ "Identifier"
+ "Name"
+ "OS_ELIGIBILITY_CONTEXT_ELIGIBLE_DEVICE_LANGUAGES"
+ "OS_ELIGIBILITY_CONTEXT_ELIGIBLE_SIRI_LANGUAGE"
+ "ShadowSiriLocale"
+ "T@\"NSArray\",&,N,V_subscriptions"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",R,N,V_gmsLanguage"
+ "T@\"NSString\",R,N,V_siriLanguage"
+ "UAFOSEligibility"
+ "_currentOSVersion"
+ "_deepestUnderlyingError:"
+ "_eligibilityCountryPolicyStringIsChina:"
+ "_gmsLanguage"
+ "_identifier"
+ "_predicateKeys"
+ "_subscriptions"
+ "_updateCountryPolicy:"
+ "_updateDeviceLanguage:"
+ "_updateEligibilityData"
+ "_updateShadowSiriLocale:"
+ "_updateShadowSiriLocaleIfNeeded"
+ "_updateSiriLanguage:"
+ "bestSupportedLanguageCodeForLanguageCode:"
+ "bestSupportedSiriLanguage"
+ "computePredicateKeys"
+ "firstObject"
+ "getPrestageSubscriptions"
+ "gmsLanguage"
+ "identifier"
+ "initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:sourceOSBuild:promotedOSBuild:"
+ "initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:fromFactory:"
+ "initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:alteredAssetSets:eliminatedAssetSets:"
+ "osVersionConfigMatch:"
+ "predicateMatch:predicateKeys:"
+ "setIdentifier:"
+ "setSubscriptions:"
+ "stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:"
+ "subscriptions"
+ "subscriptions:"
- "%s Underlying error: %u found while logging MA download error for asset set %{public}@ with ID: %{public}@:"
- "%s Usage is not expected kind \"%@\""
- "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]"
- "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke"
- "+[UAFPrestageConfiguration predicateMatch:]"
- "-[UAFConfigurationManager getPrestage:]"
- "SystemLanguage"
- "T@\"NSArray\",&,N,V_usages"
- "attributesOfItemAtPath:error:"
- "getPrestage:"
- "initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:"
- "initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:"
- "initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:"
- "mergeAssetSetUsages:"
- "setUsages:"
- "stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:"
- "usages:"

```

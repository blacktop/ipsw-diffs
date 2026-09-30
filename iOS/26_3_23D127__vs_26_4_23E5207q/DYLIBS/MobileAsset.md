## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.80.27.0.1
-  __TEXT.__text: 0x86b1c
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x6abc
+1837.100.235.0.0
+  __TEXT.__text: 0x8d9f4
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_methlist: 0x6aac
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x11f4e
-  __TEXT.__oslogstring: 0xab0c
-  __TEXT.__gcc_except_tab: 0x13bc
-  __TEXT.__unwind_info: 0x1c00
-  __TEXT.__objc_classname: 0x8ef
-  __TEXT.__objc_methname: 0x17a4f
-  __TEXT.__objc_methtype: 0x1867
-  __TEXT.__objc_stubs: 0x8a80
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0x20f8
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__cstring: 0x128ce
+  __TEXT.__oslogstring: 0xaf04
+  __TEXT.__gcc_except_tab: 0x1350
+  __TEXT.__unwind_info: 0x1ef8
+  __TEXT.__objc_classname: 0x94b
+  __TEXT.__objc_methname: 0x17820
+  __TEXT.__objc_methtype: 0x1819
+  __TEXT.__objc_stubs: 0x8b00
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x23f8
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3540
+  __DATA_CONST.__objc_selrefs: 0x3578
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x238
-  __DATA_CONST.__objc_arraydata: 0x2f8
-  __AUTH_CONST.__auth_got: 0x510
-  __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0xe9c0
-  __AUTH_CONST.__objc_const: 0xa700
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_arraydata: 0x2f0
+  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__cfstring: 0xf340
+  __AUTH_CONST.__objc_const: 0xa7a0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x8fc
+  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x8f0
   __DATA.__data: 0x358
-  __DATA.__bss: 0x170
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B3262FB-36F5-3A71-83C7-7B0A9493A424
-  Functions: 2932
-  Symbols:   8860
-  CStrings:  7443
+  UUID: 8E64D1B0-488B-3CFB-8BE2-2230C4027BA5
+  Functions: 2967
+  Symbols:   9032
+  CStrings:  7612
 
Symbols:
+ +[MAAsset getClientIdentifierForSelf]
+ +[MAAssetTypeDescriptor _assetTypeDescriptors]
+ +[MAAssetTypeDescriptor _assetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _loadDescriptorsFromPath:intoDictionary:]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors]
+ +[MAAssetTypeDescriptor _secureAssetTypeDescriptors].cold.1
+ +[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]
+ +[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]
+ +[MAAssetTypeDescriptor descriptorForAssetType:]
+ +[MAAssetTypeDescriptor typeDescriptorsToDataVault]
+ +[MAAssetTypeDescriptor typeDescriptorsToRemoveV1Assets]
+ +[MAAutoAsset(RelinquishShared) _relinquishEstimateEvictableBytesIsSynchronous:completion:]
+ +[MAAutoAsset(RelinquishShared) _relinquishResumeIsSynchronous:completion:]
+ +[MAAutoAsset(RelinquishShared) _relinquishStatusIsSynchronous:completion:]
+ +[MAAutoAsset(RelinquishShared) _relinquishSuspendIsSynchronous:neededBytes:completion:]
+ +[MAAutoAsset(RelinquishShared) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo supportsSecureCoding]
+ +[MARelinquish _statusIsSynchronous:clientDomainName:assetSetIdentifier:completion:]
+ +[MARelinquish estimateEvictableBytesSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:]
+ +[MARelinquish estimateEvictableBytesWithCompletion:]
+ +[MARelinquish resumeSyncWithReturnResumeErrorPtr:]
+ +[MARelinquish resumeWithCompletion:]
+ +[MARelinquish statusSyncWithClientDomainName:assetSetIdentifier:returnStatusErrorPtr:]
+ +[MARelinquish statusSyncWithReturnStatusErrorPtr:]
+ +[MARelinquish statusWithClientDomainName:assetSetIdentifier:completion:]
+ +[MARelinquish statusWithCompletion:]
+ +[MARelinquish suspendSyncWithNeededBytes:returnSuspendErrorPtr:]
+ +[MARelinquish suspendWithNeededBytes:completion:]
+ -[MAAssetTypeDescriptor .cxx_destruct]
+ -[MAAssetTypeDescriptor assetProperties]
+ -[MAAssetTypeDescriptor assetSpecifiers]
+ -[MAAssetTypeDescriptor assetType]
+ -[MAAssetTypeDescriptor description]
+ -[MAAssetTypeDescriptor initWithAssetType:]
+ -[MAAssetTypeDescriptor isSecure]
+ -[MAAssetTypeDescriptor shouldMakeDataVault]
+ -[MAAssetTypeDescriptor shouldRemoveV1Assets]
+ -[MAAutoAsset _stageDownloadStatusProgress:stageProgressError:progressBlock:]
+ -[MAAutoAssetSetOverview initWithDomainName:forAssetSetIdentifier:withConfiguredAssetEntries:withLatestDownloadedAtomicInstance:withDownloadedAtomicInstances:withDiscoveredAtomicInstance:withActiveClientCount:withMaximumClientCount:withTotalClientCount:]
+ -[MAAutoAssetSummary initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withMaximumClientCount:withTotalClientCount:]
+ -[MAAutoAssetSummary initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withMaximumClientCount:withTotalClientCount:withIsSecureMobileAsset:withPersonalizationStatus:withPrePersonalizationStatus:withGraftStatus:withGraftPoint:withStageGroupType:withTargetOS:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo .cxx_destruct]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo assetSetIdentifier]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo clientDomainName]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo initWithClientDomainName:assetSetIdentifier:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo init]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo summary]
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table175
+ GCC_except_table181
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table228
+ GCC_except_table233
+ GCC_except_table240
+ GCC_except_table245
+ GCC_except_table267
+ GCC_except_table27
+ GCC_except_table277
+ GCC_except_table28
+ GCC_except_table282
+ GCC_except_table288
+ GCC_except_table293
+ GCC_except_table299
+ GCC_except_table304
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyMultiple
+ _CFPreferencesCopyValue
+ _CFPreferencesSetAppValue
+ _MAPreferencesCopyNSArrayOfNumbersValue
+ _MAPreferencesCopyNSArrayOfStringsValue
+ _MAPreferencesCopyNSDataValue
+ _MAPreferencesCopyNSDictionaryValue
+ _MAPreferencesCopyNSStringValue
+ _MAPreferencesCopyValue
+ _MAPreferencesGetAll
+ _MAPreferencesGetAppBooleanValue
+ _MAPreferencesGetAppIntegerValue
+ _MAPreferencesIsCentralizedCacheDeleteEnabled
+ _MAPreferencesIsCentralizedCacheDeleteEnabled._centralizedCacheDeleteEnabled
+ _MAPreferencesIsCentralizedCacheDeleteEnabled.cold.1
+ _MAPreferencesIsCentralizedCacheDeleteEnabled.onceToken
+ _MAPreferencesIsForceKeyManager5XXErrorEnabled
+ _MAPreferencesIsForceKeyManager5XXErrorEnabled._forceKeyManager5XXErrorEnabled
+ _MAPreferencesIsForceKeyManager5XXErrorEnabled.cold.1
+ _MAPreferencesIsForceKeyManager5XXErrorEnabled.onceToken
+ _MAPreferencesIsInternalAllowed
+ _MAPreferencesIsInternalAllowed._isAppleInternal
+ _MAPreferencesIsInternalAllowed.cold.1
+ _MAPreferencesIsInternalAllowed.onceToken
+ _MAPreferencesIsVerboseLoggingEnabled
+ _MAPreferencesIsVerboseLoggingEnabled._verboseLoggingEnabled
+ _MAPreferencesIsVerboseLoggingEnabled.cold.1
+ _MAPreferencesIsVerboseLoggingEnabled.onceToken
+ _MAPreferencesSetDataValue
+ _MAPreferencesSetStringValue
+ _MAPreferencesSetValues
+ _MAPreferencesSync
+ _MARelinquishStatusString
+ _NSURLIsRegularFileKey
+ _OBJC_CLASS_$_MAAssetTypeDescriptor
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ _OBJC_CLASS_$_MARelinquish
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._assetType
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._isSecure
+ _OBJC_IVAR_$_MAAssetTypeDescriptor._typeDescriptor
+ _OBJC_IVAR_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo._assetSetIdentifier
+ _OBJC_IVAR_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo._clientDomainName
+ _OBJC_METACLASS_$_MAAssetTypeDescriptor
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ _OBJC_METACLASS_$_MARelinquish
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __MAPreferencesCopyArrayOfNumbers
+ __MAPreferencesCopyArrayOfStrings
+ __MAPreferencesCopyValue.cold.1
+ __MAPreferencesSetKeyForValue
+ __OBJC_$_CLASS_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_CLASS_METHODS_MAAutoAsset(RelinquishShared|SoftwareUpdateSuspendResume)
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_$_CLASS_METHODS_MARelinquish
+ __OBJC_$_INSTANCE_METHODS_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_$_INSTANCE_VARIABLES_MAAssetTypeDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_$_PROP_LIST_MAAssetTypeDescriptor
+ __OBJC_$_PROP_LIST_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_CLASS_RO_$_MAAssetTypeDescriptor
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_CLASS_RO_$_MARelinquish
+ __OBJC_METACLASS_RO_$_MAAssetTypeDescriptor
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo
+ __OBJC_METACLASS_RO_$_MARelinquish
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.988
+ ___107+[MARelinquish estimateEvictableBytesSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:]_block_invoke
+ ___108+[MAAutoAsset(RelinquishShared) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke
+ ___108+[MAAutoAsset(RelinquishShared) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.468
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.671
+ ___37+[MARelinquish resumeWithCompletion:]_block_invoke
+ ___37+[MARelinquish resumeWithCompletion:]_block_invoke_2
+ ___37+[MARelinquish statusWithCompletion:]_block_invoke
+ ___37+[MARelinquish statusWithCompletion:]_block_invoke_2
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1218
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1219
+ ___46+[MAAssetTypeDescriptor _assetTypeDescriptors]_block_invoke
+ ___50+[MARelinquish suspendWithNeededBytes:completion:]_block_invoke
+ ___50+[MARelinquish suspendWithNeededBytes:completion:]_block_invoke_2
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1209
+ ___51+[MARelinquish resumeSyncWithReturnResumeErrorPtr:]_block_invoke
+ ___51+[MARelinquish statusSyncWithReturnStatusErrorPtr:]_block_invoke
+ ___52+[MAAssetTypeDescriptor _secureAssetTypeDescriptors]_block_invoke
+ ___53+[MARelinquish estimateEvictableBytesWithCompletion:]_block_invoke
+ ___53+[MARelinquish estimateEvictableBytesWithCompletion:]_block_invoke_2
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1250
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke
+ ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke_2
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.965
+ ___65+[MARelinquish suspendSyncWithNeededBytes:returnSuspendErrorPtr:]_block_invoke
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.710
+ ___73+[MARelinquish statusWithClientDomainName:assetSetIdentifier:completion:]_block_invoke
+ ___73+[MARelinquish statusWithClientDomainName:assetSetIdentifier:completion:]_block_invoke_2
+ ___75+[MAAutoAsset(RelinquishShared) _relinquishResumeIsSynchronous:completion:]_block_invoke
+ ___75+[MAAutoAsset(RelinquishShared) _relinquishStatusIsSynchronous:completion:]_block_invoke
+ ___79+[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]_block_invoke
+ ___84+[MARelinquish _statusIsSynchronous:clientDomainName:assetSetIdentifier:completion:]_block_invoke
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.703
+ ___87+[MARelinquish statusSyncWithClientDomainName:assetSetIdentifier:returnStatusErrorPtr:]_block_invoke
+ ___88+[MAAutoAsset(RelinquishShared) _relinquishSuspendIsSynchronous:neededBytes:completion:]_block_invoke
+ ___91+[MAAutoAsset(RelinquishShared) _relinquishEstimateEvictableBytesIsSynchronous:completion:]_block_invoke
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1213
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1214
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1217
+ ___Block_byref_object_copy_.1384
+ ___Block_byref_object_copy_.765
+ ___Block_byref_object_copy_.886
+ ___Block_byref_object_dispose_.1385
+ ___Block_byref_object_dispose_.766
+ ___Block_byref_object_dispose_.887
+ ___MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke
+ ___MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke.cold.1
+ ___MAPreferencesIsForceKeyManager5XXErrorEnabled_block_invoke
+ ___MAPreferencesIsForceKeyManager5XXErrorEnabled_block_invoke.cold.1
+ ___MAPreferencesIsInternalAllowed_block_invoke
+ ___MAPreferencesIsVerboseLoggingEnabled_block_invoke
+ ___MAPreferencesIsVerboseLoggingEnabled_block_invoke.cold.1
+ ___MAPreferencesSetDataValue_block_invoke
+ ___MAPreferencesSetStringValue_block_invoke
+ ___MAPreferencesSetValues_block_invoke
+ ___MAPreferencesSetValues_block_invoke_2
+ ___MAPreferencesSync_block_invoke
+ ____MAPreferencesCopyValue_block_invoke.1510
+ ____MAPreferencesCopyValue_block_invoke_2
+ ____MAensureExtension_block_invoke.1391
+ ____MAsendDownloadAsset_block_invoke.1295
+ ____MAsendPMVCancelDownload_block_invoke.1313
+ ____MAsendPMVDownload_block_invoke.1301
+ ____useDaemonPreferencesLogic_block_invoke
+ ___block_descriptor_32_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e23_v28?0B8Q12"NSError"20ls32l8
+ ___block_descriptor_48_e8_32s40r_e29_v32?08"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_literal_global.1024
+ ___block_literal_global.1026
+ ___block_literal_global.1028
+ ___block_literal_global.1031
+ ___block_literal_global.1204
+ ___block_literal_global.1208
+ ___block_literal_global.1212
+ ___block_literal_global.1215
+ ___block_literal_global.1232
+ ___block_literal_global.1253
+ ___block_literal_global.1259
+ ___block_literal_global.1269
+ ___block_literal_global.1274
+ ___block_literal_global.1298
+ ___block_literal_global.1491
+ ___block_literal_global.1513
+ ___block_literal_global.1516
+ ___block_literal_global.1518
+ ___block_literal_global.1523
+ ___block_literal_global.1525
+ ___block_literal_global.1527
+ ___block_literal_global.1530
+ ___block_literal_global.2929
+ ___block_literal_global.2931
+ ___block_literal_global.2933
+ ___block_literal_global.2935
+ ___block_literal_global.513
+ ___block_literal_global.544
+ ___block_literal_global.550
+ ___block_literal_global.552
+ ___block_literal_global.612
+ ___block_literal_global.761
+ ___block_literal_global.774
+ ___block_literal_global.780
+ ___block_literal_global.782
+ ___block_literal_global.904
+ ___block_literal_global.909
+ ___block_literal_global.911
+ ___block_literal_global.913
+ __assetTypeDescriptors.assetTypeDescriptors
+ __assetTypeDescriptors.onceToken
+ __secureAssetTypeDescriptors.onceToken
+ __secureAssetTypeDescriptors.secureAssetTypeDescriptors
+ __useDaemonPreferencesLogic.onceToken
+ __useDaemonPreferencesLogic.usingDaemonPreferences
+ _isValidTypeForPreferences
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kMobileAssetPreferencesAnalyticsClearOnLaunch
+ _kMobileAssetPreferencesAnalyticsClientNameTestToolOverride
+ _kMobileAssetPreferencesAnalyticsClientNameTestToolPrepend
+ _kMobileAssetPreferencesAnalyticsLevelOnLaunch
+ _kMobileAssetPreferencesAnalyticsSendImmediate
+ _kMobileAssetPreferencesAnalyticsSubmitOnLaunch
+ _kMobileAssetPreferencesAutoAssetActivityAggressiveAssetType
+ _kMobileAssetPreferencesAutoAssetActivityAggressiveIntervalSecs
+ _kMobileAssetPreferencesAutoAssetActivityHeightenedAssetType
+ _kMobileAssetPreferencesAutoAssetActivityHeightenedIntervalSecs
+ _kMobileAssetPreferencesAutoAssetActivityIntervalSecs
+ _kMobileAssetPreferencesAutoAssetActivityTickerSecs
+ _kMobileAssetPreferencesAutoAssetAlwaysPromoteStagedAssets
+ _kMobileAssetPreferencesAutoAssetAsIfBackground
+ _kMobileAssetPreferencesAutoAssetAsIfBootedOSIsBuildVersion
+ _kMobileAssetPreferencesAutoAssetAsIfBootedOSIsOSVersion
+ _kMobileAssetPreferencesAutoAssetAsIfRamp
+ _kMobileAssetPreferencesAutoAssetBeforeFirstDefaultTimeoutSecs
+ _kMobileAssetPreferencesAutoAssetBeforeFirstPollSecs
+ _kMobileAssetPreferencesAutoAssetConnectorBackoffRetryTimes
+ _kMobileAssetPreferencesAutoAssetConnectorInitialWaitSecs
+ _kMobileAssetPreferencesAutoAssetConnectorWaitBeforeRetrySecs
+ _kMobileAssetPreferencesAutoAssetLogSetCompare
+ _kMobileAssetPreferencesAutoAssetLookupCacheAssetSelectorValidSecs
+ _kMobileAssetPreferencesAutoAssetLookupCacheSetConfigurationValidSecs
+ _kMobileAssetPreferencesAutoAssetMaxStagerDeterminingSecs
+ _kMobileAssetPreferencesAutoAssetNoPersistedOverflowLimit
+ _kMobileAssetPreferencesAutoAssetObserverIgnoreNetworkStatus
+ _kMobileAssetPreferencesAutoAssetPerformanceLoggingEnabled
+ _kMobileAssetPreferencesAutoAssetPersistedTableLoggingEnabled
+ _kMobileAssetPreferencesAutoAssetPushActivityIntervalSecs
+ _kMobileAssetPreferencesAutoAssetScheduledAlwaysNonDiscretionary
+ _kMobileAssetPreferencesAutoAssetScheduledAsIfNotInternal
+ _kMobileAssetPreferencesAutoAssetScheduledBackupTriggersDisabled
+ _kMobileAssetPreferencesAutoAssetScheduledOnlyForAssetTypes
+ _kMobileAssetPreferencesAutoAssetSecureMonitorBackoffRetryTimes
+ _kMobileAssetPreferencesAutoAssetSecureMonitorJitterMaxSecs
+ _kMobileAssetPreferencesAutoAssetSecureMonitorJitterMinSecs
+ _kMobileAssetPreferencesAutoAssetSecureMonitorOverrideRateLimiting
+ _kMobileAssetPreferencesAutoAssetSecureSimulateFailureAll
+ _kMobileAssetPreferencesAutoAssetSecureSimulateGraftFailure
+ _kMobileAssetPreferencesAutoAssetSecureSimulateRequireAll
+ _kMobileAssetPreferencesAutoAssetSessionIDBase
+ _kMobileAssetPreferencesAutoAssetSimulatedDownloadFailureResult
+ _kMobileAssetPreferencesAutoAssetSimulatedStagingLookupFailureResult
+ _kMobileAssetPreferencesAutoAssetStagerDetermineLastRequiredTimesOut
+ _kMobileAssetPreferencesAutoAssetStagerDeterminePallasResponseFewer
+ _kMobileAssetPreferencesAutoAssetStagerDownloadFirstNotInCatalog
+ _kMobileAssetPreferencesAutoAssetStagerFilesystemMaxMegabytes
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableDups
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableOlderVersions
+ _kMobileAssetPreferencesAutoAssetStagingLookupFlipRequiredOptional
+ _kMobileAssetPreferencesAutoAssetStartupSimulateFirstBoot
+ _kMobileAssetPreferencesAutoAssetSuspendResumeEnabled
+ _kMobileAssetPreferencesAutoAssetSuspendResumeForSUSetsOverride
+ _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutCancelOverride
+ _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutEvictOverride
+ _kMobileAssetPreferencesAutoHealthReportSetNames
+ _kMobileAssetPreferencesAutoStartupHealthReport
+ _kMobileAssetPreferencesDefaultNumberOfSecsGC
+ _kMobileAssetPreferencesDomain
+ _kMobileAssetPreferencesEnableCentralizedCacheDelete
+ _kMobileAssetPreferencesEnableVerboseLogging
+ _kMobileAssetPreferencesFailPersonalizationConfig
+ _kMobileAssetPreferencesFakeAvailableSpaceInBytesForSpaceCheck
+ _kMobileAssetPreferencesFakeDeviceOSBuildVersion
+ _kMobileAssetPreferencesFakeDeviceRecoveryMode
+ _kMobileAssetPreferencesForceAutoCacheDelete
+ _kMobileAssetPreferencesForceBatteryAllowedDownload
+ _kMobileAssetPreferencesForceBeforeFirstUnlock
+ _kMobileAssetPreferencesForceInProcessDownloads
+ _kMobileAssetPreferencesForceNonDiscretionaryDownload
+ _kMobileAssetPreferencesGarbageCollectionAlterAssetType
+ _kMobileAssetPreferencesGarbageCollectionAlterBehavior
+ _kMobileAssetPreferencesGarbageCollectionCurrentTimeDeltaSecs
+ _kMobileAssetPreferencesInPalletSeaShipMode
+ _kMobileAssetPreferencesInternalVariantAsCustomer
+ _kMobileAssetPreferencesMABrainForceStartupBusy
+ _kMobileAssetPreferencesMADownloadServiceDownloadTimeout
+ _kMobileAssetPreferencesPallasTimeout
+ _kMobileAssetPreferencesPreciousNumberOfSecsGC
+ _kMobileAssetPreferencesReclaimStatOnlyForAssetTypes
+ _kMobileAssetPreferencesSplunkTimeout
+ _kMobileAssetPreferencesSupportedFeaturesOverride
+ _kMobileAssetPreferencesTestMABrainReplaceAllowed
+ _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
+ _kMobileAssetPreferencesThirdPartyStagingPathComponent
+ _loadManagedPrefs
+ _newPrefsCopyValueForKey
+ _objc_msgSend$_relinquishEstimateEvictableBytesIsSynchronous:completion:
+ _objc_msgSend$_relinquishResumeIsSynchronous:completion:
+ _objc_msgSend$_relinquishStatusIsSynchronous:completion:
+ _objc_msgSend$_relinquishSuspendIsSynchronous:neededBytes:completion:
+ _objc_msgSend$_stageDownloadStatusProgress:stageProgressError:progressBlock:
+ _objc_msgSend$_statusIsSynchronous:clientDomainName:assetSetIdentifier:completion:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$getClientIdentifierForSelf
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$initWithAssetType:
+ _objc_msgSend$initWithClientDomainName:assetSetIdentifier:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$isSecure
+ _objc_msgSend$mainBundle
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringValue
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _syncPreferences
- +[MAAutoAsset(SoftwareUpdateSuspendResume) _estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:]
- +[MAAutoAsset(SoftwareUpdateSuspendResume) _resumeFromSoftwareUpdateIsSynchronous:completion:]
- +[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]
- +[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:]
- +[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:]
- +[MAAutoAssetMonitor defaultDispatchQueue]
- +[MAAutoAssetMonitor defaultDispatchQueue].cold.1
- +[MAAutoAssetMonitor supportsSecureCoding]
- -[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:]
- -[MAAutoAsset _failedStageDownloadAll:withResponseError:description:isSynchronous:completion:]
- -[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]
- -[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]
- -[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]
- -[MAAutoAsset _stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:]
- -[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]
- -[MAAutoAsset _stageDownloadAllStatusProgress:stageProgressError:progressBlock:]
- -[MAAutoAsset _successStageDetermineAllAvailable:isSynchronous:completion:]
- -[MAAutoAsset _successStageDownloadAll:isSynchronous:completion:]
- -[MAAutoAssetInfoStaging allAvailableForStagingAttributes]
- -[MAAutoAssetInfoStaging initWithAvailableForStaging:withTotalExpectedBytes:]
- -[MAAutoAssetInfoStaging initWithByGroupAvailableForStaging:withByGroupTotalExpectedBytes:]
- -[MAAutoAssetInfoStaging initWithUpdateAttributes:]
- -[MAAutoAssetInfoStaging initWithUpdateAttributes:withByGroupAvailableForStaging:withAvailableForStaging:withByGroupTotalExpectedBytes:withTotalExpectedBytes:]
- -[MAAutoAssetInfoStaging totalExpectedBytes]
- -[MAAutoAssetMonitor .cxx_destruct]
- -[MAAutoAssetMonitor assetSelector]
- -[MAAutoAssetMonitor autoAssetClientName]
- -[MAAutoAssetMonitor cancelRegistration:]
- -[MAAutoAssetMonitor cancelRegistrationSync]
- -[MAAutoAssetMonitor description]
- -[MAAutoAssetMonitor encodeWithCoder:]
- -[MAAutoAssetMonitor initForClientName:forAssetSelector:error:notifyingStatusChanges:]
- -[MAAutoAssetMonitor initForClientName:forAssetSelector:notifyingFromQueue:error:notifyingStatusChanges:]
- -[MAAutoAssetMonitor initWithCoder:]
- -[MAAutoAssetMonitor notificationDispatchQueue]
- -[MAAutoAssetMonitor registerForNotifications:]
- -[MAAutoAssetMonitor registerForNotifications:completion:]
- -[MAAutoAssetMonitor registerForNotificationsSync:]
- -[MAAutoAssetMonitor registerForNotificationsSync]
- -[MAAutoAssetMonitor setStatusChangeNotificationBlock:]
- -[MAAutoAssetMonitor statusChangeNotificationBlock]
- -[MAAutoAssetMonitor summary]
- -[MAAutoAssetSetOverview activeMonitorCount]
- -[MAAutoAssetSetOverview initWithDomainName:forAssetSetIdentifier:withConfiguredAssetEntries:withLatestDownloadedAtomicInstance:withDownloadedAtomicInstances:withDiscoveredAtomicInstance:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:]
- -[MAAutoAssetSetOverview setActiveMonitorCount:]
- -[MAAutoAssetSummary activeMonitorCount]
- -[MAAutoAssetSummary initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:]
- -[MAAutoAssetSummary initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:withIsSecureMobileAsset:withPersonalizationStatus:withPrePersonalizationStatus:withGraftStatus:withGraftPoint:withStageGroupType:withTargetOS:]
- -[MAAutoAssetSummary setActiveMonitorCount:]
- GCC_except_table166
- GCC_except_table172
- GCC_except_table179
- GCC_except_table185
- GCC_except_table199
- GCC_except_table204
- GCC_except_table210
- GCC_except_table215
- GCC_except_table221
- GCC_except_table226
- GCC_except_table232
- GCC_except_table237
- GCC_except_table244
- GCC_except_table249
- GCC_except_table255
- GCC_except_table266
- GCC_except_table271
- GCC_except_table280
- GCC_except_table287
- GCC_except_table296
- GCC_except_table300
- GCC_except_table308
- GCC_except_table313
- GCC_except_table319
- GCC_except_table324
- GCC_except_table330
- GCC_except_table335
- GCC_except_table36
- _CFStringCreateWithFormat
- _OBJC_CLASS_$_MAAutoAssetMonitor
- _OBJC_IVAR_$_MAAutoAssetInfoStaging._allAvailableForStagingAttributes
- _OBJC_IVAR_$_MAAutoAssetInfoStaging._totalExpectedBytes
- _OBJC_IVAR_$_MAAutoAssetMonitor._assetSelector
- _OBJC_IVAR_$_MAAutoAssetMonitor._autoAssetClientName
- _OBJC_IVAR_$_MAAutoAssetMonitor._notificationDispatchQueue
- _OBJC_IVAR_$_MAAutoAssetMonitor._statusChangeNotificationBlock
- _OBJC_IVAR_$_MAAutoAssetSetOverview._activeMonitorCount
- _OBJC_IVAR_$_MAAutoAssetSummary._activeMonitorCount
- _OBJC_METACLASS_$_MAAutoAssetMonitor
- __MAPreferencesGetAppBooleanValue
- __MAPreferencesIsCentralizedCacheDeleteEnabled
- __MAPreferencesIsCentralizedCacheDeleteEnabled._centralizedCacheDeleteEnabled
- __MAPreferencesIsCentralizedCacheDeleteEnabled.cold.1
- __MAPreferencesIsCentralizedCacheDeleteEnabled.onceToken
- __MAPreferencesIsInternalAllowed._isAppleInternal
- __MAPreferencesIsInternalAllowed.onceToken
- __MAPreferencesIsVerboseLoggingEnabled
- __MAPreferencesIsVerboseLoggingEnabled._verboseLoggingEnabled
- __MAPreferencesIsVerboseLoggingEnabled.cold.1
- __MAPreferencesIsVerboseLoggingEnabled.onceToken
- __OBJC_$_CLASS_METHODS_MAAutoAsset(SoftwareUpdateSuspendResume)
- __OBJC_$_CLASS_METHODS_MAAutoAssetMonitor
- __OBJC_$_CLASS_PROP_LIST_MAAutoAssetMonitor
- __OBJC_$_INSTANCE_METHODS_MAAutoAssetMonitor
- __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetMonitor
- __OBJC_$_PROP_LIST_MAAutoAssetMonitor
- __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetMonitor
- __OBJC_CLASS_RO_$_MAAutoAssetMonitor
- __OBJC_METACLASS_RO_$_MAAutoAssetMonitor
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.956
- ___106+[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:]_block_invoke
- ___106+[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:]_block_invoke
- ___109+[MAAutoAsset(SoftwareUpdateSuspendResume) _estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:]_block_invoke
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.424
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.605
- ___41-[MAAutoAssetMonitor cancelRegistration:]_block_invoke
- ___42+[MAAutoAssetMonitor defaultDispatchQueue]_block_invoke
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1136
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1137
- ___47-[MAAutoAssetMonitor registerForNotifications:]_block_invoke
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1125
- ___58-[MAAutoAssetMonitor registerForNotifications:completion:]_block_invoke
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1162
- ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_2
- ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_3
- ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_4
- ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_5
- ___62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke_2
- ___62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke_3
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.926
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.644
- ___75+[MAAutoAsset stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke_2
- ___75+[MAAutoAsset stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke_3
- ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke
- ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke_2
- ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke_3
- ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke
- ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke_2
- ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke_3
- ___81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.637
- ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke
- ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke_2
- ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke_3
- ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke
- ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke_2
- ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke_3
- ___94+[MAAutoAsset(SoftwareUpdateSuspendResume) _resumeFromSoftwareUpdateIsSynchronous:completion:]_block_invoke
- ___94-[MAAutoAsset _stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:]_block_invoke
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1131
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1132
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1135
- ___Block_byref_object_copy_.1302
- ___Block_byref_object_copy_.717
- ___Block_byref_object_copy_.820
- ___Block_byref_object_dispose_.1303
- ___Block_byref_object_dispose_.718
- ___Block_byref_object_dispose_.821
- ___MABrainStartupTransaction
- ___MABrainStartupTransaction.startupTransaction
- ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke
- ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke.cold.1
- ____MAPreferencesIsInternalAllowed_block_invoke
- ____MAPreferencesIsVerboseLoggingEnabled_block_invoke
- ____MAPreferencesIsVerboseLoggingEnabled_block_invoke.cold.1
- ____MAensureExtension_block_invoke.1309
- ____MAsendDownloadAsset_block_invoke.1211
- ____MAsendPMVCancelDownload_block_invoke.1229
- ____MAsendPMVDownload_block_invoke.1217
- ___block_descriptor_40_e8_32bs_e23_v32?0Q8q16"NSError"24ls32l8
- ___block_descriptor_40_e8_32bs_e37_v32?0"NSDictionary"8Q16"NSError"24ls32l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32r40r48r_e23_v32?0Q8q16"NSError"24lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32r40r48r_e37_v32?0"NSDictionary"8Q16"NSError"24lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_65_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s32l8s48l8
- ___block_literal_global.1000
- ___block_literal_global.1003
- ___block_literal_global.1120
- ___block_literal_global.1124
- ___block_literal_global.1128
- ___block_literal_global.1130
- ___block_literal_global.1131
- ___block_literal_global.1169
- ___block_literal_global.1175
- ___block_literal_global.1185
- ___block_literal_global.1190
- ___block_literal_global.1381
- ___block_literal_global.1386
- ___block_literal_global.1388
- ___block_literal_global.1409
- ___block_literal_global.1432
- ___block_literal_global.2824
- ___block_literal_global.2826
- ___block_literal_global.2828
- ___block_literal_global.2830
- ___block_literal_global.447
- ___block_literal_global.478
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.546
- ___block_literal_global.695
- ___block_literal_global.708
- ___block_literal_global.714
- ___block_literal_global.716
- ___block_literal_global.838
- ___block_literal_global.843
- ___block_literal_global.845
- ___block_literal_global.847
- ___block_literal_global.996
- ___block_literal_global.998
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:
- _objc_msgSend$_failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:
- _objc_msgSend$_failedStageDownloadAll:withResponseError:description:isSynchronous:completion:
- _objc_msgSend$_resumeFromSoftwareUpdateIsSynchronous:completion:
- _objc_msgSend$_stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:
- _objc_msgSend$_stageDetermineAllAvailableForUpdate:isSynchronous:completion:
- _objc_msgSend$_stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:
- _objc_msgSend$_stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:
- _objc_msgSend$_stageDownloadAll:reportingProgress:isSynchronous:completion:
- _objc_msgSend$_stageDownloadAllStatusProgress:stageProgressError:progressBlock:
- _objc_msgSend$_successStageDetermineAllAvailable:isSynchronous:completion:
- _objc_msgSend$_successStageDownloadAll:isSynchronous:completion:
- _objc_msgSend$_suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:
- _objc_msgSend$_suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:
- _objc_msgSend$activeMonitorCount
- _objc_msgSend$allAvailableForStagingAttributes
- _objc_msgSend$initForClientName:forAssetSelector:notifyingFromQueue:error:notifyingStatusChanges:
- _objc_msgSend$initWithAvailableForStaging:withTotalExpectedBytes:
- _objc_msgSend$initWithUpdateAttributes:withByGroupAvailableForStaging:withAvailableForStaging:withByGroupTotalExpectedBytes:withTotalExpectedBytes:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _os_transaction_create
CStrings:
+ " and defaults"
+ " and profile"
+ "%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@"
+ "%@|request|clientDomainName:%@|assetSetIdentifier:%@"
+ "%@|updateAttributes:%@|byGroupAvailableForStaging:%@|byGroupTotalExpectedBytes:%@"
+ "%{public}@ Completed operation to update preference %{public}@ to nil (clear)"
+ "%{public}@ Completed operation to update preference %{public}@ to string '%{public}@'"
+ "%{public}@ Completed operation to update preferences with values %{public}@"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preference %{public}@ to nil (clear)"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preference %{public}@ to string '%{public}@'"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preferences with values %{public}@"
+ "%{public}@ nil preference key provided"
+ "+[MAAutoAsset stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke"
+ "+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke"
+ "+[MAAutoAsset stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]"
+ "+[MAAutoAsset stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:]"
+ "+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke"
+ "+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]"
+ "/Library/Managed Preferences/mobile/com.apple.MobileAsset.plist"
+ "/System/Library/AssetTypeDescriptors/"
+ "/System/Library/SecureAssetTypeDescriptors/"
+ "<MAAssetTypeDescriptor: %p>: (AssetType: %@, Secure: %d)"
+ ">>>\n                   assetSelector: %@\n             assetRepresentation: %@\n                 assetWasPatched: %@\n                   assetIsStaged: %@\n              assetIsSecureAsset: %@\n       secureAssetIsPersonalized: %@\n    secureAssetIsPrePersonalized: %@\n      secureMobileAssetIsGrafted: %@\n     secureMobileAssetGraftPoint: %@\n           scheduledIntervalSecs: %ld\n          scheduledRemainingSecs: %ld\n                   pushDelaySecs: %ld\n               activeClientCount: %ld\n              maximumClientCount: %ld\n                totalClientCount: %ld\n                      stageGroup: %@\n                 targetOSVersion: %@\n%@<<<]"
+ ">>>\n                clientDomainName: %@\n              assetSetIdentifier: %@\n          configuredAssetEntries: %@\n  latestDownloadedAtomicInstance: %@\n        discoveredAtomicInstance: %@\n       downloadedAtomicInstances: %@\n               activeClientCount: %ld\n              maximumClientCount: %ld\n                totalClientCount: %ld\n<<<]"
+ "@136@0:8@16q24B32B36@40q48q56q64q72q80q88B96B100B104B108@112Q120@128"
+ "@88@0:8@16@24@32@40@48@56q64q72q80"
+ "@96@0:8@16q24B32B36@40q48q56q64q72q80q88"
+ "AnalyticsClearOnLaunch"
+ "AnalyticsClientNameTestToolOverride"
+ "AnalyticsClientNameTestToolPrepend"
+ "AnalyticsLevelOnLaunch"
+ "AnalyticsSendImmediate"
+ "AnalyticsSubmitOnLaunch"
+ "Asset Specifiers"
+ "Asset Type"
+ "AutoAssetActivityAggressiveAssetType"
+ "AutoAssetActivityAggressiveIntervalSecs"
+ "AutoAssetActivityHeightenedAssetType"
+ "AutoAssetActivityHeightenedIntervalSecs"
+ "AutoAssetActivityIntervalSecs"
+ "AutoAssetActivityTickerSecs"
+ "AutoAssetAlwaysPromoteStagedAssets"
+ "AutoAssetAsIfBackground"
+ "AutoAssetAsIfBootedOSIsBuildVersion"
+ "AutoAssetAsIfBootedOSIsOSVersion"
+ "AutoAssetAsIfRamp"
+ "AutoAssetBeforeFirstDefaultTimeoutSecs"
+ "AutoAssetBeforeFirstPollSecs"
+ "AutoAssetConnectorBackoffRetryTimes"
+ "AutoAssetConnectorInitialWaitSecs"
+ "AutoAssetConnectorWaitBeforeRetrySecs"
+ "AutoAssetLogSetCompare"
+ "AutoAssetLookupCacheAssetSelectorValidSecs"
+ "AutoAssetLookupCacheSetConfigurationValidSecs"
+ "AutoAssetMaxStagerDeterminingSecs"
+ "AutoAssetNoPersistedOverflowLimit"
+ "AutoAssetObserverIgnoreNetworkStatus"
+ "AutoAssetPerformanceLoggingEnabled"
+ "AutoAssetPersistedTableLoggingEnabled"
+ "AutoAssetPushActivityIntervalSecs"
+ "AutoAssetScheduledAlwaysNonDiscretionary"
+ "AutoAssetScheduledAsIfNotInternal"
+ "AutoAssetScheduledBackupTriggersDisabled"
+ "AutoAssetScheduledOnlyForAssetTypes"
+ "AutoAssetSecureMonitorBackoffRetryTimes"
+ "AutoAssetSecureMonitorJitterMaxSecs"
+ "AutoAssetSecureMonitorJitterMinSecs"
+ "AutoAssetSecureMonitorOverrideRateLimiting"
+ "AutoAssetSecureSimulateFailureAll"
+ "AutoAssetSecureSimulateGraftFailure"
+ "AutoAssetSecureSimulateRequireAll"
+ "AutoAssetSessionIDBase"
+ "AutoAssetSimulatedDownloadFailureResult"
+ "AutoAssetSimulatedStagingLookupFailureResult"
+ "AutoAssetStagerDetermineLastRequiredTimesOut"
+ "AutoAssetStagerDeterminePallasResponseFewer"
+ "AutoAssetStagerDownloadFirstNotInCatalog"
+ "AutoAssetStagerFilesystemMaxMegabytes"
+ "AutoAssetStagerInjectAvailableDups"
+ "AutoAssetStagerInjectAvailableOlderVersions"
+ "AutoAssetStagingLookupFlipRequiredOptional"
+ "AutoAssetStartupSimulateFirstBoot"
+ "AutoAssetSuspendResumeForSUEnabled"
+ "AutoAssetSuspendResumeForSUSetsOverride"
+ "AutoAssetSuspendResumeTimeoutCancelOverride"
+ "AutoAssetSuspendResumeTimeoutEvictOverride"
+ "AutoHealthReportSets"
+ "AutoStartupHealthReport"
+ "BeforeFirstUnlock"
+ "CFArray"
+ "Download failed due to a server redirect to a nonexistent location."
+ "Download failed due to invalid asset receipts in response from live asset server."
+ "DownloadManagerNotReady"
+ "FailPersonalizationConfig"
+ "Failed to get key: %{public}s due to not being present"
+ "Failed to load asset descriptors from path %{public}@. %@"
+ "FakeAvailableSpaceInBytesForSpaceCheck"
+ "FakeDeviceOSBuildVersion"
+ "FakeDeviceRecoveryMode"
+ "Feature Removed"
+ "ForceAutoCacheDelete"
+ "ForceBatteryAllowedDownload"
+ "ForceBeforeFirstUnlock"
+ "ForceKeyManager5XXError"
+ "ForceNonDiscretionaryDownload"
+ "GarbageCollectionAlterAssetType"
+ "GarbageCollectionAlterBehavior"
+ "GarbageCollectionCurrentTimeDeltaSecs"
+ "InPalletSeaShipMode"
+ "InternalVariantAsCustomer"
+ "Loading managed profile: %@"
+ "MA-auto(%{public}@) | SUCCESS | %{public}@"
+ "MA-auto(%{public}@)| error:%{public}@"
+ "MA-auto(relinquish-est)"
+ "MA-auto(relinquish-suspend)"
+ "MA-auto(staging-client){_stageDownloadStatusProgress} | no client progress block | %{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: Failed to determine realpath for %{public}@. Skipping caching"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: In memory record for lock file(%{public}@) not valid. Discarding"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: Updating in memory record for lockerFile:'%{public}@' realPath:'%{public}@'"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile}\n[SHORT_FILE_CLOSE][%d] (%{public}@) | lockReason:%{public}@ | released sharedLockFileDescriptor | atomicInstanceFilename:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile}\n[SHORT_FILE_OPEN][%d] (%{public}@) | lockReason:%{public}@ | successfully opened SHORT-TERM | atomicInstanceFilename:%{public}@ | "
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile} | successfully locked SHORT-TERM (%{public}@) | lockReason:%{public}@ | atomicInstanceFilename:%{public}@ | standardURLs:%ld | secureURLs:%ld"
+ "MAAssetTypeDescriptor"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateStatusRequestInfo"
+ "MABrainForceStartupBusy"
+ "MADownloadServiceDownloadTimeout"
+ "MARelinquish"
+ "Make Repository Data Vault"
+ "MobileAssetProperties"
+ "PallasTimeout"
+ "PreinstalledNotAdopted"
+ "ReclaimStatOnlyForAssetTypes"
+ "RelinquishShared"
+ "RelinquishSuspendResumeFailure"
+ "RemoveV1Assets"
+ "SplunkTimeout"
+ "SupportedFeaturesOverride"
+ "T@\"NSArray\",R,D,N"
+ "T@\"NSDictionary\",R,D,N"
+ "T@\"NSString\",R,N,V_assetSetIdentifier"
+ "T@\"NSString\",R,N,V_clientDomainName"
+ "TB,R,D,N"
+ "TB,R,N,V_isSecure"
+ "TestMABrainReplaceAllowed"
+ "ThirdPartyStagingBucketPathComponent"
+ "ThirdPartyStagingPathComponent"
+ "UnknownClient"
+ "[MA_PREFS] Current process %{public}@ entitled for using daemon preferences logic."
+ "[MA_PREFS] Read preference from: %{public}@ for: %{public}@ value: `%{public}@` (%{public}@)"
+ "[MA_PREFS] Read preference from: '%{public}@' for all defaults. Values read are: `%{public}@` (%{public}@)"
+ "[MA_PREFS] {%@} [%@] (%@) |"
+ "[MA_PREFS] {%{public}@} [%{public}@] Could not synchronize preferences for %{public}@ - this may be a permissions error"
+ "[MA_PREFS] {%{public}@} [%{public}@] nil preference key provided"
+ "[MA_PREFS] {%{public}@} [%{public}@] | Completed operation to update preference %{public}@ %{public}@ to data"
+ "[MA_PREFS] {%{public}@} [%{public}@] | Completed operation to update preference %{public}@ %{public}@ to nil (clear)"
+ "[MA_PREFS] {%{public}@} [%{public}@] | attemptsMade:%d | Unable to synchronize after setting preference %{public}@ %{public}@ to data"
+ "[MA_PREFS] {%{public}@} [%{public}@] | attemptsMade:%d | Unable to synchronize after setting preference %{public}@ %{public}@ to nil (clear)"
+ "[MA_PREFS] {MAPreferencesCopyNSArrayOfNumbersValue} invalid type for key:%{public}@ | expecting array of numbers"
+ "[MA_PREFS] {MAPreferencesCopyNSArrayOfStringsValue} invalid type for key:%{public}@ | expecting array of strings"
+ "[MA_PREFS] {MAPreferencesCopyNSDataValue} invalid type for key:%{public}@ | expecting data"
+ "[MA_PREFS] {MAPreferencesCopyNSDictionaryValue} invalid type for key:%{public}@ | expecting dictionary"
+ "[MA_PREFS] {MAPreferencesCopyNSStringValue} invalid type for key:%{public}@ | expecting string or number or boolean"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a number"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a number (from string)"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfStrings} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a string"
+ "_isSecure"
+ "_relinquishEstimateEvictableBytesIsSynchronous:completion:"
+ "_relinquishResumeIsSynchronous:completion:"
+ "_relinquishStatusIsSynchronous:completion:"
+ "_relinquishSuspendIsSynchronous:neededBytes:completion:"
+ "_stageDownloadStatusProgress:stageProgressError:progressBlock:"
+ "_statusIsSynchronous:clientDomainName:assetSetIdentifier:completion:"
+ "_typeDescriptor"
+ "addEntriesFromDictionary:"
+ "asset(%@)[%@]|patched:%@|staged:%@|secureMobileAsset:%@|personalized:%@|prePersonalized:%@|grafted:%@|graftPoint:%@|status:%@|interval:%@|remaining:%@|pushDelay:%@|clients:%@|maxClients:%@|totalClients:%@|stageGroup:%@|targetOSVersion:%@"
+ "assetProperties"
+ "assetSpecifiers"
+ "auto(relinquish-status)"
+ "bundleIdentifier"
+ "clientDomain:%@|assetIdentifier:%@|numConfiguredEntries:%ld|latestDownloadedEntry:%@|numDownloadedEntries:%ld|discoveredEntry:%@|clients:%lld|maxClients:%lld|totalClients:%lld"
+ "com.apple.private.mobileassetd.use-daemon-preference-logic"
+ "componentsSeparatedByString:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "defaultNumberOfSecsGC"
+ "defaults"
+ "descriptorForAssetType:"
+ "dictionaryWithContentsOfURL:"
+ "estimateEvictableBytesSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:"
+ "estimateEvictableBytesWithCompletion:"
+ "forceInProcessDownloads"
+ "getClientIdentifierForSelf"
+ "getResourceValue:forKey:error:"
+ "initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withMaximumClientCount:withTotalClientCount:"
+ "initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withMaximumClientCount:withTotalClientCount:withIsSecureMobileAsset:withPersonalizationStatus:withPrePersonalizationStatus:withGraftStatus:withGraftPoint:withStageGroupType:withTargetOS:"
+ "initWithClientDomainName:assetSetIdentifier:"
+ "initWithContentsOfFile:"
+ "initWithDomainName:forAssetSetIdentifier:withConfiguredAssetEntries:withLatestDownloadedAtomicInstance:withDownloadedAtomicInstances:withDiscoveredAtomicInstance:withActiveClientCount:withMaximumClientCount:withTotalClientCount:"
+ "is"
+ "is NOT"
+ "isSecure"
+ "mainBundle"
+ "mobile"
+ "numberFromString:"
+ "preciousNumberOfSecsGC"
+ "profile"
+ "q40@0:8@16@24^@32"
+ "relinquish(status-for-asset-set)"
+ "resumeSyncWithReturnResumeErrorPtr:"
+ "resumeWithCompletion:"
+ "setNumberStyle:"
+ "shouldMakeDataVault"
+ "shouldRemoveV1Assets"
+ "statusSyncWithClientDomainName:assetSetIdentifier:returnStatusErrorPtr:"
+ "statusSyncWithReturnStatusErrorPtr:"
+ "statusWithClientDomainName:assetSetIdentifier:completion:"
+ "statusWithCompletion:"
+ "stringByAppendingString:"
+ "stringByDeletingPathExtension"
+ "stringValue"
+ "suspendSyncWithNeededBytes:returnSuspendErrorPtr:"
+ "suspendWithNeededBytes:completion:"
+ "typeDescriptorsToDataVault"
+ "typeDescriptorsToRemoveV1Assets"
+ "userdefaults"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@8@\"NSDictionary\"16^B24"
+ "v44@0:8B16@20@28@?36"
+ "value of unsupported type %lu provided to set default was invalid"
- "\n>%{public}@> allAvailableForStagingAttributes:\n%{public}@"
- "\n>%{public}@> totalExpectedBytes:%llu"
- "%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@"
- "%@|updateAttributes:%@|byGroupAvailableForStaging:%@|allAvailableForStaging:%@|byGroupTotalExpectedBytes:%@"
- "+stageDetermineAllAvailable"
- "+stageDetermineAllAvailableForUpdate"
- "+stageDownloadAll"
- ">>>\n                   assetSelector: %@\n             assetRepresentation: %@\n                 assetWasPatched: %@\n                   assetIsStaged: %@\n              assetIsSecureAsset: %@\n       secureAssetIsPersonalized: %@\n    secureAssetIsPrePersonalized: %@\n      secureMobileAssetIsGrafted: %@\n     secureMobileAssetGraftPoint: %@\n           scheduledIntervalSecs: %ld\n          scheduledRemainingSecs: %ld\n                   pushDelaySecs: %ld\n               activeClientCount: %ld\n              activeMonitorCount: %ld\n              maximumClientCount: %ld\n                totalClientCount: %ld\n                      stageGroup: %@\n                 targetOSVersion: %@\n%@<<<]"
- ">>>\n                clientDomainName: %@\n              assetSetIdentifier: %@\n          configuredAssetEntries: %@\n  latestDownloadedAtomicInstance: %@\n        discoveredAtomicInstance: %@\n       downloadedAtomicInstances: %@\n               activeClientCount: %ld\n              activeMonitorCount: %ld\n              maximumClientCount: %ld\n                totalClientCount: %ld\n<<<]"
- "@104@0:8@16q24B32B36@40q48q56q64q72q80q88q96"
- "@144@0:8@16q24B32B36@40q48q56q64q72q80q88q96B104B108B112B116@120Q128@136"
- "@32@0:8@16Q24"
- "@48@0:8@16@24^@32@?40"
- "@56@0:8@16@24@32@40Q48"
- "@56@0:8@16@24@32^@40@?48"
- "@96@0:8@16@24@32@40@48@56q64q72q80q88"
- "BrainVersion"
- "DETERMINE-ALL-LEGACY-REPLY"
- "DETERMINE-ALL-LEGACY-REQUEST"
- "DETERMINE-ALL-REPLY"
- "DETERMINE-ALL-REQUEST"
- "DOWNLOAD-ALL-REPLY"
- "DOWNLOAD-ALL-REQUEST"
- "Downlaod failed due to a server redirect to a nonexistent location."
- "Download failed due to invalid asset reciepts in response from live asset server."
- "Failed to get key: %{public}s due to not beinng present"
- "MA-AUTO-STAGE(REPLY):DETERMINE_ALL_AVAILABLE"
- "MA-AUTO-STAGE(REPLY):DETERMINE_ALL_AVAILABLE_FOR_UPDATE"
- "MA-AUTO-STAGE(REPLY):DOWNLOAD_ALL"
- "MA-AUTO-STAGE:DETERMINE_ALL_AVAILABLE"
- "MA-AUTO-STAGE:DETERMINE_ALL_AVAILABLE_FOR_UPDATE"
- "MA-AUTO-STAGE:DOWNLOAD_ALL"
- "MA-auto(%@) | SUCCESS | %@"
- "MA-auto(%@)| error:%{public}@"
- "MA-auto(staging-client){+stageDetermineAllAvailableForUpdate} | no client completion block | %{public}@"
- "MA-auto(staging-client){+stageDetermineAllAvailable} | no client completion block | %{public}@"
- "MA-auto(staging-client){+stageDownloadAll} | no client completion block | %{public}@"
- "MA-auto(staging-client){_failedStageDetermineAllAvailable} | %{public}@ | SUCCESS"
- "MA-auto(staging-client){_failedStageDetermineAllAvailable} | %{public}@ | error:%{public}@"
- "MA-auto(staging-client){_failedStageDetermineAllAvailable} | no client completion block | %{public}@"
- "MA-auto(staging-client){_failedStageDownloadAll} | %{public}@ | SUCCESS"
- "MA-auto(staging-client){_failedStageDownloadAll} | %{public}@ | error:%{public}@"
- "MA-auto(staging-client){_failedStageDownloadAll} | no client completion block | %{public}@"
- "MA-auto(staging-client){_stageDownloadAllStatusProgress} | no client progress block | %{public}@"
- "MA-auto(staging-client){_successStageDetermineAllAvailable} | no client completion block | staging:%{public}@"
- "MA-auto(staging-client){_successStageDetermineAllAvailable} | staging:%{public}@ | SUCCESS"
- "MA-auto(staging-client){_successStageDownloadAll} | no client completion block | staged:%{public}@"
- "MA-auto(staging-client){_successStageDownloadAll} | staged:%{public}@ | SUCCESS"
- "MA-auto(staging-client){stageDetermineAllAvailable} | no staging-client completion block | %{public}@"
- "MA-auto(staging-client){stageDownloadAll} | no staging-client completion block | %{public}@"
- "MA-auto(suspend-resume-su-estimateEvictableBytes)"
- "MA-auto(suspend-resume-su-suspendWithNeededBytes)"
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: Failed to determine realpath for %@. Skipping caching"
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: In memory record for lock file(%@) not valid. Discarding"
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK] _readLockedSetStatusFromSharedLockFile: Updating in memory record for lockerFile:'%@' realPath:'%@'"
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile}\n[SHORT_FILE_CLOSE][%d] (%{public}@) | lockReason:%@ | released sharedLockFileDescriptor | atomicInstanceFilename:%{public}@"
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile}\n[SHORT_FILE_OPEN][%d] (%{public}@) | lockReason:%@ | successfully opened SHORT-TERM | atomicInstanceFilename:%{public}@ | "
- "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_shortTermOpenSharedLockFile} | successfully locked SHORT-TERM (%{public}@) | lockReason:%@ | atomicInstanceFilename:%{public}@ | standardURLs:%ld | secureURLs:%ld"
- "MAAuto:_stageDetermineAllAvailable"
- "MAAuto:_stageDetermineAllAvailableForUpdate"
- "MAAuto:_stageDownloadAll"
- "MAAutoAsset-under-development"
- "MAAutoAssetMonitor"
- "MAAutoAssetMonitor SPI:description not-yet-implemented [see rdar://84676752]"
- "MAAutoAssetMonitor SPI:summary not-yet-implemented [see rdar://84676752]"
- "PSUS_IMMEDIATE_PROMOTED"
- "PSUS_NEW_OS_PROMOTED"
- "STAGE_GENERAL"
- "T@\"NSDictionary\",R,&,N,V_allAvailableForStagingAttributes"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notificationDispatchQueue"
- "T@?,C,N,V_statusChangeNotificationBlock"
- "TQ,R,N,V_totalExpectedBytes"
- "TargetBuildVersion"
- "TargetOSVersion"
- "Tq,N,V_activeMonitorCount"
- "_activeMonitorCount"
- "_allAvailableForStagingAttributes"
- "_estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:"
- "_failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:"
- "_failedStageDownloadAll:withResponseError:description:isSynchronous:completion:"
- "_notificationDispatchQueue"
- "_resumeFromSoftwareUpdateIsSynchronous:completion:"
- "_stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:"
- "_stageDetermineAllAvailableForUpdate:isSynchronous:completion:"
- "_stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:"
- "_stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:"
- "_stageDownloadAll:reportingProgress:isSynchronous:completion:"
- "_stageDownloadAllStatusProgress:stageProgressError:progressBlock:"
- "_statusChangeNotificationBlock"
- "_successStageDetermineAllAvailable:isSynchronous:completion:"
- "_successStageDownloadAll:isSynchronous:completion:"
- "_suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:"
- "_suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:"
- "activeMonitorCount"
- "allAvailableForStagingAttributes"
- "asset(%@)[%@]|patched:%@|staged:%@|secureMobileAsset:%@|personalized:%@|prePersonalized:%@|grafted:%@|graftPoint:%@|status:%@|interval:%@|remaining:%@|pushDelay:%@|clients:%@|monitors:%@|maxClients:%@|totalClients:%@|stageGroup:%@|targetOSVersion:%@"
- "auto(stageDownloadAll)"
- "auto(suspend-resume-su-status)"
- "auto-monitor(cancelRegistration:)"
- "auto-monitor(cancelRegistrationSync)"
- "auto-monitor(defaultDispatchQueue)"
- "auto-monitor(registerForNotifications)"
- "auto-monitor(registerForNotifications:)"
- "auto-monitor(registerForNotificationsSync)"
- "auto-monitor(registerForNotificationsSync:)"
- "cancelRegistration:"
- "cancelRegistrationSync"
- "clientDomain:%@|assetIdentifier:%@|numConfiguredEntries:%ld|latestDownloadedEntry:%@|numDownloadedEntries:%ld|discoveredEntry:%@|clients:%lld|monitors:%lld|maxClients:%lld|totalClients:%lld"
- "com.apple.MobileAsset.framework.autoassetmonitor"
- "com.apple.mobileassetd.160731798"
- "initForClientName:forAssetSelector:error:notifyingStatusChanges:"
- "initForClientName:forAssetSelector:notifyingFromQueue:error:notifyingStatusChanges:"
- "initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:"
- "initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:withIsSecureMobileAsset:withPersonalizationStatus:withPrePersonalizationStatus:withGraftStatus:withGraftPoint:withStageGroupType:withTargetOS:"
- "initWithAvailableForStaging:withTotalExpectedBytes:"
- "initWithByGroupAvailableForStaging:withByGroupTotalExpectedBytes:"
- "initWithDomainName:forAssetSetIdentifier:withConfiguredAssetEntries:withLatestDownloadedAtomicInstance:withDownloadedAtomicInstances:withDiscoveredAtomicInstance:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:"
- "initWithUpdateAttributes:"
- "initWithUpdateAttributes:withByGroupAvailableForStaging:withAvailableForStaging:withByGroupTotalExpectedBytes:withTotalExpectedBytes:"
- "notificationDispatchQueue"
- "registerForNotifications:"
- "registerForNotifications:completion:"
- "registerForNotificationsSync"
- "registerForNotificationsSync:"
- "setActiveMonitorCount:"
- "setStatusChangeNotificationBlock:"
- "staging[ALL]|osVersion:%@|build:%@|trainName:%@|restoreVersion:%@|allAvailableForStaging:%ld|totalExpectedBytes:%llu"
- "statusChangeNotificationBlock"
- "unable to assign notification dispatch queue"
- "v32@?0@\"NSDictionary\"8Q16@\"NSError\"24"
- "v32@?0Q8q16@\"NSError\"24"
- "v44@0:8q16@?24B32@?36"
- "{__MABrainStartupTransaction} os_transaction cleared"
- "{__MABrainStartupTransaction} os_transaction created"

```

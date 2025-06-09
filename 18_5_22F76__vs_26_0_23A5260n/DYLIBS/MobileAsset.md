## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1487.122.1.0.0
-  __TEXT.__text: 0x82dbc
+1788.0.0.0.4
+  __TEXT.__text: 0x7f468
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x63e4
-  __TEXT.__const: 0x298
-  __TEXT.__gcc_except_tab: 0xbd8
-  __TEXT.__cstring: 0x10682
-  __TEXT.__oslogstring: 0xa1ca
-  __TEXT.__unwind_info: 0x1af0
-  __TEXT.__objc_classname: 0x889
-  __TEXT.__objc_methname: 0x15004
-  __TEXT.__objc_methtype: 0x1768
-  __TEXT.__objc_stubs: 0x81c0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x1ff8
+  __TEXT.__objc_methlist: 0x627c
+  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x103da
+  __TEXT.__oslogstring: 0xa0b1
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__unwind_info: 0x1a60
+  __TEXT.__objc_classname: 0x884
+  __TEXT.__objc_methname: 0x14d3f
+  __TEXT.__objc_methtype: 0x1788
+  __TEXT.__objc_stubs: 0x8020
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x20a8
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30c8
+  __DATA_CONST.__objc_selrefs: 0x3060
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__cfstring: 0xda80
-  __AUTH_CONST.__objc_const: 0x98f0
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_const: 0x97d0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x7fc
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x7e4
   __DATA.__data: 0x360
-  __DATA.__bss: 0x1c0
-  __DATA_DIRTY.__objc_data: 0x1130
+  __DATA.__bss: 0x190
+  __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA022FEE-EB35-3AD7-B2E3-B29D175AE589
-  Functions: 2797
-  Symbols:   8399
-  CStrings:  6856
+  UUID: 78A8B467-19C9-3D74-8611-63A11B1CEBA7
+  Functions: 2750
+  Symbols:   8278
+  CStrings:  6851
 
Symbols:
+ +[MAPushChannel supportsSecureCoding]
+ -[MAAutoAssetSet _autoSetAtomicOperationStatusProgress:withLogMessage:progressBlock:]
+ -[MAAutoAssetSet _newProxyObjectForSetProgressBlock:withLogMessage:]
+ -[MAAutoAssetSetAtomicEntry setAssetAttributes:]
+ -[MAAutoAssetSetAtomicEntry setAssetID:]
+ -[MAAutoAssetSetAtomicEntry setFullAssetSelector:]
+ -[MAAutoAssetSetAtomicEntry setLocalContentURL:]
+ -[MAMsuDownloadOptions requestedBuildVersion]
+ -[MAMsuDownloadOptions setRequestedBuildVersion:]
+ -[MAPushChannel .cxx_destruct]
+ -[MAPushChannel base64ChannelId]
+ -[MAPushChannel channelIDForPopulationType]
+ -[MAPushChannel description]
+ -[MAPushChannel encodeWithCoder:]
+ -[MAPushChannel hash]
+ -[MAPushChannel humanReadableChannelName]
+ -[MAPushChannel identifier]
+ -[MAPushChannel initWithCoder:]
+ -[MAPushChannel initWithIdentifier:]
+ -[MAPushChannel initWithPopulationType:]
+ -[MAPushChannel isEqual:]
+ -[MAPushChannel isEqualToPushChannelId:]
+ -[MAPushChannel populationTypeString]
+ -[MAPushChannel populationType]
+ -[MAPushNotificationController asyncSubscribeToChannelWithIdentifier:completion:]
+ -[MAPushNotificationController asyncUnsubscribeToChannelWithIdentifier:completion:]
+ -[MAPushNotificationController setVerboseLogging:]
+ -[MAPushNotificationController triggerNotificationWithPayload:withCompletion:]
+ -[MAPushNotificationController verboseLogging]
+ GCC_except_table24
+ GCC_except_table60
+ _MAClearPreferences
+ _OBJC_CLASS_$_MAPushChannel
+ _OBJC_IVAR_$_MAMsuDownloadOptions._requestedBuildVersion
+ _OBJC_IVAR_$_MAPushChannel._base64ChannelId
+ _OBJC_IVAR_$_MAPushChannel._identifier
+ _OBJC_IVAR_$_MAPushChannel._populationType
+ _OBJC_IVAR_$_MAPushNotificationController._verboseLogging
+ _OBJC_METACLASS_$_MAPushChannel
+ __MAClearPreferences
+ __OBJC_$_CLASS_METHODS_MAPushChannel
+ __OBJC_$_CLASS_PROP_LIST_MAPushChannel
+ __OBJC_$_INSTANCE_METHODS_MAPushChannel
+ __OBJC_$_INSTANCE_VARIABLES_MAPushChannel
+ __OBJC_$_PROP_LIST_MAPushChannel
+ __OBJC_CLASS_PROTOCOLS_$_MAPushChannel
+ __OBJC_CLASS_RO_$_MAPushChannel
+ __OBJC_METACLASS_RO_$_MAPushChannel
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.938
+ ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.406
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.554
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1082
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1083
+ ___50-[MAPushNotificationController _serviceConnection]_block_invoke.1071
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1108
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.908
+ ___65-[MAPushNotificationController subscribeToChannelWithIdentifier:]_block_invoke
+ ___67-[MAPushNotificationController unsubscribeToChannelWithIdentifier:]_block_invoke
+ ___68-[MAAutoAssetSet _newProxyObjectForSetProgressBlock:withLogMessage:]_block_invoke
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.593
+ ___78-[MAPushNotificationController triggerNotificationWithPayload:withCompletion:]_block_invoke
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.586
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1077
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1078
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1081
+ ___Block_byref_object_copy_.1248
+ ___Block_byref_object_copy_.699
+ ___Block_byref_object_copy_.776
+ ___Block_byref_object_dispose_.1249
+ ___Block_byref_object_dispose_.700
+ ___Block_byref_object_dispose_.777
+ ____MAensureExtension_block_invoke.1255
+ ____MAsendDownloadAsset_block_invoke.1157
+ ____MAsendPMVCancelDownload_block_invoke.1175
+ ____MAsendPMVDownload_block_invoke.1163
+ ___block_descriptor_40_e8_32s_e23_v16?0"MAPushChannel"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e30_v16?0"MAAutoAssetSetStatus"8lr48l8s32l8s40l8
+ ___block_literal_global.1066
+ ___block_literal_global.1070
+ ___block_literal_global.1074
+ ___block_literal_global.1076
+ ___block_literal_global.1077
+ ___block_literal_global.1112
+ ___block_literal_global.1118
+ ___block_literal_global.1128
+ ___block_literal_global.1133
+ ___block_literal_global.1160
+ ___block_literal_global.1318
+ ___block_literal_global.1323
+ ___block_literal_global.1325
+ ___block_literal_global.1355
+ ___block_literal_global.1375
+ ___block_literal_global.2757
+ ___block_literal_global.2759
+ ___block_literal_global.2761
+ ___block_literal_global.2763
+ ___block_literal_global.429
+ ___block_literal_global.460
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.514
+ ___block_literal_global.648
+ ___block_literal_global.673
+ ___block_literal_global.679
+ ___block_literal_global.681
+ ___block_literal_global.794
+ ___block_literal_global.799
+ ___block_literal_global.801
+ ___block_literal_global.803
+ ___block_literal_global.978
+ ___block_literal_global.980
+ ___block_literal_global.982
+ ___block_literal_global.985
+ _kMAMaxChannelIdSizeInBytes
+ _objc_msgSend$_autoSetAtomicOperationStatusProgress:withLogMessage:progressBlock:
+ _objc_msgSend$_newProxyObjectForSetProgressBlock:withLogMessage:
+ _objc_msgSend$base64ChannelId
+ _objc_msgSend$base64String
+ _objc_msgSend$channelIDForPopulationType
+ _objc_msgSend$humanReadableChannelName
+ _objc_msgSend$isEqualToPushChannelId:
+ _objc_msgSend$isThirdPartyAssetType:
+ _objc_msgSend$populationType
+ _objc_msgSend$requestedBuildVersion
+ _objc_msgSend$subscribeToChannelWithIdentifier:completion:
+ _objc_msgSend$triggerPushNotificationWithPayload:withCompletion:
+ _objc_msgSend$unsubscribeToChannelWithIdentifier:completion:
+ _objc_msgSend$verboseLogging
- +[MAAutoAssetSetControl activeSetJobSummary:error:]
- +[MAAutoAssetSetControl activeSetJobSummary:limitedToSetIdentifiers:error:]
- +[MAAutoAssetSetControl knownAssetSetSummary:error:]
- +[MAAutoAssetSetControl knownAssetSetSummary:limitedToSetIdentifiers:error:]
- +[MAAutoAssetSetControl lockedAssetSetSummary:error:]
- +[MAAutoAssetSetControl lockedAssetSetSummary:limitedToSetIdentifiers:error:]
- +[MAAutoAssetSetControl scheduledSetJobSummary:error:]
- +[MAAutoAssetSetControl scheduledSetJobSummary:limitedToSetIdentifiers:error:]
- +[MAAutoAssetSetControl stagedAssetSetSummary:error:]
- +[MAAutoAssetSetControl stagedAssetSetSummary:limitedToSetIdentifiers:error:]
- +[MAAutoAssetSetSummary assetSetRepresentationName:]
- +[MAAutoAssetSetSummary summaryNewMaxColumnStrings]
- +[MAAutoAssetSetSummary summaryPaddedBanner:]
- +[MAAutoAssetSetSummary summaryPaddedHeader:]
- +[MAAutoAssetSetSummary summaryPaddedString:paddingToLenghtOfString:paddingWith:paddingBefore:]
- +[MAAutoAssetSetSummary supportsSecureCoding]
- +[MAThirdPartyCompatibility _sanitizedURLPathComponentFor:]
- -[MAAutoAssetSet _lockAtomicStatusProgress:lockAtomicError:progressBlock:]
- -[MAAutoAssetSet _newProxyObjectForSetProgressBlock:]
- -[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]
- -[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
- -[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
- -[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]
- -[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
- -[MAAutoAssetSetControl _successControlSummary:withJobSummaryEntries:isSynchronous:completion:]
- -[MAAutoAssetSetRapidLock setShortTermLockFileName:]
- -[MAAutoAssetSetSummary .cxx_destruct]
- -[MAAutoAssetSetSummary activeClientCount]
- -[MAAutoAssetSetSummary activeMonitorCount]
- -[MAAutoAssetSetSummary assetSetIdentifier]
- -[MAAutoAssetSetSummary assetSetRepresentationName]
- -[MAAutoAssetSetSummary assetSetRepresentation]
- -[MAAutoAssetSetSummary clientDomainName]
- -[MAAutoAssetSetSummary description]
- -[MAAutoAssetSetSummary encodeWithCoder:]
- -[MAAutoAssetSetSummary initWithCoder:]
- -[MAAutoAssetSetSummary initWithDomainName:forAssetSetIdentifier:withAssetSetRepresentation:withSetJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:]
- -[MAAutoAssetSetSummary maximumClientCount]
- -[MAAutoAssetSetSummary pushDelaySecs]
- -[MAAutoAssetSetSummary scheduledIntervalSecs]
- -[MAAutoAssetSetSummary scheduledRemainingSecs]
- -[MAAutoAssetSetSummary setActiveClientCount:]
- -[MAAutoAssetSetSummary setActiveMonitorCount:]
- -[MAAutoAssetSetSummary setAssetSetIdentifier:]
- -[MAAutoAssetSetSummary setAssetSetRepresentation:]
- -[MAAutoAssetSetSummary setClientDomainName:]
- -[MAAutoAssetSetSummary setJobStatus]
- -[MAAutoAssetSetSummary setMaximumClientCount:]
- -[MAAutoAssetSetSummary setPushDelaySecs:]
- -[MAAutoAssetSetSummary setScheduledIntervalSecs:]
- -[MAAutoAssetSetSummary setScheduledRemainingSecs:]
- -[MAAutoAssetSetSummary setSetJobStatus:]
- -[MAAutoAssetSetSummary setTotalClientCount:]
- -[MAAutoAssetSetSummary summaryBuildMaxColumnStrings:]
- -[MAAutoAssetSetSummary summaryPadded:]
- -[MAAutoAssetSetSummary summary]
- -[MAAutoAssetSetSummary totalClientCount]
- -[MAPushNotificationController asyncSubscribeToChannelWithIdentifier:]
- -[MAPushNotificationController asyncUnsubscribeToChannelWithIdentifier:]
- -[MAPushNotificationController triggerNotificationWithPayload:]
- GCC_except_table11
- GCC_except_table25
- GCC_except_table32
- GCC_except_table39
- GCC_except_table45
- GCC_except_table47
- GCC_except_table59
- GCC_except_table64
- _OBJC_CLASS_$_MAAutoAssetSetSummary
- _OBJC_CLASS_$_SUCoreDevice
- _OBJC_IVAR_$_MAAutoAssetSetSummary._activeClientCount
- _OBJC_IVAR_$_MAAutoAssetSetSummary._activeMonitorCount
- _OBJC_IVAR_$_MAAutoAssetSetSummary._assetSetIdentifier
- _OBJC_IVAR_$_MAAutoAssetSetSummary._assetSetRepresentation
- _OBJC_IVAR_$_MAAutoAssetSetSummary._clientDomainName
- _OBJC_IVAR_$_MAAutoAssetSetSummary._maximumClientCount
- _OBJC_IVAR_$_MAAutoAssetSetSummary._pushDelaySecs
- _OBJC_IVAR_$_MAAutoAssetSetSummary._scheduledIntervalSecs
- _OBJC_IVAR_$_MAAutoAssetSetSummary._scheduledRemainingSecs
- _OBJC_IVAR_$_MAAutoAssetSetSummary._setJobStatus
- _OBJC_IVAR_$_MAAutoAssetSetSummary._totalClientCount
- _OBJC_METACLASS_$_MAAutoAssetSetSummary
- __MAPreferencesCopyNSStringValue
- __OBJC_$_CLASS_METHODS_MAAutoAssetSetSummary
- __OBJC_$_CLASS_PROP_LIST_MAAutoAssetSetSummary
- __OBJC_$_INSTANCE_METHODS_MAAutoAssetSetSummary
- __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSetSummary
- __OBJC_$_PROP_LIST_MAAutoAssetSetSummary
- __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetSetSummary
- __OBJC_CLASS_RO_$_MAAutoAssetSetSummary
- __OBJC_METACLASS_RO_$_MAAutoAssetSetSummary
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.929
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.400
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.542
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1055
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1056
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke.78
- ___53-[MAAutoAssetSet _newProxyObjectForSetProgressBlock:]_block_invoke
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1081
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.899
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.581
- ___75+[MAAutoAssetSetControl activeSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke
- ___76+[MAAutoAssetSetControl knownAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke
- ___77+[MAAutoAssetSetControl lockedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke
- ___77+[MAAutoAssetSetControl stagedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke
- ___78+[MAAutoAssetSetControl scheduledSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.574
- ___93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
- ___93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
- ___93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
- ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
- ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
- ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1050
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1051
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1054
- ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
- ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
- ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
- ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
- ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
- ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
- ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
- ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
- ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
- ___Block_byref_object_copy_.1218
- ___Block_byref_object_copy_.693
- ___Block_byref_object_copy_.764
- ___Block_byref_object_dispose_.1219
- ___Block_byref_object_dispose_.694
- ___Block_byref_object_dispose_.765
- ____MAensureExtension_block_invoke.1225
- ____MAsendDownloadAsset_block_invoke.1127
- ____MAsendPMVCancelDownload_block_invoke.1145
- ____MAsendPMVDownload_block_invoke.1133
- ___block_descriptor_48_e8_32bs40r_e30_v16?0"MAAutoAssetSetStatus"8lr40l8s32l8
- ___block_literal_global.1039
- ___block_literal_global.1049
- ___block_literal_global.1050
- ___block_literal_global.1085
- ___block_literal_global.1091
- ___block_literal_global.1101
- ___block_literal_global.1106
- ___block_literal_global.1130
- ___block_literal_global.1270
- ___block_literal_global.1275
- ___block_literal_global.1277
- ___block_literal_global.1321
- ___block_literal_global.1343
- ___block_literal_global.2707
- ___block_literal_global.2709
- ___block_literal_global.2711
- ___block_literal_global.2713
- ___block_literal_global.474
- ___block_literal_global.505
- ___block_literal_global.521
- ___block_literal_global.527
- ___block_literal_global.529
- ___block_literal_global.636
- ___block_literal_global.692
- ___block_literal_global.698
- ___block_literal_global.700
- ___block_literal_global.77
- ___block_literal_global.782
- ___block_literal_global.787
- ___block_literal_global.789
- ___block_literal_global.791
- ___block_literal_global.81
- ___block_literal_global.83
- ___block_literal_global.969
- ___block_literal_global.971
- ___block_literal_global.973
- ___block_literal_global.976
- _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
- _kMobileAssetPreferencesThirdPartyStagingPathComponent
- _objc_msgSend$_activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:
- _objc_msgSend$_initForAssetType:withAssetSpecifier:matchingAssetVersion:usingDecryptionKey:setAtomicInstanceUUID:
- _objc_msgSend$_knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:
- _objc_msgSend$_lockAtomicStatusProgress:lockAtomicError:progressBlock:
- _objc_msgSend$_lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:
- _objc_msgSend$_newProxyObjectForSetProgressBlock:
- _objc_msgSend$_sanitizedURLPathComponentFor:
- _objc_msgSend$_scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:
- _objc_msgSend$_stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:
- _objc_msgSend$activeSetJobSummary:limitedToSetIdentifiers:error:
- _objc_msgSend$addCharactersInString:
- _objc_msgSend$alphanumericCharacterSet
- _objc_msgSend$assetSetRepresentation
- _objc_msgSend$assetSetRepresentationName
- _objc_msgSend$initWithPushReason:forAssetType:withAssetSpecifier:matchingAssetVersion:withUpdatePolicy:withAdditional:
- _objc_msgSend$isBootedOSSecureInternal
- _objc_msgSend$knownAssetSetSummary:limitedToSetIdentifiers:error:
- _objc_msgSend$lockedAssetSetSummary:limitedToSetIdentifiers:error:
- _objc_msgSend$precomposedStringWithCanonicalMapping
- _objc_msgSend$scheduledSetJobSummary:limitedToSetIdentifiers:error:
- _objc_msgSend$setJobStatus
- _objc_msgSend$sharedDevice
- _objc_msgSend$stagedAssetSetSummary:limitedToSetIdentifiers:error:
- _objc_msgSend$stringValue
- _objc_msgSend$subscribeToChannelWithIdentifier:
- _objc_msgSend$triggerPushNotificationWithPayload:
- _objc_msgSend$unsubscribeToChannelWithIdentifier:
CStrings:
+ "%@  + MAMsuDownloadOptions reqProdVersion: %@ reqBuildVersion: %@ delayPeriod: %ld managedDevice: %d allowSameVersion: %d prereqBuild: %@ prereqVersion: %@ prereqReleaseType: %@ liveAssetAudienceUUID: %@ purpose: %@"
+ "%{public}@ | no client progress block | %{public}@"
+ "<MAPushChannelId | identifier:%@ base64String:%@ populationType:%li name: %@>"
+ "@32@0:8@?16@24"
+ "B48@0:8@16i24^@28B36@?40"
+ "B48@0:8@16i24q28B36@?40"
+ "Base64ID"
+ "Channel Population ID: %{public}@"
+ "Channel population type: %li"
+ "Customer"
+ "Developer Seeding"
+ "Download failed as an AssetVersion downgrade was detected"
+ "Failed to retrieve server url for:(%@) from daemon. %ld"
+ "Identifier"
+ "Internal Livability"
+ "MA-auto-set{_checkAtomicStatusProgress}"
+ "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | SUCCESS"
+ "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | error:%{public}@"
+ "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | no client completion block"
+ "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | SUCCESS"
+ "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | error:%{public}@"
+ "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | no client completion block"
+ "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | SUCCESS"
+ "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | error:%{public}@"
+ "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | no client completion block"
+ "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | SUCCESS"
+ "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | error:%{public}@"
+ "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%{public}@ | no client completion block"
+ "MA-auto-set{_lockAtomicStatusProgress}"
+ "MAClearPreferences"
+ "MADownloadConflict"
+ "MAPushChannel"
+ "MAPushPopulationTypeCustomer"
+ "MAPushPopulationTypeDeveloperSeeding"
+ "MAPushPopulationTypeInternalLivability"
+ "MAPushPopulationTypeManagedSeeding"
+ "MAPushPopulationTypePublicSeeding"
+ "MAPushPopulationTypeUnknown"
+ "MA_CLEAR_PREFERENCES"
+ "ManagedSeeding"
+ "POSTPONE_JOB_CHECK_SPACE"
+ "PopulationType"
+ "Public Seeding"
+ "RequestedBuildVersion"
+ "Result of clearPreferences is %lld (%{public}@)"
+ "SecureMobileAssetDisableEarlyBootGraft"
+ "Subscribed to channel %{public}@"
+ "T@\"MAAutoAssetSelector\",&,N,V_fullAssetSelector"
+ "T@\"NSString\",&,N,V_assetID"
+ "T@\"NSString\",&,N,V_requestedBuildVersion"
+ "T@\"NSString\",R,&,N,V_shortTermLockFileName"
+ "T@\"NSString\",R,N,V_base64ChannelId"
+ "T@\"NSString\",R,N,V_identifier"
+ "TB,N,V_verboseLogging"
+ "Tq,R,N,V_populationType"
+ "Unknown Client"
+ "Unsubscribed to channel %{public}@"
+ "Using caching server for %{public}@ %{public}@ is enabled: %d"
+ "Y3VzdG9tZXIgaW9z"
+ "ZGV2ZWxvcGVyIGlvcw=="
+ "[WARNING] Channel ID is nil for identifier %{public}@"
+ "[WARNING] No population type ID for device!"
+ "_autoSetAtomicOperationStatusProgress:withLogMessage:progressBlock:"
+ "_base64ChannelId"
+ "_newProxyObjectForSetProgressBlock:withLogMessage:"
+ "_populationType"
+ "_requestedBuildVersion"
+ "_verboseLogging"
+ "asyncSubscribeToChannelWithIdentifier:completion:"
+ "asyncUnsubscribeToChannelWithIdentifier:completion:"
+ "bGl2YWJpbGl0eSBpb3M="
+ "bWFuYWdlZCBpb3M=py"
+ "base64ChannelId"
+ "base64String"
+ "cHVibGljIGlvcw=="
+ "channelIDForPopulationType"
+ "humanReadableChannelName"
+ "initWithIdentifier:"
+ "initWithPopulationType:"
+ "isEqualToPushChannelId:"
+ "no client completion block"
+ "pallasNoBuildVersionMatchFound"
+ "populationType"
+ "populationTypeString"
+ "requestedBuildVersion"
+ "setAssetID:"
+ "setFullAssetSelector:"
+ "setRequestedBuildVersion:"
+ "setVerboseLogging:"
+ "subscribeToChannelWithIdentifier:completion:"
+ "triggerNotificationWithPayload:withCompletion:"
+ "triggerPushNotificationWithPayload:withCompletion:"
+ "unsubscribeToChannelWithIdentifier:completion:"
+ "v16@?0@\"MAPushChannel\"8"
+ "v32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MAPushChannel\">24"
+ "verboseLogging"
+ "{_MAClearPreferences} Encoding error: %{public}@"
- "                    setJobStatus: N\n"
- "%@  + MAMsuDownloadOptions reqProdVersion: %@ delayPeriod: %ld managedDevice: %d allowSameVersion: %d prereqBuild: %@ prereqVersion: %@ prereqReleaseType: %@ liveAssetAudienceUUID: %@ purpose: %@"
- "%@|%@|%@|%@|%@|%@|%@|%@|%@|%@|%@"
- "-_"
- ">>>\n                clientDomainName: %@\n              assetSetIdentifier: %@\n          assetSetRepresentation: %@\n           scheduledIntervalSecs: %ld\n          scheduledRemainingSecs: %ld\n                   pushDelaySecs: %ld\n               activeClientCount: %ld\n              activeMonitorCount: %ld\n              maximumClientCount: %ld\n                totalClientCount: %ld\n%@<<<]"
- "@104@0:8@16@24q32@40q48q56q64q72q80q88q96"
- "MA-AUTO-SET-CONTROL(REPLY):ACTIVE_SET_JOB_SUMMARY"
- "MA-AUTO-SET-CONTROL(REPLY):KNOWN_ASSET_SET_SUMMARY"
- "MA-AUTO-SET-CONTROL(REPLY):LOCKED_ASSET_SET_SUMMARY"
- "MA-AUTO-SET-CONTROL(REPLY):SCHEDULED_SET_JOB_SUMMARY"
- "MA-AUTO-SET-CONTROL(REPLY):STAGED_ASSET_SET_SUMMARY"
- "MA-AUTO-SET-CONTROL:ACTIVE_SET_JOB_SUMMARY"
- "MA-AUTO-SET-CONTROL:KNOWN_ASSET_SET_SUMMARY"
- "MA-AUTO-SET-CONTROL:LOCKED_ASSET_SET_SUMMARY"
- "MA-AUTO-SET-CONTROL:SCHEDULED_SET_JOB_SUMMARY"
- "MA-AUTO-SET-CONTROL:STAGED_ASSET_SET_SUMMARY"
- "MA-auto-set-control{_successControlSummary} | %{public}@ | SUCCESS"
- "MA-auto-set-control{_successControlSummary} | %{public}@ | no client completion block"
- "MA-auto-set-control{activeSetJobSummary} | no client completion block | %{public}@"
- "MA-auto-set-control{knownAssetSummary} | no client completion block | %{public}@"
- "MA-auto-set-control{lockedAssetSetSummary} | no client completion block | %{public}@"
- "MA-auto-set-control{scheduledSetJobSummary} | no client completion block | %{public}@"
- "MA-auto-set-control{stagedAssetSetSummary} | no client completion block | %{public}@"
- "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | SUCCESS"
- "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | error:%{public}@"
- "MA-auto-set{_failedCheckAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | no client completion block"
- "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%@ | SUCCESS"
- "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%@ | error:%{public}@"
- "MA-auto-set{_failedCurrentSetStatus:%{public}@} | %{public}@ | assetSetIdentifier:%@ | no client completion block"
- "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | SUCCESS"
- "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | error:%{public}@"
- "MA-auto-set{_failedLockAtomic:%{public}@} | %{public}@ | assetSetIdentifier:%@ | no client completion block"
- "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%@ | SUCCESS"
- "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%@ | error:%{public}@"
- "MA-auto-set{_failedMapLockedAtomicEntry:%{public}@} | %{public}@ | assetSetIdentifier:%@ | no client completion block"
- "MA-auto-set{_lockAtomicStatusProgress} | no client progress block | %{public}@"
- "MAAutoAssetSetSummary"
- "MAThirdPartyCompatibility: %@ override (%@) provided, with illegal characters."
- "T@\"MAAutoAssetSetStatus\",&,N,V_setJobStatus"
- "T@\"NSString\",&,N,V_shortTermLockFileName"
- "T@\"NSString\",R,&,N,V_assetID"
- "The cache server is: %d"
- "ThirdPartyStagingBucketPathComponent"
- "ThirdPartyStagingPathComponent"
- "Tq,N,V_assetSetRepresentation"
- "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%{public}@ | expecting string or number or boolean"
- "_activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:"
- "_assetSetRepresentation"
- "_knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
- "_lockAtomicStatusProgress:lockAtomicError:progressBlock:"
- "_lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
- "_newProxyObjectForSetProgressBlock:"
- "_sanitizedURLPathComponentFor:"
- "_scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:"
- "_setJobStatus"
- "_stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
- "activeSetJobSummary"
- "activeSetJobSummary:error:"
- "activeSetJobSummary:limitedToSetIdentifiers:error:"
- "addCharactersInString:"
- "alphanumericCharacterSet"
- "assetSetRepresentation"
- "assetSetRepresentationName"
- "assetSetRepresentationName:"
- "asyncSubscribeToChannelWithIdentifier:"
- "asyncUnsubscribeToChannelWithIdentifier:"
- "clientDomain:%@|asset(%@)[%@]|status:%@|interval:%@|remaining:%@|pushDelay:%@|clients:%@|monitors:%@|maxClients:%@|totalClients:%@"
- "https://mesu.apple.com/3p/%@/%@/assets/%@/%@/"
- "https://mesu.apple.com/3p/%@/assets/%@/%@/"
- "https://mesu.apple.com/3p/assets/%@/%@/"
- "https://mesu.apple.com/3p/staging/assets/%@/%@/"
- "initWithDomainName:forAssetSetIdentifier:withAssetSetRepresentation:withSetJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:"
- "ios"
- "isBootedOSSecureInternal"
- "knownAssetSetSummary:error:"
- "knownAssetSetSummary:limitedToSetIdentifiers:error:"
- "lockedAssetSetSummary"
- "lockedAssetSetSummary:error:"
- "lockedAssetSetSummary:limitedToSetIdentifiers:error:"
- "no active-set-job-summary provided by server"
- "no staged-asset-set-summary provided by server"
- "precomposedStringWithCanonicalMapping"
- "scheduledSetJobSummary"
- "scheduledSetJobSummary:error:"
- "scheduledSetJobSummary:limitedToSetIdentifiers:error:"
- "setAssetSetRepresentation:"
- "setJobStatus"
- "setJobSummary"
- "setLockSummary"
- "setSetJobStatus:"
- "setShortTermLockFileName:"
- "sharedDevice"
- "stagedAssetSetSummary"
- "stagedAssetSetSummary:error:"
- "stagedAssetSetSummary:limitedToSetIdentifiers:error:"
- "stringValue"
- "triggerNotificationWithPayload:"
- "triggerPushNotificationWithPayload:"
- "v24@0:8@\"NSString\"16"
- "v48@0:8@16i24^@28B36@?40"
- "v48@0:8@16i24q28B36@?40"

```

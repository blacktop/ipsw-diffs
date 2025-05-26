## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2811.31.8.9.19
-  __TEXT.__text: 0x6af2c
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x6604
-  __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x5237
-  __TEXT.__oslogstring: 0x67a1
-  __TEXT.__gcc_except_tab: 0xad0
+2811.32.9.28.15
+  __TEXT.__text: 0x6c244
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x6684
+  __TEXT.__const: 0x134
+  __TEXT.__cstring: 0x53ab
+  __TEXT.__oslogstring: 0x6944
+  __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__unwind_info: 0x1ad4
   __TEXT.__objc_classname: 0xfde
-  __TEXT.__objc_methname: 0xfdff
-  __TEXT.__objc_methtype: 0x2fd5
-  __TEXT.__objc_stubs: 0xb7a0
+  __TEXT.__objc_methname: 0x100cb
+  __TEXT.__objc_methtype: 0x30d9
+  __TEXT.__objc_stubs: 0xb900
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x2168
+  __DATA_CONST.__const: 0x2218
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbcf0
-  __DATA_CONST.__objc_selrefs: 0x3b40
-  __AUTH_CONST.__cfstring: 0x3c80
+  __DATA_CONST.__objc_const: 0xbd50
+  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __AUTH_CONST.__cfstring: 0x3d00
   __AUTH_CONST.__objc_const: 0x2610
-  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x68
   __DATA.__objc_classrefs: 0x598
   __DATA.__objc_superrefs: 0x2f8
   __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x1b30
+  __DATA.__data: 0x1b40
   __DATA.__common: 0x10
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_ivar: 0x32c
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1b8
+  __DATA_DIRTY.__bss: 0x1c0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2527
-  Symbols:   8599
-  CStrings:  4378
+  Functions: 2550
+  Symbols:   8667
+  CStrings:  4418
 
Symbols:
+ +[GEOSharedNavState(Testing) _msp_testTripClosedTripInPast]
+ +[MSPSharedTripService _supportsPassingClosureReasons]
+ -[MSPSenderETAController _sendClosedStateWithReason:toIdentifiers:]
+ -[MSPSenderETAController stopSharingWith:reason:error:]
+ -[MSPSenderETAController stopSharingWithGroup:reason:error:]
+ -[MSPSenderETAController stopSharingWithReason:error:]
+ -[MSPSharedTripCapabilityLevelFetcher notifyObservers:]
+ -[MSPSharedTripContactController _stopAllSharingWithReason:queue:completion:]
+ -[MSPSharedTripContactController _stopSharingWithContactValue:reason:queue:completion:]
+ -[MSPSharedTripContactController stopAllSharingWithReason:queue:completion:]
+ -[MSPSharedTripContactController stopSharingWithContactValue:reason:queue:completion:]
+ -[MSPSharedTripFetchedStatus isEffectivelyEqualToStatus:]
+ -[MSPSharedTripServer stopSharingTripWithContacts:reason:completion:]
+ -[MSPSharedTripServer stopSharingTripWithMessagesGroup:reason:completion:]
+ -[MSPSharedTripServer stopSharingTripWithReason:completion:]
+ -[MSPSharedTripService _performBlockAfterInitialConnection:]
+ -[MSPSharedTripService _serviceCanAttemptConnection:]
+ -[MSPSharedTripService _stopAllSharingWithReason:completion:]
+ -[MSPSharedTripService _stopSharingTripWithContacts:reason:completion:]
+ -[MSPSharedTripService _stopSharingTripWithMessagesGroup:reason:completion:]
+ -[MSPSharedTripService _stopSharingTripWithReason:completion:]
+ -[MSPSharedTripService _stopSharingWithContact:reason:completion:]
+ -[MSPSharedTripService performBlockAfterInitialConnection:]
+ -[MSPSharedTripService stopAllSharingWithReason:completion:]
+ -[MSPSharedTripService stopSharingTripWithContacts:reason:completion:]
+ -[MSPSharedTripService stopSharingTripWithMessagesGroup:reason:completion:]
+ -[MSPSharedTripService stopSharingTripWithReason:completion:]
+ -[MSPSharedTripService stopSharingWithContact:reason:completion:]
+ -[MSPTransitStorageIncident(MSPExtra) artworkDataSource]
+ -[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdateForHandles:]
+ GCC_except_table100
+ GCC_except_table156
+ GCC_except_table185
+ GCC_except_table39
+ GCC_except_table53
+ GCC_except_table71
+ GCC_except_table76
+ GCC_except_table87
+ GCC_except_table97
+ _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_23
+ _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_24
+ _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_25
+ _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_26
+ _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_27
+ _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_28
+ _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_29
+ _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_30
+ _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_31
+ _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_32
+ _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_33
+ _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_34
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_35
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_36
+ _GEOConfigMSPShareETABlockedIDSStatusTTL_Metadata_block_invoke_21
+ _GEOConfigMSPShareETABlockedTripIDExpirationInterval_Metadata_block_invoke_16
+ _GEOConfigMSPShareETABlockedTripShouldAlwaysMigrateFromKVS_Metadata_block_invoke_17
+ _GEOConfigMSPShareETABlockedTripShouldClearKVSAfterMigration_Metadata_block_invoke_18
+ _GEOConfigMSPShareETACapabilityFetcherRetryInterval_Metadata_block_invoke_22
+ _GEOConfigMSPShareETAFailedIDSStatusTTL_Metadata_block_invoke_20
+ _GEOConfigMSPShareETAFetchedIDSStatusTTL_Metadata_block_invoke_19
+ _GEOConfigMSPShareETAIncludeMockClosedTripWithPastETAForUITesting
+ _GEOConfigMSPShareETAIncludeMockClosedTripWithPastETAForUITesting_Metadata
+ _GEOConfigMSPShareETAIncludeMockClosedTripWithPastETAForUITesting_Metadata_block_invoke_15
+ _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_37
+ _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_38
+ _MSPSharedTripReceivingAvailable.lastLoggedAvailability
+ _MSPSharedTripSharingAvailable.lastLoggedAvailability
+ __MSPSharedTripCurrentFeatureAvailability
+ __MSPSharedTripFeatureAvailabilityEqual
+ __MSPSharedTripFeatureAvailabilityToString
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MSPSharedTripCapabilityLevelFetcherObserver
+ ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.180
+ ___54+[MSPSharedTripService _supportsPassingClosureReasons]_block_invoke
+ ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.79
+ ___58-[MSPSharedTripServer listener:shouldAcceptNewConnection:]_block_invoke.130
+ ___59-[MSPSharedTripService performBlockAfterInitialConnection:]_block_invoke
+ ___60-[MSPSharedTripCapabilityLevelFetcher _fetchQueuesDidUpdate]_block_invoke.86
+ ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke
+ ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke.76
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.82
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.83
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.84
+ ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke
+ ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke_2
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_3
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_4
+ ___61-[MSPSharedTripService stopSharingTripWithReason:completion:]_block_invoke
+ ___65-[MSPSharedTripService stopSharingWithContact:reason:completion:]_block_invoke
+ ___65-[MSPSharedTripService stopSharingWithContact:reason:completion:]_block_invoke_2
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_3
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_4
+ ___70-[MSPSharedTripService stopSharingTripWithContacts:reason:completion:]_block_invoke
+ ___75-[MSPSharedTripService stopSharingTripWithMessagesGroup:reason:completion:]_block_invoke
+ ___76-[MSPSharedTripContactController stopAllSharingWithReason:queue:completion:]_block_invoke
+ ___77-[MSPSharedTripContactController _stopAllSharingWithReason:queue:completion:]_block_invoke
+ ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.121
+ ___82-[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdateForHandles:]_block_invoke
+ ___86-[MSPSharedTripContactController stopSharingWithContactValue:reason:queue:completion:]_block_invoke
+ ___87-[MSPSharedTripContactController _stopSharingWithContactValue:reason:queue:completion:]_block_invoke
+ ___87-[MSPSharedTripContactController _stopSharingWithContactValue:reason:queue:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e42_v24?0"MSPSharedTripService"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.103
+ ___block_literal_global.110
+ ___block_literal_global.117
+ ___block_literal_global.124
+ ___block_literal_global.131
+ ___block_literal_global.138
+ ___block_literal_global.145
+ ___block_literal_global.152
+ ___block_literal_global.159
+ ___block_literal_global.176
+ ___block_literal_global.188
+ ___block_literal_global.195
+ ___block_literal_global.202
+ ___block_literal_global.209
+ ___block_literal_global.221
+ ___block_literal_global.78
+ ___block_literal_global.79
+ ___block_literal_global.88
+ ___block_literal_global.94
+ ___block_literal_global.95
+ ___block_literal_global.97
+ __performBlockAfterInitialSync:.onceToken
+ _objc_msgSend$_msp_testTripClosedTripInPast
+ _objc_msgSend$_performBlockAfterInitialConnection:
+ _objc_msgSend$_sendClosedStateWithReason:toIdentifiers:
+ _objc_msgSend$_serviceCanAttemptConnection:
+ _objc_msgSend$_stopAllSharingWithReason:completion:
+ _objc_msgSend$_stopAllSharingWithReason:queue:completion:
+ _objc_msgSend$_stopSharingTripWithContacts:reason:completion:
+ _objc_msgSend$_stopSharingTripWithMessagesGroup:reason:completion:
+ _objc_msgSend$_stopSharingTripWithReason:completion:
+ _objc_msgSend$_stopSharingWithContact:reason:completion:
+ _objc_msgSend$_stopSharingWithContactValue:reason:queue:completion:
+ _objc_msgSend$_supportsPassingClosureReasons
+ _objc_msgSend$capabilityLevelFetcher:didUpdateCapabilityLevelsForHandles:
+ _objc_msgSend$closureReason
+ _objc_msgSend$hasClosureReason
+ _objc_msgSend$isEffectivelyEqualToStatus:
+ _objc_msgSend$notifyObservers:
+ _objc_msgSend$setClosureReason:
+ _objc_msgSend$setHasArrived:
+ _objc_msgSend$stopAllSharingWithReason:queue:completion:
+ _objc_msgSend$stopSharingTripWithContacts:reason:completion:
+ _objc_msgSend$stopSharingTripWithMessagesGroup:reason:completion:
+ _objc_msgSend$stopSharingTripWithReason:completion:
+ _objc_msgSend$stopSharingWith:reason:error:
+ _objc_msgSend$stopSharingWithContactValue:reason:queue:completion:
+ _objc_msgSend$stopSharingWithGroup:reason:error:
+ _objc_msgSend$stopSharingWithReason:error:
+ _objc_retain_x10
- -[MSPSenderETAController _sendFinishedToIdentifiers:]
- -[MSPSenderETAController stopSharing:]
- -[MSPSenderETAController stopSharingWith:error:]
- -[MSPSenderETAController stopSharingWithGroup:error:]
- -[MSPSharedTripCapabilityLevelFetcher notifyObservers]
- -[MSPSharedTripContactController _stopAllSharingWithQueue:completion:]
- -[MSPSharedTripContactController _stopSharingWithContactValue:queue:completion:]
- -[MSPSharedTripContactController stopAllSharingWithQueue:completion:]
- -[MSPSharedTripContactController stopSharingWithContactValue:queue:completion:]
- -[MSPSharedTripService _stopAllSharingWithCompletion:]
- -[MSPSharedTripService _stopSharingTripWithCompletion:]
- -[MSPSharedTripService _stopSharingTripWithContacts:completion:]
- -[MSPSharedTripService _stopSharingTripWithMessagesGroup:completion:]
- -[MSPSharedTripService _stopSharingWithContact:completion:]
- -[MSPSharedTripService stopSharingTripWithCompletion:]
- -[MSPSharedTripService stopSharingTripWithContacts:completion:]
- -[MSPSharedTripService stopSharingTripWithMessagesGroup:completion:]
- -[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdate]
- GCC_except_table142
- GCC_except_table171
- GCC_except_table34
- GCC_except_table50
- GCC_except_table58
- GCC_except_table74
- GCC_except_table84
- GCC_except_table86
- _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_22
- _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_23
- _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_24
- _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_25
- _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_26
- _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_27
- _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_28
- _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_29
- _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_30
- _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_31
- _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_32
- _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_33
- _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_34
- _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_35
- _GEOConfigMSPShareETABlockedIDSStatusTTL_Metadata_block_invoke_20
- _GEOConfigMSPShareETABlockedTripIDExpirationInterval_Metadata_block_invoke_15
- _GEOConfigMSPShareETABlockedTripShouldAlwaysMigrateFromKVS_Metadata_block_invoke_16
- _GEOConfigMSPShareETABlockedTripShouldClearKVSAfterMigration_Metadata_block_invoke_17
- _GEOConfigMSPShareETACapabilityFetcherRetryInterval_Metadata_block_invoke_21
- _GEOConfigMSPShareETAFailedIDSStatusTTL_Metadata_block_invoke_19
- _GEOConfigMSPShareETAFetchedIDSStatusTTL_Metadata_block_invoke_18
- _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_36
- _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_37
- __MSPSharedTripAvailable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MSPSharedTripCapabilityLevelFetcherObserver
- ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.167
- ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.76
- ___54-[MSPSharedTripService _stopAllSharingWithCompletion:]_block_invoke
- ___54-[MSPSharedTripService _stopAllSharingWithCompletion:]_block_invoke_2
- ___54-[MSPSharedTripService _stopAllSharingWithCompletion:]_block_invoke_3
- ___54-[MSPSharedTripService _stopAllSharingWithCompletion:]_block_invoke_4
- ___54-[MSPSharedTripService stopSharingTripWithCompletion:]_block_invoke
- ___58-[MSPSharedTripServer listener:shouldAcceptNewConnection:]_block_invoke.126
- ___59-[MSPSharedTripService _stopSharingWithContact:completion:]_block_invoke
- ___59-[MSPSharedTripService _stopSharingWithContact:completion:]_block_invoke_2
- ___59-[MSPSharedTripService _stopSharingWithContact:completion:]_block_invoke_3
- ___59-[MSPSharedTripService _stopSharingWithContact:completion:]_block_invoke_4
- ___60-[MSPSharedTripCapabilityLevelFetcher _fetchQueuesDidUpdate]_block_invoke.82
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.78
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.79
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.80
- ___63-[MSPSharedTripService stopSharingTripWithContacts:completion:]_block_invoke
- ___68-[MSPSharedTripService stopSharingTripWithMessagesGroup:completion:]_block_invoke
- ___69-[MSPSharedTripContactController stopAllSharingWithQueue:completion:]_block_invoke
- ___70-[MSPSharedTripContactController _stopAllSharingWithQueue:completion:]_block_invoke
- ___71-[_MSPSharedTripSingleCapabilityLevelFetcher capabilityLevelsDidUpdate]_block_invoke
- ___79-[MSPSharedTripContactController stopSharingWithContactValue:queue:completion:]_block_invoke
- ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.112
- ___80-[MSPSharedTripContactController _stopSharingWithContactValue:queue:completion:]_block_invoke
- ___80-[MSPSharedTripContactController _stopSharingWithContactValue:queue:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8r48l8s40l8
- ___block_literal_global.105
- ___block_literal_global.108
- ___block_literal_global.112
- ___block_literal_global.119
- ___block_literal_global.126
- ___block_literal_global.133
- ___block_literal_global.140
- ___block_literal_global.147
- ___block_literal_global.154
- ___block_literal_global.161
- ___block_literal_global.178
- ___block_literal_global.190
- ___block_literal_global.197
- ___block_literal_global.204
- ___block_literal_global.211
- ___block_literal_global.81
- ___block_literal_global.84
- ___block_literal_global.93
- ___block_literal_global.98
- _objc_msgSend$_sendFinishedToIdentifiers:
- _objc_msgSend$_stopAllSharingWithCompletion:
- _objc_msgSend$_stopAllSharingWithQueue:completion:
- _objc_msgSend$_stopSharingTripWithCompletion:
- _objc_msgSend$_stopSharingTripWithContacts:completion:
- _objc_msgSend$_stopSharingTripWithMessagesGroup:completion:
- _objc_msgSend$_stopSharingWithContact:completion:
- _objc_msgSend$_stopSharingWithContactValue:queue:completion:
- _objc_msgSend$stopAllSharingWithQueue:completion:
- _objc_msgSend$stopSharing:
- _objc_msgSend$stopSharingTripWithCompletion:
- _objc_msgSend$stopSharingTripWithContacts:completion:
- _objc_msgSend$stopSharingTripWithMessagesGroup:completion:
- _objc_msgSend$stopSharingWith:error:
- _objc_msgSend$stopSharingWithContactValue:queue:completion:
- _objc_msgSend$stopSharingWithGroup:error:
CStrings:
+ "- %{private}@ recorded as blocked+expired, but handle still blocked"
+ "-[MSPSharedTripServer stopSharingTripWithContacts:reason:completion:]"
+ "-[MSPSharedTripServer stopSharingTripWithMessagesGroup:reason:completion:]"
+ "-[MSPSharedTripServer stopSharingTripWithReason:completion:]"
+ "<%p groupID %@, last updated %@, closed %@ (reason: %lu), localName \"%@\", destination \"%@\" (%lu waypoints), current waypoint: %lu, reached %@, location %@, eta %@, (coords %@pt, routingPathLegs %@), traffic colors %@, muted %@, resumed %@"
+ "Available"
+ "B32@0:8Q16^@24"
+ "B40@0:8@16Q24^@32"
+ "MSPShareETAIncludeMockClosedTripWithPastETAForUITestingKey"
+ "MSPSharedTripCapabilityLevelFetcher notifyObservers for %lu updated handles: %{private}@"
+ "Not Available"
+ "Operation not permitted"
+ "Trip Receiving is %s: %{public}@"
+ "Trip Sharing is %s: %{public}@"
+ "Will send closed state with reason: %lu"
+ "[Service] %{public}@ supports archiving sharing state: %s"
+ "[Service] %{public}@ supports passing sharing closure reasons: %s"
+ "[Service] Call to deprecated performAfterInitialSync:, please use performBlockAfterInitialConnection: instead"
+ "[Service] Network reachability changed: %{public}@ -> %{public}@, notifying sending observers"
+ "_cleanUpNecessaryForGroup %{public}@ (updateLongerAgoThanExpiryInterval %#.1lfs %{public}@, arrived %{public}@, closed %{public}@ for reason %lu, etaInPast %{public}@)"
+ "_msp_testTripClosedTripInPast"
+ "_performBlockAfterInitialConnection:"
+ "_sendClosedStateWithReason:toIdentifiers:"
+ "_serviceCanAttemptConnection:"
+ "_stopAllSharingWithReason:completion:"
+ "_stopAllSharingWithReason:queue:completion:"
+ "_stopSharingTripWithContacts:reason:completion:"
+ "_stopSharingTripWithMessagesGroup:reason:completion:"
+ "_stopSharingTripWithReason:completion:"
+ "_stopSharingWithContact:reason:completion:"
+ "_stopSharingWithContactValue:reason:queue:completion:"
+ "_supportsPassingClosureReasons"
+ "artworkDataSource"
+ "capabilityLevelFetcher:didUpdateCapabilityLevelsForHandles:"
+ "capabilityLevelsDidUpdateForHandles:"
+ "closureReason"
+ "com.apple.Preferences"
+ "hasClosureReason"
+ "isEffectivelyEqualToStatus:"
+ "notifyObservers:"
+ "performBlockAfterInitialConnection:"
+ "serverEnabled: %@, userEnabled: %@, hasValidAccount: %@, mapsIsInstalled: %@, hasContactsAuthorisation: %@, processEntitledToShare: %@, processEntitledToReceive: %@"
+ "setClosureReason:"
+ "setHasArrived:"
+ "stopAllSharingWithReason:completion:"
+ "stopAllSharingWithReason:queue:completion:"
+ "stopSharingTripWithContacts:reason:completion:"
+ "stopSharingTripWithMessagesGroup:reason:completion:"
+ "stopSharingTripWithReason:completion:"
+ "stopSharingWith:reason:error:"
+ "stopSharingWithContact:reason:completion:"
+ "stopSharingWithContactValue:reason:queue:completion:"
+ "stopSharingWithGroup:reason:error:"
+ "stopSharingWithReason:error:"
+ "v24@?0@\"MSPSharedTripService\"8@\"NSError\"16"
+ "v32@0:8@\"MSPSharedTripCapabilityLevelFetcher\"16@\"NSSet\"24"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v48@0:8@16Q24@32@?40"
- "- %{private}@ recorded as blocked/expired, but still blocked"
- "-[MSPSharedTripServer stopSharingTripWithCompletion:]"
- "-[MSPSharedTripServer stopSharingTripWithContacts:completion:]"
- "-[MSPSharedTripServer stopSharingTripWithMessagesGroup:completion:]"
- "<%p groupID %@, last updated %@, closed %@, localName \"%@\", destination \"%@\" (%lu waypoints), current waypoint: %lu, reached %@, location %@, eta %@, (coords %@pt, routingPathLegs %@), traffic colors %@, muted %@, resumed %@"
- "MSPSharedTripCapabilityLevelFetcher notifyObservers"
- "[Service] Network reachability changed: %@ -> %@, notifying sending observers"
- "[Service] Supports archiving sharing state: %s"
- "_cleanUpNecessaryForGroup %@ updateLongerAgoThanExpiryInterval %@ arrived %@ closed %@ etaInPast %@"
- "_sendFinishedToIdentifiers:"
- "_stopAllSharingWithCompletion:"
- "_stopAllSharingWithQueue:completion:"
- "_stopSharingTripWithCompletion:"
- "_stopSharingTripWithContacts:completion:"
- "_stopSharingTripWithMessagesGroup:completion:"
- "_stopSharingWithContact:completion:"
- "_stopSharingWithContactValue:queue:completion:"
- "stopAllSharingWithQueue:completion:"
- "stopSharing:"
- "stopSharingWith:error:"
- "stopSharingWithContactValue:queue:completion:"
- "stopSharingWithGroup:error:"

```

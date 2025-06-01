## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.21.0.16.0
-  __TEXT.__text: 0x67d00
-  __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_methlist: 0x4e30
-  __TEXT.__const: 0x868
-  __TEXT.__cstring: 0x5f72
-  __TEXT.__oslogstring: 0x680c
-  __TEXT.__gcc_except_tab: 0x4cc
+301.21.1.3.0
+  __TEXT.__text: 0x6a824
+  __TEXT.__auth_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x5014
+  __TEXT.__const: 0x840
+  __TEXT.__cstring: 0x6231
+  __TEXT.__oslogstring: 0x6e24
+  __TEXT.__gcc_except_tab: 0x4d8
   __TEXT.__dlopen_cstrs: 0x35f
   __TEXT.__ustring: 0x136
-  __TEXT.__swift5_typeref: 0x7b0
-  __TEXT.__swift5_capture: 0x3bc
-  __TEXT.__swift5_reflstr: 0x24c
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x660
-  __TEXT.__swift5_fieldmd: 0x298
+  __TEXT.__swift5_typeref: 0x774
+  __TEXT.__swift5_capture: 0x398
+  __TEXT.__swift5_reflstr: 0x261
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__constg_swiftt: 0x67c
+  __TEXT.__swift5_fieldmd: 0x2dc
   __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__unwind_info: 0x2150
   __TEXT.__eh_frame: 0x1568
-  __TEXT.__objc_classname: 0x9c1
-  __TEXT.__objc_methname: 0xbc14
-  __TEXT.__objc_methtype: 0xbbc
-  __TEXT.__objc_stubs: 0x81e0
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x1bb0
-  __DATA_CONST.__objc_classlist: 0x358
-  __DATA_CONST.__objc_catlist: 0x28
+  __TEXT.__objc_classname: 0x9db
+  __TEXT.__objc_methname: 0xc192
+  __TEXT.__objc_methtype: 0xbf1
+  __TEXT.__objc_stubs: 0x8560
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x1cd0
+  __DATA_CONST.__objc_classlist: 0x360
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x76b8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_const: 0x7720
+  __DATA_CONST.__objc_selrefs: 0x2aa0
   __DATA_CONST.__objc_arraydata: 0x2060
-  __AUTH_CONST.__cfstring: 0x6aa0
-  __AUTH_CONST.__objc_const: 0x2d20
-  __AUTH_CONST.__const: 0x12a8
-  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__cfstring: 0x6ca0
+  __AUTH_CONST.__objc_const: 0x2df0
+  __AUTH_CONST.__const: 0x1320
+  __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0x1478
   __AUTH_CONST.__objc_arrayobj: 0x528
-  __AUTH_CONST.__auth_got: 0x8c8
-  __AUTH.__objc_data: 0x1548
+  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH.__objc_data: 0x1578
   __AUTH.__data: 0x688
-  __DATA.__objc_classrefs: 0x528
-  __DATA.__objc_superrefs: 0x258
-  __DATA.__objc_ivar: 0x608
-  __DATA.__data: 0x540
+  __DATA.__objc_classrefs: 0x530
+  __DATA.__objc_superrefs: 0x268
+  __DATA.__objc_ivar: 0x610
+  __DATA.__data: 0x520
   __DATA.__bss: 0xb60
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xcb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A787CE43-5EAE-3C9B-A934-D33236790B10
-  Functions: 2758
-  Symbols:   7616
-  CStrings:  4680
+  UUID: 5497773F-3DCA-3C96-A842-CF4904507712
+  Functions: 2836
+  Symbols:   7777
+  CStrings:  4800
 
Symbols:
+ +[FLFollowUpController(ICQUI) icq_dismissFollowUpWithIdentifier:]
+ +[ICQDaemonEventOffer _mutablePlaceholderPersistanceDictionary]
+ +[ICQDaemonEventOffer persistenceKey]
+ +[ICQDaemonOfferConditions backupRestoreComplete]
+ +[ICQError _errorWithCode:statusCode:]
+ +[ICQError clientErrorWithStatusCode:]
+ +[_ICQFollowupSpecification clearFollowupWithController:offerType:completion:]
+ +[_ICQFollowupSpecification clearNotificationWithController:offerType:completion:]
+ +[_ICQHelperFunctions _fetchNextBackupSize:]
+ +[_ICQHelperFunctions _fetchNextBackupSize:].cold.1
+ +[_ICQHelperFunctions _requestedEventOfferInOptions:]
+ +[_ICQHelperFunctions backupRestoreCompletedInOptions:]
+ +[_ICQHelperFunctions followUpIdentifierPrefixForRequestType:]
+ +[_ICQHelperFunctions standardDateFormat:]
+ -[ICQDaemonEventOffer _initWithAccount:error:]
+ -[ICQDaemonOffer isEventOffer]
+ -[ICQDaemonOffer requestType]
+ -[ICQDaemonOfferConditions isBackupRestoreComplete]
+ -[ICQDaemonOfferConditions setBackupRestoreComplete:]
+ -[ICQDaemonOfferManager _processOfferStub:account:offerType:]
+ -[ICQDaemonOfferManager _teardownCachedEventOfferAndNotify:]
+ -[ICQDaemonOfferManager clearFollowupsOfferType:completion:]
+ -[ICQDaemonOfferManager tearDownCachedEventOffer]
+ -[ICQDaemonOfferRequestBuilder renewAuthHeadersForRequest:completion:]
+ -[ICQDaemonOfferStub isEventOffer]
+ -[ICQDaemonOfferStubs chooseEventStubForConditions:]
+ -[ICQDaemonOfferStubs chooseEventStub]
+ -[ICQDaemonOfferStubs chooseFirstEventStub]
+ -[ICQDaemonOfferStubs eventStubs]
+ -[ICQLink hasServerUIAction]
+ -[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]
+ -[ICQOfferManager getEventOfferWithOptions:completion:]
+ -[ICQOfferManager(Testing) teardownCachedEventOffer]
+ -[NSMutableURLRequest(ICQ) icq_hasAuthHeaders]
+ -[NSMutableURLRequest(ICQ) icq_renewAuthorizationHeadersForAccount:store:completion:]
+ -[NSMutableURLRequest(ICQ) icq_renewAuthorizationHeadersForAccount:store:completion:].cold.1
+ -[NSURL(ICQ) icq_URLByAppendingQueryItems:]
+ -[NSURL(ICQ) icq_URLByAppendingQueryParamName:value:]
+ -[NSURL(ICQ) icq_queryItemForName:]
+ -[_ICQFollowupSpecification eventOffer]
+ -[_ICQFollowupSpecification setEventOffer:]
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table23
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table56
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table90
+ _ICQActionParameterDismissLockScreenKey
+ _ICQActionParameterFollowUpIdentifierKey
+ _ICQActionParameterSkipCFUKey
+ _ICQStatusCodeKey
+ _ICQiCloudSettingsUniversalURL
+ _OBJC_CLASS_$_ICQAnalytics
+ _OBJC_CLASS_$_ICQDaemonEventOffer
+ _OBJC_IVAR_$_ICQDaemonOfferConditions._backupRestoreComplete
+ _OBJC_IVAR_$_ICQDaemonOfferStubs._eventStubs
+ _OBJC_IVAR_$__ICQFollowupSpecification._eventOffer
+ _OBJC_METACLASS_$_ICQAnalytics
+ _OBJC_METACLASS_$_ICQDaemonEventOffer
+ __DATA_ICQAnalytics
+ __DATA__TtC11iCloudQuota22ManageStorageAnalytics
+ __ICQBackupRestoreCompletedKey
+ __ICQDaemonOfferChangedDueToPushDarwinNotificationNameEvent
+ __ICQIdentifierPrefixEvent
+ __ICQIsEventOfferDictionary
+ __ICQIsEventOfferKey
+ __IVARS__TtC11iCloudQuota22ManageStorageAnalytics
+ __METACLASS_DATA_ICQAnalytics
+ __METACLASS_DATA__TtC11iCloudQuota22ManageStorageAnalytics
+ __OBJC_$_CATEGORY_FLFollowUpController_$_ICQUI
+ __OBJC_$_CLASS_METHODS_FLFollowUpController(ICQUI)
+ __OBJC_$_CLASS_METHODS_ICQDaemonEventOffer
+ __OBJC_$_INSTANCE_METHODS_ICQAnalytics
+ __OBJC_$_INSTANCE_METHODS_ICQDaemonEventOffer
+ __OBJC_CLASS_RO_$_ICQDaemonEventOffer
+ __OBJC_METACLASS_RO_$_ICQDaemonEventOffer
+ ___107-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdDisplayDelayedOfferWithContext:completion:]_block_invoke.576
+ ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke.373
+ ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke.383
+ ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke_2.384
+ ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke_3.385
+ ___125-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchNewOfferResponseWithContent:andMaxDelaySecs:completion:]_block_invoke.574
+ ___142-[ICQDaemonOfferManager _fetchDictionaryForAccount:quotaKey:quotaReason:stub:notificationID:contextDictionary:mlDaemonExtraFields:completion:]_block_invoke_2
+ ___143-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchDaemonOfferForAccount:stub:notificationID:isoNewOfferResponse:completion:]_block_invoke.571
+ ___143-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchDaemonOfferForAccount:stub:notificationID:isoNewOfferResponse:completion:]_block_invoke.571.cold.1
+ ___162-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdRefreshOfferDetailsAndDisplay:completion:account:accountStore:notificationID:isoNewOfferResponse:]_block_invoke.570
+ ___39-[ICQOfferManager _refetchDefaultOffer]_block_invoke.54
+ ___43-[ICQOfferManager postBackupRestoredOffer:]_block_invoke
+ ___43-[ICQOfferManager postBackupRestoredOffer:]_block_invoke.cold.1
+ ___44+[_ICQHelperFunctions _fetchNextBackupSize:]_block_invoke
+ ___55-[ICQOfferManager getEventOfferWithOptions:completion:]_block_invoke
+ ___55-[ICQOfferManager getEventOfferWithOptions:completion:]_block_invoke.cold.1
+ ___56-[ICQDaemonOfferManager _getHandlerForBundleId:options:]_block_invoke_3
+ ___57-[ICQDaemonOfferManager clearAllFollowupsWithCompletion:]_block_invoke_3
+ ___60-[ICQDaemonOfferManager _teardownCachedEventOfferAndNotify:]_block_invoke
+ ___60-[ICQDaemonOfferManager clearFollowupsOfferType:completion:]_block_invoke
+ ___60-[ICQDaemonOfferManager clearFollowupsOfferType:completion:]_block_invoke.cold.1
+ ___61-[ICQDaemonOfferManager _processOfferStub:account:offerType:]_block_invoke
+ ___61-[ICQDaemonOfferManager _processOfferStub:account:offerType:]_block_invoke.241
+ ___65+[FLFollowUpController(ICQUI) icq_dismissFollowUpWithIdentifier:]_block_invoke
+ ___66+[ICQDaemonOfferManager getCkBackupDeviceIDWithCompletionHandler:]_block_invoke.370
+ ___66+[ICQDaemonOfferManager getCkBackupDeviceIDWithCompletionHandler:]_block_invoke.370.cold.1
+ ___67-[NSMutableURLRequest(ICQ) icq_addHeadersForUpgradeWithCompletion:]_block_invoke.32
+ ___67-[NSMutableURLRequest(ICQ) icq_addHeadersForUpgradeWithCompletion:]_block_invoke.32.cold.1
+ ___67-[NSMutableURLRequest(ICQ) icq_addHeadersForUpgradeWithCompletion:]_block_invoke.cold.1
+ ___70-[ICQDaemonOfferRequestBuilder renewAuthHeadersForRequest:completion:]_block_invoke
+ ___70-[ICQDaemonOfferRequestBuilder renewAuthHeadersForRequest:completion:]_block_invoke.cold.1
+ ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.263
+ ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.264
+ ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke_2.265
+ ___76-[ICQDaemonOfferManager daemonOfferDictionaryForAccount:options:completion:]_block_invoke.183
+ ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke_2
+ ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke_2.cold.1
+ ___82+[_ICQFollowupSpecification clearNotificationWithController:offerType:completion:]_block_invoke
+ ___84-[ICQDaemonOfferManager _persistAndNotifyMissingPlaceholdersForRequestType:account:]_block_invoke
+ ___85-[NSMutableURLRequest(ICQ) icq_renewAuthorizationHeadersForAccount:store:completion:]_block_invoke
+ ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.38
+ ___93-[ICQDaemonOfferManager _coalescedFetchDaemonOfferForAccount:stub:notificationID:completion:]_block_invoke.344
+ ___93-[ICQDaemonOfferManager _coalescedFetchDaemonOfferForAccount:stub:notificationID:completion:]_block_invoke.344.cold.1
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.21
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.21.cold.1
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.25
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.25.cold.1
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.cold.1
+ ___95-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:]_block_invoke.cold.2
+ ___98-[ICQDaemonOfferManager _showDaemonAlertForOffer:notificationDictionary:store:account:completion:]_block_invoke.350
+ ___98-[ICQDaemonOfferManager _showDaemonAlertForOffer:notificationDictionary:store:account:completion:]_block_invoke.351
+ ___block_descriptor_112_e8_32s40s48s56bs64bs72r80r88r96r104w_e5_v8?0lw104l8s32l8s56l8r72l8r80l8s40l8r88l8r96l8s48l8s64l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32s_e39_v24?0"NSMutableURLRequest"8?<v?B>16ls32l8
+ ___block_descriptor_48_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e8_v12?0B8lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72r80r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8r56l8s48l8r64l8r72l8r80l8s40l8
+ ___block_literal_global.134
+ ___block_literal_global.189
+ ___block_literal_global.258
+ ___block_literal_global.334
+ ___block_literal_global.346
+ ___block_literal_global.363
+ ___block_literal_global.382
+ ___block_literal_global.55
+ ___block_literal_global.569
+ ___block_literal_global.573
+ ___block_literal_global.578
+ ___block_literal_global.71
+ ___block_literal_global.85
+ ___kCFBooleanFalse
+ ___swift_memcpy16_8
+ ___swift_memcpy40_8
+ __unnamed_array_storage.169
+ __unnamed_array_storage.170
+ __unnamed_array_storage.190
+ __unnamed_array_storage.285
+ __unnamed_array_storage.291
+ __unnamed_array_storage.294
+ __unnamed_array_storage.295
+ __unnamed_array_storage.297
+ __unnamed_array_storage.52
+ _dispatch_assert_queue_not$V2
+ _kACRenewCredentialsShouldAvoidUIKey
+ _kACRenewCredentialsShouldForceKey
+ _objc_msgSend$_errorWithCode:statusCode:
+ _objc_msgSend$_fetchNextBackupSize:
+ _objc_msgSend$_processOfferStub:account:offerType:
+ _objc_msgSend$_requestedEventOfferInOptions:
+ _objc_msgSend$_teardownCachedEventOfferAndNotify:
+ _objc_msgSend$backupRestoreComplete
+ _objc_msgSend$backupRestoreCompletedInOptions:
+ _objc_msgSend$chooseEventStub
+ _objc_msgSend$chooseEventStubForConditions:
+ _objc_msgSend$chooseFirstEventStub
+ _objc_msgSend$clearFollowupWithController:offerType:completion:
+ _objc_msgSend$clearFollowupsOfferType:completion:
+ _objc_msgSend$clientErrorWithStatusCode:
+ _objc_msgSend$dateFormat
+ _objc_msgSend$eventOffer
+ _objc_msgSend$eventStubs
+ _objc_msgSend$executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:
+ _objc_msgSend$followUpIdentifierPrefixForRequestType:
+ _objc_msgSend$getEventOfferWithOptions:completion:
+ _objc_msgSend$icq_URLByAppendingQueryItems:
+ _objc_msgSend$icq_hasAuthHeaders
+ _objc_msgSend$icq_renewAuthorizationHeadersForAccount:store:completion:
+ _objc_msgSend$isBackupRestoreComplete
+ _objc_msgSend$isEventOffer
+ _objc_msgSend$renewAuthHeadersForRequest:completion:
+ _objc_msgSend$renewCredentialsForAccount:options:completion:
+ _objc_msgSend$setBackupRestoreComplete:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$standardDateFormat:
+ _objc_msgSend$tearDownCachedEventOffer
+ _objc_msgSend$valueForHTTPHeaderField:
+ _symbolic SDySSypGSg
+ _symbolic SS13appIdentifier_t
+ _symbolic So29ICQCloudStorageDataControllerCSg
+ _symbolic _____ 11iCloudQuota22ManageStorageAnalyticsC
+ _symbolic _____ 11iCloudQuota9AnalyticsC5EventV
+ _symbolic _____ 11iCloudQuota9AnalyticsC7JourneyO
+ _symbolic _____Sg 11iCloudQuota9AnalyticsC7JourneyO
- +[_ICQFollowupSpecification clearFollowupWithController:isPremium:completion:]
- +[_ICQFollowupSpecification clearNotificationWithController:isPremium:completion:]
- -[ICQDaemonOfferManager _processOfferStub:account:isPremiumOffer:]
- -[ICQDaemonOfferManager clearFollowupsIsPremiumOffer:completion:]
- -[ICQNetworkRequestController executeRequest:acceptedStatusCodes:completion:]
- GCC_except_table104
- GCC_except_table20
- GCC_except_table26
- GCC_except_table33
- GCC_except_table44
- GCC_except_table46
- GCC_except_table54
- GCC_except_table64
- GCC_except_table71
- GCC_except_table86
- GCC_except_table99
- _OBJC_CLASS_$__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- _OBJC_IVAR_$_ICQLink._serverUIURL
- _OBJC_METACLASS_$__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- __DATA__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- __DATA__TtC11iCloudQuota9Analytics
- __IVARS__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- __IVARS__TtC11iCloudQuota9Analytics
- __METACLASS_DATA__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- __METACLASS_DATA__TtC11iCloudQuota9Analytics
- __OBJC_$_INSTANCE_METHODS__TtC11iCloudQuota29AppsSyncingToiCloudDriveModel
- ___107-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdDisplayDelayedOfferWithContext:completion:]_block_invoke.574
- ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke.369
- ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke.375
- ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke_2.380
- ___118-[ICQDaemonOfferManager _coalescedReconsiderOffersForAccount:isForBuddy:quotaReason:options:choiceHandler:completion:]_block_invoke_3.381
- ___125-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchNewOfferResponseWithContent:andMaxDelaySecs:completion:]_block_invoke.573
- ___143-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchDaemonOfferForAccount:stub:notificationID:isoNewOfferResponse:completion:]_block_invoke.570
- ___143-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdFetchDaemonOfferForAccount:stub:notificationID:isoNewOfferResponse:completion:]_block_invoke.570.cold.1
- ___162-[ICQDaemonOfferManager(iCloudSubscriptionOptimizerDaemon) _subdRefreshOfferDetailsAndDisplay:completion:account:accountStore:notificationID:isoNewOfferResponse:]_block_invoke.569
- ___39-[ICQOfferManager _refetchDefaultOffer]_block_invoke.53
- ___65-[ICQDaemonOfferManager clearFollowupsIsPremiumOffer:completion:]_block_invoke
- ___65-[ICQDaemonOfferManager clearFollowupsIsPremiumOffer:completion:]_block_invoke.cold.1
- ___66+[ICQDaemonOfferManager getCkBackupDeviceIDWithCompletionHandler:]_block_invoke.366
- ___66+[ICQDaemonOfferManager getCkBackupDeviceIDWithCompletionHandler:]_block_invoke.366.cold.1
- ___66-[ICQDaemonOfferManager _processOfferStub:account:isPremiumOffer:]_block_invoke
- ___66-[ICQDaemonOfferManager _processOfferStub:account:isPremiumOffer:]_block_invoke.238
- ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.266
- ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.267
- ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke_2.268
- ___76-[ICQDaemonOfferManager daemonOfferDictionaryForAccount:options:completion:]_block_invoke.182
- ___77-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:completion:]_block_invoke
- ___77-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:completion:]_block_invoke.21
- ___77-[ICQNetworkRequestController executeRequest:acceptedStatusCodes:completion:]_block_invoke.cold.1
- ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke.121
- ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke.124
- ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke.124.cold.1
- ___78+[_ICQHelperFunctions remoteBackupSizeForAccount:timeoutInSeconds:completion:]_block_invoke.cold.1
- ___82+[_ICQFollowupSpecification clearNotificationWithController:isPremium:completion:]_block_invoke
- ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.37
- ___93-[ICQDaemonOfferManager _coalescedFetchDaemonOfferForAccount:stub:notificationID:completion:]_block_invoke.340
- ___93-[ICQDaemonOfferManager _coalescedFetchDaemonOfferForAccount:stub:notificationID:completion:]_block_invoke.340.cold.1
- ___98-[ICQDaemonOfferManager _showDaemonAlertForOffer:notificationDictionary:store:account:completion:]_block_invoke.346
- ___98-[ICQDaemonOfferManager _showDaemonAlertForOffer:notificationDictionary:store:account:completion:]_block_invoke.347
- ___block_descriptor_41_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8s56l8r64l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80w_e5_v8?0lw80l8s32l8s64l8r72l8s40l8s48l8s56l8
- ___block_literal_global.126
- ___block_literal_global.246
- ___block_literal_global.336
- ___block_literal_global.342
- ___block_literal_global.355
- ___block_literal_global.378
- ___block_literal_global.49
- ___block_literal_global.568
- ___block_literal_global.572
- ___block_literal_global.577
- ___block_literal_global.61
- ___block_literal_global.79
- __swift_stdlib_reportUnimplementedInitializer
- __unnamed_array_storage.163
- __unnamed_array_storage.181
- __unnamed_array_storage.278
- __unnamed_array_storage.279
- __unnamed_array_storage.282
- __unnamed_array_storage.283
- __unnamed_array_storage.288
- __unnamed_array_storage.300
- __unnamed_array_storage.46
- _associated conformance 11iCloudQuota014AppsSyncingToiA10DriveModelC7Combine16ObservableObjectAA0J19WillChangePublisherAdEP_AD0M0
- _block_copy_helper.10
- _block_descriptor.12
- _block_destroy_helper.11
- _objc_msgSend$_processOfferStub:account:isPremiumOffer:
- _objc_msgSend$clearFollowupWithController:isPremium:completion:
- _objc_msgSend$clearFollowupsIsPremiumOffer:completion:
- _objc_msgSend$executeRequest:acceptedStatusCodes:completion:
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
- _symbolic So21ICQAppsSyncingToDriveC
- _symbolic So21ICQAppsSyncingToDriveCSg
- _symbolic _____ 11iCloudQuota014AppsSyncingToiA10DriveModelC
- _symbolic _____SgXw 11iCloudQuota014AppsSyncingToiA10DriveModelC
- _symbolic _____ySo21ICQAppsSyncingToDriveCSgG 7Combine9PublishedV
- _symbolic _____ySo21ICQAppsSyncingToDriveCSg_G 7Combine9PublishedV9PublisherV
CStrings:
+ "\x01\""
+ " enableTelemetry=YES "
+ "$__lazy_storage_$_dataController"
+ "%s account change detected while validating auth headers. request %@"
+ "%s renew credentials returned with result %lu, error %@"
+ "-[NSMutableURLRequest(ICQ) icq_renewAuthorizationHeadersForAccount:store:completion:]"
+ "-[NSMutableURLRequest(ICQ) icq_renewAuthorizationHeadersForAccount:store:completion:]_block_invoke"
+ "400 or 401 but we have not attempted to renew yet."
+ "@32@0:8q16q24"
+ "Account not provided, skipping check"
+ "Adding event offer stub %@"
+ "Already attempted renewal, giving up on this request"
+ "Attempting to clear followup! offer type: %@"
+ "Auth headers validated with success: %d request: %@"
+ "Backup restore offer found: %@"
+ "Backup restore offer not found with error: %@"
+ "Chose backup restored stub %@"
+ "Clearing ICQFollowup items for offerType %@"
+ "Creating backup restored offer placeholder"
+ "Event"
+ "Event offer did not have an ID, this usually means no backup offer was fetched and we got a placeholder instead"
+ "Failed to clear followup with error %{public}@, offerType: %@"
+ "Failed to renew headers, will not launch request"
+ "Failed to renew headers, will not retry"
+ "Finished getting stubs"
+ "ICQAnalytics"
+ "ICQDaemonEventOffer"
+ "ICQDaemonOfferChangedDueToPushDarwinNotificationEvent"
+ "ICQDaemonOfferRequestBuilder renewAuthHeadersForRequest validation completed with success: %d"
+ "ICQUI"
+ "Missing auth header or client info header, attempting to renew credentials. request: %@"
+ "Missing auth headers and no account provided or found, unable to renew credentials."
+ "Request (%@) failed from client error %ld with data (%@) with response (%@) with error (%@). Will attempt to renew headers."
+ "Request headers renewed successfully"
+ "Reverting to original backup restore notification"
+ "SIGNPOST BEGIN [id: %hu]: StorageAppsRequest  enableTelemetry=YES "
+ "Skipping CFU for lockscreen link: %@"
+ "Succeeded at clearing followup! offerType: %@"
+ "Successfully cleared lockscreen notification for followup item ID %@"
+ "T@\"NSArray\",R,N,V_eventStubs"
+ "T@\"NSURL\",&,N"
+ "TB,N,GisBackupRestoreComplete,V_backupRestoreComplete"
+ "TB,N,V_eventOffer"
+ "TB,R,N,GisEventOffer"
+ "Unable to clear lockscreen notification for followup item ID %@, error: %@"
+ "User hit event: %s"
+ "Validating auth headers"
+ "X-Apple-Locale-Date-Format-Long"
+ "X-Apple-Locale-Date-Format-Short"
+ "X-MMe-Client-Info"
+ "_ICQCachedEventOfferInternal"
+ "_TtC11iCloudQuota22ManageStorageAnalytics"
+ "_backupRestoreComplete"
+ "_errorWithCode:statusCode:"
+ "_eventOffer"
+ "_eventStubs"
+ "_fetchNextBackupSize:"
+ "_processOfferStub:account:offerType:"
+ "_requestedEventOfferInOptions:"
+ "_teardownCachedEventOfferAndNotify:"
+ "allSetScreenImpressionWithAttributingAppIdentifier:"
+ "all_set_impression_"
+ "backupRestoreComplete"
+ "backupRestoreCompletedInOptions:"
+ "chooseEventStub"
+ "chooseEventStubForConditions:"
+ "chooseFirstEventStub"
+ "clearFollowupWithController:offerType:completion:"
+ "clearFollowupsOfferType:completion:"
+ "clearNotificationWithController:offerType:completion:"
+ "clientErrorWithStatusCode:"
+ "com.apple.iCloudQuota.analytics"
+ "com.apple.iCloudQuotaDaemon.ICQFollowupEvent"
+ "dateFormat"
+ "dismissLockScreen"
+ "eventOffer"
+ "eventOffers"
+ "eventStubs"
+ "executeRequest:acceptedStatusCodes:renewHeadersBlock:completion:"
+ "followUpIdentifierPrefixForRequestType:"
+ "followUpItemIdentifier"
+ "freshmintPageDisplayedFromInAppBannerWithAppIdentifier:"
+ "freshmintPageInteractionFromInAppBannerWithAppIdentifier:interactionIdentifier:"
+ "freshmint_display"
+ "getEventOfferWithOptions:completion:"
+ "hasServerUIAction"
+ "https://icq.icloud.com"
+ "https://setup.icloud.com/email/prefs/storage?root=APPLE_ACCOUNT&path=ICLOUD_SERVICE"
+ "icq_URLByAppendingQueryItems:"
+ "icq_URLByAppendingQueryParamName:value:"
+ "icq_dismissFollowUpWithIdentifier:"
+ "icq_hasAuthHeaders"
+ "icq_queryItemForName:"
+ "icq_renewAuthorizationHeadersForAccount:store:completion:"
+ "isBackupRestoreComplete"
+ "isEventOffer"
+ "loadFailedWithLoadIdentifier:duration:errorCode:"
+ "loadSucceededWithLoadIdentifier:duration:"
+ "logInAppBannerEventWithAppIdentifier:eventName:"
+ "offer: %@ and error: %@"
+ "renewAuthHeadersForRequest:completion:"
+ "renewCredentialsForAccount:options:completion:"
+ "request already has auth headers. request: %@"
+ "setBackupRestoreComplete:"
+ "setDateStyle:"
+ "setEventOffer:"
+ "setTimeStyle:"
+ "skipCFU"
+ "standardDateFormat:"
+ "tearDownCachedEventOffer"
+ "teardownCachedEventOffer"
+ "v24@?0@\"NSMutableURLRequest\"8@?<v@?B>16"
+ "v40@0:8@16@24q32"
+ "v40@0:8@16q24q32"
+ "v48@0:8@16@24@?32@?40"
+ "validateAuthorizationHeaders completed renew credentials with success: %d"
+ "valueForHTTPHeaderField:"
- "\x01#"
- "Attempting to clear followup! isPremium: %@"
- "Clearing ICQFollowup items for %@ offer"
- "Error fetching Apps Syncing to Drive %@"
- "Failed to clear followup with error %{public}@, isPremium: %@"
- "SIGNPOST BEGIN [id: %hu]: StorageAppsRequest "
- "Setting up notification link: %@"
- "Succeeded at clearing followup! isPremium: %@"
- "_TtC11iCloudQuota29AppsSyncingToiCloudDriveModel"
- "_TtC11iCloudQuota9Analytics"
- "_iCloudDriveApps"
- "_processOfferStub:account:isPremiumOffer:"
- "clearFollowupWithController:isPremium:completion:"
- "clearFollowupsIsPremiumOffer:completion:"
- "clearNotificationWithController:isPremium:completion:"
- "executeRequest:acceptedStatusCodes:completion:"
- "iCloudQuota.AppsSyncingToiCloudDriveModel"
- "init()"

```

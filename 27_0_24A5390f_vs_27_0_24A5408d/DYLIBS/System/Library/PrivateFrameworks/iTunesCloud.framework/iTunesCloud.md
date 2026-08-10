## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.110.81.1.0
-  __TEXT.__text: 0x3c126c
-  __TEXT.__objc_methlist: 0x1811c
+4026.110.1.0.0
+  __TEXT.__text: 0x3c9cac
+  __TEXT.__objc_methlist: 0x187cc
   __TEXT.__const: 0x225e8
   __TEXT.__dlopen_cstrs: 0x4cf
-  __TEXT.__gcc_except_tab: 0x2b08
-  __TEXT.__cstring: 0x175fa
-  __TEXT.__oslogstring: 0x20a3c
+  __TEXT.__gcc_except_tab: 0x2b50
+  __TEXT.__cstring: 0x17a42
+  __TEXT.__oslogstring: 0x22336
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x6970
+  __TEXT.__unwind_info: 0x6b10
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7338
-  __DATA_CONST.__objc_classlist: 0xd90
+  __DATA_CONST.__const: 0x7448
+  __DATA_CONST.__objc_classlist: 0xdd0
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x2e8
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa320
-  __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xbc0
+  __DATA_CONST.__objc_selrefs: 0xa570
+  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x1058
-  __AUTH_CONST.__const: 0x18438
-  __AUTH_CONST.__cfstring: 0x185c0
-  __AUTH_CONST.__objc_const: 0x30920
-  __AUTH_CONST.__objc_intobj: 0x438
+  __DATA_CONST.__got: 0x1088
+  __AUTH_CONST.__const: 0x18638
+  __AUTH_CONST.__cfstring: 0x18a80
+  __AUTH_CONST.__objc_const: 0x31728
+  __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0xa68
-  __AUTH.__objc_data: 0x53c0
-  __DATA.__objc_ivar: 0x2400
-  __DATA.__data: 0x3078
-  __DATA.__bss: 0x4d0
+  __AUTH.__objc_data: 0x5640
+  __DATA.__objc_ivar: 0x24a8
+  __DATA.__data: 0x3198
+  __DATA.__bss: 0x540
   __DATA.__common: 0xb88
   __DATA_DIRTY.__objc_data: 0x33e0
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10003
-  Symbols:   21094
-  CStrings:  5387
+  Functions: 10164
+  Symbols:   21444
+  CStrings:  5496
 
Symbols:
+ +[ICCloudAPNSChannelPushMessage ISO8601TimestampFromDate:]
+ +[ICCloudAPNSChannelPushMessage dateFromISO8601Timestamp:]
+ +[ICCloudAPNSChannelPushMessage messageWithAPSIncomingMessage:]
+ +[ICCloudAPNSChannelPushMessage supportsSecureCoding]
+ +[ICCloudAPNSChannelRegistrationConfiguration allLibraryAlbumsConfiguration]
+ +[ICCloudChannelRegistrationAvailability sharedInstance]
+ +[ICCloudClientAPNSChannelManager _exportedInterface]
+ +[ICCloudClientAPNSChannelManager _remoteObjectInterface]
+ +[ICCloudClientAPNSChannelManager sharedInstance]
+ +[ICCloudEntityUpdate cancelledUpdateWithError:]
+ +[ICCloudEntityUpdate pushReceivedUpdateWithMessage:]
+ +[ICCloudEntityUpdate resubscribedUpdateWithChannelIDs:reason:]
+ +[ICCloudEntityUpdate unsubscribedUpdateWithChannelIDs:reason:]
+ +[ICCloudEntityUpdateRegistrationToken _mintedToken]
+ +[_ICCloudAPNSChannelRegistrationState supportsSecureCoding]
+ -[ICCloudAPNSChannelPushMessage .cxx_destruct]
+ -[ICCloudAPNSChannelPushMessage channelID]
+ -[ICCloudAPNSChannelPushMessage contentType]
+ -[ICCloudAPNSChannelPushMessage copyWithZone:]
+ -[ICCloudAPNSChannelPushMessage description]
+ -[ICCloudAPNSChannelPushMessage encodeWithCoder:]
+ -[ICCloudAPNSChannelPushMessage goLiveDate]
+ -[ICCloudAPNSChannelPushMessage initWithChannelID:contentType:storeID:storefront:goLiveDate:relevanceBitmask:receivedDate:]
+ -[ICCloudAPNSChannelPushMessage initWithCoder:]
+ -[ICCloudAPNSChannelPushMessage isRelevantForCatalogEntity]
+ -[ICCloudAPNSChannelPushMessage isRelevantForLibraryEntity]
+ -[ICCloudAPNSChannelPushMessage receivedDate]
+ -[ICCloudAPNSChannelPushMessage relevanceBitmask]
+ -[ICCloudAPNSChannelPushMessage storeID]
+ -[ICCloudAPNSChannelPushMessage storefront]
+ -[ICCloudAPNSChannelRegistrationConfiguration .cxx_destruct]
+ -[ICCloudAPNSChannelRegistrationConfiguration channelID]
+ -[ICCloudAPNSChannelRegistrationConfiguration copyWithZone:]
+ -[ICCloudAPNSChannelRegistrationConfiguration description]
+ -[ICCloudAPNSChannelRegistrationConfiguration entityType]
+ -[ICCloudAPNSChannelRegistrationConfiguration expectedReleaseDate]
+ -[ICCloudAPNSChannelRegistrationConfiguration initWithChannelID:entityType:storeID:reason:expectedReleaseDate:]
+ -[ICCloudAPNSChannelRegistrationConfiguration observesAllLibraryAlbums]
+ -[ICCloudAPNSChannelRegistrationConfiguration reason]
+ -[ICCloudAPNSChannelRegistrationConfiguration storeID]
+ -[ICCloudChannelRegistrationAvailability .cxx_destruct]
+ -[ICCloudChannelRegistrationAvailability _commitAvailability:source:]
+ -[ICCloudChannelRegistrationAvailability _fetchActiveUserBagAndCommit:]
+ -[ICCloudChannelRegistrationAvailability _fetchBagWithReason:]
+ -[ICCloudChannelRegistrationAvailability _handleActiveUserIdentityDidChangeNotification:]
+ -[ICCloudChannelRegistrationAvailability _handleURLBagProviderDidUpdateBagNotification:]
+ -[ICCloudChannelRegistrationAvailability _init]
+ -[ICCloudChannelRegistrationAvailability _scheduleBagFetchRetry]
+ -[ICCloudChannelRegistrationAvailability currentState]
+ -[ICCloudChannelRegistrationAvailability dealloc]
+ -[ICCloudChannelRegistrationAvailability isAvailable]
+ -[ICCloudChannelRegistrationAvailability observer]
+ -[ICCloudChannelRegistrationAvailability setObserver:]
+ -[ICCloudClient deliverTestCloudChannelPushMessageWithUserInfo:]
+ -[ICCloudClient registerForUpdatesWithConfiguration:updateHandler:completionHandler:]
+ -[ICCloudClient unregisterForUpdatesToMonitoredEntityUsingToken:]
+ -[ICCloudClient unregisterUpdatesForChannelID:reason:]
+ -[ICCloudClient updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:]
+ -[ICCloudClientAPNSChannelManager .cxx_destruct]
+ -[ICCloudClientAPNSChannelManager _buildConnectionWithListenerEndpoint:]
+ -[ICCloudClientAPNSChannelManager _dispatchObserveAllUpdate:]
+ -[ICCloudClientAPNSChannelManager _handleConnectionLoss:forConnection:]
+ -[ICCloudClientAPNSChannelManager _init]
+ -[ICCloudClientAPNSChannelManager _registerForAllLibraryAlbumUpdatesWithHandler:completionHandler:]
+ -[ICCloudClientAPNSChannelManager _sendResyncOnConnection:]
+ -[ICCloudClientAPNSChannelManager _snapshotChannelStatesForResync]
+ -[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]
+ -[ICCloudClientAPNSChannelManager _xpcConnection]
+ -[ICCloudClientAPNSChannelManager _xpcSetObservesAllLibraryAlbumChannels:]
+ -[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]
+ -[ICCloudClientAPNSChannelManager channelRegistrations:failedWithError:]
+ -[ICCloudClientAPNSChannelManager channelRegistrationsDisabled:]
+ -[ICCloudClientAPNSChannelManager cloudChannelSubscriptionsDidBecomeDisabled:]
+ -[ICCloudClientAPNSChannelManager cloudChannelSubscriptionsDidBecomeEnabled:]
+ -[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]
+ -[ICCloudClientAPNSChannelManager monitoredChannels:wereResubscribedForReason:]
+ -[ICCloudClientAPNSChannelManager monitoredChannels:wereUnsubscribedForReason:]
+ -[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]
+ -[ICCloudClientAPNSChannelManager registerForUpdatesWithConfiguration:updateHandler:completionHandler:]
+ -[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]
+ -[ICCloudClientAPNSChannelManager unregisterUpdatesForTokens:]
+ -[ICCloudEntityUpdate .cxx_destruct]
+ -[ICCloudEntityUpdate channelIDs]
+ -[ICCloudEntityUpdate copyWithZone:]
+ -[ICCloudEntityUpdate description]
+ -[ICCloudEntityUpdate error]
+ -[ICCloudEntityUpdate initWithType:pushMessage:error:channelIDs:unsubscribeReason:resubscribeReason:]
+ -[ICCloudEntityUpdate pushMessage]
+ -[ICCloudEntityUpdate resubscribeReason]
+ -[ICCloudEntityUpdate type]
+ -[ICCloudEntityUpdate unsubscribeReason]
+ -[ICCloudEntityUpdateRegistrationToken .cxx_destruct]
+ -[ICCloudEntityUpdateRegistrationToken _initInternal]
+ -[ICCloudEntityUpdateRegistrationToken copyWithZone:]
+ -[ICCloudEntityUpdateRegistrationToken description]
+ -[ICCloudEntityUpdateRegistrationToken hash]
+ -[ICCloudEntityUpdateRegistrationToken isEqual:]
+ -[ICMusicContentKeySession _notifyRenewalWaitersIfFinished]
+ -[ICURLBag musicChannelSubscriptionsFetchWindowEndSeconds]
+ -[ICURLBag musicChannelSubscriptionsFetchWindowStartSeconds]
+ -[_ICCloudAPNSChannelRegistrationState .cxx_destruct]
+ -[_ICCloudAPNSChannelRegistrationState channelID]
+ -[_ICCloudAPNSChannelRegistrationState copyWithZone:]
+ -[_ICCloudAPNSChannelRegistrationState description]
+ -[_ICCloudAPNSChannelRegistrationState encodeWithCoder:]
+ -[_ICCloudAPNSChannelRegistrationState entityType]
+ -[_ICCloudAPNSChannelRegistrationState expectedReleaseDate]
+ -[_ICCloudAPNSChannelRegistrationState initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:]
+ -[_ICCloudAPNSChannelRegistrationState initWithCoder:]
+ -[_ICCloudAPNSChannelRegistrationState reasons]
+ -[_ICCloudAPNSChannelRegistrationState storeID]
+ -[_ICCloudUpdateRegistration .cxx_destruct]
+ -[_ICCloudUpdateRegistration configuration]
+ -[_ICCloudUpdateRegistration handler]
+ -[_ICCloudUpdateRegistration initWithConfiguration:handler:]
+ GCC_except_table1021
+ GCC_except_table1029
+ GCC_except_table1117
+ GCC_except_table1195
+ GCC_except_table1199
+ GCC_except_table1201
+ GCC_except_table1203
+ GCC_except_table1275
+ GCC_except_table1370
+ GCC_except_table1569
+ GCC_except_table1582
+ GCC_except_table1840
+ GCC_except_table2024
+ GCC_except_table2053
+ GCC_except_table2068
+ GCC_except_table2108
+ GCC_except_table2220
+ GCC_except_table2235
+ GCC_except_table2284
+ GCC_except_table2286
+ GCC_except_table2292
+ GCC_except_table2299
+ GCC_except_table2327
+ GCC_except_table2342
+ GCC_except_table2347
+ GCC_except_table2349
+ GCC_except_table2354
+ GCC_except_table2357
+ GCC_except_table2370
+ GCC_except_table2447
+ GCC_except_table2456
+ GCC_except_table2459
+ GCC_except_table2462
+ GCC_except_table2465
+ GCC_except_table247
+ GCC_except_table2478
+ GCC_except_table2480
+ GCC_except_table2497
+ GCC_except_table250
+ GCC_except_table2536
+ GCC_except_table2567
+ GCC_except_table2569
+ GCC_except_table2571
+ GCC_except_table2573
+ GCC_except_table265
+ GCC_except_table2923
+ GCC_except_table2968
+ GCC_except_table3115
+ GCC_except_table3132
+ GCC_except_table3142
+ GCC_except_table3166
+ GCC_except_table3176
+ GCC_except_table3274
+ GCC_except_table3553
+ GCC_except_table3557
+ GCC_except_table3560
+ GCC_except_table3575
+ GCC_except_table3586
+ GCC_except_table3605
+ GCC_except_table3645
+ GCC_except_table3659
+ GCC_except_table3772
+ GCC_except_table3932
+ GCC_except_table4097
+ GCC_except_table4139
+ GCC_except_table4239
+ GCC_except_table4247
+ GCC_except_table4249
+ GCC_except_table4251
+ GCC_except_table4253
+ GCC_except_table4255
+ GCC_except_table4259
+ GCC_except_table4266
+ GCC_except_table4270
+ GCC_except_table4285
+ GCC_except_table4288
+ GCC_except_table4467
+ GCC_except_table4519
+ GCC_except_table4523
+ GCC_except_table4531
+ GCC_except_table4595
+ GCC_except_table4637
+ GCC_except_table4643
+ GCC_except_table467
+ GCC_except_table4710
+ GCC_except_table472
+ GCC_except_table4787
+ GCC_except_table4875
+ GCC_except_table4958
+ GCC_except_table5026
+ GCC_except_table5107
+ GCC_except_table5267
+ GCC_except_table5524
+ GCC_except_table5629
+ GCC_except_table5677
+ GCC_except_table5701
+ GCC_except_table5742
+ GCC_except_table5743
+ GCC_except_table5816
+ GCC_except_table5834
+ GCC_except_table6094
+ GCC_except_table6101
+ GCC_except_table6109
+ GCC_except_table6120
+ GCC_except_table6121
+ GCC_except_table6123
+ GCC_except_table6124
+ GCC_except_table6129
+ GCC_except_table6134
+ GCC_except_table6139
+ GCC_except_table6150
+ GCC_except_table6165
+ GCC_except_table6167
+ GCC_except_table6173
+ GCC_except_table6182
+ GCC_except_table6191
+ GCC_except_table6225
+ GCC_except_table6257
+ GCC_except_table6270
+ GCC_except_table6277
+ GCC_except_table6278
+ GCC_except_table6355
+ GCC_except_table6378
+ GCC_except_table6383
+ GCC_except_table6389
+ GCC_except_table6392
+ GCC_except_table6395
+ GCC_except_table6398
+ GCC_except_table6401
+ GCC_except_table6404
+ GCC_except_table6407
+ GCC_except_table6410
+ GCC_except_table6413
+ GCC_except_table6416
+ GCC_except_table6419
+ GCC_except_table6520
+ GCC_except_table6734
+ GCC_except_table6741
+ GCC_except_table6915
+ GCC_except_table6919
+ GCC_except_table6921
+ GCC_except_table6948
+ GCC_except_table6994
+ GCC_except_table7167
+ GCC_except_table7299
+ GCC_except_table7419
+ GCC_except_table7431
+ GCC_except_table7454
+ GCC_except_table7532
+ GCC_except_table754
+ GCC_except_table7547
+ GCC_except_table7570
+ GCC_except_table7581
+ GCC_except_table7625
+ GCC_except_table7626
+ GCC_except_table7627
+ GCC_except_table7628
+ GCC_except_table7629
+ GCC_except_table766
+ GCC_except_table7688
+ GCC_except_table7740
+ GCC_except_table7743
+ GCC_except_table7752
+ GCC_except_table7759
+ GCC_except_table7806
+ GCC_except_table7896
+ GCC_except_table7929
+ GCC_except_table7987
+ GCC_except_table7988
+ GCC_except_table8001
+ GCC_except_table808
+ GCC_except_table8423
+ GCC_except_table8427
+ GCC_except_table8431
+ GCC_except_table8453
+ GCC_except_table8460
+ GCC_except_table8471
+ GCC_except_table8476
+ GCC_except_table8511
+ GCC_except_table8514
+ GCC_except_table8585
+ GCC_except_table8630
+ GCC_except_table8678
+ GCC_except_table8707
+ GCC_except_table8712
+ GCC_except_table8714
+ GCC_except_table8716
+ GCC_except_table8748
+ GCC_except_table8880
+ GCC_except_table8888
+ GCC_except_table8893
+ GCC_except_table8908
+ GCC_except_table8916
+ GCC_except_table8960
+ GCC_except_table9109
+ GCC_except_table9113
+ GCC_except_table9115
+ GCC_except_table9153
+ GCC_except_table9156
+ GCC_except_table9163
+ GCC_except_table9166
+ GCC_except_table920
+ GCC_except_table929
+ GCC_except_table9407
+ GCC_except_table9417
+ GCC_except_table9475
+ GCC_except_table9562
+ GCC_except_table9567
+ GCC_except_table9807
+ _ICCloudChannelRegistrationAvailabilityDidChangeNotification
+ _ICCloudChannelRegistrationAvailabilityKey
+ _ICCloudChannelRegistrationIsAvailableForBag
+ _ICCloudEntityUpdateTypeGetName
+ _ICCloudMonitoredChannelResubscribeReasonGetName
+ _ICCloudMonitoredChannelUnsubscribeReasonGetName
+ _ICCloudMonitoredEntityTypeGetName
+ _ICURLBagKeyCloudChannelRegistrationConfiguration
+ _ICURLBagKeyCloudChannelRegistrationEnabled
+ _ICURLBagKeyCloudChannelRegistrationFetchOffsetEndSeconds
+ _ICURLBagKeyCloudChannelRegistrationFetchOffsetStartSeconds
+ _OBJC_CLASS_$_ICCloudAPNSChannelPushMessage
+ _OBJC_CLASS_$_ICCloudAPNSChannelRegistrationConfiguration
+ _OBJC_CLASS_$_ICCloudChannelRegistrationAvailability
+ _OBJC_CLASS_$_ICCloudClientAPNSChannelManager
+ _OBJC_CLASS_$_ICCloudEntityUpdate
+ _OBJC_CLASS_$_ICCloudEntityUpdateRegistrationToken
+ _OBJC_CLASS_$__ICCloudAPNSChannelRegistrationState
+ _OBJC_CLASS_$__ICCloudUpdateRegistration
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._channelID
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._contentType
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._goLiveDate
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._receivedDate
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._relevanceBitmask
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._storeID
+ _OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._storefront
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._channelID
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._entityType
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._expectedReleaseDate
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._observesAllLibraryAlbums
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._reason
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._storeID
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._fetchInFlight
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._hasCommittedOnce
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._lock
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._needsReEvaluation
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._observer
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._pendingReEvaluationReason
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._state
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._connectionQueue
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._lastSetupCompletedResyncRequest
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._libraryAlbumObserverTokens
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._listenerEndpointProvider
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._lock
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._registrationsByToken
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._tokensByChannelAndReason
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._xpcConnection
+ _OBJC_IVAR_$_ICCloudEntityUpdate._channelIDs
+ _OBJC_IVAR_$_ICCloudEntityUpdate._error
+ _OBJC_IVAR_$_ICCloudEntityUpdate._pushMessage
+ _OBJC_IVAR_$_ICCloudEntityUpdate._resubscribeReason
+ _OBJC_IVAR_$_ICCloudEntityUpdate._type
+ _OBJC_IVAR_$_ICCloudEntityUpdate._unsubscribeReason
+ _OBJC_IVAR_$_ICCloudEntityUpdateRegistrationToken._uuid
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._channelID
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._entityType
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._expectedReleaseDate
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._reasons
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._storeID
+ _OBJC_IVAR_$__ICCloudUpdateRegistration._configuration
+ _OBJC_IVAR_$__ICCloudUpdateRegistration._handler
+ _OBJC_METACLASS_$_ICCloudAPNSChannelPushMessage
+ _OBJC_METACLASS_$_ICCloudAPNSChannelRegistrationConfiguration
+ _OBJC_METACLASS_$_ICCloudChannelRegistrationAvailability
+ _OBJC_METACLASS_$_ICCloudClientAPNSChannelManager
+ _OBJC_METACLASS_$_ICCloudEntityUpdate
+ _OBJC_METACLASS_$_ICCloudEntityUpdateRegistrationToken
+ _OBJC_METACLASS_$__ICCloudAPNSChannelRegistrationState
+ _OBJC_METACLASS_$__ICCloudUpdateRegistration
+ __ContentTypeForPayloadValue.__contentTypeDict
+ __ContentTypeForPayloadValue.onceToken
+ __ISO8601DateFormatter
+ __ISO8601DateFormatter.sFormatter
+ __ISO8601DateFormatter.sOnceToken
+ __OBJC_$_CLASS_METHODS_ICCloudAPNSChannelPushMessage
+ __OBJC_$_CLASS_METHODS_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_$_CLASS_METHODS_ICCloudChannelRegistrationAvailability
+ __OBJC_$_CLASS_METHODS_ICCloudClientAPNSChannelManager
+ __OBJC_$_CLASS_METHODS_ICCloudEntityUpdate
+ __OBJC_$_CLASS_METHODS_ICCloudEntityUpdateRegistrationToken
+ __OBJC_$_CLASS_METHODS__ICCloudAPNSChannelRegistrationState
+ __OBJC_$_CLASS_PROP_LIST_ICCloudAPNSChannelPushMessage
+ __OBJC_$_CLASS_PROP_LIST__ICCloudAPNSChannelRegistrationState
+ __OBJC_$_INSTANCE_METHODS_ICCloudAPNSChannelPushMessage
+ __OBJC_$_INSTANCE_METHODS_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_$_INSTANCE_METHODS_ICCloudChannelRegistrationAvailability
+ __OBJC_$_INSTANCE_METHODS_ICCloudClientAPNSChannelManager
+ __OBJC_$_INSTANCE_METHODS_ICCloudEntityUpdate
+ __OBJC_$_INSTANCE_METHODS_ICCloudEntityUpdateRegistrationToken
+ __OBJC_$_INSTANCE_METHODS__ICCloudAPNSChannelRegistrationState
+ __OBJC_$_INSTANCE_METHODS__ICCloudUpdateRegistration
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudAPNSChannelPushMessage
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudChannelRegistrationAvailability
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudClientAPNSChannelManager
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudEntityUpdate
+ __OBJC_$_INSTANCE_VARIABLES_ICCloudEntityUpdateRegistrationToken
+ __OBJC_$_INSTANCE_VARIABLES__ICCloudAPNSChannelRegistrationState
+ __OBJC_$_INSTANCE_VARIABLES__ICCloudUpdateRegistration
+ __OBJC_$_PROP_LIST_ICCloudAPNSChannelPushMessage
+ __OBJC_$_PROP_LIST_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_$_PROP_LIST_ICCloudChannelRegistrationAvailability
+ __OBJC_$_PROP_LIST_ICCloudClientAPNSChannelManager
+ __OBJC_$_PROP_LIST_ICCloudEntityUpdate
+ __OBJC_$_PROP_LIST__ICCloudAPNSChannelRegistrationState
+ __OBJC_$_PROP_LIST__ICCloudUpdateRegistration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICCloudChannelRegistrationAvailabilityObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICCloudClientAPNSChannelDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICCloudServerAPNSChannelProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICCloudChannelRegistrationAvailabilityObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICCloudClientAPNSChannelDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICCloudServerAPNSChannelProtocol
+ __OBJC_$_PROTOCOL_REFS_ICCloudChannelRegistrationAvailabilityObserver
+ __OBJC_$_PROTOCOL_REFS_ICCloudClientAPNSChannelDelegate
+ __OBJC_$_PROTOCOL_REFS_ICCloudServerAPNSChannelProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ICCloudAPNSChannelPushMessage
+ __OBJC_CLASS_PROTOCOLS_$_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_ICCloudClientAPNSChannelManager
+ __OBJC_CLASS_PROTOCOLS_$_ICCloudEntityUpdate
+ __OBJC_CLASS_PROTOCOLS_$_ICCloudEntityUpdateRegistrationToken
+ __OBJC_CLASS_PROTOCOLS_$__ICCloudAPNSChannelRegistrationState
+ __OBJC_CLASS_RO_$_ICCloudAPNSChannelPushMessage
+ __OBJC_CLASS_RO_$_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_CLASS_RO_$_ICCloudChannelRegistrationAvailability
+ __OBJC_CLASS_RO_$_ICCloudClientAPNSChannelManager
+ __OBJC_CLASS_RO_$_ICCloudEntityUpdate
+ __OBJC_CLASS_RO_$_ICCloudEntityUpdateRegistrationToken
+ __OBJC_CLASS_RO_$__ICCloudAPNSChannelRegistrationState
+ __OBJC_CLASS_RO_$__ICCloudUpdateRegistration
+ __OBJC_LABEL_PROTOCOL_$_ICCloudChannelRegistrationAvailabilityObserver
+ __OBJC_LABEL_PROTOCOL_$_ICCloudClientAPNSChannelDelegate
+ __OBJC_LABEL_PROTOCOL_$_ICCloudServerAPNSChannelProtocol
+ __OBJC_METACLASS_RO_$_ICCloudAPNSChannelPushMessage
+ __OBJC_METACLASS_RO_$_ICCloudAPNSChannelRegistrationConfiguration
+ __OBJC_METACLASS_RO_$_ICCloudChannelRegistrationAvailability
+ __OBJC_METACLASS_RO_$_ICCloudClientAPNSChannelManager
+ __OBJC_METACLASS_RO_$_ICCloudEntityUpdate
+ __OBJC_METACLASS_RO_$_ICCloudEntityUpdateRegistrationToken
+ __OBJC_METACLASS_RO_$__ICCloudAPNSChannelRegistrationState
+ __OBJC_METACLASS_RO_$__ICCloudUpdateRegistration
+ __OBJC_PROTOCOL_$_ICCloudChannelRegistrationAvailabilityObserver
+ __OBJC_PROTOCOL_$_ICCloudClientAPNSChannelDelegate
+ __OBJC_PROTOCOL_$_ICCloudServerAPNSChannelProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ICCloudClientAPNSChannelDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_ICCloudServerAPNSChannelProtocol
+ ___103-[ICCloudClientAPNSChannelManager registerForUpdatesWithConfiguration:updateHandler:completionHandler:]_block_invoke
+ ___49+[ICCloudClientAPNSChannelManager sharedInstance]_block_invoke
+ ___49-[ICCloudClientAPNSChannelManager _xpcConnection]_block_invoke
+ ___53+[ICCloudClientAPNSChannelManager _exportedInterface]_block_invoke
+ ___56+[ICCloudChannelRegistrationAvailability sharedInstance]_block_invoke
+ ___57+[ICCloudClientAPNSChannelManager _remoteObjectInterface]_block_invoke
+ ___59-[ICCloudClientAPNSChannelManager _sendResyncOnConnection:]_block_invoke
+ ___59-[ICMusicContentKeySession _notifyRenewalWaitersIfFinished]_block_invoke
+ ___61-[ICCloudClientAPNSChannelManager _dispatchObserveAllUpdate:]_block_invoke
+ ___62-[ICCloudClientAPNSChannelManager unregisterUpdatesForTokens:]_block_invoke
+ ___64-[ICCloudChannelRegistrationAvailability _scheduleBagFetchRetry]_block_invoke
+ ___64-[ICCloudClient deliverTestCloudChannelPushMessageWithUserInfo:]_block_invoke
+ ___64-[ICCloudClientAPNSChannelManager channelRegistrationsDisabled:]_block_invoke
+ ___66-[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]_block_invoke
+ ___71-[ICCloudChannelRegistrationAvailability _fetchActiveUserBagAndCommit:]_block_invoke
+ ___71-[ICCloudClientAPNSChannelManager _handleConnectionLoss:forConnection:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager _buildConnectionWithListenerEndpoint:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager _buildConnectionWithListenerEndpoint:]_block_invoke_2
+ ___72-[ICCloudClientAPNSChannelManager channelRegistrations:failedWithError:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]_block_invoke
+ ___73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
+ ___74-[ICCloudClientAPNSChannelManager _xpcSetObservesAllLibraryAlbumChannels:]_block_invoke
+ ___76+[ICCloudAPNSChannelRegistrationConfiguration allLibraryAlbumsConfiguration]_block_invoke
+ ___83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke
+ ___83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke_2
+ ___88-[ICCloudClient updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:]_block_invoke
+ ____ContentTypeForPayloadValue_block_invoke
+ ____ISO8601DateFormatter_block_invoke
+ ___block_descriptor_48_e8_32s_e30_v24?0"ICURLBag"8"NSError"16ls32l8
+ ___block_descriptor_57_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ __exportedInterface.sExportedInterface
+ __exportedInterface.sOnceToken
+ __remoteObjectInterface.sOnceToken
+ __remoteObjectInterface.sRemoteInterface
+ _allLibraryAlbumsConfiguration.sConfiguration
+ _allLibraryAlbumsConfiguration.sOnceToken
+ _objc_msgSend$_buildConnectionWithListenerEndpoint:
+ _objc_msgSend$_commitAvailability:source:
+ _objc_msgSend$_dispatchObserveAllUpdate:
+ _objc_msgSend$_exportedInterface
+ _objc_msgSend$_fetchActiveUserBagAndCommit:
+ _objc_msgSend$_fetchBagWithReason:
+ _objc_msgSend$_handleConnectionLoss:forConnection:
+ _objc_msgSend$_initInternal
+ _objc_msgSend$_mintedToken
+ _objc_msgSend$_notifyRenewalWaitersIfFinished
+ _objc_msgSend$_registerForAllLibraryAlbumUpdatesWithHandler:completionHandler:
+ _objc_msgSend$_scheduleBagFetchRetry
+ _objc_msgSend$_sendResyncOnConnection:
+ _objc_msgSend$_snapshotChannelStatesForResync
+ _objc_msgSend$_tearDownAllRegistrationsWithError:notifyDaemon:
+ _objc_msgSend$_xpcSetObservesAllLibraryAlbumChannels:
+ _objc_msgSend$_xpcUpdateReasonsWithState:completion:
+ _objc_msgSend$allLibraryAlbumsConfiguration
+ _objc_msgSend$anyObject
+ _objc_msgSend$cancelledUpdateWithError:
+ _objc_msgSend$channelID
+ _objc_msgSend$cloudChannelSubscriptionsDidBecomeDisabled:
+ _objc_msgSend$cloudChannelSubscriptionsDidBecomeEnabled:
+ _objc_msgSend$dateFromISO8601Timestamp:
+ _objc_msgSend$deliverTestCloudChannelPushMessageWithUserInfo:completion:
+ _objc_msgSend$entityType
+ _objc_msgSend$expectedReleaseDate
+ _objc_msgSend$handleCloudServerSetupCompleted
+ _objc_msgSend$handler
+ _objc_msgSend$initWithChannelID:contentType:storeID:storefront:goLiveDate:relevanceBitmask:receivedDate:
+ _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:
+ _objc_msgSend$initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:
+ _objc_msgSend$initWithConfiguration:handler:
+ _objc_msgSend$initWithType:pushMessage:error:channelIDs:unsubscribeReason:resubscribeReason:
+ _objc_msgSend$isAvailable
+ _objc_msgSend$observer
+ _objc_msgSend$observesAllLibraryAlbums
+ _objc_msgSend$pushReceivedUpdateWithMessage:
+ _objc_msgSend$registerForUpdatesWithConfiguration:updateHandler:completionHandler:
+ _objc_msgSend$resubscribedUpdateWithChannelIDs:reason:
+ _objc_msgSend$resyncWithChannelStates:completion:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setObservesAllLibraryAlbumChannels:completion:
+ _objc_msgSend$unregisterUpdatesForChannelID:reason:
+ _objc_msgSend$unregisterUpdatesForTokens:
+ _objc_msgSend$unsubscribedUpdateWithChannelIDs:reason:
+ _objc_msgSend$updateMonitoredReasonsWithChannelState:completion:
+ _objc_msgSend$updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:completion:
+ _sharedInstance.sOnceToken
+ _sharedInstance.sSharedInstance
- GCC_except_table1057
- GCC_except_table1083
- GCC_except_table1135
- GCC_except_table1139
- GCC_except_table1141
- GCC_except_table1215
- GCC_except_table1301
- GCC_except_table1500
- GCC_except_table1513
- GCC_except_table1771
- GCC_except_table1955
- GCC_except_table1984
- GCC_except_table1999
- GCC_except_table2039
- GCC_except_table2151
- GCC_except_table2166
- GCC_except_table2215
- GCC_except_table2217
- GCC_except_table2223
- GCC_except_table2230
- GCC_except_table2258
- GCC_except_table2273
- GCC_except_table2278
- GCC_except_table2280
- GCC_except_table2285
- GCC_except_table2288
- GCC_except_table2301
- GCC_except_table2378
- GCC_except_table2387
- GCC_except_table2390
- GCC_except_table2393
- GCC_except_table2396
- GCC_except_table2398
- GCC_except_table2409
- GCC_except_table2411
- GCC_except_table2428
- GCC_except_table2498
- GCC_except_table2500
- GCC_except_table2502
- GCC_except_table2504
- GCC_except_table2854
- GCC_except_table2899
- GCC_except_table3046
- GCC_except_table3063
- GCC_except_table3073
- GCC_except_table3097
- GCC_except_table3107
- GCC_except_table3205
- GCC_except_table3484
- GCC_except_table3488
- GCC_except_table3491
- GCC_except_table3506
- GCC_except_table3517
- GCC_except_table3536
- GCC_except_table3576
- GCC_except_table3590
- GCC_except_table3703
- GCC_except_table3863
- GCC_except_table4028
- GCC_except_table407
- GCC_except_table4070
- GCC_except_table412
- GCC_except_table4170
- GCC_except_table4178
- GCC_except_table4180
- GCC_except_table4182
- GCC_except_table4184
- GCC_except_table4186
- GCC_except_table4190
- GCC_except_table4197
- GCC_except_table4201
- GCC_except_table4216
- GCC_except_table4219
- GCC_except_table4398
- GCC_except_table4450
- GCC_except_table4454
- GCC_except_table4457
- GCC_except_table4462
- GCC_except_table4568
- GCC_except_table4572
- GCC_except_table4574
- GCC_except_table4718
- GCC_except_table4806
- GCC_except_table4889
- GCC_except_table4957
- GCC_except_table5038
- GCC_except_table5198
- GCC_except_table5455
- GCC_except_table5560
- GCC_except_table5608
- GCC_except_table5632
- GCC_except_table5673
- GCC_except_table5674
- GCC_except_table5747
- GCC_except_table5765
- GCC_except_table6025
- GCC_except_table6032
- GCC_except_table6040
- GCC_except_table6051
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6054
- GCC_except_table6055
- GCC_except_table6060
- GCC_except_table6065
- GCC_except_table6070
- GCC_except_table6081
- GCC_except_table6096
- GCC_except_table6098
- GCC_except_table6104
- GCC_except_table6113
- GCC_except_table6156
- GCC_except_table6188
- GCC_except_table6201
- GCC_except_table6208
- GCC_except_table6209
- GCC_except_table6269
- GCC_except_table6272
- GCC_except_table6286
- GCC_except_table6309
- GCC_except_table6314
- GCC_except_table6320
- GCC_except_table6323
- GCC_except_table6326
- GCC_except_table6329
- GCC_except_table6332
- GCC_except_table6335
- GCC_except_table6344
- GCC_except_table6347
- GCC_except_table6350
- GCC_except_table6451
- GCC_except_table6665
- GCC_except_table6672
- GCC_except_table6846
- GCC_except_table6850
- GCC_except_table6852
- GCC_except_table6879
- GCC_except_table6925
- GCC_except_table694
- GCC_except_table706
- GCC_except_table7098
- GCC_except_table7230
- GCC_except_table7350
- GCC_except_table7361
- GCC_except_table7384
- GCC_except_table7462
- GCC_except_table7477
- GCC_except_table748
- GCC_except_table7500
- GCC_except_table7511
- GCC_except_table7555
- GCC_except_table7556
- GCC_except_table7557
- GCC_except_table7558
- GCC_except_table7559
- GCC_except_table7600
- GCC_except_table7618
- GCC_except_table7673
- GCC_except_table7682
- GCC_except_table7689
- GCC_except_table7736
- GCC_except_table7755
- GCC_except_table7788
- GCC_except_table7846
- GCC_except_table7847
- GCC_except_table7860
- GCC_except_table8280
- GCC_except_table8284
- GCC_except_table8288
- GCC_except_table8310
- GCC_except_table8317
- GCC_except_table8328
- GCC_except_table8333
- GCC_except_table8368
- GCC_except_table8371
- GCC_except_table8442
- GCC_except_table8487
- GCC_except_table8535
- GCC_except_table8564
- GCC_except_table8569
- GCC_except_table8571
- GCC_except_table8573
- GCC_except_table860
- GCC_except_table8605
- GCC_except_table869
- GCC_except_table8737
- GCC_except_table8745
- GCC_except_table8750
- GCC_except_table8765
- GCC_except_table8773
- GCC_except_table8817
- GCC_except_table8966
- GCC_except_table8970
- GCC_except_table8972
- GCC_except_table9010
- GCC_except_table9013
- GCC_except_table9020
- GCC_except_table9023
- GCC_except_table9246
- GCC_except_table9256
- GCC_except_table9314
- GCC_except_table9401
- GCC_except_table9406
- GCC_except_table961
- GCC_except_table9646
- GCC_except_table969
- ___68-[ICMusicContentKeySession _finishProcessingKeyWithIdentifier:item:]_block_invoke
CStrings:
+ "<%@ %p channelID=%@ contentType=%ld _storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ observesAllLibraryAlbums=%d>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reasons=%@ expectedReleaseDate=%@>"
+ "<%@ %p type=%@ pushMessage=%@ error=%@ channelIDs=%@ unsubscribeReason=%@ resubscribeReason=%@>"
+ "<%@: %p>"
+ "ALBUM"
+ "APNSChannel"
+ "Budget"
+ "Cannot unregister updates: token is nil."
+ "ChannelsResubscribed"
+ "ChannelsUnsubscribed"
+ "Daemon rejected test cloud channel push delivery: %{public}@"
+ "Daemon rejected test library channel registration update: %{public}@"
+ "Failed to deliver test cloud channel push message with error: %{public}@"
+ "Failed to update test library channel registrations with error: %{public}@"
+ "FeatureNotAvailable"
+ "ICCloudAPNSChannelPushMessage - not decoding push; missing channelID. payload=%{public}@"
+ "ICCloudAPNSChannelPushMessage - not decoding push; missing storeID. payload=%{public}@"
+ "ICCloudAPNSChannelPushMessage - not decoding push; userInfo is not a dictionary. apsMessage=%{public}@"
+ "ICCloudAPNSChannelPushMessage - unknown contentType=%{public}@ channelID=%{public}@"
+ "ICCloudChannelRegistrationAvailability - availability changed old=%{public}@ new=%{public}@ source=%{public}@"
+ "ICCloudChannelRegistrationAvailability - availability unchanged state=%{public}@ source=%{public}@"
+ "ICCloudChannelRegistrationAvailability - fetching active-user bag reason=%{public}@"
+ "ICCloudChannelRegistrationAvailability - ignoring bag update for non-active identity."
+ "ICCloudChannelRegistrationAvailability - not able to fetch bag err=%{public}@"
+ "ICCloudChannelRegistrationAvailability - not dispatching transition; no observer wired newState=%{public}@"
+ "ICCloudChannelRegistrationAvailability - not fetching bag; no active identity source=%{public}@"
+ "ICCloudChannelRegistrationAvailability - scheduling bag fetch retry delay=%.0fs"
+ "ICCloudChannelRegistrationAvailabilityDidChangeNotification"
+ "ICCloudChannelRegistrationAvailabilityKey"
+ "ICCloudClientAPNSChannelManager - creating XPC connection connection=%{public}@"
+ "ICCloudClientAPNSChannelManager - creating XPC connection."
+ "ICCloudClientAPNSChannelManager - dispatching observe-all update=%{public}@ handlerCount=%lu"
+ "ICCloudClientAPNSChannelManager - dispatching update handlerCount=%lu channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - feature disabled daemonChannels=%{public}@ localOnly=%{public}@ handlers=%lu"
+ "ICCloudClientAPNSChannelManager - handling XPC connection loss reason=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to add reason on daemon; committing locally channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to obtain listener endpoint err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to re-arm observe-all err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to re-arm observe-all; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to resync err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send resync; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send setObservesAllLibraryAlbumChannels; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send updateMonitoredReasons; proxy err channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to update daemon channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons during tear-down channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons for race-repair channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not delivering push; feature is unavailable. channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not dispatching observe-all update; feature is unavailable."
+ "ICCloudClientAPNSChannelManager - not dispatching update; no handlers on channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not reconnecting after server setup; feature is unavailable."
+ "ICCloudClientAPNSChannelManager - not registering observe-all; feature is unavailable."
+ "ICCloudClientAPNSChannelManager - not registering observe-all; invalid arguments updateHandler=%p completionHandler=%p"
+ "ICCloudClientAPNSChannelManager - not registering; daemon update failed channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not registering; feature is unavailable. channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - not registering; invalid arguments configuration=%{public}@ updateHandler=%p, completionHandler=%p"
+ "ICCloudClientAPNSChannelManager - not resyncing after server setup; debounced."
+ "ICCloudClientAPNSChannelManager - not resyncing after server setup; no registrations."
+ "ICCloudClientAPNSChannelManager - not sending daemon updates; nothing to unregister."
+ "ICCloudClientAPNSChannelManager - not sending setObservesAllLibraryAlbumChannels=%{BOOL}u; no XPC connection."
+ "ICCloudClientAPNSChannelManager - not sending updateMonitoredReasons; no XPC connection. channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not unregistering channel; no matching tokens channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - not unregistering tokens; feature is unavailable. tokenCount=%lu"
+ "ICCloudClientAPNSChannelManager - not unregistering unknown tokens count=%lu"
+ "ICCloudClientAPNSChannelManager - not unregistering; feature is unavailable. channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - not unregistering; invalid arguments channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - per-channel cancellation channelIDs=%{public}@ handlers=%lu err=%{public}@"
+ "ICCloudClientAPNSChannelManager - rebuilding XPC connection after server setup."
+ "ICCloudClientAPNSChannelManager - received resync ack."
+ "ICCloudClientAPNSChannelManager - receiving update pushMessage=%{public}@"
+ "ICCloudClientAPNSChannelManager - registering configuration=%{public}@ token=%{public}@"
+ "ICCloudClientAPNSChannelManager - registering observe-all token=%{public}@ armDaemon=%{BOOL}u"
+ "ICCloudClientAPNSChannelManager - registering token=%{public}@ channelID=%{public}@ reason=%ld isRegisteredChannel=%{BOOL}u isRegisteredReason=%{BOOL}u"
+ "ICCloudClientAPNSChannelManager - sending resync channelCount=%lu"
+ "ICCloudClientAPNSChannelManager - sending setObservesAllLibraryAlbumChannels=%{BOOL}u"
+ "ICCloudClientAPNSChannelManager - sending updateMonitoredReasons state=%{public}@"
+ "ICCloudClientAPNSChannelManager - setObservesAllLibraryAlbumChannels failed err=%{public}@"
+ "ICCloudClientAPNSChannelManager - tearing down registrations xpcUpdates=%lu handlers=%lu notifyDaemon=%{BOOL}u err=%{public}@"
+ "ICCloudClientAPNSChannelManager - unregistering channel channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - unregistering tokens count=%lu"
+ "ICCloudClientAPNSChannelManager - unregistering tokens count=%lu channelID=%{public}@ reason=%ld"
+ "Invalid"
+ "NoLongerMonitored"
+ "PushReceived"
+ "SubscribeFailed"
+ "active-identity-change-notification"
+ "albumStoreID"
+ "apnsChannel"
+ "bag-fetch-retry"
+ "bag-update-notification"
+ "channelID"
+ "channelId"
+ "com.apple.iTunesCloud.ICCloudClientAPNSChannelManager.connectionQueue"
+ "contentType"
+ "entityType"
+ "expectedReleaseDate"
+ "fetch-end-offset-seconds"
+ "fetch-start-offset-seconds"
+ "goLiveDate"
+ "goLiveTimestamp"
+ "init"
+ "interrupted"
+ "invalidated"
+ "lazy-initialize"
+ "music-channel-subscriptions"
+ "reasons"
+ "receivedDate"
+ "relevanceBitmask"
```

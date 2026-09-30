## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud`

```diff

-4026.100.81.0.0
-  __TEXT.__text: 0x31b46c
-  __TEXT.__objc_methlist: 0x18044
+4026.140.1.0.0
+  __TEXT.__text: 0x324644
+  __TEXT.__objc_methlist: 0x18704
   __TEXT.__const: 0x272c8
   __TEXT.__dlopen_cstrs: 0x2ff
-  __TEXT.__gcc_except_tab: 0x29d8
-  __TEXT.__cstring: 0x17156
-  __TEXT.__oslogstring: 0x20552
+  __TEXT.__gcc_except_tab: 0x2a20
+  __TEXT.__cstring: 0x1759e
+  __TEXT.__oslogstring: 0x21e4c
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x66c8
+  __TEXT.__unwind_info: 0x6890
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2b58
-  __DATA_CONST.__objc_classlist: 0xd98
+  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__objc_classlist: 0xdd8
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x2d8
+  __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa1f8
-  __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xbc0
+  __DATA_CONST.__objc_selrefs: 0xa458
+  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x1028
-  __AUTH_CONST.__const: 0x17800
-  __AUTH_CONST.__cfstring: 0x18440
-  __AUTH_CONST.__objc_const: 0x30800
-  __AUTH_CONST.__objc_intobj: 0x420
+  __DATA_CONST.__got: 0x1058
+  __AUTH_CONST.__const: 0x17a90
+  __AUTH_CONST.__cfstring: 0x18900
+  __AUTH_CONST.__objc_const: 0x31610
+  __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x990
-  __AUTH.__objc_data: 0x4fb0
-  __DATA.__objc_ivar: 0x23e8
-  __DATA.__data: 0x2a58
-  __DATA.__bss: 0x3b8
+  __AUTH.__objc_data: 0x5230
+  __DATA.__objc_ivar: 0x2490
+  __DATA.__data: 0x2b78
+  __DATA.__bss: 0x428
   __DATA.__common: 0xa58
   __DATA_DIRTY.__objc_data: 0x3840
   __DATA_DIRTY.__data: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9973
-  Symbols:   21291
-  CStrings:  5322
+  Functions: 10134
+  Symbols:   21649
+  CStrings:  5431
 
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
+ GCC_except_table1070
+ GCC_except_table1080
+ GCC_except_table1168
+ GCC_except_table1195
+ GCC_except_table1247
+ GCC_except_table1251
+ GCC_except_table1253
+ GCC_except_table1255
+ GCC_except_table1327
+ GCC_except_table1422
+ GCC_except_table1621
+ GCC_except_table1634
+ GCC_except_table1892
+ GCC_except_table2076
+ GCC_except_table2105
+ GCC_except_table2120
+ GCC_except_table2166
+ GCC_except_table2278
+ GCC_except_table2294
+ GCC_except_table2343
+ GCC_except_table2345
+ GCC_except_table2351
+ GCC_except_table2358
+ GCC_except_table2386
+ GCC_except_table2401
+ GCC_except_table2406
+ GCC_except_table2408
+ GCC_except_table2413
+ GCC_except_table2416
+ GCC_except_table2429
+ GCC_except_table2525
+ GCC_except_table2565
+ GCC_except_table2596
+ GCC_except_table2598
+ GCC_except_table2600
+ GCC_except_table2602
+ GCC_except_table269
+ GCC_except_table274
+ GCC_except_table291
+ GCC_except_table2952
+ GCC_except_table3004
+ GCC_except_table3168
+ GCC_except_table3185
+ GCC_except_table3198
+ GCC_except_table3222
+ GCC_except_table3232
+ GCC_except_table3331
+ GCC_except_table3610
+ GCC_except_table3616
+ GCC_except_table3619
+ GCC_except_table3645
+ GCC_except_table3664
+ GCC_except_table3704
+ GCC_except_table3720
+ GCC_except_table3833
+ GCC_except_table3994
+ GCC_except_table4161
+ GCC_except_table4204
+ GCC_except_table4304
+ GCC_except_table4312
+ GCC_except_table4314
+ GCC_except_table4316
+ GCC_except_table4318
+ GCC_except_table4320
+ GCC_except_table4324
+ GCC_except_table4331
+ GCC_except_table4335
+ GCC_except_table4350
+ GCC_except_table4354
+ GCC_except_table4533
+ GCC_except_table4586
+ GCC_except_table4590
+ GCC_except_table4593
+ GCC_except_table4598
+ GCC_except_table4662
+ GCC_except_table4704
+ GCC_except_table4708
+ GCC_except_table4710
+ GCC_except_table4777
+ GCC_except_table4854
+ GCC_except_table496
+ GCC_except_table5016
+ GCC_except_table503
+ GCC_except_table5084
+ GCC_except_table5165
+ GCC_except_table5325
+ GCC_except_table5582
+ GCC_except_table5686
+ GCC_except_table5733
+ GCC_except_table5757
+ GCC_except_table5798
+ GCC_except_table5799
+ GCC_except_table5874
+ GCC_except_table5892
+ GCC_except_table6152
+ GCC_except_table6159
+ GCC_except_table6167
+ GCC_except_table6178
+ GCC_except_table6179
+ GCC_except_table6181
+ GCC_except_table6182
+ GCC_except_table6187
+ GCC_except_table6192
+ GCC_except_table6197
+ GCC_except_table6208
+ GCC_except_table6224
+ GCC_except_table6226
+ GCC_except_table6232
+ GCC_except_table6241
+ GCC_except_table6250
+ GCC_except_table6284
+ GCC_except_table6327
+ GCC_except_table6334
+ GCC_except_table6335
+ GCC_except_table6395
+ GCC_except_table6398
+ GCC_except_table6418
+ GCC_except_table6441
+ GCC_except_table6446
+ GCC_except_table6452
+ GCC_except_table6455
+ GCC_except_table6458
+ GCC_except_table6461
+ GCC_except_table6464
+ GCC_except_table6467
+ GCC_except_table6470
+ GCC_except_table6473
+ GCC_except_table6476
+ GCC_except_table6479
+ GCC_except_table6482
+ GCC_except_table6583
+ GCC_except_table6796
+ GCC_except_table6803
+ GCC_except_table6977
+ GCC_except_table6981
+ GCC_except_table6983
+ GCC_except_table7010
+ GCC_except_table7056
+ GCC_except_table7229
+ GCC_except_table7361
+ GCC_except_table7481
+ GCC_except_table7495
+ GCC_except_table7521
+ GCC_except_table7598
+ GCC_except_table7613
+ GCC_except_table7636
+ GCC_except_table7647
+ GCC_except_table7690
+ GCC_except_table7691
+ GCC_except_table7692
+ GCC_except_table7693
+ GCC_except_table7694
+ GCC_except_table7753
+ GCC_except_table7808
+ GCC_except_table7819
+ GCC_except_table7828
+ GCC_except_table785
+ GCC_except_table7875
+ GCC_except_table7965
+ GCC_except_table799
+ GCC_except_table7998
+ GCC_except_table8064
+ GCC_except_table8485
+ GCC_except_table8489
+ GCC_except_table8493
+ GCC_except_table851
+ GCC_except_table8515
+ GCC_except_table8522
+ GCC_except_table8535
+ GCC_except_table8540
+ GCC_except_table8575
+ GCC_except_table8578
+ GCC_except_table8649
+ GCC_except_table8694
+ GCC_except_table8742
+ GCC_except_table8771
+ GCC_except_table8776
+ GCC_except_table8778
+ GCC_except_table8780
+ GCC_except_table8813
+ GCC_except_table8945
+ GCC_except_table8953
+ GCC_except_table8958
+ GCC_except_table8973
+ GCC_except_table8981
+ GCC_except_table9025
+ GCC_except_table9176
+ GCC_except_table9180
+ GCC_except_table9182
+ GCC_except_table9220
+ GCC_except_table9223
+ GCC_except_table9230
+ GCC_except_table9233
+ GCC_except_table9474
+ GCC_except_table9484
+ GCC_except_table9542
+ GCC_except_table9629
+ GCC_except_table9634
+ GCC_except_table965
+ GCC_except_table976
+ GCC_except_table9874
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._channelID
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._contentType
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._goLiveDate
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._receivedDate
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._relevanceBitmask
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._storeID
+ OBJC_IVAR_$_ICCloudAPNSChannelPushMessage._storefront
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._channelID
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._entityType
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._expectedReleaseDate
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._observesAllLibraryAlbums
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._reason
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._storeID
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._fetchInFlight
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._hasCommittedOnce
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._lock
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._needsReEvaluation
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._observer
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._pendingReEvaluationReason
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._state
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._connectionQueue
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._lastSetupCompletedResyncRequest
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._libraryAlbumObserverTokens
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._listenerEndpointProvider
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._lock
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._registrationsByToken
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._tokensByChannelAndReason
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._xpcConnection
+ OBJC_IVAR_$_ICCloudEntityUpdate._channelIDs
+ OBJC_IVAR_$_ICCloudEntityUpdate._error
+ OBJC_IVAR_$_ICCloudEntityUpdate._pushMessage
+ OBJC_IVAR_$_ICCloudEntityUpdate._resubscribeReason
+ OBJC_IVAR_$_ICCloudEntityUpdate._type
+ OBJC_IVAR_$_ICCloudEntityUpdate._unsubscribeReason
+ OBJC_IVAR_$_ICCloudEntityUpdateRegistrationToken._uuid
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._channelID
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._entityType
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._expectedReleaseDate
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._reasons
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._storeID
+ OBJC_IVAR_$__ICCloudUpdateRegistration._configuration
+ OBJC_IVAR_$__ICCloudUpdateRegistration._handler
+ _ContentTypeForPayloadValue.__contentTypeDict
+ _ContentTypeForPayloadValue.onceToken
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
+ _ISO8601DateFormatter.sFormatter
+ _ISO8601DateFormatter.sOnceToken
+ _OBJC_CLASS_$_ICCloudAPNSChannelPushMessage
+ _OBJC_CLASS_$_ICCloudAPNSChannelRegistrationConfiguration
+ _OBJC_CLASS_$_ICCloudChannelRegistrationAvailability
+ _OBJC_CLASS_$_ICCloudClientAPNSChannelManager
+ _OBJC_CLASS_$_ICCloudEntityUpdate
+ _OBJC_CLASS_$_ICCloudEntityUpdateRegistrationToken
+ _OBJC_CLASS_$__ICCloudAPNSChannelRegistrationState
+ _OBJC_CLASS_$__ICCloudUpdateRegistration
+ _OBJC_METACLASS_$_ICCloudAPNSChannelPushMessage
+ _OBJC_METACLASS_$_ICCloudAPNSChannelRegistrationConfiguration
+ _OBJC_METACLASS_$_ICCloudChannelRegistrationAvailability
+ _OBJC_METACLASS_$_ICCloudClientAPNSChannelManager
+ _OBJC_METACLASS_$_ICCloudEntityUpdate
+ _OBJC_METACLASS_$_ICCloudEntityUpdateRegistrationToken
+ _OBJC_METACLASS_$__ICCloudAPNSChannelRegistrationState
+ _OBJC_METACLASS_$__ICCloudUpdateRegistration
+ __103-[ICCloudClientAPNSChannelManager registerForUpdatesWithConfiguration:updateHandler:completionHandler:]_block_invoke
+ __59-[ICCloudClientAPNSChannelManager _sendResyncOnConnection:]_block_invoke
+ __64-[ICCloudClient deliverTestCloudChannelPushMessageWithUserInfo:]_block_invoke
+ __66-[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]_block_invoke
+ __72-[ICCloudClientAPNSChannelManager _buildConnectionWithListenerEndpoint:]_block_invoke
+ __73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
+ __74-[ICCloudClientAPNSChannelManager _xpcSetObservesAllLibraryAlbumChannels:]_block_invoke
+ __83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke
+ __88-[ICCloudClient updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:]_block_invoke
+ __ISO8601DateFormatter
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
+ ___72-[ICCloudClientAPNSChannelManager channelRegistrations:failedWithError:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]_block_invoke
+ ___72-[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]_block_invoke
+ ___73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
+ ___74-[ICCloudClientAPNSChannelManager _xpcSetObservesAllLibraryAlbumChannels:]_block_invoke
+ ___76+[ICCloudAPNSChannelRegistrationConfiguration allLibraryAlbumsConfiguration]_block_invoke
+ ___83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke
+ ___88-[ICCloudClient updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:]_block_invoke
+ ____ContentTypeForPayloadValue_block_invoke
+ ____ISO8601DateFormatter_block_invoke
+ ___block_descriptor_48_e8_32s_e30_v24?0"ICURLBag"8"NSError"16l
+ ___block_descriptor_57_e8_32s40bs48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0l
+ _exportedInterface.sExportedInterface
+ _exportedInterface.sOnceToken
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
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$unregisterUpdatesForChannelID:reason:
+ _objc_msgSend$unregisterUpdatesForTokens:
+ _objc_msgSend$unsubscribedUpdateWithChannelIDs:reason:
+ _objc_msgSend$updateMonitoredReasonsWithChannelState:completion:
+ _objc_msgSend$updateTestLibraryChannelRegistrationsWithAddedStates:removedChannelIDs:completion:
+ _remoteObjectInterface.sOnceToken
+ _remoteObjectInterface.sRemoteInterface
+ allLibraryAlbumsConfiguration.sConfiguration
+ allLibraryAlbumsConfiguration.sOnceToken
+ sharedInstance.sOnceToken
+ sharedInstance.sSharedInstance
- GCC_except_table1003
- GCC_except_table1013
- GCC_except_table1101
- GCC_except_table1128
- GCC_except_table1180
- GCC_except_table1184
- GCC_except_table1186
- GCC_except_table1188
- GCC_except_table1260
- GCC_except_table1346
- GCC_except_table1545
- GCC_except_table1558
- GCC_except_table1816
- GCC_except_table2000
- GCC_except_table2031
- GCC_except_table2046
- GCC_except_table2094
- GCC_except_table2206
- GCC_except_table2222
- GCC_except_table2271
- GCC_except_table2273
- GCC_except_table2279
- GCC_except_table2286
- GCC_except_table2314
- GCC_except_table2329
- GCC_except_table2334
- GCC_except_table2336
- GCC_except_table2341
- GCC_except_table2344
- GCC_except_table2357
- GCC_except_table2453
- GCC_except_table2495
- GCC_except_table2526
- GCC_except_table2528
- GCC_except_table2530
- GCC_except_table2532
- GCC_except_table2882
- GCC_except_table2934
- GCC_except_table3098
- GCC_except_table3115
- GCC_except_table3128
- GCC_except_table3152
- GCC_except_table3162
- GCC_except_table3261
- GCC_except_table3540
- GCC_except_table3546
- GCC_except_table3549
- GCC_except_table3564
- GCC_except_table3575
- GCC_except_table3594
- GCC_except_table3650
- GCC_except_table3763
- GCC_except_table3924
- GCC_except_table4091
- GCC_except_table4134
- GCC_except_table4234
- GCC_except_table4242
- GCC_except_table4244
- GCC_except_table4246
- GCC_except_table4248
- GCC_except_table4250
- GCC_except_table4254
- GCC_except_table4261
- GCC_except_table4265
- GCC_except_table4280
- GCC_except_table4284
- GCC_except_table429
- GCC_except_table436
- GCC_except_table4463
- GCC_except_table4516
- GCC_except_table4520
- GCC_except_table4523
- GCC_except_table4528
- GCC_except_table4592
- GCC_except_table4634
- GCC_except_table4638
- GCC_except_table4640
- GCC_except_table4707
- GCC_except_table4784
- GCC_except_table4946
- GCC_except_table5014
- GCC_except_table5095
- GCC_except_table5255
- GCC_except_table5512
- GCC_except_table5616
- GCC_except_table5663
- GCC_except_table5687
- GCC_except_table5728
- GCC_except_table5729
- GCC_except_table5804
- GCC_except_table5822
- GCC_except_table6082
- GCC_except_table6089
- GCC_except_table6097
- GCC_except_table6108
- GCC_except_table6109
- GCC_except_table6110
- GCC_except_table6111
- GCC_except_table6112
- GCC_except_table6117
- GCC_except_table6122
- GCC_except_table6127
- GCC_except_table6138
- GCC_except_table6154
- GCC_except_table6156
- GCC_except_table6162
- GCC_except_table6171
- GCC_except_table6214
- GCC_except_table6257
- GCC_except_table6264
- GCC_except_table6265
- GCC_except_table6325
- GCC_except_table6328
- GCC_except_table6348
- GCC_except_table6371
- GCC_except_table6376
- GCC_except_table6382
- GCC_except_table6385
- GCC_except_table6388
- GCC_except_table6391
- GCC_except_table6394
- GCC_except_table6397
- GCC_except_table6400
- GCC_except_table6403
- GCC_except_table6406
- GCC_except_table6409
- GCC_except_table6412
- GCC_except_table6513
- GCC_except_table6726
- GCC_except_table6733
- GCC_except_table6907
- GCC_except_table6911
- GCC_except_table6913
- GCC_except_table6940
- GCC_except_table6986
- GCC_except_table7159
- GCC_except_table718
- GCC_except_table7291
- GCC_except_table732
- GCC_except_table7411
- GCC_except_table7424
- GCC_except_table7451
- GCC_except_table7528
- GCC_except_table7543
- GCC_except_table7566
- GCC_except_table7577
- GCC_except_table7620
- GCC_except_table7621
- GCC_except_table7622
- GCC_except_table7623
- GCC_except_table7624
- GCC_except_table7665
- GCC_except_table7683
- GCC_except_table7738
- GCC_except_table7749
- GCC_except_table7758
- GCC_except_table7824
- GCC_except_table784
- GCC_except_table7857
- GCC_except_table7923
- GCC_except_table8342
- GCC_except_table8346
- GCC_except_table8350
- GCC_except_table8372
- GCC_except_table8379
- GCC_except_table8392
- GCC_except_table8397
- GCC_except_table8432
- GCC_except_table8435
- GCC_except_table8506
- GCC_except_table8551
- GCC_except_table8599
- GCC_except_table8628
- GCC_except_table8633
- GCC_except_table8635
- GCC_except_table8637
- GCC_except_table8670
- GCC_except_table8802
- GCC_except_table8810
- GCC_except_table8815
- GCC_except_table8830
- GCC_except_table8838
- GCC_except_table8882
- GCC_except_table898
- GCC_except_table9033
- GCC_except_table9037
- GCC_except_table9039
- GCC_except_table9077
- GCC_except_table9080
- GCC_except_table9087
- GCC_except_table909
- GCC_except_table9090
- GCC_except_table9313
- GCC_except_table9323
- GCC_except_table9381
- GCC_except_table9468
- GCC_except_table9473
- GCC_except_table9713
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

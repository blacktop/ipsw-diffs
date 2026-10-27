## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud`

```diff

-4026.140.1.0.0
-  __TEXT.__text: 0x324644
-  __TEXT.__objc_methlist: 0x18704
-  __TEXT.__const: 0x272c8
+4026.240.1.0.0
+  __TEXT.__text: 0x3282dc
+  __TEXT.__objc_methlist: 0x1895c
+  __TEXT.__const: 0x272d8
   __TEXT.__dlopen_cstrs: 0x2ff
-  __TEXT.__gcc_except_tab: 0x2a20
-  __TEXT.__cstring: 0x1759e
-  __TEXT.__oslogstring: 0x21e4c
+  __TEXT.__gcc_except_tab: 0x2a58
+  __TEXT.__cstring: 0x177d0
+  __TEXT.__oslogstring: 0x22399
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x6890
+  __TEXT.__unwind_info: 0x6928
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__const: 0x2c10
   __DATA_CONST.__objc_classlist: 0xdd8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa458
+  __DATA_CONST.__objc_selrefs: 0xa590
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x1058
-  __AUTH_CONST.__const: 0x17a90
-  __AUTH_CONST.__cfstring: 0x18900
-  __AUTH_CONST.__objc_const: 0x31610
+  __DATA_CONST.__got: 0x1068
+  __AUTH_CONST.__const: 0x17b80
+  __AUTH_CONST.__cfstring: 0x18a20
+  __AUTH_CONST.__objc_const: 0x319b8
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x990
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x5230
-  __DATA.__objc_ivar: 0x2490
-  __DATA.__data: 0x2b78
-  __DATA.__bss: 0x428
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x24d0
+  __DATA.__data: 0x2aa8
+  __DATA.__bss: 0x438
   __DATA.__common: 0xa58
-  __DATA_DIRTY.__objc_data: 0x3840
-  __DATA_DIRTY.__data: 0x108
+  __DATA_DIRTY.__objc_data: 0x87f0
+  __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__bss: 0x420
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10134
-  Symbols:   21649
-  CStrings:  5431
+  Functions: 10189
+  Symbols:   21748
+  CStrings:  5457
 
Symbols:
+ +[ICCloudAPNSChannelPushMessage dateFromISO8601Timestamp:defaultFetchStartSeconds:]
+ +[ICCloudAPNSChannelPushMessage messageWithAPSIncomingMessage:defaultFetchStartSeconds:]
+ +[ICCloudEntityUpdate allUpdatesPaused]
+ +[ICCloudEntityUpdate pushReceivedUpdateWithMessages:]
+ +[ICCloudEntityUpdateRegistrationToken supportsSecureCoding]
+ +[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]
+ -[ICCloudAPNSChannelPushMessage hash]
+ -[ICCloudAPNSChannelPushMessage isEqual:]
+ -[ICCloudAPNSChannelRegistrationConfiguration initWithChannelID:entityType:storeID:reason:expectedReleaseDate:lastProcessedGoLiveTimestamp:registrationToken:]
+ -[ICCloudAPNSChannelRegistrationConfiguration lastProcessedGoLiveTimestamp]
+ -[ICCloudAPNSChannelRegistrationConfiguration registrationToken]
+ -[ICCloudChannelRegistrationAvailability _updateCloudChannelConfigurationUsingBag:source:]
+ -[ICCloudChannelRegistrationAvailability maxAllowedCloudChannelRegistrations]
+ -[ICCloudChannelRegistrationAvailability registrationFetchEndOffsetSeconds]
+ -[ICCloudChannelRegistrationAvailability registrationFetchStartOffsetSeconds]
+ -[ICCloudClientAPNSChannelManager _computeChannelStatesForResync]
+ -[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]
+ -[ICCloudClientAPNSChannelManager _dispatchUpdate:toRegistrationsForChannelIDs:]
+ -[ICCloudClientAPNSChannelManager _postCloudChannelRegistrationConfigurationChanged:]
+ -[ICCloudClientAPNSChannelManager _resumeUpdates]
+ -[ICCloudClientAPNSChannelManager _serverSetupDidComplete]
+ -[ICCloudClientAPNSChannelManager _xpcRegisterChannelState:completion:]
+ -[ICCloudClientAPNSChannelManager _xpcUnregisterToken:completion:]
+ -[ICCloudClientAPNSChannelManager cloudChannelSubscriptionsConfigurationChanged:]
+ -[ICCloudClientAPNSChannelManager invalidateAllRegistrations]
+ -[ICCloudClientAPNSChannelManager monitoredChannelsWereUpdatedWithMessagesByChannelID:completion:]
+ -[ICCloudClientAPNSChannelManager unregisterAllUpdates]
+ -[ICCloudEntityUpdate initWithType:pushMessages:error:channelIDs:unsubscribeReason:resubscribeReason:]
+ -[ICCloudEntityUpdate pushMessages]
+ -[ICCloudEntityUpdateRegistrationToken _UUID]
+ -[ICCloudEntityUpdateRegistrationToken _initWithUUID:]
+ -[ICCloudEntityUpdateRegistrationToken encodeWithCoder:]
+ -[ICCloudEntityUpdateRegistrationToken initWithCoder:]
+ -[ICCloudServiceStatusMonitor initWithUserIdentity:]
+ -[ICDefaults setShouldTreatCloudChannelRegistrationAsDisabled:]
+ -[ICDefaults shouldTreatCloudChannelRegistrationAsDisabled]
+ -[ICInAppMessageConfiguration syncEnabled]
+ -[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]
+ -[ICLibraryAuthServiceClientTokenProvider _handleAccountAuthenticationDidFinishNotification]
+ -[ICLibraryAuthServiceClientTokenProvider _shouldIncrementFailureCountForError:]
+ -[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]
+ -[ICLibraryAuthServiceClientTokenStatus allowRecoveryRefresh]
+ -[ICLibraryAuthServiceClientTokenStatus failureCount]
+ -[ICLibraryAuthServiceClientTokenStatus setAllowRecoveryRefresh:]
+ -[ICLibraryAuthServiceClientTokenStatus setFailureCount:]
+ -[ICMusicLibraryAuthTokenStatus failureCount]
+ -[ICMusicLibraryAuthTokenStatus setFailureCount:]
+ -[ICMusicSubscriptionStatusCache lastKnownSubscriptionStatusResponseForUserIdentity:]
+ -[ICURLBag musicChannelSubscriptionsMaxAllowedRegistrations]
+ -[_ICCloudAPNSChannelRegistrationState initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:registrationToken:lastProcessedGoLiveTimestamp:]
+ -[_ICCloudAPNSChannelRegistrationState lastProcessedGoLiveTimestamp]
+ -[_ICCloudAPNSChannelRegistrationState registrationToken]
+ -[_ICCloudUpdateRegistration initWithConfiguration:handler:token:]
+ -[_ICCloudUpdateRegistration lastProcessedGoLiveTimestamp]
+ -[_ICCloudUpdateRegistration setLastProcessedGoLiveTimestamp:]
+ -[_ICCloudUpdateRegistration token]
+ GCC_except_table1089
+ GCC_except_table1099
+ GCC_except_table1187
+ GCC_except_table1214
+ GCC_except_table1266
+ GCC_except_table1270
+ GCC_except_table1272
+ GCC_except_table1274
+ GCC_except_table1346
+ GCC_except_table1440
+ GCC_except_table152
+ GCC_except_table1639
+ GCC_except_table1652
+ GCC_except_table1910
+ GCC_except_table2094
+ GCC_except_table2123
+ GCC_except_table2138
+ GCC_except_table2186
+ GCC_except_table2298
+ GCC_except_table2314
+ GCC_except_table2363
+ GCC_except_table2365
+ GCC_except_table2371
+ GCC_except_table2378
+ GCC_except_table2421
+ GCC_except_table2426
+ GCC_except_table2428
+ GCC_except_table2433
+ GCC_except_table2436
+ GCC_except_table2449
+ GCC_except_table2545
+ GCC_except_table2585
+ GCC_except_table2616
+ GCC_except_table2618
+ GCC_except_table2620
+ GCC_except_table2622
+ GCC_except_table279
+ GCC_except_table284
+ GCC_except_table2976
+ GCC_except_table3028
+ GCC_except_table304
+ GCC_except_table31
+ GCC_except_table3192
+ GCC_except_table3209
+ GCC_except_table3246
+ GCC_except_table3256
+ GCC_except_table3355
+ GCC_except_table3640
+ GCC_except_table3643
+ GCC_except_table3658
+ GCC_except_table3669
+ GCC_except_table3688
+ GCC_except_table3728
+ GCC_except_table3744
+ GCC_except_table3857
+ GCC_except_table4018
+ GCC_except_table4185
+ GCC_except_table4228
+ GCC_except_table43
+ GCC_except_table4328
+ GCC_except_table4336
+ GCC_except_table4338
+ GCC_except_table4340
+ GCC_except_table4342
+ GCC_except_table4344
+ GCC_except_table4348
+ GCC_except_table4355
+ GCC_except_table4359
+ GCC_except_table4374
+ GCC_except_table4378
+ GCC_except_table4557
+ GCC_except_table4610
+ GCC_except_table4614
+ GCC_except_table4617
+ GCC_except_table4622
+ GCC_except_table4686
+ GCC_except_table4728
+ GCC_except_table4732
+ GCC_except_table4734
+ GCC_except_table4802
+ GCC_except_table4879
+ GCC_except_table5041
+ GCC_except_table5110
+ GCC_except_table513
+ GCC_except_table5191
+ GCC_except_table520
+ GCC_except_table5351
+ GCC_except_table5608
+ GCC_except_table5712
+ GCC_except_table5759
+ GCC_except_table5783
+ GCC_except_table5824
+ GCC_except_table5825
+ GCC_except_table5900
+ GCC_except_table5918
+ GCC_except_table6186
+ GCC_except_table6194
+ GCC_except_table6205
+ GCC_except_table6206
+ GCC_except_table6207
+ GCC_except_table6209
+ GCC_except_table6214
+ GCC_except_table6219
+ GCC_except_table6235
+ GCC_except_table6251
+ GCC_except_table6253
+ GCC_except_table6259
+ GCC_except_table6268
+ GCC_except_table6278
+ GCC_except_table6312
+ GCC_except_table6355
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6423
+ GCC_except_table6426
+ GCC_except_table6469
+ GCC_except_table6474
+ GCC_except_table6480
+ GCC_except_table6483
+ GCC_except_table6486
+ GCC_except_table6489
+ GCC_except_table6492
+ GCC_except_table6495
+ GCC_except_table6498
+ GCC_except_table6501
+ GCC_except_table6504
+ GCC_except_table6507
+ GCC_except_table6510
+ GCC_except_table6611
+ GCC_except_table6826
+ GCC_except_table6833
+ GCC_except_table7007
+ GCC_except_table7011
+ GCC_except_table7013
+ GCC_except_table7040
+ GCC_except_table7086
+ GCC_except_table7260
+ GCC_except_table7392
+ GCC_except_table7512
+ GCC_except_table7526
+ GCC_except_table7553
+ GCC_except_table7630
+ GCC_except_table7645
+ GCC_except_table7668
+ GCC_except_table7679
+ GCC_except_table7722
+ GCC_except_table7723
+ GCC_except_table7724
+ GCC_except_table7725
+ GCC_except_table7726
+ GCC_except_table7767
+ GCC_except_table7785
+ GCC_except_table7837
+ GCC_except_table7840
+ GCC_except_table7851
+ GCC_except_table7860
+ GCC_except_table7907
+ GCC_except_table8013
+ GCC_except_table802
+ GCC_except_table8046
+ GCC_except_table8112
+ GCC_except_table816
+ GCC_except_table8534
+ GCC_except_table8538
+ GCC_except_table8542
+ GCC_except_table8564
+ GCC_except_table8571
+ GCC_except_table8584
+ GCC_except_table8589
+ GCC_except_table8624
+ GCC_except_table8627
+ GCC_except_table868
+ GCC_except_table8698
+ GCC_except_table8743
+ GCC_except_table8791
+ GCC_except_table8820
+ GCC_except_table8825
+ GCC_except_table8827
+ GCC_except_table8829
+ GCC_except_table8862
+ GCC_except_table8994
+ GCC_except_table9002
+ GCC_except_table9007
+ GCC_except_table9022
+ GCC_except_table9030
+ GCC_except_table9074
+ GCC_except_table9225
+ GCC_except_table9229
+ GCC_except_table9231
+ GCC_except_table9269
+ GCC_except_table9272
+ GCC_except_table9279
+ GCC_except_table9282
+ GCC_except_table9529
+ GCC_except_table9539
+ GCC_except_table9597
+ GCC_except_table9684
+ GCC_except_table9689
+ GCC_except_table984
+ GCC_except_table9929
+ GCC_except_table995
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._lastProcessedGoLiveTimestamp
+ OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._registrationToken
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._maxAllowedRegistrations
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchEndOffsetSeconds
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchStartOffsetSeconds
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._deliveryQueue
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._isInvalidating
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._pauseUpdates
+ OBJC_IVAR_$_ICCloudClientAPNSChannelManager._registrationsByChannel
+ OBJC_IVAR_$_ICCloudEntityUpdate._pushMessages
+ OBJC_IVAR_$_ICCloudServiceStatusMonitor._userIdentity
+ OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._allowRecoveryRefresh
+ OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._failureCount
+ OBJC_IVAR_$_ICMusicLibraryAuthTokenStatus._failureCount
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._lastProcessedGoLiveTimestamp
+ OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._registrationToken
+ OBJC_IVAR_$__ICCloudUpdateRegistration._lastProcessedGoLiveTimestamp
+ OBJC_IVAR_$__ICCloudUpdateRegistration._token
+ _ContentTypeForPayloadValue.sContentTypeDict
+ _ICCloudChannelRegistrationConfigurationChangedNotification
+ _ICCloudChannelRegistrationEndOffsetSecondsKey
+ _ICCloudChannelRegistrationFetchEndOffsetSeconds
+ _ICCloudChannelRegistrationFetchStartOffsetSeconds
+ _ICCloudChannelRegistrationMaxAllowedSubscriptions
+ _ICCloudChannelRegistrationMaxSubscriptionsKey
+ _ICCloudChannelRegistrationStartOffsetSecondsKey
+ _ICURLBagKeyCloudChannelRegistrationMaxAllowedSubscription
+ _ISO8601DateFormatterWithFractionalSeconds.sFormatter
+ _ISO8601DateFormatterWithFractionalSeconds.sOnceToken
+ _ServerDidCompleteSetup
+ __55-[ICCloudClientAPNSChannelManager unregisterAllUpdates]_block_invoke
+ __58-[ICCloudClientAPNSChannelManager _serverSetupDidComplete]_block_invoke
+ __61-[ICCloudClientAPNSChannelManager invalidateAllRegistrations]_block_invoke
+ __61-[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]_block_invoke
+ __66-[ICCloudClientAPNSChannelManager _xpcUnregisterToken:completion:]_block_invoke
+ __71-[ICCloudClientAPNSChannelManager _xpcRegisterChannelState:completion:]_block_invoke
+ __84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke
+ __85+[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
+ __ICLogCategoryAPNSChannel
+ __OBJC_$_CLASS_PROP_LIST_ICCloudEntityUpdateRegistrationToken
+ __OBJC_$_PROP_LIST_ICCloudEntityUpdateRegistrationToken
+ ___55-[ICCloudClientAPNSChannelManager unregisterAllUpdates]_block_invoke
+ ___58-[ICCloudClientAPNSChannelManager _serverSetupDidComplete]_block_invoke
+ ___61-[ICCloudClientAPNSChannelManager invalidateAllRegistrations]_block_invoke
+ ___61-[ICCloudClientAPNSChannelManager invalidateAllRegistrations]_block_invoke_2
+ ___61-[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]_block_invoke
+ ___61-[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]_block_invoke_2
+ ___66-[ICCloudClientAPNSChannelManager _xpcUnregisterToken:completion:]_block_invoke
+ ___71-[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]_block_invoke
+ ___71-[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]_block_invoke_2
+ ___71-[ICCloudClientAPNSChannelManager _xpcRegisterChannelState:completion:]_block_invoke
+ ___80-[ICCloudClientAPNSChannelManager _dispatchUpdate:toRegistrationsForChannelIDs:]_block_invoke
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke_2
+ ___85+[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
+ ___85-[ICMusicSubscriptionStatusCache lastKnownSubscriptionStatusResponseForUserIdentity:]_block_invoke
+ ____ISO8601DateFormatterWithFractionalSeconds_block_invoke
+ ___block_descriptor_48_e8_32r40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"ICInAppMessageConfiguration"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16l
+ ___block_descriptor_48_e8_32s40r_e15_v32?0816^B24l
+ ___block_descriptor_48_e8_32s40s_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
+ ___block_descriptor_49_e8_32s40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16l
+ __handleAccountAuthenticationDidFinishNotification
+ _objc_msgSend$_computeChannelStatesForResync
+ _objc_msgSend$_deliverMessages:forChannelID:group:
+ _objc_msgSend$_dispatchUpdate:toRegistrationsForChannelIDs:
+ _objc_msgSend$_handleAccountAuthenticationDidFinishNotification
+ _objc_msgSend$_initWithUUID:
+ _objc_msgSend$_performSyncIfEnabledWithCompletion:
+ _objc_msgSend$_postCloudChannelRegistrationConfigurationChanged:
+ _objc_msgSend$_resumeUpdates
+ _objc_msgSend$_shouldIncrementFailureCountForError:
+ _objc_msgSend$_updateCloudChannelConfigurationUsingBag:source:
+ _objc_msgSend$_updateEntriesForExternalAccountsChanges:
+ _objc_msgSend$_xpcRegisterChannelState:completion:
+ _objc_msgSend$_xpcUnregisterToken:completion:
+ _objc_msgSend$allUpdatesPaused
+ _objc_msgSend$allowRecoveryRefresh
+ _objc_msgSend$beginObservingCloudServiceStatusForUserIdentity:completionHandler:
+ _objc_msgSend$dateFromISO8601Timestamp:defaultFetchStartSeconds:
+ _objc_msgSend$goLiveDate
+ _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:lastProcessedGoLiveTimestamp:registrationToken:
+ _objc_msgSend$initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:registrationToken:lastProcessedGoLiveTimestamp:
+ _objc_msgSend$initWithConfiguration:handler:token:
+ _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$initWithType:pushMessages:error:channelIDs:unsubscribeReason:resubscribeReason:
+ _objc_msgSend$invalidateAllRegistrationsWithCompletion:
+ _objc_msgSend$lastKnownSubscriptionStatusResponseForUserIdentity:
+ _objc_msgSend$lastProcessedGoLiveTimestamp
+ _objc_msgSend$maxAllowedCloudChannelRegistrations
+ _objc_msgSend$pushReceivedUpdateWithMessages:
+ _objc_msgSend$registerChannelState:completion:
+ _objc_msgSend$registrationFetchEndOffsetSeconds
+ _objc_msgSend$registrationFetchStartOffsetSeconds
+ _objc_msgSend$registrationToken
+ _objc_msgSend$requestCapabilitiesForUserIdentity:withPrivacyPromptPolicy:completionHandler:
+ _objc_msgSend$requestStorefrontCountryCodeForUserIdentity:completionHandler:
+ _objc_msgSend$requestStorefrontIdentifierForUserIdentity:completionHandler:
+ _objc_msgSend$revokeMusicKitUserTokensForAccountDSID:withCompletion:
+ _objc_msgSend$setAllowRecoveryRefresh:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setLastProcessedGoLiveTimestamp:
+ _objc_msgSend$shouldTreatCloudChannelRegistrationAsDisabled
+ _objc_msgSend$syncEnabled
+ _objc_msgSend$unregisterChannelWithToken:completion:
- +[ICCloudAPNSChannelPushMessage dateFromISO8601Timestamp:]
- +[ICCloudAPNSChannelPushMessage messageWithAPSIncomingMessage:]
- -[ICCloudChannelRegistrationAvailability _commitAvailability:source:]
- -[ICCloudClient unregisterUpdatesForChannelID:reason:]
- -[ICCloudClientAPNSChannelManager _snapshotChannelStatesForResync]
- -[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]
- -[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]
- -[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]
- -[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]
- -[ICCloudEntityUpdate initWithType:pushMessage:error:channelIDs:unsubscribeReason:resubscribeReason:]
- -[ICCloudEntityUpdateRegistrationToken _initInternal]
- -[ICCloudServiceStatusMonitor requestUserTokenForDeveloperToken:completionHandler:]
- -[ICLibraryAuthServiceClientTokenProvider _shouldStopBackgroundRefreshForError:]
- -[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]
- -[ICMusicLibraryAuthTokenStatus setShouldExcludeFromBackgroundRefresh:]
- -[_ICCloudUpdateRegistration initWithConfiguration:handler:]
- GCC_except_table1070
- GCC_except_table1080
- GCC_except_table1168
- GCC_except_table1195
- GCC_except_table1247
- GCC_except_table1251
- GCC_except_table1253
- GCC_except_table1255
- GCC_except_table1327
- GCC_except_table1422
- GCC_except_table148
- GCC_except_table1621
- GCC_except_table1634
- GCC_except_table1892
- GCC_except_table2076
- GCC_except_table2105
- GCC_except_table2120
- GCC_except_table2166
- GCC_except_table2278
- GCC_except_table2294
- GCC_except_table2343
- GCC_except_table2345
- GCC_except_table2351
- GCC_except_table2358
- GCC_except_table2386
- GCC_except_table2401
- GCC_except_table2408
- GCC_except_table2413
- GCC_except_table2416
- GCC_except_table2429
- GCC_except_table2525
- GCC_except_table2565
- GCC_except_table2596
- GCC_except_table2598
- GCC_except_table2600
- GCC_except_table2602
- GCC_except_table269
- GCC_except_table274
- GCC_except_table291
- GCC_except_table2952
- GCC_except_table3004
- GCC_except_table3168
- GCC_except_table3185
- GCC_except_table3198
- GCC_except_table3232
- GCC_except_table3331
- GCC_except_table3610
- GCC_except_table3616
- GCC_except_table3619
- GCC_except_table3645
- GCC_except_table3664
- GCC_except_table37
- GCC_except_table3704
- GCC_except_table3720
- GCC_except_table3833
- GCC_except_table3994
- GCC_except_table4161
- GCC_except_table4204
- GCC_except_table4304
- GCC_except_table4312
- GCC_except_table4314
- GCC_except_table4316
- GCC_except_table4318
- GCC_except_table4320
- GCC_except_table4324
- GCC_except_table4331
- GCC_except_table4335
- GCC_except_table4350
- GCC_except_table4354
- GCC_except_table4533
- GCC_except_table4586
- GCC_except_table4590
- GCC_except_table4593
- GCC_except_table4598
- GCC_except_table4662
- GCC_except_table4704
- GCC_except_table4708
- GCC_except_table4710
- GCC_except_table4777
- GCC_except_table4854
- GCC_except_table496
- GCC_except_table5016
- GCC_except_table503
- GCC_except_table5084
- GCC_except_table5165
- GCC_except_table5325
- GCC_except_table5582
- GCC_except_table5686
- GCC_except_table5733
- GCC_except_table5757
- GCC_except_table5798
- GCC_except_table5799
- GCC_except_table5874
- GCC_except_table5892
- GCC_except_table6152
- GCC_except_table6159
- GCC_except_table6167
- GCC_except_table6179
- GCC_except_table6180
- GCC_except_table6181
- GCC_except_table6182
- GCC_except_table6187
- GCC_except_table6192
- GCC_except_table6197
- GCC_except_table6226
- GCC_except_table6232
- GCC_except_table6241
- GCC_except_table6250
- GCC_except_table6284
- GCC_except_table6327
- GCC_except_table6334
- GCC_except_table6335
- GCC_except_table6395
- GCC_except_table6398
- GCC_except_table6418
- GCC_except_table6441
- GCC_except_table6452
- GCC_except_table6455
- GCC_except_table6458
- GCC_except_table6461
- GCC_except_table6464
- GCC_except_table6467
- GCC_except_table6470
- GCC_except_table6473
- GCC_except_table6476
- GCC_except_table6479
- GCC_except_table6482
- GCC_except_table6583
- GCC_except_table6796
- GCC_except_table6803
- GCC_except_table6977
- GCC_except_table6981
- GCC_except_table6983
- GCC_except_table7010
- GCC_except_table7056
- GCC_except_table7229
- GCC_except_table7361
- GCC_except_table7481
- GCC_except_table7495
- GCC_except_table7521
- GCC_except_table7598
- GCC_except_table7613
- GCC_except_table7636
- GCC_except_table7647
- GCC_except_table7690
- GCC_except_table7691
- GCC_except_table7692
- GCC_except_table7693
- GCC_except_table7694
- GCC_except_table7735
- GCC_except_table7753
- GCC_except_table7805
- GCC_except_table7808
- GCC_except_table7819
- GCC_except_table7828
- GCC_except_table785
- GCC_except_table7875
- GCC_except_table7965
- GCC_except_table799
- GCC_except_table7998
- GCC_except_table8064
- GCC_except_table8485
- GCC_except_table8489
- GCC_except_table8493
- GCC_except_table851
- GCC_except_table8515
- GCC_except_table8522
- GCC_except_table8535
- GCC_except_table8540
- GCC_except_table8575
- GCC_except_table8578
- GCC_except_table8649
- GCC_except_table8694
- GCC_except_table8742
- GCC_except_table8771
- GCC_except_table8776
- GCC_except_table8778
- GCC_except_table8780
- GCC_except_table8813
- GCC_except_table8945
- GCC_except_table8953
- GCC_except_table8958
- GCC_except_table8973
- GCC_except_table8981
- GCC_except_table9025
- GCC_except_table9176
- GCC_except_table9180
- GCC_except_table9182
- GCC_except_table9220
- GCC_except_table9223
- GCC_except_table9230
- GCC_except_table9233
- GCC_except_table9474
- GCC_except_table9484
- GCC_except_table9542
- GCC_except_table9629
- GCC_except_table9634
- GCC_except_table965
- GCC_except_table976
- GCC_except_table9874
- OBJC_IVAR_$_ICCloudClientAPNSChannelManager._listenerEndpointProvider
- OBJC_IVAR_$_ICCloudClientAPNSChannelManager._tokensByChannelAndReason
- _ContentTypeForPayloadValue.__contentTypeDict
- _ICCloudChannelRegistrationAvailabilityDidChangeNotification
- __103-[ICCloudClientAPNSChannelManager registerForUpdatesWithConfiguration:updateHandler:completionHandler:]_block_invoke
- __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke
- __66-[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]_block_invoke
- __73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
- __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke
- __83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke
- __85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
- ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke_2
- ___62-[ICCloudClientAPNSChannelManager unregisterUpdatesForTokens:]_block_invoke
- ___64-[ICCloudClientAPNSChannelManager channelRegistrationsDisabled:]_block_invoke
- ___66-[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]_block_invoke
- ___72-[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]_block_invoke
- ___72-[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]_block_invoke
- ___73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke_2
- ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
- ___block_descriptor_41_e8_32r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
- ___block_descriptor_56_e8_32s40r48r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
- ___block_descriptor_57_e8_32s40bs48bs_e17_v16?0"NSError"8l
- ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0l
- _objc_msgSend$_commitAvailability:source:
- _objc_msgSend$_initInternal
- _objc_msgSend$_shouldStopBackgroundRefreshForError:
- _objc_msgSend$_snapshotChannelStatesForResync
- _objc_msgSend$_updateEntriesForAccountsChanges
- _objc_msgSend$_xpcUpdateReasonsWithState:completion:
- _objc_msgSend$anyObject
- _objc_msgSend$beginObservingCloudServiceStatusWithCompletionHandler:
- _objc_msgSend$cloudChannelSubscriptionsDidBecomeEnabled:
- _objc_msgSend$dateFromISO8601Timestamp:
- _objc_msgSend$handleCloudServerSetupCompleted
- _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:
- _objc_msgSend$initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:
- _objc_msgSend$initWithConfiguration:handler:
- _objc_msgSend$initWithType:pushMessage:error:channelIDs:unsubscribeReason:resubscribeReason:
- _objc_msgSend$pushReceivedUpdateWithMessage:
- _objc_msgSend$requestCapabilitiesWithPrivacyPromptPolicy:completionHandler:
- _objc_msgSend$requestStorefrontCountryCodeWithCompletionHandler:
- _objc_msgSend$requestStorefrontIdentifierWithCompletionHandler:
- _objc_msgSend$requestUserTokenForDeveloperToken:options:completionHandler:
- _objc_msgSend$setShouldExcludeFromBackgroundRefresh:
- _objc_msgSend$shouldExcludeFromBackgroundRefresh
- _objc_msgSend$unregisterUpdatesForChannelID:reason:
- _objc_msgSend$updateMonitoredReasonsWithChannelState:completion:
CStrings:
+ "%{public}@ Allowing recovery refresh for account %{public}@"
+ "%{public}@ Cancelling existing periodic poll task"
+ "%{public}@ Clearing error state for account %{public}@ that was pending privacy acceptance"
+ "%{public}@ Failed to load DSID for last known subscription status. err=%{public}@"
+ "%{public}@ Failed to load configuration for sync. err=%{public}@"
+ "%{public}@ Not scheduling periodic poll because in-app message syncing is disabled. err=%{public}@"
+ "%{public}@ Not scheduling refresh timer since there are no accounts to schedule"
+ "%{public}@ Not syncing because in-app message syncing is disabled"
+ "%{public}@ was initialized with initial subscription status %{public}@."
+ "<%@ %p channelID=%@ contentType=%ld storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ lastProcessedGoLiveTimestamp=%@ registrationToken=%p observesAllLibraryAlbums=%d>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reasons=%@ expectedReleaseDate=%@ registrationToken=%@ lastProcessedGoLiveTimestamp=%@>"
+ "<%@ %p type=%@ pushMessages=%@ error=%@ channelIDs=%@ unsubscribeReason=%@ resubscribeReason=%@>"
+ "<%@: %p %@>"
+ "<%@:%p result=%@ lastError=%@ lastUpdate='%@' failureCount=%lu allowRecoveryRefresh=%@"
+ "ICCloudAPNSChannelPushMessage - Could not create date from time=%{public}@, setting to %{public}@"
+ "ICCloudChannelRegistrationAvailability - availability changed old=%{public}@ new=%{public}@, registrationStartOffset old=%lu, new=%lu,  registrationEndOffset old=%lu, new=%lu, maxSubscriptions old=%lu, new=%lu source=%{public}@"
+ "ICCloudChannelRegistrationAvailability - scheduling bag fetch retry delay=%.0f"
+ "ICCloudChannelRegistrationConfigurationChangedNotification"
+ "ICCloudChannelRegistrationEndOffsetSecondsKey"
+ "ICCloudChannelRegistrationMaxSubscriptionsKey"
+ "ICCloudChannelRegistrationStartOffsetSecondsKey"
+ "ICCloudClient - not unregistering; token is nil."
+ "ICCloudClientAPNSChannelManager - dispatching a lifecycle update channels=%{public}@ handlers=%lu"
+ "ICCloudClientAPNSChannelManager - dispatching updates channelID=%{public}@ ordered=%lu unordered=%lu"
+ "ICCloudClientAPNSChannelManager - feature disabled daemonChannels=%{public}@ localOnly=%{public}@"
+ "ICCloudClientAPNSChannelManager - forwarding tokens with no local registration count=%lu"
+ "ICCloudClientAPNSChannelManager - invalidateAllRegistrations failed err=%{public}@"
+ "ICCloudClientAPNSChannelManager - invalidating all registrations handlers=%lu"
+ "ICCloudClientAPNSChannelManager - not able to registerChannelState channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send invalidateAllRegistrations; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send registerChannelState; proxy error. channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send unregisterChannelWithToken; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to unregisterChannelWithToken err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not delivering per-channel cancellation channelIDs=%{public}@; updates are paused"
+ "ICCloudClientAPNSChannelManager - not delivering pushes; feature is unavailable. channelCount=%lu"
+ "ICCloudClientAPNSChannelManager - not delivering pushes; updates are paused"
+ "ICCloudClientAPNSChannelManager - not dispatching a lifecycle update channels=%{public}@; updates are paused"
+ "ICCloudClientAPNSChannelManager - not dispatching observe-all update; updates are paused."
+ "ICCloudClientAPNSChannelManager - not dispatching updates; no handlers on channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not registering; daemon minted no token channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not registering; invalidation in progress channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - not resyncing after server setup; hasRegistrations=%{BOOL}u, updatesPaused=%{BOOL}u, _lastSetupCompletedResyncRequest=%{public}@"
+ "ICCloudClientAPNSChannelManager - not seating token; invalidation in progress channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not sending invalidateAllRegistrations; no XPC connection."
+ "ICCloudClientAPNSChannelManager - not sending registerChannelState; no XPC connection. channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not sending unregisterChannelWithToken; no XPC connection."
+ "ICCloudClientAPNSChannelManager - paused all updates registrations=%lu handlers=%lu"
+ "ICCloudClientAPNSChannelManager - pausing all updates"
+ "ICCloudClientAPNSChannelManager - receiving updates channelID=%{public}@ count=%lu"
+ "ICCloudClientAPNSChannelManager - registered token=%{public}@ channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - resuming updates"
+ "ICCloudClientAPNSChannelManager - resyncing all existing registrations _pauseUpdates=%{BOOL}u."
+ "ICCloudClientAPNSChannelManager - sending registerChannelState state=%{public}@"
+ "ICCloudClientAPNSChannelManager - tearing down registrations tokens=%lu handlers=%lu notifyDaemon=%{BOOL}u paused=%{BOOL}u err=%{public}@"
+ "ICCloudClientAPNSChannelManager - updates are already paused"
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ failed to get remote object proxy: %{public}@"
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ service interrupted."
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ service invalidated."
+ "ICCloudServiceStatusMonitor %{public}@: Revocation of music user tokens completed"
+ "ICCloudServiceStatusMonitor %{public}@: Revocation of music user tokens completed error=%{public}@"
+ "ICCloudServiceStatusMonitor %{public}@: Revoking music user tokens DSID %{public}@"
+ "ICInternalDefaultsKeyTreatCloudChannelRegistrationAsDisabled"
+ "UpdatesPaused"
+ "allowRecoveryRefresh"
+ "com.apple.StoreServices.authfinish"
+ "com.apple.iTunesCloud.ICCloudClientAPNSChannelManager.deliveryQueue"
+ "inAppMessagesSyncEnabled"
+ "lastProcessedGoLiveTimestamp"
+ "max-channel-subscriptions"
+ "registrationToken"
+ "v24@?0@\"ICCloudEntityUpdateRegistrationToken\"8@\"NSError\"16"
- "%{public}@ Skipping background refresh of DSID %@. last error: %{public}@}"
- "%{public}@ was initialized."
- "%{public}@: Revocation of music user tokens completed"
- "%{public}@: Revocation of music user tokens completed error=%{public}@"
- "%{public}@: Revoking music user tokens DSID %{public}@"
- "<%@ %p channelID=%@ contentType=%ld _storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
- "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ observesAllLibraryAlbums=%d>"
- "<%@ %p channelID=%@ entityType=%ld storeID=%lld reasons=%@ expectedReleaseDate=%@>"
- "<%@ %p type=%@ pushMessage=%@ error=%@ channelIDs=%@ unsubscribeReason=%@ resubscribeReason=%@>"
- "<%@: %p>"
- "<%@:%p result=%@ lastError=%@ lastUpdate='%@' autoRefreshEnabled=%@>"
- "Cannot unregister updates: token is nil."
- "ICCloudAPNSChannelPushMessage - not decoding push; missing storeID. payload=%{public}@"
- "ICCloudChannelRegistrationAvailability - availability changed old=%{public}@ new=%{public}@ source=%{public}@"
- "ICCloudChannelRegistrationAvailability - not dispatching transition; no observer wired newState=%{public}@"
- "ICCloudChannelRegistrationAvailability - scheduling bag fetch retry delay=%.0fs"
- "ICCloudChannelRegistrationAvailabilityDidChangeNotification"
- "ICCloudClientAPNSChannelManager - dispatching update handlerCount=%lu channelID=%{public}@"
- "ICCloudClientAPNSChannelManager - feature disabled daemonChannels=%{public}@ localOnly=%{public}@ handlers=%lu"
- "ICCloudClientAPNSChannelManager - not able to add reason on daemon; committing locally channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not able to send updateMonitoredReasons; proxy err channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not able to update daemon channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons during tear-down channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not able to updateMonitoredReasons for race-repair channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not delivering push; feature is unavailable. channelID=%{public}@"
- "ICCloudClientAPNSChannelManager - not dispatching update; no handlers on channelID=%{public}@"
- "ICCloudClientAPNSChannelManager - not registering; daemon update failed channelID=%{public}@ err=%{public}@"
- "ICCloudClientAPNSChannelManager - not resyncing after server setup; debounced."
- "ICCloudClientAPNSChannelManager - not resyncing after server setup; no registrations."
- "ICCloudClientAPNSChannelManager - not sending daemon updates; nothing to unregister."
- "ICCloudClientAPNSChannelManager - not sending updateMonitoredReasons; no XPC connection. channelID=%{public}@"
- "ICCloudClientAPNSChannelManager - not unregistering channel; no matching tokens channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - not unregistering tokens; feature is unavailable. tokenCount=%lu"
- "ICCloudClientAPNSChannelManager - not unregistering unknown tokens count=%lu"
- "ICCloudClientAPNSChannelManager - not unregistering; feature is unavailable. channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - not unregistering; invalid arguments channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - receiving update pushMessage=%{public}@"
- "ICCloudClientAPNSChannelManager - registering configuration=%{public}@ token=%{public}@"
- "ICCloudClientAPNSChannelManager - registering token=%{public}@ channelID=%{public}@ reason=%ld isRegisteredChannel=%{BOOL}u isRegisteredReason=%{BOOL}u"
- "ICCloudClientAPNSChannelManager - sending updateMonitoredReasons state=%{public}@"
- "ICCloudClientAPNSChannelManager - tearing down registrations xpcUpdates=%lu handlers=%lu notifyDaemon=%{BOOL}u err=%{public}@"
- "ICCloudClientAPNSChannelManager - unregistering channel channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - unregistering tokens count=%lu channelID=%{public}@ reason=%ld"
- "excludeFromBackgroundRefresh"
- "shouldExcludeFromBackgroundRefresh"
```

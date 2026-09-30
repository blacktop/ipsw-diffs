## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4026.200.13.0.0
-  __TEXT.__text: 0x3c1a5c
-  __TEXT.__objc_methlist: 0x188a4
+4026.200.17.0.0
+  __TEXT.__text: 0x3c410c
+  __TEXT.__objc_methlist: 0x189a4
   __TEXT.__const: 0x225f8
   __TEXT.__dlopen_cstrs: 0x4cf
-  __TEXT.__gcc_except_tab: 0x2b6c
-  __TEXT.__cstring: 0x17ae4
-  __TEXT.__oslogstring: 0x223bb
+  __TEXT.__gcc_except_tab: 0x2b70
+  __TEXT.__cstring: 0x17c21
+  __TEXT.__oslogstring: 0x22515
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x8378
+  __TEXT.__unwind_info: 0x83b0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7458
+  __DATA_CONST.__const: 0x7490
   __DATA_CONST.__objc_classlist: 0xdd0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa5c8
+  __DATA_CONST.__objc_selrefs: 0xa650
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
   __DATA_CONST.__got: 0x1090
-  __AUTH_CONST.__const: 0x18638
-  __AUTH_CONST.__cfstring: 0x18ae0
-  __AUTH_CONST.__objc_const: 0x31880
+  __AUTH_CONST.__const: 0x18658
+  __AUTH_CONST.__cfstring: 0x18b60
+  __AUTH_CONST.__objc_const: 0x31a40
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0xa68
-  __AUTH.__objc_data: 0x5640
-  __DATA.__objc_ivar: 0x24bc
-  __DATA.__data: 0x31a0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x24e0
+  __DATA.__data: 0x30d0
   __DATA.__common: 0xb88
-  __DATA_DIRTY.__objc_data: 0x33e0
-  __DATA_DIRTY.__data: 0x108
+  __DATA_DIRTY.__objc_data: 0x87f0
+  __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__bss: 0x398
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10179
-  Symbols:   21475
-  CStrings:  5500
+  Functions: 10201
+  Symbols:   21519
+  CStrings:  5510
 
Symbols:
+ +[ICCloudAPNSChannelPushMessage dateFromISO8601Timestamp:defaultFetchStartSeconds:]
+ +[ICCloudAPNSChannelPushMessage messageWithAPSIncomingMessage:defaultFetchStartSeconds:]
+ +[ICCloudEntityUpdate allUpdatesPaused]
+ +[ICCloudEntityUpdate pushReceivedUpdateWithMessages:]
+ +[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]
+ -[ICCloudAPNSChannelPushMessage hash]
+ -[ICCloudAPNSChannelPushMessage isEqual:]
+ -[ICCloudAPNSChannelRegistrationConfiguration initWithChannelID:entityType:storeID:reason:expectedReleaseDate:lastProcessedGoLiveTimestamp:registrationToken:]
+ -[ICCloudAPNSChannelRegistrationConfiguration lastProcessedGoLiveTimestamp]
+ -[ICCloudAPNSChannelRegistrationConfiguration registrationToken]
+ -[ICCloudClientAPNSChannelManager _computeChannelStatesForResync]
+ -[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]
+ -[ICCloudClientAPNSChannelManager _dispatchUpdate:toRegistrationsForChannelIDs:]
+ -[ICCloudClientAPNSChannelManager _resumeUpdates]
+ -[ICCloudClientAPNSChannelManager _serverSetupDidComplete]
+ -[ICCloudClientAPNSChannelManager _xpcRegisterChannelState:completion:]
+ -[ICCloudClientAPNSChannelManager _xpcUnregisterToken:completion:]
+ -[ICCloudClientAPNSChannelManager monitoredChannelsWereUpdatedWithMessagesByChannelID:completion:]
+ -[ICCloudClientAPNSChannelManager unregisterAllUpdates]
+ -[ICCloudEntityUpdate initWithType:pushMessages:error:channelIDs:unsubscribeReason:resubscribeReason:]
+ -[ICCloudEntityUpdate pushMessages]
+ -[ICCloudEntityUpdateRegistrationToken _UUID]
+ -[ICCloudServiceStatusMonitor initWithUserIdentity:]
+ -[ICInAppMessageConfiguration syncEnabled]
+ -[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]
+ -[_ICCloudAPNSChannelRegistrationState initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:registrationToken:lastProcessedGoLiveTimestamp:]
+ -[_ICCloudAPNSChannelRegistrationState lastProcessedGoLiveTimestamp]
+ -[_ICCloudAPNSChannelRegistrationState registrationToken]
+ -[_ICCloudUpdateRegistration initWithConfiguration:handler:token:]
+ -[_ICCloudUpdateRegistration lastProcessedGoLiveTimestamp]
+ -[_ICCloudUpdateRegistration setLastProcessedGoLiveTimestamp:]
+ -[_ICCloudUpdateRegistration token]
+ GCC_except_table1038
+ GCC_except_table1126
+ GCC_except_table1152
+ GCC_except_table1208
+ GCC_except_table1210
+ GCC_except_table1212
+ GCC_except_table1284
+ GCC_except_table1378
+ GCC_except_table1577
+ GCC_except_table1590
+ GCC_except_table1848
+ GCC_except_table2032
+ GCC_except_table2061
+ GCC_except_table2076
+ GCC_except_table2116
+ GCC_except_table2228
+ GCC_except_table2243
+ GCC_except_table2292
+ GCC_except_table2294
+ GCC_except_table2307
+ GCC_except_table2335
+ GCC_except_table2357
+ GCC_except_table2362
+ GCC_except_table2365
+ GCC_except_table2378
+ GCC_except_table2455
+ GCC_except_table2464
+ GCC_except_table2467
+ GCC_except_table2470
+ GCC_except_table2473
+ GCC_except_table2475
+ GCC_except_table2486
+ GCC_except_table2488
+ GCC_except_table2505
+ GCC_except_table253
+ GCC_except_table2544
+ GCC_except_table256
+ GCC_except_table2575
+ GCC_except_table2577
+ GCC_except_table2579
+ GCC_except_table2581
+ GCC_except_table274
+ GCC_except_table2935
+ GCC_except_table2980
+ GCC_except_table3128
+ GCC_except_table3145
+ GCC_except_table3155
+ GCC_except_table3179
+ GCC_except_table3189
+ GCC_except_table3287
+ GCC_except_table3570
+ GCC_except_table3573
+ GCC_except_table3588
+ GCC_except_table3599
+ GCC_except_table3618
+ GCC_except_table3658
+ GCC_except_table3672
+ GCC_except_table3785
+ GCC_except_table3945
+ GCC_except_table4110
+ GCC_except_table4152
+ GCC_except_table4252
+ GCC_except_table4260
+ GCC_except_table4262
+ GCC_except_table4264
+ GCC_except_table4266
+ GCC_except_table4268
+ GCC_except_table4279
+ GCC_except_table4283
+ GCC_except_table4298
+ GCC_except_table4301
+ GCC_except_table4480
+ GCC_except_table4536
+ GCC_except_table4539
+ GCC_except_table4544
+ GCC_except_table4608
+ GCC_except_table4650
+ GCC_except_table4654
+ GCC_except_table4656
+ GCC_except_table4723
+ GCC_except_table474
+ GCC_except_table479
+ GCC_except_table4800
+ GCC_except_table4888
+ GCC_except_table4971
+ GCC_except_table5040
+ GCC_except_table5121
+ GCC_except_table5281
+ GCC_except_table5538
+ GCC_except_table5643
+ GCC_except_table5691
+ GCC_except_table5715
+ GCC_except_table5756
+ GCC_except_table5757
+ GCC_except_table5830
+ GCC_except_table5848
+ GCC_except_table6124
+ GCC_except_table6135
+ GCC_except_table6137
+ GCC_except_table6138
+ GCC_except_table6139
+ GCC_except_table6144
+ GCC_except_table6149
+ GCC_except_table6154
+ GCC_except_table6165
+ GCC_except_table6182
+ GCC_except_table6188
+ GCC_except_table6197
+ GCC_except_table6207
+ GCC_except_table6241
+ GCC_except_table6273
+ GCC_except_table6293
+ GCC_except_table6294
+ GCC_except_table6354
+ GCC_except_table6357
+ GCC_except_table6371
+ GCC_except_table6394
+ GCC_except_table6399
+ GCC_except_table6405
+ GCC_except_table6408
+ GCC_except_table6411
+ GCC_except_table6414
+ GCC_except_table6417
+ GCC_except_table6420
+ GCC_except_table6423
+ GCC_except_table6426
+ GCC_except_table6429
+ GCC_except_table6432
+ GCC_except_table6435
+ GCC_except_table6536
+ GCC_except_table6750
+ GCC_except_table6757
+ GCC_except_table6931
+ GCC_except_table6935
+ GCC_except_table6937
+ GCC_except_table6964
+ GCC_except_table7010
+ GCC_except_table7184
+ GCC_except_table7316
+ GCC_except_table7436
+ GCC_except_table7448
+ GCC_except_table7471
+ GCC_except_table7549
+ GCC_except_table7564
+ GCC_except_table7587
+ GCC_except_table7598
+ GCC_except_table761
+ GCC_except_table7642
+ GCC_except_table7643
+ GCC_except_table7644
+ GCC_except_table7645
+ GCC_except_table7646
+ GCC_except_table7687
+ GCC_except_table7705
+ GCC_except_table773
+ GCC_except_table7757
+ GCC_except_table7769
+ GCC_except_table7776
+ GCC_except_table7823
+ GCC_except_table7929
+ GCC_except_table7962
+ GCC_except_table8020
+ GCC_except_table8021
+ GCC_except_table8034
+ GCC_except_table815
+ GCC_except_table8456
+ GCC_except_table8460
+ GCC_except_table8486
+ GCC_except_table8493
+ GCC_except_table8504
+ GCC_except_table8509
+ GCC_except_table8544
+ GCC_except_table8547
+ GCC_except_table8618
+ GCC_except_table8663
+ GCC_except_table8711
+ GCC_except_table8740
+ GCC_except_table8745
+ GCC_except_table8747
+ GCC_except_table8749
+ GCC_except_table8781
+ GCC_except_table8913
+ GCC_except_table8921
+ GCC_except_table8926
+ GCC_except_table8941
+ GCC_except_table8949
+ GCC_except_table8993
+ GCC_except_table9142
+ GCC_except_table9146
+ GCC_except_table9148
+ GCC_except_table9186
+ GCC_except_table9189
+ GCC_except_table9196
+ GCC_except_table9199
+ GCC_except_table929
+ GCC_except_table938
+ GCC_except_table9444
+ GCC_except_table9454
+ GCC_except_table9512
+ GCC_except_table9599
+ GCC_except_table9604
+ GCC_except_table9844
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._lastProcessedGoLiveTimestamp
+ _OBJC_IVAR_$_ICCloudAPNSChannelRegistrationConfiguration._registrationToken
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._deliveryQueue
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._pauseUpdates
+ _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._registrationsByChannel
+ _OBJC_IVAR_$_ICCloudEntityUpdate._pushMessages
+ _OBJC_IVAR_$_ICCloudServiceStatusMonitor._userIdentity
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._lastProcessedGoLiveTimestamp
+ _OBJC_IVAR_$__ICCloudAPNSChannelRegistrationState._registrationToken
+ _OBJC_IVAR_$__ICCloudUpdateRegistration._lastProcessedGoLiveTimestamp
+ _OBJC_IVAR_$__ICCloudUpdateRegistration._token
+ __ContentTypeForPayloadValue.sContentTypeDict
+ __ISO8601DateFormatterWithFractionalSeconds.sFormatter
+ __ISO8601DateFormatterWithFractionalSeconds.sOnceToken
+ __OBJC_$_PROP_LIST_ICCloudEntityUpdateRegistrationToken
+ ___58-[ICCloudClientAPNSChannelManager _serverSetupDidComplete]_block_invoke
+ ___61-[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]_block_invoke
+ ___61-[ICInAppMessageManager _performSyncIfEnabledWithCompletion:]_block_invoke_2
+ ___66-[ICCloudClientAPNSChannelManager _xpcUnregisterToken:completion:]_block_invoke
+ ___71-[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]_block_invoke
+ ___71-[ICCloudClientAPNSChannelManager _deliverMessages:forChannelID:group:]_block_invoke_2
+ ___71-[ICCloudClientAPNSChannelManager _xpcRegisterChannelState:completion:]_block_invoke
+ ___80-[ICCloudClientAPNSChannelManager _dispatchUpdate:toRegistrationsForChannelIDs:]_block_invoke
+ ___85+[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
+ ____ISO8601DateFormatterWithFractionalSeconds_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"ICInAppMessageConfiguration"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16ls32l8s40l8s56l8s48l8s64l8
+ _objc_msgSend$_computeChannelStatesForResync
+ _objc_msgSend$_deliverMessages:forChannelID:group:
+ _objc_msgSend$_dispatchUpdate:toRegistrationsForChannelIDs:
+ _objc_msgSend$_performSyncIfEnabledWithCompletion:
+ _objc_msgSend$_resumeUpdates
+ _objc_msgSend$_xpcRegisterChannelState:completion:
+ _objc_msgSend$_xpcUnregisterToken:completion:
+ _objc_msgSend$beginObservingCloudServiceStatusForUserIdentity:completionHandler:
+ _objc_msgSend$dateFromISO8601Timestamp:defaultFetchStartSeconds:
+ _objc_msgSend$goLiveDate
+ _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:lastProcessedGoLiveTimestamp:registrationToken:
+ _objc_msgSend$initWithChannelID:entityType:storeID:reasons:expectedReleaseDate:registrationToken:lastProcessedGoLiveTimestamp:
+ _objc_msgSend$initWithConfiguration:handler:token:
+ _objc_msgSend$initWithType:pushMessages:error:channelIDs:unsubscribeReason:resubscribeReason:
+ _objc_msgSend$lastProcessedGoLiveTimestamp
+ _objc_msgSend$pushReceivedUpdateWithMessages:
+ _objc_msgSend$registerChannelState:completion:
+ _objc_msgSend$registrationToken
+ _objc_msgSend$requestCapabilitiesForUserIdentity:withPrivacyPromptPolicy:completionHandler:
+ _objc_msgSend$requestStorefrontCountryCodeForUserIdentity:completionHandler:
+ _objc_msgSend$requestStorefrontIdentifierForUserIdentity:completionHandler:
+ _objc_msgSend$revokeMusicKitUserTokensForAccountDSID:withCompletion:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setLastProcessedGoLiveTimestamp:
+ _objc_msgSend$syncEnabled
+ _objc_msgSend$unregisterChannelWithToken:completion:
- +[ICCloudAPNSChannelPushMessage dateFromISO8601Timestamp:]
- +[ICCloudAPNSChannelPushMessage messageWithAPSIncomingMessage:]
- -[ICCloudClient unregisterUpdatesForChannelID:reason:]
- -[ICCloudClientAPNSChannelManager _snapshotChannelStatesForResync]
- -[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]
- -[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]
- -[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]
- -[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]
- -[ICCloudEntityUpdate initWithType:pushMessage:error:channelIDs:unsubscribeReason:resubscribeReason:]
- -[ICCloudServiceStatusMonitor requestUserTokenForDeveloperToken:completionHandler:]
- -[_ICCloudUpdateRegistration initWithConfiguration:handler:]
- GCC_except_table1022
- GCC_except_table1118
- GCC_except_table1144
- GCC_except_table1196
- GCC_except_table1200
- GCC_except_table1202
- GCC_except_table1276
- GCC_except_table1371
- GCC_except_table1570
- GCC_except_table1583
- GCC_except_table1841
- GCC_except_table2025
- GCC_except_table2054
- GCC_except_table2069
- GCC_except_table2109
- GCC_except_table2221
- GCC_except_table2236
- GCC_except_table2285
- GCC_except_table2287
- GCC_except_table2293
- GCC_except_table2328
- GCC_except_table2343
- GCC_except_table2348
- GCC_except_table2358
- GCC_except_table2371
- GCC_except_table2448
- GCC_except_table2457
- GCC_except_table2460
- GCC_except_table2463
- GCC_except_table2466
- GCC_except_table2468
- GCC_except_table247
- GCC_except_table2479
- GCC_except_table2481
- GCC_except_table2498
- GCC_except_table250
- GCC_except_table2537
- GCC_except_table2568
- GCC_except_table2570
- GCC_except_table2572
- GCC_except_table2574
- GCC_except_table265
- GCC_except_table2928
- GCC_except_table2973
- GCC_except_table3121
- GCC_except_table3138
- GCC_except_table3148
- GCC_except_table3172
- GCC_except_table3182
- GCC_except_table3280
- GCC_except_table3559
- GCC_except_table3563
- GCC_except_table3581
- GCC_except_table3592
- GCC_except_table3611
- GCC_except_table3651
- GCC_except_table3665
- GCC_except_table3778
- GCC_except_table3938
- GCC_except_table4103
- GCC_except_table4145
- GCC_except_table4245
- GCC_except_table4253
- GCC_except_table4255
- GCC_except_table4257
- GCC_except_table4259
- GCC_except_table4261
- GCC_except_table4265
- GCC_except_table4276
- GCC_except_table4291
- GCC_except_table4294
- GCC_except_table4473
- GCC_except_table4525
- GCC_except_table4529
- GCC_except_table4537
- GCC_except_table4601
- GCC_except_table4643
- GCC_except_table4647
- GCC_except_table4649
- GCC_except_table468
- GCC_except_table4716
- GCC_except_table473
- GCC_except_table4793
- GCC_except_table4881
- GCC_except_table4964
- GCC_except_table5032
- GCC_except_table5113
- GCC_except_table5273
- GCC_except_table5530
- GCC_except_table5635
- GCC_except_table5683
- GCC_except_table5707
- GCC_except_table5748
- GCC_except_table5749
- GCC_except_table5822
- GCC_except_table5840
- GCC_except_table6100
- GCC_except_table6127
- GCC_except_table6128
- GCC_except_table6129
- GCC_except_table6130
- GCC_except_table6131
- GCC_except_table6141
- GCC_except_table6146
- GCC_except_table6157
- GCC_except_table6172
- GCC_except_table6174
- GCC_except_table6189
- GCC_except_table6199
- GCC_except_table6233
- GCC_except_table6265
- GCC_except_table6278
- GCC_except_table6285
- GCC_except_table6346
- GCC_except_table6349
- GCC_except_table6363
- GCC_except_table6386
- GCC_except_table6391
- GCC_except_table6397
- GCC_except_table6400
- GCC_except_table6403
- GCC_except_table6406
- GCC_except_table6409
- GCC_except_table6412
- GCC_except_table6415
- GCC_except_table6418
- GCC_except_table6421
- GCC_except_table6424
- GCC_except_table6427
- GCC_except_table6528
- GCC_except_table6742
- GCC_except_table6749
- GCC_except_table6923
- GCC_except_table6927
- GCC_except_table6929
- GCC_except_table6956
- GCC_except_table7002
- GCC_except_table7175
- GCC_except_table7307
- GCC_except_table7427
- GCC_except_table7439
- GCC_except_table7462
- GCC_except_table7540
- GCC_except_table755
- GCC_except_table7555
- GCC_except_table7578
- GCC_except_table7589
- GCC_except_table7633
- GCC_except_table7634
- GCC_except_table7635
- GCC_except_table7636
- GCC_except_table7637
- GCC_except_table767
- GCC_except_table7678
- GCC_except_table7696
- GCC_except_table7748
- GCC_except_table7751
- GCC_except_table7767
- GCC_except_table7814
- GCC_except_table7907
- GCC_except_table7940
- GCC_except_table7998
- GCC_except_table7999
- GCC_except_table8012
- GCC_except_table809
- GCC_except_table8434
- GCC_except_table8438
- GCC_except_table8442
- GCC_except_table8471
- GCC_except_table8482
- GCC_except_table8487
- GCC_except_table8522
- GCC_except_table8525
- GCC_except_table8596
- GCC_except_table8641
- GCC_except_table8689
- GCC_except_table8718
- GCC_except_table8723
- GCC_except_table8725
- GCC_except_table8727
- GCC_except_table8759
- GCC_except_table8891
- GCC_except_table8899
- GCC_except_table8904
- GCC_except_table8919
- GCC_except_table8927
- GCC_except_table8971
- GCC_except_table9120
- GCC_except_table9124
- GCC_except_table9126
- GCC_except_table9164
- GCC_except_table9167
- GCC_except_table9174
- GCC_except_table9177
- GCC_except_table921
- GCC_except_table930
- GCC_except_table9422
- GCC_except_table9432
- GCC_except_table9490
- GCC_except_table9577
- GCC_except_table9582
- GCC_except_table9822
- _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._listenerEndpointProvider
- _OBJC_IVAR_$_ICCloudClientAPNSChannelManager._tokensByChannelAndReason
- __ContentTypeForPayloadValue.__contentTypeDict
- ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke_2
- ___62-[ICCloudClientAPNSChannelManager unregisterUpdatesForTokens:]_block_invoke
- ___64-[ICCloudClientAPNSChannelManager channelRegistrationsDisabled:]_block_invoke
- ___66-[ICCloudClientAPNSChannelManager handleCloudServerSetupCompleted]_block_invoke
- ___72-[ICCloudClientAPNSChannelManager monitoredEntityWasUpdatedWithMessage:]_block_invoke
- ___72-[ICCloudClientAPNSChannelManager unregisterUpdatesForChannelID:reason:]_block_invoke
- ___73-[ICCloudClientAPNSChannelManager _xpcUpdateReasonsWithState:completion:]_block_invoke
- ___83-[ICCloudClientAPNSChannelManager _tearDownAllRegistrationsWithError:notifyDaemon:]_block_invoke_2
- ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke
- ___block_descriptor_57_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
- _objc_msgSend$_snapshotChannelStatesForResync
- _objc_msgSend$_xpcUpdateReasonsWithState:completion:
- _objc_msgSend$anyObject
- _objc_msgSend$beginObservingCloudServiceStatusWithCompletionHandler:
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
- _objc_msgSend$unregisterUpdatesForChannelID:reason:
- _objc_msgSend$updateMonitoredReasonsWithChannelState:completion:
CStrings:
+ "%{public}@ Cancelling existing periodic poll task"
+ "%{public}@ Failed to load configuration for sync. err=%{public}@"
+ "%{public}@ Not scheduling periodic poll because in-app message syncing is disabled. err=%{public}@"
+ "%{public}@ Not syncing because in-app message syncing is disabled"
+ "<%@ %p channelID=%@ contentType=%ld storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ lastProcessedGoLiveTimestamp=%@ registrationToken=%p observesAllLibraryAlbums=%d>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reasons=%@ expectedReleaseDate=%@ registrationToken=%@ lastProcessedGoLiveTimestamp=%@>"
+ "<%@ %p type=%@ pushMessages=%@ error=%@ channelIDs=%@ unsubscribeReason=%@ resubscribeReason=%@>"
+ "<%@: %p %@>"
+ "ICCloudAPNSChannelPushMessage - Could not create date from time=%{public}@, setting to %{public}@"
+ "ICCloudChannelRegistrationAvailability - scheduling bag fetch retry delay=%.0f"
+ "ICCloudClient - not unregistering; token is nil."
+ "ICCloudClientAPNSChannelManager - dispatching a lifecycle update channels=%{public}@ handlers=%lu"
+ "ICCloudClientAPNSChannelManager - dispatching updates channelID=%{public}@ ordered=%lu unordered=%lu"
+ "ICCloudClientAPNSChannelManager - feature disabled daemonChannels=%{public}@ localOnly=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to registerChannelState channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send registerChannelState; proxy error. channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to send unregisterChannelWithToken; proxy err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not able to unregisterChannelWithToken err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not delivering per-channel cancellation channelIDs=%{public}@; updates are paused"
+ "ICCloudClientAPNSChannelManager - not delivering pushes; feature is unavailable. channelCount=%lu"
+ "ICCloudClientAPNSChannelManager - not dispatching a lifecycle update channels=%{public}@; updates are paused"
+ "ICCloudClientAPNSChannelManager - not dispatching observe-all update; updates are paused."
+ "ICCloudClientAPNSChannelManager - not dispatching updates; no handlers on channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not registering; daemon minted no token channelID=%{public}@ err=%{public}@"
+ "ICCloudClientAPNSChannelManager - not resyncing after server setup; hasRegistrations=%{BOOL}u, updatesPaused=%{BOOL}u, _lastSetupCompletedResyncRequest=%{public}@"
+ "ICCloudClientAPNSChannelManager - not sending registerChannelState; no XPC connection. channelID=%{public}@"
+ "ICCloudClientAPNSChannelManager - not sending unregisterChannelWithToken; no XPC connection."
+ "ICCloudClientAPNSChannelManager - pausing updates is not allowed on this platform"
+ "ICCloudClientAPNSChannelManager - receiving updates channelID=%{public}@ count=%lu"
+ "ICCloudClientAPNSChannelManager - registered token=%{public}@ channelID=%{public}@ reason=%ld"
+ "ICCloudClientAPNSChannelManager - resyncing all existing registrations _pauseUpdates=%{BOOL}u."
+ "ICCloudClientAPNSChannelManager - sending registerChannelState state=%{public}@"
+ "ICCloudClientAPNSChannelManager - tearing down registrations tokens=%lu handlers=%lu notifyDaemon=%{BOOL}u paused=%{BOOL}u err=%{public}@"
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ failed to get remote object proxy: %{public}@"
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ service interrupted."
+ "ICCloudServiceStatusMonitor %{public}@: Connection to %{public}@ service invalidated."
+ "ICCloudServiceStatusMonitor %{public}@: Revocation of music user tokens completed"
+ "ICCloudServiceStatusMonitor %{public}@: Revocation of music user tokens completed error=%{public}@"
+ "ICCloudServiceStatusMonitor %{public}@: Revoking music user tokens DSID %{public}@"
+ "UpdatesPaused"
+ "com.apple.iTunesCloud.ICCloudClientAPNSChannelManager.deliveryQueue"
+ "inAppMessagesSyncEnabled"
+ "lastProcessedGoLiveTimestamp"
+ "registrationToken"
+ "v24@?0@\"ICCloudEntityUpdateRegistrationToken\"8@\"NSError\"16"
- "%{public}@: Revocation of music user tokens completed"
- "%{public}@: Revocation of music user tokens completed error=%{public}@"
- "%{public}@: Revoking music user tokens DSID %{public}@"
- "<%@ %p channelID=%@ contentType=%ld _storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
- "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ observesAllLibraryAlbums=%d>"
- "<%@ %p channelID=%@ entityType=%ld storeID=%lld reasons=%@ expectedReleaseDate=%@>"
- "<%@ %p type=%@ pushMessage=%@ error=%@ channelIDs=%@ unsubscribeReason=%@ resubscribeReason=%@>"
- "<%@: %p token=%@>"
- "Cannot unregister updates: token is nil."
- "ICCloudAPNSChannelPushMessage - not decoding push; missing storeID. payload=%{public}@"
- "ICCloudChannelRegistrationAvailability - scheduling bag fetch retry delay=%.0fs"
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
- "ICCloudClientAPNSChannelManager - not unregistering; feature is unavailable. channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - not unregistering; invalid arguments channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - receiving update pushMessage=%{public}@"
- "ICCloudClientAPNSChannelManager - registering configuration=%{public}@ token=%{public}@"
- "ICCloudClientAPNSChannelManager - registering token=%{public}@ channelID=%{public}@ reason=%ld isRegisteredChannel=%{BOOL}u isRegisteredReason=%{BOOL}u"
- "ICCloudClientAPNSChannelManager - sending updateMonitoredReasons state=%{public}@"
- "ICCloudClientAPNSChannelManager - tearing down registrations xpcUpdates=%lu handlers=%lu notifyDaemon=%{BOOL}u err=%{public}@"
- "ICCloudClientAPNSChannelManager - unregistering channel channelID=%{public}@ reason=%ld"
- "ICCloudClientAPNSChannelManager - unregistering tokens count=%lu channelID=%{public}@ reason=%ld"
```

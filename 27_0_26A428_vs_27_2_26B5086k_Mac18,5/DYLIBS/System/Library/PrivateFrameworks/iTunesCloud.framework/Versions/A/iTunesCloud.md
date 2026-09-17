## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud`

```diff

-4026.140.1.0.0
-  __TEXT.__text: 0x31c674
-  __TEXT.__objc_methlist: 0x18704
-  __TEXT.__const: 0x272c8
+4026.200.13.0.0
+  __TEXT.__text: 0x31cc4c
+  __TEXT.__objc_methlist: 0x187dc
+  __TEXT.__const: 0x272d8
   __TEXT.__dlopen_cstrs: 0x2ff
-  __TEXT.__gcc_except_tab: 0x2a20
-  __TEXT.__cstring: 0x1759e
-  __TEXT.__oslogstring: 0x21e4c
+  __TEXT.__gcc_except_tab: 0x2a3c
+  __TEXT.__cstring: 0x17640
+  __TEXT.__oslogstring: 0x21ed1
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x81f8
+  __TEXT.__unwind_info: 0x8218
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__const: 0x2bf8
   __DATA_CONST.__objc_classlist: 0xdd8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa458
+  __DATA_CONST.__objc_selrefs: 0xa4b0
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x1058
+  __DATA_CONST.__got: 0x1060
   __AUTH_CONST.__const: 0x17a90
-  __AUTH_CONST.__cfstring: 0x18900
-  __AUTH_CONST.__objc_const: 0x31610
+  __AUTH_CONST.__cfstring: 0x18960
+  __AUTH_CONST.__objc_const: 0x31768
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x990
   __AUTH.__objc_data: 0x5230
-  __DATA.__objc_ivar: 0x2490
+  __DATA.__objc_ivar: 0x24a4
   __DATA.__data: 0x2b78
   __DATA.__common: 0xa58
   __DATA_DIRTY.__objc_data: 0x3840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10134
-  Symbols:   21649
-  CStrings:  5431
+  Functions: 10149
+  Symbols:   21680
+  CStrings:  5435
 
Symbols:
+ +[ICCloudEntityUpdateRegistrationToken supportsSecureCoding]
+ -[ICCloudChannelRegistrationAvailability _updateCloudChannelConfigurationUsingBag:source:]
+ -[ICCloudChannelRegistrationAvailability registrationFetchEndOffsetSeconds]
+ -[ICCloudChannelRegistrationAvailability registrationFetchStartOffsetSeconds]
+ -[ICCloudClientAPNSChannelManager cloudChannelSubscriptionsRegistrationOffsetsChanged:]
+ -[ICCloudEntityUpdateRegistrationToken _initWithUUID:]
+ -[ICCloudEntityUpdateRegistrationToken encodeWithCoder:]
+ -[ICCloudEntityUpdateRegistrationToken initWithCoder:]
+ -[ICLibraryAuthServiceClientTokenProvider _handleAccountAuthenticationDidFinishNotification]
+ -[ICLibraryAuthServiceClientTokenProvider _shouldIncrementFailureCountForError:]
+ -[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]
+ -[ICLibraryAuthServiceClientTokenStatus allowRecoveryRefresh]
+ -[ICLibraryAuthServiceClientTokenStatus failureCount]
+ -[ICLibraryAuthServiceClientTokenStatus setAllowRecoveryRefresh:]
+ -[ICLibraryAuthServiceClientTokenStatus setFailureCount:]
+ -[ICMusicLibraryAuthTokenStatus failureCount]
+ -[ICMusicLibraryAuthTokenStatus setFailureCount:]
+ GCC_except_table1071
+ GCC_except_table1081
+ GCC_except_table1169
+ GCC_except_table1196
+ GCC_except_table1248
+ GCC_except_table1252
+ GCC_except_table1254
+ GCC_except_table1256
+ GCC_except_table1328
+ GCC_except_table1423
+ GCC_except_table1622
+ GCC_except_table1635
+ GCC_except_table1893
+ GCC_except_table2077
+ GCC_except_table2106
+ GCC_except_table2121
+ GCC_except_table2167
+ GCC_except_table2279
+ GCC_except_table2295
+ GCC_except_table2344
+ GCC_except_table2346
+ GCC_except_table2352
+ GCC_except_table2359
+ GCC_except_table2387
+ GCC_except_table2402
+ GCC_except_table2407
+ GCC_except_table2409
+ GCC_except_table2414
+ GCC_except_table2417
+ GCC_except_table2430
+ GCC_except_table2526
+ GCC_except_table2566
+ GCC_except_table2597
+ GCC_except_table2599
+ GCC_except_table2601
+ GCC_except_table2603
+ GCC_except_table2957
+ GCC_except_table3009
+ GCC_except_table3174
+ GCC_except_table3191
+ GCC_except_table3204
+ GCC_except_table3228
+ GCC_except_table3238
+ GCC_except_table3337
+ GCC_except_table3622
+ GCC_except_table3625
+ GCC_except_table3640
+ GCC_except_table3651
+ GCC_except_table3670
+ GCC_except_table3710
+ GCC_except_table3726
+ GCC_except_table3839
+ GCC_except_table4000
+ GCC_except_table4167
+ GCC_except_table4210
+ GCC_except_table4310
+ GCC_except_table4322
+ GCC_except_table4326
+ GCC_except_table4330
+ GCC_except_table4337
+ GCC_except_table4341
+ GCC_except_table4356
+ GCC_except_table4360
+ GCC_except_table4539
+ GCC_except_table4592
+ GCC_except_table4596
+ GCC_except_table4599
+ GCC_except_table4604
+ GCC_except_table4668
+ GCC_except_table4714
+ GCC_except_table4716
+ GCC_except_table4783
+ GCC_except_table4860
+ GCC_except_table497
+ GCC_except_table5022
+ GCC_except_table504
+ GCC_except_table5090
+ GCC_except_table5171
+ GCC_except_table5331
+ GCC_except_table5588
+ GCC_except_table5692
+ GCC_except_table5739
+ GCC_except_table5763
+ GCC_except_table5804
+ GCC_except_table5805
+ GCC_except_table5880
+ GCC_except_table5898
+ GCC_except_table6158
+ GCC_except_table6166
+ GCC_except_table6174
+ GCC_except_table6185
+ GCC_except_table6186
+ GCC_except_table6188
+ GCC_except_table6189
+ GCC_except_table6194
+ GCC_except_table6199
+ GCC_except_table6204
+ GCC_except_table6215
+ GCC_except_table6231
+ GCC_except_table6233
+ GCC_except_table6239
+ GCC_except_table6248
+ GCC_except_table6258
+ GCC_except_table6292
+ GCC_except_table6342
+ GCC_except_table6343
+ GCC_except_table6403
+ GCC_except_table6406
+ GCC_except_table6426
+ GCC_except_table6449
+ GCC_except_table6454
+ GCC_except_table6460
+ GCC_except_table6463
+ GCC_except_table6466
+ GCC_except_table6469
+ GCC_except_table6472
+ GCC_except_table6475
+ GCC_except_table6478
+ GCC_except_table6481
+ GCC_except_table6484
+ GCC_except_table6487
+ GCC_except_table6490
+ GCC_except_table6591
+ GCC_except_table6804
+ GCC_except_table6811
+ GCC_except_table6985
+ GCC_except_table6989
+ GCC_except_table6991
+ GCC_except_table7018
+ GCC_except_table7064
+ GCC_except_table7237
+ GCC_except_table7369
+ GCC_except_table7489
+ GCC_except_table7503
+ GCC_except_table7529
+ GCC_except_table7606
+ GCC_except_table7621
+ GCC_except_table7644
+ GCC_except_table7655
+ GCC_except_table7698
+ GCC_except_table7699
+ GCC_except_table7700
+ GCC_except_table7701
+ GCC_except_table7702
+ GCC_except_table7743
+ GCC_except_table7761
+ GCC_except_table7813
+ GCC_except_table7816
+ GCC_except_table7827
+ GCC_except_table7836
+ GCC_except_table786
+ GCC_except_table7883
+ GCC_except_table7976
+ GCC_except_table800
+ GCC_except_table8009
+ GCC_except_table8075
+ GCC_except_table8496
+ GCC_except_table8500
+ GCC_except_table8504
+ GCC_except_table852
+ GCC_except_table8526
+ GCC_except_table8533
+ GCC_except_table8546
+ GCC_except_table8551
+ GCC_except_table8586
+ GCC_except_table8589
+ GCC_except_table8660
+ GCC_except_table8705
+ GCC_except_table8753
+ GCC_except_table8782
+ GCC_except_table8787
+ GCC_except_table8789
+ GCC_except_table8791
+ GCC_except_table8824
+ GCC_except_table8956
+ GCC_except_table8964
+ GCC_except_table8969
+ GCC_except_table8984
+ GCC_except_table8992
+ GCC_except_table9036
+ GCC_except_table9187
+ GCC_except_table9191
+ GCC_except_table9193
+ GCC_except_table9231
+ GCC_except_table9234
+ GCC_except_table9241
+ GCC_except_table9244
+ GCC_except_table9489
+ GCC_except_table9499
+ GCC_except_table9557
+ GCC_except_table9644
+ GCC_except_table9649
+ GCC_except_table966
+ GCC_except_table977
+ GCC_except_table9889
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchEndOffsetSeconds
+ OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchStartOffsetSeconds
+ OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._allowRecoveryRefresh
+ OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._failureCount
+ OBJC_IVAR_$_ICMusicLibraryAuthTokenStatus._failureCount
+ _ICCloudChannelRegistrationEndOffsetSeconds
+ _ICCloudChannelRegistrationFetchEndOffsetSeconds
+ _ICCloudChannelRegistrationFetchStartOffsetSeconds
+ _ICCloudChannelRegistrationOffsetsDidChangeNotification
+ _ICCloudChannelRegistrationStartOffsetSeconds
+ __84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke
+ __OBJC_$_CLASS_PROP_LIST_ICCloudEntityUpdateRegistrationToken
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
+ ___block_descriptor_49_e8_32s40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
+ __handleAccountAuthenticationDidFinishNotification
+ _objc_msgSend$_handleAccountAuthenticationDidFinishNotification
+ _objc_msgSend$_initWithUUID:
+ _objc_msgSend$_shouldIncrementFailureCountForError:
+ _objc_msgSend$_updateCloudChannelConfigurationUsingBag:source:
+ _objc_msgSend$_updateEntriesForExternalAccountsChanges:
+ _objc_msgSend$allowRecoveryRefresh
+ _objc_msgSend$cloudChannelSubscriptionsRegistrationOffsetsChanged:
+ _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$musicChannelSubscriptionsFetchWindowEndSeconds
+ _objc_msgSend$musicChannelSubscriptionsFetchWindowStartSeconds
+ _objc_msgSend$registrationFetchEndOffsetSeconds
+ _objc_msgSend$registrationFetchStartOffsetSeconds
+ _objc_msgSend$setAllowRecoveryRefresh:
- -[ICCloudChannelRegistrationAvailability _commitAvailability:source:]
- -[ICCloudEntityUpdateRegistrationToken _initInternal]
- -[ICLibraryAuthServiceClientTokenProvider _shouldStopBackgroundRefreshForError:]
- -[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]
- -[ICMusicLibraryAuthTokenStatus setShouldExcludeFromBackgroundRefresh:]
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
- GCC_except_table2406
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
- GCC_except_table2952
- GCC_except_table3004
- GCC_except_table3168
- GCC_except_table3185
- GCC_except_table3198
- GCC_except_table3222
- GCC_except_table3232
- GCC_except_table3331
- GCC_except_table3610
- GCC_except_table3619
- GCC_except_table3634
- GCC_except_table3645
- GCC_except_table3664
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
- GCC_except_table6178
- GCC_except_table6179
- GCC_except_table6180
- GCC_except_table6181
- GCC_except_table6182
- GCC_except_table6192
- GCC_except_table6197
- GCC_except_table6208
- GCC_except_table6224
- GCC_except_table6226
- GCC_except_table6232
- GCC_except_table6241
- GCC_except_table6250
- GCC_except_table6284
- GCC_except_table6327
- GCC_except_table6334
- GCC_except_table6395
- GCC_except_table6398
- GCC_except_table6418
- GCC_except_table6441
- GCC_except_table6446
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
- __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke_2
- ___block_descriptor_41_e8_32r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
- ___block_descriptor_56_e8_32s40r48r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24l
- _objc_msgSend$_commitAvailability:source:
- _objc_msgSend$_initInternal
- _objc_msgSend$_shouldStopBackgroundRefreshForError:
- _objc_msgSend$_updateEntriesForAccountsChanges
- _objc_msgSend$setShouldExcludeFromBackgroundRefresh:
- _objc_msgSend$shouldExcludeFromBackgroundRefresh
CStrings:
+ "%{public}@ Allowing recovery refresh for account %{public}@"
+ "%{public}@ Clearing error state for account %{public}@ that was pending privacy acceptance"
+ "%{public}@ Not scheduling refresh timer since there are no accounts to schedule"
+ "<%@: %p token=%@>"
+ "<%@:%p result=%@ lastError=%@ lastUpdate='%@' failureCount=%lu allowRecoveryRefresh=%@"
+ "ICCloudChannelRegistrationAvailability - availability changed old=%{public}@ new=%{public}@, registrationStartOffset old=%lu, new=%lu,  registrationEndOffset old=%lu, new=%lu, source=%{public}@"
+ "ICCloudChannelRegistrationEndOffsetSeconds"
+ "ICCloudChannelRegistrationOffsetsDidChangeNotification"
+ "ICCloudChannelRegistrationStartOffsetSeconds"
+ "allowRecoveryRefresh"
+ "com.apple.StoreServices.authfinish"
- "%{public}@ Skipping background refresh of DSID %@. last error: %{public}@}"
- "<%@: %p>"
- "<%@:%p result=%@ lastError=%@ lastUpdate='%@' autoRefreshEnabled=%@>"
- "ICCloudChannelRegistrationAvailability - availability changed old=%{public}@ new=%{public}@ source=%{public}@"
- "ICCloudChannelRegistrationAvailability - not dispatching transition; no observer wired newState=%{public}@"
- "excludeFromBackgroundRefresh"
- "shouldExcludeFromBackgroundRefresh"
```

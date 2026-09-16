## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4026.110.1.0.0
-  __TEXT.__text: 0x3c14e4
-  __TEXT.__objc_methlist: 0x187cc
-  __TEXT.__const: 0x225e8
+4026.200.13.0.0
+  __TEXT.__text: 0x3c1a5c
+  __TEXT.__objc_methlist: 0x188a4
+  __TEXT.__const: 0x225f8
   __TEXT.__dlopen_cstrs: 0x4cf
-  __TEXT.__gcc_except_tab: 0x2b50
-  __TEXT.__cstring: 0x17a42
-  __TEXT.__oslogstring: 0x22336
+  __TEXT.__gcc_except_tab: 0x2b6c
+  __TEXT.__cstring: 0x17ae4
+  __TEXT.__oslogstring: 0x223bb
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x8350
+  __TEXT.__unwind_info: 0x8378
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7448
+  __DATA_CONST.__const: 0x7458
   __DATA_CONST.__objc_classlist: 0xdd0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa570
+  __DATA_CONST.__objc_selrefs: 0xa5c8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x1088
+  __DATA_CONST.__got: 0x1090
   __AUTH_CONST.__const: 0x18638
-  __AUTH_CONST.__cfstring: 0x18a80
-  __AUTH_CONST.__objc_const: 0x31728
+  __AUTH_CONST.__cfstring: 0x18ae0
+  __AUTH_CONST.__objc_const: 0x31880
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0xa68
   __AUTH.__objc_data: 0x5640
-  __DATA.__objc_ivar: 0x24a8
+  __DATA.__objc_ivar: 0x24bc
   __DATA.__data: 0x31a0
   __DATA.__common: 0xb88
   __DATA_DIRTY.__objc_data: 0x33e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10164
-  Symbols:   21444
-  CStrings:  5496
+  Functions: 10179
+  Symbols:   21475
+  CStrings:  5500
 
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
+ GCC_except_table1022
+ GCC_except_table1030
+ GCC_except_table1118
+ GCC_except_table1144
+ GCC_except_table1196
+ GCC_except_table1200
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1276
+ GCC_except_table1371
+ GCC_except_table1570
+ GCC_except_table1583
+ GCC_except_table1841
+ GCC_except_table2025
+ GCC_except_table2054
+ GCC_except_table2069
+ GCC_except_table2109
+ GCC_except_table2221
+ GCC_except_table2236
+ GCC_except_table2285
+ GCC_except_table2287
+ GCC_except_table2293
+ GCC_except_table2300
+ GCC_except_table2328
+ GCC_except_table2343
+ GCC_except_table2348
+ GCC_except_table2350
+ GCC_except_table2355
+ GCC_except_table2358
+ GCC_except_table2371
+ GCC_except_table2448
+ GCC_except_table2457
+ GCC_except_table2460
+ GCC_except_table2463
+ GCC_except_table2466
+ GCC_except_table2468
+ GCC_except_table2479
+ GCC_except_table2481
+ GCC_except_table2498
+ GCC_except_table2537
+ GCC_except_table2568
+ GCC_except_table2570
+ GCC_except_table2572
+ GCC_except_table2574
+ GCC_except_table2928
+ GCC_except_table2973
+ GCC_except_table3121
+ GCC_except_table3138
+ GCC_except_table3148
+ GCC_except_table3172
+ GCC_except_table3182
+ GCC_except_table3280
+ GCC_except_table3559
+ GCC_except_table3563
+ GCC_except_table3566
+ GCC_except_table3581
+ GCC_except_table3592
+ GCC_except_table3611
+ GCC_except_table3651
+ GCC_except_table3665
+ GCC_except_table3778
+ GCC_except_table3938
+ GCC_except_table4103
+ GCC_except_table4145
+ GCC_except_table4245
+ GCC_except_table4257
+ GCC_except_table4261
+ GCC_except_table4265
+ GCC_except_table4272
+ GCC_except_table4276
+ GCC_except_table4291
+ GCC_except_table4294
+ GCC_except_table4473
+ GCC_except_table4525
+ GCC_except_table4529
+ GCC_except_table4532
+ GCC_except_table4537
+ GCC_except_table4601
+ GCC_except_table4647
+ GCC_except_table4649
+ GCC_except_table468
+ GCC_except_table4716
+ GCC_except_table473
+ GCC_except_table4793
+ GCC_except_table4881
+ GCC_except_table4964
+ GCC_except_table5032
+ GCC_except_table5113
+ GCC_except_table5273
+ GCC_except_table5530
+ GCC_except_table5635
+ GCC_except_table5683
+ GCC_except_table5707
+ GCC_except_table5748
+ GCC_except_table5749
+ GCC_except_table5822
+ GCC_except_table5840
+ GCC_except_table6100
+ GCC_except_table6108
+ GCC_except_table6116
+ GCC_except_table6127
+ GCC_except_table6128
+ GCC_except_table6130
+ GCC_except_table6131
+ GCC_except_table6136
+ GCC_except_table6141
+ GCC_except_table6146
+ GCC_except_table6157
+ GCC_except_table6172
+ GCC_except_table6174
+ GCC_except_table6180
+ GCC_except_table6189
+ GCC_except_table6199
+ GCC_except_table6233
+ GCC_except_table6265
+ GCC_except_table6285
+ GCC_except_table6286
+ GCC_except_table6346
+ GCC_except_table6349
+ GCC_except_table6363
+ GCC_except_table6386
+ GCC_except_table6391
+ GCC_except_table6397
+ GCC_except_table6400
+ GCC_except_table6403
+ GCC_except_table6406
+ GCC_except_table6409
+ GCC_except_table6412
+ GCC_except_table6415
+ GCC_except_table6418
+ GCC_except_table6421
+ GCC_except_table6424
+ GCC_except_table6427
+ GCC_except_table6528
+ GCC_except_table6742
+ GCC_except_table6749
+ GCC_except_table6923
+ GCC_except_table6927
+ GCC_except_table6929
+ GCC_except_table6956
+ GCC_except_table7002
+ GCC_except_table7175
+ GCC_except_table7307
+ GCC_except_table7427
+ GCC_except_table7439
+ GCC_except_table7462
+ GCC_except_table7540
+ GCC_except_table755
+ GCC_except_table7555
+ GCC_except_table7578
+ GCC_except_table7589
+ GCC_except_table7633
+ GCC_except_table7634
+ GCC_except_table7635
+ GCC_except_table7636
+ GCC_except_table7637
+ GCC_except_table767
+ GCC_except_table7678
+ GCC_except_table7696
+ GCC_except_table7748
+ GCC_except_table7751
+ GCC_except_table7760
+ GCC_except_table7767
+ GCC_except_table7814
+ GCC_except_table7907
+ GCC_except_table7940
+ GCC_except_table7998
+ GCC_except_table7999
+ GCC_except_table8012
+ GCC_except_table809
+ GCC_except_table8434
+ GCC_except_table8438
+ GCC_except_table8442
+ GCC_except_table8464
+ GCC_except_table8482
+ GCC_except_table8487
+ GCC_except_table8522
+ GCC_except_table8525
+ GCC_except_table8596
+ GCC_except_table8641
+ GCC_except_table8689
+ GCC_except_table8718
+ GCC_except_table8723
+ GCC_except_table8725
+ GCC_except_table8727
+ GCC_except_table8759
+ GCC_except_table8891
+ GCC_except_table8899
+ GCC_except_table8904
+ GCC_except_table8919
+ GCC_except_table8927
+ GCC_except_table8971
+ GCC_except_table9120
+ GCC_except_table9124
+ GCC_except_table9126
+ GCC_except_table9164
+ GCC_except_table9167
+ GCC_except_table9174
+ GCC_except_table9177
+ GCC_except_table921
+ GCC_except_table930
+ GCC_except_table9422
+ GCC_except_table9432
+ GCC_except_table9490
+ GCC_except_table9577
+ GCC_except_table9582
+ GCC_except_table9822
+ _ICCloudChannelRegistrationEndOffsetSeconds
+ _ICCloudChannelRegistrationFetchEndOffsetSeconds
+ _ICCloudChannelRegistrationFetchStartOffsetSeconds
+ _ICCloudChannelRegistrationOffsetsDidChangeNotification
+ _ICCloudChannelRegistrationStartOffsetSeconds
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchEndOffsetSeconds
+ _OBJC_IVAR_$_ICCloudChannelRegistrationAvailability._registrationFetchStartOffsetSeconds
+ _OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._allowRecoveryRefresh
+ _OBJC_IVAR_$_ICLibraryAuthServiceClientTokenStatus._failureCount
+ _OBJC_IVAR_$_ICMusicLibraryAuthTokenStatus._failureCount
+ __OBJC_$_CLASS_PROP_LIST_ICCloudEntityUpdateRegistrationToken
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke
+ ___84-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForExternalAccountsChanges:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24lr32l8r40l8
+ ___block_descriptor_49_e8_32s40r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24ls32l8r40l8
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
- GCC_except_table1021
- GCC_except_table1029
- GCC_except_table1117
- GCC_except_table1143
- GCC_except_table1195
- GCC_except_table1199
- GCC_except_table1201
- GCC_except_table1203
- GCC_except_table1275
- GCC_except_table1370
- GCC_except_table1569
- GCC_except_table1582
- GCC_except_table1840
- GCC_except_table2024
- GCC_except_table2053
- GCC_except_table2068
- GCC_except_table2108
- GCC_except_table2220
- GCC_except_table2235
- GCC_except_table2284
- GCC_except_table2286
- GCC_except_table2292
- GCC_except_table2299
- GCC_except_table2327
- GCC_except_table2342
- GCC_except_table2347
- GCC_except_table2349
- GCC_except_table2354
- GCC_except_table2357
- GCC_except_table2370
- GCC_except_table2447
- GCC_except_table2456
- GCC_except_table2459
- GCC_except_table2462
- GCC_except_table2465
- GCC_except_table2467
- GCC_except_table2478
- GCC_except_table2480
- GCC_except_table2497
- GCC_except_table2536
- GCC_except_table2567
- GCC_except_table2569
- GCC_except_table2571
- GCC_except_table2573
- GCC_except_table2923
- GCC_except_table2968
- GCC_except_table3115
- GCC_except_table3132
- GCC_except_table3142
- GCC_except_table3166
- GCC_except_table3176
- GCC_except_table3274
- GCC_except_table3553
- GCC_except_table3557
- GCC_except_table3560
- GCC_except_table3575
- GCC_except_table3586
- GCC_except_table3605
- GCC_except_table3645
- GCC_except_table3659
- GCC_except_table3772
- GCC_except_table3932
- GCC_except_table4097
- GCC_except_table4139
- GCC_except_table4239
- GCC_except_table4247
- GCC_except_table4249
- GCC_except_table4251
- GCC_except_table4266
- GCC_except_table4270
- GCC_except_table4285
- GCC_except_table4288
- GCC_except_table4467
- GCC_except_table4519
- GCC_except_table4523
- GCC_except_table4526
- GCC_except_table4531
- GCC_except_table4595
- GCC_except_table4637
- GCC_except_table4641
- GCC_except_table467
- GCC_except_table4710
- GCC_except_table472
- GCC_except_table4787
- GCC_except_table4875
- GCC_except_table4958
- GCC_except_table5026
- GCC_except_table5107
- GCC_except_table5267
- GCC_except_table5524
- GCC_except_table5629
- GCC_except_table5677
- GCC_except_table5701
- GCC_except_table5742
- GCC_except_table5743
- GCC_except_table5816
- GCC_except_table5834
- GCC_except_table6094
- GCC_except_table6101
- GCC_except_table6109
- GCC_except_table6120
- GCC_except_table6121
- GCC_except_table6122
- GCC_except_table6123
- GCC_except_table6124
- GCC_except_table6134
- GCC_except_table6139
- GCC_except_table6150
- GCC_except_table6165
- GCC_except_table6167
- GCC_except_table6173
- GCC_except_table6182
- GCC_except_table6191
- GCC_except_table6225
- GCC_except_table6257
- GCC_except_table6270
- GCC_except_table6277
- GCC_except_table6338
- GCC_except_table6341
- GCC_except_table6355
- GCC_except_table6378
- GCC_except_table6383
- GCC_except_table6389
- GCC_except_table6392
- GCC_except_table6395
- GCC_except_table6398
- GCC_except_table6401
- GCC_except_table6404
- GCC_except_table6407
- GCC_except_table6410
- GCC_except_table6413
- GCC_except_table6416
- GCC_except_table6419
- GCC_except_table6520
- GCC_except_table6734
- GCC_except_table6741
- GCC_except_table6915
- GCC_except_table6919
- GCC_except_table6921
- GCC_except_table6948
- GCC_except_table6994
- GCC_except_table7167
- GCC_except_table7299
- GCC_except_table7419
- GCC_except_table7431
- GCC_except_table7454
- GCC_except_table7532
- GCC_except_table754
- GCC_except_table7547
- GCC_except_table7570
- GCC_except_table7581
- GCC_except_table7625
- GCC_except_table7626
- GCC_except_table7627
- GCC_except_table7628
- GCC_except_table7629
- GCC_except_table766
- GCC_except_table7670
- GCC_except_table7688
- GCC_except_table7740
- GCC_except_table7743
- GCC_except_table7752
- GCC_except_table7759
- GCC_except_table7806
- GCC_except_table7896
- GCC_except_table7929
- GCC_except_table7987
- GCC_except_table7988
- GCC_except_table8001
- GCC_except_table808
- GCC_except_table8423
- GCC_except_table8427
- GCC_except_table8431
- GCC_except_table8453
- GCC_except_table8460
- GCC_except_table8476
- GCC_except_table8511
- GCC_except_table8514
- GCC_except_table8585
- GCC_except_table8630
- GCC_except_table8678
- GCC_except_table8707
- GCC_except_table8712
- GCC_except_table8714
- GCC_except_table8716
- GCC_except_table8748
- GCC_except_table8880
- GCC_except_table8888
- GCC_except_table8893
- GCC_except_table8908
- GCC_except_table8916
- GCC_except_table8960
- GCC_except_table9109
- GCC_except_table9113
- GCC_except_table9115
- GCC_except_table9153
- GCC_except_table9156
- GCC_except_table9163
- GCC_except_table9166
- GCC_except_table920
- GCC_except_table929
- GCC_except_table9407
- GCC_except_table9417
- GCC_except_table9475
- GCC_except_table9562
- GCC_except_table9567
- GCC_except_table9807
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke_2
- ___block_descriptor_41_e8_32r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24lr32l8
- ___block_descriptor_56_e8_32s40r48r_e64_v32?0"NSNumber"8"ICLibraryAuthServiceClientTokenStatus"16^B24lr40l8r48l8s32l8
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

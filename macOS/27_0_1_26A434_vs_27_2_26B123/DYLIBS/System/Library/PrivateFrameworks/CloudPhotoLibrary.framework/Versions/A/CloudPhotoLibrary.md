## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x1e6a04
-  __TEXT.__objc_methlist: 0x15d44
+916.58.114.0.0
+  __TEXT.__text: 0x1e6f30
+  __TEXT.__objc_methlist: 0x15cf4
   __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4d80
-  __TEXT.__oslogstring: 0x16c0c
-  __TEXT.__cstring: 0x18d42
-  __TEXT.__unwind_info: 0x6db8
+  __TEXT.__gcc_except_tab: 0x4d4c
+  __TEXT.__oslogstring: 0x16c84
+  __TEXT.__cstring: 0x18e39
+  __TEXT.__ustring: 0xc
+  __TEXT.__unwind_info: 0x6dc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92d0
+  __DATA_CONST.__objc_selrefs: 0x92c0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x948
-  __DATA_CONST.__objc_arraydata: 0x1448
+  __DATA_CONST.__objc_arraydata: 0x14c8
   __DATA_CONST.__got: 0xb40
   __AUTH_CONST.__const: 0x9840
-  __AUTH_CONST.__cfstring: 0x17ae0
-  __AUTH_CONST.__objc_const: 0x23a08
-  __AUTH_CONST.__objc_intobj: 0x768
+  __AUTH_CONST.__cfstring: 0x17c60
+  __AUTH_CONST.__objc_const: 0x23ac8
+  __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_floatobj: 0x50
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1c28
-  __DATA.__data: 0x1610
-  __DATA.__bss: 0xb50
+  __DATA.__objc_ivar: 0x1c3c
+  __DATA.__data: 0x120
+  __DATA.__bss: 0xb40
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x62c0
-  __DATA_DIRTY.__bss: 0x430
+  __DATA_DIRTY.__objc_data: 0x6310
+  __DATA_DIRTY.__data: 0x14f0
+  __DATA_DIRTY.__bss: 0x440
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9917
+  Functions: 9920
   Symbols:   19365
-  CStrings:  5118
+  CStrings:  5130
 
Symbols:
+ +[CPLShare scopeTypeForShareURL:]
+ -[CPLEngineLibrary containerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLEngineLibrary setContainerHasBeenWipedDueToEncryptedDataReset:]
+ -[CPLEngineScheduler _disableSynchronizationBecauseContainerHasBeenWipedDueToEncryptedDataResetLocked]
+ -[CPLEngineScheduler noteContainerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLNetworkState isSufficientlyDifferentFromNetworkState:]
+ -[CPLPostChange lastUserEditedDate]
+ -[CPLPostChange setLastUserEditedDate:]
+ -[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:localChanges:]
+ -[CPLPushToTransportScopeTask _updateContributors:localChanges:]
+ -[CPLStatus containerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLStatus setContainerHasBeenWipedDueToEncryptedDataReset:]
+ -[CPLSyncSession report:]
+ -[CPLSyncSession reportCount:direction:]
+ -[CPLTextCommentChange lastUserEditedDate]
+ -[CPLTextCommentChange setLastUserEditedDate:]
+ -[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]
+ GCC_except_table1161
+ GCC_except_table1237
+ GCC_except_table1291
+ GCC_except_table1296
+ GCC_except_table1335
+ GCC_except_table1357
+ GCC_except_table1531
+ GCC_except_table1580
+ GCC_except_table1586
+ GCC_except_table1593
+ GCC_except_table1603
+ GCC_except_table1610
+ GCC_except_table1613
+ GCC_except_table1616
+ GCC_except_table1628
+ GCC_except_table1710
+ GCC_except_table1798
+ GCC_except_table2050
+ GCC_except_table2060
+ GCC_except_table2288
+ GCC_except_table2289
+ GCC_except_table2292
+ GCC_except_table2299
+ GCC_except_table2303
+ GCC_except_table2330
+ GCC_except_table2337
+ GCC_except_table2347
+ GCC_except_table2350
+ GCC_except_table2539
+ GCC_except_table2640
+ GCC_except_table2706
+ GCC_except_table2714
+ GCC_except_table2755
+ GCC_except_table2847
+ GCC_except_table2854
+ GCC_except_table3007
+ GCC_except_table3096
+ GCC_except_table3388
+ GCC_except_table3390
+ GCC_except_table3495
+ GCC_except_table3506
+ GCC_except_table3561
+ GCC_except_table3563
+ GCC_except_table3676
+ GCC_except_table3700
+ GCC_except_table3800
+ GCC_except_table3806
+ GCC_except_table3967
+ GCC_except_table4016
+ GCC_except_table4261
+ GCC_except_table4350
+ GCC_except_table4352
+ GCC_except_table4361
+ GCC_except_table4567
+ GCC_except_table4581
+ GCC_except_table4742
+ GCC_except_table4772
+ GCC_except_table4809
+ GCC_except_table4827
+ GCC_except_table4838
+ GCC_except_table4846
+ GCC_except_table4848
+ GCC_except_table4862
+ GCC_except_table4867
+ GCC_except_table5241
+ GCC_except_table5275
+ GCC_except_table5277
+ GCC_except_table5303
+ GCC_except_table5437
+ GCC_except_table5447
+ GCC_except_table5508
+ GCC_except_table5686
+ GCC_except_table5694
+ GCC_except_table5784
+ GCC_except_table5788
+ GCC_except_table5794
+ GCC_except_table5802
+ GCC_except_table5817
+ GCC_except_table5824
+ GCC_except_table5871
+ GCC_except_table5931
+ GCC_except_table5942
+ GCC_except_table5945
+ GCC_except_table5994
+ GCC_except_table6006
+ GCC_except_table6158
+ GCC_except_table6200
+ GCC_except_table6210
+ GCC_except_table6211
+ GCC_except_table6270
+ GCC_except_table6273
+ GCC_except_table6360
+ GCC_except_table6376
+ GCC_except_table6399
+ GCC_except_table6417
+ GCC_except_table6579
+ GCC_except_table6607
+ GCC_except_table6650
+ GCC_except_table6673
+ GCC_except_table6707
+ GCC_except_table6719
+ GCC_except_table6748
+ GCC_except_table6775
+ GCC_except_table6779
+ GCC_except_table6805
+ GCC_except_table6837
+ GCC_except_table6878
+ GCC_except_table6943
+ GCC_except_table6969
+ GCC_except_table6973
+ GCC_except_table6982
+ GCC_except_table7000
+ GCC_except_table7018
+ GCC_except_table7027
+ GCC_except_table7028
+ GCC_except_table7042
+ GCC_except_table7100
+ GCC_except_table7226
+ GCC_except_table7241
+ GCC_except_table7244
+ GCC_except_table7371
+ GCC_except_table7375
+ GCC_except_table7379
+ GCC_except_table7382
+ GCC_except_table7756
+ GCC_except_table7802
+ GCC_except_table7804
+ GCC_except_table7825
+ GCC_except_table7839
+ GCC_except_table7843
+ GCC_except_table7851
+ GCC_except_table7854
+ GCC_except_table7874
+ GCC_except_table7881
+ GCC_except_table7904
+ GCC_except_table7939
+ GCC_except_table7970
+ GCC_except_table7981
+ GCC_except_table8003
+ GCC_except_table8006
+ GCC_except_table8008
+ GCC_except_table8010
+ GCC_except_table803
+ GCC_except_table8041
+ GCC_except_table808
+ GCC_except_table8092
+ GCC_except_table814
+ GCC_except_table8236
+ GCC_except_table8259
+ GCC_except_table8289
+ GCC_except_table8440
+ GCC_except_table8442
+ GCC_except_table845
+ GCC_except_table8472
+ GCC_except_table8481
+ GCC_except_table8486
+ GCC_except_table8502
+ GCC_except_table8517
+ GCC_except_table8529
+ GCC_except_table8534
+ GCC_except_table861
+ GCC_except_table8618
+ GCC_except_table8707
+ GCC_except_table8766
+ GCC_except_table8847
+ GCC_except_table8856
+ GCC_except_table8870
+ GCC_except_table8889
+ GCC_except_table8910
+ GCC_except_table892
+ GCC_except_table8957
+ GCC_except_table8961
+ GCC_except_table8965
+ GCC_except_table9049
+ GCC_except_table912
+ GCC_except_table918
+ GCC_except_table927
+ GCC_except_table938
+ GCC_except_table954
+ OBJC_IVAR_$_CPLEngineScheduler._lastSessionFailedBecauseOfNetwork
+ OBJC_IVAR_$_CPLPostChange._lastUserEditedDate
+ OBJC_IVAR_$_CPLPushToTransportScopeTask._cloudCache
+ OBJC_IVAR_$_CPLPushToTransportScopeTask._idMapping
+ OBJC_IVAR_$_CPLTextCommentChange._lastUserEditedDate
+ OBJC_IVAR_$_CPLUploadPushedChangesTask._hasNotedScopeNeedsToPullFromTransport
+ _CPLRecordModificationDatePrecision
+ __64-[CPLPushToTransportScopeTask _updateContributors:localChanges:]_block_invoke
+ __82-[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]_block_invoke
+ ___57-[CPLStatus containerHasBeenWipedDueToEncryptedDataReset]_block_invoke
+ ___61-[CPLStatus setContainerHasBeenWipedDueToEncryptedDataReset:]_block_invoke
+ ___64-[CPLPushToTransportScopeTask _updateContributors:localChanges:]_block_invoke
+ ___64-[CPLPushToTransportScopeTask _updateContributors:localChanges:]_block_invoke_2
+ ___70-[CPLEngineScheduler noteContainerHasBeenWipedDueToEncryptedDataReset]_block_invoke
+ ___78-[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:localChanges:]_block_invoke
+ ___82-[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]_block_invoke
+ ___block_descriptor_72_e8_32s40r48r56r64r_e35_v16?0"CPLEngineStoreTransaction"8l
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e35_v16?0"CPLEngineStoreTransaction"8l
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e35_v16?0"CPLEngineStoreTransaction"8l
+ _objc_msgSend$_contributorsUpdatesInTransaction:localChanges:
+ _objc_msgSend$_updateContributors:localChanges:
+ _objc_msgSend$containerHasBeenWipedDueToEncryptedDataReset
+ _objc_msgSend$isSufficientlyDifferentFromNetworkState:
+ _objc_msgSend$noteContainerHasBeenWipedDueToEncryptedDataReset
+ _objc_msgSend$reportCount:direction:
+ _objc_msgSend$setContainerHasBeenWipedDueToEncryptedDataReset:
+ _objc_msgSend$setUpdateSharingContributorUserIdentifiers:
- -[CPLEngineLibrary containerHasBeenWiped]
- -[CPLEngineLibrary setContainerHasBeenWiped:]
- -[CPLEngineScheduler _disableSynchronizationBecauseContainerHasBeenWipedLocked]
- -[CPLEngineScheduler noteContainerHasBeenWiped]
- -[CPLNetworkState isSufficentlyDifferentFromNetworkState:]
- -[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:]
- -[CPLPushToTransportScopeTask _updateContributors:]
- -[CPLStatus containerHasBeenWiped]
- -[CPLStatus setContainerHasBeenWiped:]
- -[CPLUploadPushedChangesTask _canUseOverQuotaRule]
- -[CPLUploadPushedChangesTask _checkForRecordExistence]
- -[CPLUploadPushedChangesTask _copyResourceChangeFromChange:toChange:fingerprintScheme:error:]
- -[CPLUploadPushedChangesTask _noteSuccessfulUpdateInTransaction:]
- -[CPLUploadPushedChangesTask _reenqueueExtractedBatchWithRejectedRecords:extractedBatch:error:]
- GCC_except_table1159
- GCC_except_table1235
- GCC_except_table1289
- GCC_except_table1294
- GCC_except_table1333
- GCC_except_table1353
- GCC_except_table1529
- GCC_except_table1578
- GCC_except_table1582
- GCC_except_table1589
- GCC_except_table1599
- GCC_except_table1608
- GCC_except_table1611
- GCC_except_table1614
- GCC_except_table1620
- GCC_except_table1708
- GCC_except_table1796
- GCC_except_table2048
- GCC_except_table2058
- GCC_except_table2286
- GCC_except_table2287
- GCC_except_table2290
- GCC_except_table2297
- GCC_except_table2301
- GCC_except_table2328
- GCC_except_table2335
- GCC_except_table2345
- GCC_except_table2348
- GCC_except_table2537
- GCC_except_table2638
- GCC_except_table2704
- GCC_except_table2712
- GCC_except_table2753
- GCC_except_table2845
- GCC_except_table2852
- GCC_except_table3005
- GCC_except_table3094
- GCC_except_table3384
- GCC_except_table3386
- GCC_except_table3491
- GCC_except_table3502
- GCC_except_table3557
- GCC_except_table3559
- GCC_except_table3672
- GCC_except_table3696
- GCC_except_table3790
- GCC_except_table3796
- GCC_except_table3963
- GCC_except_table4012
- GCC_except_table4257
- GCC_except_table4342
- GCC_except_table4348
- GCC_except_table4357
- GCC_except_table4562
- GCC_except_table4576
- GCC_except_table4737
- GCC_except_table4767
- GCC_except_table4804
- GCC_except_table4822
- GCC_except_table4835
- GCC_except_table4843
- GCC_except_table4845
- GCC_except_table4859
- GCC_except_table4861
- GCC_except_table5238
- GCC_except_table5272
- GCC_except_table5274
- GCC_except_table5300
- GCC_except_table5434
- GCC_except_table5444
- GCC_except_table5502
- GCC_except_table5683
- GCC_except_table5693
- GCC_except_table5785
- GCC_except_table5789
- GCC_except_table5795
- GCC_except_table5803
- GCC_except_table5819
- GCC_except_table5825
- GCC_except_table5872
- GCC_except_table5929
- GCC_except_table5936
- GCC_except_table5941
- GCC_except_table5988
- GCC_except_table6004
- GCC_except_table6156
- GCC_except_table6198
- GCC_except_table6208
- GCC_except_table6209
- GCC_except_table6268
- GCC_except_table6271
- GCC_except_table6356
- GCC_except_table6374
- GCC_except_table6397
- GCC_except_table6413
- GCC_except_table6575
- GCC_except_table6603
- GCC_except_table6646
- GCC_except_table6668
- GCC_except_table6702
- GCC_except_table6714
- GCC_except_table6743
- GCC_except_table6770
- GCC_except_table6774
- GCC_except_table6800
- GCC_except_table6832
- GCC_except_table6873
- GCC_except_table6938
- GCC_except_table6964
- GCC_except_table6968
- GCC_except_table6977
- GCC_except_table6995
- GCC_except_table7008
- GCC_except_table7022
- GCC_except_table7023
- GCC_except_table7037
- GCC_except_table7095
- GCC_except_table7221
- GCC_except_table7235
- GCC_except_table7238
- GCC_except_table7365
- GCC_except_table7367
- GCC_except_table7369
- GCC_except_table7376
- GCC_except_table7750
- GCC_except_table7792
- GCC_except_table7796
- GCC_except_table7813
- GCC_except_table7827
- GCC_except_table7837
- GCC_except_table7845
- GCC_except_table7848
- GCC_except_table7868
- GCC_except_table7875
- GCC_except_table7898
- GCC_except_table7933
- GCC_except_table7964
- GCC_except_table7975
- GCC_except_table799
- GCC_except_table7997
- GCC_except_table8000
- GCC_except_table8002
- GCC_except_table8004
- GCC_except_table8035
- GCC_except_table804
- GCC_except_table8086
- GCC_except_table810
- GCC_except_table821
- GCC_except_table8230
- GCC_except_table8253
- GCC_except_table8283
- GCC_except_table8433
- GCC_except_table8435
- GCC_except_table8465
- GCC_except_table8474
- GCC_except_table8479
- GCC_except_table8495
- GCC_except_table851
- GCC_except_table8510
- GCC_except_table8522
- GCC_except_table8527
- GCC_except_table8611
- GCC_except_table870
- GCC_except_table8700
- GCC_except_table8759
- GCC_except_table8837
- GCC_except_table8852
- GCC_except_table8874
- GCC_except_table8880
- GCC_except_table8899
- GCC_except_table8909
- GCC_except_table8951
- GCC_except_table8958
- GCC_except_table8962
- GCC_except_table9046
- GCC_except_table910
- GCC_except_table916
- GCC_except_table925
- GCC_except_table936
- GCC_except_table952
- OBJC_IVAR_$_CPLUploadPushedChangesTask._hasPushedSomeChanges
- __51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke
- ___34-[CPLStatus containerHasBeenWiped]_block_invoke
- ___38-[CPLStatus setContainerHasBeenWiped:]_block_invoke
- ___47-[CPLEngineScheduler noteContainerHasBeenWiped]_block_invoke
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke_2
- ___65-[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:]_block_invoke
- ___93-[CPLUploadPushedChangesTask _copyResourceChangeFromChange:toChange:fingerprintScheme:error:]_block_invoke
- ___block_descriptor_64_e8_32s40r48r56r_e35_v16?0"CPLEngineStoreTransaction"8l
- ___block_descriptor_72_e8_32s40s48r56r64r_e35_v16?0"CPLEngineStoreTransaction"8l
- ___block_descriptor_72_e8_32s40s48s56r64r_e64_B48?0"CPLRecordChange"8"CPLRecordChange"16"NSString"24:32:40l
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e35_v16?0"CPLEngineStoreTransaction"8l
- __os_feature_enabled_impl
- _objc_msgSend$_canUseOverQuotaRule
- _objc_msgSend$_checkForRecordExistence
- _objc_msgSend$_checkPrioritiesWithFetchCache:
- _objc_msgSend$_clearUploadBatch
- _objc_msgSend$_contributorsUpdatesInTransaction:
- _objc_msgSend$_deleteGeneratedResourcesAfterError:
- _objc_msgSend$_discardUploadedExtractedBatch:error:
- _objc_msgSend$_extractAndUploadOneBatch
- _objc_msgSend$_generateNeededDerivativesWithFetchCache:fingerprintContext:
- _objc_msgSend$_prepareUploadBatch
- _objc_msgSend$_reenqueueExtractedBatchWithRejectedRecords:extractedBatch:error:
- _objc_msgSend$_updateContributors:
- _objc_msgSend$containerHasBeenWiped
- _objc_msgSend$isSufficentlyDifferentFromNetworkState:
- _objc_msgSend$noteContainerHasBeenWiped
- _objc_msgSend$setContainerHasBeenWiped:
CStrings:
+ " - expiringState: %@, expiryDate: %@, viewingMode: %@, keyAsset: %@, thumbnailImageDataLength: %lu"
+ " - expiringState: %@, viewingMode: %@, keyAsset: %@, thumbnailImageDataLength: %lu"
+ "CloudPhotoLibrary-916.58.114"
+ "Ignoring contributors update %@"
+ "Notified that network state did change but last session did not fail because of network"
+ "album"
+ "container has been wiped due to encrypted data reset"
+ "containerHasBeenWipedDueToEncryptedDataReset"
+ "lastUserEditedDate"
+ "lued"
+ "photos"
+ "photos.icloud.com"
+ "photos_links"
+ "photos_sharedcollections"
+ "photos_sharing"
+ "shared"
+ "shared_library"
+ "⬆️"
+ "⬇️"
- " - expiringState: %@, expiryDate: %@, viewingMode: %@"
- " - expiringState: %@, viewingMode: %@"
- "CloudPhotoLibrary-911.0.134"
- "Photos"
- "SharedCollections"
- "container has been wiped"
- "containerHasBeenWiped"
```

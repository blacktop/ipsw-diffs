## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x1ddb3c
-  __TEXT.__objc_methlist: 0x15d44
+916.41.100.0.0
+  __TEXT.__text: 0x1dde84
+  __TEXT.__objc_methlist: 0x15cac
   __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4d80
-  __TEXT.__oslogstring: 0x16c0c
-  __TEXT.__cstring: 0x18d42
-  __TEXT.__unwind_info: 0x8680
+  __TEXT.__gcc_except_tab: 0x4d4c
+  __TEXT.__oslogstring: 0x16c84
+  __TEXT.__cstring: 0x18e21
+  __TEXT.__unwind_info: 0x8670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92d0
+  __DATA_CONST.__objc_selrefs: 0x92a0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x948
-  __DATA_CONST.__objc_arraydata: 0x1448
+  __DATA_CONST.__objc_arraydata: 0x14b8
   __DATA_CONST.__got: 0xb40
   __AUTH_CONST.__const: 0x9840
-  __AUTH_CONST.__cfstring: 0x17ae0
-  __AUTH_CONST.__objc_const: 0x23a08
-  __AUTH_CONST.__objc_intobj: 0x768
+  __AUTH_CONST.__cfstring: 0x17be0
+  __AUTH_CONST.__objc_const: 0x23a68
+  __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_floatobj: 0x50
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1c28
+  __DATA.__objc_ivar: 0x1c34
   __DATA.__data: 0x1610
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x62c0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9917
-  Symbols:   19365
-  CStrings:  5118
+  Functions: 9914
+  Symbols:   19356
+  CStrings:  5126
 
Symbols:
+ +[CPLShare scopeTypeForShareURL:]
+ -[CPLEngineLibrary containerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLEngineLibrary setContainerHasBeenWipedDueToEncryptedDataReset:]
+ -[CPLEngineScheduler _disableSynchronizationBecauseContainerHasBeenWipedDueToEncryptedDataResetLocked]
+ -[CPLEngineScheduler noteContainerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLNetworkState isSufficientlyDifferentFromNetworkState:]
+ -[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:localChanges:]
+ -[CPLPushToTransportScopeTask _updateContributors:localChanges:]
+ -[CPLStatus containerHasBeenWipedDueToEncryptedDataReset]
+ -[CPLStatus setContainerHasBeenWipedDueToEncryptedDataReset:]
+ -[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]
+ GCC_except_table4563
+ GCC_except_table4577
+ GCC_except_table4738
+ GCC_except_table4768
+ GCC_except_table4805
+ GCC_except_table4823
+ GCC_except_table4834
+ GCC_except_table4842
+ GCC_except_table4844
+ GCC_except_table4858
+ GCC_except_table4860
+ GCC_except_table4863
+ GCC_except_table5237
+ GCC_except_table5271
+ GCC_except_table5273
+ GCC_except_table5299
+ GCC_except_table5433
+ GCC_except_table5443
+ GCC_except_table5501
+ GCC_except_table5504
+ GCC_except_table5682
+ GCC_except_table5690
+ GCC_except_table5780
+ GCC_except_table5784
+ GCC_except_table5790
+ GCC_except_table5798
+ GCC_except_table5813
+ GCC_except_table5814
+ GCC_except_table5820
+ GCC_except_table5867
+ GCC_except_table5875
+ GCC_except_table5905
+ GCC_except_table5910
+ GCC_except_table5912
+ GCC_except_table5927
+ GCC_except_table5934
+ GCC_except_table5939
+ GCC_except_table5986
+ GCC_except_table6002
+ GCC_except_table6154
+ GCC_except_table6196
+ GCC_except_table6206
+ GCC_except_table6207
+ GCC_except_table6266
+ GCC_except_table6269
+ GCC_except_table6354
+ GCC_except_table6372
+ GCC_except_table6395
+ GCC_except_table6411
+ GCC_except_table6573
+ GCC_except_table6601
+ GCC_except_table6644
+ GCC_except_table6667
+ GCC_except_table6701
+ GCC_except_table6713
+ GCC_except_table6742
+ GCC_except_table6769
+ GCC_except_table6773
+ GCC_except_table6799
+ GCC_except_table6831
+ GCC_except_table6872
+ GCC_except_table6937
+ GCC_except_table6963
+ GCC_except_table6967
+ GCC_except_table6976
+ GCC_except_table6994
+ GCC_except_table7007
+ GCC_except_table7012
+ GCC_except_table7021
+ GCC_except_table7036
+ GCC_except_table7094
+ GCC_except_table7220
+ GCC_except_table8434
+ GCC_except_table8436
+ GCC_except_table8466
+ GCC_except_table8475
+ GCC_except_table8480
+ GCC_except_table8496
+ GCC_except_table8511
+ GCC_except_table8523
+ GCC_except_table8528
+ GCC_except_table8612
+ GCC_except_table8701
+ GCC_except_table8760
+ GCC_except_table8841
+ GCC_except_table8850
+ GCC_except_table8864
+ GCC_except_table8883
+ GCC_except_table8904
+ GCC_except_table8948
+ GCC_except_table8955
+ GCC_except_table8959
+ GCC_except_table9043
+ OBJC_IVAR_$_CPLEngineScheduler._lastSessionFailedBecauseOfNetwork
+ OBJC_IVAR_$_CPLPushToTransportScopeTask._cloudCache
+ OBJC_IVAR_$_CPLPushToTransportScopeTask._idMapping
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
- GCC_except_table4864
- GCC_except_table5238
- GCC_except_table5272
- GCC_except_table5274
- GCC_except_table5300
- GCC_except_table5434
- GCC_except_table5444
- GCC_except_table5502
- GCC_except_table5505
- GCC_except_table5683
- GCC_except_table5693
- GCC_except_table5785
- GCC_except_table5789
- GCC_except_table5795
- GCC_except_table5803
- GCC_except_table5818
- GCC_except_table5819
- GCC_except_table5825
- GCC_except_table5872
- GCC_except_table5883
- GCC_except_table5909
- GCC_except_table5924
- GCC_except_table5926
- GCC_except_table5929
- GCC_except_table5940
- GCC_except_table5943
- GCC_except_table5992
- GCC_except_table6004
- GCC_except_table6156
- GCC_except_table6198
- GCC_except_table6208
- GCC_except_table6209
- GCC_except_table6268
- GCC_except_table6271
- GCC_except_table6358
- GCC_except_table6374
- GCC_except_table6397
- GCC_except_table6415
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
- GCC_except_table7013
- GCC_except_table7023
- GCC_except_table7037
- GCC_except_table7095
- GCC_except_table7221
- GCC_except_table8433
- GCC_except_table8435
- GCC_except_table8465
- GCC_except_table8474
- GCC_except_table8479
- GCC_except_table8495
- GCC_except_table8510
- GCC_except_table8522
- GCC_except_table8527
- GCC_except_table8611
- GCC_except_table8700
- GCC_except_table8759
- GCC_except_table8837
- GCC_except_table8852
- GCC_except_table8874
- GCC_except_table8880
- GCC_except_table8899
- GCC_except_table8909
- GCC_except_table8954
- GCC_except_table8958
- GCC_except_table8962
- GCC_except_table9046
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
+ "CloudPhotoLibrary-916.41.100"
+ "Ignoring contributors update %@"
+ "Notified that network state did change but last session did not fail because of network"
+ "album"
+ "container has been wiped due to encrypted data reset"
+ "containerHasBeenWipedDueToEncryptedDataReset"
+ "photos"
+ "photos.icloud.com"
+ "photos_links"
+ "photos_sharedcollections"
+ "photos_sharing"
+ "shared"
+ "shared_library"
- " - expiringState: %@, expiryDate: %@, viewingMode: %@"
- " - expiringState: %@, viewingMode: %@"
- "CloudPhotoLibrary-911.0.134"
- "Photos"
- "SharedCollections"
- "container has been wiped"
- "containerHasBeenWiped"
```

## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x1c35cc
-  __TEXT.__objc_methlist: 0x15d54
+916.40.110.0.0
+  __TEXT.__text: 0x1c392c
+  __TEXT.__objc_methlist: 0x15cbc
   __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4d78
-  __TEXT.__oslogstring: 0x16d40
-  __TEXT.__cstring: 0x181b9
-  __TEXT.__unwind_info: 0x8530
+  __TEXT.__gcc_except_tab: 0x4d48
+  __TEXT.__oslogstring: 0x16db8
+  __TEXT.__cstring: 0x18298
+  __TEXT.__unwind_info: 0x8520
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9318
+  __DATA_CONST.__objc_selrefs: 0x92e8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x940
-  __DATA_CONST.__objc_arraydata: 0x1448
+  __DATA_CONST.__objc_arraydata: 0x14b8
   __DATA_CONST.__got: 0xb48
   __AUTH_CONST.__const: 0x2cc0
-  __AUTH_CONST.__cfstring: 0x17d60
-  __AUTH_CONST.__objc_const: 0x239e8
-  __AUTH_CONST.__objc_intobj: 0x798
+  __AUTH_CONST.__cfstring: 0x17e60
+  __AUTH_CONST.__objc_const: 0x23a48
+  __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_floatobj: 0x50
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1c28
+  __DATA.__objc_ivar: 0x1c34
   __DATA.__data: 0x1680
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x62c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9798
-  Symbols:   19170
-  CStrings:  5153
+  Functions: 9795
+  Symbols:   19161
+  CStrings:  5161
 
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
+ GCC_except_table4510
+ GCC_except_table4524
+ GCC_except_table4682
+ GCC_except_table4712
+ GCC_except_table4743
+ GCC_except_table4761
+ GCC_except_table4768
+ GCC_except_table4776
+ GCC_except_table4778
+ GCC_except_table4792
+ GCC_except_table4794
+ GCC_except_table4797
+ GCC_except_table5171
+ GCC_except_table5205
+ GCC_except_table5207
+ GCC_except_table5233
+ GCC_except_table5367
+ GCC_except_table5377
+ GCC_except_table5434
+ GCC_except_table5437
+ GCC_except_table5615
+ GCC_except_table5623
+ GCC_except_table5713
+ GCC_except_table5717
+ GCC_except_table5723
+ GCC_except_table5730
+ GCC_except_table5746
+ GCC_except_table5752
+ GCC_except_table5798
+ GCC_except_table5804
+ GCC_except_table5808
+ GCC_except_table5834
+ GCC_except_table5839
+ GCC_except_table5841
+ GCC_except_table5843
+ GCC_except_table5845
+ GCC_except_table5847
+ GCC_except_table5849
+ GCC_except_table5851
+ GCC_except_table5854
+ GCC_except_table5859
+ GCC_except_table5861
+ GCC_except_table5864
+ GCC_except_table5866
+ GCC_except_table5911
+ GCC_except_table5913
+ GCC_except_table5915
+ GCC_except_table5927
+ GCC_except_table6077
+ GCC_except_table6119
+ GCC_except_table6130
+ GCC_except_table6189
+ GCC_except_table6192
+ GCC_except_table6277
+ GCC_except_table6279
+ GCC_except_table6295
+ GCC_except_table6318
+ GCC_except_table6334
+ GCC_except_table6336
+ GCC_except_table6496
+ GCC_except_table6524
+ GCC_except_table6567
+ GCC_except_table6587
+ GCC_except_table6613
+ GCC_except_table6624
+ GCC_except_table6645
+ GCC_except_table6665
+ GCC_except_table6669
+ GCC_except_table6695
+ GCC_except_table6727
+ GCC_except_table6767
+ GCC_except_table6832
+ GCC_except_table6858
+ GCC_except_table6862
+ GCC_except_table6871
+ GCC_except_table6889
+ GCC_except_table6902
+ GCC_except_table6907
+ GCC_except_table6916
+ GCC_except_table6930
+ GCC_except_table6985
+ GCC_except_table7110
+ GCC_except_table7124
+ GCC_except_table7127
+ GCC_except_table7254
+ GCC_except_table7256
+ GCC_except_table7258
+ GCC_except_table7262
+ GCC_except_table7265
+ GCC_except_table7642
+ GCC_except_table7684
+ GCC_except_table7688
+ GCC_except_table7690
+ GCC_except_table7705
+ GCC_except_table7711
+ GCC_except_table7719
+ GCC_except_table7725
+ GCC_except_table7729
+ GCC_except_table7737
+ GCC_except_table7740
+ GCC_except_table7760
+ GCC_except_table7767
+ GCC_except_table7790
+ GCC_except_table7825
+ GCC_except_table7856
+ GCC_except_table7867
+ GCC_except_table7887
+ GCC_except_table7890
+ GCC_except_table7892
+ GCC_except_table7894
+ GCC_except_table7925
+ GCC_except_table7976
+ GCC_except_table8120
+ GCC_except_table8146
+ GCC_except_table8176
+ GCC_except_table8333
+ GCC_except_table8335
+ GCC_except_table8365
+ GCC_except_table8374
+ GCC_except_table8379
+ GCC_except_table8395
+ GCC_except_table8409
+ GCC_except_table8419
+ GCC_except_table8424
+ GCC_except_table8508
+ GCC_except_table8595
+ GCC_except_table8654
+ GCC_except_table8735
+ GCC_except_table8744
+ GCC_except_table8758
+ GCC_except_table8777
+ GCC_except_table8798
+ GCC_except_table8842
+ GCC_except_table8849
+ GCC_except_table8853
+ GCC_except_table8933
+ _CPLRecordModificationDatePrecision
+ _OBJC_IVAR_$_CPLEngineScheduler._lastSessionFailedBecauseOfNetwork
+ _OBJC_IVAR_$_CPLPushToTransportScopeTask._cloudCache
+ _OBJC_IVAR_$_CPLPushToTransportScopeTask._idMapping
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._hasNotedScopeNeedsToPullFromTransport
+ ___57-[CPLStatus containerHasBeenWipedDueToEncryptedDataReset]_block_invoke
+ ___61-[CPLStatus setContainerHasBeenWipedDueToEncryptedDataReset:]_block_invoke
+ ___64-[CPLPushToTransportScopeTask _updateContributors:localChanges:]_block_invoke
+ ___64-[CPLPushToTransportScopeTask _updateContributors:localChanges:]_block_invoke_2
+ ___70-[CPLEngineScheduler noteContainerHasBeenWipedDueToEncryptedDataReset]_block_invoke
+ ___78-[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:localChanges:]_block_invoke
+ ___82-[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]_block_invoke
+ ___82-[CPLUploadPushedChangesTask _setScopeHasChangesToPullFromTransportInTransaction:]_block_invoke_2
+ ___block_descriptor_72_e8_32s40r48r56r64r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e9_B16?0^8ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8s40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8s40l8s48l8r56l8r64l8r72l8r80l8
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
- GCC_except_table4509
- GCC_except_table4523
- GCC_except_table4681
- GCC_except_table4711
- GCC_except_table4742
- GCC_except_table4760
- GCC_except_table4767
- GCC_except_table4775
- GCC_except_table4777
- GCC_except_table4791
- GCC_except_table4793
- GCC_except_table4796
- GCC_except_table5170
- GCC_except_table5204
- GCC_except_table5206
- GCC_except_table5232
- GCC_except_table5366
- GCC_except_table5376
- GCC_except_table5433
- GCC_except_table5436
- GCC_except_table5614
- GCC_except_table5622
- GCC_except_table5712
- GCC_except_table5716
- GCC_except_table5722
- GCC_except_table5729
- GCC_except_table5744
- GCC_except_table5751
- GCC_except_table5797
- GCC_except_table5803
- GCC_except_table5807
- GCC_except_table5833
- GCC_except_table5838
- GCC_except_table5840
- GCC_except_table5842
- GCC_except_table5844
- GCC_except_table5846
- GCC_except_table5848
- GCC_except_table5850
- GCC_except_table5853
- GCC_except_table5858
- GCC_except_table5860
- GCC_except_table5862
- GCC_except_table5865
- GCC_except_table5910
- GCC_except_table5912
- GCC_except_table5914
- GCC_except_table5926
- GCC_except_table6076
- GCC_except_table6118
- GCC_except_table6128
- GCC_except_table6188
- GCC_except_table6191
- GCC_except_table6276
- GCC_except_table6278
- GCC_except_table6294
- GCC_except_table6317
- GCC_except_table6333
- GCC_except_table6335
- GCC_except_table6495
- GCC_except_table6523
- GCC_except_table6566
- GCC_except_table6586
- GCC_except_table6612
- GCC_except_table6623
- GCC_except_table6644
- GCC_except_table6664
- GCC_except_table6668
- GCC_except_table6694
- GCC_except_table6726
- GCC_except_table6766
- GCC_except_table6831
- GCC_except_table6857
- GCC_except_table6861
- GCC_except_table6870
- GCC_except_table6888
- GCC_except_table6901
- GCC_except_table6906
- GCC_except_table6914
- GCC_except_table6929
- GCC_except_table6984
- GCC_except_table7109
- GCC_except_table7123
- GCC_except_table7126
- GCC_except_table7253
- GCC_except_table7255
- GCC_except_table7257
- GCC_except_table7261
- GCC_except_table7264
- GCC_except_table7641
- GCC_except_table7683
- GCC_except_table7687
- GCC_except_table7689
- GCC_except_table7704
- GCC_except_table7710
- GCC_except_table7718
- GCC_except_table7724
- GCC_except_table7728
- GCC_except_table7736
- GCC_except_table7739
- GCC_except_table7759
- GCC_except_table7766
- GCC_except_table7789
- GCC_except_table7824
- GCC_except_table7855
- GCC_except_table7866
- GCC_except_table7886
- GCC_except_table7889
- GCC_except_table7891
- GCC_except_table7893
- GCC_except_table7924
- GCC_except_table7975
- GCC_except_table8119
- GCC_except_table8145
- GCC_except_table8175
- GCC_except_table8332
- GCC_except_table8334
- GCC_except_table8364
- GCC_except_table8373
- GCC_except_table8378
- GCC_except_table8394
- GCC_except_table8408
- GCC_except_table8418
- GCC_except_table8423
- GCC_except_table8507
- GCC_except_table8594
- GCC_except_table8653
- GCC_except_table8731
- GCC_except_table8746
- GCC_except_table8768
- GCC_except_table8774
- GCC_except_table8793
- GCC_except_table8803
- GCC_except_table8848
- GCC_except_table8852
- GCC_except_table8856
- GCC_except_table8936
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._hasPushedSomeChanges
- ___34-[CPLStatus containerHasBeenWiped]_block_invoke
- ___38-[CPLStatus setContainerHasBeenWiped:]_block_invoke
- ___47-[CPLEngineScheduler noteContainerHasBeenWiped]_block_invoke
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke_2
- ___65-[CPLPushToTransportScopeTask _contributorsUpdatesInTransaction:]_block_invoke
- ___93-[CPLUploadPushedChangesTask _copyResourceChangeFromChange:toChange:fingerprintScheme:error:]_block_invoke
- ___block_descriptor_64_e8_32s40r48r56r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e64_B48?0"CPLRecordChange"8"CPLRecordChange"16"NSString"24:32:40lr56l8s32l8r64l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e9_B16?0^8ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8s40l8s48l8r56l8r64l8r72l8
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
+ "CloudPhotoLibrary-916.40.110"
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
- "CloudPhotoLibrary-912.0.235"
- "Photos"
- "SharedCollections"
- "container has been wiped"
- "containerHasBeenWiped"
```

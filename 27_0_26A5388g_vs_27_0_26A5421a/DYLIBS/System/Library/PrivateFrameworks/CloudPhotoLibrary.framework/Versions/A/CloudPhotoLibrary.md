## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0x1e5acc
-  __TEXT.__objc_methlist: 0x15cbc
+911.0.134.0.0
+  __TEXT.__text: 0x1e69c0
+  __TEXT.__objc_methlist: 0x15d44
   __TEXT.__const: 0x328
   __TEXT.__gcc_except_tab: 0x4d80
-  __TEXT.__oslogstring: 0x16b50
-  __TEXT.__cstring: 0x18c7c
-  __TEXT.__unwind_info: 0x6d78
+  __TEXT.__oslogstring: 0x16c0c
+  __TEXT.__cstring: 0x18d11
+  __TEXT.__unwind_info: 0x6db8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92a0
+  __DATA_CONST.__objc_selrefs: 0x92d0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x948
-  __DATA_CONST.__objc_arraydata: 0x1438
+  __DATA_CONST.__objc_arraydata: 0x1448
   __DATA_CONST.__got: 0xb40
-  __AUTH_CONST.__const: 0x9820
-  __AUTH_CONST.__cfstring: 0x179a0
-  __AUTH_CONST.__objc_const: 0x239b0
+  __AUTH_CONST.__const: 0x9840
+  __AUTH_CONST.__cfstring: 0x17a80
+  __AUTH_CONST.__objc_const: 0x23a08
   __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1c24
-  __DATA.__data: 0x1600
+  __DATA.__objc_ivar: 0x1c28
+  __DATA.__data: 0x1610
   __DATA.__bss: 0xb48
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x62c0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9901
-  Symbols:   19338
-  CStrings:  5105
+  Functions: 9917
+  Symbols:   19365
+  CStrings:  5115
 
Symbols:
+ +[CPLEngineSyncManager qualityOfServiceForTurboSyncSessions]
+ +[CPLScopedIdentifier scopedIdentifiersFromArrayOfUnknownIdentifiers:withScopeIdentifier:]
+ +[CPLTransportContainerConfiguration isValidContainerIdentifier:]
+ -[CPLEngineResourceDownloadQueue countOfDownloadedResources]
+ -[CPLEngineResourceDownloadQueue removeDownloadedResource:error:]
+ -[CPLGenerateDerivativesSubtask initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:session:]
+ -[CPLLibraryManager discardDownloadedResource:]
+ -[CPLProxyLibraryManager discardDownloadedResource:]
+ -[CPLSyncSession desiredQOS]
+ -[CPLSyncSession newSessionQueueWithName:]
+ -[CPLSyncSessionPrediction shouldUseTurboMode]
+ GCC_except_table1159
+ GCC_except_table1235
+ GCC_except_table1289
+ GCC_except_table1294
+ GCC_except_table1333
+ GCC_except_table1353
+ GCC_except_table1355
+ GCC_except_table1529
+ GCC_except_table1578
+ GCC_except_table1582
+ GCC_except_table1584
+ GCC_except_table1589
+ GCC_except_table1591
+ GCC_except_table1599
+ GCC_except_table1601
+ GCC_except_table1614
+ GCC_except_table1620
+ GCC_except_table1622
+ GCC_except_table1624
+ GCC_except_table1626
+ GCC_except_table1708
+ GCC_except_table1796
+ GCC_except_table2048
+ GCC_except_table2058
+ GCC_except_table2287
+ GCC_except_table2290
+ GCC_except_table2297
+ GCC_except_table2301
+ GCC_except_table2328
+ GCC_except_table2335
+ GCC_except_table2345
+ GCC_except_table2348
+ GCC_except_table2537
+ GCC_except_table2638
+ GCC_except_table2704
+ GCC_except_table2712
+ GCC_except_table275
+ GCC_except_table2753
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table2845
+ GCC_except_table2852
+ GCC_except_table286
+ GCC_except_table288
+ GCC_except_table3005
+ GCC_except_table3094
+ GCC_except_table318
+ GCC_except_table3384
+ GCC_except_table3386
+ GCC_except_table3491
+ GCC_except_table3502
+ GCC_except_table3559
+ GCC_except_table3672
+ GCC_except_table3696
+ GCC_except_table3796
+ GCC_except_table3802
+ GCC_except_table3963
+ GCC_except_table4012
+ GCC_except_table403
+ GCC_except_table4257
+ GCC_except_table4346
+ GCC_except_table4348
+ GCC_except_table4357
+ GCC_except_table453
+ GCC_except_table4562
+ GCC_except_table4576
+ GCC_except_table468
+ GCC_except_table4737
+ GCC_except_table4767
+ GCC_except_table4804
+ GCC_except_table4822
+ GCC_except_table4835
+ GCC_except_table4843
+ GCC_except_table4845
+ GCC_except_table4861
+ GCC_except_table4864
+ GCC_except_table5238
+ GCC_except_table5272
+ GCC_except_table5274
+ GCC_except_table5300
+ GCC_except_table541
+ GCC_except_table5434
+ GCC_except_table5444
+ GCC_except_table545
+ GCC_except_table5502
+ GCC_except_table5505
+ GCC_except_table561
+ GCC_except_table5683
+ GCC_except_table5693
+ GCC_except_table5785
+ GCC_except_table5789
+ GCC_except_table5803
+ GCC_except_table5818
+ GCC_except_table5819
+ GCC_except_table5825
+ GCC_except_table583
+ GCC_except_table5872
+ GCC_except_table5879
+ GCC_except_table5883
+ GCC_except_table5909
+ GCC_except_table5920
+ GCC_except_table5922
+ GCC_except_table5924
+ GCC_except_table5926
+ GCC_except_table5929
+ GCC_except_table5936
+ GCC_except_table5938
+ GCC_except_table5940
+ GCC_except_table5941
+ GCC_except_table5943
+ GCC_except_table5988
+ GCC_except_table5990
+ GCC_except_table5992
+ GCC_except_table6004
+ GCC_except_table602
+ GCC_except_table612
+ GCC_except_table6156
+ GCC_except_table6198
+ GCC_except_table6208
+ GCC_except_table6209
+ GCC_except_table6268
+ GCC_except_table6271
+ GCC_except_table630
+ GCC_except_table6356
+ GCC_except_table6358
+ GCC_except_table6374
+ GCC_except_table6397
+ GCC_except_table6413
+ GCC_except_table6415
+ GCC_except_table643
+ GCC_except_table6575
+ GCC_except_table6603
+ GCC_except_table6646
+ GCC_except_table6668
+ GCC_except_table6702
+ GCC_except_table6714
+ GCC_except_table6743
+ GCC_except_table6770
+ GCC_except_table6774
+ GCC_except_table6800
+ GCC_except_table6832
+ GCC_except_table6873
+ GCC_except_table6938
+ GCC_except_table6964
+ GCC_except_table6968
+ GCC_except_table6977
+ GCC_except_table6995
+ GCC_except_table7008
+ GCC_except_table7013
+ GCC_except_table7022
+ GCC_except_table7023
+ GCC_except_table7037
+ GCC_except_table7095
+ GCC_except_table7221
+ GCC_except_table7235
+ GCC_except_table7238
+ GCC_except_table7367
+ GCC_except_table7369
+ GCC_except_table7373
+ GCC_except_table7376
+ GCC_except_table758
+ GCC_except_table7750
+ GCC_except_table7792
+ GCC_except_table7796
+ GCC_except_table7798
+ GCC_except_table7813
+ GCC_except_table7827
+ GCC_except_table7833
+ GCC_except_table7845
+ GCC_except_table7848
+ GCC_except_table7868
+ GCC_except_table7875
+ GCC_except_table7898
+ GCC_except_table792
+ GCC_except_table7933
+ GCC_except_table796
+ GCC_except_table7964
+ GCC_except_table7975
+ GCC_except_table799
+ GCC_except_table7997
+ GCC_except_table8000
+ GCC_except_table8002
+ GCC_except_table8004
+ GCC_except_table801
+ GCC_except_table8035
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table8086
+ GCC_except_table810
+ GCC_except_table812
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table8230
+ GCC_except_table825
+ GCC_except_table8253
+ GCC_except_table827
+ GCC_except_table8283
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table835
+ GCC_except_table837
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table843
+ GCC_except_table8433
+ GCC_except_table8435
+ GCC_except_table8474
+ GCC_except_table8479
+ GCC_except_table8495
+ GCC_except_table851
+ GCC_except_table8510
+ GCC_except_table8522
+ GCC_except_table8527
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table859
+ GCC_except_table8611
+ GCC_except_table870
+ GCC_except_table8700
+ GCC_except_table872
+ GCC_except_table874
+ GCC_except_table8759
+ GCC_except_table876
+ GCC_except_table878
+ GCC_except_table880
+ GCC_except_table882
+ GCC_except_table8837
+ GCC_except_table884
+ GCC_except_table8852
+ GCC_except_table886
+ GCC_except_table8874
+ GCC_except_table888
+ GCC_except_table8880
+ GCC_except_table8899
+ GCC_except_table890
+ GCC_except_table8909
+ GCC_except_table8951
+ GCC_except_table8954
+ GCC_except_table8958
+ GCC_except_table8962
+ GCC_except_table9046
+ GCC_except_table910
+ GCC_except_table916
+ GCC_except_table925
+ GCC_except_table936
+ GCC_except_table952
+ OBJC_IVAR_$_CPLEngineScheduler._overridesOtherBudgets
+ _CPLCustomBundleIDKey
+ _CPLLibraryPathsKey
+ _CPLSyncSessionPredictionTypeTurbo
+ _OUTLINED_FUNCTION_130
+ _OUTLINED_FUNCTION_131
+ __OBJC_$_PROP_LIST_CPLSyncSessionPrediction
+ ___28-[CPLLibraryManager barrier]_block_invoke
+ ___47-[CPLLibraryManager discardDownloadedResource:]_block_invoke
+ ___52-[CPLProxyLibraryManager discardDownloadedResource:]_block_invoke
+ ___52-[CPLProxyLibraryManager discardDownloadedResource:]_block_invoke_2
+ ___52-[CPLProxyLibraryManager discardDownloadedResource:]_block_invoke_3
+ ___57-[CPLEngineScheduler setShouldOverride:forSystemBudgets:]_block_invoke
+ _objc_msgSend$countOfDownloadedResources
+ _objc_msgSend$desiredQOS
+ _objc_msgSend$discardDownloadedResource:
+ _objc_msgSend$initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:session:
+ _objc_msgSend$newSessionQueueWithName:
+ _objc_msgSend$predictedValueForType:
+ _objc_msgSend$qualityOfServiceForTurboSyncSessions
+ _objc_msgSend$removeDownloadedResource:error:
+ _objc_msgSend$shouldUseTurboMode
+ _objc_msgSend$wellKnownConfigurations
- -[CPLGenerateDerivativesSubtask initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:]
- -[CPLGenerateDerivativesSubtask setPredictor:]
- -[CPLGenerateDerivativesSubtask setSession:]
- GCC_except_table1156
- GCC_except_table1232
- GCC_except_table1286
- GCC_except_table1291
- GCC_except_table1330
- GCC_except_table1350
- GCC_except_table1352
- GCC_except_table1526
- GCC_except_table1575
- GCC_except_table1579
- GCC_except_table1581
- GCC_except_table1586
- GCC_except_table1588
- GCC_except_table1596
- GCC_except_table1598
- GCC_except_table1605
- GCC_except_table1617
- GCC_except_table1619
- GCC_except_table1621
- GCC_except_table1623
- GCC_except_table1705
- GCC_except_table1793
- GCC_except_table2046
- GCC_except_table2056
- GCC_except_table2285
- GCC_except_table2289
- GCC_except_table2296
- GCC_except_table2300
- GCC_except_table2327
- GCC_except_table2334
- GCC_except_table2344
- GCC_except_table2347
- GCC_except_table2536
- GCC_except_table2637
- GCC_except_table2703
- GCC_except_table2711
- GCC_except_table274
- GCC_except_table2752
- GCC_except_table280
- GCC_except_table283
- GCC_except_table2844
- GCC_except_table285
- GCC_except_table2851
- GCC_except_table287
- GCC_except_table3004
- GCC_except_table3093
- GCC_except_table317
- GCC_except_table3383
- GCC_except_table3385
- GCC_except_table3489
- GCC_except_table3500
- GCC_except_table3555
- GCC_except_table3668
- GCC_except_table3692
- GCC_except_table3786
- GCC_except_table3792
- GCC_except_table3959
- GCC_except_table399
- GCC_except_table4008
- GCC_except_table402
- GCC_except_table4253
- GCC_except_table4338
- GCC_except_table4344
- GCC_except_table4353
- GCC_except_table452
- GCC_except_table4558
- GCC_except_table4572
- GCC_except_table467
- GCC_except_table4732
- GCC_except_table4762
- GCC_except_table4799
- GCC_except_table4817
- GCC_except_table4830
- GCC_except_table4838
- GCC_except_table4840
- GCC_except_table4854
- GCC_except_table4856
- GCC_except_table5231
- GCC_except_table5264
- GCC_except_table5266
- GCC_except_table5292
- GCC_except_table540
- GCC_except_table5426
- GCC_except_table5436
- GCC_except_table544
- GCC_except_table5494
- GCC_except_table5497
- GCC_except_table560
- GCC_except_table5675
- GCC_except_table5685
- GCC_except_table5777
- GCC_except_table5781
- GCC_except_table5787
- GCC_except_table5810
- GCC_except_table5811
- GCC_except_table5817
- GCC_except_table582
- GCC_except_table5864
- GCC_except_table5871
- GCC_except_table5875
- GCC_except_table5901
- GCC_except_table5906
- GCC_except_table5908
- GCC_except_table5910
- GCC_except_table5912
- GCC_except_table5921
- GCC_except_table5928
- GCC_except_table5930
- GCC_except_table5932
- GCC_except_table5933
- GCC_except_table5935
- GCC_except_table5980
- GCC_except_table5982
- GCC_except_table5984
- GCC_except_table5996
- GCC_except_table600
- GCC_except_table611
- GCC_except_table6148
- GCC_except_table6190
- GCC_except_table6200
- GCC_except_table6201
- GCC_except_table6260
- GCC_except_table6263
- GCC_except_table629
- GCC_except_table6348
- GCC_except_table6350
- GCC_except_table6366
- GCC_except_table6389
- GCC_except_table6405
- GCC_except_table6407
- GCC_except_table642
- GCC_except_table6567
- GCC_except_table6595
- GCC_except_table6638
- GCC_except_table6660
- GCC_except_table6694
- GCC_except_table6706
- GCC_except_table6735
- GCC_except_table6762
- GCC_except_table6766
- GCC_except_table6792
- GCC_except_table6824
- GCC_except_table6865
- GCC_except_table6930
- GCC_except_table6956
- GCC_except_table6960
- GCC_except_table6969
- GCC_except_table6987
- GCC_except_table7000
- GCC_except_table7005
- GCC_except_table7014
- GCC_except_table7015
- GCC_except_table7029
- GCC_except_table7087
- GCC_except_table7213
- GCC_except_table7227
- GCC_except_table7230
- GCC_except_table7357
- GCC_except_table7359
- GCC_except_table7361
- GCC_except_table7368
- GCC_except_table757
- GCC_except_table7742
- GCC_except_table7784
- GCC_except_table7788
- GCC_except_table7790
- GCC_except_table7805
- GCC_except_table7811
- GCC_except_table7825
- GCC_except_table7829
- GCC_except_table7840
- GCC_except_table7860
- GCC_except_table7867
- GCC_except_table7890
- GCC_except_table791
- GCC_except_table7925
- GCC_except_table795
- GCC_except_table7956
- GCC_except_table7967
- GCC_except_table798
- GCC_except_table7989
- GCC_except_table7992
- GCC_except_table7994
- GCC_except_table7996
- GCC_except_table800
- GCC_except_table8027
- GCC_except_table803
- GCC_except_table805
- GCC_except_table8077
- GCC_except_table809
- GCC_except_table811
- GCC_except_table820
- GCC_except_table822
- GCC_except_table8221
- GCC_except_table824
- GCC_except_table8244
- GCC_except_table826
- GCC_except_table8274
- GCC_except_table828
- GCC_except_table830
- GCC_except_table832
- GCC_except_table834
- GCC_except_table836
- GCC_except_table838
- GCC_except_table840
- GCC_except_table842
- GCC_except_table8424
- GCC_except_table8426
- GCC_except_table8456
- GCC_except_table8470
- GCC_except_table8486
- GCC_except_table850
- GCC_except_table8501
- GCC_except_table8513
- GCC_except_table8518
- GCC_except_table852
- GCC_except_table854
- GCC_except_table856
- GCC_except_table858
- GCC_except_table8602
- GCC_except_table867
- GCC_except_table869
- GCC_except_table8691
- GCC_except_table871
- GCC_except_table873
- GCC_except_table875
- GCC_except_table8750
- GCC_except_table877
- GCC_except_table879
- GCC_except_table881
- GCC_except_table8828
- GCC_except_table883
- GCC_except_table8843
- GCC_except_table885
- GCC_except_table8865
- GCC_except_table887
- GCC_except_table8871
- GCC_except_table8890
- GCC_except_table8900
- GCC_except_table8942
- GCC_except_table8945
- GCC_except_table8949
- GCC_except_table8953
- GCC_except_table9036
- GCC_except_table907
- GCC_except_table913
- GCC_except_table922
- GCC_except_table933
- GCC_except_table949
- _CPLSyncSessionPredictionTypeTurboMode
- _objc_msgSend$initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:
- _objc_msgSend$setSession:
CStrings:
+ "%@ failed to discard downloaded %@: %@"
+ "CPLAllowAllContainers"
+ "CPLCustomBundleID"
+ "CPLLibraryPaths"
+ "CPLStatusDidChange"
+ "CloudPhotoLibrary-911.0.134"
+ "Discarding %@ but the file is not present in the resource storage any more: %@"
+ "Handling CPL status change"
+ "Trying to discard a downloaded resource while the library is not open"
+ "com.apple.VisualIntelligence"
+ "com.apple.campo"
+ "com.apple.photos.asc.e2ee.secure"
+ "turbo"
+ "\xf0A"
- "CloudPhotoLibrary-910.34.101"
- "com.apple.photos.asc.e2ee"
- "turboMode"
- "\xf01"
```

## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x1cb0d4
-  __TEXT.__objc_methlist: 0x15ccc
+912.0.111.0.0
+  __TEXT.__text: 0x1cbd3c
+  __TEXT.__objc_methlist: 0x15d44
   __TEXT.__const: 0x328
   __TEXT.__gcc_except_tab: 0x4d78
-  __TEXT.__oslogstring: 0x16c84
-  __TEXT.__cstring: 0x180f3
-  __TEXT.__unwind_info: 0x6d20
+  __TEXT.__oslogstring: 0x16d40
+  __TEXT.__cstring: 0x18172
+  __TEXT.__unwind_info: 0x6d60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92e8
+  __DATA_CONST.__objc_selrefs: 0x9310
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x940
-  __DATA_CONST.__objc_arraydata: 0x1438
+  __DATA_CONST.__objc_arraydata: 0x1448
   __DATA_CONST.__got: 0xb48
-  __AUTH_CONST.__const: 0x2ca0
-  __AUTH_CONST.__cfstring: 0x17c20
-  __AUTH_CONST.__objc_const: 0x23990
+  __AUTH_CONST.__const: 0x2cc0
+  __AUTH_CONST.__cfstring: 0x17ce0
+  __AUTH_CONST.__objc_const: 0x239e8
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1c24
-  __DATA.__data: 0x1670
+  __DATA.__objc_ivar: 0x1c28
+  __DATA.__data: 0x1680
   __DATA.__bss: 0xc90
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x62c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9782
-  Symbols:   19142
-  CStrings:  5140
+  Functions: 9797
+  Symbols:   19168
+  CStrings:  5149
 
Symbols:
+ +[CPLEngineSyncManager qualityOfServiceForTurboSyncSessions]
+ +[CPLScopedIdentifier scopedIdentifiersFromArrayOfUnknownIdentifiers:withScopeIdentifier:]
+ -[CPLEngineResourceDownloadQueue countOfDownloadedResources]
+ -[CPLEngineResourceDownloadQueue removeDownloadedResource:error:]
+ -[CPLGenerateDerivativesSubtask initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:session:]
+ -[CPLLibraryManager discardDownloadedResource:]
+ -[CPLProxyLibraryManager discardDownloadedResource:]
+ -[CPLSyncSession desiredQOS]
+ -[CPLSyncSession newSessionQueueWithName:]
+ -[CPLSyncSessionPrediction shouldUseTurboMode]
+ GCC_except_table1123
+ GCC_except_table1206
+ GCC_except_table1260
+ GCC_except_table1265
+ GCC_except_table1311
+ GCC_except_table1329
+ GCC_except_table1331
+ GCC_except_table1505
+ GCC_except_table1554
+ GCC_except_table1558
+ GCC_except_table1560
+ GCC_except_table1565
+ GCC_except_table1567
+ GCC_except_table1575
+ GCC_except_table1577
+ GCC_except_table1590
+ GCC_except_table1596
+ GCC_except_table1598
+ GCC_except_table1600
+ GCC_except_table1602
+ GCC_except_table1684
+ GCC_except_table1772
+ GCC_except_table2024
+ GCC_except_table2032
+ GCC_except_table2259
+ GCC_except_table2262
+ GCC_except_table2269
+ GCC_except_table2273
+ GCC_except_table2300
+ GCC_except_table2307
+ GCC_except_table2317
+ GCC_except_table2320
+ GCC_except_table2509
+ GCC_except_table256
+ GCC_except_table2608
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table2674
+ GCC_except_table2682
+ GCC_except_table269
+ GCC_except_table2723
+ GCC_except_table2815
+ GCC_except_table2822
+ GCC_except_table2975
+ GCC_except_table299
+ GCC_except_table3064
+ GCC_except_table3354
+ GCC_except_table3356
+ GCC_except_table3461
+ GCC_except_table3472
+ GCC_except_table3529
+ GCC_except_table3642
+ GCC_except_table3666
+ GCC_except_table374
+ GCC_except_table3754
+ GCC_except_table3760
+ GCC_except_table378
+ GCC_except_table3921
+ GCC_except_table3968
+ GCC_except_table4213
+ GCC_except_table428
+ GCC_except_table4293
+ GCC_except_table4295
+ GCC_except_table4304
+ GCC_except_table439
+ GCC_except_table4509
+ GCC_except_table4523
+ GCC_except_table4681
+ GCC_except_table4711
+ GCC_except_table4742
+ GCC_except_table4760
+ GCC_except_table4767
+ GCC_except_table4775
+ GCC_except_table4777
+ GCC_except_table4793
+ GCC_except_table4796
+ GCC_except_table512
+ GCC_except_table516
+ GCC_except_table5170
+ GCC_except_table5204
+ GCC_except_table5206
+ GCC_except_table5232
+ GCC_except_table532
+ GCC_except_table5366
+ GCC_except_table5376
+ GCC_except_table5433
+ GCC_except_table5436
+ GCC_except_table554
+ GCC_except_table5622
+ GCC_except_table5712
+ GCC_except_table5716
+ GCC_except_table572
+ GCC_except_table5722
+ GCC_except_table5729
+ GCC_except_table5744
+ GCC_except_table5745
+ GCC_except_table5751
+ GCC_except_table5797
+ GCC_except_table5803
+ GCC_except_table5807
+ GCC_except_table582
+ GCC_except_table5833
+ GCC_except_table5844
+ GCC_except_table5846
+ GCC_except_table5848
+ GCC_except_table5853
+ GCC_except_table5858
+ GCC_except_table5860
+ GCC_except_table5862
+ GCC_except_table5863
+ GCC_except_table5865
+ GCC_except_table5910
+ GCC_except_table5912
+ GCC_except_table5914
+ GCC_except_table5926
+ GCC_except_table600
+ GCC_except_table6076
+ GCC_except_table6118
+ GCC_except_table6128
+ GCC_except_table6129
+ GCC_except_table613
+ GCC_except_table6188
+ GCC_except_table6191
+ GCC_except_table6276
+ GCC_except_table6278
+ GCC_except_table6294
+ GCC_except_table6317
+ GCC_except_table6333
+ GCC_except_table6335
+ GCC_except_table6495
+ GCC_except_table6523
+ GCC_except_table6566
+ GCC_except_table6586
+ GCC_except_table6612
+ GCC_except_table6623
+ GCC_except_table6644
+ GCC_except_table6664
+ GCC_except_table6668
+ GCC_except_table6694
+ GCC_except_table6726
+ GCC_except_table6766
+ GCC_except_table6831
+ GCC_except_table6857
+ GCC_except_table6861
+ GCC_except_table6870
+ GCC_except_table6888
+ GCC_except_table6901
+ GCC_except_table6914
+ GCC_except_table6915
+ GCC_except_table6929
+ GCC_except_table6984
+ GCC_except_table7109
+ GCC_except_table7123
+ GCC_except_table7126
+ GCC_except_table723
+ GCC_except_table7255
+ GCC_except_table7257
+ GCC_except_table7261
+ GCC_except_table7264
+ GCC_except_table729
+ GCC_except_table764
+ GCC_except_table7641
+ GCC_except_table768
+ GCC_except_table7683
+ GCC_except_table7687
+ GCC_except_table7689
+ GCC_except_table7704
+ GCC_except_table771
+ GCC_except_table7718
+ GCC_except_table7724
+ GCC_except_table773
+ GCC_except_table7736
+ GCC_except_table7739
+ GCC_except_table7759
+ GCC_except_table776
+ GCC_except_table7766
+ GCC_except_table778
+ GCC_except_table7789
+ GCC_except_table782
+ GCC_except_table7824
+ GCC_except_table784
+ GCC_except_table7855
+ GCC_except_table7866
+ GCC_except_table7886
+ GCC_except_table7889
+ GCC_except_table7891
+ GCC_except_table7893
+ GCC_except_table7924
+ GCC_except_table793
+ GCC_except_table795
+ GCC_except_table797
+ GCC_except_table7975
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table809
+ GCC_except_table811
+ GCC_except_table8119
+ GCC_except_table813
+ GCC_except_table8145
+ GCC_except_table815
+ GCC_except_table8175
+ GCC_except_table823
+ GCC_except_table825
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table8332
+ GCC_except_table8334
+ GCC_except_table8373
+ GCC_except_table8378
+ GCC_except_table8394
+ GCC_except_table8408
+ GCC_except_table8418
+ GCC_except_table842
+ GCC_except_table8423
+ GCC_except_table844
+ GCC_except_table846
+ GCC_except_table848
+ GCC_except_table850
+ GCC_except_table8507
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table856
+ GCC_except_table858
+ GCC_except_table8594
+ GCC_except_table860
+ GCC_except_table862
+ GCC_except_table8653
+ GCC_except_table8731
+ GCC_except_table8746
+ GCC_except_table8768
+ GCC_except_table8774
+ GCC_except_table8793
+ GCC_except_table8803
+ GCC_except_table882
+ GCC_except_table8845
+ GCC_except_table8848
+ GCC_except_table8852
+ GCC_except_table8856
+ GCC_except_table888
+ GCC_except_table8935
+ GCC_except_table897
+ GCC_except_table906
+ GCC_except_table918
+ _CPLCustomBundleIDKey
+ _CPLLibraryPathsKey
+ _CPLSyncSessionPredictionTypeTurbo
+ _OBJC_IVAR_$_CPLEngineScheduler._overridesOtherBudgets
+ _OUTLINED_FUNCTION_126
+ _OUTLINED_FUNCTION_127
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
- -[CPLGenerateDerivativesSubtask initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:]
- -[CPLGenerateDerivativesSubtask setPredictor:]
- -[CPLGenerateDerivativesSubtask setSession:]
- GCC_except_table1120
- GCC_except_table1203
- GCC_except_table1257
- GCC_except_table1262
- GCC_except_table1308
- GCC_except_table1326
- GCC_except_table1328
- GCC_except_table1502
- GCC_except_table1551
- GCC_except_table1555
- GCC_except_table1557
- GCC_except_table1562
- GCC_except_table1564
- GCC_except_table1572
- GCC_except_table1574
- GCC_except_table1581
- GCC_except_table1593
- GCC_except_table1595
- GCC_except_table1597
- GCC_except_table1599
- GCC_except_table1681
- GCC_except_table1769
- GCC_except_table2022
- GCC_except_table2030
- GCC_except_table2257
- GCC_except_table2261
- GCC_except_table2268
- GCC_except_table2272
- GCC_except_table2299
- GCC_except_table2306
- GCC_except_table2316
- GCC_except_table2319
- GCC_except_table2508
- GCC_except_table255
- GCC_except_table2607
- GCC_except_table261
- GCC_except_table264
- GCC_except_table266
- GCC_except_table2673
- GCC_except_table268
- GCC_except_table2681
- GCC_except_table2722
- GCC_except_table2814
- GCC_except_table2821
- GCC_except_table2974
- GCC_except_table298
- GCC_except_table3063
- GCC_except_table3353
- GCC_except_table3355
- GCC_except_table3459
- GCC_except_table3470
- GCC_except_table3525
- GCC_except_table3638
- GCC_except_table3662
- GCC_except_table370
- GCC_except_table3744
- GCC_except_table3750
- GCC_except_table377
- GCC_except_table3917
- GCC_except_table3964
- GCC_except_table4209
- GCC_except_table427
- GCC_except_table4285
- GCC_except_table4291
- GCC_except_table4300
- GCC_except_table438
- GCC_except_table4505
- GCC_except_table4519
- GCC_except_table4676
- GCC_except_table4706
- GCC_except_table4737
- GCC_except_table4755
- GCC_except_table4762
- GCC_except_table4770
- GCC_except_table4772
- GCC_except_table4786
- GCC_except_table4788
- GCC_except_table511
- GCC_except_table515
- GCC_except_table5163
- GCC_except_table5196
- GCC_except_table5198
- GCC_except_table5224
- GCC_except_table531
- GCC_except_table5358
- GCC_except_table5368
- GCC_except_table5425
- GCC_except_table5428
- GCC_except_table553
- GCC_except_table5606
- GCC_except_table570
- GCC_except_table5704
- GCC_except_table5708
- GCC_except_table5714
- GCC_except_table5721
- GCC_except_table5736
- GCC_except_table5737
- GCC_except_table5743
- GCC_except_table5789
- GCC_except_table5795
- GCC_except_table5799
- GCC_except_table581
- GCC_except_table5825
- GCC_except_table5830
- GCC_except_table5832
- GCC_except_table5834
- GCC_except_table5836
- GCC_except_table5845
- GCC_except_table5852
- GCC_except_table5854
- GCC_except_table5855
- GCC_except_table5857
- GCC_except_table5902
- GCC_except_table5904
- GCC_except_table5906
- GCC_except_table5918
- GCC_except_table599
- GCC_except_table6068
- GCC_except_table6110
- GCC_except_table612
- GCC_except_table6120
- GCC_except_table6121
- GCC_except_table6180
- GCC_except_table6183
- GCC_except_table6268
- GCC_except_table6270
- GCC_except_table6286
- GCC_except_table6309
- GCC_except_table6325
- GCC_except_table6327
- GCC_except_table6487
- GCC_except_table6515
- GCC_except_table6558
- GCC_except_table6578
- GCC_except_table6604
- GCC_except_table6615
- GCC_except_table6636
- GCC_except_table6656
- GCC_except_table6660
- GCC_except_table6686
- GCC_except_table6718
- GCC_except_table6758
- GCC_except_table6823
- GCC_except_table6849
- GCC_except_table6853
- GCC_except_table6862
- GCC_except_table6880
- GCC_except_table6893
- GCC_except_table6898
- GCC_except_table6907
- GCC_except_table6921
- GCC_except_table6976
- GCC_except_table7101
- GCC_except_table7115
- GCC_except_table7118
- GCC_except_table722
- GCC_except_table7245
- GCC_except_table7247
- GCC_except_table7249
- GCC_except_table7256
- GCC_except_table728
- GCC_except_table763
- GCC_except_table7633
- GCC_except_table767
- GCC_except_table7675
- GCC_except_table7679
- GCC_except_table7681
- GCC_except_table7696
- GCC_except_table770
- GCC_except_table7702
- GCC_except_table7716
- GCC_except_table772
- GCC_except_table7720
- GCC_except_table7731
- GCC_except_table775
- GCC_except_table7751
- GCC_except_table7758
- GCC_except_table777
- GCC_except_table7781
- GCC_except_table781
- GCC_except_table7816
- GCC_except_table783
- GCC_except_table7847
- GCC_except_table7858
- GCC_except_table7878
- GCC_except_table7881
- GCC_except_table7883
- GCC_except_table7885
- GCC_except_table7916
- GCC_except_table792
- GCC_except_table794
- GCC_except_table796
- GCC_except_table7966
- GCC_except_table798
- GCC_except_table800
- GCC_except_table802
- GCC_except_table804
- GCC_except_table806
- GCC_except_table808
- GCC_except_table810
- GCC_except_table8110
- GCC_except_table812
- GCC_except_table8136
- GCC_except_table814
- GCC_except_table8166
- GCC_except_table822
- GCC_except_table824
- GCC_except_table826
- GCC_except_table828
- GCC_except_table830
- GCC_except_table8323
- GCC_except_table8325
- GCC_except_table8355
- GCC_except_table8369
- GCC_except_table8385
- GCC_except_table839
- GCC_except_table8399
- GCC_except_table8409
- GCC_except_table841
- GCC_except_table8414
- GCC_except_table843
- GCC_except_table845
- GCC_except_table847
- GCC_except_table849
- GCC_except_table8498
- GCC_except_table851
- GCC_except_table853
- GCC_except_table855
- GCC_except_table857
- GCC_except_table8585
- GCC_except_table859
- GCC_except_table8644
- GCC_except_table8722
- GCC_except_table8737
- GCC_except_table8759
- GCC_except_table8765
- GCC_except_table8784
- GCC_except_table879
- GCC_except_table8794
- GCC_except_table8836
- GCC_except_table8839
- GCC_except_table8843
- GCC_except_table8847
- GCC_except_table885
- GCC_except_table8926
- GCC_except_table894
- GCC_except_table903
- GCC_except_table915
- _CPLSyncSessionPredictionTypeTurboMode
- _objc_msgSend$initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:
- _objc_msgSend$setSession:
CStrings:
+ "%@ failed to discard downloaded %@: %@"
+ "CPLCustomBundleID"
+ "CPLLibraryPaths"
+ "CPLStatusDidChange"
+ "CloudPhotoLibrary-912.0.111"
+ "Discarding %@ but the file is not present in the resource storage any more: %@"
+ "Handling CPL status change"
+ "Trying to discard a downloaded resource while the library is not open"
+ "com.apple.VisualIntelligence"
+ "com.apple.campo"
+ "com.apple.photos.asc.e2ee.secure"
+ "turbo"
+ "\xf0A"
- "CloudPhotoLibrary-910.33.102"
- "com.apple.photos.asc.e2ee"
- "turboMode"
- "\xf01"
```

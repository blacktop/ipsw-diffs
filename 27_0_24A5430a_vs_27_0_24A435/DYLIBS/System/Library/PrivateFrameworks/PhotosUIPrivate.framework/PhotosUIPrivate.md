## PhotosUIPrivate

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0x58aec4
-  __TEXT.__objc_methlist: 0x5057c
-  __TEXT.__const: 0x19740
+912.0.235.0.0
+  __TEXT.__text: 0x5ab904
+  __TEXT.__objc_methlist: 0x5091c
+  __TEXT.__const: 0x1a248
   __TEXT.__dlopen_cstrs: 0x69b
-  __TEXT.__swift5_typeref: 0x16768
-  __TEXT.__constg_swiftt: 0xac04
-  __TEXT.__swift5_builtin: 0x708
-  __TEXT.__swift5_reflstr: 0x8667
-  __TEXT.__swift5_fieldmd: 0x70c8
-  __TEXT.__swift5_assocty: 0x18d0
-  __TEXT.__swift5_capture: 0x4d5c
-  __TEXT.__swift5_proto: 0xc04
-  __TEXT.__swift5_types: 0x774
-  __TEXT.__oslogstring: 0x14e37
-  __TEXT.__cstring: 0x34b80
-  __TEXT.__swift_as_entry: 0x264
-  __TEXT.__swift_as_ret: 0x264
-  __TEXT.__swift_as_cont: 0x588
+  __TEXT.__swift5_typeref: 0x170ba
+  __TEXT.__constg_swiftt: 0xadd0
+  __TEXT.__swift5_builtin: 0x730
+  __TEXT.__swift5_reflstr: 0x89f7
+  __TEXT.__swift5_fieldmd: 0x7300
+  __TEXT.__swift5_assocty: 0x1918
+  __TEXT.__swift5_capture: 0x52b8
+  __TEXT.__swift5_proto: 0xc3c
+  __TEXT.__swift5_types: 0x790
+  __TEXT.__oslogstring: 0x15348
+  __TEXT.__cstring: 0x35731
+  __TEXT.__swift_as_entry: 0x2d4
+  __TEXT.__swift_as_ret: 0x2fc
+  __TEXT.__swift_as_cont: 0x6c8
   __TEXT.__swift5_protos: 0x74
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x8878
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__gcc_except_tab: 0x8b3c
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0x182c8
-  __TEXT.__eh_frame: 0x7408
+  __TEXT.__unwind_info: 0x18c40
+  __TEXT.__eh_frame: 0x89f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc450
-  __DATA_CONST.__objc_classlist: 0x1e48
+  __DATA_CONST.__const: 0xc5f0
+  __DATA_CONST.__objc_classlist: 0x1e58
   __DATA_CONST.__objc_catlist: 0x1b0
   __DATA_CONST.__objc_catlist2: 0x10
-  __DATA_CONST.__objc_protolist: 0x1428
+  __DATA_CONST.__objc_protolist: 0x1430
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a6e0
+  __DATA_CONST.__objc_selrefs: 0x2aa20
   __DATA_CONST.__objc_protorefs: 0x508
   __DATA_CONST.__objc_superrefs: 0x10f0
   __DATA_CONST.__vfx_script_tbl: 0x10
-  __DATA_CONST.__objc_arraydata: 0x15f8
-  __DATA_CONST.__got: 0x5760
-  __AUTH_CONST.__const: 0x17a10
-  __AUTH_CONST.__cfstring: 0x269a0
-  __AUTH_CONST.__objc_const: 0x858f0
+  __DATA_CONST.__objc_arraydata: 0x1630
+  __DATA_CONST.__got: 0x5898
+  __AUTH_CONST.__const: 0x188d0
+  __AUTH_CONST.__cfstring: 0x26e60
+  __AUTH_CONST.__objc_const: 0x86100
   __AUTH_CONST.__objc_arrayobj: 0xed0
-  __AUTH_CONST.__objc_intobj: 0x1638
+  __AUTH_CONST.__objc_intobj: 0x1668
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__auth_got: 0x54e0
-  __AUTH.__objc_data: 0x19180
-  __AUTH.__data: 0x4fb8
-  __DATA.__objc_ivar: 0x5ce0
-  __DATA.__data: 0x14268
+  __AUTH_CONST.__auth_got: 0x5658
+  __AUTH.__objc_data: 0x192b0
+  __AUTH.__data: 0x5178
+  __DATA.__objc_ivar: 0x5d28
+  __DATA.__data: 0x14618
   __DATA.__objc_stublist: 0x28
-  __DATA.__common: 0x358
-  __DATA_DIRTY.__objc_data: 0x22c0
-  __DATA_DIRTY.__data: 0x220
+  __DATA.__common: 0x360
+  __DATA_DIRTY.__objc_data: 0x22d8
+  __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 41801
-  Symbols:   67620
-  CStrings:  8030
+  Functions: 42678
+  Symbols:   67978
+  CStrings:  8122
 
Symbols:
+ +[PUPhotoEditEffectsSupport _setTextureStyleWithPreset:intensity:grain:forCompositionController:]
+ +[PUPhotoEditEffectsSupport updateCompositionController:withTexturePreset:intensity:grain:]
+ -[PUActivityAssetItem excludeProvenance]
+ -[PUActivityAssetItem setExcludeProvenance:]
+ -[PUActivityItemSourceController setShouldExcludeProvenanceDataInAllItemSources:]
+ -[PUActivityItemSourceController shouldExcludeProvenanceDataInAllItemSources]
+ -[PUActivityViewController _precomputePCCAnalytics]
+ -[PUActivityViewController _presentProvenanceSensitiveEditsDetectedAlertForActivity:withCompletionHandler:]
+ -[PUActivityViewController excludeProvenance]
+ -[PUActivityViewController setExcludeProvenance:]
+ -[PUAssetViewModel isViewingProvenance]
+ -[PUAssetViewModel provenanceViewerState]
+ -[PUAssetViewModel setProvenanceViewerState:]
+ -[PUAssetViewModelChange provenanceViewerStateChanged]
+ -[PUAssetViewModelChange setProvenanceViewerStateChanged:]
+ -[PUBrowsingViewModel provenanceOverlayController]
+ -[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]
+ -[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]
+ -[PUOneUpImageTileViewController _removeProvenanceInformativeOverlayForAssetViewModel:]
+ -[PUOneUpImageTileViewController _toggleProvenanceCompareForCurrentAsset]
+ -[PUOneUpImageTileViewController _updateProvenanceCompareTapGestureRecognizer]
+ -[PUOneUpImageTileViewController _updateProvenanceImageOverride]
+ -[PUOneUpImageTileViewController _updateProvenanceOverlayView]
+ -[PUOneUpImageTileViewController allowAnimatedResizeForNextInvalidation]
+ -[PUOneUpImageTileViewController beginProvenanceRevealResizeAnimation]
+ -[PUOneUpImageTileViewController setAllowAnimatedResizeForNextInvalidation:]
+ -[PUOneUpSettings setSimulateCinematicResourceLoading:]
+ -[PUOneUpSettings simulateCinematicResourceLoading]
+ -[PUOneUpViewController oneUpActionsControllerDidRequestShowProvenanceMetadata]
+ -[PUOneUpViewController provenanceOverlayController:didChangeFetcherState:forAsset:]
+ -[PUOneUpViewController provenanceOverlayController:didFailWithError:forAsset:]
+ -[PUPhotoEditMediaToolController _isCinematicCapableRegularVideo]
+ -[PUPhotoEditMediaToolController _isCinematicCapableVideo]
+ -[PUPhotoEditProtoSettings cinematicVideoUseRefinedCinematography]
+ -[PUPhotoEditProtoSettings setCinematicVideoUseRefinedCinematography:]
+ -[PUPhotoEditProtoSettings setSimulateCinematicResourceLoading:]
+ -[PUPhotoEditProtoSettings setTextureStyleBottomLayout:]
+ -[PUPhotoEditProtoSettings setUseNewStylesThumbnailsBehavior:]
+ -[PUPhotoEditProtoSettings simulateCinematicResourceLoading]
+ -[PUPhotoEditProtoSettings textureStyleBottomLayout]
+ -[PUPhotoEditProtoSettings useNewStylesThumbnailsBehavior]
+ -[PUPhotoEditViewController _onCinematicResourceDownloadDidComplete:error:]
+ -[PUPhotoEditViewController cinematicResourceLoadAlert]
+ -[PUPhotoEditViewController convertToCinematicVideo]
+ -[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]
+ -[PUPhotoEditViewController isCinematicResourceDownloadCancelled]
+ -[PUPhotoEditViewController isDownloadingCinematicResources]
+ -[PUPhotoEditViewController setCinematicResourceLoadAlert:]
+ -[PUPhotoEditViewController setIsCinematicResourceDownloadCancelled:]
+ -[PUPhotoEditViewController setIsDownloadingCinematicResources:]
+ -[PUPhotoPickerRemoteViewController _confirmProvenanceWarning:completionHandler:]
+ -[PUPhotosDetailsViewController widgetTapped:]
+ -[PUPickerAssetPreparationOptions initWithIncludeLocation:includeCaption:includeKeywords:includeProvenance:userEncodingPolicy:]
+ -[PUPickerAssetPreparationOptions shouldIncludeProvenance]
+ -[PUPickerConfiguration canIncludeProvenanceByDefault]
+ -[PUPickerPrincipalUIViewController confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:]
+ GCC_except_table10045
+ GCC_except_table10049
+ GCC_except_table10053
+ GCC_except_table10071
+ GCC_except_table10238
+ GCC_except_table10255
+ GCC_except_table10266
+ GCC_except_table10267
+ GCC_except_table10297
+ GCC_except_table10365
+ GCC_except_table10405
+ GCC_except_table10407
+ GCC_except_table10414
+ GCC_except_table10418
+ GCC_except_table10424
+ GCC_except_table10521
+ GCC_except_table10579
+ GCC_except_table1058
+ GCC_except_table10612
+ GCC_except_table10877
+ GCC_except_table10879
+ GCC_except_table10994
+ GCC_except_table1103
+ GCC_except_table11101
+ GCC_except_table1120
+ GCC_except_table11264
+ GCC_except_table1127
+ GCC_except_table11305
+ GCC_except_table11334
+ GCC_except_table11342
+ GCC_except_table11386
+ GCC_except_table11387
+ GCC_except_table11389
+ GCC_except_table11390
+ GCC_except_table11393
+ GCC_except_table11397
+ GCC_except_table11418
+ GCC_except_table11760
+ GCC_except_table11766
+ GCC_except_table11770
+ GCC_except_table11839
+ GCC_except_table1203
+ GCC_except_table1207
+ GCC_except_table12185
+ GCC_except_table12186
+ GCC_except_table1221
+ GCC_except_table1222
+ GCC_except_table12237
+ GCC_except_table1224
+ GCC_except_table12241
+ GCC_except_table1232
+ GCC_except_table12532
+ GCC_except_table12549
+ GCC_except_table12562
+ GCC_except_table12576
+ GCC_except_table12596
+ GCC_except_table1263
+ GCC_except_table12645
+ GCC_except_table1265
+ GCC_except_table1268
+ GCC_except_table12800
+ GCC_except_table12818
+ GCC_except_table12823
+ GCC_except_table12826
+ GCC_except_table12829
+ GCC_except_table12840
+ GCC_except_table12890
+ GCC_except_table12899
+ GCC_except_table12907
+ GCC_except_table12947
+ GCC_except_table12983
+ GCC_except_table12999
+ GCC_except_table13001
+ GCC_except_table13037
+ GCC_except_table13130
+ GCC_except_table13135
+ GCC_except_table1321
+ GCC_except_table1329
+ GCC_except_table13403
+ GCC_except_table13478
+ GCC_except_table13492
+ GCC_except_table13499
+ GCC_except_table13515
+ GCC_except_table13516
+ GCC_except_table13519
+ GCC_except_table13526
+ GCC_except_table13641
+ GCC_except_table13643
+ GCC_except_table13705
+ GCC_except_table13747
+ GCC_except_table13809
+ GCC_except_table13834
+ GCC_except_table13850
+ GCC_except_table13865
+ GCC_except_table13889
+ GCC_except_table13917
+ GCC_except_table13939
+ GCC_except_table13972
+ GCC_except_table13983
+ GCC_except_table13992
+ GCC_except_table14005
+ GCC_except_table14017
+ GCC_except_table14022
+ GCC_except_table14024
+ GCC_except_table14029
+ GCC_except_table14030
+ GCC_except_table14031
+ GCC_except_table14051
+ GCC_except_table14098
+ GCC_except_table14322
+ GCC_except_table14466
+ GCC_except_table14553
+ GCC_except_table14576
+ GCC_except_table14587
+ GCC_except_table14611
+ GCC_except_table14614
+ GCC_except_table14622
+ GCC_except_table14624
+ GCC_except_table14672
+ GCC_except_table14724
+ GCC_except_table15092
+ GCC_except_table1538
+ GCC_except_table15531
+ GCC_except_table15532
+ GCC_except_table15541
+ GCC_except_table15544
+ GCC_except_table15547
+ GCC_except_table15555
+ GCC_except_table15590
+ GCC_except_table15625
+ GCC_except_table15703
+ GCC_except_table1573
+ GCC_except_table15781
+ GCC_except_table15787
+ GCC_except_table15791
+ GCC_except_table1583
+ GCC_except_table15831
+ GCC_except_table15884
+ GCC_except_table15885
+ GCC_except_table15894
+ GCC_except_table15903
+ GCC_except_table15908
+ GCC_except_table15910
+ GCC_except_table15942
+ GCC_except_table15954
+ GCC_except_table15962
+ GCC_except_table15964
+ GCC_except_table15968
+ GCC_except_table15971
+ GCC_except_table15975
+ GCC_except_table15978
+ GCC_except_table15980
+ GCC_except_table15982
+ GCC_except_table15987
+ GCC_except_table16006
+ GCC_except_table16013
+ GCC_except_table16017
+ GCC_except_table16028
+ GCC_except_table16039
+ GCC_except_table16087
+ GCC_except_table16160
+ GCC_except_table16164
+ GCC_except_table16278
+ GCC_except_table16281
+ GCC_except_table16287
+ GCC_except_table16320
+ GCC_except_table16337
+ GCC_except_table16395
+ GCC_except_table16425
+ GCC_except_table16482
+ GCC_except_table16503
+ GCC_except_table16518
+ GCC_except_table16600
+ GCC_except_table16601
+ GCC_except_table16620
+ GCC_except_table16629
+ GCC_except_table16636
+ GCC_except_table16643
+ GCC_except_table16649
+ GCC_except_table16659
+ GCC_except_table16666
+ GCC_except_table16850
+ GCC_except_table16861
+ GCC_except_table16864
+ GCC_except_table16866
+ GCC_except_table16873
+ GCC_except_table16875
+ GCC_except_table16877
+ GCC_except_table16880
+ GCC_except_table16895
+ GCC_except_table16962
+ GCC_except_table16971
+ GCC_except_table16972
+ GCC_except_table16999
+ GCC_except_table170
+ GCC_except_table17004
+ GCC_except_table17202
+ GCC_except_table17227
+ GCC_except_table17390
+ GCC_except_table17497
+ GCC_except_table17498
+ GCC_except_table17625
+ GCC_except_table17659
+ GCC_except_table17701
+ GCC_except_table17706
+ GCC_except_table17735
+ GCC_except_table17737
+ GCC_except_table17739
+ GCC_except_table17885
+ GCC_except_table17888
+ GCC_except_table17897
+ GCC_except_table180
+ GCC_except_table18084
+ GCC_except_table18085
+ GCC_except_table18119
+ GCC_except_table18138
+ GCC_except_table18140
+ GCC_except_table18205
+ GCC_except_table18278
+ GCC_except_table18295
+ GCC_except_table18296
+ GCC_except_table18299
+ GCC_except_table18306
+ GCC_except_table18307
+ GCC_except_table18315
+ GCC_except_table18328
+ GCC_except_table18336
+ GCC_except_table18347
+ GCC_except_table18493
+ GCC_except_table18495
+ GCC_except_table18497
+ GCC_except_table18505
+ GCC_except_table18795
+ GCC_except_table18796
+ GCC_except_table18815
+ GCC_except_table18817
+ GCC_except_table18846
+ GCC_except_table18857
+ GCC_except_table18866
+ GCC_except_table18881
+ GCC_except_table18882
+ GCC_except_table18886
+ GCC_except_table18895
+ GCC_except_table18905
+ GCC_except_table1892
+ GCC_except_table19023
+ GCC_except_table19035
+ GCC_except_table19083
+ GCC_except_table19093
+ GCC_except_table19108
+ GCC_except_table19111
+ GCC_except_table19113
+ GCC_except_table19115
+ GCC_except_table19116
+ GCC_except_table19121
+ GCC_except_table19204
+ GCC_except_table19211
+ GCC_except_table19292
+ GCC_except_table19307
+ GCC_except_table19365
+ GCC_except_table19420
+ GCC_except_table19580
+ GCC_except_table19597
+ GCC_except_table19777
+ GCC_except_table1991
+ GCC_except_table19943
+ GCC_except_table2
+ GCC_except_table20031
+ GCC_except_table20055
+ GCC_except_table20463
+ GCC_except_table20467
+ GCC_except_table20476
+ GCC_except_table20480
+ GCC_except_table20498
+ GCC_except_table20509
+ GCC_except_table20559
+ GCC_except_table20608
+ GCC_except_table20859
+ GCC_except_table21007
+ GCC_except_table21012
+ GCC_except_table21153
+ GCC_except_table21163
+ GCC_except_table21208
+ GCC_except_table21262
+ GCC_except_table21263
+ GCC_except_table21353
+ GCC_except_table21544
+ GCC_except_table21548
+ GCC_except_table21627
+ GCC_except_table21628
+ GCC_except_table21636
+ GCC_except_table21715
+ GCC_except_table21749
+ GCC_except_table21831
+ GCC_except_table21832
+ GCC_except_table21886
+ GCC_except_table2200
+ GCC_except_table2201
+ GCC_except_table22012
+ GCC_except_table2203
+ GCC_except_table2212
+ GCC_except_table22207
+ GCC_except_table22208
+ GCC_except_table22225
+ GCC_except_table22229
+ GCC_except_table22252
+ GCC_except_table22364
+ GCC_except_table2263
+ GCC_except_table22683
+ GCC_except_table22724
+ GCC_except_table2281
+ GCC_except_table22817
+ GCC_except_table22841
+ GCC_except_table22856
+ GCC_except_table22976
+ GCC_except_table23012
+ GCC_except_table23015
+ GCC_except_table23017
+ GCC_except_table23022
+ GCC_except_table23054
+ GCC_except_table23060
+ GCC_except_table23125
+ GCC_except_table23141
+ GCC_except_table2326
+ GCC_except_table2334
+ GCC_except_table2335
+ GCC_except_table2336
+ GCC_except_table2338
+ GCC_except_table23410
+ GCC_except_table23414
+ GCC_except_table23416
+ GCC_except_table23423
+ GCC_except_table23424
+ GCC_except_table23426
+ GCC_except_table23427
+ GCC_except_table23429
+ GCC_except_table2350
+ GCC_except_table23531
+ GCC_except_table23633
+ GCC_except_table23670
+ GCC_except_table2373
+ GCC_except_table23732
+ GCC_except_table23833
+ GCC_except_table23840
+ GCC_except_table23842
+ GCC_except_table23844
+ GCC_except_table23863
+ GCC_except_table23868
+ GCC_except_table23874
+ GCC_except_table23890
+ GCC_except_table2390
+ GCC_except_table2392
+ GCC_except_table2396
+ GCC_except_table2398
+ GCC_except_table24091
+ GCC_except_table24114
+ GCC_except_table24125
+ GCC_except_table24230
+ GCC_except_table2427
+ GCC_except_table24285
+ GCC_except_table24292
+ GCC_except_table24296
+ GCC_except_table24310
+ GCC_except_table24313
+ GCC_except_table24444
+ GCC_except_table24472
+ GCC_except_table24489
+ GCC_except_table24539
+ GCC_except_table2464
+ GCC_except_table24699
+ GCC_except_table24768
+ GCC_except_table24778
+ GCC_except_table24786
+ GCC_except_table25002
+ GCC_except_table25018
+ GCC_except_table278
+ GCC_except_table2793
+ GCC_except_table2795
+ GCC_except_table2851
+ GCC_except_table2855
+ GCC_except_table2858
+ GCC_except_table29
+ GCC_except_table2946
+ GCC_except_table2971
+ GCC_except_table2972
+ GCC_except_table2980
+ GCC_except_table30
+ GCC_except_table3032
+ GCC_except_table3090
+ GCC_except_table3093
+ GCC_except_table323
+ GCC_except_table33
+ GCC_except_table3303
+ GCC_except_table3335
+ GCC_except_table3358
+ GCC_except_table3381
+ GCC_except_table3384
+ GCC_except_table3831
+ GCC_except_table3834
+ GCC_except_table3840
+ GCC_except_table39
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table3969
+ GCC_except_table4017
+ GCC_except_table4037
+ GCC_except_table4075
+ GCC_except_table4078
+ GCC_except_table4079
+ GCC_except_table4080
+ GCC_except_table4083
+ GCC_except_table412
+ GCC_except_table4160
+ GCC_except_table4162
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table424
+ GCC_except_table4295
+ GCC_except_table44
+ GCC_except_table440
+ GCC_except_table4412
+ GCC_except_table442
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4488
+ GCC_except_table45
+ GCC_except_table4515
+ GCC_except_table4622
+ GCC_except_table4637
+ GCC_except_table4796
+ GCC_except_table4819
+ GCC_except_table4906
+ GCC_except_table50
+ GCC_except_table5099
+ GCC_except_table5150
+ GCC_except_table5159
+ GCC_except_table5166
+ GCC_except_table5167
+ GCC_except_table5168
+ GCC_except_table5190
+ GCC_except_table5212
+ GCC_except_table5316
+ GCC_except_table5435
+ GCC_except_table5442
+ GCC_except_table559
+ GCC_except_table562
+ GCC_except_table5841
+ GCC_except_table5879
+ GCC_except_table5899
+ GCC_except_table5901
+ GCC_except_table5911
+ GCC_except_table5942
+ GCC_except_table5966
+ GCC_except_table5992
+ GCC_except_table6015
+ GCC_except_table6049
+ GCC_except_table6059
+ GCC_except_table6343
+ GCC_except_table6345
+ GCC_except_table6348
+ GCC_except_table6349
+ GCC_except_table6356
+ GCC_except_table6489
+ GCC_except_table6541
+ GCC_except_table6545
+ GCC_except_table6548
+ GCC_except_table6565
+ GCC_except_table6597
+ GCC_except_table6661
+ GCC_except_table6691
+ GCC_except_table6698
+ GCC_except_table6769
+ GCC_except_table6800
+ GCC_except_table6905
+ GCC_except_table6909
+ GCC_except_table6912
+ GCC_except_table6915
+ GCC_except_table6982
+ GCC_except_table6994
+ GCC_except_table7004
+ GCC_except_table7008
+ GCC_except_table7157
+ GCC_except_table7166
+ GCC_except_table7174
+ GCC_except_table7248
+ GCC_except_table7303
+ GCC_except_table7311
+ GCC_except_table7453
+ GCC_except_table7469
+ GCC_except_table7504
+ GCC_except_table7510
+ GCC_except_table7515
+ GCC_except_table7523
+ GCC_except_table7528
+ GCC_except_table7533
+ GCC_except_table7562
+ GCC_except_table7683
+ GCC_except_table7684
+ GCC_except_table796
+ GCC_except_table8087
+ GCC_except_table815
+ GCC_except_table8160
+ GCC_except_table817
+ GCC_except_table8272
+ GCC_except_table8279
+ GCC_except_table8285
+ GCC_except_table8350
+ GCC_except_table8380
+ GCC_except_table8381
+ GCC_except_table841
+ GCC_except_table843
+ GCC_except_table8536
+ GCC_except_table8725
+ GCC_except_table8733
+ GCC_except_table8734
+ GCC_except_table8749
+ GCC_except_table8750
+ GCC_except_table8765
+ GCC_except_table8777
+ GCC_except_table8783
+ GCC_except_table8802
+ GCC_except_table8806
+ GCC_except_table8832
+ GCC_except_table8884
+ GCC_except_table9012
+ GCC_except_table9096
+ GCC_except_table9101
+ GCC_except_table9144
+ GCC_except_table9228
+ GCC_except_table9240
+ GCC_except_table9280
+ GCC_except_table9305
+ GCC_except_table9349
+ GCC_except_table9376
+ GCC_except_table9390
+ GCC_except_table9397
+ GCC_except_table9437
+ GCC_except_table9450
+ GCC_except_table9452
+ GCC_except_table9456
+ GCC_except_table9457
+ GCC_except_table951
+ GCC_except_table952
+ GCC_except_table9523
+ GCC_except_table9526
+ GCC_except_table954
+ GCC_except_table966
+ GCC_except_table9664
+ GCC_except_table9669
+ GCC_except_table967
+ GCC_except_table9671
+ GCC_except_table9720
+ GCC_except_table9794
+ GCC_except_table9803
+ GCC_except_table985
+ GCC_except_table992
+ GCC_except_table9945
+ GCC_except_table9997
+ _CPAnalyticsEventPCCShareCompleted
+ _OBJC_CLASS_$_PHImportAsset
+ _OBJC_CLASS_$_PITextureStyleAutoCalculator
+ _OBJC_CLASS_$_PXCinematicResourceManager
+ _OBJC_CLASS_$_PXProvenanceOverlayController
+ _OBJC_CLASS_$_UIGraphicsImageRendererFormat
+ _OBJC_CLASS_$__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ _OBJC_IVAR_$_PUActivityAssetItem._excludeProvenance
+ _OBJC_IVAR_$_PUActivityItemSourceController._shouldExcludeProvenanceDataInAllItemSources
+ _OBJC_IVAR_$_PUActivityViewController._excludeProvenance
+ _OBJC_IVAR_$_PUActivityViewController._unprocessedProvenanceAssetCount
+ _OBJC_IVAR_$_PUAssetViewModel._provenanceViewerState
+ _OBJC_IVAR_$_PUAssetViewModelChange._provenanceViewerStateChanged
+ _OBJC_IVAR_$_PUBrowsingViewModel._provenanceOverlayController
+ _OBJC_IVAR_$_PUOneUpImageTileViewController._allowAnimatedResizeForNextInvalidation
+ _OBJC_IVAR_$_PUOneUpSettings._simulateCinematicResourceLoading
+ _OBJC_IVAR_$_PUPhotoEditMediaToolController._cinematicModelProgress
+ _OBJC_IVAR_$_PUPhotoEditProtoSettings._simulateCinematicResourceLoading
+ _OBJC_IVAR_$_PUPhotoEditProtoSettings._textureStyleBottomLayout
+ _OBJC_IVAR_$_PUPhotoEditProtoSettings._useNewStylesThumbnailsBehavior
+ _OBJC_IVAR_$_PUPhotoEditViewController._cinematicResourceLoadAlert
+ _OBJC_IVAR_$_PUPhotoEditViewController._hasPerformedCinematicConversion
+ _OBJC_IVAR_$_PUPhotoEditViewController._isCinematicResourceDownloadCancelled
+ _OBJC_IVAR_$_PUPhotoEditViewController._isDownloadingCinematicResources
+ _OBJC_IVAR_$_PUPickerAssetPreparationOptions._shouldIncludeProvenance
+ _OBJC_METACLASS_$__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ _PAMediaConversionErrorIsTransient
+ _PAMediaConversionIsProvenanceEligibilityError
+ _PIGeneratedTilesAdjustmentKey
+ _PIPortraitVideoAdjustmentKey
+ _PITextureStyleAdjustmentKey
+ _PLShouldExcludeProvenanceWhenSharing
+ _PUCanRenderCinematicEverywhere
+ _PUProvenanceAssetsContainSensitiveEdits
+ _PUProvenanceAssetsContainSensitiveEdits.onceToken
+ _PUProvenanceAssetsContainSensitiveEdits.sensitiveAdjustments
+ _PXAssetEditOperationTypeDisableCinematicVideo
+ _PXAssetEditOperationTypeEnableCinematicVideo
+ _PXCinematicResourceManagerErrorDomain
+ _PXPhotosFileProviderRegisterConfigurationSetShouldIncludeProvenance
+ _PXProvenanceSFSymbolName
+ _PXWidgetIdentifierImageProvenance
+ _UIFontDescriptorSystemDesignRounded
+ _UIFontWidthCompressed
+ __DATA__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ __DATA__TtC15PhotosUIPrivate41PUCinematicOneUpResourceLoadingController
+ __INSTANCE_METHODS__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ __IVARS__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ __IVARS__TtC15PhotosUIPrivate41PUCinematicOneUpResourceLoadingController
+ __METACLASS_DATA__TtC15PhotosUIPrivate38PUCinematicVideoEditOperationPerformer
+ __METACLASS_DATA__TtC15PhotosUIPrivate41PUCinematicOneUpResourceLoadingController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PXProvenanceOverlayControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PXProvenanceOverlayControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_PXProvenanceOverlayControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_PXProvenanceOverlayControllerDelegate
+ __OBJC_PROTOCOL_$_PXProvenanceOverlayControllerDelegate
+ ___107-[PUActivityViewController _presentProvenanceSensitiveEditsDetectedAlertForActivity:withCompletionHandler:]_block_invoke
+ ___107-[PUActivityViewController _presentProvenanceSensitiveEditsDetectedAlertForActivity:withCompletionHandler:]_block_invoke_2
+ ___107-[PUActivityViewController _presentProvenanceSensitiveEditsDetectedAlertForActivity:withCompletionHandler:]_block_invoke_3
+ ___126-[PUPickerPrincipalUIViewController confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:]_block_invoke
+ ___126-[PUPickerPrincipalUIViewController confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:]_block_invoke_2
+ ___126-[PUPickerPrincipalUIViewController confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:]_block_invoke_3
+ ___42-[PUEditAIFeedbackController menuElements]_block_invoke
+ ___45-[PUActivityViewController _performActivity:]_block_invoke_7
+ ___46-[PUPhotosDetailsViewController widgetTapped:]_block_invoke
+ ___53-[PUPhotoEditMediaToolController didBecomeActiveTool]_block_invoke
+ ___58-[PUImportActionCoordinator _importItems:allowDuplicates:]_block_invoke
+ ___61-[PUPhotoEditMediaToolController _handlePortraitVideoButton:]_block_invoke
+ ___64-[PUPhotoEditViewController _continueLoadingWithAutocalculators]_block_invoke_4
+ ___67+[PUPhotoEditEffectsSupport _clearStylesWithCompositionController:]_block_invoke_2
+ ___73-[PUOneUpImageTileViewController _toggleProvenanceCompareForCurrentAsset]_block_invoke
+ ___74-[PUActivityViewController _customizationGroupsForActivityViewController:]_block_invoke_11
+ ___75-[PUPhotoEditViewController _onCinematicResourceDownloadDidComplete:error:]_block_invoke
+ ___78-[PUOneUpImageTileViewController _updateProvenanceCompareTapGestureRecognizer]_block_invoke
+ ___79-[PUOneUpViewController provenanceOverlayController:didFailWithError:forAsset:]_block_invoke
+ ___81-[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]_block_invoke
+ ___81-[PUImportActionCoordinator _importItemsContainProvenanceData:completionHandler:]_block_invoke_2
+ ___81-[PUPhotoPickerRemoteViewController _confirmProvenanceWarning:completionHandler:]_block_invoke
+ ___81-[PUPhotoPickerRemoteViewController _confirmProvenanceWarning:completionHandler:]_block_invoke_2
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_2
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_3
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_4
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_5
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_6
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_7
+ ___85-[PUPhotoEditViewController downloadCinematicResourcesIfNeededWithCompletionHandler:]_block_invoke_8
+ ___85-[PXAssetEditOperationManager(AdditionalPerformersHook) registerAdditionalPerformers]_block_invoke_3
+ ___87-[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]_block_invoke
+ ___87-[PUImportActionCoordinator _presentProvenanceImportWarningForItems:completionHandler:]_block_invoke_2
+ ___97+[PUPhotoEditEffectsSupport _setTextureStyleWithPreset:intensity:grain:forCompositionController:]_block_invoke
+ ___98+[PUPhotoKitAssetsDataSource badgeInfoPromiseForAsset:assetCollection:spatialPresentationEnabled:]_block_invoke_5
+ ___98-[PUPickerPrincipalUIViewController coordinator:didFinishPicking:additionalSelectionState:action:]_block_invoke_3
+ ___PUProvenanceAssetsContainSensitiveEdits_block_invoke
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80r88r96r104r_e42_v32?0"PUAssetReference"8"NSArray"16^B24ls32l8s40l8r80l8s48l8s56l8s64l8r88l8r96l8r104l8s72l8
+ ___block_descriptor_120_e8_32r40r48r56r64r72r80r88r96r104r112r_e36_v32?0"PUActivityAssetItem"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8
+ ___block_descriptor_32_e44_v16?0"PITextureStyleAdjustmentController"8l
+ ___block_descriptor_32_e45_v16?0"PIPortraitVideoAdjustmentController"8l
+ ___block_descriptor_40_e8_32w_e20_v16?0"NSProgress"8lw32l8
+ ___block_descriptor_41_e8_32w_e20_v20?0B8"NSError"12lw32l8
+ ___block_descriptor_48_e8_32bs40w_e23_v24?0B8B12"NSError"16lw40l8s32l8
+ ___block_descriptor_49_e8_32s_e44_v16?0"PITextureStyleAdjustmentController"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8ls40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40w48w_e23_v16?0"UIAlertAction"8lw40l8s32l8w48l8
+ ___block_descriptor_58_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___swift_closure_destructor.103Tm
+ ___swift_closure_destructor.110Tm
+ ___swift_closure_destructor.167Tm
+ ___swift_closure_destructor.188Tm
+ ___swift_closure_destructor.190Tm
+ ___swift_closure_destructor.214Tm
+ ___swift_closure_destructor.26Tm
+ ___swift_closure_destructor.30Tm
+ ___swift_closure_destructor.70Tm
+ ___swift_closure_destructor.87Tm
+ ___swift_get_extra_inhabitant_index.156Tm
+ ___swift_store_extra_inhabitant_index.157Tm
+ _associated conformance 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC07TextureF033_567B04E452D00D382DBBCD37BC34CF3ALLV7SwiftUI4ViewAA4BodyAgHP_AgH
+ _associated conformance 15PhotosUIPrivate38PUCinematicVideoEditOperationPerformerC5Error33_C7D106D62E07D5D036D95EBF1685AA41LLO10Foundation09LocalizedH0AAsAD
+ _associated conformance 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC18ModelDownloadError33_37D2D234A2B9615F6190E200AAFA4C2ELLO10Foundation09LocalizedK0AAs0K0
+ _associated conformance 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC18ModelDownloadError33_37D2D234A2B9615F6190E200AAFA4C2ELLOSHAASQ
+ _associated conformance So24PXAssetEditOperationTypeaSHSCSQ
+ _associated conformance So24PXAssetEditOperationTypeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So24PXAssetEditOperationTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _get_enum_tag_for_layout_string 15PhotosUIPrivate38PUCinematicVideoEditOperationPerformerC5Error33_C7D106D62E07D5D036D95EBF1685AA41LLO
+ _get_enum_tag_for_layout_string 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC0fG5StateO
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQOyACyACyACyAA6ZStackVyAA05TupleD0VyAeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQOy15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV_ACyALyAWGAA14_OpacityEffectVGQo__AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQOyAT07TextureQ0AVLLV_ACyALyA2_GAZGQo_QPGGAA12_FrameLayoutVGAA12_ScaleEffectVGAA13_OffsetEffectVG_ACyALyA16_GAZGQo_AA23_CompositingGroupEffectVGAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGAA30_EnvironmentKeyWritingModifierVySo0N21EditLayoutOrientationVGGAaDHPA28_AaDHPA22_AaDHPqd0__AaDHD3_A19_HO_A21_AA0E8ModifierHPyHCHC_A27_AAA35_HPyHCHC_A33_AAA35_HPyHCHC
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA6ZStackVyAA05TupleD0VyAA08ModifiedD0VyAA6VStackVyAA6SpacerVGAA12_FrameLayoutVG_AIyAA16ScrollViewReaderVyAA0M0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAU12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQOyAIyAY05PhotovW7ControlVAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGG_Qo__AY05PhotoV11ControlModeOQo_GAA08_PaddingK0VGQPGGAIyAA6HStackVyAGyAIyAY16ExpandableSliderVAA15_HiddenModifierVG_A12_QPGGA2_yAA0K9DirectionOGGGAaTHPA17_AaTHPyHC_A30_AaTHPA26_AaTHPyHC_A29_AA0M8ModifierHPyHCHCHC
+ _get_witness_table 7SwiftUI4FormVyAA12TupleContentVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_A2LSgQPGAA9EmptyViewVG_AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedE0VyAGyAisAE12labelsHiddenQryFQOyAsAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA6_GSiAsAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAI_A6_Qo_GG_AA06InlinetS0VQo__Qo_AA012_ConditionalE0VyAA6VStackVyAIGAPGGAA25_AppearanceActionModifierVG_A6_Qo_SgAGyAisAEAYQryFQOyAsAEAZyQrqd__AAA_Rd__lFQOyA1_yAISo34PXPhotosFileProviderEncodingPolicyVA8_ySayA32_GSiAsAEA10__A11_Qrqd___SbtSHRd__lFQOyAI_A32_Qo_GG_A16_Qo__Qo_AIGSgQPGGAaRHPyHC
+ _objc_msgSend$_confirmProvenanceWarning:completionHandler:
+ _objc_msgSend$_importItemsContainProvenanceData:completionHandler:
+ _objc_msgSend$_isCinematicCapableRegularVideo
+ _objc_msgSend$_isCinematicCapableVideo
+ _objc_msgSend$_onCinematicResourceDownloadDidComplete:error:
+ _objc_msgSend$_precomputePCCAnalytics
+ _objc_msgSend$_presentProvenanceImportWarningForItems:completionHandler:
+ _objc_msgSend$_presentProvenanceSensitiveEditsDetectedAlertForActivity:withCompletionHandler:
+ _objc_msgSend$_removeProvenanceInformativeOverlayForAssetViewModel:
+ _objc_msgSend$_setTextureStyleWithPreset:intensity:grain:forCompositionController:
+ _objc_msgSend$_toggleProvenanceCompareForCurrentAsset
+ _objc_msgSend$_updateProvenanceCompareTapGestureRecognizer
+ _objc_msgSend$_updateProvenanceImageOverride
+ _objc_msgSend$_updateProvenanceOverlayView
+ _objc_msgSend$acknowledgeFailureForAsset:
+ _objc_msgSend$addInformativeOverlayForAsset:toView:visibleImage:animated:
+ _objc_msgSend$adjustmentKeys
+ _objc_msgSend$allowAnimatedResizeForNextInvalidation
+ _objc_msgSend$assetHasCinematicDepthEnabled:queue:handler:
+ _objc_msgSend$beginProvenanceRevealResizeAnimation
+ _objc_msgSend$canIncludeProvenanceByDefault
+ _objc_msgSend$canRenderTextureStylesOnComposition:
+ _objc_msgSend$cancelFetchingForAsset:
+ _objc_msgSend$cinematicCapableVideoConsideredAsCinematic:videoDepthEnabled:
+ _objc_msgSend$cinematicResourceLoadAlert
+ _objc_msgSend$cinematicVideoUseRefinedCinematography
+ _objc_msgSend$classicStandardVideo
+ _objc_msgSend$compareTapGestureRecognizerForAsset:tapHandler:
+ _objc_msgSend$compositionControllerWithoutSource:
+ _objc_msgSend$confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:
+ _objc_msgSend$convertToCinematicVideo
+ _objc_msgSend$defaultFormat
+ _objc_msgSend$displayOverrideImage:imageData:
+ _objc_msgSend$downloadCinematicResourcesIfNeededWithCompletionHandler:
+ _objc_msgSend$downloadResourcesForAsset:progressHandler:completion:
+ _objc_msgSend$drawInRect:blendMode:alpha:
+ _objc_msgSend$enableCinematicEverywhere
+ _objc_msgSend$excludeProvenance
+ _objc_msgSend$fetcherStateForAsset:
+ _objc_msgSend$fontDescriptorWithDesign:
+ _objc_msgSend$forceProvenanceMetadataBaking
+ _objc_msgSend$geometryBasedAdjustmentIdentifiers
+ _objc_msgSend$grainIntensity
+ _objc_msgSend$hasReachedImageLoadedStateForAsset:
+ _objc_msgSend$imageDataForAsset:
+ _objc_msgSend$imageForAsset:
+ _objc_msgSend$imageTileViewController:delegateForGestureRecognizer:
+ _objc_msgSend$imageTileViewControllerViewForAttachingGestureRecognizers:
+ _objc_msgSend$initWithIncludeAllPhotosData:includeLocationData:includeLivePhotoData:includeProvenanceData:
+ _objc_msgSend$initWithIncludeLocation:includeCaption:includeKeywords:includeProvenance:userEncodingPolicy:
+ _objc_msgSend$initWithSize:format:
+ _objc_msgSend$invalidatePrimaryContentTiles
+ _objc_msgSend$isCinematicCapableRegularVideo
+ _objc_msgSend$isCinematicCapableVideo
+ _objc_msgSend$isCinematicResourceDownloadCancelled
+ _objc_msgSend$isDisplayingProvenanceForAsset:
+ _objc_msgSend$isDownloadingCinematicResources
+ _objc_msgSend$isViewingProvenance
+ _objc_msgSend$loadResourceForAsset:networkAccessAllowed:requireLocalResources:forceRunAsUnadjustedAsset:progressHandler:resultHandler:
+ _objc_msgSend$loadResourceForAsset:requireLocalResources:forceRunAsUnadjustedAsset:resultHandler:
+ _objc_msgSend$markInformativeCompareDiscoveredForAsset:
+ _objc_msgSend$metadataViewControllerForAsset:
+ _objc_msgSend$modifyPortraitVideoAdjustment:
+ _objc_msgSend$oneUpActionsControllerDidRequestShowProvenanceMetadata
+ _objc_msgSend$overlayHostView
+ _objc_msgSend$performToggleProvenanceShowMetadataAction
+ _objc_msgSend$performToggleProvenanceViewerAction
+ _objc_msgSend$provenanceOverlayController
+ _objc_msgSend$provenanceState
+ _objc_msgSend$provenanceViewerState
+ _objc_msgSend$provenanceViewerStateChanged
+ _objc_msgSend$reloadItemAtIndexPath:dataSource:
+ _objc_msgSend$removeInformativeOverlayForAsset:fromView:animated:
+ _objc_msgSend$removeOverlayViewForAsset:fromView:animated:
+ _objc_msgSend$requestOriginalAVAssetForPHAsset:networkAccessAllowed:completion:
+ _objc_msgSend$scanAssetsForProvenanceData:atEnd:
+ _objc_msgSend$setAllowAnimatedResizeForNextInvalidation:
+ _objc_msgSend$setCellEffect:
+ _objc_msgSend$setCinematicResourceLoadAlert:
+ _objc_msgSend$setCinematicVideoUseRefinedCinematography:
+ _objc_msgSend$setErrors:forMediaType:
+ _objc_msgSend$setExcludeProvenance:
+ _objc_msgSend$setForceProvenanceMetadataBaking:
+ _objc_msgSend$setGrainIntensity:
+ _objc_msgSend$setGrainIntensityValue:
+ _objc_msgSend$setInitialImage:forAsset:
+ _objc_msgSend$setIsCinematicResourceDownloadCancelled:
+ _objc_msgSend$setIsDownloadingCinematicResources:
+ _objc_msgSend$setOnGrainIntensityValueChanged:
+ _objc_msgSend$setProvenanceViewerState:
+ _objc_msgSend$setProvenanceViewerStateChanged:
+ _objc_msgSend$setShouldExcludeProvenanceDataInAllItemSources:
+ _objc_msgSend$setShouldStripProvenance:
+ _objc_msgSend$setSimulateCinematicResourceLoading:
+ _objc_msgSend$setTextureIntensityValue:
+ _objc_msgSend$setTextureStyleBottomLayout:
+ _objc_msgSend$setUseNewStylesThumbnailsBehavior:
+ _objc_msgSend$shouldExcludeProvenanceDataInAllItemSources
+ _objc_msgSend$shouldIncludeProvenance
+ _objc_msgSend$showGlobalProvenanceExclusionSwitch
+ _objc_msgSend$simulateCinematicResourceLoading
+ _objc_msgSend$snappableWidgetIdentifier
+ _objc_msgSend$statusForAsset:
+ _objc_msgSend$textureStyleAdjustmentController
+ _objc_msgSend$textureStyleBottomLayout
+ _objc_msgSend$updateCompositionController:withTexturePreset:intensity:grain:
+ _objc_msgSend$updateEnabledInteractions
+ _objc_msgSend$updateInformativeOverlayLayoutForView:
+ _objc_msgSend$useNewStylesThumbnailsBehavior
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SDy__________G 12PhotosUIEdit23PhotoStyleTextureEffectV7VariantO AC
+ _symbolic SDy__________G So24UIFontDescriptorTraitKeya 12CoreGraphics7CGFloatV
+ _symbolic SbSo7NSErrorCSgIeyBhyy_
+ _symbolic ScCySo7AVAssetC______pG s5ErrorP
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic SccySo20PEResourceLoadResultC______pG s5ErrorP
+ _symbolic Sccyyt_____G s5NeverO
+ _symbolic So10NSProgressC_SSSg7messaget
+ _symbolic So21PXActionProgressToastCSg
+ _symbolic So26PEPhotoKitMediaDestinationC
+ _symbolic So29PXAssetEditOperationPerformerC
+ _symbolic So30UIGraphicsImageRendererContextCIgg_
+ _symbolic So35PIPortraitVideoAdjustmentControllerCIgg_
+ _symbolic So7UIImageC
+ _symbolic _____ 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic _____ 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC07TextureF033_567B04E452D00D382DBBCD37BC34CF3ALLV
+ _symbolic _____ 15PhotosUIPrivate38PUCinematicVideoEditOperationPerformerC
+ _symbolic _____ 15PhotosUIPrivate38PUCinematicVideoEditOperationPerformerC5Error33_C7D106D62E07D5D036D95EBF1685AA41LLO
+ _symbolic _____ 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC
+ _symbolic _____ 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC0fG5StateO
+ _symbolic _____ 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC18ModelDownloadError33_37D2D234A2B9615F6190E200AAFA4C2ELLO
+ _symbolic _____ So24PXAssetEditOperationTypea
+ _symbolic _____Iegn_ 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic _____Sg 10Foundation16AttributedStringV
+ _symbolic _____Sg 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic _____Sg So24PXAssetEditOperationTypea
+ _symbolic _____Sg13operationType_t So24PXAssetEditOperationTypea
+ _symbolic _____SgXw 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC
+ _symbolic _____SgXwz_Xx 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC
+ _symbolic _____XDXMT 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC
+ _symbolic _____yAAyAAy_____yAAyAAyAAy_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G_____G_____G_AAyAEyAUGAGGQo______G_____y_____GG_____y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AA05TupleD0V AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV AA23_CompositingGroupEffectV AA21_TraitWritingModifierV AA18TransitionTraitKeyV AA30_EnvironmentKeyWritingModifierV So0N21EditLayoutOrientationV
+ _symbolic _____yAAyAAy_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G_____G_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdG0VyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AP AA14_OpacityEffectV AiAEAJ_AKQrAN_qd__AQXEtAaHRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV AA4TextV AA14_OpacityEffectV AA16_FixedSizeLayoutV
+ _symbolic _____yAAy_____yAAyAAyAAy_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G_____G_____G_AAyAEyAUGAGGQo______G_____y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AA05TupleD0V AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV AA23_CompositingGroupEffectV AA21_TraitWritingModifierV AA18TransitionTraitKeyV
+ _symbolic _____yAAy_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdG0VyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AP AA14_OpacityEffectV AiAEAJ_AKQrAN_qd__AQXEtAaHRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV
+ _symbolic _____y_____G 7SwiftUI22PlaceholderContentViewV 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC07TextureK033_567B04E452D00D382DBBCD37BC34CF3ALLV
+ _symbolic _____y_____G 7SwiftUI7BindingV 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12PhotosUIEdit23PhotoStyleTextureEffectV7VariantO
+ _symbolic _____y_____GSg 7SwiftUI6ToggleV AA4TextV
+ _symbolic _____y_____G_A2CSgt 7SwiftUI6ToggleV AA4TextV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 12PhotosUIEdit16ExpandableSliderV AA15_HiddenModifierV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA4TextV AA14_OpacityEffectV
+ _symbolic _____y__________G s17_NativeDictionaryV 12PhotosUIEdit23PhotoStyleTextureEffectV7VariantO AE
+ _symbolic _____y__________G______y_____y_____yAAy__________y_____SgGG_Qo_______Qo_Gt 7SwiftUI15ModifiedContentV 12PhotosUIEdit16ExpandableSliderV AA15_HiddenModifierV AA16ScrollViewReaderV AA0L0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AlDE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AD05PhotosT7ControlV AA022_EnvironmentKeyWritingJ0V AA5ColorV AD0ysZ4ModeO
+ _symbolic _____y___________G 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV 12PhotosUIEdit16ExpandableSliderV
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC So24UIFontDescriptorTraitKeya 12CoreGraphics7CGFloatV
+ _symbolic _____y___________y_____yAAG_____GQo_ 7SwiftUI4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA018PlaceholderContentC0VyxGXEtAaBRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorN033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedH0V AJ AA14_OpacityEffectV
+ _symbolic _____y___________y_____yAAG_____GQo_ 7SwiftUI4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA018PlaceholderContentC0VyxGXEtAaBRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC07TextureN033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedH0V AJ AA14_OpacityEffectV
+ _symbolic _____y___________y_____yAAG_____GQo_______y______AByACyAHGAEGQo_t 7SwiftUI4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA018PlaceholderContentC0VyxGXEtAaBRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorN033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedH0V AJ AA14_OpacityEffectV AcAEAD_AEQrAH_qd__AKXEtAaBRd__lFQO AN07TextureN0APLLV
+ _symbolic _____y___________y_____y__________G______y_____y_____yADy__________y_____SgGG_Qo_______Qo_GQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA08ModifiedI0V 12PhotosUIEdit16ExpandableSliderV AA15_HiddenModifierV AA06ScrollD6ReaderV AA0D0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AtLE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AL05PhotoxY7ControlV AA022_EnvironmentKeyWritingP0V AA5ColorV AL05PhotoX11ControlModeO
+ _symbolic _____y___________y_____y___________y_____yADG_____GQo_______y______AEyAFyAKGAHGQo_QPGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA12TupleContentV AA0D0PAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderiD0VyxGXEtAaJRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorS033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedI0V AR AA14_OpacityEffectV AkAEAL_AMQrAP_qd__ASXEtAaJRd__lFQO AV07TextureS0AXLLV
+ _symbolic _____y__________y_____SgGG 7SwiftUI15ModifiedContentV 12PhotosUIEdit24PhotoStyleTextureControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV
+ _symbolic _____y__________y_____yABG_A2ESgQPG_____G 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV
+ _symbolic _____y__________y_____yABG_A2ESgQPG_____G______y_____yAAyAB_____y_____y_____yAB__________ySayALGSi_____yAB_ALQo_GG______Qo__Qo______y_____yABGAHGG_____G_ALQo_SgAAyAB_____y_____yAKyAB_____AMySayA2_GSi_____yAB_A2_Qo_GG_ARQo__Qo_ABGSgt 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedF0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalF0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s5ErrorP
+ _symbolic _____y_____yAAyAAyAAy_____y_____y_____y______AAyAByAEG_____GQo_______y______AAyAByAJGAGGQo_QPGG_____G_____G_____GGAGG 7SwiftUI15ModifiedContentV AA011PlaceholderD4ViewV AA6ZStackV AA05TupleD0V AA0F0PAAE9animation_4bodyQrAA9AnimationVSg_qd__AEyxGXEtAaJRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AA14_OpacityEffectV AkAEAL_AMQrAP_qd__AQXEtAaJRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV
+ _symbolic _____y_____yAAyAAyAAy_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G_____G_____G_AAyAEyAUGAGGQo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AA05TupleD0V AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV AA23_CompositingGroupEffectV
+ _symbolic _____y_____yAAyAAy__________G_____GGADG 7SwiftUI15ModifiedContentV AA011PlaceholderD4ViewV AA4TextV AA14_OpacityEffectV AA16_FixedSizeLayoutV
+ _symbolic _____y_____yAByABy_____y_____y_____y______AByAAyAEG_____GQo_______y______AByAAyAJGAGGQo_QPGG_____G_____G_____GG 7SwiftUI22PlaceholderContentViewV AA08ModifiedD0V AA6ZStackV AA05TupleD0V AA0E0PAAE9animation_4bodyQrAA9AnimationVSg_qd__ACyxGXEtAaJRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AA14_OpacityEffectV AkAEAL_AMQrAP_qd__AQXEtAaJRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV AA12_ScaleEffectV AA13_OffsetEffectV
+ _symbolic _____y_____yABy__________G_____GG 7SwiftUI22PlaceholderContentViewV AA08ModifiedD0V AA4TextV AA14_OpacityEffectV AA16_FixedSizeLayoutV
+ _symbolic _____y_____y_____AAy_____yACG_A2ESgQPG_____G______y_____yAByAC_____y_____y_____yAC__________ySayALGSi_____yAC_ALQo_GG______Qo__Qo______y_____yACGAHGG_____G_ALQo_SgAByAC_____y_____yAKyAC_____AMySayA2_GSi_____yAC_A2_Qo_GG_ARQo__Qo_ACGSgQPG 7SwiftUI12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedD0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalD0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
+ _symbolic _____y_____y_____G_A2DSgQPG 7SwiftUI12TupleContentV AA6ToggleV AA4TextV
+ _symbolic _____y_____y_____G_____G 7SwiftUI15ModifiedContentV AA011PlaceholderD4ViewV 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC07TextureL033_567B04E452D00D382DBBCD37BC34CF3ALLV AA14_OpacityEffectV
+ _symbolic _____y_____y__________y_____SgGG_Qo_ 7SwiftUI4ViewP12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AA15ModifiedContentV AD05PhotogH7ControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV
+ _symbolic _____y_____y_____yAAy__________G______y_____y_____yAAy__________y_____SgGG_Qo_______Qo_GQPGGAIy_____GG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V 12PhotosUIEdit16ExpandableSliderV AA15_HiddenModifierV AA16ScrollViewReaderV AA0N0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO ApHE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AH05PhotouV7ControlV AA022_EnvironmentKeyWritingL0V AA5ColorV AH05PhotoU11ControlModeO AA15LayoutDirectionO
+ _symbolic _____y_____y_____y_____ABy_____yADG_A2FSgQPG_____G______y_____yACyAD_____y_____y_____yAD__________ySayAMGSi_____yAD_AMQo_GG______Qo__Qo______y_____yADGAIGG_____G_AMQo_SgACyAD_____y_____yALyAD_____ANySayA3_GSi_____yAD_A3_Qo_GG_ASQo__Qo_ADGSgQPGG 7SwiftUI4FormV AA12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedE0V AoAE12labelsHiddenQryFQO AoAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQO AA0T0V 15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinetS0V AA012_ConditionalE0V AA6VStackV AA25_AppearanceActionModifierV AoAEAUQryFQO AoAEAVyQrqd__AaWRd__lFQO So34PXPhotosFileProviderEncodingPolicyV AoAEA5__A6_Qrqd___SbtSHRd__lFQO
+ _symbolic _____y_____y_____y__________G______y_____y_____yACy__________y_____SgGG_Qo_______Qo_GQPGG 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V 12PhotosUIEdit16ExpandableSliderV AA15_HiddenModifierV AA16ScrollViewReaderV AA0N0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO ApHE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AH05PhotouV7ControlV AA022_EnvironmentKeyWritingL0V AA5ColorV AH05PhotoU11ControlModeO
+ _symbolic _____y_____y_____y___________y_____yACG_____GQo_______y______ADyAEyAJGAGGQo_QPGG 7SwiftUI6ZStackV AA12TupleContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholdereF0VyxGXEtAaFRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedE0V AN AA14_OpacityEffectV AgAEAH_AIQrAL_qd__AOXEtAaFRd__lFQO AR07TextureP0ATLLV
+ _symbolic _____y_____y_____y_____yAAy__________y_____SgGG_Qo_______Qo_G_____G 7SwiftUI15ModifiedContentV AA16ScrollViewReaderV AA0F0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AG12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AK05PhotooP7ControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV AK0uoV4ModeO AA14_PaddingLayoutV
+ _symbolic _____y_____y_____y_____y_____G_____G_ACy_____y_____y_____yACy__________y_____SgGG_Qo_______Qo_G_____GQPGG 7SwiftUI6ZStackV AA12TupleContentV AA08ModifiedE0V AA6VStackV AA6SpacerV AA12_FrameLayoutV AA16ScrollViewReaderV AA0L0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AQ12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AU05PhotouV7ControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV AU05PhotoU11ControlModeO AA08_PaddingJ0V
+ _symbolic _____y_____y_____y_____y______AAy_____yADG_____GQo_______y______AAyAEyAJGAGGQo_QPGG_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdG0VyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorQ033_567B04E452D00D382DBBCD37BC34CF3ALLV AP AA14_OpacityEffectV AiAEAJ_AKQrAN_qd__AQXEtAaHRd__lFQO AT07TextureQ0AVLLV AA12_FrameLayoutV
+ _symbolic _____y_____y_____y_____y_____y_____G_____G_ADy_____y_____y_____yADy__________y_____SgGG_Qo_______Qo_G_____GQPGGADy_____yACyADy__________G_ATQPGGALy_____GGG 7SwiftUI19_ConditionalContentV AA6ZStackV AA05TupleD0V AA08ModifiedD0V AA6VStackV AA6SpacerV AA12_FrameLayoutV AA16ScrollViewReaderV AA0M0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AS12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AW05PhotovW7ControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV AW05PhotoV11ControlModeO AA08_PaddingK0V AA6HStackV AW16ExpandableSliderV AA15_HiddenModifierV AA0K9DirectionO
+ _symbolic _____y_____y_____y_____y_____y_____G_____G_ADy_____y_____y_____yADy__________y_____SgGG_Qo_______Qo_G_____GQPGGADy_____yACyADy__________G_ATQPGGALy_____GG_G 7SwiftUI19_ConditionalContentV7StorageO AA6ZStackV AA05TupleD0V AA08ModifiedD0V AA6VStackV AA6SpacerV AA12_FrameLayoutV AA16ScrollViewReaderV AA0N0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AU12PhotosUIEditE43photoStyleTextureIntensityValueLabelYOffsetyQrSdFQO AY05PhotowX7ControlV AA30_EnvironmentKeyWritingModifierV AA5ColorV AY05PhotoW11ControlModeO AA08_PaddingL0V AA6HStackV AY16ExpandableSliderV AA15_HiddenModifierV AA0L9DirectionO
+ _symbolic _____ytIegnr_ 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic _____z_Xx 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _symbolic y_____c 12PhotosUIEdit23PhotoStyleTextureEffectV
+ _type_layout_string 15PhotosUIPrivate38PUCinematicVideoEditOperationPerformerC5Error33_C7D106D62E07D5D036D95EBF1685AA41LLO
+ _type_layout_string 15PhotosUIPrivate41PUCinematicOneUpResourceLoadingControllerC0fG5StateO
- -[PUPickerAssetPreparationOptions initWithIncludeLocation:includeCaption:includeKeywords:userEncodingPolicy:]
- GCC_except_table0
- GCC_except_table10010
- GCC_except_table10014
- GCC_except_table10018
- GCC_except_table10036
- GCC_except_table10203
- GCC_except_table10220
- GCC_except_table10231
- GCC_except_table10232
- GCC_except_table10262
- GCC_except_table10330
- GCC_except_table10370
- GCC_except_table10372
- GCC_except_table10379
- GCC_except_table10383
- GCC_except_table10389
- GCC_except_table1047
- GCC_except_table10486
- GCC_except_table10544
- GCC_except_table10577
- GCC_except_table10841
- GCC_except_table10843
- GCC_except_table1092
- GCC_except_table10958
- GCC_except_table11065
- GCC_except_table1109
- GCC_except_table1116
- GCC_except_table11228
- GCC_except_table11269
- GCC_except_table11298
- GCC_except_table11306
- GCC_except_table11350
- GCC_except_table11351
- GCC_except_table11353
- GCC_except_table11354
- GCC_except_table11357
- GCC_except_table11361
- GCC_except_table11382
- GCC_except_table11694
- GCC_except_table11724
- GCC_except_table11734
- GCC_except_table11803
- GCC_except_table1191
- GCC_except_table1195
- GCC_except_table1205
- GCC_except_table1206
- GCC_except_table1208
- GCC_except_table12147
- GCC_except_table12148
- GCC_except_table1216
- GCC_except_table12199
- GCC_except_table12203
- GCC_except_table1234
- GCC_except_table1246
- GCC_except_table1248
- GCC_except_table12494
- GCC_except_table12511
- GCC_except_table12524
- GCC_except_table12538
- GCC_except_table12558
- GCC_except_table12607
- GCC_except_table12762
- GCC_except_table12780
- GCC_except_table12785
- GCC_except_table12788
- GCC_except_table12791
- GCC_except_table12802
- GCC_except_table12852
- GCC_except_table12865
- GCC_except_table12905
- GCC_except_table12941
- GCC_except_table12957
- GCC_except_table12959
- GCC_except_table12995
- GCC_except_table1302
- GCC_except_table13088
- GCC_except_table13093
- GCC_except_table1310
- GCC_except_table13361
- GCC_except_table13436
- GCC_except_table13450
- GCC_except_table13457
- GCC_except_table13473
- GCC_except_table13474
- GCC_except_table13477
- GCC_except_table13484
- GCC_except_table13598
- GCC_except_table13600
- GCC_except_table13662
- GCC_except_table13704
- GCC_except_table13766
- GCC_except_table13791
- GCC_except_table13807
- GCC_except_table13822
- GCC_except_table13846
- GCC_except_table13874
- GCC_except_table13886
- GCC_except_table13896
- GCC_except_table13906
- GCC_except_table13919
- GCC_except_table13940
- GCC_except_table13974
- GCC_except_table13979
- GCC_except_table13981
- GCC_except_table13986
- GCC_except_table13987
- GCC_except_table13988
- GCC_except_table14008
- GCC_except_table14055
- GCC_except_table14279
- GCC_except_table14419
- GCC_except_table14522
- GCC_except_table14526
- GCC_except_table14537
- GCC_except_table14561
- GCC_except_table14564
- GCC_except_table14574
- GCC_except_table15023
- GCC_except_table1518
- GCC_except_table15456
- GCC_except_table15457
- GCC_except_table15466
- GCC_except_table15469
- GCC_except_table15472
- GCC_except_table15480
- GCC_except_table15515
- GCC_except_table1553
- GCC_except_table15550
- GCC_except_table15628
- GCC_except_table1563
- GCC_except_table15706
- GCC_except_table15712
- GCC_except_table15716
- GCC_except_table15756
- GCC_except_table15806
- GCC_except_table15814
- GCC_except_table15819
- GCC_except_table15821
- GCC_except_table15853
- GCC_except_table15865
- GCC_except_table15873
- GCC_except_table15875
- GCC_except_table15879
- GCC_except_table15886
- GCC_except_table15889
- GCC_except_table15891
- GCC_except_table15893
- GCC_except_table15898
- GCC_except_table15917
- GCC_except_table15924
- GCC_except_table15928
- GCC_except_table15939
- GCC_except_table15950
- GCC_except_table15998
- GCC_except_table16071
- GCC_except_table16075
- GCC_except_table16189
- GCC_except_table16192
- GCC_except_table16198
- GCC_except_table16230
- GCC_except_table16247
- GCC_except_table16305
- GCC_except_table16335
- GCC_except_table16392
- GCC_except_table16413
- GCC_except_table16428
- GCC_except_table16510
- GCC_except_table16511
- GCC_except_table16528
- GCC_except_table16537
- GCC_except_table16544
- GCC_except_table16551
- GCC_except_table16557
- GCC_except_table16567
- GCC_except_table16574
- GCC_except_table16758
- GCC_except_table16769
- GCC_except_table16772
- GCC_except_table16774
- GCC_except_table16781
- GCC_except_table16783
- GCC_except_table16785
- GCC_except_table16788
- GCC_except_table168
- GCC_except_table16803
- GCC_except_table16870
- GCC_except_table16876
- GCC_except_table16904
- GCC_except_table16909
- GCC_except_table17107
- GCC_except_table17132
- GCC_except_table17295
- GCC_except_table17402
- GCC_except_table17403
- GCC_except_table17528
- GCC_except_table17562
- GCC_except_table176
- GCC_except_table17604
- GCC_except_table17609
- GCC_except_table17638
- GCC_except_table17640
- GCC_except_table17642
- GCC_except_table17788
- GCC_except_table17791
- GCC_except_table17800
- GCC_except_table17987
- GCC_except_table17988
- GCC_except_table18022
- GCC_except_table18041
- GCC_except_table18043
- GCC_except_table18108
- GCC_except_table18181
- GCC_except_table18198
- GCC_except_table18199
- GCC_except_table18202
- GCC_except_table18209
- GCC_except_table18210
- GCC_except_table18218
- GCC_except_table18231
- GCC_except_table18239
- GCC_except_table18250
- GCC_except_table18396
- GCC_except_table18398
- GCC_except_table18400
- GCC_except_table18408
- GCC_except_table18698
- GCC_except_table18699
- GCC_except_table18718
- GCC_except_table1872
- GCC_except_table18720
- GCC_except_table18749
- GCC_except_table18760
- GCC_except_table18769
- GCC_except_table18784
- GCC_except_table18785
- GCC_except_table18789
- GCC_except_table18798
- GCC_except_table18808
- GCC_except_table18926
- GCC_except_table18938
- GCC_except_table18986
- GCC_except_table18996
- GCC_except_table19011
- GCC_except_table19014
- GCC_except_table19016
- GCC_except_table19017
- GCC_except_table19018
- GCC_except_table19019
- GCC_except_table19024
- GCC_except_table19107
- GCC_except_table19195
- GCC_except_table19210
- GCC_except_table19268
- GCC_except_table19323
- GCC_except_table19483
- GCC_except_table19500
- GCC_except_table19680
- GCC_except_table1971
- GCC_except_table19846
- GCC_except_table19934
- GCC_except_table19958
- GCC_except_table20366
- GCC_except_table20370
- GCC_except_table20379
- GCC_except_table20383
- GCC_except_table20401
- GCC_except_table20412
- GCC_except_table20462
- GCC_except_table20511
- GCC_except_table20762
- GCC_except_table20910
- GCC_except_table20915
- GCC_except_table21056
- GCC_except_table21066
- GCC_except_table21068
- GCC_except_table21111
- GCC_except_table21166
- GCC_except_table21256
- GCC_except_table21447
- GCC_except_table21451
- GCC_except_table21530
- GCC_except_table21531
- GCC_except_table21539
- GCC_except_table21618
- GCC_except_table21652
- GCC_except_table21734
- GCC_except_table21735
- GCC_except_table21789
- GCC_except_table2180
- GCC_except_table2181
- GCC_except_table2183
- GCC_except_table21915
- GCC_except_table2192
- GCC_except_table22110
- GCC_except_table22111
- GCC_except_table22128
- GCC_except_table22132
- GCC_except_table22155
- GCC_except_table22267
- GCC_except_table2243
- GCC_except_table22586
- GCC_except_table2261
- GCC_except_table22627
- GCC_except_table22720
- GCC_except_table22744
- GCC_except_table22759
- GCC_except_table22879
- GCC_except_table22915
- GCC_except_table22918
- GCC_except_table22920
- GCC_except_table22925
- GCC_except_table22957
- GCC_except_table22963
- GCC_except_table23028
- GCC_except_table23044
- GCC_except_table2306
- GCC_except_table2314
- GCC_except_table2315
- GCC_except_table2316
- GCC_except_table2318
- GCC_except_table2330
- GCC_except_table23313
- GCC_except_table23317
- GCC_except_table23319
- GCC_except_table23326
- GCC_except_table23327
- GCC_except_table23329
- GCC_except_table23330
- GCC_except_table23332
- GCC_except_table23434
- GCC_except_table2353
- GCC_except_table23536
- GCC_except_table23573
- GCC_except_table23635
- GCC_except_table23648
- GCC_except_table2370
- GCC_except_table2372
- GCC_except_table23736
- GCC_except_table23743
- GCC_except_table23747
- GCC_except_table2376
- GCC_except_table23766
- GCC_except_table23771
- GCC_except_table23777
- GCC_except_table2378
- GCC_except_table23793
- GCC_except_table23994
- GCC_except_table24017
- GCC_except_table24028
- GCC_except_table2407
- GCC_except_table24133
- GCC_except_table24188
- GCC_except_table24195
- GCC_except_table24199
- GCC_except_table24213
- GCC_except_table24216
- GCC_except_table24347
- GCC_except_table24375
- GCC_except_table24392
- GCC_except_table2444
- GCC_except_table24442
- GCC_except_table24602
- GCC_except_table24671
- GCC_except_table24681
- GCC_except_table24689
- GCC_except_table24905
- GCC_except_table24921
- GCC_except_table27
- GCC_except_table276
- GCC_except_table2772
- GCC_except_table2774
- GCC_except_table28
- GCC_except_table2830
- GCC_except_table2834
- GCC_except_table2837
- GCC_except_table2925
- GCC_except_table2929
- GCC_except_table2951
- GCC_except_table2959
- GCC_except_table3011
- GCC_except_table3069
- GCC_except_table3072
- GCC_except_table31
- GCC_except_table321
- GCC_except_table3282
- GCC_except_table3314
- GCC_except_table3337
- GCC_except_table3360
- GCC_except_table3363
- GCC_except_table35
- GCC_except_table38
- GCC_except_table3805
- GCC_except_table3808
- GCC_except_table3814
- GCC_except_table388
- GCC_except_table389
- GCC_except_table3943
- GCC_except_table3991
- GCC_except_table4011
- GCC_except_table4049
- GCC_except_table4052
- GCC_except_table4053
- GCC_except_table4054
- GCC_except_table4057
- GCC_except_table409
- GCC_except_table4134
- GCC_except_table4136
- GCC_except_table415
- GCC_except_table416
- GCC_except_table417
- GCC_except_table421
- GCC_except_table4269
- GCC_except_table43
- GCC_except_table433
- GCC_except_table435
- GCC_except_table4386
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4462
- GCC_except_table4489
- GCC_except_table4596
- GCC_except_table46
- GCC_except_table4611
- GCC_except_table4770
- GCC_except_table4793
- GCC_except_table4879
- GCC_except_table5072
- GCC_except_table5123
- GCC_except_table5132
- GCC_except_table5139
- GCC_except_table5140
- GCC_except_table5141
- GCC_except_table5163
- GCC_except_table5185
- GCC_except_table5289
- GCC_except_table5408
- GCC_except_table5415
- GCC_except_table552
- GCC_except_table555
- GCC_except_table5814
- GCC_except_table5852
- GCC_except_table5872
- GCC_except_table5874
- GCC_except_table5884
- GCC_except_table5912
- GCC_except_table5915
- GCC_except_table5965
- GCC_except_table5988
- GCC_except_table6022
- GCC_except_table6032
- GCC_except_table6316
- GCC_except_table6318
- GCC_except_table6321
- GCC_except_table6322
- GCC_except_table6329
- GCC_except_table6462
- GCC_except_table6514
- GCC_except_table6518
- GCC_except_table6521
- GCC_except_table6538
- GCC_except_table6570
- GCC_except_table6634
- GCC_except_table6664
- GCC_except_table6671
- GCC_except_table6742
- GCC_except_table6773
- GCC_except_table6878
- GCC_except_table6882
- GCC_except_table6885
- GCC_except_table6888
- GCC_except_table6955
- GCC_except_table6967
- GCC_except_table6977
- GCC_except_table6981
- GCC_except_table7120
- GCC_except_table7130
- GCC_except_table7139
- GCC_except_table7221
- GCC_except_table7276
- GCC_except_table7284
- GCC_except_table7426
- GCC_except_table7442
- GCC_except_table7477
- GCC_except_table7483
- GCC_except_table7488
- GCC_except_table7496
- GCC_except_table7501
- GCC_except_table7506
- GCC_except_table7535
- GCC_except_table7656
- GCC_except_table7657
- GCC_except_table787
- GCC_except_table806
- GCC_except_table8060
- GCC_except_table808
- GCC_except_table8133
- GCC_except_table8245
- GCC_except_table8252
- GCC_except_table8258
- GCC_except_table832
- GCC_except_table8323
- GCC_except_table834
- GCC_except_table8353
- GCC_except_table8354
- GCC_except_table8509
- GCC_except_table8698
- GCC_except_table8706
- GCC_except_table8707
- GCC_except_table8715
- GCC_except_table8730
- GCC_except_table8748
- GCC_except_table8767
- GCC_except_table8771
- GCC_except_table8797
- GCC_except_table8849
- GCC_except_table8977
- GCC_except_table9061
- GCC_except_table9066
- GCC_except_table9109
- GCC_except_table9193
- GCC_except_table9205
- GCC_except_table9245
- GCC_except_table9270
- GCC_except_table9314
- GCC_except_table9341
- GCC_except_table9355
- GCC_except_table9362
- GCC_except_table9402
- GCC_except_table941
- GCC_except_table9415
- GCC_except_table9417
- GCC_except_table942
- GCC_except_table9421
- GCC_except_table9422
- GCC_except_table944
- GCC_except_table9488
- GCC_except_table9491
- GCC_except_table956
- GCC_except_table957
- GCC_except_table9629
- GCC_except_table9634
- GCC_except_table9636
- GCC_except_table9685
- GCC_except_table975
- GCC_except_table9759
- GCC_except_table9768
- GCC_except_table982
- GCC_except_table9910
- GCC_except_table9962
- ___block_descriptor_105_e8_32s40s48s56s64s72r80r88r96r_e42_v32?0"PUAssetReference"8"NSArray"16^B24ls32l8s40l8r72l8s48l8s56l8s64l8r80l8r88l8r96l8
- ___block_descriptor_112_e8_32r40r48r56r64r72r80r88r96r104r_e36_v32?0"PUActivityAssetItem"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8
- ___swift_closure_destructor.106Tm
- ___swift_closure_destructor.154Tm
- ___swift_closure_destructor.46Tm
- ___swift_closure_destructor.68Tm
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQOyACyACyACyAA6ZStackVyAeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQOy15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV_ACyALyAUGAA14_OpacityEffectVGQo_GAA12_FrameLayoutVGAA06_ScaleZ0VGAA07_OffsetZ0VG_ACyALyA8_GAXGQo_AA017_CompositingGroupZ0VGAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGAA30_EnvironmentKeyWritingModifierVySo0M21EditLayoutOrientationVGGAaDHPA20_AaDHPA14_AaDHPqd0__AaDHD3_A11_HO_A13_AA0E8ModifierHPyHCHC_A19_AAA27_HPyHCHC_A25_AAA27_HPyHCHC
- _get_witness_table 7SwiftUI4FormVyAA12TupleContentVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_ALQPGAA9EmptyViewVG_AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedE0VyAGyAirAE12labelsHiddenQryFQOyArAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA5_GSiArAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAI_A5_Qo_GG_AA06InlinetS0VQo__Qo_AA012_ConditionalE0VyAA6VStackVyAIGAOGGAA25_AppearanceActionModifierVG_A5_Qo_SgAGyAirAEAXQryFQOyArAEAYyQrqd__AaZRd__lFQOyA0_yAISo34PXPhotosFileProviderEncodingPolicyVA7_ySayA31_GSiArAEA9__A10_Qrqd___SbtSHRd__lFQOyAI_A31_Qo_GG_A15_Qo__Qo_AIGSgQPGGAaQHPyHC
- _objc_msgSend$initWithIncludeAllPhotosData:includeLocationData:includeLivePhotoData:
- _objc_msgSend$initWithIncludeLocation:includeCaption:includeKeywords:userEncodingPolicy:
- _objc_msgSend$standardVideo
- _symbolic _____yAAyAAy_____yAAyAAyAAy_____y_____y______AAy_____yACG_____GQo_G_____G_____G_____G_AAyADyAOGAFGQo______G_____y_____GG_____y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V AA017_CompositingGroupZ0V AA21_TraitWritingModifierV AA18TransitionTraitKeyV AA30_EnvironmentKeyWritingModifierV So0M21EditLayoutOrientationV
- _symbolic _____yAAyAAy_____y_____y______AAy_____yACG_____GQo_G_____G_____G_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdF0VyxGXEtAaFRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AN AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V
- _symbolic _____yAAy_____yAAyAAyAAy_____y_____y______AAy_____yACG_____GQo_G_____G_____G_____G_AAyADyAOGAFGQo______G_____y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V AA017_CompositingGroupZ0V AA21_TraitWritingModifierV AA18TransitionTraitKeyV
- _symbolic _____yAAy_____y_____y______AAy_____yACG_____GQo_G_____G_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdF0VyxGXEtAaFRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AN AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V
- _symbolic _____y_____G_ACt 7SwiftUI6ToggleV AA4TextV
- _symbolic _____y___________y___________y_____yACG_____GQo_G 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA0D0PAAE9animation_4bodyQrAA9AnimationVSg_qd__AA018PlaceholderContentD0VyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorR033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedL0V AP AA14_OpacityEffectV
- _symbolic _____y__________y_____yABG_AEQPG_____G 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV
- _symbolic _____y__________y_____yABG_AEQPG_____G______y_____yAAyAB_____y_____y_____yAB__________ySayAKGSi_____yAB_AKQo_GG______Qo__Qo______y_____yABGAGGG_____G_AKQo_SgAAyAB_____y_____yAJyAB_____ALySayA1_GSi_____yAB_A1_Qo_GG_AQQo__Qo_ABGSgt 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedF0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalF0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
- _symbolic _____y_____yAAyAAyAAy_____y_____y______AAyAByADG_____GQo_G_____G_____G_____GGAFG 7SwiftUI15ModifiedContentV AA011PlaceholderD4ViewV AA6ZStackV AA0F0PAAE9animation_4bodyQrAA9AnimationVSg_qd__AEyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V
- _symbolic _____y_____yAAyAAyAAy_____y_____y______AAy_____yACG_____GQo_G_____G_____G_____G_AAyADyAOGAFGQo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdE0VyxGXEtAaDRd__lFQO AA6ZStackV AeAEAF_AGQrAJ_qd__AMXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AL AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V AA017_CompositingGroupZ0V
- _symbolic _____y_____yAByABy_____y_____y______AByAAyADG_____GQo_G_____G_____G_____GG 7SwiftUI22PlaceholderContentViewV AA08ModifiedD0V AA6ZStackV AA0E0PAAE9animation_4bodyQrAA9AnimationVSg_qd__ACyxGXEtAaHRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AA14_OpacityEffectV AA12_FrameLayoutV AA06_ScaleZ0V AA07_OffsetZ0V
- _symbolic _____y_____y_____AAy_____yACG_AEQPG_____G______y_____yAByAC_____y_____y_____yAC__________ySayAKGSi_____yAC_AKQo_GG______Qo__Qo______y_____yACGAGGG_____G_AKQo_SgAByAC_____y_____yAJyAC_____ALySayA1_GSi_____yAC_A1_Qo_GG_AQQo__Qo_ACGSgQPG 7SwiftUI12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedD0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalD0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
- _symbolic _____y_____y_____G_ADQPG 7SwiftUI12TupleContentV AA6ToggleV AA4TextV
- _symbolic _____y_____y___________y_____yABG_____GQo_G 7SwiftUI6ZStackV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA018PlaceholderContentD0VyxGXEtAaDRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorO033_567B04E452D00D382DBBCD37BC34CF3ALLV AA08ModifiedI0V AL AA14_OpacityEffectV
- _symbolic _____y_____y_____y_____ABy_____yADG_AFQPG_____G______y_____yACyAD_____y_____y_____yAD__________ySayALGSi_____yAD_ALQo_GG______Qo__Qo______y_____yADGAHGG_____G_ALQo_SgACyAD_____y_____yAKyAD_____AMySayA2_GSi_____yAD_A2_Qo_GG_ARQo__Qo_ADGSgQPGG 7SwiftUI4FormV AA12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedE0V AoAE12labelsHiddenQryFQO AoAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQO AA0T0V 15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinetS0V AA012_ConditionalE0V AA6VStackV AA25_AppearanceActionModifierV AoAEAUQryFQO AoAEAVyQrqd__AaWRd__lFQO So34PXPhotosFileProviderEncodingPolicyV AoAEA5__A6_Qrqd___SbtSHRd__lFQO
- _symbolic _____y_____y_____y______AAy_____yACG_____GQo_G_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA4ViewPAAE9animation_4bodyQrAA9AnimationVSg_qd__AA011PlaceholderdF0VyxGXEtAaFRd__lFQO 15PhotosUIPrivate27PUPhotoStyleUnifiedControlsC05ColorP033_567B04E452D00D382DBBCD37BC34CF3ALLV AN AA14_OpacityEffectV AA12_FrameLayoutV
CStrings:
+ "%{public}@: Import contains provenance data. Presenting warning before continuing."
+ "(exclude live: %@, exclude location: %@, exclude provenance: %@, exclude caption: %@, exclude AX description: %@, exclude keywords: %@, include all photos data: %@, unmodified original: %@, format preference: %@)"
+ "-[PUPickerPrincipalUIViewController confirmProvenanceSensitiveEditsForFetchResult:additionalSelectionState:completionHandler:]"
+ "<%@:%p, asset:%@, excludeLiveness:%@, excludeLocation:%@, excludeProvenance:%@, excludeCaption:%@, excludeAccessibilityDescription:%@>"
+ "Aborted picking after provenance check."
+ "BAR_BUTTON_ITEM_TITLE_EXIT_PROVENANCE_MODE"
+ "BAR_BUTTON_ITEM_TITLE_SHOW_PROVENANCE_METADATA"
+ "CINEMATIC_BADGE_MENU_ACTION_DISABLE_CINEMATIC"
+ "CINEMATIC_BADGE_MENU_ACTION_ENABLE_CINEMATIC"
+ "CIPhotoEffectMono"
+ "CinEverywhere: assetNeedsDownload=%{bool}d, modelNeedsDownload=%{bool}d, weights=(%f, %f)"
+ "CinEverywhere: downloadResources completion (hasOngoingDownload: %{bool}d, success=%{bool}d, error=%s)"
+ "CinEverywhere: requestAVAsset failed: %@. Assuming download needed."
+ "Cinematic resource initialization failed"
+ "DeviceSupportsGenerativeModelSystems"
+ "Error downloading cinematic resources from mediaToolController's didBecomeActiveTool, but no error is returned"
+ "Error downloading cinematic resources from mediaToolController's didBecomeActiveTool: %{public}@"
+ "Failed to obtain AVAsset"
+ "Failed to set cinematic video effect for asset %s. Error: %s"
+ "IMPORT_PROVENANCE_WARNING_IMPORT_ACTION"
+ "IMPORT_PROVENANCE_WARNING_MESSAGE"
+ "IMPORT_PROVENANCE_WARNING_TITLE"
+ "In lockdown mode. Including provenance by default in share sheet."
+ "Loading cinematic one up asset failed with error: %@."
+ "Loading cinematic one up resource failed with error: %@."
+ "Not a PhotoKit asset."
+ "PECinematicVideoModelDownloadAlertInformativeText"
+ "PECinematicVideoModelDownloadAlertTitle"
+ "PECinematicVideoOneUpAssetDownloadProgressSubtitle"
+ "PECinematicVideoOneUpDownloadCancelButtonTitle"
+ "PECinematicVideoOneUpDownloadConfirmationButtonTitle"
+ "PECinematicVideoOneUpDownloadConfirmationMessage"
+ "PECinematicVideoOneUpDownloadConfirmationTitle"
+ "PECinematicVideoOneUpModelDownloadErrorBusyTitle"
+ "PECinematicVideoOneUpModelDownloadProgressSubtitle"
+ "PEMediaDestination.saveInternalEdits invoked its completion handler with unexpected contents."
+ "PEResourceManager returned unusable PEResourceLoadResult."
+ "PHOTOEDIT_STYLES_CUSTOMIZE_BUTTON"
+ "PHOTOEDIT_STYLES_CUSTOMIZE_BUTTON_ACCESSIBILITY_LABEL"
+ "PICKER_OPTIONS_VIEW_SECTION_METADATA_STRIPPING_PROVENANCE_TOGGLE"
+ "PROVENANCE_ALERT_ELIGIBILITY_MESSAGE"
+ "PROVENANCE_ALERT_ELIGIBILITY_TITLE"
+ "PROVENANCE_ALERT_FATAL_MESSAGE"
+ "PROVENANCE_ALERT_FATAL_TITLE"
+ "PROVENANCE_ALERT_TRANSIENT_MESSAGE"
+ "PROVENANCE_ALERT_TRANSIENT_TITLE"
+ "PROVENANCE_SHARE_CONTINUE_ACTION"
+ "PROVENANCE_SHARE_EDIT_WARNING_MESSAGE"
+ "PROVENANCE_SHARE_EDIT_WARNING_TITLE"
+ "PROVENANCE_SHARE_SUPPRESS_WARNING_ACTION"
+ "PUOneUpBarButtonItemIdentifierProvenanceExitMode"
+ "PUOneUpBarButtonItemIdentifierProvenanceShowMetadata"
+ "PUOneUpCinematicResourceLoadingController"
+ "PUPhotoKitAssetsDataSource: Cinematic Everywhere hardware support: %{BOOL}d"
+ "PUProvenanceSuppressSensitiveEditSharingWarning"
+ "PhotosUIProvenance"
+ "Provenance"
+ "Provolone"
+ "SHARING_OPTIONS_ALL_PHOTOS_DATA_FOOTER_PROVENANCE"
+ "SHARING_OPTIONS_PROVENANCE_SUBTITLE"
+ "SHARING_OPTIONS_PROVENANCE_TITLE"
+ "Sharing %ld assets to activity type: %@\nOptions:\nSend As: %@\nExport Unmodified Originals: %@\n(Prepared As: %@)\nInclude Location: %@\nInclude Provenance: %@\nInclude Caption: %@\nInclude Accessibility Description: %@\nAll Photos Data: %@\n\n"
+ "Simluate Cinematic Resource Loading"
+ "Texture Style Bottom Layout"
+ "Use New Thumbnails Behavior"
+ "User cancelled 1up download of cinematic actionable video."
+ "User confirmed 1up download of cinematic actionable video."
+ "User manually cancelled cinematic resource download."
+ "downloadCinematicResources(avAsset:)"
+ "excludeProvenance"
+ "importAsset"
+ "info"
+ "loadOneUpAsset failed with error: %s"
+ "loadOneUpAssetForAsset(_:)"
+ "loadOneUpResources failed with error: %s"
+ "loadOneUpResourcesForAsset(_:)"
+ "noProvenance"
+ "pccProcessingBatchCount"
+ "perform failed with error: %@"
+ "performUndo failed with error: %@"
+ "pickerShouldStripProvenance"
+ "provenanceViewerStateChanged"
+ "requestOriginalAVAsset(for:networkAccessAllowed:)"
+ "setCinematicVideoEffect(enabled:)"
+ "simulateLoadingOneUpResources failed with error: %s"
+ "simulateLoadingOneUpResources(_:)"
+ "slider.horizontal.below.rectangle"
+ "textureStyleBottomLayout"
+ "unhandled operationType: "
+ "useNewStylesThumbnailsBehavior"
+ "v16@?0@\"NSProgress\"8"
+ "v16@?0@\"PITextureStyleAdjustmentController\"8"
+ "v24@?0B8B12@\"NSError\"16"
+ "withProvenance"
+ "{ProvenanceIcon}"
+ "\xf0!"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0B\xf0\xd5"
- "(exclude live: %@, exclude location: %@, exclude caption: %@, exclude AX description: %@, exclude keywords: %@, include all photos data: %@, unmodified original: %@, format preference: %@)"
- "<%@:%p, asset:%@, excludeLiveness:%@, excludeLocation:%@, excludeCaption:%@, excludeAccessibilityDescription:%@>"
- "Asset has cinematicMetadata but is not a cinematic video. This is unexpected"
- "Sharing %ld assets to activity type: %@\nOptions:\nSend As: %@\nExport Unmodified Originals: %@\n(Prepared As: %@)\nInclude Location: %@\nInclude Caption: %@\nInclude Accessibility Description: %@\nAll Photos Data: %@\n\n"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf02\xf0\xd5"
```

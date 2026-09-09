## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0x2dbf9c
-  __TEXT.__objc_methlist: 0x26d04
-  __TEXT.__const: 0x1758
+912.0.235.0.0
+  __TEXT.__text: 0x2e3c10
+  __TEXT.__objc_methlist: 0x26f6c
+  __TEXT.__const: 0x17e0
   __TEXT.__dlopen_cstrs: 0x280
-  __TEXT.__constg_swiftt: 0x544
-  __TEXT.__swift5_typeref: 0x4cd
-  __TEXT.__swift5_reflstr: 0x161
-  __TEXT.__swift5_fieldmd: 0x1a8
+  __TEXT.__constg_swiftt: 0x67c
+  __TEXT.__swift5_typeref: 0x547
   __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x191
+  __TEXT.__swift5_fieldmd: 0x23c
   __TEXT.__swift5_assocty: 0xd0
   __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x32803
+  __TEXT.__cstring: 0x33122
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x23567
+  __TEXT.__oslogstring: 0x24831
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x969c
+  __TEXT.__gcc_except_tab: 0x985c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x96e0
-  __TEXT.__eh_frame: 0x4a0
+  __TEXT.__unwind_info: 0x97e0
+  __TEXT.__eh_frame: 0x4d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8fb8
-  __DATA_CONST.__objc_classlist: 0xf30
+  __DATA_CONST.__const: 0x90f0
+  __DATA_CONST.__objc_classlist: 0xf40
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x146f0
+  __DATA_CONST.__objc_selrefs: 0x14900
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc60
-  __DATA_CONST.__objc_arraydata: 0x920
-  __DATA_CONST.__got: 0x29c8
-  __AUTH_CONST.__const: 0x46d8
-  __AUTH_CONST.__cfstring: 0x2d680
-  __AUTH_CONST.__objc_const: 0x42310
-  __AUTH_CONST.__objc_intobj: 0x23e8
-  __AUTH_CONST.__objc_arrayobj: 0x798
-  __AUTH_CONST.__objc_doubleobj: 0x130
+  __DATA_CONST.__objc_arraydata: 0x940
+  __DATA_CONST.__got: 0x2a40
+  __AUTH_CONST.__const: 0x4778
+  __AUTH_CONST.__cfstring: 0x2da60
+  __AUTH_CONST.__objc_const: 0x42728
+  __AUTH_CONST.__objc_intobj: 0x24f0
+  __AUTH_CONST.__objc_arrayobj: 0x7b0
+  __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x18c8
-  __AUTH.__objc_data: 0x7de8
-  __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x35fc
-  __DATA.__data: 0x2bc8
+  __AUTH_CONST.__auth_got: 0x1918
+  __AUTH.__objc_data: 0x7e38
+  __AUTH.__data: 0x3c0
+  __DATA.__objc_ivar: 0x3638
+  __DATA.__data: 0x2c18
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0x1a60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14909
-  Symbols:   34053
-  CStrings:  8867
+  Functions: 15026
+  Symbols:   34248
+  CStrings:  8957
 
Symbols:
+ +[PHAsset fetchProcessedProvenanceAssetWithOriginatingAssetIdentifier:options:]
+ +[PHAssetCreationMetadataCopyOptions shouldEmbedProvenanceIntoSharedRenderForAsset:shouldCopyProvenanceData:]
+ +[PHAssetCreationMetadataCopyOptions shouldProcessProvenanceForAsset:shouldCopyProvenanceData:]
+ +[PHAssetCreationMetadataCopyOptions shouldStripProvenanceForAsset:shouldCopyProvenanceData:]
+ +[PHAssetCreationRequest _creationRequestForProcessedProvenanceAssetFromUnprocessedProvenanceAsset:resourceBundle:processedProvenanceResourceURL:]
+ +[PHAssetCreationRequest _validateProvenanceStateForProcessing:]
+ +[PHAssetCreationRequest creationRequestForProcessedProvenanceAssetFromUnprocessedProvenanceAsset:resourceInfo:]
+ +[PHAssetCreationRequest processedProvenanceReplacementForSharingAsset:completionHandler:]
+ +[PHAssetCreationRequestPlaceholderSupport _processedProvenanceCarrierURLFromSourceAsset:]
+ +[PHAssetCreationRequestPlaceholderSupport _removeProvenanceSidecarResourcesFrom:byType:]
+ +[PHAssetExportRequest _adjustedProvenanceRenderURLToShareForAsset:options:fileURLs:]
+ +[PHAssetExportRequest _insertAssetWithProcessedProvenanceResourceURL:unprocessedAsset:]
+ +[PHAssetExportRequest _shouldCombineEditedProvenanceIntoRenderForAsset:options:fileURLs:]
+ +[PHImportAsset scanAssetsForProvenanceData:atEnd:]
+ +[PHImportAsset stripProvenanceExtensionFrompPath:]
+ +[PHResourceLocalAvailabilityRequest _shouldAddOriginalProvenanceResourceToResourcesToShareForAsset:shouldStripProvenance:]
+ -[PHAsset _setupProvenanceStateFromFetchDictionary:]
+ -[PHAsset isCinematicCapableVideo]
+ -[PHAsset provenanceState]
+ -[PHAssetCreationMetadataCopyOptions setShouldCopyProvenanceData:]
+ -[PHAssetCreationMetadataCopyOptions shouldCopyProvenanceData]
+ -[PHAssetCreationRequest _addProcessedProvenanceResourceToAssetResources:processedProvenanceResourceURL:unprocessedOriginal:error:]
+ -[PHAssetCreationRequest _cleanupTemporaryProvenanceFilesIfNecessary]
+ -[PHAssetCreationRequest _getOriginalResource:sidecarProvenanceResource:]
+ -[PHAssetCreationRequest _updateAssetResourcesWithProcessedProvenanceResource:]
+ -[PHAssetCreationRequest originalProvenanceAssetFilename]
+ -[PHAssetCreationRequest originalProvenanceAssetUUID]
+ -[PHAssetCreationRequest performAsyncPreprocessingWithCompletionHandler:]
+ -[PHAssetCreationRequest setOriginalProvenanceAssetFilename:]
+ -[PHAssetCreationRequest setOriginalProvenanceAssetUUID:]
+ -[PHAssetCreationRequest setUseMockProvenanceProcessingClientForUnitTestSupport:]
+ -[PHAssetCreationRequest useMockProvenanceProcessingClientForUnitTestSupport]
+ -[PHAssetCreationRequestPlaceholderSupport _shouldEmbedProvenanceIntoRenderForSourceAsset:]
+ -[PHAssetExportRequestOptions forceProvenanceMetadataBaking]
+ -[PHAssetExportRequestOptions setForceProvenanceMetadataBaking:]
+ -[PHAssetExportRequestOptions setShouldStripProvenance:]
+ -[PHAssetExportRequestOptions shouldStripProvenance]
+ -[PHAssetPTPProperties provenanceState]
+ -[PHAssetResourceCreationOptions hasProvenanceData]
+ -[PHAssetResourceCreationOptions setHasProvenanceData:]
+ -[PHExternalAssetResource hasProvenanceData]
+ -[PHImportAsset hasProvenanceMetadata]
+ -[PHImportAsset provenanceAsset]
+ -[PHImportAsset setProvenanceAsset:]
+ -[PHImportSource processPotentialProvenanceAsset:plusProvenanceDNG:]
+ -[PHPTPAssetManager _isProvenanceAssetRequiringProcessing:]
+ -[PHPhotoLibrary(ContentProvenance) lastAvailableContentProvenanceLowerBoundTimestampData]
+ -[PHResourceLocalAvailabilityRequestOptions preferUncombinedProvenanceResources]
+ -[PHResourceLocalAvailabilityRequestOptions setPreferUncombinedProvenanceResources:]
+ -[PHResourceLocalAvailabilityRequestOptions setShouldStripProvenance:]
+ -[PHResourceLocalAvailabilityRequestOptions shouldStripProvenance]
+ GCC_except_table10027
+ GCC_except_table10118
+ GCC_except_table10353
+ GCC_except_table10354
+ GCC_except_table10355
+ GCC_except_table10356
+ GCC_except_table10357
+ GCC_except_table10358
+ GCC_except_table10359
+ GCC_except_table10360
+ GCC_except_table10361
+ GCC_except_table10362
+ GCC_except_table10363
+ GCC_except_table10364
+ GCC_except_table10365
+ GCC_except_table10366
+ GCC_except_table10367
+ GCC_except_table10368
+ GCC_except_table10369
+ GCC_except_table10370
+ GCC_except_table10371
+ GCC_except_table10372
+ GCC_except_table10373
+ GCC_except_table10374
+ GCC_except_table10375
+ GCC_except_table10376
+ GCC_except_table10377
+ GCC_except_table10378
+ GCC_except_table10379
+ GCC_except_table10380
+ GCC_except_table10381
+ GCC_except_table10382
+ GCC_except_table10383
+ GCC_except_table10384
+ GCC_except_table10385
+ GCC_except_table10386
+ GCC_except_table10387
+ GCC_except_table10388
+ GCC_except_table10389
+ GCC_except_table10390
+ GCC_except_table10391
+ GCC_except_table10392
+ GCC_except_table10393
+ GCC_except_table10394
+ GCC_except_table10395
+ GCC_except_table10396
+ GCC_except_table10397
+ GCC_except_table10398
+ GCC_except_table10399
+ GCC_except_table10400
+ GCC_except_table10401
+ GCC_except_table10402
+ GCC_except_table10403
+ GCC_except_table10404
+ GCC_except_table10405
+ GCC_except_table10406
+ GCC_except_table10407
+ GCC_except_table10408
+ GCC_except_table10409
+ GCC_except_table10410
+ GCC_except_table10411
+ GCC_except_table10412
+ GCC_except_table10413
+ GCC_except_table10414
+ GCC_except_table10415
+ GCC_except_table10416
+ GCC_except_table1044
+ GCC_except_table10527
+ GCC_except_table10536
+ GCC_except_table10537
+ GCC_except_table10538
+ GCC_except_table10539
+ GCC_except_table10553
+ GCC_except_table10571
+ GCC_except_table10604
+ GCC_except_table10605
+ GCC_except_table10606
+ GCC_except_table10607
+ GCC_except_table10608
+ GCC_except_table10636
+ GCC_except_table10637
+ GCC_except_table10638
+ GCC_except_table10639
+ GCC_except_table10640
+ GCC_except_table10641
+ GCC_except_table10643
+ GCC_except_table10644
+ GCC_except_table10645
+ GCC_except_table10682
+ GCC_except_table10683
+ GCC_except_table10687
+ GCC_except_table10706
+ GCC_except_table1071
+ GCC_except_table10711
+ GCC_except_table1075
+ GCC_except_table10793
+ GCC_except_table1084
+ GCC_except_table1086
+ GCC_except_table10886
+ GCC_except_table11054
+ GCC_except_table11073
+ GCC_except_table11076
+ GCC_except_table11077
+ GCC_except_table11103
+ GCC_except_table11105
+ GCC_except_table11195
+ GCC_except_table11223
+ GCC_except_table11757
+ GCC_except_table11914
+ GCC_except_table11917
+ GCC_except_table11923
+ GCC_except_table11931
+ GCC_except_table11935
+ GCC_except_table11937
+ GCC_except_table11941
+ GCC_except_table11947
+ GCC_except_table12053
+ GCC_except_table12073
+ GCC_except_table12075
+ GCC_except_table12077
+ GCC_except_table12079
+ GCC_except_table12163
+ GCC_except_table12170
+ GCC_except_table12172
+ GCC_except_table12174
+ GCC_except_table12180
+ GCC_except_table1220
+ GCC_except_table12217
+ GCC_except_table12348
+ GCC_except_table1236
+ GCC_except_table12374
+ GCC_except_table12386
+ GCC_except_table12428
+ GCC_except_table12430
+ GCC_except_table12443
+ GCC_except_table12552
+ GCC_except_table12597
+ GCC_except_table12606
+ GCC_except_table12607
+ GCC_except_table12614
+ GCC_except_table1263
+ GCC_except_table12652
+ GCC_except_table12659
+ GCC_except_table12671
+ GCC_except_table12676
+ GCC_except_table12726
+ GCC_except_table12818
+ GCC_except_table12821
+ GCC_except_table12827
+ GCC_except_table12829
+ GCC_except_table12869
+ GCC_except_table12888
+ GCC_except_table12899
+ GCC_except_table12961
+ GCC_except_table12964
+ GCC_except_table12972
+ GCC_except_table12978
+ GCC_except_table12980
+ GCC_except_table13045
+ GCC_except_table13123
+ GCC_except_table13127
+ GCC_except_table13131
+ GCC_except_table13168
+ GCC_except_table13192
+ GCC_except_table13199
+ GCC_except_table13338
+ GCC_except_table13350
+ GCC_except_table13444
+ GCC_except_table13511
+ GCC_except_table1355
+ GCC_except_table13717
+ GCC_except_table1372
+ GCC_except_table13796
+ GCC_except_table13838
+ GCC_except_table13887
+ GCC_except_table13897
+ GCC_except_table13917
+ GCC_except_table13960
+ GCC_except_table13962
+ GCC_except_table13975
+ GCC_except_table13977
+ GCC_except_table13979
+ GCC_except_table13998
+ GCC_except_table14144
+ GCC_except_table14155
+ GCC_except_table14182
+ GCC_except_table14188
+ GCC_except_table14204
+ GCC_except_table14274
+ GCC_except_table14276
+ GCC_except_table14322
+ GCC_except_table14324
+ GCC_except_table14348
+ GCC_except_table14351
+ GCC_except_table14505
+ GCC_except_table1461
+ GCC_except_table1553
+ GCC_except_table1578
+ GCC_except_table1624
+ GCC_except_table1699
+ GCC_except_table1797
+ GCC_except_table1898
+ GCC_except_table1902
+ GCC_except_table1922
+ GCC_except_table1927
+ GCC_except_table1941
+ GCC_except_table2134
+ GCC_except_table2136
+ GCC_except_table2138
+ GCC_except_table2140
+ GCC_except_table2147
+ GCC_except_table2154
+ GCC_except_table2156
+ GCC_except_table2170
+ GCC_except_table2222
+ GCC_except_table2224
+ GCC_except_table2226
+ GCC_except_table2228
+ GCC_except_table2230
+ GCC_except_table2232
+ GCC_except_table2235
+ GCC_except_table2237
+ GCC_except_table2246
+ GCC_except_table2248
+ GCC_except_table2251
+ GCC_except_table2253
+ GCC_except_table2255
+ GCC_except_table2284
+ GCC_except_table2286
+ GCC_except_table2289
+ GCC_except_table2292
+ GCC_except_table2332
+ GCC_except_table2400
+ GCC_except_table2405
+ GCC_except_table2416
+ GCC_except_table2428
+ GCC_except_table2466
+ GCC_except_table2637
+ GCC_except_table2650
+ GCC_except_table2678
+ GCC_except_table2693
+ GCC_except_table2712
+ GCC_except_table2722
+ GCC_except_table2759
+ GCC_except_table2764
+ GCC_except_table2826
+ GCC_except_table2929
+ GCC_except_table2940
+ GCC_except_table2942
+ GCC_except_table2948
+ GCC_except_table2956
+ GCC_except_table2988
+ GCC_except_table3064
+ GCC_except_table3069
+ GCC_except_table3074
+ GCC_except_table3077
+ GCC_except_table3087
+ GCC_except_table3098
+ GCC_except_table3100
+ GCC_except_table3107
+ GCC_except_table3234
+ GCC_except_table3238
+ GCC_except_table3241
+ GCC_except_table3308
+ GCC_except_table3316
+ GCC_except_table3351
+ GCC_except_table3355
+ GCC_except_table3360
+ GCC_except_table3490
+ GCC_except_table3527
+ GCC_except_table3536
+ GCC_except_table3546
+ GCC_except_table3550
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table3564
+ GCC_except_table3579
+ GCC_except_table3584
+ GCC_except_table3595
+ GCC_except_table3596
+ GCC_except_table3613
+ GCC_except_table3622
+ GCC_except_table3719
+ GCC_except_table3725
+ GCC_except_table3746
+ GCC_except_table3748
+ GCC_except_table3750
+ GCC_except_table3825
+ GCC_except_table3856
+ GCC_except_table3858
+ GCC_except_table3876
+ GCC_except_table3878
+ GCC_except_table3881
+ GCC_except_table4044
+ GCC_except_table4086
+ GCC_except_table4088
+ GCC_except_table4103
+ GCC_except_table4106
+ GCC_except_table4108
+ GCC_except_table4141
+ GCC_except_table4146
+ GCC_except_table4147
+ GCC_except_table4414
+ GCC_except_table4421
+ GCC_except_table4451
+ GCC_except_table4475
+ GCC_except_table4477
+ GCC_except_table4482
+ GCC_except_table4487
+ GCC_except_table4498
+ GCC_except_table4502
+ GCC_except_table4523
+ GCC_except_table4536
+ GCC_except_table4537
+ GCC_except_table4597
+ GCC_except_table4922
+ GCC_except_table4932
+ GCC_except_table4991
+ GCC_except_table4993
+ GCC_except_table4997
+ GCC_except_table4999
+ GCC_except_table5002
+ GCC_except_table5072
+ GCC_except_table5077
+ GCC_except_table5107
+ GCC_except_table5237
+ GCC_except_table5241
+ GCC_except_table5589
+ GCC_except_table5620
+ GCC_except_table5666
+ GCC_except_table5685
+ GCC_except_table5697
+ GCC_except_table5709
+ GCC_except_table5737
+ GCC_except_table5742
+ GCC_except_table5745
+ GCC_except_table5747
+ GCC_except_table5754
+ GCC_except_table5767
+ GCC_except_table5776
+ GCC_except_table5780
+ GCC_except_table5819
+ GCC_except_table5852
+ GCC_except_table5857
+ GCC_except_table5881
+ GCC_except_table5889
+ GCC_except_table5911
+ GCC_except_table5917
+ GCC_except_table5921
+ GCC_except_table5935
+ GCC_except_table5938
+ GCC_except_table5941
+ GCC_except_table5964
+ GCC_except_table5998
+ GCC_except_table6019
+ GCC_except_table6028
+ GCC_except_table6067
+ GCC_except_table6079
+ GCC_except_table6113
+ GCC_except_table6116
+ GCC_except_table6122
+ GCC_except_table6126
+ GCC_except_table6138
+ GCC_except_table6200
+ GCC_except_table6227
+ GCC_except_table6229
+ GCC_except_table6243
+ GCC_except_table6312
+ GCC_except_table6390
+ GCC_except_table6395
+ GCC_except_table6400
+ GCC_except_table6558
+ GCC_except_table6561
+ GCC_except_table6574
+ GCC_except_table6599
+ GCC_except_table6609
+ GCC_except_table6612
+ GCC_except_table6651
+ GCC_except_table6688
+ GCC_except_table6690
+ GCC_except_table7090
+ GCC_except_table7110
+ GCC_except_table7123
+ GCC_except_table7136
+ GCC_except_table7155
+ GCC_except_table7186
+ GCC_except_table7189
+ GCC_except_table7191
+ GCC_except_table7193
+ GCC_except_table7195
+ GCC_except_table7204
+ GCC_except_table7252
+ GCC_except_table7266
+ GCC_except_table7304
+ GCC_except_table7306
+ GCC_except_table7345
+ GCC_except_table7598
+ GCC_except_table7601
+ GCC_except_table7623
+ GCC_except_table7630
+ GCC_except_table7646
+ GCC_except_table7648
+ GCC_except_table7649
+ GCC_except_table7650
+ GCC_except_table7651
+ GCC_except_table7652
+ GCC_except_table7653
+ GCC_except_table7664
+ GCC_except_table7665
+ GCC_except_table7666
+ GCC_except_table7823
+ GCC_except_table8042
+ GCC_except_table8087
+ GCC_except_table8105
+ GCC_except_table8106
+ GCC_except_table8166
+ GCC_except_table8188
+ GCC_except_table8192
+ GCC_except_table8199
+ GCC_except_table8253
+ GCC_except_table8453
+ GCC_except_table8455
+ GCC_except_table8502
+ GCC_except_table8542
+ GCC_except_table8546
+ GCC_except_table8548
+ GCC_except_table8550
+ GCC_except_table8562
+ GCC_except_table8567
+ GCC_except_table8607
+ GCC_except_table8635
+ GCC_except_table8677
+ GCC_except_table8769
+ GCC_except_table8827
+ GCC_except_table8847
+ GCC_except_table8850
+ GCC_except_table8928
+ GCC_except_table8932
+ GCC_except_table8936
+ GCC_except_table8937
+ GCC_except_table8938
+ GCC_except_table8939
+ GCC_except_table8940
+ GCC_except_table8942
+ GCC_except_table8944
+ GCC_except_table8948
+ GCC_except_table8959
+ GCC_except_table8962
+ GCC_except_table8983
+ GCC_except_table9027
+ GCC_except_table9092
+ GCC_except_table9249
+ GCC_except_table9290
+ GCC_except_table9296
+ GCC_except_table9299
+ GCC_except_table9562
+ GCC_except_table9566
+ GCC_except_table9570
+ GCC_except_table9590
+ GCC_except_table9591
+ GCC_except_table9687
+ GCC_except_table9697
+ GCC_except_table9730
+ GCC_except_table9782
+ GCC_except_table9827
+ GCC_except_table9847
+ GCC_except_table9901
+ GCC_except_table9934
+ GCC_except_table9936
+ GCC_except_table994
+ _OBJC_CLASS_$_PFContentProvenanceResourceInfo
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyAddPFMetadata
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetProvenanceFlags
+ _OBJC_IVAR_$_PHAsset._provenanceState
+ _OBJC_IVAR_$_PHAssetCreationMetadataCopyOptions._shouldCopyProvenanceData
+ _OBJC_IVAR_$_PHAssetCreationRequest._originalProvenanceAssetFilename
+ _OBJC_IVAR_$_PHAssetCreationRequest._originalProvenanceAssetUUID
+ _OBJC_IVAR_$_PHAssetCreationRequest._processedProvenanceURL
+ _OBJC_IVAR_$_PHAssetCreationRequest._useMockProvenanceProcessingClientForUnitTestSupport
+ _OBJC_IVAR_$_PHAssetCreationRequestPlaceholderSupport._downloadSourceMode_shouldCopyProvenanceData
+ _OBJC_IVAR_$_PHAssetExportRequestOptions._forceProvenanceMetadataBaking
+ _OBJC_IVAR_$_PHAssetExportRequestOptions._shouldStripProvenance
+ _OBJC_IVAR_$_PHAssetPTPProperties._provenanceState
+ _OBJC_IVAR_$_PHAssetResourceCreationOptions._hasProvenanceData
+ _OBJC_IVAR_$_PHImportAsset._provenanceAsset
+ _OBJC_IVAR_$_PHPTPAssetManager._finalizationRequestLock_provenanceReadyAssets
+ _OBJC_IVAR_$_PHResourceLocalAvailabilityRequestOptions._preferUncombinedProvenanceResources
+ _OBJC_IVAR_$_PHResourceLocalAvailabilityRequestOptions._shouldStripProvenance
+ _PAMediaConversionIsCancellationError
+ _PAMediaConversionResourceRoleProvenanceUnprocessed
+ _PAMediaConversionServiceOptionColorSpaceKey
+ _PAMediaConversionServiceOptionFormatConversionOnlyKey
+ _PAMediaConversionServiceOptionIsContentProvenanceProcessingConversionKey
+ _PAMediaConversionServiceOptionJobPriorityKey
+ _PAMediaConversionServiceOptionLivePhotoPairingIdentifierKey
+ _PAMediaConversionServiceOptionProvenanceOriginalAssetLocalIdentifierKey
+ _PAMediaConversionServiceOptionRequestReasonKey
+ _PHAssetExportRequestOriginalProvenanceURLKey
+ _PHAssetExportRequestProvenanceMetadataOperationForAssetWithOptions
+ _PHQueryForAssetCollectionType_Album_block_invoke_109
+ _PHQueryForAssetCollectionType_CollectionShare_block_invoke_121
+ _PHQueryForAssetCollectionType_Conversation_block_invoke_118
+ _PHQueryForAssetCollectionType_ImportSession_block_invoke_117
+ _PHQueryForAssetCollectionType_Memory_block_invoke_113
+ _PHQueryForAssetCollectionType_MomentShare_block_invoke_115
+ _PHQueryForAssetCollectionType_Moment_block_invoke_110
+ _PHQueryForAssetCollectionType_NoFetchType_block_invoke_123
+ _PHQueryForAssetCollectionType_Other_block_invoke_122
+ _PHQueryForAssetCollectionType_PhotosHighlight_block_invoke_114
+ _PHQueryForAssetCollectionType_Project_block_invoke_119
+ _PHQueryForAssetCollectionType_SmartAlbum_block_invoke_111
+ _PHQueryForAssetCollectionType_Suggestion_block_invoke_116
+ _PHQueryForAssetCollectionType_Unknown_block_invoke_112
+ _PHQueryForAssetCollectionType_Utility_block_invoke_120
+ _PHQueryForAssetInAlbumKind_ActionCamVideoAlbum_block_invoke_99
+ _PHQueryForAssetInAlbumKind_ProResAlbum_block_invoke_98
+ _PHQueryForAssetInAlbumKind_ProvenanceAlbum
+ _PHQueryForAssetInAlbumKind_ProvenanceAlbum_block_invoke_96
+ _PHQueryForAssetInAlbumKind_SharedLibrarySharingSuggestionsAlbum_block_invoke_97
+ _PHQueryForAssetsAlbum_SortKeyOther_block_invoke_100
+ _PHQueryForAssetsInAlbum_SortKeyContentTitle_block_invoke_108
+ _PHQueryForAssetsInAlbum_SortKeyCreationDate_block_invoke_102
+ _PHQueryForAssetsInAlbum_SortKeyImportDate_block_invoke_104
+ _PHQueryForAssetsInAlbum_SortKeyLastModifiedDate_block_invoke_103
+ _PHQueryForAssetsInAlbum_SortKeyManual_block_invoke_101
+ _PHQueryForAssetsInAlbum_SortKeyPublishDate_block_invoke_107
+ _PHQueryForAssetsInAlbum_SortKeyTitle_block_invoke_106
+ _PHQueryForAssetsInAlbum_SortKeyTrashDate_block_invoke_105
+ _PHQueryForAssetsInUtility_GenericDocument_block_invoke_133
+ _PHQueryForAssetsInUtility_Handwriting_block_invoke_136
+ _PHQueryForAssetsInUtility_IdentityDocuments_block_invoke_139
+ _PHQueryForAssetsInUtility_Illustrations_block_invoke_135
+ _PHQueryForAssetsInUtility_Maps_block_invoke_138
+ _PHQueryForAssetsInUtility_Other_block_invoke_140
+ _PHQueryForAssetsInUtility_QRCodes_block_invoke_137
+ _PHQueryForAssetsInUtility_Receipts_block_invoke_134
+ _PHQueryForTransientAssetCollectionType_Generic_block_invoke_124
+ _PHQueryForTransientAssetCollectionType_ImportHistory_block_invoke_125
+ _PHQueryForTransientAssetCollectionType_Other_block_invoke_132
+ _PHQueryForTransientAssetCollectionType_RecentlyEdited_block_invoke_126
+ _PHQueryForTransientAssetCollectionType_RecentlyShared_block_invoke_127
+ _PHQueryForTransientAssetCollectionType_RecentlyViewed_block_invoke_128
+ _PHQueryForTransientAssetCollectionType_SavedToday_block_invoke_131
+ _PHQueryForTransientAssetCollectionType_SearchCollectionResults_block_invoke_130
+ _PHQueryForTransientAssetCollectionType_SearchTopResults_block_invoke_129
+ _PHResourceLocalAvailabilityRequestOriginalProvenanceURLKey
+ _PHResourceLocalAvailabilityRequestOriginalProvenanceUTIKey
+ _PHResourceLocalAvailabilityRequestProcessedProvenanceURLKey
+ _PLProvenanceGetLog
+ _PLShouldExcludeProvenanceOverPTPTransfer
+ __DATA__TtC6Photos20PHReferenceImageInfo
+ __DATA__TtC6Photos21PHAssetProvenanceInfo
+ __IVARS__TtC6Photos20PHReferenceImageInfo
+ __IVARS__TtC6Photos21PHAssetProvenanceInfo
+ __METACLASS_DATA__TtC6Photos20PHReferenceImageInfo
+ __METACLASS_DATA__TtC6Photos21PHAssetProvenanceInfo
+ __OBJC_$_CLASS_METHODS_PHAssetCreationRequestPlaceholderSupport
+ __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ __OBJC_CLASS_PROTOCOLS_$_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|ContentProvenance|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
+ ___51+[PHImportAsset scanAssetsForProvenanceData:atEnd:]_block_invoke
+ ___51+[PHImportAsset scanAssetsForProvenanceData:atEnd:]_block_invoke_2
+ ___73-[PHAssetCreationRequest performAsyncPreprocessingWithCompletionHandler:]_block_invoke
+ ___79+[PHAsset fetchProcessedProvenanceAssetWithOriginatingAssetIdentifier:options:]_block_invoke
+ ___88+[PHAssetExportRequest _insertAssetWithProcessedProvenanceResourceURL:unprocessedAsset:]_block_invoke
+ ___90+[PHAssetCreationRequest processedProvenanceReplacementForSharingAsset:completionHandler:]_block_invoke
+ ___90+[PHAssetCreationRequest processedProvenanceReplacementForSharingAsset:completionHandler:]_block_invoke_2
+ ___block_descriptor_112_e8_32s40s48s56bs64r72r80r88r96r104w_e5_v8?0lr64l8s32l8r72l8r80l8s40l8s48l8w104l8s56l8r88l8r96l8
+ ___block_descriptor_48_e8_32r40r_e42_v32?0"NSNumber"8"PHAssetResource"16^B24lr32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e20_v20?0B8"NSError"12lr56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e40_v32?0B8B12"NSDictionary"16"NSError"24lr56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e37_v32?0q8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e20_v24?0q8"NSError"16lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e40_v32?0B8B12"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e20_v24?0q8"NSError"16ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56r_e42_v32?0"NSNumber"8"PHAssetResource"16^B24ls32l8s40l8s48l8r56l8
+ ___swift_memcpy16_8
+ _kDCIMImageWriterProvenanceMetadataPathExtension
+ _kPLImageWriterProvenancePath
+ _objc_msgSend$_addProcessedProvenanceResourceToAssetResources:processedProvenanceResourceURL:unprocessedOriginal:error:
+ _objc_msgSend$_adjustedProvenanceRenderURLToShareForAsset:options:fileURLs:
+ _objc_msgSend$_cleanupTemporaryProvenanceFilesIfNecessary
+ _objc_msgSend$_creationRequestForProcessedProvenanceAssetFromUnprocessedProvenanceAsset:resourceBundle:processedProvenanceResourceURL:
+ _objc_msgSend$_getOriginalResource:sidecarProvenanceResource:
+ _objc_msgSend$_insertAssetWithProcessedProvenanceResourceURL:unprocessedAsset:
+ _objc_msgSend$_isProvenanceAssetRequiringProcessing:
+ _objc_msgSend$_processedProvenanceCarrierURLFromSourceAsset:
+ _objc_msgSend$_removeProvenanceSidecarResourcesFrom:byType:
+ _objc_msgSend$_setupProvenanceStateFromFetchDictionary:
+ _objc_msgSend$_shouldAddOriginalProvenanceResourceToResourcesToShareForAsset:shouldStripProvenance:
+ _objc_msgSend$_shouldCombineEditedProvenanceIntoRenderForAsset:options:fileURLs:
+ _objc_msgSend$_shouldEmbedProvenanceIntoRenderForSourceAsset:
+ _objc_msgSend$_updateAssetResourcesWithProcessedProvenanceResource:
+ _objc_msgSend$_validateProvenanceStateForProcessing:
+ _objc_msgSend$assetResourceForDuplicatingExternalAssetResource:creationOptions:
+ _objc_msgSend$creationRequestForProcessedProvenanceAssetFromUnprocessedProvenanceAsset:resourceInfo:
+ _objc_msgSend$embedProcessedProvenanceFromRegularImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:
+ _objc_msgSend$forceProvenanceMetadataBaking
+ _objc_msgSend$hasProvenanceData
+ _objc_msgSend$hasProvenanceMetadata
+ _objc_msgSend$hasUnprocessedProvenanceAuxiliaryMetadata
+ _objc_msgSend$hasUnprocessedProvenanceDNGMetadata
+ _objc_msgSend$initWithMetadata:
+ _objc_msgSend$initWithOriginalPhotoURL:alternatePhotoURL:fullSizePhotoURL:adjustmentBaseFullSizePhotoURL:spatialOvercapturePhotoURL:originalPairedVideoURL:fullSizePairedVideoURL:adjustmentBaseFullSizePairedVideoURL:spatialOvercapturePairedVideoURL:fullSizeVideoURL:adjustmentsURL:originalAdjustmentsURL:adjustmentsSecondaryDataURL:originalProvenanceURL:mediaSubtypes:playbackStyle:playbackVariation:videoComplementVisibilityState:
+ _objc_msgSend$initWithProvenanceState:
+ _objc_msgSend$lastAvailableContentProvenanceLowerBoundTimestampData
+ _objc_msgSend$livePhotoPairingIdentifierMetadataKey
+ _objc_msgSend$maskForProvenanceProcessingExclusions
+ _objc_msgSend$originalProvenanceAssetUUID
+ _objc_msgSend$originalProvenanceURL
+ _objc_msgSend$performChangesWithProgress:completionHandler:
+ _objc_msgSend$policyWithKey:value:
+ _objc_msgSend$powderState
+ _objc_msgSend$preferUncombinedProvenanceResources
+ _objc_msgSend$processPotentialProvenanceAsset:plusProvenanceDNG:
+ _objc_msgSend$provenanceAsset
+ _objc_msgSend$provenanceAssetDidProcessFromOriginalAssetWithUUID:error:
+ _objc_msgSend$provenanceFlags
+ _objc_msgSend$provenanceState
+ _objc_msgSend$scheduleProvenanceTimestampBackgroundJob
+ _objc_msgSend$setHasProvenanceData:
+ _objc_msgSend$setOriginalProvenanceAssetFilename:
+ _objc_msgSend$setOriginalProvenanceAssetUUID:
+ _objc_msgSend$setPowderState:
+ _objc_msgSend$setPreferUncombinedProvenanceResources:
+ _objc_msgSend$setProvenanceAsset:
+ _objc_msgSend$setProvenanceMetadataBehavior:withProcessedSourceImageURL:
+ _objc_msgSend$setProvenanceMetadataBehavior:withProvenanceSidecarURL:
+ _objc_msgSend$setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:
+ _objc_msgSend$setResourceURL:forRole:
+ _objc_msgSend$setShouldCopyProvenanceData:
+ _objc_msgSend$setShouldPreserveProvenance:
+ _objc_msgSend$setShouldStripProvenance:
+ _objc_msgSend$setUrlForTransfer:
+ _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:copyProvenanceData:isCurrentUser:library:
+ _objc_msgSend$shouldCopyProvenanceData
+ _objc_msgSend$shouldEmbedProvenanceIntoSharedRenderForAsset:shouldCopyProvenanceData:
+ _objc_msgSend$shouldStripProvenance
+ _objc_msgSend$shouldStripProvenanceForAsset:shouldCopyProvenanceData:
+ _objc_msgSend$stripProvenanceExtensionFrompPath:
+ _objc_msgSend$stripProvenanceMetadataFromOriginalProvenanceImageAtURL:destinationURL:options:completionHandler:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getEnumCaseMultiPayload
+ _swift_storeEnumTagMultiPayload
+ _symbolic So31PFContentProvenanceResourceInfoCSg
+ _symbolic So7PHAssetC
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 6Photos20PHReferenceImageInfoC
+ _symbolic _____ 6Photos20PHReferenceImageInfoC0C6Source33_1A73BF63275DDEEDDC1664B3A274BE79LLO
+ _symbolic _____ 6Photos20PHReferenceImageInfoC10CacheState33_1A73BF63275DDEEDDC1664B3A274BE79LLV
+ _symbolic _____ 6Photos21PHAssetProvenanceInfoC
+ _symbolic _____Sg 22UniformTypeIdentifiers6UTTypeV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 6Photos20PHReferenceImageInfoC10CacheState33_1A73BF63275DDEEDDC1664B3A274BE79LLV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 6Photos20PHReferenceImageInfoC10CacheState33_1A73BF63275DDEEDDC1664B3A274BE79LLV So16os_unfair_lock_sV
+ _type_layout_string 6Photos20PHReferenceImageInfoC10CacheState33_1A73BF63275DDEEDDC1664B3A274BE79LLV
- GCC_except_table10055
- GCC_except_table10177
- GCC_except_table10187
- GCC_except_table10201
- GCC_except_table10202
- GCC_except_table10209
- GCC_except_table10212
- GCC_except_table10235
- GCC_except_table10236
- GCC_except_table10237
- GCC_except_table10238
- GCC_except_table10239
- GCC_except_table10241
- GCC_except_table10242
- GCC_except_table10245
- GCC_except_table10246
- GCC_except_table10247
- GCC_except_table10248
- GCC_except_table10249
- GCC_except_table10251
- GCC_except_table10252
- GCC_except_table10254
- GCC_except_table10255
- GCC_except_table10256
- GCC_except_table10257
- GCC_except_table10258
- GCC_except_table10259
- GCC_except_table10260
- GCC_except_table10261
- GCC_except_table10262
- GCC_except_table10263
- GCC_except_table10266
- GCC_except_table10267
- GCC_except_table10269
- GCC_except_table10270
- GCC_except_table10271
- GCC_except_table10273
- GCC_except_table10274
- GCC_except_table10276
- GCC_except_table10277
- GCC_except_table10279
- GCC_except_table10280
- GCC_except_table10281
- GCC_except_table10282
- GCC_except_table10283
- GCC_except_table10284
- GCC_except_table10285
- GCC_except_table10286
- GCC_except_table10287
- GCC_except_table10288
- GCC_except_table10289
- GCC_except_table10290
- GCC_except_table10291
- GCC_except_table10292
- GCC_except_table10293
- GCC_except_table10294
- GCC_except_table10295
- GCC_except_table10296
- GCC_except_table10297
- GCC_except_table10306
- GCC_except_table10307
- GCC_except_table10316
- GCC_except_table10331
- GCC_except_table10341
- GCC_except_table1039
- GCC_except_table10463
- GCC_except_table10472
- GCC_except_table10473
- GCC_except_table10474
- GCC_except_table10475
- GCC_except_table10476
- GCC_except_table10477
- GCC_except_table10478
- GCC_except_table10489
- GCC_except_table10507
- GCC_except_table10543
- GCC_except_table10544
- GCC_except_table10554
- GCC_except_table10572
- GCC_except_table10573
- GCC_except_table10574
- GCC_except_table10575
- GCC_except_table10576
- GCC_except_table10577
- GCC_except_table10578
- GCC_except_table10579
- GCC_except_table10580
- GCC_except_table10581
- GCC_except_table1061
- GCC_except_table10619
- GCC_except_table10623
- GCC_except_table10647
- GCC_except_table1065
- GCC_except_table10729
- GCC_except_table1074
- GCC_except_table1076
- GCC_except_table10822
- GCC_except_table10989
- GCC_except_table11008
- GCC_except_table11011
- GCC_except_table11012
- GCC_except_table11038
- GCC_except_table11040
- GCC_except_table11130
- GCC_except_table11158
- GCC_except_table11692
- GCC_except_table11849
- GCC_except_table11852
- GCC_except_table11858
- GCC_except_table11866
- GCC_except_table11870
- GCC_except_table11872
- GCC_except_table11876
- GCC_except_table11882
- GCC_except_table11988
- GCC_except_table12007
- GCC_except_table12009
- GCC_except_table12011
- GCC_except_table12013
- GCC_except_table12048
- GCC_except_table12097
- GCC_except_table1210
- GCC_except_table12104
- GCC_except_table12106
- GCC_except_table12108
- GCC_except_table12151
- GCC_except_table1226
- GCC_except_table12282
- GCC_except_table12308
- GCC_except_table12320
- GCC_except_table12362
- GCC_except_table12364
- GCC_except_table12377
- GCC_except_table12482
- GCC_except_table12486
- GCC_except_table12527
- GCC_except_table1253
- GCC_except_table12531
- GCC_except_table12540
- GCC_except_table12541
- GCC_except_table12586
- GCC_except_table12605
- GCC_except_table12610
- GCC_except_table12660
- GCC_except_table12752
- GCC_except_table12755
- GCC_except_table12761
- GCC_except_table12763
- GCC_except_table12803
- GCC_except_table12822
- GCC_except_table12833
- GCC_except_table12895
- GCC_except_table12898
- GCC_except_table12906
- GCC_except_table12912
- GCC_except_table12914
- GCC_except_table12979
- GCC_except_table13057
- GCC_except_table13061
- GCC_except_table13065
- GCC_except_table13102
- GCC_except_table13126
- GCC_except_table13133
- GCC_except_table13272
- GCC_except_table13284
- GCC_except_table13378
- GCC_except_table13445
- GCC_except_table1345
- GCC_except_table1362
- GCC_except_table13651
- GCC_except_table13730
- GCC_except_table13772
- GCC_except_table13821
- GCC_except_table13831
- GCC_except_table13851
- GCC_except_table13866
- GCC_except_table13894
- GCC_except_table13896
- GCC_except_table13909
- GCC_except_table13911
- GCC_except_table13913
- GCC_except_table14078
- GCC_except_table14089
- GCC_except_table14116
- GCC_except_table14122
- GCC_except_table14138
- GCC_except_table14208
- GCC_except_table14210
- GCC_except_table14256
- GCC_except_table14258
- GCC_except_table14282
- GCC_except_table14285
- GCC_except_table14439
- GCC_except_table1451
- GCC_except_table1543
- GCC_except_table1568
- GCC_except_table1614
- GCC_except_table1689
- GCC_except_table1787
- GCC_except_table1888
- GCC_except_table1892
- GCC_except_table1912
- GCC_except_table1917
- GCC_except_table1921
- GCC_except_table2118
- GCC_except_table2122
- GCC_except_table2124
- GCC_except_table2126
- GCC_except_table2128
- GCC_except_table2132
- GCC_except_table2135
- GCC_except_table2146
- GCC_except_table2190
- GCC_except_table2192
- GCC_except_table2194
- GCC_except_table2196
- GCC_except_table2198
- GCC_except_table2200
- GCC_except_table2223
- GCC_except_table2225
- GCC_except_table2227
- GCC_except_table2229
- GCC_except_table2231
- GCC_except_table2234
- GCC_except_table2236
- GCC_except_table2271
- GCC_except_table2273
- GCC_except_table2276
- GCC_except_table2279
- GCC_except_table2383
- GCC_except_table2388
- GCC_except_table2396
- GCC_except_table2406
- GCC_except_table2444
- GCC_except_table2615
- GCC_except_table2628
- GCC_except_table2656
- GCC_except_table2671
- GCC_except_table2690
- GCC_except_table2700
- GCC_except_table2737
- GCC_except_table2742
- GCC_except_table2804
- GCC_except_table2907
- GCC_except_table2918
- GCC_except_table2920
- GCC_except_table2926
- GCC_except_table2934
- GCC_except_table2966
- GCC_except_table3042
- GCC_except_table3047
- GCC_except_table3052
- GCC_except_table3055
- GCC_except_table3065
- GCC_except_table3076
- GCC_except_table3078
- GCC_except_table3085
- GCC_except_table3212
- GCC_except_table3216
- GCC_except_table3219
- GCC_except_table3286
- GCC_except_table3294
- GCC_except_table3329
- GCC_except_table3333
- GCC_except_table3338
- GCC_except_table3468
- GCC_except_table3501
- GCC_except_table3507
- GCC_except_table3510
- GCC_except_table3520
- GCC_except_table3524
- GCC_except_table3530
- GCC_except_table3537
- GCC_except_table3541
- GCC_except_table3552
- GCC_except_table3557
- GCC_except_table3569
- GCC_except_table3585
- GCC_except_table3594
- GCC_except_table3691
- GCC_except_table3697
- GCC_except_table3718
- GCC_except_table3720
- GCC_except_table3722
- GCC_except_table3769
- GCC_except_table3828
- GCC_except_table3830
- GCC_except_table3848
- GCC_except_table3850
- GCC_except_table3853
- GCC_except_table4016
- GCC_except_table4050
- GCC_except_table4058
- GCC_except_table4060
- GCC_except_table4075
- GCC_except_table4080
- GCC_except_table4113
- GCC_except_table4118
- GCC_except_table4119
- GCC_except_table4373
- GCC_except_table4380
- GCC_except_table4408
- GCC_except_table4431
- GCC_except_table4433
- GCC_except_table4438
- GCC_except_table4443
- GCC_except_table4454
- GCC_except_table4458
- GCC_except_table4476
- GCC_except_table4543
- GCC_except_table4868
- GCC_except_table4878
- GCC_except_table4937
- GCC_except_table4939
- GCC_except_table4943
- GCC_except_table4945
- GCC_except_table4948
- GCC_except_table5018
- GCC_except_table5023
- GCC_except_table5053
- GCC_except_table5183
- GCC_except_table5187
- GCC_except_table5535
- GCC_except_table5566
- GCC_except_table5612
- GCC_except_table5631
- GCC_except_table5637
- GCC_except_table5643
- GCC_except_table5655
- GCC_except_table5657
- GCC_except_table5683
- GCC_except_table5688
- GCC_except_table5693
- GCC_except_table5699
- GCC_except_table5707
- GCC_except_table5720
- GCC_except_table5724
- GCC_except_table5796
- GCC_except_table5801
- GCC_except_table5825
- GCC_except_table5829
- GCC_except_table5833
- GCC_except_table5855
- GCC_except_table5861
- GCC_except_table5865
- GCC_except_table5879
- GCC_except_table5882
- GCC_except_table5908
- GCC_except_table5942
- GCC_except_table5963
- GCC_except_table5972
- GCC_except_table6011
- GCC_except_table6023
- GCC_except_table6057
- GCC_except_table6060
- GCC_except_table6066
- GCC_except_table6070
- GCC_except_table6082
- GCC_except_table6115
- GCC_except_table6144
- GCC_except_table6173
- GCC_except_table6187
- GCC_except_table6256
- GCC_except_table6333
- GCC_except_table6338
- GCC_except_table6343
- GCC_except_table6501
- GCC_except_table6504
- GCC_except_table6517
- GCC_except_table6542
- GCC_except_table6552
- GCC_except_table6555
- GCC_except_table6593
- GCC_except_table6630
- GCC_except_table6632
- GCC_except_table7031
- GCC_except_table7051
- GCC_except_table7064
- GCC_except_table7077
- GCC_except_table7096
- GCC_except_table7126
- GCC_except_table7129
- GCC_except_table7131
- GCC_except_table7133
- GCC_except_table7135
- GCC_except_table7144
- GCC_except_table7192
- GCC_except_table7206
- GCC_except_table7242
- GCC_except_table7244
- GCC_except_table7283
- GCC_except_table7536
- GCC_except_table7539
- GCC_except_table7561
- GCC_except_table7568
- GCC_except_table7584
- GCC_except_table7586
- GCC_except_table7587
- GCC_except_table7588
- GCC_except_table7589
- GCC_except_table7590
- GCC_except_table7591
- GCC_except_table7602
- GCC_except_table7603
- GCC_except_table7604
- GCC_except_table7761
- GCC_except_table7980
- GCC_except_table8025
- GCC_except_table8043
- GCC_except_table8044
- GCC_except_table8104
- GCC_except_table8126
- GCC_except_table8130
- GCC_except_table8137
- GCC_except_table8191
- GCC_except_table8391
- GCC_except_table8393
- GCC_except_table8440
- GCC_except_table8480
- GCC_except_table8484
- GCC_except_table8486
- GCC_except_table8488
- GCC_except_table8500
- GCC_except_table8505
- GCC_except_table8545
- GCC_except_table8573
- GCC_except_table8615
- GCC_except_table8706
- GCC_except_table8764
- GCC_except_table8784
- GCC_except_table8787
- GCC_except_table8806
- GCC_except_table8865
- GCC_except_table8873
- GCC_except_table8874
- GCC_except_table8875
- GCC_except_table8876
- GCC_except_table8877
- GCC_except_table8879
- GCC_except_table8881
- GCC_except_table8885
- GCC_except_table8896
- GCC_except_table8899
- GCC_except_table8920
- GCC_except_table8964
- GCC_except_table9029
- GCC_except_table9186
- GCC_except_table9227
- GCC_except_table9233
- GCC_except_table9236
- GCC_except_table9499
- GCC_except_table9503
- GCC_except_table9507
- GCC_except_table9527
- GCC_except_table9528
- GCC_except_table9624
- GCC_except_table9634
- GCC_except_table9667
- GCC_except_table9719
- GCC_except_table9764
- GCC_except_table9784
- GCC_except_table9810
- GCC_except_table9838
- GCC_except_table9871
- GCC_except_table990
- GCC_except_table9964
- _OUTLINED_FUNCTION_27
- _PHQueryForAssetCollectionType_Album_block_invoke_108
- _PHQueryForAssetCollectionType_CollectionShare_block_invoke_120
- _PHQueryForAssetCollectionType_Conversation_block_invoke_117
- _PHQueryForAssetCollectionType_ImportSession_block_invoke_116
- _PHQueryForAssetCollectionType_Memory_block_invoke_112
- _PHQueryForAssetCollectionType_MomentShare_block_invoke_114
- _PHQueryForAssetCollectionType_Moment_block_invoke_109
- _PHQueryForAssetCollectionType_NoFetchType_block_invoke_122
- _PHQueryForAssetCollectionType_Other_block_invoke_121
- _PHQueryForAssetCollectionType_PhotosHighlight_block_invoke_113
- _PHQueryForAssetCollectionType_Project_block_invoke_118
- _PHQueryForAssetCollectionType_SmartAlbum_block_invoke_110
- _PHQueryForAssetCollectionType_Suggestion_block_invoke_115
- _PHQueryForAssetCollectionType_Unknown_block_invoke_111
- _PHQueryForAssetCollectionType_Utility_block_invoke_119
- _PHQueryForAssetInAlbumKind_ActionCamVideoAlbum_block_invoke_98
- _PHQueryForAssetInAlbumKind_ProResAlbum_block_invoke_97
- _PHQueryForAssetInAlbumKind_SharedLibrarySharingSuggestionsAlbum_block_invoke_96
- _PHQueryForAssetsAlbum_SortKeyOther_block_invoke_99
- _PHQueryForAssetsInAlbum_SortKeyContentTitle_block_invoke_107
- _PHQueryForAssetsInAlbum_SortKeyCreationDate_block_invoke_101
- _PHQueryForAssetsInAlbum_SortKeyImportDate_block_invoke_103
- _PHQueryForAssetsInAlbum_SortKeyLastModifiedDate_block_invoke_102
- _PHQueryForAssetsInAlbum_SortKeyManual_block_invoke_100
- _PHQueryForAssetsInAlbum_SortKeyPublishDate_block_invoke_106
- _PHQueryForAssetsInAlbum_SortKeyTitle_block_invoke_105
- _PHQueryForAssetsInAlbum_SortKeyTrashDate_block_invoke_104
- _PHQueryForAssetsInUtility_GenericDocument_block_invoke_132
- _PHQueryForAssetsInUtility_Handwriting_block_invoke_135
- _PHQueryForAssetsInUtility_IdentityDocuments_block_invoke_138
- _PHQueryForAssetsInUtility_Illustrations_block_invoke_134
- _PHQueryForAssetsInUtility_Maps_block_invoke_137
- _PHQueryForAssetsInUtility_Other_block_invoke_139
- _PHQueryForAssetsInUtility_QRCodes_block_invoke_136
- _PHQueryForAssetsInUtility_Receipts_block_invoke_133
- _PHQueryForTransientAssetCollectionType_Generic_block_invoke_123
- _PHQueryForTransientAssetCollectionType_ImportHistory_block_invoke_124
- _PHQueryForTransientAssetCollectionType_Other_block_invoke_131
- _PHQueryForTransientAssetCollectionType_RecentlyEdited_block_invoke_125
- _PHQueryForTransientAssetCollectionType_RecentlyShared_block_invoke_126
- _PHQueryForTransientAssetCollectionType_RecentlyViewed_block_invoke_127
- _PHQueryForTransientAssetCollectionType_SavedToday_block_invoke_130
- _PHQueryForTransientAssetCollectionType_SearchCollectionResults_block_invoke_129
- _PHQueryForTransientAssetCollectionType_SearchTopResults_block_invoke_128
- __OBJC_$_CLASS_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_$_INSTANCE_METHODS_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- __OBJC_CLASS_PROTOCOLS_$_PHPhotoLibrary(ImportDeDup|Search|MediaProcessing|PHDebugUtilities|PHAdoptionUtilities|Repair|PhotosFormat|ProjectExtensions|Widgets|MigrationDate|CloudIdentifierReservations|PXCPLStatus|CollectionShare|PHAsset|CloudPhotoLibrary|FeatureAvailability|CloudIdentifiers|PHBatchFetchingArray|PersonAvailability|AssetAnalysis|PhotosKnowledgeSPI|DuplicateProcessing)
- ___block_descriptor_40_e8_32r_e42_v32?0"NSNumber"8"PHAssetResource"16^B24lr32l8
- ___block_descriptor_81_e8_32s40s48r_e42_v32?0"NSNumber"8"PHAssetResource"16^B24ls32l8s40l8r48l8
- ___block_descriptor_96_e8_32s40s48s56bs64r72r80r88r_e5_v8?0lr64l8s32l8s40l8s48l8r72l8r80l8r88l8s56l8
- _objc_msgSend$initWithOriginalPhotoURL:alternatePhotoURL:fullSizePhotoURL:adjustmentBaseFullSizePhotoURL:spatialOvercapturePhotoURL:originalPairedVideoURL:fullSizePairedVideoURL:adjustmentBaseFullSizePairedVideoURL:spatialOvercapturePairedVideoURL:fullSizeVideoURL:adjustmentsURL:originalAdjustmentsURL:adjustmentsSecondaryDataURL:mediaSubtypes:playbackStyle:playbackVariation:videoComplementVisibilityState:
- _objc_msgSend$setupPlaceholderAssetWithRequiredPropertiesFromSourceAsset:placeholderAssetUUID:bundleScope:share:importSessionID:bakeInAdjustmentsFromSourceAsset:flattenLivePhoto:copyTitleDescriptionAndKeywords:copyCameraProcessingAdjustmentResources:isCurrentUser:library:
CStrings:
+ " shouldCopyProvenanceData=%d"
+ "%@ missing resources for provenance processing"
+ "%@.DNG"
+ "%K == %ld"
+ "+[PHResourceLocalAvailabilityRequest _singularResourcesToShareForAsset:fromAvailableResources:options:useOriginalResources:knownUnsupported:error:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/Projects/PhotoKit/Sources/PHResourceLocalAvailabilityRequest.m"
+ "<%@: %p, variant: \"%@\", livePhotoAsStill: %d, allowRaw: %d, flattenSlomo: %d, stripLocation: %d, stripProvenance: %d, stripCaption: %d, stripAXDescription: %d, stripKeywords: %d, assetBundle: %d, disableMetadataCorrections: %d, unmodifiedOriginals: %d>"
+ "Adding provenance-ready asset (%{public}@) to delegate"
+ "Asset %@ is not in a provenance state that can be processed for sharing"
+ "CombiningProvenanceResources"
+ "Creating processed provenance resource from asset: %@ new asset UUID: %@ from combined-provenance resource: %d"
+ "Edited provenance asset selected its original as a provenance source but has no full-size render to carry it"
+ "Error deleting temporary directory %@"
+ "Failed to embed processed provenance into shared render for source asset %@"
+ "Failed to insert processed provenance replacement for asset %@"
+ "Failed to insert processed provenance replacement for asset %{public}@: %@"
+ "Failed to retrieve resources to process provenance for share for asset %@"
+ "Failed to retrieve resources to process provenance for share for asset %{public}@ (success=%d cancelled=%d): %@"
+ "Ignoring provenance-ready asset (%{public}@) due to on-demand processing error: %{public}@"
+ "ImageConversionService async processing failed: %@"
+ "Missing original provenance resource for source asset %@"
+ "Missing photo resource to regenerate provenance for source asset %@"
+ "MissingProcessedProvenanceResource"
+ "No combined provenance resource (virtual or otherwise) for asset (%{public}@), primary original may already contain embedded DNG"
+ "No photo library for asset %@; cannot process provenance for share"
+ "No photoLibrary for asset %{public}@; cannot process provenance for share"
+ "PAIRING: setting %@ as provenance asset of %@"
+ "PHAssetCreationRequest provenance development"
+ "PHAssetCreationRequestPlaceholderSupport-ProvenanceRenderEmbed-%@"
+ "PHAssetCreationRequestPlaceholderSupport-ProvenanceStrip-%@"
+ "PHAssetExportRequestMetadataOperation PHAssetExportRequestProvenanceMetadataOperationForAssetWithOptions(PHAsset *__strong _Nonnull, PHAssetExportRequestOptions *__strong _Nonnull, NSDictionary<PHAssetExportRequestFileURLKey,NSURL *> *__strong _Nonnull)"
+ "PHAssetExportRequestOriginalProvenanceURLKey"
+ "PHQueryForAssetCollectionType_Album_block_invoke_109"
+ "PHQueryForAssetCollectionType_CollectionShare_block_invoke_121"
+ "PHQueryForAssetCollectionType_Conversation_block_invoke_118"
+ "PHQueryForAssetCollectionType_ImportSession_block_invoke_117"
+ "PHQueryForAssetCollectionType_Memory_block_invoke_113"
+ "PHQueryForAssetCollectionType_MomentShare_block_invoke_115"
+ "PHQueryForAssetCollectionType_Moment_block_invoke_110"
+ "PHQueryForAssetCollectionType_NoFetchType_block_invoke_123"
+ "PHQueryForAssetCollectionType_Other_block_invoke_122"
+ "PHQueryForAssetCollectionType_PhotosHighlight_block_invoke_114"
+ "PHQueryForAssetCollectionType_Project_block_invoke_119"
+ "PHQueryForAssetCollectionType_SmartAlbum_block_invoke_111"
+ "PHQueryForAssetCollectionType_Suggestion_block_invoke_116"
+ "PHQueryForAssetCollectionType_Unknown_block_invoke_112"
+ "PHQueryForAssetCollectionType_Utility_block_invoke_120"
+ "PHQueryForAssetInAlbumKind_ActionCamVideoAlbum_block_invoke_99"
+ "PHQueryForAssetInAlbumKind_ProResAlbum_block_invoke_98"
+ "PHQueryForAssetInAlbumKind_ProvenanceAlbum_block_invoke_96"
+ "PHQueryForAssetInAlbumKind_SharedLibrarySharingSuggestionsAlbum_block_invoke_97"
+ "PHQueryForAssetsAlbum_SortKeyOther_block_invoke_100"
+ "PHQueryForAssetsInAlbum_SortKeyContentTitle_block_invoke_108"
+ "PHQueryForAssetsInAlbum_SortKeyCreationDate_block_invoke_102"
+ "PHQueryForAssetsInAlbum_SortKeyImportDate_block_invoke_104"
+ "PHQueryForAssetsInAlbum_SortKeyLastModifiedDate_block_invoke_103"
+ "PHQueryForAssetsInAlbum_SortKeyManual_block_invoke_101"
+ "PHQueryForAssetsInAlbum_SortKeyPublishDate_block_invoke_107"
+ "PHQueryForAssetsInAlbum_SortKeyTitle_block_invoke_106"
+ "PHQueryForAssetsInAlbum_SortKeyTrashDate_block_invoke_105"
+ "PHQueryForAssetsInUtility_GenericDocument_block_invoke_133"
+ "PHQueryForAssetsInUtility_Handwriting_block_invoke_136"
+ "PHQueryForAssetsInUtility_IdentityDocuments_block_invoke_139"
+ "PHQueryForAssetsInUtility_Illustrations_block_invoke_135"
+ "PHQueryForAssetsInUtility_Maps_block_invoke_138"
+ "PHQueryForAssetsInUtility_Other_block_invoke_140"
+ "PHQueryForAssetsInUtility_QRCodes_block_invoke_137"
+ "PHQueryForAssetsInUtility_Receipts_block_invoke_134"
+ "PHQueryForTransientAssetCollectionType_Generic_block_invoke_124"
+ "PHQueryForTransientAssetCollectionType_ImportHistory_block_invoke_125"
+ "PHQueryForTransientAssetCollectionType_Other_block_invoke_132"
+ "PHQueryForTransientAssetCollectionType_RecentlyEdited_block_invoke_126"
+ "PHQueryForTransientAssetCollectionType_RecentlyShared_block_invoke_127"
+ "PHQueryForTransientAssetCollectionType_RecentlyViewed_block_invoke_128"
+ "PHQueryForTransientAssetCollectionType_SavedToday_block_invoke_131"
+ "PHQueryForTransientAssetCollectionType_SearchCollectionResults_block_invoke_130"
+ "PHQueryForTransientAssetCollectionType_SearchTopResults_block_invoke_129"
+ "PHResourceLocalAvailabilityRequestOriginalProvenanceURLKey"
+ "PHResourceLocalAvailabilityRequestOriginalProvenanceUTIKey"
+ "PHResourceLocalAvailabilityRequestProcessedProvenanceURLKey"
+ "PHResourceLocalAvailabilityRequestResourceAvailabilityProvenanceCombiningRequired"
+ "Photo URL is unexpectedly nil in the resourceInfo dictionary"
+ "Primary original already contains embedded DNG for asset (%{public}@)"
+ "Processed provenance asset will be created from pre-processed resource at url: %@ for asset %@"
+ "Processed provenance asset will be created from the combined-provenance resource at url: %@ for asset %@"
+ "Processed provenance asset will be created from the original resource at url: %@ and provenance resource url: %@ for asset %@"
+ "Processed provenance resource created from asset: %@"
+ "Provenance asset (%{public}@) provenanceState=%d does not require processing"
+ "Provenance asset (%{public}@) provenanceState=%d requires processing"
+ "Provenance processing for asset %{public}@ cancelled before develop"
+ "Provenance processing for asset %{public}@ cancelled during develop"
+ "Provenance transfer over PTP disabled; asset (%{public}@) does not require processing"
+ "Requires provenance processing for asset (%{public}@)"
+ "Separate DNG resource exists for asset (%{public}@), awaiting combined resource from processing"
+ "Unable to remove processed provenance temp directory: %@"
+ "Using combined provenance resource for asset (%{public}@)"
+ "[PHAssetCreationRequestPlaceholderSupport] Failed to embed processed provenance into shared render for source asset %{public}@: %@; failing share"
+ "[PHAssetCreationRequestPlaceholderSupport] Missing original resource with provenance data for source asset %{public}@; failing share"
+ "[PHAssetCreationRequestPlaceholderSupport] No Photo resource to regenerate provenance for source asset %{public}@; failing share"
+ "[PHAssetExportRequest] Adjusted processed provenance asset missing original or full-size photo URL."
+ "[PHAssetExportRequest] Asset is unprocessed provenance but we are missing the original photo. "
+ "[PHAssetExportRequest] Expected to embed provenance into full-size render for asset %{public}@ but missing URL: fullSizePhoto=%{public}@ photo=%{public}@"
+ "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%{public}@, metadataOperationProvenance=%{public}@, metadataOperationCaption=%{public}@, metadataOperationCaptionAccessibilityDescription=%{public}@, metadataOperationKeywords=%{public}@, metadataChangeCustomDate=%{private}@, livePhotoMetadataFixup=%{BOOL}d producingNewFilesForExport=%{BOOL}d, options.variant=%{public}@, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@, needsReplacementLivePhotoIdentifier = %{BOOL}d %{public}@"
+ "[PHAssetExportRequest] Failed to build processed provenance creation request for asset %{public}@"
+ "[PHAssetExportRequest] Failed to insert processed provenance asset: %@"
+ "[PHAssetExportRequest] Failed to remove staging directory at %@: %@"
+ "[PHAssetExportRequest] Failed to remove temporary processed provenance original directory for asset %{public}@: %@"
+ "[PHAssetExportRequest] Failed to retrieve required resources for processed provenance insertion for asset %{public}@ (success=%d cancelled=%d): %@"
+ "[PHAssetExportRequest] Failed to stage processed provenance resource for asset %{public}@: %@"
+ "[PHAssetExportRequest] Inserting processed provenance asset for asset %{public}@"
+ "[PHAssetExportRequest] Processed provenance insertion for asset %{public}@ completed (request: %p)"
+ "[PHAssetExportRequest] Returning provenanceMetadataOperation: %ld. Asset state: %hi"
+ "[PHAssetExportRequest] Skipping processed-provenance insertion for asset %{public}@: exported resource is not processed provenance (state=%hd)"
+ "[PHAssetExportRequest] We processed fileURLs %@. Removing the DNG and remained with these fileURLs to share: %@"
+ "[PHInternalAssetExportRequest] Waiting for provenance combining of resources of asset %{public}@..."
+ "[PHResourceLocalAvailabilityRequest: %llu] Failed to refetch resources for combined provenance asset: %{public}@, "
+ "[PHResourceLocalAvailabilityRequest] Refusing to pair provenance sidecar with derivative-only resources for asset: %@, resources: %@, options: %@"
+ "[PHResourceLocalAvailabilityRequest] Routing edited provenance render to FullSizePhotoURLKey (keeping original in PhotoURLKey) for asset:%@"
+ "[PHResourceLocalAvailabilityRequest] Selected original as provenance source but no full-size render is available to carry it for asset: %@, resources: %@, options: %@"
+ "[PHResourceLocalAvailabilityRequest] Using original/primary resource(s): %{BOOL}d for asset %{public}@ because it is edited: %{BOOL}d, known unsupported: %{BOOL}d, isRAW: %{BOOL}d, dontAllowRAW: %{BOOL}d, should use unmodified original: %{BOOL}d requiresCombinedProvenance:%{BOOL}d"
+ "_PHResourceLocalAvailabilityRequestResourceTypeCombinedProvenance"
+ "_PHResourceLocalAvailabilityRequestResourceTypeOriginalProvenance"
+ "asset %{public}@ is ineligible for provenance processing (savedAssetType: %{public}@)"
+ "asset %{public}@ is not in unprocessed provenance (state: %d)"
+ "asset %{public}@ is trashed; refusing create a provenance processing request"
+ "combined_provenance"
+ "hasProvenanceData"
+ "originalProvenanceAssetFilename"
+ "originalProvenanceAssetUUID"
+ "powderState"
+ "provenance"
+ "provenance combining"
+ "provenance resource not for display"
+ "provenance-embed-"
+ "shouldCopyProvenanceData"
+ "smartAlbumProvenance"
+ "v24@?0q8@\"NSError\"16"
+ "void PHAssetExportRequestPerformMediaConversion(PHMediaFormatConversionSource *__strong, BOOL, BOOL, UTType * _Nullable __strong, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, NSDate * _Nullable __strong, NSTimeZone * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSURL *__strong, NSURL *__strong, NSURL *__strong, NSURL *__strong, BOOL, NSString * _Nullable __strong, NSProgress *__strong, int64_t, NSURL *__strong, BOOL, NSString *__strong, NSString * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
+ "\xf0A"
- "<%@: %p, variant: \"%@\", livePhotoAsStill: %d, allowRaw: %d, flattenSlomo: %d, stripLocation: %d, stripCaption: %d, stripAXDescription: %d, stripKeywords: %d, assetBundle: %d, disableMetadataCorrections: %d, unmodifiedOriginals: %d>"
- "PHQueryForAssetCollectionType_Album_block_invoke_108"
- "PHQueryForAssetCollectionType_CollectionShare_block_invoke_120"
- "PHQueryForAssetCollectionType_Conversation_block_invoke_117"
- "PHQueryForAssetCollectionType_ImportSession_block_invoke_116"
- "PHQueryForAssetCollectionType_Memory_block_invoke_112"
- "PHQueryForAssetCollectionType_MomentShare_block_invoke_114"
- "PHQueryForAssetCollectionType_Moment_block_invoke_109"
- "PHQueryForAssetCollectionType_NoFetchType_block_invoke_122"
- "PHQueryForAssetCollectionType_Other_block_invoke_121"
- "PHQueryForAssetCollectionType_PhotosHighlight_block_invoke_113"
- "PHQueryForAssetCollectionType_Project_block_invoke_118"
- "PHQueryForAssetCollectionType_SmartAlbum_block_invoke_110"
- "PHQueryForAssetCollectionType_Suggestion_block_invoke_115"
- "PHQueryForAssetCollectionType_Unknown_block_invoke_111"
- "PHQueryForAssetCollectionType_Utility_block_invoke_119"
- "PHQueryForAssetInAlbumKind_ActionCamVideoAlbum_block_invoke_98"
- "PHQueryForAssetInAlbumKind_ProResAlbum_block_invoke_97"
- "PHQueryForAssetInAlbumKind_SharedLibrarySharingSuggestionsAlbum_block_invoke_96"
- "PHQueryForAssetsAlbum_SortKeyOther_block_invoke_99"
- "PHQueryForAssetsInAlbum_SortKeyContentTitle_block_invoke_107"
- "PHQueryForAssetsInAlbum_SortKeyCreationDate_block_invoke_101"
- "PHQueryForAssetsInAlbum_SortKeyImportDate_block_invoke_103"
- "PHQueryForAssetsInAlbum_SortKeyLastModifiedDate_block_invoke_102"
- "PHQueryForAssetsInAlbum_SortKeyManual_block_invoke_100"
- "PHQueryForAssetsInAlbum_SortKeyPublishDate_block_invoke_106"
- "PHQueryForAssetsInAlbum_SortKeyTitle_block_invoke_105"
- "PHQueryForAssetsInAlbum_SortKeyTrashDate_block_invoke_104"
- "PHQueryForAssetsInUtility_GenericDocument_block_invoke_132"
- "PHQueryForAssetsInUtility_Handwriting_block_invoke_135"
- "PHQueryForAssetsInUtility_IdentityDocuments_block_invoke_138"
- "PHQueryForAssetsInUtility_Illustrations_block_invoke_134"
- "PHQueryForAssetsInUtility_Maps_block_invoke_137"
- "PHQueryForAssetsInUtility_Other_block_invoke_139"
- "PHQueryForAssetsInUtility_QRCodes_block_invoke_136"
- "PHQueryForAssetsInUtility_Receipts_block_invoke_133"
- "PHQueryForTransientAssetCollectionType_Generic_block_invoke_123"
- "PHQueryForTransientAssetCollectionType_ImportHistory_block_invoke_124"
- "PHQueryForTransientAssetCollectionType_Other_block_invoke_131"
- "PHQueryForTransientAssetCollectionType_RecentlyEdited_block_invoke_125"
- "PHQueryForTransientAssetCollectionType_RecentlyShared_block_invoke_126"
- "PHQueryForTransientAssetCollectionType_RecentlyViewed_block_invoke_127"
- "PHQueryForTransientAssetCollectionType_SavedToday_block_invoke_130"
- "PHQueryForTransientAssetCollectionType_SearchCollectionResults_block_invoke_129"
- "PHQueryForTransientAssetCollectionType_SearchTopResults_block_invoke_128"
- "[PHAssetExportRequest] Export request processing required for asset %{public}@: %{BOOL}d (metadataOperationLocation=%{public}@, metadataOperationCaption=%{public}@, metadataOperationCaptionAccessibilityDescription=%{public}@, metadataOperationKeywords=%{public}@, metadataChangeCustomDate=%{private}@, livePhotoMetadataFixup=%{BOOL}d producingNewFilesForExport=%{BOOL}d, options.variant=%{public}@, requiresSloMoFlattening=%{BOOL}d, videoExportPreset=%{public}@, type = %{public}@, needsReplacementLivePhotoIdentifier = %{BOOL}d %{public}@"
- "[PHResourceLocalAvailabilityRequest] Using original/primary resource(s): %{BOOL}d for asset %{public}@ because it is edited: %{BOOL}d, known unsupported: %{BOOL}d, isRAW: %{BOOL}d, dontAllowRAW: %{BOOL}d, should use unmodified original: %{BOOL}d"
- "void PHAssetExportRequestPerformMediaConversion(PHMediaFormatConversionSource *__strong, BOOL, BOOL, UTType * _Nullable __strong, PHAssetExportRequestMetadataOperation, CLLocation * _Nullable __strong, NSDate * _Nullable __strong, NSTimeZone * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSString * _Nullable __strong, PHAssetExportRequestMetadataOperation, NSArray<NSString *> * _Nullable __strong, NSString * _Nullable __strong, NSProgress *__strong, int64_t, NSURL *__strong, BOOL, NSString *__strong, NSString * _Nullable __strong, void (^__strong)(NSURL * _Nullable __strong, NSError * _Nullable __strong))"
- "\xf01"
```

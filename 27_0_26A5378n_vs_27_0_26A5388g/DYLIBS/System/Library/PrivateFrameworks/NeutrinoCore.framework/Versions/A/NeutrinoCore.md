## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-910.28.103.0.0
-  __TEXT.__text: 0x33b0bc
-  __TEXT.__objc_methlist: 0x201f4
-  __TEXT.__const: 0x26f8
-  __TEXT.__constg_swiftt: 0x158
-  __TEXT.__swift5_typeref: 0x395
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x8a
-  __TEXT.__swift5_fieldmd: 0x15c
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x3f0b8
+910.34.101.0.0
+  __TEXT.__text: 0x33c79c
+  __TEXT.__objc_methlist: 0x20234
+  __TEXT.__const: 0x2918
+  __TEXT.__swift5_typeref: 0x3e7
+  __TEXT.__swift5_reflstr: 0x93
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__constg_swiftt: 0x178
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_fieldmd: 0x178
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__cstring: 0x3f21d
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x7edc
-  __TEXT.__oslogstring: 0x5400
+  __TEXT.__gcc_except_tab: 0x7fb0
+  __TEXT.__oslogstring: 0x550b
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x8610
+  __TEXT.__unwind_info: 0x8670
   __TEXT.__eh_frame: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15b0
+  __DATA_CONST.__const: 0x15f0
   __DATA_CONST.__objc_classlist: 0x15b0
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb2b0
+  __DATA_CONST.__objc_selrefs: 0xb2e0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xfe0
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x2210
-  __AUTH_CONST.__const: 0x80a0
-  __AUTH_CONST.__cfstring: 0x1c8a0
-  __AUTH_CONST.__objc_const: 0x35f28
+  __DATA_CONST.__got: 0x2218
+  __AUTH_CONST.__const: 0x80a8
+  __AUTH_CONST.__cfstring: 0x1c8e0
+  __AUTH_CONST.__objc_const: 0x35f78
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8b8
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xfc0
-  __DATA.__objc_ivar: 0x1960
-  __DATA.__data: 0x3838
+  __AUTH_CONST.__auth_got: 0xfc8
+  __DATA.__objc_ivar: 0x1968
+  __DATA.__data: 0x3898
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xe70
+  __DATA.__bss: 0x1270
   __DATA_DIRTY.__objc_data: 0xd8e0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11726
-  Symbols:   25156
-  CStrings:  7152
+  Functions: 11748
+  Symbols:   25190
+  CStrings:  7160
 
Symbols:
+ +[NUPipelineFactory _buildRenderNodePipelineForClass:baseSettings:error:]
+ +[NUPixelFormat pixelFormatForColorSpace:]
+ +[NUVideoUtilities insufficientlyCoveredMainFrameCountForAuxTrack:mainVideoTrack:halfWindow:minSamplesPerWindow:totalMainFrames:]
+ -[NUGlobalSettings enableConcurrentAudioExport]
+ -[NUGlobalSettings enableResumableVideoExport]
+ -[NUGlobalSettings semanticStyleForceSyntheticNoise]
+ -[NUGlobalSettings setEnableConcurrentAudioExport:]
+ -[NUGlobalSettings setEnableResumableVideoExport:]
+ -[NUGlobalSettings setSemanticStyleForceSyntheticNoise:]
+ -[NUPipelineProcessor prepareForConfiguration:controlData:error:]
+ -[NUPipelineProcessor resumeWithConfiguration:serializedState:controlData:error:]
+ -[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]
+ -[NUVideoCorruptionInfo insufficientlyCoveredFrameCount]
+ -[NUVideoCorruptionInfo setInsufficientlyCoveredFrameCount:]
+ -[NUVideoCorruptionInfo setTotalMainFrameCount:]
+ -[NUVideoCorruptionInfo totalMainFrameCount]
+ -[_NUMediaGeometry nu_updateDigest:]
+ GCC_except_table10176
+ GCC_except_table10183
+ GCC_except_table10184
+ GCC_except_table10186
+ GCC_except_table10187
+ GCC_except_table10285
+ GCC_except_table10288
+ GCC_except_table10291
+ GCC_except_table10295
+ GCC_except_table10298
+ GCC_except_table10299
+ GCC_except_table10301
+ GCC_except_table10302
+ GCC_except_table10303
+ GCC_except_table10305
+ GCC_except_table10306
+ GCC_except_table10317
+ GCC_except_table10322
+ GCC_except_table10329
+ GCC_except_table10330
+ GCC_except_table10332
+ GCC_except_table10333
+ GCC_except_table10336
+ GCC_except_table10337
+ GCC_except_table10340
+ GCC_except_table10343
+ GCC_except_table10344
+ GCC_except_table10347
+ GCC_except_table10362
+ GCC_except_table10363
+ GCC_except_table10364
+ GCC_except_table10381
+ GCC_except_table10382
+ GCC_except_table10383
+ GCC_except_table10393
+ GCC_except_table10394
+ GCC_except_table10395
+ GCC_except_table10396
+ GCC_except_table10397
+ GCC_except_table10398
+ GCC_except_table10456
+ GCC_except_table10507
+ GCC_except_table10596
+ GCC_except_table10600
+ GCC_except_table1097
+ GCC_except_table11044
+ GCC_except_table11205
+ GCC_except_table11207
+ GCC_except_table11253
+ GCC_except_table11307
+ GCC_except_table11315
+ GCC_except_table11322
+ GCC_except_table11323
+ GCC_except_table11327
+ GCC_except_table1277
+ GCC_except_table1281
+ GCC_except_table1289
+ GCC_except_table1290
+ GCC_except_table1291
+ GCC_except_table1295
+ GCC_except_table1319
+ GCC_except_table1328
+ GCC_except_table1353
+ GCC_except_table1357
+ GCC_except_table1359
+ GCC_except_table1361
+ GCC_except_table1371
+ GCC_except_table1419
+ GCC_except_table1421
+ GCC_except_table1629
+ GCC_except_table1642
+ GCC_except_table1654
+ GCC_except_table1677
+ GCC_except_table1689
+ GCC_except_table1694
+ GCC_except_table1783
+ GCC_except_table1786
+ GCC_except_table1795
+ GCC_except_table1817
+ GCC_except_table1904
+ GCC_except_table2029
+ GCC_except_table2035
+ GCC_except_table2060
+ GCC_except_table2712
+ GCC_except_table5689
+ GCC_except_table5714
+ GCC_except_table5750
+ GCC_except_table5752
+ GCC_except_table5754
+ GCC_except_table5759
+ GCC_except_table5769
+ GCC_except_table5773
+ GCC_except_table5809
+ GCC_except_table5828
+ GCC_except_table5849
+ GCC_except_table5854
+ GCC_except_table5873
+ GCC_except_table5876
+ GCC_except_table5882
+ GCC_except_table5885
+ GCC_except_table5894
+ GCC_except_table5899
+ GCC_except_table5901
+ GCC_except_table5908
+ GCC_except_table5922
+ GCC_except_table5928
+ GCC_except_table5935
+ GCC_except_table5942
+ GCC_except_table5948
+ GCC_except_table5956
+ GCC_except_table5959
+ GCC_except_table5970
+ GCC_except_table5972
+ GCC_except_table5974
+ GCC_except_table5981
+ GCC_except_table5983
+ GCC_except_table5986
+ GCC_except_table5989
+ GCC_except_table6097
+ GCC_except_table6101
+ GCC_except_table6161
+ GCC_except_table6194
+ GCC_except_table6231
+ GCC_except_table6238
+ GCC_except_table6259
+ GCC_except_table6339
+ GCC_except_table6351
+ GCC_except_table6356
+ GCC_except_table6363
+ GCC_except_table6380
+ GCC_except_table6401
+ GCC_except_table6402
+ GCC_except_table6406
+ GCC_except_table6407
+ GCC_except_table6510
+ GCC_except_table6519
+ GCC_except_table6539
+ GCC_except_table6556
+ GCC_except_table6630
+ GCC_except_table6700
+ GCC_except_table6703
+ GCC_except_table6726
+ GCC_except_table6770
+ GCC_except_table6913
+ GCC_except_table6988
+ GCC_except_table7003
+ GCC_except_table7004
+ GCC_except_table7005
+ GCC_except_table7018
+ GCC_except_table7019
+ GCC_except_table7020
+ GCC_except_table7021
+ GCC_except_table7036
+ GCC_except_table7037
+ GCC_except_table7051
+ GCC_except_table7052
+ GCC_except_table7056
+ GCC_except_table7096
+ GCC_except_table7169
+ GCC_except_table7170
+ GCC_except_table7180
+ GCC_except_table7182
+ GCC_except_table7184
+ GCC_except_table7198
+ GCC_except_table7199
+ GCC_except_table7201
+ GCC_except_table7202
+ GCC_except_table7204
+ GCC_except_table7205
+ GCC_except_table7275
+ GCC_except_table7312
+ GCC_except_table7351
+ GCC_except_table7352
+ GCC_except_table7402
+ GCC_except_table8093
+ GCC_except_table8096
+ GCC_except_table8163
+ GCC_except_table8302
+ GCC_except_table8311
+ GCC_except_table8314
+ GCC_except_table8316
+ GCC_except_table8321
+ GCC_except_table8337
+ GCC_except_table8338
+ GCC_except_table8343
+ GCC_except_table8344
+ GCC_except_table8371
+ GCC_except_table8372
+ GCC_except_table8373
+ GCC_except_table8374
+ GCC_except_table8387
+ GCC_except_table8566
+ GCC_except_table8613
+ GCC_except_table8956
+ GCC_except_table9041
+ GCC_except_table9219
+ GCC_except_table9412
+ GCC_except_table9427
+ GCC_except_table9464
+ GCC_except_table9471
+ GCC_except_table9511
+ GCC_except_table9512
+ GCC_except_table9513
+ GCC_except_table9514
+ GCC_except_table9519
+ GCC_except_table9525
+ GCC_except_table9526
+ GCC_except_table9533
+ GCC_except_table9543
+ GCC_except_table9545
+ GCC_except_table9546
+ GCC_except_table9548
+ GCC_except_table9558
+ GCC_except_table9560
+ GCC_except_table9566
+ GCC_except_table9568
+ GCC_except_table9570
+ GCC_except_table9572
+ GCC_except_table9580
+ GCC_except_table9605
+ GCC_except_table9606
+ GCC_except_table9607
+ GCC_except_table9608
+ GCC_except_table9609
+ GCC_except_table9610
+ GCC_except_table9611
+ GCC_except_table9612
+ GCC_except_table9613
+ GCC_except_table9670
+ GCC_except_table9677
+ GCC_except_table9755
+ GCC_except_table9803
+ GCC_except_table9827
+ GCC_except_table9828
+ GCC_except_table9832
+ GCC_except_table9835
+ GCC_except_table9842
+ GCC_except_table9852
+ GCC_except_table9862
+ GCC_except_table9872
+ GCC_except_table9874
+ GCC_except_table9877
+ GCC_except_table9878
+ GCC_except_table9879
+ GCC_except_table9951
+ GCC_except_table9961
+ OBJC_IVAR_$_NUVideoCorruptionInfo._insufficientlyCoveredFrameCount
+ OBJC_IVAR_$_NUVideoCorruptionInfo._totalMainFrameCount
+ _NUMediaCharacteristicForSemanticStyleTrackCorruptionInfo
+ _NUQuicktimeMetadataKey_SmartStyleEditInfos
+ _NUSemanticStyleTrackCorruptionInfoFromAsset
+ ___17-[NUFactory stop]_block_invoke
+ ___40+[NUVideoUtilities validateAsset:error:]_block_invoke_2
+ ___46-[NUGlobalSettings enableResumableVideoExport]_block_invoke
+ ___47-[NUGlobalSettings enableConcurrentAudioExport]_block_invoke
+ ___52-[NUGlobalSettings semanticStyleForceSyntheticNoise]_block_invoke
+ ___83-[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]_block_invoke
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ _associated conformance So26NURawDecodeCachingStrategyaSHSCSQ
+ _associated conformance So26NURawDecodeCachingStrategyas12CaseIterable12NeutrinoCore8AllCasessACP_Sl
+ _associated conformance So26NURawDecodeCachingStrategyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So26NURawDecodeCachingStrategyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_buildRenderNodePipelineForClass:baseSettings:error:
+ _objc_msgSend$booleanWithDefault:
+ _objc_msgSend$debugDescriptionOfAssetTrack:
+ _objc_msgSend$insufficientlyCoveredFrameCount
+ _objc_msgSend$insufficientlyCoveredMainFrameCountForAuxTrack:mainVideoTrack:halfWindow:minSamplesPerWindow:totalMainFrames:
+ _objc_msgSend$prepareForConfiguration:controlData:error:
+ _objc_msgSend$presentationTimeStamp
+ _objc_msgSend$processorForConfiguration:identifier:controlData:error:
+ _objc_msgSend$resumeWithConfiguration:serializedState:controlData:error:
+ _objc_msgSend$semanticStyleInterpolationHalfWindowTime
+ _objc_msgSend$setInsufficientlyCoveredFrameCount:
+ _objc_msgSend$setTotalMainFrameCount:
+ _objc_msgSend$stepInPresentationOrderByCount:
+ _objc_msgSend$totalMainFrameCount
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic $ss12CaseIterableP
+ _symbolic Say_____G So26NURawDecodeCachingStrategya
+ _symbolic _____ So26NURawDecodeCachingStrategya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So26NURawDecodeCachingStrategya
- +[NUGlobalSettings enableConcurrentAudioExport]
- +[NUGlobalSettings enableResumableVideoExport]
- +[NUGlobalSettings renderMeteorPlusAsHDR]
- +[NUGlobalSettings semanticStyleForceSyntheticNoise]
- +[NUGlobalSettings setEnableConcurrentAudioExport:]
- +[NUGlobalSettings setEnableResumableVideoExport:]
- +[NUGlobalSettings setRenderMeteorPlusAsHDR:]
- +[NUGlobalSettings setSemanticStyleForceSyntheticNoise:]
- -[NUPipelineProcessor prepareForConfiguration:serializedState:error:]
- -[NUPipelineProcessorCache processorForConfiguration:identifier:error:]
- GCC_except_table10167
- GCC_except_table10168
- GCC_except_table10174
- GCC_except_table10175
- GCC_except_table10178
- GCC_except_table10275
- GCC_except_table10276
- GCC_except_table10279
- GCC_except_table10280
- GCC_except_table10281
- GCC_except_table10282
- GCC_except_table10283
- GCC_except_table10286
- GCC_except_table10294
- GCC_except_table10296
- GCC_except_table10297
- GCC_except_table10307
- GCC_except_table10308
- GCC_except_table10313
- GCC_except_table10314
- GCC_except_table10315
- GCC_except_table10318
- GCC_except_table10319
- GCC_except_table10320
- GCC_except_table10321
- GCC_except_table10326
- GCC_except_table10331
- GCC_except_table10338
- GCC_except_table10341
- GCC_except_table10342
- GCC_except_table10352
- GCC_except_table10353
- GCC_except_table10354
- GCC_except_table10355
- GCC_except_table10357
- GCC_except_table10367
- GCC_except_table10372
- GCC_except_table10373
- GCC_except_table10374
- GCC_except_table10389
- GCC_except_table10447
- GCC_except_table10498
- GCC_except_table10587
- GCC_except_table10591
- GCC_except_table1100
- GCC_except_table11035
- GCC_except_table11196
- GCC_except_table11198
- GCC_except_table11244
- GCC_except_table11298
- GCC_except_table11306
- GCC_except_table11313
- GCC_except_table11314
- GCC_except_table11318
- GCC_except_table1280
- GCC_except_table1284
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1297
- GCC_except_table1301
- GCC_except_table1322
- GCC_except_table1331
- GCC_except_table1356
- GCC_except_table1362
- GCC_except_table1363
- GCC_except_table1364
- GCC_except_table1374
- GCC_except_table1422
- GCC_except_table1424
- GCC_except_table1631
- GCC_except_table1644
- GCC_except_table1656
- GCC_except_table1679
- GCC_except_table1691
- GCC_except_table1696
- GCC_except_table1785
- GCC_except_table1788
- GCC_except_table1797
- GCC_except_table1819
- GCC_except_table1906
- GCC_except_table2034
- GCC_except_table2036
- GCC_except_table2061
- GCC_except_table2711
- GCC_except_table5688
- GCC_except_table5713
- GCC_except_table5749
- GCC_except_table5751
- GCC_except_table5753
- GCC_except_table5758
- GCC_except_table5767
- GCC_except_table5772
- GCC_except_table5808
- GCC_except_table5827
- GCC_except_table5848
- GCC_except_table5853
- GCC_except_table5872
- GCC_except_table5874
- GCC_except_table5880
- GCC_except_table5883
- GCC_except_table5893
- GCC_except_table5896
- GCC_except_table5900
- GCC_except_table5903
- GCC_except_table5909
- GCC_except_table5926
- GCC_except_table5933
- GCC_except_table5939
- GCC_except_table5943
- GCC_except_table5952
- GCC_except_table5957
- GCC_except_table5962
- GCC_except_table5971
- GCC_except_table5973
- GCC_except_table5976
- GCC_except_table5982
- GCC_except_table5984
- GCC_except_table5987
- GCC_except_table6096
- GCC_except_table6100
- GCC_except_table6160
- GCC_except_table6192
- GCC_except_table6230
- GCC_except_table6237
- GCC_except_table6258
- GCC_except_table6334
- GCC_except_table6343
- GCC_except_table6348
- GCC_except_table6355
- GCC_except_table6372
- GCC_except_table6390
- GCC_except_table6393
- GCC_except_table6394
- GCC_except_table6399
- GCC_except_table6502
- GCC_except_table6511
- GCC_except_table6531
- GCC_except_table6548
- GCC_except_table6622
- GCC_except_table6687
- GCC_except_table6692
- GCC_except_table6718
- GCC_except_table6762
- GCC_except_table6905
- GCC_except_table6980
- GCC_except_table6995
- GCC_except_table6996
- GCC_except_table6997
- GCC_except_table7010
- GCC_except_table7011
- GCC_except_table7012
- GCC_except_table7013
- GCC_except_table7028
- GCC_except_table7029
- GCC_except_table7043
- GCC_except_table7044
- GCC_except_table7048
- GCC_except_table7088
- GCC_except_table7161
- GCC_except_table7162
- GCC_except_table7166
- GCC_except_table7168
- GCC_except_table7172
- GCC_except_table7177
- GCC_except_table7181
- GCC_except_table7186
- GCC_except_table7190
- GCC_except_table7191
- GCC_except_table7196
- GCC_except_table7267
- GCC_except_table7304
- GCC_except_table7394
- GCC_except_table8085
- GCC_except_table8088
- GCC_except_table8155
- GCC_except_table8294
- GCC_except_table8298
- GCC_except_table8303
- GCC_except_table8308
- GCC_except_table8313
- GCC_except_table8327
- GCC_except_table8329
- GCC_except_table8330
- GCC_except_table8336
- GCC_except_table8356
- GCC_except_table8363
- GCC_except_table8365
- GCC_except_table8366
- GCC_except_table8379
- GCC_except_table8558
- GCC_except_table8605
- GCC_except_table8947
- GCC_except_table9032
- GCC_except_table9210
- GCC_except_table9403
- GCC_except_table9418
- GCC_except_table9455
- GCC_except_table9462
- GCC_except_table9502
- GCC_except_table9503
- GCC_except_table9504
- GCC_except_table9505
- GCC_except_table9510
- GCC_except_table9516
- GCC_except_table9517
- GCC_except_table9524
- GCC_except_table9527
- GCC_except_table9534
- GCC_except_table9537
- GCC_except_table9539
- GCC_except_table9540
- GCC_except_table9541
- GCC_except_table9542
- GCC_except_table9547
- GCC_except_table9552
- GCC_except_table9557
- GCC_except_table9563
- GCC_except_table9571
- GCC_except_table9578
- GCC_except_table9579
- GCC_except_table9581
- GCC_except_table9582
- GCC_except_table9584
- GCC_except_table9585
- GCC_except_table9589
- GCC_except_table9595
- GCC_except_table9661
- GCC_except_table9668
- GCC_except_table9746
- GCC_except_table9794
- GCC_except_table9818
- GCC_except_table9819
- GCC_except_table9823
- GCC_except_table9824
- GCC_except_table9825
- GCC_except_table9826
- GCC_except_table9853
- GCC_except_table9859
- GCC_except_table9860
- GCC_except_table9861
- GCC_except_table9863
- GCC_except_table9865
- GCC_except_table9942
- GCC_except_table9952
- __40+[NUVideoUtilities validateAsset:error:]_block_invoke
- ___41+[NUGlobalSettings renderMeteorPlusAsHDR]_block_invoke
- ___46+[NUGlobalSettings enableResumableVideoExport]_block_invoke
- ___47+[NUGlobalSettings enableConcurrentAudioExport]_block_invoke
- ___52+[NUGlobalSettings semanticStyleForceSyntheticNoise]_block_invoke
- ___71-[NUPipelineProcessorCache processorForConfiguration:identifier:error:]_block_invoke
- _objc_msgSend$prepareForConfiguration:error:
- _objc_msgSend$processorForConfiguration:identifier:error:
- _objc_msgSend$renderMeteorPlusAsHDR
- _objc_msgSend$resumeWithConfiguration:serializedState:error:
CStrings:
+ "+[NUPipelineFactory _buildRenderNodePipelineForClass:baseSettings:error:]"
+ "+[NUVideoUtilities insufficientlyCoveredMainFrameCountForAuxTrack:mainVideoTrack:halfWindow:minSamplesPerWindow:totalMainFrames:]"
+ "-[NUPipelineProcessor prepareForConfiguration:controlData:error:]"
+ "-[NUPipelineProcessor resumeWithConfiguration:serializedState:controlData:error:]"
+ "-[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAdjustment.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAdjustmentSerialization.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUComposition.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Crop/NUCropModel.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Crop/NUCropModelAlgo.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Crop/NUQuad2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometry.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometryPrimitives.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometrySpaceMap.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NUImageGeometry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NURect.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/NUVideoAttributes.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUCompoundTransform.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUGeometryTransform.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUSpace.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Histogram/NUHistogram.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Histogram/NUHistogramCalculator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Histogram/NUImageHistogram.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUAuxiliaryImage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUBufferStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUCVPixelBuffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUIOSurface.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUIOSurfaceStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUImageFactory.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUImageLayout.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUImageStorage.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUImageTile.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUImageUtilities.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUPixelBuffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUPixelFormat.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUPurgeableStoragePool.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Image/NUStorageImageBuffer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/LivePhoto/NULivePhotoRenderRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Mask/NUBrushStroke.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Mask/NUBrushStrokeMaskIntersector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Mask/NUMaskSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Mask/NUMaskUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Math/NURational.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Metal/NUComputeKernel.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Performance/NUPerformance.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Performance/NUProcessorCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUAsset.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUAudioMixEffect.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUChannel.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUChannelExpression.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUComputeRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUControlDescriptor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMedia.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaAVBuilder.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaMetadata.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaSample.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaTransform.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineFactory.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelinePrimitives.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineProcessor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineProcessorCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NURawAssetPipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NURawProfilePipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUStyleTransferPipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUAuxiliaryImageCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUAuxiliaryRenderNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUCacheNodeRegistry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUComputePipelineProcessorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUExpressionComputeNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUHDRGainMapNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUImageAccumulationNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUMediaTransformNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUPipelineIntermediateNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUPipelineProcessorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Audio.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Clamp.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Crop.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Filter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+KeyFrame.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Orientation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Pipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Placeholder.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Time.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Transform.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipeline.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineFilter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineHelper.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineProcessorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineRegistry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineState.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CGAuxiliaryImage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CGImage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CIImage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+RAW.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Scale.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Test.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Video.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderTagGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderTagNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUStyleTransferNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUSwitchNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Pipeline/SlowMotion/NUSlowMotionUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Region/NURegion.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUAuxiliaryImageRenderRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUBufferRenderRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUClassifyPipelineImageCorrectionRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUExportJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUFaceDetectionRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUHistogramRenderJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImageDataRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImageExportFormat.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImageExportJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImageProperties.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImagePropertiesRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUImageRenderJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUJobPriorityQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUJobQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUPriority.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURedEyeDetectionRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURegionPolicy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderResourcePool.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderResultCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderTransaction.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NURunQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUScale.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUScalePolicy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUScheduledQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUScheduler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoAttributesRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoCompositionInstruction.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoCompositor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoExportJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoExporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPlaybackCompositor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPlaybackFrameRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoProperties.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPropertiesRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoRenderRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionDetectionRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionForegroundIsolationSegmentationRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionInstanceSegmentationRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionSegmentationRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Runtime/NUDevice.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Runtime/NUDisplay_Mac.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Runtime/NUGlobalSettings.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Runtime/NUPlatform.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Runtime/NUPlatform_Mac.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Sampler/NUColorSampler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Sampler/NUTagColorSampler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUModel.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUPattern.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUSchema.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUSchemaRegistry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUSetting.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUSoftwareVersion.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Schema/NUVersion.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Statistics/NUDataSet.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/CoreImageDataAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUCoalescer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUColorSpace.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUDigest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUError.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUFactory.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUObjectPointerArray.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUObservatory.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUOrderedDictionary.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUResponse.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ofBFcT/Sources/Photos/workspaces/neutrino/Core/Util/NUVideoUtilities.m"
+ "AVAssetWritingPlanner returned no segment recommendations"
+ "AVAssetWritingPlanner returned no segment recommendations: track=%{public}@, trackDuration=%{public}@, naturalTimeScale=%d, minFrameDuration=%{public}@, nominalFrameRate=%.3f, minimumSegmentDuration=%{public}@, minimumSegmentFrameCount=%ld"
+ "CMTIME_IS_NUMERIC(halfWindow)"
+ "Failed to get style learn time, using video frame time %@: %{public}@"
+ "InsufficientAuxiliaryTrackSamples (%@, %lu/%lu frames insufficiently covered = %.1f%%)"
+ "_NUMediaGeometry<"
+ "auxTrack != nil"
+ "com.apple.quicktime.smartstyle.edit.infos"
+ "mainVideoTrack != nil"
+ "minSamplesPerWindow > 0"
- "+[NUPipelineFactory _buildRenderNodePipelineForClass:error:]"
- "-[NUPipelineProcessor prepareForConfiguration:serializedState:error:]"
- "-[NUPipelineProcessorCache processorForConfiguration:identifier:error:]"
- "-[NUVideoExporter exportSegmentsWithPlanner:error:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAdjustment.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAdjustmentSerialization.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUComposition.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Adjustments/NUSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Crop/NUCropModel.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Crop/NUCropModelAlgo.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Crop/NUQuad2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometry.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometryPrimitives.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NUGeometrySpaceMap.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NUImageGeometry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NURect.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/NUVideoAttributes.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUCompoundTransform.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUGeometryTransform.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Geometry/transforms/NUSpace.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Histogram/NUHistogram.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Histogram/NUHistogramCalculator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Histogram/NUImageHistogram.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUAuxiliaryImage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUBufferStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUCVPixelBuffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUIOSurface.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUIOSurfaceStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUImageFactory.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUImageLayout.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUImageStorage.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUImageTile.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUImageUtilities.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUPixelBuffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUPixelFormat.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUPurgeableStoragePool.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Image/NUStorageImageBuffer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/LivePhoto/NULivePhotoRenderRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Mask/NUBrushStroke.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Mask/NUBrushStrokeMaskIntersector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Mask/NUMaskSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Mask/NUMaskUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Math/NURational.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Metal/NUComputeKernel.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Performance/NUPerformance.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Performance/NUProcessorCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUAsset.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUAudioMixEffect.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUChannel.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUChannelExpression.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUComputeRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUControlDescriptor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMedia.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaAVBuilder.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaCacheNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaMetadata.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaSample.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUMediaTransform.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineFactory.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelinePrimitives.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineProcessor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUPipelineProcessorCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NURawAssetPipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NURawProfilePipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/API/NUStyleTransferPipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUAuxiliaryImageCacheNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUAuxiliaryRenderNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUCacheNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUCacheNodeRegistry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUComputePipelineProcessorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUExpressionComputeNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUHDRGainMapNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUImageAccumulationNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUMediaTransformNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUPipelineIntermediateNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUPipelineProcessorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Audio.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Clamp.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Crop.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Filter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+KeyFrame.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Orientation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Pipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Placeholder.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Time.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode+Transform.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipeline.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineFilter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineHelper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineProcessorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineRegistry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderPipelineState.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CGAuxiliaryImage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CGImage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+CIImage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+RAW.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Scale.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Test.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode+Video.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderSourceNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderTagGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NURenderTagNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUStyleTransferNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/NUSwitchNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Pipeline/SlowMotion/NUSlowMotionUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Region/NURegion.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUAuxiliaryImageRenderRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUBufferRenderRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUClassifyPipelineImageCorrectionRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUExportJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUFaceDetectionRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUHistogramRenderJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImageDataRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImageExportFormat.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImageExportJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImageProperties.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImagePropertiesRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUImageRenderJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUJobPriorityQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUJobQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUPriority.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURedEyeDetectionRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURegionPolicy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderResourcePool.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderResultCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderTransaction.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NURunQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUScale.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUScalePolicy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUScheduledQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUScheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoAttributesRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoCompositionInstruction.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoCompositor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoExportJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoExporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPlaybackCompositor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPlaybackFrameRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoProperties.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoPropertiesRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVideoRenderRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionDetectionRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionForegroundIsolationSegmentationRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionInstanceSegmentationRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Render/NUVisionSegmentationRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Runtime/NUDevice.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Runtime/NUDisplay_Mac.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Runtime/NUGlobalSettings.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Runtime/NUPlatform.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Runtime/NUPlatform_Mac.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Sampler/NUColorSampler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Sampler/NUTagColorSampler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUIdentifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUModel.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUPattern.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUSchema.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUSchemaRegistry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUSetting.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUSoftwareVersion.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Schema/NUVersion.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Statistics/NUDataSet.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/CoreImageDataAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUCoalescer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUColorSpace.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUDigest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUError.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUFactory.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUObjectPointerArray.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUObservatory.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUOrderedDictionary.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUResponse.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/neutrino/Core/Util/NUVideoUtilities.m"
- "AVAssetWritingPlanner returned no segment recommendations (regression of rdar://170564263?)"
- "Failed to get style learn time: %{public}@"
- "NU_RENDER_METEOR_PLUS_AS_HDR"
```

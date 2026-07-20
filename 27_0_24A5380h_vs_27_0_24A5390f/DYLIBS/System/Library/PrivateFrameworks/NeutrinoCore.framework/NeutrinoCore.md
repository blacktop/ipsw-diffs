## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

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
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-910.27.103.0.0
-  __TEXT.__text: 0x30bb98
-  __TEXT.__objc_methlist: 0x201fc
-  __TEXT.__const: 0x2708
-  __TEXT.__constg_swiftt: 0x158
-  __TEXT.__swift5_typeref: 0x395
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x8a
-  __TEXT.__swift5_fieldmd: 0x15c
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x3d68a
+910.33.102.0.0
+  __TEXT.__text: 0x30d0e8
+  __TEXT.__objc_methlist: 0x2023c
+  __TEXT.__const: 0x2918
+  __TEXT.__swift5_typeref: 0x3e7
+  __TEXT.__swift5_reflstr: 0x93
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__constg_swiftt: 0x178
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_fieldmd: 0x178
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__cstring: 0x3d7ef
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x7e84
-  __TEXT.__oslogstring: 0x537e
+  __TEXT.__gcc_except_tab: 0x7f54
+  __TEXT.__oslogstring: 0x5489
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x8400
+  __TEXT.__unwind_info: 0x8460
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f10
+  __DATA_CONST.__const: 0x3f50
   __DATA_CONST.__objc_classlist: 0x15b0
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb290
+  __DATA_CONST.__objc_selrefs: 0xb2c0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xfe0
   __DATA_CONST.__objc_arraydata: 0xae0
-  __DATA_CONST.__got: 0x21f0
-  __AUTH_CONST.__const: 0x4e78
-  __AUTH_CONST.__cfstring: 0x1c880
-  __AUTH_CONST.__objc_const: 0x35f28
+  __DATA_CONST.__got: 0x21f8
+  __AUTH_CONST.__const: 0x4e80
+  __AUTH_CONST.__cfstring: 0x1c8c0
+  __AUTH_CONST.__objc_const: 0x35f78
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x10b8
-  __DATA.__objc_ivar: 0x1964
-  __DATA.__data: 0x3838
+  __AUTH_CONST.__auth_got: 0x10c0
+  __DATA.__objc_ivar: 0x196c
+  __DATA.__data: 0x3898
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xe80
+  __DATA.__bss: 0x1280
   __DATA_DIRTY.__objc_data: 0xd8e0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11639
-  Symbols:   25055
-  CStrings:  7148
+  Functions: 11663
+  Symbols:   25091
+  CStrings:  7156
 
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
+ GCC_except_table10131
+ GCC_except_table10138
+ GCC_except_table10139
+ GCC_except_table10141
+ GCC_except_table10142
+ GCC_except_table10240
+ GCC_except_table10243
+ GCC_except_table10246
+ GCC_except_table10250
+ GCC_except_table10253
+ GCC_except_table10254
+ GCC_except_table10256
+ GCC_except_table10257
+ GCC_except_table10258
+ GCC_except_table10260
+ GCC_except_table10261
+ GCC_except_table10272
+ GCC_except_table10277
+ GCC_except_table10285
+ GCC_except_table10289
+ GCC_except_table10290
+ GCC_except_table10296
+ GCC_except_table10297
+ GCC_except_table10311
+ GCC_except_table10312
+ GCC_except_table10313
+ GCC_except_table10330
+ GCC_except_table10331
+ GCC_except_table10332
+ GCC_except_table10342
+ GCC_except_table10343
+ GCC_except_table10344
+ GCC_except_table10345
+ GCC_except_table10346
+ GCC_except_table10347
+ GCC_except_table10393
+ GCC_except_table10444
+ GCC_except_table10521
+ GCC_except_table10525
+ GCC_except_table1065
+ GCC_except_table10967
+ GCC_except_table11128
+ GCC_except_table11130
+ GCC_except_table11176
+ GCC_except_table11228
+ GCC_except_table11236
+ GCC_except_table11241
+ GCC_except_table11242
+ GCC_except_table11246
+ GCC_except_table1245
+ GCC_except_table1249
+ GCC_except_table1257
+ GCC_except_table1258
+ GCC_except_table1259
+ GCC_except_table1263
+ GCC_except_table1264
+ GCC_except_table1285
+ GCC_except_table1294
+ GCC_except_table1317
+ GCC_except_table1321
+ GCC_except_table1323
+ GCC_except_table1325
+ GCC_except_table1335
+ GCC_except_table1383
+ GCC_except_table1385
+ GCC_except_table1591
+ GCC_except_table1604
+ GCC_except_table1616
+ GCC_except_table1639
+ GCC_except_table1651
+ GCC_except_table1656
+ GCC_except_table1745
+ GCC_except_table1748
+ GCC_except_table1757
+ GCC_except_table1779
+ GCC_except_table1804
+ GCC_except_table1805
+ GCC_except_table1866
+ GCC_except_table1989
+ GCC_except_table1995
+ GCC_except_table2020
+ GCC_except_table2672
+ GCC_except_table5626
+ GCC_except_table5667
+ GCC_except_table5703
+ GCC_except_table5705
+ GCC_except_table5707
+ GCC_except_table5712
+ GCC_except_table5722
+ GCC_except_table5726
+ GCC_except_table5772
+ GCC_except_table5791
+ GCC_except_table5812
+ GCC_except_table5817
+ GCC_except_table5836
+ GCC_except_table5839
+ GCC_except_table5845
+ GCC_except_table5848
+ GCC_except_table5857
+ GCC_except_table5868
+ GCC_except_table5882
+ GCC_except_table5888
+ GCC_except_table5895
+ GCC_except_table5902
+ GCC_except_table5908
+ GCC_except_table5916
+ GCC_except_table5919
+ GCC_except_table5930
+ GCC_except_table5932
+ GCC_except_table5934
+ GCC_except_table5941
+ GCC_except_table5943
+ GCC_except_table5946
+ GCC_except_table5949
+ GCC_except_table6057
+ GCC_except_table6061
+ GCC_except_table6121
+ GCC_except_table6154
+ GCC_except_table6191
+ GCC_except_table6198
+ GCC_except_table6219
+ GCC_except_table6299
+ GCC_except_table6314
+ GCC_except_table6319
+ GCC_except_table6334
+ GCC_except_table6355
+ GCC_except_table6356
+ GCC_except_table6360
+ GCC_except_table6361
+ GCC_except_table6464
+ GCC_except_table6473
+ GCC_except_table6493
+ GCC_except_table6510
+ GCC_except_table6584
+ GCC_except_table6654
+ GCC_except_table6657
+ GCC_except_table6680
+ GCC_except_table6724
+ GCC_except_table6867
+ GCC_except_table6942
+ GCC_except_table6957
+ GCC_except_table6958
+ GCC_except_table6959
+ GCC_except_table6972
+ GCC_except_table6973
+ GCC_except_table6974
+ GCC_except_table6975
+ GCC_except_table6990
+ GCC_except_table6991
+ GCC_except_table7005
+ GCC_except_table7006
+ GCC_except_table7010
+ GCC_except_table7050
+ GCC_except_table7123
+ GCC_except_table7124
+ GCC_except_table7134
+ GCC_except_table7136
+ GCC_except_table7138
+ GCC_except_table7147
+ GCC_except_table7150
+ GCC_except_table7151
+ GCC_except_table7153
+ GCC_except_table7154
+ GCC_except_table7156
+ GCC_except_table7157
+ GCC_except_table7227
+ GCC_except_table7262
+ GCC_except_table7299
+ GCC_except_table7300
+ GCC_except_table7350
+ GCC_except_table8041
+ GCC_except_table8044
+ GCC_except_table8109
+ GCC_except_table8256
+ GCC_except_table8259
+ GCC_except_table8261
+ GCC_except_table8266
+ GCC_except_table8282
+ GCC_except_table8283
+ GCC_except_table8288
+ GCC_except_table8289
+ GCC_except_table8316
+ GCC_except_table8317
+ GCC_except_table8318
+ GCC_except_table8319
+ GCC_except_table8332
+ GCC_except_table8511
+ GCC_except_table8558
+ GCC_except_table8901
+ GCC_except_table8995
+ GCC_except_table9173
+ GCC_except_table9366
+ GCC_except_table9381
+ GCC_except_table9418
+ GCC_except_table9425
+ GCC_except_table9463
+ GCC_except_table9464
+ GCC_except_table9465
+ GCC_except_table9466
+ GCC_except_table9471
+ GCC_except_table9477
+ GCC_except_table9478
+ GCC_except_table9485
+ GCC_except_table9495
+ GCC_except_table9497
+ GCC_except_table9498
+ GCC_except_table9500
+ GCC_except_table9510
+ GCC_except_table9512
+ GCC_except_table9518
+ GCC_except_table9520
+ GCC_except_table9522
+ GCC_except_table9524
+ GCC_except_table9532
+ GCC_except_table9557
+ GCC_except_table9558
+ GCC_except_table9559
+ GCC_except_table9560
+ GCC_except_table9561
+ GCC_except_table9562
+ GCC_except_table9563
+ GCC_except_table9564
+ GCC_except_table9565
+ GCC_except_table9622
+ GCC_except_table9629
+ GCC_except_table9707
+ GCC_except_table9755
+ GCC_except_table9779
+ GCC_except_table9780
+ GCC_except_table9784
+ GCC_except_table9785
+ GCC_except_table9787
+ GCC_except_table9804
+ GCC_except_table9814
+ GCC_except_table9820
+ GCC_except_table9825
+ GCC_except_table9827
+ GCC_except_table9830
+ GCC_except_table9831
+ GCC_except_table9832
+ GCC_except_table9906
+ GCC_except_table9916
+ _NUMediaCharacteristicForSemanticStyleTrackCorruptionInfo
+ _NUQuicktimeMetadataKey_SmartStyleEditInfos
+ _NUSemanticStyleTrackCorruptionInfoFromAsset
+ _OBJC_IVAR_$_NUVideoCorruptionInfo._insufficientlyCoveredFrameCount
+ _OBJC_IVAR_$_NUVideoCorruptionInfo._totalMainFrameCount
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
+ _objc_msgSend$isWideGamut
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
- GCC_except_table10122
- GCC_except_table10123
- GCC_except_table10129
- GCC_except_table10130
- GCC_except_table10133
- GCC_except_table10230
- GCC_except_table10231
- GCC_except_table10234
- GCC_except_table10235
- GCC_except_table10236
- GCC_except_table10237
- GCC_except_table10238
- GCC_except_table10241
- GCC_except_table10249
- GCC_except_table10251
- GCC_except_table10252
- GCC_except_table10262
- GCC_except_table10263
- GCC_except_table10268
- GCC_except_table10269
- GCC_except_table10270
- GCC_except_table10273
- GCC_except_table10274
- GCC_except_table10275
- GCC_except_table10276
- GCC_except_table10281
- GCC_except_table10299
- GCC_except_table10303
- GCC_except_table10304
- GCC_except_table10306
- GCC_except_table10316
- GCC_except_table10321
- GCC_except_table10322
- GCC_except_table10323
- GCC_except_table10338
- GCC_except_table10384
- GCC_except_table10435
- GCC_except_table10512
- GCC_except_table10516
- GCC_except_table1068
- GCC_except_table10958
- GCC_except_table11119
- GCC_except_table11121
- GCC_except_table11167
- GCC_except_table11219
- GCC_except_table11227
- GCC_except_table11232
- GCC_except_table11233
- GCC_except_table11237
- GCC_except_table1248
- GCC_except_table1252
- GCC_except_table1260
- GCC_except_table1261
- GCC_except_table1265
- GCC_except_table1266
- GCC_except_table1267
- GCC_except_table1288
- GCC_except_table1297
- GCC_except_table1320
- GCC_except_table1326
- GCC_except_table1327
- GCC_except_table1328
- GCC_except_table1338
- GCC_except_table1386
- GCC_except_table1388
- GCC_except_table1593
- GCC_except_table1606
- GCC_except_table1618
- GCC_except_table1641
- GCC_except_table1653
- GCC_except_table1658
- GCC_except_table1747
- GCC_except_table1750
- GCC_except_table1759
- GCC_except_table1781
- GCC_except_table1806
- GCC_except_table1807
- GCC_except_table1868
- GCC_except_table1994
- GCC_except_table1996
- GCC_except_table2021
- GCC_except_table2671
- GCC_except_table5625
- GCC_except_table5666
- GCC_except_table5702
- GCC_except_table5704
- GCC_except_table5706
- GCC_except_table5711
- GCC_except_table5720
- GCC_except_table5725
- GCC_except_table5771
- GCC_except_table5790
- GCC_except_table5811
- GCC_except_table5816
- GCC_except_table5835
- GCC_except_table5837
- GCC_except_table5843
- GCC_except_table5846
- GCC_except_table5856
- GCC_except_table5859
- GCC_except_table5869
- GCC_except_table5886
- GCC_except_table5893
- GCC_except_table5899
- GCC_except_table5903
- GCC_except_table5912
- GCC_except_table5917
- GCC_except_table5922
- GCC_except_table5931
- GCC_except_table5933
- GCC_except_table5936
- GCC_except_table5942
- GCC_except_table5944
- GCC_except_table5947
- GCC_except_table6056
- GCC_except_table6060
- GCC_except_table6120
- GCC_except_table6152
- GCC_except_table6190
- GCC_except_table6197
- GCC_except_table6218
- GCC_except_table6294
- GCC_except_table6303
- GCC_except_table6306
- GCC_except_table6326
- GCC_except_table6344
- GCC_except_table6347
- GCC_except_table6348
- GCC_except_table6353
- GCC_except_table6456
- GCC_except_table6465
- GCC_except_table6485
- GCC_except_table6502
- GCC_except_table6576
- GCC_except_table6641
- GCC_except_table6646
- GCC_except_table6672
- GCC_except_table6716
- GCC_except_table6859
- GCC_except_table6934
- GCC_except_table6949
- GCC_except_table6950
- GCC_except_table6951
- GCC_except_table6964
- GCC_except_table6965
- GCC_except_table6966
- GCC_except_table6967
- GCC_except_table6982
- GCC_except_table6983
- GCC_except_table6997
- GCC_except_table6998
- GCC_except_table7002
- GCC_except_table7042
- GCC_except_table7115
- GCC_except_table7116
- GCC_except_table7120
- GCC_except_table7122
- GCC_except_table7126
- GCC_except_table7131
- GCC_except_table7135
- GCC_except_table7140
- GCC_except_table7141
- GCC_except_table7142
- GCC_except_table7145
- GCC_except_table7146
- GCC_except_table7219
- GCC_except_table7254
- GCC_except_table7342
- GCC_except_table8033
- GCC_except_table8036
- GCC_except_table8101
- GCC_except_table8240
- GCC_except_table8243
- GCC_except_table8253
- GCC_except_table8258
- GCC_except_table8272
- GCC_except_table8274
- GCC_except_table8275
- GCC_except_table8281
- GCC_except_table8301
- GCC_except_table8308
- GCC_except_table8310
- GCC_except_table8311
- GCC_except_table8324
- GCC_except_table8503
- GCC_except_table8550
- GCC_except_table8892
- GCC_except_table8986
- GCC_except_table9164
- GCC_except_table9357
- GCC_except_table9372
- GCC_except_table9409
- GCC_except_table9416
- GCC_except_table9454
- GCC_except_table9455
- GCC_except_table9456
- GCC_except_table9457
- GCC_except_table9462
- GCC_except_table9468
- GCC_except_table9469
- GCC_except_table9476
- GCC_except_table9479
- GCC_except_table9486
- GCC_except_table9489
- GCC_except_table9491
- GCC_except_table9492
- GCC_except_table9493
- GCC_except_table9494
- GCC_except_table9499
- GCC_except_table9504
- GCC_except_table9509
- GCC_except_table9515
- GCC_except_table9523
- GCC_except_table9530
- GCC_except_table9531
- GCC_except_table9533
- GCC_except_table9534
- GCC_except_table9536
- GCC_except_table9537
- GCC_except_table9541
- GCC_except_table9547
- GCC_except_table9613
- GCC_except_table9620
- GCC_except_table9698
- GCC_except_table9746
- GCC_except_table9770
- GCC_except_table9771
- GCC_except_table9775
- GCC_except_table9776
- GCC_except_table9777
- GCC_except_table9778
- GCC_except_table9805
- GCC_except_table9811
- GCC_except_table9812
- GCC_except_table9813
- GCC_except_table9816
- GCC_except_table9818
- GCC_except_table9823
- GCC_except_table9897
- GCC_except_table9907
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
- "AVAssetWritingPlanner returned no segment recommendations (regression of rdar://170564263?)"
- "Failed to get style learn time: %{public}@"
- "NU_RENDER_METEOR_PLUS_AS_HDR"
```

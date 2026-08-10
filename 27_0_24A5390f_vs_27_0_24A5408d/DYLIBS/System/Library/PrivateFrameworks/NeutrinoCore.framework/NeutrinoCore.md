## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x30d0e8
-  __TEXT.__objc_methlist: 0x2023c
+912.0.111.0.0
+  __TEXT.__text: 0x310f64
+  __TEXT.__objc_methlist: 0x20474
   __TEXT.__const: 0x2918
   __TEXT.__swift5_typeref: 0x3e7
   __TEXT.__swift5_reflstr: 0x93

   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x3d7ef
+  __TEXT.__cstring: 0x3dae2
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x7f54
+  __TEXT.__gcc_except_tab: 0x7f8c
   __TEXT.__oslogstring: 0x5489
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x8460
+  __TEXT.__unwind_info: 0x84f0
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f50
-  __DATA_CONST.__objc_classlist: 0x15b0
+  __DATA_CONST.__const: 0x3f78
+  __DATA_CONST.__objc_classlist: 0x15b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb2c0
+  __DATA_CONST.__objc_selrefs: 0xb338
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0xfe0
+  __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0xae0
-  __DATA_CONST.__got: 0x21f8
+  __DATA_CONST.__got: 0x2200
   __AUTH_CONST.__const: 0x4e80
-  __AUTH_CONST.__cfstring: 0x1c8c0
-  __AUTH_CONST.__objc_const: 0x35f78
+  __AUTH_CONST.__cfstring: 0x1ca00
+  __AUTH_CONST.__objc_const: 0x36110
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x10c0
-  __DATA.__objc_ivar: 0x196c
+  __AUTH_CONST.__auth_got: 0x10c8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1970
   __DATA.__data: 0x3898
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1280

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11663
-  Symbols:   25091
-  CStrings:  7156
+  Functions: 11708
+  Symbols:   25161
+  CStrings:  7174
 
Symbols:
+ -[NUDataAccumulatorCacheNode evaluateSettings:pipelineState:error:]
+ -[NUImageGeometry geometryByApplyingCleanAperture]
+ -[NUImageGeometry geometryByCroppingToScaledRect:]
+ -[NUImageGeometry geometryByResettingCleanAperture]
+ -[NUImageGeometry geometryByUpdatingScale:]
+ -[NUImageGeometry geometryWithDuration:]
+ -[NUImageGeometry geometryWithRoundingPolicy:]
+ -[NUImageGeometry geometryWithSpaceMap:]
+ -[NUImageGeometry geometryWithZeroOrigin]
+ -[NUImageGeometry hasCleanRect]
+ -[NUKeyFrameNode _clapCompensationScale]
+ -[NUKeyFrameNode _evaluateImage:]
+ -[NUKeyFrameNode _evaluateImageGeometry:]
+ -[NUKeyFrameNode _transformWithError:]
+ -[NUKeyFrameNode applyCleanAperture]
+ -[NUKeyFrameNode canPropagateOriginalAuxiliaryData:]
+ -[NUKeyFrameNode canPropagateOriginalLivePhotoMetadataTrack]
+ -[NUKeyFrameNode cleanAperture]
+ -[NUKeyFrameNode initWithInput:keyFrameTime:applyCleanAperture:]
+ -[NUKeyFrameNode initWithSettings:inputs:]
+ -[NUKeyFrameNode keyFrameTime]
+ -[NUKeyFrameNode nodeByReplayingAgainstCache:pipelineState:error:]
+ -[NUKeyFrameNode resolvedNodeWithCachedInputs:settings:pipelineState:error:]
+ -[NUKeyFrameNode sampleMode]
+ -[NUKeyFrameNode targetScale]
+ -[NUKeyFrameNode videoExtent]
+ -[NUKeyFrameNode videoScale]
+ -[NUKeyFrameSourceNode cleanAperture]
+ -[NUPipelineOutputNode applyCleanAperture]
+ -[NUPixelBufferSourceNode cleanAperture]
+ -[NURenderJob shouldApplyCleanAperture]
+ -[NURuntimeExpression identifier]
+ -[NURuntimeExpression initWithNode:format:identifier:]
+ -[NUVideoFrameSourceNode _evaluateImageGeometryWithSourceOptions:error:]
+ -[NUVideoFrameSourceNode cleanAperture]
+ -[_NUComputedMedia identifier]
+ -[_NUMediaGeometry geometryByApplyingCleanAperture]
+ -[_NUMediaGeometry geometryByCroppingToScaledRect:]
+ -[_NUMediaGeometry geometryByResettingCleanAperture]
+ -[_NUMediaGeometry geometryWithRoundingPolicy:]
+ -[_NUMediaGeometry geometryWithZeroOrigin]
+ -[_NUMediaGeometry hash]
+ -[_NUMediaGeometry isEqual:]
+ -[_NUMediaGeometry isEqualToMediaGeometry:]
+ GCC_except_table10176
+ GCC_except_table10177
+ GCC_except_table10183
+ GCC_except_table10184
+ GCC_except_table10186
+ GCC_except_table10187
+ GCC_except_table10295
+ GCC_except_table10298
+ GCC_except_table10299
+ GCC_except_table10303
+ GCC_except_table10305
+ GCC_except_table10306
+ GCC_except_table10316
+ GCC_except_table10322
+ GCC_except_table10323
+ GCC_except_table10329
+ GCC_except_table10338
+ GCC_except_table10341
+ GCC_except_table10353
+ GCC_except_table10354
+ GCC_except_table10355
+ GCC_except_table10356
+ GCC_except_table10357
+ GCC_except_table10358
+ GCC_except_table10360
+ GCC_except_table10362
+ GCC_except_table10363
+ GCC_except_table10364
+ GCC_except_table10369
+ GCC_except_table10370
+ GCC_except_table10371
+ GCC_except_table10372
+ GCC_except_table10373
+ GCC_except_table10375
+ GCC_except_table10376
+ GCC_except_table10377
+ GCC_except_table10378
+ GCC_except_table10379
+ GCC_except_table10380
+ GCC_except_table10381
+ GCC_except_table10382
+ GCC_except_table10387
+ GCC_except_table10388
+ GCC_except_table10389
+ GCC_except_table10390
+ GCC_except_table10391
+ GCC_except_table10392
+ GCC_except_table10438
+ GCC_except_table10489
+ GCC_except_table10566
+ GCC_except_table10570
+ GCC_except_table1071
+ GCC_except_table11012
+ GCC_except_table11173
+ GCC_except_table11175
+ GCC_except_table11221
+ GCC_except_table11273
+ GCC_except_table11281
+ GCC_except_table11286
+ GCC_except_table11287
+ GCC_except_table11291
+ GCC_except_table1266
+ GCC_except_table1270
+ GCC_except_table1278
+ GCC_except_table1279
+ GCC_except_table1280
+ GCC_except_table1283
+ GCC_except_table1284
+ GCC_except_table1306
+ GCC_except_table1315
+ GCC_except_table1338
+ GCC_except_table1342
+ GCC_except_table1344
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1356
+ GCC_except_table1404
+ GCC_except_table1406
+ GCC_except_table1620
+ GCC_except_table1634
+ GCC_except_table1646
+ GCC_except_table1669
+ GCC_except_table1681
+ GCC_except_table1686
+ GCC_except_table1775
+ GCC_except_table1778
+ GCC_except_table1787
+ GCC_except_table1809
+ GCC_except_table1834
+ GCC_except_table1835
+ GCC_except_table1896
+ GCC_except_table2019
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table2023
+ GCC_except_table2025
+ GCC_except_table2050
+ GCC_except_table2104
+ GCC_except_table2209
+ GCC_except_table2210
+ GCC_except_table2702
+ GCC_except_table2767
+ GCC_except_table2815
+ GCC_except_table2827
+ GCC_except_table2986
+ GCC_except_table3133
+ GCC_except_table3220
+ GCC_except_table3221
+ GCC_except_table3222
+ GCC_except_table3223
+ GCC_except_table3224
+ GCC_except_table3227
+ GCC_except_table3231
+ GCC_except_table3235
+ GCC_except_table3237
+ GCC_except_table3240
+ GCC_except_table3242
+ GCC_except_table3243
+ GCC_except_table3244
+ GCC_except_table3245
+ GCC_except_table3246
+ GCC_except_table3247
+ GCC_except_table3255
+ GCC_except_table3259
+ GCC_except_table3271
+ GCC_except_table3287
+ GCC_except_table3293
+ GCC_except_table3294
+ GCC_except_table3299
+ GCC_except_table3300
+ GCC_except_table3304
+ GCC_except_table3307
+ GCC_except_table3308
+ GCC_except_table3310
+ GCC_except_table3311
+ GCC_except_table3314
+ GCC_except_table3316
+ GCC_except_table3318
+ GCC_except_table3319
+ GCC_except_table3320
+ GCC_except_table3321
+ GCC_except_table3322
+ GCC_except_table3326
+ GCC_except_table3332
+ GCC_except_table3684
+ GCC_except_table3864
+ GCC_except_table388
+ GCC_except_table3933
+ GCC_except_table3937
+ GCC_except_table3939
+ GCC_except_table4076
+ GCC_except_table4084
+ GCC_except_table4085
+ GCC_except_table4090
+ GCC_except_table4096
+ GCC_except_table4124
+ GCC_except_table4131
+ GCC_except_table4136
+ GCC_except_table4138
+ GCC_except_table416
+ GCC_except_table422
+ GCC_except_table4265
+ GCC_except_table4266
+ GCC_except_table4267
+ GCC_except_table4270
+ GCC_except_table4271
+ GCC_except_table4272
+ GCC_except_table4279
+ GCC_except_table4284
+ GCC_except_table4285
+ GCC_except_table4286
+ GCC_except_table4288
+ GCC_except_table4290
+ GCC_except_table4305
+ GCC_except_table4307
+ GCC_except_table4332
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4372
+ GCC_except_table4373
+ GCC_except_table4379
+ GCC_except_table4382
+ GCC_except_table4383
+ GCC_except_table4384
+ GCC_except_table4386
+ GCC_except_table4390
+ GCC_except_table4396
+ GCC_except_table4400
+ GCC_except_table4404
+ GCC_except_table4405
+ GCC_except_table4406
+ GCC_except_table4408
+ GCC_except_table4415
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4493
+ GCC_except_table469
+ GCC_except_table4792
+ GCC_except_table4903
+ GCC_except_table4909
+ GCC_except_table4912
+ GCC_except_table4922
+ GCC_except_table4926
+ GCC_except_table4927
+ GCC_except_table4941
+ GCC_except_table5050
+ GCC_except_table5180
+ GCC_except_table5262
+ GCC_except_table5554
+ GCC_except_table556
+ GCC_except_table5656
+ GCC_except_table5697
+ GCC_except_table5733
+ GCC_except_table5735
+ GCC_except_table5737
+ GCC_except_table5742
+ GCC_except_table5751
+ GCC_except_table5752
+ GCC_except_table5756
+ GCC_except_table5802
+ GCC_except_table5821
+ GCC_except_table583
+ GCC_except_table5842
+ GCC_except_table5869
+ GCC_except_table5890
+ GCC_except_table5891
+ GCC_except_table5892
+ GCC_except_table5893
+ GCC_except_table5896
+ GCC_except_table5897
+ GCC_except_table5898
+ GCC_except_table5903
+ GCC_except_table5909
+ GCC_except_table5910
+ GCC_except_table5911
+ GCC_except_table5912
+ GCC_except_table5917
+ GCC_except_table5931
+ GCC_except_table5935
+ GCC_except_table5936
+ GCC_except_table5944
+ GCC_except_table5953
+ GCC_except_table5954
+ GCC_except_table5955
+ GCC_except_table5956
+ GCC_except_table5957
+ GCC_except_table5958
+ GCC_except_table5959
+ GCC_except_table5960
+ GCC_except_table5962
+ GCC_except_table5964
+ GCC_except_table5967
+ GCC_except_table5968
+ GCC_except_table5969
+ GCC_except_table5970
+ GCC_except_table5971
+ GCC_except_table5973
+ GCC_except_table5975
+ GCC_except_table5976
+ GCC_except_table5978
+ GCC_except_table5979
+ GCC_except_table607
+ GCC_except_table6087
+ GCC_except_table6091
+ GCC_except_table615
+ GCC_except_table6151
+ GCC_except_table6183
+ GCC_except_table6184
+ GCC_except_table6221
+ GCC_except_table6228
+ GCC_except_table6249
+ GCC_except_table6329
+ GCC_except_table6341
+ GCC_except_table6344
+ GCC_except_table6349
+ GCC_except_table6364
+ GCC_except_table6382
+ GCC_except_table6385
+ GCC_except_table6386
+ GCC_except_table6390
+ GCC_except_table6391
+ GCC_except_table6494
+ GCC_except_table6503
+ GCC_except_table6523
+ GCC_except_table6540
+ GCC_except_table6614
+ GCC_except_table6685
+ GCC_except_table6688
+ GCC_except_table6711
+ GCC_except_table6755
+ GCC_except_table6898
+ GCC_except_table6988
+ GCC_except_table6989
+ GCC_except_table7003
+ GCC_except_table7004
+ GCC_except_table7021
+ GCC_except_table7022
+ GCC_except_table7036
+ GCC_except_table7037
+ GCC_except_table7042
+ GCC_except_table7082
+ GCC_except_table7155
+ GCC_except_table7160
+ GCC_except_table7162
+ GCC_except_table7166
+ GCC_except_table7168
+ GCC_except_table7170
+ GCC_except_table7171
+ GCC_except_table7175
+ GCC_except_table7179
+ GCC_except_table7180
+ GCC_except_table7181
+ GCC_except_table7182
+ GCC_except_table7183
+ GCC_except_table7185
+ GCC_except_table7186
+ GCC_except_table7188
+ GCC_except_table7189
+ GCC_except_table7259
+ GCC_except_table7294
+ GCC_except_table7331
+ GCC_except_table7332
+ GCC_except_table7382
+ GCC_except_table8075
+ GCC_except_table8078
+ GCC_except_table8144
+ GCC_except_table8286
+ GCC_except_table8291
+ GCC_except_table8294
+ GCC_except_table8296
+ GCC_except_table8301
+ GCC_except_table8315
+ GCC_except_table8323
+ GCC_except_table8324
+ GCC_except_table8344
+ GCC_except_table8351
+ GCC_except_table8352
+ GCC_except_table8353
+ GCC_except_table8354
+ GCC_except_table8367
+ GCC_except_table8555
+ GCC_except_table8602
+ GCC_except_table8945
+ GCC_except_table9039
+ GCC_except_table9217
+ GCC_except_table9411
+ GCC_except_table9426
+ GCC_except_table9470
+ GCC_except_table9509
+ GCC_except_table9516
+ GCC_except_table9523
+ GCC_except_table9530
+ GCC_except_table9533
+ GCC_except_table9547
+ GCC_except_table9567
+ GCC_except_table9569
+ GCC_except_table9571
+ GCC_except_table9577
+ GCC_except_table9580
+ GCC_except_table9584
+ GCC_except_table9585
+ GCC_except_table9587
+ GCC_except_table9588
+ GCC_except_table9589
+ GCC_except_table9590
+ GCC_except_table9591
+ GCC_except_table9593
+ GCC_except_table9594
+ GCC_except_table9595
+ GCC_except_table9596
+ GCC_except_table9597
+ GCC_except_table9598
+ GCC_except_table9599
+ GCC_except_table9600
+ GCC_except_table9601
+ GCC_except_table9602
+ GCC_except_table9603
+ GCC_except_table9604
+ GCC_except_table9605
+ GCC_except_table9606
+ GCC_except_table9607
+ GCC_except_table9608
+ GCC_except_table9609
+ GCC_except_table9610
+ GCC_except_table9667
+ GCC_except_table9674
+ GCC_except_table9752
+ GCC_except_table9800
+ GCC_except_table9824
+ GCC_except_table9829
+ GCC_except_table9840
+ GCC_except_table9849
+ GCC_except_table9859
+ GCC_except_table9865
+ GCC_except_table9866
+ GCC_except_table9867
+ GCC_except_table9870
+ GCC_except_table9872
+ GCC_except_table9875
+ GCC_except_table9876
+ GCC_except_table9877
+ GCC_except_table9951
+ GCC_except_table9961
+ _CVImageBufferGetCleanRect
+ _NUOrientationTransformRelativeRect
+ _NUPixelRectAbsolute
+ _NUPixelRectRelative
+ _OBJC_CLASS_$_NUKeyFrameNode
+ _OBJC_IVAR_$_NURuntimeExpression._identifier
+ _OBJC_IVAR_$__NUComputedMedia._identifier
+ _OBJC_METACLASS_$_NUKeyFrameNode
+ __OBJC_$_INSTANCE_METHODS_NUKeyFrameNode
+ __OBJC_$_PROP_LIST_NUKeyFrameNode
+ __OBJC_CLASS_RO_$_NUKeyFrameNode
+ __OBJC_METACLASS_RO_$_NUKeyFrameNode
+ ___82-[_NUComputeProcessorPipeline outputMediaWithInputMedias:format:renderNode:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e43_v32?0"NSString"8"<NUMediaPrivate>"16^B24ls32l8r40l8r48l8
+ _objc_msgSend$_clapCompensationScale
+ _objc_msgSend$geometryByApplyingCleanAperture
+ _objc_msgSend$geometryByCroppingToScaledRect:
+ _objc_msgSend$geometryByResettingCleanAperture
+ _objc_msgSend$geometryWithDuration:
+ _objc_msgSend$geometryWithRoundingPolicy:
+ _objc_msgSend$geometryWithSpaceMap:
+ _objc_msgSend$geometryWithZeroOrigin
+ _objc_msgSend$imageByClampingToRect:
+ _objc_msgSend$initWithInput:keyFrameTime:applyCleanAperture:
+ _objc_msgSend$initWithNode:format:identifier:
+ _objc_msgSend$initWithScaledExtent:renderScale:orientation:
+ _objc_msgSend$isEqualToMediaGeometry:
+ _objc_msgSend$keyFrameTime
+ _objc_msgSend$shouldApplyCleanAperture
+ _objc_msgSend$videoExtent
+ _objc_msgSend$videoScale
+ _objc_msgSend$writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:
- -[NURenderPipelineState applyCleanAperture]
- -[NURenderPipelineState setApplyCleanAperture:]
- GCC_except_table10131
- GCC_except_table10132
- GCC_except_table10138
- GCC_except_table10139
- GCC_except_table10141
- GCC_except_table10142
- GCC_except_table10239
- GCC_except_table10240
- GCC_except_table10243
- GCC_except_table10244
- GCC_except_table10245
- GCC_except_table10246
- GCC_except_table10247
- GCC_except_table10248
- GCC_except_table10250
- GCC_except_table10253
- GCC_except_table10254
- GCC_except_table10256
- GCC_except_table10257
- GCC_except_table10258
- GCC_except_table10260
- GCC_except_table10261
- GCC_except_table10271
- GCC_except_table10272
- GCC_except_table10277
- GCC_except_table10278
- GCC_except_table10279
- GCC_except_table10280
- GCC_except_table10282
- GCC_except_table10283
- GCC_except_table10287
- GCC_except_table10296
- GCC_except_table10297
- GCC_except_table10300
- GCC_except_table10308
- GCC_except_table10309
- GCC_except_table10310
- GCC_except_table10311
- GCC_except_table10312
- GCC_except_table10313
- GCC_except_table10315
- GCC_except_table10318
- GCC_except_table10319
- GCC_except_table10326
- GCC_except_table10331
- GCC_except_table10343
- GCC_except_table10344
- GCC_except_table10393
- GCC_except_table10444
- GCC_except_table10521
- GCC_except_table10525
- GCC_except_table1065
- GCC_except_table10967
- GCC_except_table11128
- GCC_except_table11130
- GCC_except_table11176
- GCC_except_table11228
- GCC_except_table11236
- GCC_except_table11241
- GCC_except_table11242
- GCC_except_table11246
- GCC_except_table1245
- GCC_except_table1249
- GCC_except_table1257
- GCC_except_table1258
- GCC_except_table1259
- GCC_except_table1262
- GCC_except_table1263
- GCC_except_table1264
- GCC_except_table1294
- GCC_except_table1317
- GCC_except_table1321
- GCC_except_table1323
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1335
- GCC_except_table1383
- GCC_except_table1385
- GCC_except_table1591
- GCC_except_table1604
- GCC_except_table1616
- GCC_except_table1639
- GCC_except_table1651
- GCC_except_table1656
- GCC_except_table1745
- GCC_except_table1748
- GCC_except_table1757
- GCC_except_table1779
- GCC_except_table1804
- GCC_except_table1805
- GCC_except_table1866
- GCC_except_table1989
- GCC_except_table1990
- GCC_except_table1991
- GCC_except_table1992
- GCC_except_table1993
- GCC_except_table1995
- GCC_except_table2074
- GCC_except_table2179
- GCC_except_table2180
- GCC_except_table2672
- GCC_except_table2737
- GCC_except_table2785
- GCC_except_table2797
- GCC_except_table2956
- GCC_except_table3103
- GCC_except_table3183
- GCC_except_table3190
- GCC_except_table3191
- GCC_except_table3192
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3197
- GCC_except_table3198
- GCC_except_table3201
- GCC_except_table3204
- GCC_except_table3205
- GCC_except_table3207
- GCC_except_table3210
- GCC_except_table3211
- GCC_except_table3212
- GCC_except_table3214
- GCC_except_table3215
- GCC_except_table3216
- GCC_except_table3217
- GCC_except_table3225
- GCC_except_table3229
- GCC_except_table3257
- GCC_except_table3263
- GCC_except_table3266
- GCC_except_table3269
- GCC_except_table3270
- GCC_except_table3274
- GCC_except_table3277
- GCC_except_table3278
- GCC_except_table3280
- GCC_except_table3281
- GCC_except_table3284
- GCC_except_table3286
- GCC_except_table3289
- GCC_except_table3290
- GCC_except_table3291
- GCC_except_table3292
- GCC_except_table3302
- GCC_except_table3654
- GCC_except_table3834
- GCC_except_table387
- GCC_except_table3903
- GCC_except_table3907
- GCC_except_table3909
- GCC_except_table4046
- GCC_except_table4054
- GCC_except_table4055
- GCC_except_table4060
- GCC_except_table4066
- GCC_except_table4071
- GCC_except_table4094
- GCC_except_table4106
- GCC_except_table4108
- GCC_except_table420
- GCC_except_table4235
- GCC_except_table4236
- GCC_except_table4237
- GCC_except_table4240
- GCC_except_table4241
- GCC_except_table4242
- GCC_except_table4247
- GCC_except_table4249
- GCC_except_table4254
- GCC_except_table4255
- GCC_except_table4256
- GCC_except_table4258
- GCC_except_table4260
- GCC_except_table4275
- GCC_except_table4302
- GCC_except_table4338
- GCC_except_table4339
- GCC_except_table4342
- GCC_except_table4343
- GCC_except_table4348
- GCC_except_table4349
- GCC_except_table4352
- GCC_except_table4353
- GCC_except_table4354
- GCC_except_table4355
- GCC_except_table4356
- GCC_except_table4357
- GCC_except_table4358
- GCC_except_table4360
- GCC_except_table4366
- GCC_except_table4370
- GCC_except_table4374
- GCC_except_table4375
- GCC_except_table4376
- GCC_except_table4463
- GCC_except_table467
- GCC_except_table4762
- GCC_except_table4873
- GCC_except_table4879
- GCC_except_table4882
- GCC_except_table4892
- GCC_except_table4896
- GCC_except_table4897
- GCC_except_table4911
- GCC_except_table5020
- GCC_except_table5150
- GCC_except_table5232
- GCC_except_table5524
- GCC_except_table553
- GCC_except_table5626
- GCC_except_table5667
- GCC_except_table5703
- GCC_except_table5705
- GCC_except_table5707
- GCC_except_table5712
- GCC_except_table5721
- GCC_except_table5722
- GCC_except_table5726
- GCC_except_table577
- GCC_except_table5772
- GCC_except_table5791
- GCC_except_table5812
- GCC_except_table5817
- GCC_except_table5836
- GCC_except_table5838
- GCC_except_table5839
- GCC_except_table5844
- GCC_except_table5845
- GCC_except_table5848
- GCC_except_table5857
- GCC_except_table5860
- GCC_except_table5861
- GCC_except_table5862
- GCC_except_table5863
- GCC_except_table5864
- GCC_except_table5865
- GCC_except_table5867
- GCC_except_table5870
- GCC_except_table5871
- GCC_except_table5872
- GCC_except_table5873
- GCC_except_table5876
- GCC_except_table5879
- GCC_except_table5880
- GCC_except_table5881
- GCC_except_table5882
- GCC_except_table5888
- GCC_except_table5913
- GCC_except_table5914
- GCC_except_table5915
- GCC_except_table5916
- GCC_except_table5919
- GCC_except_table5923
- GCC_except_table5926
- GCC_except_table5927
- GCC_except_table5928
- GCC_except_table5929
- GCC_except_table5939
- GCC_except_table5940
- GCC_except_table5941
- GCC_except_table601
- GCC_except_table6057
- GCC_except_table6061
- GCC_except_table609
- GCC_except_table6121
- GCC_except_table6153
- GCC_except_table6154
- GCC_except_table6191
- GCC_except_table6198
- GCC_except_table6219
- GCC_except_table6299
- GCC_except_table6311
- GCC_except_table6314
- GCC_except_table6319
- GCC_except_table6334
- GCC_except_table6352
- GCC_except_table6355
- GCC_except_table6356
- GCC_except_table6360
- GCC_except_table6361
- GCC_except_table6464
- GCC_except_table6473
- GCC_except_table6493
- GCC_except_table6510
- GCC_except_table6584
- GCC_except_table6649
- GCC_except_table6654
- GCC_except_table6657
- GCC_except_table6724
- GCC_except_table6867
- GCC_except_table6942
- GCC_except_table6957
- GCC_except_table6958
- GCC_except_table6959
- GCC_except_table6972
- GCC_except_table6974
- GCC_except_table6975
- GCC_except_table6991
- GCC_except_table7010
- GCC_except_table7050
- GCC_except_table7123
- GCC_except_table7124
- GCC_except_table7128
- GCC_except_table7130
- GCC_except_table7134
- GCC_except_table7136
- GCC_except_table7138
- GCC_except_table7139
- GCC_except_table7143
- GCC_except_table7147
- GCC_except_table7148
- GCC_except_table7149
- GCC_except_table7150
- GCC_except_table7151
- GCC_except_table7153
- GCC_except_table7154
- GCC_except_table7157
- GCC_except_table7227
- GCC_except_table7262
- GCC_except_table7299
- GCC_except_table7300
- GCC_except_table7350
- GCC_except_table8041
- GCC_except_table8044
- GCC_except_table8109
- GCC_except_table8248
- GCC_except_table8251
- GCC_except_table8256
- GCC_except_table8259
- GCC_except_table8261
- GCC_except_table8266
- GCC_except_table8280
- GCC_except_table8282
- GCC_except_table8288
- GCC_except_table8289
- GCC_except_table8309
- GCC_except_table8316
- GCC_except_table8319
- GCC_except_table8332
- GCC_except_table8511
- GCC_except_table8558
- GCC_except_table8901
- GCC_except_table8995
- GCC_except_table9173
- GCC_except_table9366
- GCC_except_table9381
- GCC_except_table9418
- GCC_except_table9425
- GCC_except_table9464
- GCC_except_table9465
- GCC_except_table9466
- GCC_except_table9471
- GCC_except_table9477
- GCC_except_table9478
- GCC_except_table9485
- GCC_except_table9488
- GCC_except_table9495
- GCC_except_table9497
- GCC_except_table9498
- GCC_except_table9500
- GCC_except_table9501
- GCC_except_table9502
- GCC_except_table9503
- GCC_except_table9512
- GCC_except_table9513
- GCC_except_table9517
- GCC_except_table9518
- GCC_except_table9520
- GCC_except_table9524
- GCC_except_table9526
- GCC_except_table9532
- GCC_except_table9535
- GCC_except_table9539
- GCC_except_table9544
- GCC_except_table9549
- GCC_except_table9550
- GCC_except_table9551
- GCC_except_table9552
- GCC_except_table9554
- GCC_except_table9559
- GCC_except_table9560
- GCC_except_table9561
- GCC_except_table9564
- GCC_except_table9622
- GCC_except_table9629
- GCC_except_table9707
- GCC_except_table9755
- GCC_except_table9779
- GCC_except_table9780
- GCC_except_table9784
- GCC_except_table9785
- GCC_except_table9786
- GCC_except_table9787
- GCC_except_table9795
- GCC_except_table9804
- GCC_except_table9814
- GCC_except_table9820
- GCC_except_table9821
- GCC_except_table9822
- GCC_except_table9827
- GCC_except_table9906
- GCC_except_table9916
- _OBJC_IVAR_$_NURenderPipelineState._applyCleanAperture
- __Z19NUPixelRectAbsolute11NUPixelRectS_
- __Z19NUPixelRectRelative11NUPixelRectS_
- _objc_msgSend$setApplyCleanAperture:
- _objc_msgSend$writeOpenEXRRepresentationOfImage:toURL:options:error:
CStrings:
+ " clean: [%g,%g;%gx%g]"
+ " extent: (%0.3f,%0.3f) %0.3fx%0.3f"
+ "(%f,%f) %fx%f"
+ "-[NUImageGeometry geometryByUpdatingScale:]"
+ "-[NUKeyFrameNode _evaluateImage:]"
+ "-[NUKeyFrameNode _evaluateImageGeometry:]"
+ "-[NUKeyFrameNode _transformWithError:]"
+ "-[NUKeyFrameNode initWithInput:keyFrameTime:applyCleanAperture:]"
+ "-[NUKeyFrameNode initWithSettings:inputs:]"
+ "-[NUKeyFrameNode nodeByReplayingAgainstCache:pipelineState:error:]"
+ "-[NURuntimeExpression initWithNode:format:identifier:]"
+ "-[NUVideoFrameSourceNode cleanAperture]"
+ "CIImage_%@.tiff"
+ "Invalid input render scale"
+ "Invalid media duration"
+ "Mismatched rounding policy"
+ "NUKeyFrameNode (CLAP-bake) evaluated without resolved settings"
+ "NUKeyFrameNode CLAP-bake mode requires RenderImage evaluation mode"
+ "NUKeyFrameNode requires a valid numeric keyFrameTime when applyCleanAperture is YES"
+ "cleanAperture"
+ "invalid input render scale"
+ "scaledSize: %@, scaledExtent: %@, extent: %@, scale: %@ (%f), orientation: %@, rounding: %@, cleanRect: %@, duration: %@"
+ "useOriginalExtent"
+ "videoExtent"
+ "videoScale"
- " clean: [%lu,%lu;%lux%lu]"
- " extent: %@"
- "(%ld,%ld) %ldx%ld"
- "-[NURuntimeExpression initWithNode:format:]"
- "CIImage_%@.exr"
- "Invalid applyCleanAperture value"
- "scaledSize: %@, scaledExtent: %@, extent: %@, scale: %@ (%f), orientation: %@, rounding: %@, cleanRect: %@"
```

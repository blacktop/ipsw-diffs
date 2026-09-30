## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0x33c79c
-  __TEXT.__objc_methlist: 0x20234
+911.0.134.0.0
+  __TEXT.__text: 0x340944
+  __TEXT.__objc_methlist: 0x2046c
   __TEXT.__const: 0x2918
   __TEXT.__swift5_typeref: 0x3e7
   __TEXT.__swift5_reflstr: 0x93

   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x3f21d
+  __TEXT.__cstring: 0x3f510
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x7fb0
+  __TEXT.__gcc_except_tab: 0x7fe8
   __TEXT.__oslogstring: 0x550b
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x8670
+  __TEXT.__unwind_info: 0x8700
   __TEXT.__eh_frame: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x15f0
-  __DATA_CONST.__objc_classlist: 0x15b0
+  __DATA_CONST.__objc_classlist: 0x15b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb2e0
+  __DATA_CONST.__objc_selrefs: 0xb358
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0xfe0
+  __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x2218
-  __AUTH_CONST.__const: 0x80a8
-  __AUTH_CONST.__cfstring: 0x1c8e0
-  __AUTH_CONST.__objc_const: 0x35f78
+  __DATA_CONST.__got: 0x2220
+  __AUTH_CONST.__const: 0x80d8
+  __AUTH_CONST.__cfstring: 0x1ca20
+  __AUTH_CONST.__objc_const: 0x36110
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8b8
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xfc8
-  __DATA.__objc_ivar: 0x1968
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x196c
   __DATA.__data: 0x3898
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1270

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11748
-  Symbols:   25190
-  CStrings:  7160
+  Functions: 11793
+  Symbols:   25260
+  CStrings:  7178
 
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
+ GCC_except_table10006
+ GCC_except_table10221
+ GCC_except_table10222
+ GCC_except_table10228
+ GCC_except_table10229
+ GCC_except_table10231
+ GCC_except_table10232
+ GCC_except_table10338
+ GCC_except_table10346
+ GCC_except_table10348
+ GCC_except_table10367
+ GCC_except_table10372
+ GCC_except_table10373
+ GCC_except_table10374
+ GCC_except_table10380
+ GCC_except_table10389
+ GCC_except_table10392
+ GCC_except_table10404
+ GCC_except_table10405
+ GCC_except_table10406
+ GCC_except_table10407
+ GCC_except_table10408
+ GCC_except_table10409
+ GCC_except_table10411
+ GCC_except_table10413
+ GCC_except_table10414
+ GCC_except_table10415
+ GCC_except_table10420
+ GCC_except_table10421
+ GCC_except_table10422
+ GCC_except_table10423
+ GCC_except_table10424
+ GCC_except_table10426
+ GCC_except_table10427
+ GCC_except_table10428
+ GCC_except_table10429
+ GCC_except_table10430
+ GCC_except_table10431
+ GCC_except_table10432
+ GCC_except_table10433
+ GCC_except_table10438
+ GCC_except_table10439
+ GCC_except_table10440
+ GCC_except_table10441
+ GCC_except_table10442
+ GCC_except_table10443
+ GCC_except_table10501
+ GCC_except_table10552
+ GCC_except_table10641
+ GCC_except_table10645
+ GCC_except_table1103
+ GCC_except_table11089
+ GCC_except_table11250
+ GCC_except_table11252
+ GCC_except_table11298
+ GCC_except_table11352
+ GCC_except_table11360
+ GCC_except_table11367
+ GCC_except_table11368
+ GCC_except_table11372
+ GCC_except_table1302
+ GCC_except_table1310
+ GCC_except_table1311
+ GCC_except_table1312
+ GCC_except_table1315
+ GCC_except_table1316
+ GCC_except_table1340
+ GCC_except_table1349
+ GCC_except_table1374
+ GCC_except_table1378
+ GCC_except_table1380
+ GCC_except_table1381
+ GCC_except_table1382
+ GCC_except_table1392
+ GCC_except_table1440
+ GCC_except_table1442
+ GCC_except_table1658
+ GCC_except_table1672
+ GCC_except_table1684
+ GCC_except_table1707
+ GCC_except_table1719
+ GCC_except_table1724
+ GCC_except_table1813
+ GCC_except_table1816
+ GCC_except_table1825
+ GCC_except_table1847
+ GCC_except_table1934
+ GCC_except_table2059
+ GCC_except_table2061
+ GCC_except_table2062
+ GCC_except_table2063
+ GCC_except_table2065
+ GCC_except_table2090
+ GCC_except_table2144
+ GCC_except_table2249
+ GCC_except_table2250
+ GCC_except_table2742
+ GCC_except_table2807
+ GCC_except_table2857
+ GCC_except_table2869
+ GCC_except_table3028
+ GCC_except_table3175
+ GCC_except_table3255
+ GCC_except_table3266
+ GCC_except_table3267
+ GCC_except_table3268
+ GCC_except_table3272
+ GCC_except_table3275
+ GCC_except_table3278
+ GCC_except_table3279
+ GCC_except_table3283
+ GCC_except_table3286
+ GCC_except_table3287
+ GCC_except_table3288
+ GCC_except_table3290
+ GCC_except_table3291
+ GCC_except_table3292
+ GCC_except_table3293
+ GCC_except_table3301
+ GCC_except_table3307
+ GCC_except_table3319
+ GCC_except_table3336
+ GCC_except_table3342
+ GCC_except_table3344
+ GCC_except_table3347
+ GCC_except_table3348
+ GCC_except_table3352
+ GCC_except_table3355
+ GCC_except_table3356
+ GCC_except_table3359
+ GCC_except_table3360
+ GCC_except_table3363
+ GCC_except_table3365
+ GCC_except_table3367
+ GCC_except_table3368
+ GCC_except_table3369
+ GCC_except_table3370
+ GCC_except_table3371
+ GCC_except_table3375
+ GCC_except_table3381
+ GCC_except_table3733
+ GCC_except_table3914
+ GCC_except_table3983
+ GCC_except_table3987
+ GCC_except_table3989
+ GCC_except_table411
+ GCC_except_table4126
+ GCC_except_table4136
+ GCC_except_table4137
+ GCC_except_table4144
+ GCC_except_table4152
+ GCC_except_table4180
+ GCC_except_table4187
+ GCC_except_table4192
+ GCC_except_table4194
+ GCC_except_table4321
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4328
+ GCC_except_table4335
+ GCC_except_table4340
+ GCC_except_table4341
+ GCC_except_table4342
+ GCC_except_table4344
+ GCC_except_table4346
+ GCC_except_table4361
+ GCC_except_table4363
+ GCC_except_table4388
+ GCC_except_table439
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4428
+ GCC_except_table4429
+ GCC_except_table4435
+ GCC_except_table4438
+ GCC_except_table4439
+ GCC_except_table4440
+ GCC_except_table4442
+ GCC_except_table4446
+ GCC_except_table445
+ GCC_except_table4452
+ GCC_except_table4456
+ GCC_except_table4460
+ GCC_except_table4461
+ GCC_except_table4462
+ GCC_except_table4464
+ GCC_except_table4471
+ GCC_except_table4473
+ GCC_except_table4474
+ GCC_except_table4549
+ GCC_except_table4849
+ GCC_except_table496
+ GCC_except_table4960
+ GCC_except_table4966
+ GCC_except_table4969
+ GCC_except_table4979
+ GCC_except_table4983
+ GCC_except_table4984
+ GCC_except_table4998
+ GCC_except_table5108
+ GCC_except_table5242
+ GCC_except_table5324
+ GCC_except_table5616
+ GCC_except_table5719
+ GCC_except_table5744
+ GCC_except_table5780
+ GCC_except_table5782
+ GCC_except_table5784
+ GCC_except_table5789
+ GCC_except_table5798
+ GCC_except_table5799
+ GCC_except_table5803
+ GCC_except_table583
+ GCC_except_table5839
+ GCC_except_table5858
+ GCC_except_table5879
+ GCC_except_table5903
+ GCC_except_table5924
+ GCC_except_table5929
+ GCC_except_table5931
+ GCC_except_table5936
+ GCC_except_table5937
+ GCC_except_table5938
+ GCC_except_table5943
+ GCC_except_table5949
+ GCC_except_table5950
+ GCC_except_table5951
+ GCC_except_table5952
+ GCC_except_table5957
+ GCC_except_table5971
+ GCC_except_table5975
+ GCC_except_table5976
+ GCC_except_table5984
+ GCC_except_table5993
+ GCC_except_table5994
+ GCC_except_table5995
+ GCC_except_table5996
+ GCC_except_table5997
+ GCC_except_table5998
+ GCC_except_table5999
+ GCC_except_table6000
+ GCC_except_table6002
+ GCC_except_table6004
+ GCC_except_table6007
+ GCC_except_table6008
+ GCC_except_table6009
+ GCC_except_table6010
+ GCC_except_table6011
+ GCC_except_table6013
+ GCC_except_table6015
+ GCC_except_table6016
+ GCC_except_table6018
+ GCC_except_table6019
+ GCC_except_table610
+ GCC_except_table6127
+ GCC_except_table6131
+ GCC_except_table6191
+ GCC_except_table6223
+ GCC_except_table6224
+ GCC_except_table6261
+ GCC_except_table6268
+ GCC_except_table6289
+ GCC_except_table634
+ GCC_except_table6369
+ GCC_except_table6381
+ GCC_except_table6386
+ GCC_except_table6393
+ GCC_except_table6410
+ GCC_except_table6428
+ GCC_except_table6431
+ GCC_except_table6432
+ GCC_except_table6436
+ GCC_except_table6437
+ GCC_except_table644
+ GCC_except_table6540
+ GCC_except_table6549
+ GCC_except_table6569
+ GCC_except_table6586
+ GCC_except_table6660
+ GCC_except_table6731
+ GCC_except_table6734
+ GCC_except_table6757
+ GCC_except_table6801
+ GCC_except_table6944
+ GCC_except_table7034
+ GCC_except_table7035
+ GCC_except_table7049
+ GCC_except_table7050
+ GCC_except_table7067
+ GCC_except_table7068
+ GCC_except_table7082
+ GCC_except_table7083
+ GCC_except_table7088
+ GCC_except_table7128
+ GCC_except_table7206
+ GCC_except_table7208
+ GCC_except_table7212
+ GCC_except_table7214
+ GCC_except_table7216
+ GCC_except_table7217
+ GCC_except_table7221
+ GCC_except_table7225
+ GCC_except_table7226
+ GCC_except_table7229
+ GCC_except_table7230
+ GCC_except_table7231
+ GCC_except_table7233
+ GCC_except_table7234
+ GCC_except_table7236
+ GCC_except_table7237
+ GCC_except_table7307
+ GCC_except_table7344
+ GCC_except_table7383
+ GCC_except_table7384
+ GCC_except_table7434
+ GCC_except_table8127
+ GCC_except_table8130
+ GCC_except_table8198
+ GCC_except_table8341
+ GCC_except_table8346
+ GCC_except_table8349
+ GCC_except_table8351
+ GCC_except_table8356
+ GCC_except_table8370
+ GCC_except_table8378
+ GCC_except_table8379
+ GCC_except_table8399
+ GCC_except_table8406
+ GCC_except_table8407
+ GCC_except_table8408
+ GCC_except_table8409
+ GCC_except_table8422
+ GCC_except_table8610
+ GCC_except_table8657
+ GCC_except_table9000
+ GCC_except_table9085
+ GCC_except_table9263
+ GCC_except_table9457
+ GCC_except_table9472
+ GCC_except_table9509
+ GCC_except_table9516
+ GCC_except_table9557
+ GCC_except_table9564
+ GCC_except_table9571
+ GCC_except_table9578
+ GCC_except_table9581
+ GCC_except_table9595
+ GCC_except_table9615
+ GCC_except_table9617
+ GCC_except_table9619
+ GCC_except_table9625
+ GCC_except_table9628
+ GCC_except_table9632
+ GCC_except_table9633
+ GCC_except_table9635
+ GCC_except_table9636
+ GCC_except_table9637
+ GCC_except_table9638
+ GCC_except_table9639
+ GCC_except_table9641
+ GCC_except_table9642
+ GCC_except_table9643
+ GCC_except_table9644
+ GCC_except_table9645
+ GCC_except_table9646
+ GCC_except_table9647
+ GCC_except_table9648
+ GCC_except_table9649
+ GCC_except_table9650
+ GCC_except_table9651
+ GCC_except_table9652
+ GCC_except_table9653
+ GCC_except_table9654
+ GCC_except_table9655
+ GCC_except_table9656
+ GCC_except_table9657
+ GCC_except_table9658
+ GCC_except_table9715
+ GCC_except_table9722
+ GCC_except_table9800
+ GCC_except_table9848
+ GCC_except_table9873
+ GCC_except_table9880
+ GCC_except_table9887
+ GCC_except_table9888
+ GCC_except_table9897
+ GCC_except_table9907
+ GCC_except_table9913
+ GCC_except_table9914
+ GCC_except_table9915
+ GCC_except_table9917
+ GCC_except_table9919
+ GCC_except_table9922
+ GCC_except_table9923
+ GCC_except_table9924
+ GCC_except_table9996
+ OBJC_IVAR_$_NURuntimeExpression._identifier
+ OBJC_IVAR_$__NUComputedMedia._identifier
+ _CVImageBufferGetCleanRect
+ _NUOrientationTransformRelativeRect
+ _NUPixelRectAbsolute
+ _NUPixelRectRelative
+ _OBJC_CLASS_$_NUKeyFrameNode
+ _OBJC_METACLASS_$_NUKeyFrameNode
+ __OBJC_$_INSTANCE_METHODS_NUKeyFrameNode
+ __OBJC_$_PROP_LIST_NUKeyFrameNode
+ __OBJC_CLASS_RO_$_NUKeyFrameNode
+ __OBJC_METACLASS_RO_$_NUKeyFrameNode
+ ___82-[_NUComputeProcessorPipeline outputMediaWithInputMedias:format:renderNode:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e43_v32?0"NSString"8"<NUMediaPrivate>"16^B24l
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
- GCC_except_table10176
- GCC_except_table10177
- GCC_except_table10183
- GCC_except_table10184
- GCC_except_table10186
- GCC_except_table10187
- GCC_except_table10284
- GCC_except_table10285
- GCC_except_table10288
- GCC_except_table10289
- GCC_except_table10290
- GCC_except_table10291
- GCC_except_table10292
- GCC_except_table10293
- GCC_except_table10295
- GCC_except_table10298
- GCC_except_table10299
- GCC_except_table10301
- GCC_except_table10302
- GCC_except_table10303
- GCC_except_table10305
- GCC_except_table10306
- GCC_except_table10316
- GCC_except_table10317
- GCC_except_table10322
- GCC_except_table10323
- GCC_except_table10324
- GCC_except_table10325
- GCC_except_table10327
- GCC_except_table10328
- GCC_except_table10332
- GCC_except_table10359
- GCC_except_table10360
- GCC_except_table10363
- GCC_except_table10364
- GCC_except_table10366
- GCC_except_table10376
- GCC_except_table10383
- GCC_except_table10384
- GCC_except_table10386
- GCC_except_table10387
- GCC_except_table10393
- GCC_except_table10394
- GCC_except_table10397
- GCC_except_table10398
- GCC_except_table10456
- GCC_except_table10507
- GCC_except_table10596
- GCC_except_table10600
- GCC_except_table1097
- GCC_except_table11044
- GCC_except_table11205
- GCC_except_table11207
- GCC_except_table11253
- GCC_except_table11307
- GCC_except_table11315
- GCC_except_table11322
- GCC_except_table11323
- GCC_except_table11327
- GCC_except_table1277
- GCC_except_table1281
- GCC_except_table1289
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1294
- GCC_except_table1295
- GCC_except_table1328
- GCC_except_table1353
- GCC_except_table1357
- GCC_except_table1359
- GCC_except_table1360
- GCC_except_table1361
- GCC_except_table1371
- GCC_except_table1419
- GCC_except_table1421
- GCC_except_table1629
- GCC_except_table1642
- GCC_except_table1654
- GCC_except_table1677
- GCC_except_table1689
- GCC_except_table1694
- GCC_except_table1783
- GCC_except_table1786
- GCC_except_table1795
- GCC_except_table1817
- GCC_except_table1904
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2031
- GCC_except_table2032
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2114
- GCC_except_table2219
- GCC_except_table2220
- GCC_except_table2712
- GCC_except_table2777
- GCC_except_table2827
- GCC_except_table2839
- GCC_except_table2998
- GCC_except_table3145
- GCC_except_table3225
- GCC_except_table3232
- GCC_except_table3233
- GCC_except_table3236
- GCC_except_table3237
- GCC_except_table3238
- GCC_except_table3241
- GCC_except_table3242
- GCC_except_table3245
- GCC_except_table3248
- GCC_except_table3249
- GCC_except_table3253
- GCC_except_table3256
- GCC_except_table3257
- GCC_except_table3258
- GCC_except_table3259
- GCC_except_table3260
- GCC_except_table3261
- GCC_except_table3276
- GCC_except_table3277
- GCC_except_table3282
- GCC_except_table3305
- GCC_except_table3311
- GCC_except_table3314
- GCC_except_table3317
- GCC_except_table3318
- GCC_except_table3322
- GCC_except_table3325
- GCC_except_table3326
- GCC_except_table3329
- GCC_except_table3330
- GCC_except_table3333
- GCC_except_table3337
- GCC_except_table3338
- GCC_except_table3339
- GCC_except_table3340
- GCC_except_table3345
- GCC_except_table3351
- GCC_except_table3703
- GCC_except_table3884
- GCC_except_table3953
- GCC_except_table3957
- GCC_except_table3959
- GCC_except_table4096
- GCC_except_table410
- GCC_except_table4106
- GCC_except_table4107
- GCC_except_table4114
- GCC_except_table4122
- GCC_except_table4127
- GCC_except_table4150
- GCC_except_table4162
- GCC_except_table4164
- GCC_except_table4291
- GCC_except_table4292
- GCC_except_table4293
- GCC_except_table4296
- GCC_except_table4297
- GCC_except_table4298
- GCC_except_table4303
- GCC_except_table4305
- GCC_except_table4310
- GCC_except_table4311
- GCC_except_table4312
- GCC_except_table4314
- GCC_except_table4316
- GCC_except_table4331
- GCC_except_table4358
- GCC_except_table4394
- GCC_except_table4395
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4404
- GCC_except_table4405
- GCC_except_table4408
- GCC_except_table4409
- GCC_except_table4410
- GCC_except_table4411
- GCC_except_table4412
- GCC_except_table4413
- GCC_except_table4414
- GCC_except_table4416
- GCC_except_table4422
- GCC_except_table4426
- GCC_except_table443
- GCC_except_table4430
- GCC_except_table4431
- GCC_except_table4432
- GCC_except_table4519
- GCC_except_table4819
- GCC_except_table4930
- GCC_except_table4936
- GCC_except_table4939
- GCC_except_table494
- GCC_except_table4949
- GCC_except_table4953
- GCC_except_table4954
- GCC_except_table4968
- GCC_except_table5078
- GCC_except_table5212
- GCC_except_table5294
- GCC_except_table5586
- GCC_except_table5689
- GCC_except_table5714
- GCC_except_table5750
- GCC_except_table5752
- GCC_except_table5754
- GCC_except_table5759
- GCC_except_table5768
- GCC_except_table5769
- GCC_except_table5773
- GCC_except_table580
- GCC_except_table5809
- GCC_except_table5828
- GCC_except_table5849
- GCC_except_table5854
- GCC_except_table5873
- GCC_except_table5875
- GCC_except_table5876
- GCC_except_table5881
- GCC_except_table5882
- GCC_except_table5885
- GCC_except_table5894
- GCC_except_table5897
- GCC_except_table5898
- GCC_except_table5899
- GCC_except_table5901
- GCC_except_table5904
- GCC_except_table5907
- GCC_except_table5908
- GCC_except_table5910
- GCC_except_table5913
- GCC_except_table5916
- GCC_except_table5917
- GCC_except_table5918
- GCC_except_table5919
- GCC_except_table5920
- GCC_except_table5921
- GCC_except_table5922
- GCC_except_table5953
- GCC_except_table5954
- GCC_except_table5955
- GCC_except_table5956
- GCC_except_table5959
- GCC_except_table5963
- GCC_except_table5966
- GCC_except_table5967
- GCC_except_table5968
- GCC_except_table5969
- GCC_except_table5979
- GCC_except_table5980
- GCC_except_table5981
- GCC_except_table604
- GCC_except_table6097
- GCC_except_table6101
- GCC_except_table6161
- GCC_except_table6193
- GCC_except_table6194
- GCC_except_table6231
- GCC_except_table6238
- GCC_except_table6259
- GCC_except_table628
- GCC_except_table6339
- GCC_except_table6351
- GCC_except_table6356
- GCC_except_table6363
- GCC_except_table638
- GCC_except_table6380
- GCC_except_table6398
- GCC_except_table6401
- GCC_except_table6402
- GCC_except_table6406
- GCC_except_table6407
- GCC_except_table6510
- GCC_except_table6519
- GCC_except_table6539
- GCC_except_table6556
- GCC_except_table6630
- GCC_except_table6695
- GCC_except_table6700
- GCC_except_table6703
- GCC_except_table6770
- GCC_except_table6913
- GCC_except_table6988
- GCC_except_table7003
- GCC_except_table7004
- GCC_except_table7005
- GCC_except_table7018
- GCC_except_table7020
- GCC_except_table7021
- GCC_except_table7037
- GCC_except_table7056
- GCC_except_table7096
- GCC_except_table7169
- GCC_except_table7170
- GCC_except_table7174
- GCC_except_table7176
- GCC_except_table7180
- GCC_except_table7182
- GCC_except_table7184
- GCC_except_table7185
- GCC_except_table7189
- GCC_except_table7193
- GCC_except_table7194
- GCC_except_table7197
- GCC_except_table7198
- GCC_except_table7199
- GCC_except_table7204
- GCC_except_table7205
- GCC_except_table7275
- GCC_except_table7312
- GCC_except_table7351
- GCC_except_table7352
- GCC_except_table7402
- GCC_except_table8093
- GCC_except_table8096
- GCC_except_table8163
- GCC_except_table8302
- GCC_except_table8306
- GCC_except_table8311
- GCC_except_table8314
- GCC_except_table8316
- GCC_except_table8321
- GCC_except_table8335
- GCC_except_table8338
- GCC_except_table8343
- GCC_except_table8344
- GCC_except_table8364
- GCC_except_table8371
- GCC_except_table8374
- GCC_except_table8387
- GCC_except_table8566
- GCC_except_table8613
- GCC_except_table8956
- GCC_except_table9041
- GCC_except_table9219
- GCC_except_table9412
- GCC_except_table9427
- GCC_except_table9464
- GCC_except_table9471
- GCC_except_table9511
- GCC_except_table9512
- GCC_except_table9513
- GCC_except_table9514
- GCC_except_table9519
- GCC_except_table9525
- GCC_except_table9526
- GCC_except_table9533
- GCC_except_table9536
- GCC_except_table9543
- GCC_except_table9545
- GCC_except_table9546
- GCC_except_table9548
- GCC_except_table9549
- GCC_except_table9550
- GCC_except_table9551
- GCC_except_table9560
- GCC_except_table9561
- GCC_except_table9565
- GCC_except_table9566
- GCC_except_table9568
- GCC_except_table9572
- GCC_except_table9574
- GCC_except_table9580
- GCC_except_table9583
- GCC_except_table9587
- GCC_except_table9592
- GCC_except_table9597
- GCC_except_table9598
- GCC_except_table9599
- GCC_except_table9600
- GCC_except_table9602
- GCC_except_table9607
- GCC_except_table9608
- GCC_except_table9609
- GCC_except_table9612
- GCC_except_table9670
- GCC_except_table9677
- GCC_except_table9755
- GCC_except_table9803
- GCC_except_table9827
- GCC_except_table9828
- GCC_except_table9832
- GCC_except_table9833
- GCC_except_table9834
- GCC_except_table9835
- GCC_except_table9842
- GCC_except_table9843
- GCC_except_table9852
- GCC_except_table9862
- GCC_except_table9868
- GCC_except_table9869
- GCC_except_table9870
- GCC_except_table9874
- GCC_except_table9951
- GCC_except_table9961
- OBJC_IVAR_$_NURenderPipelineState._applyCleanAperture
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

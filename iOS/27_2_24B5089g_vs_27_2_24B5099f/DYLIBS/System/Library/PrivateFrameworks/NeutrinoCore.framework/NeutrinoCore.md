## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x3159a4
-  __TEXT.__objc_methlist: 0x21104
-  __TEXT.__const: 0x2798
+916.51.202.0.0
+  __TEXT.__text: 0x323700
+  __TEXT.__objc_methlist: 0x216fc
+  __TEXT.__const: 0x27a8
   __TEXT.__dlopen_cstrs: 0x45
-  __TEXT.__swift5_typeref: 0x3c9
+  __TEXT.__swift5_typeref: 0x52b
   __TEXT.__swift5_reflstr: 0x93
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__constg_swiftt: 0x158

   __TEXT.__swift5_fieldmd: 0x15c
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x3ec2e
-  __TEXT.__swift5_capture: 0x1f0
-  __TEXT.__gcc_except_tab: 0x813c
-  __TEXT.__oslogstring: 0x58ae
+  __TEXT.__cstring: 0x3f687
+  __TEXT.__swift5_capture: 0x350
+  __TEXT.__gcc_except_tab: 0x8170
+  __TEXT.__oslogstring: 0x58cd
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0xa238
-  __TEXT.__eh_frame: 0x418
+  __TEXT.__unwind_info: 0xa450
+  __TEXT.__eh_frame: 0x678
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4010
-  __DATA_CONST.__objc_classlist: 0x1600
+  __DATA_CONST.__const: 0x40e8
+  __DATA_CONST.__objc_classlist: 0x1618
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x4d8
+  __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb718
+  __DATA_CONST.__objc_selrefs: 0xb860
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1018
-  __DATA_CONST.__objc_arraydata: 0xae0
-  __DATA_CONST.__got: 0x2270
-  __AUTH_CONST.__const: 0x4e60
-  __AUTH_CONST.__cfstring: 0x1d020
-  __AUTH_CONST.__objc_const: 0x37a10
+  __DATA_CONST.__objc_superrefs: 0x1028
+  __DATA_CONST.__objc_arraydata: 0xaf0
+  __DATA_CONST.__got: 0x22d8
+  __AUTH_CONST.__const: 0x5468
+  __AUTH_CONST.__cfstring: 0x1d4e0
+  __AUTH_CONST.__objc_const: 0x37ed0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8e8
-  __AUTH_CONST.__objc_dictobj: 0x348
+  __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1a7c
-  __DATA.__data: 0x1c0
+  __AUTH_CONST.__auth_got: 0x10f0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x1aa8
+  __DATA.__data: 0x248
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__objc_data: 0xdbb0
+  __DATA_DIRTY.__objc_data: 0xdb60
   __DATA_DIRTY.__data: 0x3780
   __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11937
-  Symbols:   20870
-  CStrings:  7304
+  Functions: 12140
+  Symbols:   21069
+  CStrings:  7379
 
Symbols:
+ +[NUAssetCapability rawDecodeCapabilityFormat]
+ +[NUChannelData nullDataWithOptionalFormat:]
+ +[NUPipelineFactory optionalSelectorPipelineWithFormat:includeFallback:]
+ +[NUPixelFormat YCC8f420]
+ +[NUPixelFormat YCC8v420]
+ -[NSArray(NUControlDataRepresentable) nu_cardinality]
+ -[NSArray(NUControlDataRepresentable) nu_subdataAtIndex:format:error:]
+ -[NSObject(NUControlDataRepresentable) nu_cardinality]
+ -[NSObject(NUControlDataRepresentable) nu_subdataAtIndex:format:error:]
+ -[NSObject(NUControlDataRepresentable) nu_subdataForKey:format:error:]
+ -[NUArrayDescriptor defaultValueType]
+ -[NUBrushStrokeMaskIntersector initWithBrushMask:mask:strokeScale:ciContext:]
+ -[NUChannelArrayFormat genericFormat]
+ -[NUChannelAudioMediaFormat genericFormat]
+ -[NUChannelComponentMediaFormat genericFormat]
+ -[NUChannelComputedDataMediaFormat genericFormat]
+ -[NUChannelControlFormat optionalFormat]
+ -[NUChannelElementFormat arrayItemFormat]
+ -[NUChannelElementFormat elementChannel]
+ -[NUChannelElementFormat genericFormat]
+ -[NUChannelElementFormat isArray]
+ -[NUChannelFormat genericFormat]
+ -[NUChannelFormat isUnknown]
+ -[NUChannelFormat optionalFormat]
+ -[NUChannelGenericMediaFormat genericFormat]
+ -[NUChannelImageMediaFormat genericFormat]
+ -[NUChannelMetadataMediaFormat genericFormat]
+ -[NUChannelNullData isNull]
+ -[NUChannelOptionalFormat genericFormat]
+ -[NUChannelOptionalFormat optionalFormat]
+ -[NUClosureExpression .cxx_destruct]
+ -[NUClosureExpression compactDescription]
+ -[NUClosureExpression copyWithArguments:]
+ -[NUClosureExpression description]
+ -[NUClosureExpression evaluateWithArgumentData:format:error:]
+ -[NUClosureExpression formatWithArgumentData:error:]
+ -[NUClosureExpression hash]
+ -[NUClosureExpression initWithName:format:arguments:evaluate:]
+ -[NUClosureExpression isEqualToExpression:]
+ -[NUClosureExpression name]
+ -[NUClosureExpression nu_updateDigest:]
+ -[NUClosureExpression resultFormat]
+ -[NUCropModel cropRectFittingSize:nearCenter:]
+ -[NUFactory _evictVisionSessionIfUsed]
+ -[NUHistogramCalculator .cxx_destruct]
+ -[NUHistogramCalculator ciContext]
+ -[NUHistogramCalculator setCiContext:]
+ -[NUImageExportRequest _commonInit]
+ -[NUImageExportRequest progress]
+ -[NULivePhotoExportRequest progress]
+ -[NUOptionalDescriptor descriptorForKey:]
+ -[NUOptionalDescriptor valueForKey:data:]
+ -[NUUnknownChannelFormat canAcceptDataWithFormat:]
+ -[NUUnknownChannelFormat canSpecializeFormat:]
+ -[NUUnknownChannelFormat channelType]
+ -[NUUnknownChannelFormat hash]
+ -[NUUnknownChannelFormat isComparableToChannelFormat:]
+ -[NUUnknownChannelFormat isEqualToChannelFormat:]
+ -[NUUnknownChannelFormat isGeneric]
+ -[NUUnknownChannelFormat isUnknown]
+ -[NUUnknownChannelFormat specializedWithFormat:]
+ -[NUVectorDescriptor defaultValueType]
+ -[NUVideoCompositor maximumPendingVideoCompositionRequests]
+ -[NUVideoCompositor setMaximumPendingVideoCompositionRequests:]
+ -[NUVideoExportRequest maximumPendingVideoCompositionRequests]
+ -[NUVideoExportRequest setMaximumPendingVideoCompositionRequests:]
+ -[NUVideoExporterTrack maximumPendingVideoCompositionRequests]
+ -[NUVideoExporterTrack setMaximumPendingVideoCompositionRequests:]
+ -[_NUAsset addCapability:data:]
+ -[_NUChannelPort isElement]
+ -[_NUMapPipeline addElementOutputFormat:]
+ -[_NUMapPipeline initWithArrayFormat:]
+ -[_NUOptionalSelectorPipeline _evaluateInputsWithContext:error:]
+ -[_NUOptionalSelectorPipeline _evaluateOutputPort:context:error:]
+ -[_NUOptionalSelectorPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUOptionalSelectorPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUOptionalSelectorPipeline alias]
+ -[_NUOptionalSelectorPipeline initWithChannelFormat:]
+ -[_NUOptionalSelectorPipeline initWithChannelFormat:includeFallback:]
+ -[_NUOptionalSelectorPipeline initWithName:opaque:]
+ -[_NUOptionalSelectorPipeline isInline]
+ -[_NUPipeline _addOptionalSelectorWithInput:fallback:error:]
+ -[_NUPipeline ifNotNil:else:]
+ -[_NUPipeline ifNotNil:else:error:]
+ -[_NUPipeline insertMap:at:block:error:]
+ -[_NUPipeline insertMapAt:format:block:error:]
+ -[_NUPipeline insertMapAt:input:block:error:]
+ -[_NUPipeline insertMapWithFormat:at:block:error:]
+ -[_NUPipeline insertReduce:with:at:block:error:]
+ -[_NUPipeline insertReduceAt:arrayFormat:resultFormat:block:error:]
+ -[_NUPipeline insertReduceAt:input:initialResult:block:error:]
+ -[_NUPipeline insertReduceWithArrayFormat:resultFormat:at:block:error:]
+ -[_NUPipeline insertSwitchAt:format:unwrappingChannels:block:error:]
+ -[_NUPipeline insertSwitchAt:on:with:block:error:]
+ -[_NUPipeline insertSwitchAt:on:with:unwrappingChannels:block:error:]
+ -[_NUPipeline insertSwitchAt:on:with:unwrappingPorts:block:error:]
+ -[_NUPipeline insertUnwrapAt:withBlock:error:]
+ -[_NUPipeline mapInput:block:error:]
+ -[_NUPipeline switchOn:with:unwrappingPorts:block:]
+ -[_NUPipeline switchOn:with:unwrappingPorts:block:error:]
+ -[_NUPipeline unwrapInputs:block:]
+ -[_NUPipeline unwrapInputs:block:error:]
+ -[_NUPipeline unwrapOptional:]
+ -[_NUPipeline unwrapOptional:error:]
+ -[_NUReducePipeline initWithArrayFormat:resultFormat:]
+ -[_NUReducePipeline resultInputPort]
+ -[_NUReducePipeline resultOutputPort]
+ -[_NUSwitchPipeline _addOptionalInputChannel:]
+ -[_NUSwitchPipeline _evaluateOutputPort:context:error:]
+ -[_NUSwitchPipeline initWithSingleChannelMode:]
+ -[_NUSwitchPipeline isDynamic]
+ -[_NUTagPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUTagPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUUnwrapPipeline _addInputChannel:]
+ -[_NUUnwrapPipeline _addOutputChannel:]
+ -[_NUUnwrapPipeline _evaluateOutputPort:context:error:]
+ -[_NUUnwrapPipeline alias]
+ -[_NUUnwrapPipeline initWithName:opaque:]
+ -[_NUUnwrapPipeline init]
+ -[_NUUnwrapPipeline isDynamic]
+ -[_NUUnwrapPipeline isInline]
+ GCC_except_table10053
+ GCC_except_table10101
+ GCC_except_table10125
+ GCC_except_table10126
+ GCC_except_table10130
+ GCC_except_table10131
+ GCC_except_table10132
+ GCC_except_table10133
+ GCC_except_table10141
+ GCC_except_table10160
+ GCC_except_table10166
+ GCC_except_table10167
+ GCC_except_table10168
+ GCC_except_table10171
+ GCC_except_table10173
+ GCC_except_table10176
+ GCC_except_table10177
+ GCC_except_table10178
+ GCC_except_table10252
+ GCC_except_table10262
+ GCC_except_table10485
+ GCC_except_table10585
+ GCC_except_table10586
+ GCC_except_table10589
+ GCC_except_table10590
+ GCC_except_table10591
+ GCC_except_table10592
+ GCC_except_table10593
+ GCC_except_table10594
+ GCC_except_table10596
+ GCC_except_table10599
+ GCC_except_table10600
+ GCC_except_table10602
+ GCC_except_table10603
+ GCC_except_table10604
+ GCC_except_table10606
+ GCC_except_table10607
+ GCC_except_table10617
+ GCC_except_table10618
+ GCC_except_table10623
+ GCC_except_table10624
+ GCC_except_table10625
+ GCC_except_table10626
+ GCC_except_table10628
+ GCC_except_table10629
+ GCC_except_table10630
+ GCC_except_table10631
+ GCC_except_table10633
+ GCC_except_table10634
+ GCC_except_table10635
+ GCC_except_table10636
+ GCC_except_table10637
+ GCC_except_table10638
+ GCC_except_table10639
+ GCC_except_table10642
+ GCC_except_table10643
+ GCC_except_table10646
+ GCC_except_table10647
+ GCC_except_table10648
+ GCC_except_table10654
+ GCC_except_table10655
+ GCC_except_table10656
+ GCC_except_table10657
+ GCC_except_table10658
+ GCC_except_table10659
+ GCC_except_table10661
+ GCC_except_table10663
+ GCC_except_table10664
+ GCC_except_table10665
+ GCC_except_table10670
+ GCC_except_table10671
+ GCC_except_table10672
+ GCC_except_table10673
+ GCC_except_table10674
+ GCC_except_table10676
+ GCC_except_table10677
+ GCC_except_table10679
+ GCC_except_table10680
+ GCC_except_table10681
+ GCC_except_table10682
+ GCC_except_table10683
+ GCC_except_table10688
+ GCC_except_table10689
+ GCC_except_table10690
+ GCC_except_table10691
+ GCC_except_table10692
+ GCC_except_table10693
+ GCC_except_table10739
+ GCC_except_table10790
+ GCC_except_table1083
+ GCC_except_table10867
+ GCC_except_table10871
+ GCC_except_table11377
+ GCC_except_table11538
+ GCC_except_table11540
+ GCC_except_table11586
+ GCC_except_table11638
+ GCC_except_table11646
+ GCC_except_table11651
+ GCC_except_table11652
+ GCC_except_table11656
+ GCC_except_table1278
+ GCC_except_table1282
+ GCC_except_table1290
+ GCC_except_table1291
+ GCC_except_table1295
+ GCC_except_table1296
+ GCC_except_table1297
+ GCC_except_table1318
+ GCC_except_table1327
+ GCC_except_table1350
+ GCC_except_table1356
+ GCC_except_table1357
+ GCC_except_table1358
+ GCC_except_table1368
+ GCC_except_table1418
+ GCC_except_table1420
+ GCC_except_table1638
+ GCC_except_table1652
+ GCC_except_table1664
+ GCC_except_table1687
+ GCC_except_table1699
+ GCC_except_table1704
+ GCC_except_table173
+ GCC_except_table1794
+ GCC_except_table1797
+ GCC_except_table1806
+ GCC_except_table1831
+ GCC_except_table1856
+ GCC_except_table1857
+ GCC_except_table1923
+ GCC_except_table2049
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2052
+ GCC_except_table2053
+ GCC_except_table2055
+ GCC_except_table2080
+ GCC_except_table2133
+ GCC_except_table2243
+ GCC_except_table2244
+ GCC_except_table2720
+ GCC_except_table2800
+ GCC_except_table2944
+ GCC_except_table2956
+ GCC_except_table3119
+ GCC_except_table3266
+ GCC_except_table335
+ GCC_except_table3353
+ GCC_except_table3354
+ GCC_except_table3355
+ GCC_except_table3356
+ GCC_except_table3364
+ GCC_except_table3367
+ GCC_except_table3368
+ GCC_except_table3370
+ GCC_except_table3374
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3377
+ GCC_except_table3378
+ GCC_except_table3379
+ GCC_except_table3380
+ GCC_except_table3388
+ GCC_except_table3391
+ GCC_except_table3392
+ GCC_except_table3397
+ GCC_except_table3404
+ GCC_except_table3426
+ GCC_except_table3427
+ GCC_except_table3429
+ GCC_except_table343
+ GCC_except_table3432
+ GCC_except_table3433
+ GCC_except_table3437
+ GCC_except_table3440
+ GCC_except_table3441
+ GCC_except_table3443
+ GCC_except_table3444
+ GCC_except_table3447
+ GCC_except_table3449
+ GCC_except_table3451
+ GCC_except_table3452
+ GCC_except_table3453
+ GCC_except_table3454
+ GCC_except_table3455
+ GCC_except_table3459
+ GCC_except_table3465
+ GCC_except_table358
+ GCC_except_table398
+ GCC_except_table4031
+ GCC_except_table4102
+ GCC_except_table4106
+ GCC_except_table4108
+ GCC_except_table4248
+ GCC_except_table4256
+ GCC_except_table4257
+ GCC_except_table426
+ GCC_except_table4262
+ GCC_except_table4267
+ GCC_except_table4272
+ GCC_except_table4295
+ GCC_except_table4302
+ GCC_except_table4307
+ GCC_except_table4309
+ GCC_except_table432
+ GCC_except_table4436
+ GCC_except_table4437
+ GCC_except_table4441
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table4448
+ GCC_except_table4450
+ GCC_except_table4455
+ GCC_except_table4456
+ GCC_except_table4457
+ GCC_except_table4459
+ GCC_except_table4461
+ GCC_except_table4476
+ GCC_except_table4503
+ GCC_except_table4539
+ GCC_except_table4540
+ GCC_except_table4543
+ GCC_except_table4544
+ GCC_except_table4549
+ GCC_except_table4550
+ GCC_except_table4553
+ GCC_except_table4554
+ GCC_except_table4555
+ GCC_except_table4556
+ GCC_except_table4557
+ GCC_except_table4558
+ GCC_except_table4559
+ GCC_except_table4561
+ GCC_except_table4567
+ GCC_except_table4571
+ GCC_except_table4575
+ GCC_except_table4576
+ GCC_except_table4577
+ GCC_except_table4579
+ GCC_except_table4586
+ GCC_except_table4588
+ GCC_except_table4589
+ GCC_except_table4664
+ GCC_except_table479
+ GCC_except_table4982
+ GCC_except_table5098
+ GCC_except_table5104
+ GCC_except_table5107
+ GCC_except_table5117
+ GCC_except_table5121
+ GCC_except_table5122
+ GCC_except_table5136
+ GCC_except_table5245
+ GCC_except_table5347
+ GCC_except_table5350
+ GCC_except_table5352
+ GCC_except_table5389
+ GCC_except_table5471
+ GCC_except_table566
+ GCC_except_table5763
+ GCC_except_table5867
+ GCC_except_table5908
+ GCC_except_table593
+ GCC_except_table5946
+ GCC_except_table5948
+ GCC_except_table5953
+ GCC_except_table5962
+ GCC_except_table5967
+ GCC_except_table6013
+ GCC_except_table6079
+ GCC_except_table6081
+ GCC_except_table6082
+ GCC_except_table6087
+ GCC_except_table6088
+ GCC_except_table6121
+ GCC_except_table6123
+ GCC_except_table6125
+ GCC_except_table6126
+ GCC_except_table6132
+ GCC_except_table6134
+ GCC_except_table6137
+ GCC_except_table6140
+ GCC_except_table6141
+ GCC_except_table6142
+ GCC_except_table6143
+ GCC_except_table6148
+ GCC_except_table6149
+ GCC_except_table6155
+ GCC_except_table6156
+ GCC_except_table6161
+ GCC_except_table6162
+ GCC_except_table6163
+ GCC_except_table6165
+ GCC_except_table6166
+ GCC_except_table6167
+ GCC_except_table6168
+ GCC_except_table6169
+ GCC_except_table617
+ GCC_except_table6174
+ GCC_except_table6175
+ GCC_except_table6176
+ GCC_except_table6177
+ GCC_except_table6179
+ GCC_except_table6180
+ GCC_except_table6184
+ GCC_except_table6185
+ GCC_except_table6186
+ GCC_except_table6187
+ GCC_except_table6188
+ GCC_except_table6189
+ GCC_except_table6190
+ GCC_except_table6191
+ GCC_except_table6193
+ GCC_except_table6195
+ GCC_except_table6198
+ GCC_except_table6199
+ GCC_except_table6200
+ GCC_except_table6201
+ GCC_except_table6202
+ GCC_except_table6204
+ GCC_except_table6206
+ GCC_except_table6207
+ GCC_except_table6209
+ GCC_except_table6210
+ GCC_except_table625
+ GCC_except_table6318
+ GCC_except_table6322
+ GCC_except_table6414
+ GCC_except_table6415
+ GCC_except_table6453
+ GCC_except_table6459
+ GCC_except_table6467
+ GCC_except_table6492
+ GCC_except_table6572
+ GCC_except_table6584
+ GCC_except_table6587
+ GCC_except_table6592
+ GCC_except_table6608
+ GCC_except_table6626
+ GCC_except_table6629
+ GCC_except_table6630
+ GCC_except_table6634
+ GCC_except_table6635
+ GCC_except_table6739
+ GCC_except_table6748
+ GCC_except_table6768
+ GCC_except_table6785
+ GCC_except_table6925
+ GCC_except_table6930
+ GCC_except_table6933
+ GCC_except_table6956
+ GCC_except_table7000
+ GCC_except_table7143
+ GCC_except_table7219
+ GCC_except_table7234
+ GCC_except_table7235
+ GCC_except_table7236
+ GCC_except_table7249
+ GCC_except_table7250
+ GCC_except_table7251
+ GCC_except_table7252
+ GCC_except_table7267
+ GCC_except_table7268
+ GCC_except_table7282
+ GCC_except_table7283
+ GCC_except_table7288
+ GCC_except_table7328
+ GCC_except_table7401
+ GCC_except_table7402
+ GCC_except_table7406
+ GCC_except_table7408
+ GCC_except_table7412
+ GCC_except_table7414
+ GCC_except_table7416
+ GCC_except_table7417
+ GCC_except_table7421
+ GCC_except_table7425
+ GCC_except_table7426
+ GCC_except_table7427
+ GCC_except_table7428
+ GCC_except_table7429
+ GCC_except_table7431
+ GCC_except_table7432
+ GCC_except_table7435
+ GCC_except_table7505
+ GCC_except_table7540
+ GCC_except_table7577
+ GCC_except_table7578
+ GCC_except_table7628
+ GCC_except_table8338
+ GCC_except_table8341
+ GCC_except_table8409
+ GCC_except_table8548
+ GCC_except_table8551
+ GCC_except_table8556
+ GCC_except_table8559
+ GCC_except_table8561
+ GCC_except_table8566
+ GCC_except_table8580
+ GCC_except_table8582
+ GCC_except_table8583
+ GCC_except_table8588
+ GCC_except_table8589
+ GCC_except_table8609
+ GCC_except_table8616
+ GCC_except_table8617
+ GCC_except_table8618
+ GCC_except_table8619
+ GCC_except_table8632
+ GCC_except_table8820
+ GCC_except_table8867
+ GCC_except_table9246
+ GCC_except_table9340
+ GCC_except_table9518
+ GCC_except_table9727
+ GCC_except_table9764
+ GCC_except_table9771
+ GCC_except_table9809
+ GCC_except_table9810
+ GCC_except_table9811
+ GCC_except_table9812
+ GCC_except_table9817
+ GCC_except_table9823
+ GCC_except_table9824
+ GCC_except_table9831
+ GCC_except_table9834
+ GCC_except_table9841
+ GCC_except_table9843
+ GCC_except_table9844
+ GCC_except_table9846
+ GCC_except_table9847
+ GCC_except_table9848
+ GCC_except_table9849
+ GCC_except_table9854
+ GCC_except_table9857
+ GCC_except_table9858
+ GCC_except_table9859
+ GCC_except_table9864
+ GCC_except_table9866
+ GCC_except_table9868
+ GCC_except_table9870
+ GCC_except_table9872
+ GCC_except_table9878
+ GCC_except_table9881
+ GCC_except_table9885
+ GCC_except_table9886
+ GCC_except_table9888
+ GCC_except_table9889
+ GCC_except_table9890
+ GCC_except_table9891
+ GCC_except_table9892
+ GCC_except_table9894
+ GCC_except_table9895
+ GCC_except_table9896
+ GCC_except_table9897
+ GCC_except_table9898
+ GCC_except_table9899
+ GCC_except_table9900
+ GCC_except_table9901
+ GCC_except_table9902
+ GCC_except_table9903
+ GCC_except_table9904
+ GCC_except_table9905
+ GCC_except_table9906
+ GCC_except_table9907
+ GCC_except_table9908
+ GCC_except_table9909
+ GCC_except_table9910
+ GCC_except_table9911
+ GCC_except_table9968
+ GCC_except_table9975
+ _CIRAWDecoderVersion6
+ _CIRAWDecoderVersion6DNG
+ _CIRAWDecoderVersion7
+ _CIRAWDecoderVersion7DNG
+ _CIRAWDecoderVersion8
+ _CIRAWDecoderVersion8DNG
+ _CIRAWDecoderVersion9
+ _CIRAWDecoderVersion9DNG
+ _NUAssetOptionUseOriginalExtent
+ _NUChannelNameCondition
+ _NUChannelNameFallback
+ _NUChannelNameInput
+ _NUChannelNameOutput
+ _NUChannelNameResult
+ _NUMediaAttachmentKeyPixelFormat
+ _OBJC_CLASS_$_NUClosureExpression
+ _OBJC_CLASS_$_NUUnknownChannelFormat
+ _OBJC_CLASS_$__NUOptionalSelectorPipeline
+ _OBJC_CLASS_$__NUUnwrapPipeline
+ _OBJC_IVAR_$_NUClosureExpression._evaluate
+ _OBJC_IVAR_$_NUClosureExpression._name
+ _OBJC_IVAR_$_NUClosureExpression._resultFormat
+ _OBJC_IVAR_$_NUHistogramCalculator._ciContext
+ _OBJC_IVAR_$_NUImageExportRequest._progress
+ _OBJC_IVAR_$_NULivePhotoExportRequest._progress
+ _OBJC_IVAR_$_NUVideoCompositor._maximumPendingVideoCompositionRequests
+ _OBJC_IVAR_$_NUVideoExportRequest._maximumPendingVideoCompositionRequests
+ _OBJC_IVAR_$_NUVideoExporterTrack._maximumPendingVideoCompositionRequests
+ _OBJC_IVAR_$__NUOptionalSelectorPipeline._fallback
+ _OBJC_IVAR_$__NUReducePipeline._resultChannel
+ _OBJC_IVAR_$__NUReducePipeline._resultInputPort
+ _OBJC_IVAR_$__NUReducePipeline._resultOutputPort
+ _OBJC_IVAR_$__NUSwitchPipeline._singleMode
+ _OBJC_METACLASS_$_NUClosureExpression
+ _OBJC_METACLASS_$_NUUnknownChannelFormat
+ _OBJC_METACLASS_$__NUOptionalSelectorPipeline
+ _OBJC_METACLASS_$__NUUnwrapPipeline
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ __OBJC_$_INSTANCE_METHODS_NSArray(NUDigest|NURenderPipelineFunction|NUControlDataRepresentable)
+ __OBJC_$_INSTANCE_METHODS_NUClosureExpression
+ __OBJC_$_INSTANCE_METHODS_NUUnknownChannelFormat
+ __OBJC_$_INSTANCE_METHODS__NUOptionalSelectorPipeline
+ __OBJC_$_INSTANCE_METHODS__NUUnwrapPipeline
+ __OBJC_$_INSTANCE_VARIABLES_NUClosureExpression
+ __OBJC_$_INSTANCE_VARIABLES__NUOptionalSelectorPipeline
+ __OBJC_$_PROP_LIST_AVVideoCompositingPrivate
+ __OBJC_$_PROP_LIST_NUClosureExpression
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVVideoCompositingPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVVideoCompositingPrivate
+ __OBJC_$_PROTOCOL_REFS_AVVideoCompositingPrivate
+ __OBJC_CLASS_RO_$_NUClosureExpression
+ __OBJC_CLASS_RO_$_NUUnknownChannelFormat
+ __OBJC_CLASS_RO_$__NUOptionalSelectorPipeline
+ __OBJC_CLASS_RO_$__NUUnwrapPipeline
+ __OBJC_LABEL_PROTOCOL_$_AVVideoCompositingPrivate
+ __OBJC_METACLASS_RO_$_NUClosureExpression
+ __OBJC_METACLASS_RO_$_NUUnknownChannelFormat
+ __OBJC_METACLASS_RO_$__NUOptionalSelectorPipeline
+ __OBJC_METACLASS_RO_$__NUUnwrapPipeline
+ __OBJC_PROTOCOL_$_AVVideoCompositingPrivate
+ __ZL19NUCropClosestCenterPK15NUCropHalfPlaneDv2_dPS2_
+ ___34-[NUClosureExpression description]_block_invoke
+ ___34-[_NUPipeline unwrapInputs:block:]_block_invoke
+ ___40-[_NUPipeline unwrapInputs:block:error:]_block_invoke
+ ___41-[NUClosureExpression compactDescription]_block_invoke
+ ___44-[NUFactory _applicationWillBecomeInactive:]_block_invoke
+ ___45-[_NUPipeline insertMapAt:input:block:error:]_block_invoke
+ ___46+[NUAssetCapability rawDecodeCapabilityFormat]_block_invoke
+ ___46-[_NUPipeline insertMapAt:format:block:error:]_block_invoke
+ ___50-[_NUPipeline insertSwitchAt:on:with:block:error:]_block_invoke
+ ___51-[_NUPipeline switchOn:with:unwrappingPorts:block:]_block_invoke
+ ___62+[_NURawAssetPipeline rawDecodeVersionForAsset:options:error:]_block_invoke_2
+ ___62+[_NURawAssetPipeline rawDecodeVersionForAsset:options:error:]_block_invoke_3
+ ___62+[_NURawAssetPipeline rawDecodeVersionForAsset:options:error:]_block_invoke_4
+ ___62-[_NUPipeline insertReduceAt:input:initialResult:block:error:]_block_invoke
+ ___66-[_NUPipeline insertSwitchAt:on:with:unwrappingPorts:block:error:]_block_invoke
+ ___67-[_NUPipeline insertReduceAt:arrayFormat:resultFormat:block:error:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e64_"NSDictionary"32?0"<NUMutablePipeline>"8"NSDictionary"16^24ls32l8
+ ___block_descriptor_40_e8_32bs_e84_"NUChannelPortRef"40?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24^32ls32l8
+ ___block_descriptor_48_e8_32s40bs_e82_"<NUChannelOutputPort>"32?0"<NUMutablePipeline>"8"<NUChannelOutputPort>"16^24ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e26_v32?0"NUChannel"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e33_B24?0"<NUMutablePipeline>"8^16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e36_v32?0"NSString"8"<NUMedia>"16^B24ls32l8s40l8s48l8s56l8
+ _kCIFormat420f
+ _kCIFormat420v
+ _rawDecodeCapabilityFormat.format
+ _rawDecodeCapabilityFormat.onceToken
+ _swift_release_x28
+ _swift_retain_x26
+ _swift_retain_x27
+ _symbolic ______pSDy_____So16NUChannelPortRefCGAE______pIgggozo_ So17NUMutablePipelineP So13NUChannelNamea s5ErrorP
+ _symbolic ______pSDy_____So16NUChannelPortRefCGSAySo7NSErrorCSgGSgAESgIgggyo_ So17NUMutablePipelineP So13NUChannelNamea
+ _symbolic ______pSo16NUChannelPortRefCA2C______pIggggozo_ So17NUMutablePipelineP s5ErrorP
+ _symbolic ______pSo16NUChannelPortRefCACSAySo7NSErrorCSgGSgACSgIggggyo_ So17NUMutablePipelineP
+ _symbolic ______pSo16NUChannelPortRefCSayACGAC______pIggggozo_ So17NUMutablePipelineP s5ErrorP
+ _symbolic ______pSo16NUChannelPortRefCSayACGSAySo7NSErrorCSgGSgACSgIggggyo_ So17NUMutablePipelineP
- +[NUAssetCapability rawDecode_v6]
- +[NUAssetCapability rawDecode_v7]
- +[NUAssetCapability rawDecode_v8]
- +[NUAssetCapability rawDecode_v9]
- +[NUChannelFormat null]
- -[NSObject(NUControlDataRepresentable) nu_valueForKey:format:error:]
- -[NUChannelFormat isNull]
- -[NUChannelNullData initWithFormat:]
- -[NUChannelNullFormat canAcceptDataWithFormat:]
- -[NUChannelNullFormat channelType]
- -[NUChannelNullFormat hash]
- -[NUChannelNullFormat isComparableToChannelFormat:]
- -[NUChannelNullFormat isEqualToChannelFormat:]
- -[NUChannelNullFormat isNull]
- -[NUVideoExportRequest setProgress:]
- -[_NUMapPipeline addElementOutputChannel:]
- -[_NUMapPipeline initWithArrayChannel:]
- -[_NUReducePipeline accumulatorInputPort]
- -[_NUReducePipeline accumulatorOutputPort]
- -[_NUReducePipeline initWithArrayChannel:accumulatorChannel:]
- GCC_except_table10013
- GCC_except_table10014
- GCC_except_table10018
- GCC_except_table10019
- GCC_except_table10020
- GCC_except_table10021
- GCC_except_table10029
- GCC_except_table10038
- GCC_except_table10048
- GCC_except_table10054
- GCC_except_table10055
- GCC_except_table10056
- GCC_except_table10059
- GCC_except_table10061
- GCC_except_table10064
- GCC_except_table10065
- GCC_except_table10066
- GCC_except_table10140
- GCC_except_table10365
- GCC_except_table10366
- GCC_except_table10372
- GCC_except_table10373
- GCC_except_table10375
- GCC_except_table10376
- GCC_except_table10473
- GCC_except_table10474
- GCC_except_table10479
- GCC_except_table10480
- GCC_except_table10481
- GCC_except_table10482
- GCC_except_table10490
- GCC_except_table10491
- GCC_except_table10492
- GCC_except_table10494
- GCC_except_table10495
- GCC_except_table10505
- GCC_except_table10506
- GCC_except_table10511
- GCC_except_table10512
- GCC_except_table10513
- GCC_except_table10514
- GCC_except_table10516
- GCC_except_table10517
- GCC_except_table10518
- GCC_except_table10519
- GCC_except_table10521
- GCC_except_table10522
- GCC_except_table10523
- GCC_except_table10524
- GCC_except_table10525
- GCC_except_table10526
- GCC_except_table10527
- GCC_except_table10530
- GCC_except_table10531
- GCC_except_table10534
- GCC_except_table10535
- GCC_except_table10536
- GCC_except_table10542
- GCC_except_table10543
- GCC_except_table10544
- GCC_except_table10545
- GCC_except_table10546
- GCC_except_table10547
- GCC_except_table10549
- GCC_except_table10551
- GCC_except_table10552
- GCC_except_table10553
- GCC_except_table10558
- GCC_except_table10559
- GCC_except_table10560
- GCC_except_table10561
- GCC_except_table10562
- GCC_except_table10564
- GCC_except_table10565
- GCC_except_table10566
- GCC_except_table10567
- GCC_except_table10568
- GCC_except_table10569
- GCC_except_table10570
- GCC_except_table10571
- GCC_except_table10576
- GCC_except_table10577
- GCC_except_table10578
- GCC_except_table10579
- GCC_except_table10580
- GCC_except_table10581
- GCC_except_table10627
- GCC_except_table10755
- GCC_except_table10759
- GCC_except_table1080
- GCC_except_table11260
- GCC_except_table11421
- GCC_except_table11423
- GCC_except_table11469
- GCC_except_table11521
- GCC_except_table11529
- GCC_except_table11534
- GCC_except_table11535
- GCC_except_table11539
- GCC_except_table1275
- GCC_except_table1279
- GCC_except_table1287
- GCC_except_table1288
- GCC_except_table1289
- GCC_except_table1293
- GCC_except_table1294
- GCC_except_table1315
- GCC_except_table1324
- GCC_except_table1347
- GCC_except_table1351
- GCC_except_table1353
- GCC_except_table1355
- GCC_except_table1365
- GCC_except_table1413
- GCC_except_table1415
- GCC_except_table1632
- GCC_except_table1646
- GCC_except_table1658
- GCC_except_table1681
- GCC_except_table1693
- GCC_except_table1698
- GCC_except_table170
- GCC_except_table1788
- GCC_except_table1791
- GCC_except_table1800
- GCC_except_table1825
- GCC_except_table1850
- GCC_except_table1851
- GCC_except_table1917
- GCC_except_table2041
- GCC_except_table2042
- GCC_except_table2043
- GCC_except_table2044
- GCC_except_table2045
- GCC_except_table2047
- GCC_except_table2072
- GCC_except_table2125
- GCC_except_table2235
- GCC_except_table2236
- GCC_except_table2777
- GCC_except_table2845
- GCC_except_table2893
- GCC_except_table2905
- GCC_except_table3088
- GCC_except_table3235
- GCC_except_table3315
- GCC_except_table332
- GCC_except_table3322
- GCC_except_table3323
- GCC_except_table3324
- GCC_except_table3325
- GCC_except_table3326
- GCC_except_table3329
- GCC_except_table3330
- GCC_except_table3333
- GCC_except_table3336
- GCC_except_table3337
- GCC_except_table3339
- GCC_except_table3342
- GCC_except_table3343
- GCC_except_table3344
- GCC_except_table3345
- GCC_except_table3347
- GCC_except_table3348
- GCC_except_table3349
- GCC_except_table3366
- GCC_except_table3389
- GCC_except_table3390
- GCC_except_table3395
- GCC_except_table3396
- GCC_except_table3398
- GCC_except_table340
- GCC_except_table3401
- GCC_except_table3402
- GCC_except_table3406
- GCC_except_table3409
- GCC_except_table3410
- GCC_except_table3412
- GCC_except_table3413
- GCC_except_table3416
- GCC_except_table3418
- GCC_except_table3422
- GCC_except_table3423
- GCC_except_table3424
- GCC_except_table3428
- GCC_except_table3434
- GCC_except_table355
- GCC_except_table395
- GCC_except_table3968
- GCC_except_table4039
- GCC_except_table4043
- GCC_except_table4045
- GCC_except_table4182
- GCC_except_table4190
- GCC_except_table4191
- GCC_except_table4196
- GCC_except_table4202
- GCC_except_table4207
- GCC_except_table423
- GCC_except_table4230
- GCC_except_table4237
- GCC_except_table4242
- GCC_except_table4244
- GCC_except_table429
- GCC_except_table4371
- GCC_except_table4372
- GCC_except_table4373
- GCC_except_table4376
- GCC_except_table4377
- GCC_except_table4378
- GCC_except_table4383
- GCC_except_table4385
- GCC_except_table4390
- GCC_except_table4391
- GCC_except_table4392
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4411
- GCC_except_table4413
- GCC_except_table4474
- GCC_except_table4475
- GCC_except_table4479
- GCC_except_table4484
- GCC_except_table4485
- GCC_except_table4488
- GCC_except_table4489
- GCC_except_table4490
- GCC_except_table4491
- GCC_except_table4492
- GCC_except_table4493
- GCC_except_table4494
- GCC_except_table4496
- GCC_except_table4502
- GCC_except_table4506
- GCC_except_table4510
- GCC_except_table4511
- GCC_except_table4512
- GCC_except_table4514
- GCC_except_table4521
- GCC_except_table4523
- GCC_except_table4524
- GCC_except_table4599
- GCC_except_table476
- GCC_except_table4915
- GCC_except_table5030
- GCC_except_table5036
- GCC_except_table5039
- GCC_except_table5049
- GCC_except_table5053
- GCC_except_table5054
- GCC_except_table5068
- GCC_except_table5177
- GCC_except_table5281
- GCC_except_table5283
- GCC_except_table5285
- GCC_except_table5322
- GCC_except_table5404
- GCC_except_table563
- GCC_except_table5696
- GCC_except_table5798
- GCC_except_table5839
- GCC_except_table5875
- GCC_except_table5877
- GCC_except_table5879
- GCC_except_table5884
- GCC_except_table5893
- GCC_except_table5894
- GCC_except_table5898
- GCC_except_table590
- GCC_except_table5984
- GCC_except_table5989
- GCC_except_table6008
- GCC_except_table6010
- GCC_except_table6011
- GCC_except_table6016
- GCC_except_table6017
- GCC_except_table6019
- GCC_except_table6020
- GCC_except_table6047
- GCC_except_table6050
- GCC_except_table6051
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6054
- GCC_except_table6056
- GCC_except_table6057
- GCC_except_table6058
- GCC_except_table6061
- GCC_except_table6062
- GCC_except_table6063
- GCC_except_table6064
- GCC_except_table6065
- GCC_except_table6066
- GCC_except_table6067
- GCC_except_table6068
- GCC_except_table6069
- GCC_except_table6070
- GCC_except_table6071
- GCC_except_table6072
- GCC_except_table6077
- GCC_except_table6078
- GCC_except_table6084
- GCC_except_table6085
- GCC_except_table6092
- GCC_except_table6094
- GCC_except_table6095
- GCC_except_table6096
- GCC_except_table6097
- GCC_except_table6098
- GCC_except_table6103
- GCC_except_table6104
- GCC_except_table6106
- GCC_except_table6108
- GCC_except_table6109
- GCC_except_table6113
- GCC_except_table6114
- GCC_except_table6115
- GCC_except_table6116
- GCC_except_table6117
- GCC_except_table6119
- GCC_except_table6120
- GCC_except_table6130
- GCC_except_table614
- GCC_except_table622
- GCC_except_table6247
- GCC_except_table6251
- GCC_except_table6311
- GCC_except_table6343
- GCC_except_table6344
- GCC_except_table6388
- GCC_except_table6396
- GCC_except_table6421
- GCC_except_table6501
- GCC_except_table6513
- GCC_except_table6516
- GCC_except_table6521
- GCC_except_table6537
- GCC_except_table6555
- GCC_except_table6558
- GCC_except_table6559
- GCC_except_table6563
- GCC_except_table6564
- GCC_except_table6668
- GCC_except_table6677
- GCC_except_table6697
- GCC_except_table6714
- GCC_except_table6788
- GCC_except_table6854
- GCC_except_table6862
- GCC_except_table6885
- GCC_except_table6929
- GCC_except_table7072
- GCC_except_table7148
- GCC_except_table7163
- GCC_except_table7164
- GCC_except_table7165
- GCC_except_table7178
- GCC_except_table7179
- GCC_except_table7180
- GCC_except_table7181
- GCC_except_table7196
- GCC_except_table7197
- GCC_except_table7211
- GCC_except_table7212
- GCC_except_table7217
- GCC_except_table7257
- GCC_except_table7330
- GCC_except_table7331
- GCC_except_table7335
- GCC_except_table7337
- GCC_except_table7341
- GCC_except_table7343
- GCC_except_table7345
- GCC_except_table7346
- GCC_except_table7350
- GCC_except_table7354
- GCC_except_table7355
- GCC_except_table7356
- GCC_except_table7357
- GCC_except_table7358
- GCC_except_table7360
- GCC_except_table7361
- GCC_except_table7363
- GCC_except_table7364
- GCC_except_table7469
- GCC_except_table7506
- GCC_except_table7507
- GCC_except_table7557
- GCC_except_table8250
- GCC_except_table8253
- GCC_except_table8321
- GCC_except_table8460
- GCC_except_table8463
- GCC_except_table8468
- GCC_except_table8471
- GCC_except_table8473
- GCC_except_table8478
- GCC_except_table8492
- GCC_except_table8494
- GCC_except_table8495
- GCC_except_table8500
- GCC_except_table8501
- GCC_except_table8521
- GCC_except_table8528
- GCC_except_table8529
- GCC_except_table8530
- GCC_except_table8531
- GCC_except_table8544
- GCC_except_table8732
- GCC_except_table8779
- GCC_except_table9134
- GCC_except_table9228
- GCC_except_table9406
- GCC_except_table9600
- GCC_except_table9615
- GCC_except_table9652
- GCC_except_table9659
- GCC_except_table9697
- GCC_except_table9698
- GCC_except_table9699
- GCC_except_table9700
- GCC_except_table9705
- GCC_except_table9711
- GCC_except_table9719
- GCC_except_table9722
- GCC_except_table9729
- GCC_except_table9731
- GCC_except_table9732
- GCC_except_table9734
- GCC_except_table9735
- GCC_except_table9736
- GCC_except_table9737
- GCC_except_table9742
- GCC_except_table9744
- GCC_except_table9745
- GCC_except_table9746
- GCC_except_table9747
- GCC_except_table9751
- GCC_except_table9752
- GCC_except_table9754
- GCC_except_table9756
- GCC_except_table9758
- GCC_except_table9760
- GCC_except_table9766
- GCC_except_table9769
- GCC_except_table9773
- GCC_except_table9774
- GCC_except_table9776
- GCC_except_table9777
- GCC_except_table9778
- GCC_except_table9779
- GCC_except_table9780
- GCC_except_table9782
- GCC_except_table9783
- GCC_except_table9784
- GCC_except_table9785
- GCC_except_table9786
- GCC_except_table9787
- GCC_except_table9788
- GCC_except_table9789
- GCC_except_table9790
- GCC_except_table9791
- GCC_except_table9792
- GCC_except_table9793
- GCC_except_table9794
- GCC_except_table9795
- GCC_except_table9796
- GCC_except_table9797
- GCC_except_table9798
- GCC_except_table9799
- GCC_except_table9941
- GCC_except_table9989
- _OBJC_CLASS_$_NUChannelNullFormat
- _OBJC_IVAR_$__NUReducePipeline._accumulatorChannel
- _OBJC_IVAR_$__NUReducePipeline._accumulatorInputPort
- _OBJC_IVAR_$__NUReducePipeline._accumulatorOutputPort
- _OBJC_METACLASS_$_NUChannelNullFormat
- __OBJC_$_CLASS_METHODS_NUChannelFormat
- __OBJC_$_CLASS_PROP_LIST_NUChannelFormat
- __OBJC_$_INSTANCE_METHODS_NSArray(NUDigest|NURenderPipelineFunction)
- __OBJC_$_INSTANCE_METHODS_NUChannelNullFormat
- __OBJC_CLASS_RO_$_NUChannelNullFormat
- __OBJC_METACLASS_RO_$_NUChannelNullFormat
- ___44-[_NUPipeline reduce:withInput:block:error:]_block_invoke
- ___block_descriptor_40_e18_B16?0"NSString"8l
- ___block_descriptor_56_e8_32s40s48s_e36_v32?0"NSString"8"<NUMedia>"16^B24ls32l8s40l8s48l8
CStrings:
+ "$some"
+ "+[NUChannelData nullDataWithOptionalFormat:]"
+ "-[NUClosureExpression initWithName:format:arguments:evaluate:]"
+ "-[NUUnknownChannelFormat canSpecializeFormat:]"
+ "-[NUUnknownChannelFormat specializedWithFormat:]"
+ "-[_NUMapPipeline addElementOutputFormat:]"
+ "-[_NUMapPipeline initWithArrayFormat:]"
+ "-[_NUOptionalSelectorPipeline initWithChannelFormat:includeFallback:]"
+ "-[_NUOptionalSelectorPipeline initWithName:opaque:]"
+ "-[_NUPipeline ifNotNil:else:]"
+ "-[_NUPipeline ifNotNil:else:error:]"
+ "-[_NUPipeline insertMap:at:block:error:]"
+ "-[_NUPipeline insertMapAt:input:block:error:]"
+ "-[_NUPipeline insertMapWithFormat:at:block:error:]"
+ "-[_NUPipeline insertReduce:with:at:block:error:]"
+ "-[_NUPipeline insertReduceWithArrayFormat:resultFormat:at:block:error:]"
+ "-[_NUPipeline insertSwitchAt:format:unwrappingChannels:block:error:]"
+ "-[_NUPipeline insertSwitchAt:on:with:block:error:]"
+ "-[_NUPipeline insertSwitchAt:on:with:unwrappingChannels:block:error:]"
+ "-[_NUPipeline insertSwitchAt:on:with:unwrappingPorts:block:error:]"
+ "-[_NUPipeline insertUnwrapAt:withBlock:error:]"
+ "-[_NUPipeline switchOn:with:unwrappingPorts:block:]"
+ "-[_NUPipeline unwrapInputs:block:]"
+ "-[_NUPipeline unwrapInputs:block:error:]"
+ "-[_NUPipeline unwrapOptional:]"
+ "-[_NUPipeline unwrapOptional:error:]"
+ "-[_NUReducePipeline initWithArrayFormat:resultFormat:]"
+ "-[_NUSwitchPipeline _addOptionalInputChannel:]"
+ "-[_NUSwitchPipeline _evaluateOutputPort:context:error:]"
+ "-[_NUUnwrapPipeline _evaluateOutputPort:context:error:]"
+ "-[_NUUnwrapPipeline initWithName:opaque:]"
+ "8"
+ "@\"NSDictionary\"32@?0@\"<NUMutablePipeline>\"8@\"NSDictionary\"16^@24"
+ "@\"NUChannelPortRef\"40@?0@\"<NUMutablePipeline>\"8@\"NUChannelPortRef\"16@\"NSArray\"24^@32"
+ "Cannot add an element input channel"
+ "Cannot add an element output channel"
+ "Cannot unwrap a channel named after the switch's own"
+ "Crop rect should be known at evaluation time"
+ "Failed to add ifNotNil/else pipeline: %@"
+ "Failed to add switch input"
+ "Failed to add switch output"
+ "Failed to add switch unwrapped input"
+ "Failed to add unwrap input"
+ "Failed to add unwrap pipeline: %@"
+ "Failed to add unwrapOptional pipeline: %@"
+ "Failed to build unwrap pipeline"
+ "Failed to connect optional selector pipeline"
+ "Failed to connect unwrap input"
+ "Failed to evaluate fallback input"
+ "Failed to evaluate optional input"
+ "Failed to insert map pipeline"
+ "Failed to insert reduce pipeline"
+ "Failed to insert switch pipeline"
+ "Failed to insert unwrap pipeline"
+ "Failed to resolve port to unwrap"
+ "Failed to resolve unwrap input"
+ "Failed to unwrap optional input"
+ "Fallback input is null"
+ "Missing switch input port"
+ "Missing unwrap input port"
+ "Missing unwrapped input port"
+ "NUHistogramCalculator"
+ "Not an array format"
+ "Output channel cannot be optional"
+ "Unexpected custom compositor %{public}@, leaving the composition request depth alone"
+ "Unwrap has no input to unwrap"
+ "Unwrap input is not optional"
+ "Value is not a collection"
+ "YCC8f420"
+ "YCC8v420"
+ "[channel.name isEqualToString:NUChannelNameOutput]"
+ "arrayFormat != nil"
+ "arrayFormat.isArray"
+ "arrayFormat.isOptional == NO"
+ "closure"
+ "closure<%@,%@>"
+ "elementFormat != nil"
+ "evaluate != nil"
+ "fallback"
+ "fallback != nil"
+ "format.isOptional"
+ "optionalInput != nil"
+ "optionalInputs != nil"
+ "optionalSelector"
+ "ports != nil"
+ "result"
+ "resultFormat != nil"
+ "s!"
+ "s?"
+ "u"
+ "unwrap"
+ "unwrapped%lu"
+ "v32@?0@\"NUChannel\"8Q16^B24"
- "-[NUChannelNullData initWithFormat:]"
- "-[_NUMapPipeline addElementOutputChannel:]"
- "-[_NUMapPipeline initWithArrayChannel:]"
- "-[_NUPipeline map:block:error:]"
- "-[_NUPipeline reduce:with:block:error:]"
- "-[_NUReducePipeline initWithArrayChannel:accumulatorChannel:]"
- "Duplicate input name"
- "Duplicate input name: %@"
- "Failed to reduce"
- "Unsupported RAW decoder version: %{public}@, ignored."
- "accumulatorChannel != nil"
- "arrayChannel != nil"
- "arrayChannel.format.isArray"
- "elementChannel != nil"
- "rawDecode_v6"
- "rawDecode_v7"
- "rawDecode_v8"
- "rawDecode_v9"
```

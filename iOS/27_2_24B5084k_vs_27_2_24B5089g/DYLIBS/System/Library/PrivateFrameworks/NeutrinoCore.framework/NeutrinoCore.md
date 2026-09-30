## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-916.40.110.0.0
-  __TEXT.__text: 0x313370
-  __TEXT.__objc_methlist: 0x20f14
+916.45.110.0.0
+  __TEXT.__text: 0x3159a4
+  __TEXT.__objc_methlist: 0x21104
   __TEXT.__const: 0x2798
   __TEXT.__dlopen_cstrs: 0x45
   __TEXT.__swift5_typeref: 0x3c9

   __TEXT.__swift5_fieldmd: 0x15c
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x3e92e
-  __TEXT.__swift5_capture: 0x230
-  __TEXT.__gcc_except_tab: 0x8150
+  __TEXT.__cstring: 0x3ec2e
+  __TEXT.__swift5_capture: 0x1f0
+  __TEXT.__gcc_except_tab: 0x813c
   __TEXT.__oslogstring: 0x58ae
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0xa1d0
-  __TEXT.__eh_frame: 0x478
+  __TEXT.__unwind_info: 0xa238
+  __TEXT.__eh_frame: 0x418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4050
-  __DATA_CONST.__objc_classlist: 0x15f8
+  __DATA_CONST.__const: 0x4010
+  __DATA_CONST.__objc_classlist: 0x1600
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb6b0
+  __DATA_CONST.__objc_selrefs: 0xb718
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1010
+  __DATA_CONST.__objc_superrefs: 0x1018
   __DATA_CONST.__objc_arraydata: 0xae0
   __DATA_CONST.__got: 0x2270
-  __AUTH_CONST.__const: 0x4f50
-  __AUTH_CONST.__cfstring: 0x1d060
-  __AUTH_CONST.__objc_const: 0x37770
+  __AUTH_CONST.__const: 0x4e60
+  __AUTH_CONST.__cfstring: 0x1d020
+  __AUTH_CONST.__objc_const: 0x37a10
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_dictobj: 0x348

   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x1a50
-  __DATA.__data: 0x3938
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1a7c
+  __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__objc_data: 0xd8e0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__objc_data: 0xdbb0
+  __DATA_DIRTY.__data: 0x3780
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11910
-  Symbols:   25634
-  CStrings:  7288
+  Functions: 11937
+  Symbols:   25704
+  CStrings:  7304
 
Symbols:
+ +[NUPipelineFactory buildPipelineWithBuilder:]
+ +[NUPipelineFactory computePipelineWithProcessorName:bundleIdentifier:error:]
+ +[NUPipelineFactory metadataPipelineWithProcessorName:bundleIdentifier:error:]
+ +[NUPipelineFactory renderPipelineWithProcessorName:bundleIdentifier:error:]
+ +[NUPipelineProcessor processorWithName:bundleIdentifier:error:]
+ -[NUArrayDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUChannelControlFormat isOptional]
+ -[NUChannelControlFormat nonOptionalFormat]
+ -[NUChannelFormat isOptional]
+ -[NUChannelFormat nonOptionalFormat]
+ -[NUChannelOptionalFormat .cxx_destruct]
+ -[NUChannelOptionalFormat arrayItemFormat]
+ -[NUChannelOptionalFormat canAcceptDataWithFormat:]
+ -[NUChannelOptionalFormat canSpecializeFormat:]
+ -[NUChannelOptionalFormat channelType]
+ -[NUChannelOptionalFormat debugDescription]
+ -[NUChannelOptionalFormat description]
+ -[NUChannelOptionalFormat elementChannel]
+ -[NUChannelOptionalFormat hash]
+ -[NUChannelOptionalFormat initWithWrappedFormat:]
+ -[NUChannelOptionalFormat init]
+ -[NUChannelOptionalFormat isArray]
+ -[NUChannelOptionalFormat isComparableToChannelFormat:]
+ -[NUChannelOptionalFormat isComputedData]
+ -[NUChannelOptionalFormat isEqualToChannelFormat:]
+ -[NUChannelOptionalFormat isEqualToOptionalFormat:]
+ -[NUChannelOptionalFormat isGeneric]
+ -[NUChannelOptionalFormat isOptional]
+ -[NUChannelOptionalFormat nonOptionalFormat]
+ -[NUChannelOptionalFormat requiresSubchannelDataForKey:]
+ -[NUChannelOptionalFormat specializedWithFormat:]
+ -[NUChannelOptionalFormat subchannelFormatForKey:]
+ -[NUChannelOptionalFormat subchannelKeys]
+ -[NUChannelOptionalFormat wrappedFormat]
+ -[NUCompoundDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUControlDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUControlDescriptor nonOptionalDescriptor]
+ -[NUCoreImageFilterPipelineProcessor copyWithZone:]
+ -[NUEnumDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUExpressionComputeProcessor copyWithZone:]
+ -[NUFaceDetectionPipelineProcessor copyWithZone:]
+ -[NUNumberDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUOptionalDescriptor initWithDescriptor:validatedDefaultValue:]
+ -[NUOptionalDescriptor isOptional]
+ -[NUOptionalDescriptor nonOptionalDescriptor]
+ -[NUPipelineProcessor copyWithZone:]
+ -[NUPipelineProcessorCache processorForConfiguration:processor:controlData:error:]
+ -[NUVectorDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[_NUHDRColorVolumePipeline .cxx_destruct]
+ -[_NUHDRColorVolumePipeline build:]
+ -[_NUHDRGainMapApplyPipeline .cxx_destruct]
+ -[_NUHDRGainMapComputePipeline .cxx_destruct]
+ -[_NUHDRGainMapComputePipeline build:]
+ -[_NUMapPipeline .cxx_destruct]
+ -[_NUMapPipeline addElementOutputChannel:]
+ -[_NUMapPipeline elementInputPort]
+ -[_NUMapPipeline initWithArrayChannel:]
+ -[_NUPipeline addPipelineWithBuilder:]
+ -[_NUReducePipeline .cxx_destruct]
+ -[_NUReducePipeline accumulatorInputPort]
+ -[_NUReducePipeline accumulatorOutputPort]
+ -[_NUReducePipeline elementInputPort]
+ -[_NUReducePipeline initWithArrayChannel:accumulatorChannel:]
+ GCC_except_table10013
+ GCC_except_table10014
+ GCC_except_table10021
+ GCC_except_table10038
+ GCC_except_table10048
+ GCC_except_table10054
+ GCC_except_table10055
+ GCC_except_table10056
+ GCC_except_table10059
+ GCC_except_table10061
+ GCC_except_table10064
+ GCC_except_table10065
+ GCC_except_table10066
+ GCC_except_table10140
+ GCC_except_table10150
+ GCC_except_table10365
+ GCC_except_table10366
+ GCC_except_table10372
+ GCC_except_table10373
+ GCC_except_table10375
+ GCC_except_table10376
+ GCC_except_table10473
+ GCC_except_table10474
+ GCC_except_table10479
+ GCC_except_table10484
+ GCC_except_table10492
+ GCC_except_table10505
+ GCC_except_table10512
+ GCC_except_table10514
+ GCC_except_table10518
+ GCC_except_table10519
+ GCC_except_table10521
+ GCC_except_table10527
+ GCC_except_table10536
+ GCC_except_table10546
+ GCC_except_table10547
+ GCC_except_table10549
+ GCC_except_table10551
+ GCC_except_table10552
+ GCC_except_table10553
+ GCC_except_table10558
+ GCC_except_table10559
+ GCC_except_table10560
+ GCC_except_table10561
+ GCC_except_table10562
+ GCC_except_table10564
+ GCC_except_table10565
+ GCC_except_table10566
+ GCC_except_table10567
+ GCC_except_table10568
+ GCC_except_table10569
+ GCC_except_table10570
+ GCC_except_table10571
+ GCC_except_table10576
+ GCC_except_table10577
+ GCC_except_table10578
+ GCC_except_table10579
+ GCC_except_table10580
+ GCC_except_table10581
+ GCC_except_table10627
+ GCC_except_table10678
+ GCC_except_table10755
+ GCC_except_table10759
+ GCC_except_table11260
+ GCC_except_table11421
+ GCC_except_table11423
+ GCC_except_table11469
+ GCC_except_table11521
+ GCC_except_table11529
+ GCC_except_table11534
+ GCC_except_table11535
+ GCC_except_table11539
+ GCC_except_table2125
+ GCC_except_table2777
+ GCC_except_table2845
+ GCC_except_table2893
+ GCC_except_table2905
+ GCC_except_table3088
+ GCC_except_table3235
+ GCC_except_table3322
+ GCC_except_table3323
+ GCC_except_table3324
+ GCC_except_table3325
+ GCC_except_table3326
+ GCC_except_table3330
+ GCC_except_table3336
+ GCC_except_table3337
+ GCC_except_table3339
+ GCC_except_table3342
+ GCC_except_table3343
+ GCC_except_table3344
+ GCC_except_table3346
+ GCC_except_table3347
+ GCC_except_table3348
+ GCC_except_table3349
+ GCC_except_table3357
+ GCC_except_table3360
+ GCC_except_table3366
+ GCC_except_table3389
+ GCC_except_table3398
+ GCC_except_table3401
+ GCC_except_table3402
+ GCC_except_table3409
+ GCC_except_table3410
+ GCC_except_table3412
+ GCC_except_table3413
+ GCC_except_table3416
+ GCC_except_table3418
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3422
+ GCC_except_table3423
+ GCC_except_table3424
+ GCC_except_table3428
+ GCC_except_table3434
+ GCC_except_table3968
+ GCC_except_table4039
+ GCC_except_table4043
+ GCC_except_table4045
+ GCC_except_table4190
+ GCC_except_table4191
+ GCC_except_table4196
+ GCC_except_table4202
+ GCC_except_table4207
+ GCC_except_table4230
+ GCC_except_table4237
+ GCC_except_table4242
+ GCC_except_table4244
+ GCC_except_table4372
+ GCC_except_table4373
+ GCC_except_table4376
+ GCC_except_table4377
+ GCC_except_table4378
+ GCC_except_table4383
+ GCC_except_table4385
+ GCC_except_table4390
+ GCC_except_table4391
+ GCC_except_table4392
+ GCC_except_table4394
+ GCC_except_table4396
+ GCC_except_table4411
+ GCC_except_table4438
+ GCC_except_table4474
+ GCC_except_table4475
+ GCC_except_table4478
+ GCC_except_table4479
+ GCC_except_table4484
+ GCC_except_table4488
+ GCC_except_table4490
+ GCC_except_table4491
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4494
+ GCC_except_table4502
+ GCC_except_table4506
+ GCC_except_table4510
+ GCC_except_table4511
+ GCC_except_table4512
+ GCC_except_table4514
+ GCC_except_table4521
+ GCC_except_table4523
+ GCC_except_table4524
+ GCC_except_table4599
+ GCC_except_table4915
+ GCC_except_table5030
+ GCC_except_table5036
+ GCC_except_table5039
+ GCC_except_table5049
+ GCC_except_table5053
+ GCC_except_table5054
+ GCC_except_table5068
+ GCC_except_table5177
+ GCC_except_table5281
+ GCC_except_table5283
+ GCC_except_table5285
+ GCC_except_table5322
+ GCC_except_table5404
+ GCC_except_table5696
+ GCC_except_table5798
+ GCC_except_table5839
+ GCC_except_table5875
+ GCC_except_table5877
+ GCC_except_table5879
+ GCC_except_table5884
+ GCC_except_table5893
+ GCC_except_table5894
+ GCC_except_table5898
+ GCC_except_table5944
+ GCC_except_table5963
+ GCC_except_table5984
+ GCC_except_table5989
+ GCC_except_table6008
+ GCC_except_table6010
+ GCC_except_table6011
+ GCC_except_table6016
+ GCC_except_table6017
+ GCC_except_table6019
+ GCC_except_table6020
+ GCC_except_table6034
+ GCC_except_table6050
+ GCC_except_table6051
+ GCC_except_table6054
+ GCC_except_table6055
+ GCC_except_table6056
+ GCC_except_table6057
+ GCC_except_table6058
+ GCC_except_table6061
+ GCC_except_table6062
+ GCC_except_table6063
+ GCC_except_table6064
+ GCC_except_table6068
+ GCC_except_table6077
+ GCC_except_table6085
+ GCC_except_table6096
+ GCC_except_table6098
+ GCC_except_table6109
+ GCC_except_table6115
+ GCC_except_table6116
+ GCC_except_table6117
+ GCC_except_table6118
+ GCC_except_table6119
+ GCC_except_table6120
+ GCC_except_table6122
+ GCC_except_table6124
+ GCC_except_table6127
+ GCC_except_table6128
+ GCC_except_table6129
+ GCC_except_table6130
+ GCC_except_table6131
+ GCC_except_table6133
+ GCC_except_table6135
+ GCC_except_table6136
+ GCC_except_table6138
+ GCC_except_table6139
+ GCC_except_table6247
+ GCC_except_table6251
+ GCC_except_table6311
+ GCC_except_table6343
+ GCC_except_table6344
+ GCC_except_table6382
+ GCC_except_table6388
+ GCC_except_table6421
+ GCC_except_table6501
+ GCC_except_table6513
+ GCC_except_table6516
+ GCC_except_table6521
+ GCC_except_table6537
+ GCC_except_table6555
+ GCC_except_table6558
+ GCC_except_table6559
+ GCC_except_table6563
+ GCC_except_table6564
+ GCC_except_table6668
+ GCC_except_table6677
+ GCC_except_table6697
+ GCC_except_table6714
+ GCC_except_table6788
+ GCC_except_table6854
+ GCC_except_table6859
+ GCC_except_table6862
+ GCC_except_table6885
+ GCC_except_table6929
+ GCC_except_table7072
+ GCC_except_table7148
+ GCC_except_table7163
+ GCC_except_table7164
+ GCC_except_table7165
+ GCC_except_table7178
+ GCC_except_table7179
+ GCC_except_table7180
+ GCC_except_table7181
+ GCC_except_table7196
+ GCC_except_table7197
+ GCC_except_table7211
+ GCC_except_table7212
+ GCC_except_table7217
+ GCC_except_table7257
+ GCC_except_table7341
+ GCC_except_table7343
+ GCC_except_table7345
+ GCC_except_table7346
+ GCC_except_table7350
+ GCC_except_table7354
+ GCC_except_table7355
+ GCC_except_table7356
+ GCC_except_table7357
+ GCC_except_table7358
+ GCC_except_table7360
+ GCC_except_table7361
+ GCC_except_table7363
+ GCC_except_table7364
+ GCC_except_table7434
+ GCC_except_table7469
+ GCC_except_table7506
+ GCC_except_table7507
+ GCC_except_table7557
+ GCC_except_table8250
+ GCC_except_table8253
+ GCC_except_table8321
+ GCC_except_table8460
+ GCC_except_table8463
+ GCC_except_table8471
+ GCC_except_table8473
+ GCC_except_table8478
+ GCC_except_table8492
+ GCC_except_table8494
+ GCC_except_table8500
+ GCC_except_table8501
+ GCC_except_table8521
+ GCC_except_table8528
+ GCC_except_table8529
+ GCC_except_table8530
+ GCC_except_table8531
+ GCC_except_table8544
+ GCC_except_table8732
+ GCC_except_table8779
+ GCC_except_table9134
+ GCC_except_table9228
+ GCC_except_table9406
+ GCC_except_table9600
+ GCC_except_table9615
+ GCC_except_table9652
+ GCC_except_table9659
+ GCC_except_table9697
+ GCC_except_table9705
+ GCC_except_table9712
+ GCC_except_table9719
+ GCC_except_table9729
+ GCC_except_table9731
+ GCC_except_table9732
+ GCC_except_table9734
+ GCC_except_table9735
+ GCC_except_table9736
+ GCC_except_table9745
+ GCC_except_table9766
+ GCC_except_table9769
+ GCC_except_table9773
+ GCC_except_table9774
+ GCC_except_table9776
+ GCC_except_table9777
+ GCC_except_table9778
+ GCC_except_table9779
+ GCC_except_table9780
+ GCC_except_table9782
+ GCC_except_table9783
+ GCC_except_table9784
+ GCC_except_table9785
+ GCC_except_table9786
+ GCC_except_table9787
+ GCC_except_table9788
+ GCC_except_table9789
+ GCC_except_table9790
+ GCC_except_table9791
+ GCC_except_table9792
+ GCC_except_table9793
+ GCC_except_table9794
+ GCC_except_table9795
+ GCC_except_table9796
+ GCC_except_table9797
+ GCC_except_table9798
+ GCC_except_table9799
+ GCC_except_table9856
+ GCC_except_table9863
+ GCC_except_table9941
+ GCC_except_table9989
+ _OBJC_CLASS_$_NUChannelOptionalFormat
+ _OBJC_IVAR_$_NUChannelOptionalFormat._wrappedFormat
+ _OBJC_IVAR_$__NUHDRColorVolumePipeline._filterProcessor
+ _OBJC_IVAR_$__NUHDRGainMapApplyPipeline._filterProcessor
+ _OBJC_IVAR_$__NUHDRGainMapComputePipeline._filterProcessor
+ _OBJC_IVAR_$__NUMapPipeline._arrayChannel
+ _OBJC_IVAR_$__NUMapPipeline._elementInputPort
+ _OBJC_IVAR_$__NUReducePipeline._accumulatorChannel
+ _OBJC_IVAR_$__NUReducePipeline._accumulatorInputPort
+ _OBJC_IVAR_$__NUReducePipeline._accumulatorOutputPort
+ _OBJC_IVAR_$__NUReducePipeline._arrayChannel
+ _OBJC_IVAR_$__NUReducePipeline._elementInputPort
+ _OBJC_METACLASS_$_NUChannelOptionalFormat
+ __OBJC_$_INSTANCE_METHODS_NUChannelOptionalFormat
+ __OBJC_$_INSTANCE_VARIABLES_NUChannelOptionalFormat
+ __OBJC_$_INSTANCE_VARIABLES__NUHDRColorVolumePipeline
+ __OBJC_$_INSTANCE_VARIABLES__NUHDRGainMapApplyPipeline
+ __OBJC_$_INSTANCE_VARIABLES__NUMapPipeline
+ __OBJC_$_INSTANCE_VARIABLES__NUReducePipeline
+ __OBJC_$_PROP_LIST_NUChannelOptionalFormat
+ __OBJC_$_PROP_LIST__NUMapPipeline
+ __OBJC_$_PROP_LIST__NUReducePipeline
+ __OBJC_CLASS_PROTOCOLS_$_NUPipelineProcessor
+ __OBJC_CLASS_RO_$_NUChannelOptionalFormat
+ __OBJC_METACLASS_RO_$_NUChannelOptionalFormat
+ ___64+[NUPipelineProcessor processorWithName:bundleIdentifier:error:]_block_invoke
+ ___82-[NUPipelineProcessorCache processorForConfiguration:processor:controlData:error:]_block_invoke
+ _objc_msgSend$accumulatorInputPort
+ _objc_msgSend$accumulatorOutputPort
+ _objc_msgSend$addElementOutputChannel:
+ _objc_msgSend$addPipelineWithBuilder:error:
+ _objc_msgSend$canAcceptDataWithNonOptionalDescriptor:
+ _objc_msgSend$elementInputPort
+ _objc_msgSend$initWithArrayChannel:
+ _objc_msgSend$initWithArrayChannel:accumulatorChannel:
+ _objc_msgSend$initWithDescriptor:validatedDefaultValue:
+ _objc_msgSend$initWithWrappedFormat:
+ _objc_msgSend$isEqualToOptionalFormat:
+ _objc_msgSend$nonOptionalDescriptor
+ _objc_msgSend$nonOptionalFormat
+ _objc_msgSend$processorForConfiguration:processor:controlData:error:
+ _objc_msgSend$processorWithName:bundleIdentifier:error:
+ _objc_msgSend$wrappedFormat
- +[NUPipelineFactory computePipelineWithProcessorIdentifier:error:]
- +[NUPipelineFactory metadataPipelineWithProcessorIdentifier:error:]
- +[NUPipelineFactory renderPipelineWithProcessorIdentifier:error:]
- +[NUPipelineProcessor identifier]
- +[NUPipelineProcessor processorWithIdentifier:error:]
- -[NUArrayDescriptor canAcceptDataWithDescriptor:]
- -[NUCompoundDescriptor canAcceptDataWithDescriptor:]
- -[NUCoreImageFilterPipelineProcessor identifier]
- -[NUEnumDescriptor canAcceptDataWithDescriptor:]
- -[NUNumberDescriptor canAcceptDataWithDescriptor:]
- -[NUPipelineProcessor identifier]
- -[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]
- -[NUVectorDescriptor canAcceptDataWithDescriptor:]
- -[_NUMapPipeline _addInputChannel:]
- -[_NUMapPipeline _addOutputChannel:]
- -[_NUMapPipeline init]
- -[_NUPipeline addMapPipeline:error:]
- -[_NUPipeline addReducePipeline:error:]
- -[_NUReducePipeline _addInputChannel:]
- -[_NUReducePipeline init]
- GCC_except_table10002
- GCC_except_table10012
- GCC_except_table10023
- GCC_except_table10025
- GCC_except_table10028
- GCC_except_table10030
- GCC_except_table10104
- GCC_except_table10114
- GCC_except_table10329
- GCC_except_table10330
- GCC_except_table10336
- GCC_except_table10337
- GCC_except_table10339
- GCC_except_table10340
- GCC_except_table10437
- GCC_except_table10438
- GCC_except_table10441
- GCC_except_table10442
- GCC_except_table10443
- GCC_except_table10444
- GCC_except_table10445
- GCC_except_table10446
- GCC_except_table10448
- GCC_except_table10451
- GCC_except_table10452
- GCC_except_table10454
- GCC_except_table10455
- GCC_except_table10456
- GCC_except_table10458
- GCC_except_table10459
- GCC_except_table10469
- GCC_except_table10470
- GCC_except_table10475
- GCC_except_table10476
- GCC_except_table10483
- GCC_except_table10485
- GCC_except_table10486
- GCC_except_table10489
- GCC_except_table10498
- GCC_except_table10499
- GCC_except_table10500
- GCC_except_table10507
- GCC_except_table10508
- GCC_except_table10509
- GCC_except_table10510
- GCC_except_table10515
- GCC_except_table10528
- GCC_except_table10529
- GCC_except_table10532
- GCC_except_table10533
- GCC_except_table10540
- GCC_except_table10541
- GCC_except_table10591
- GCC_except_table10642
- GCC_except_table10719
- GCC_except_table10723
- GCC_except_table11219
- GCC_except_table11380
- GCC_except_table11382
- GCC_except_table11428
- GCC_except_table11480
- GCC_except_table11488
- GCC_except_table11493
- GCC_except_table11494
- GCC_except_table11498
- GCC_except_table2126
- GCC_except_table2774
- GCC_except_table2840
- GCC_except_table2888
- GCC_except_table2900
- GCC_except_table3060
- GCC_except_table3207
- GCC_except_table3287
- GCC_except_table3294
- GCC_except_table3295
- GCC_except_table3296
- GCC_except_table3297
- GCC_except_table3298
- GCC_except_table3301
- GCC_except_table3302
- GCC_except_table3305
- GCC_except_table3308
- GCC_except_table3309
- GCC_except_table3311
- GCC_except_table3314
- GCC_except_table3316
- GCC_except_table3317
- GCC_except_table3318
- GCC_except_table3319
- GCC_except_table3320
- GCC_except_table3321
- GCC_except_table3332
- GCC_except_table3338
- GCC_except_table3362
- GCC_except_table3367
- GCC_except_table3368
- GCC_except_table3370
- GCC_except_table3374
- GCC_except_table3378
- GCC_except_table3381
- GCC_except_table3382
- GCC_except_table3384
- GCC_except_table3385
- GCC_except_table3388
- GCC_except_table3392
- GCC_except_table3393
- GCC_except_table3394
- GCC_except_table3400
- GCC_except_table3759
- GCC_except_table3945
- GCC_except_table4014
- GCC_except_table4018
- GCC_except_table4020
- GCC_except_table4157
- GCC_except_table4165
- GCC_except_table4166
- GCC_except_table4171
- GCC_except_table4177
- GCC_except_table4205
- GCC_except_table4212
- GCC_except_table4217
- GCC_except_table4219
- GCC_except_table4346
- GCC_except_table4347
- GCC_except_table4348
- GCC_except_table4351
- GCC_except_table4352
- GCC_except_table4353
- GCC_except_table4358
- GCC_except_table4360
- GCC_except_table4365
- GCC_except_table4366
- GCC_except_table4367
- GCC_except_table4369
- GCC_except_table4386
- GCC_except_table4388
- GCC_except_table4449
- GCC_except_table4450
- GCC_except_table4453
- GCC_except_table4454
- GCC_except_table4459
- GCC_except_table4460
- GCC_except_table4463
- GCC_except_table4464
- GCC_except_table4465
- GCC_except_table4466
- GCC_except_table4467
- GCC_except_table4468
- GCC_except_table4469
- GCC_except_table4471
- GCC_except_table4477
- GCC_except_table4481
- GCC_except_table4486
- GCC_except_table4487
- GCC_except_table4498
- GCC_except_table4499
- GCC_except_table4574
- GCC_except_table4890
- GCC_except_table5005
- GCC_except_table5011
- GCC_except_table5014
- GCC_except_table5024
- GCC_except_table5028
- GCC_except_table5029
- GCC_except_table5043
- GCC_except_table5152
- GCC_except_table5256
- GCC_except_table5258
- GCC_except_table5260
- GCC_except_table5297
- GCC_except_table5379
- GCC_except_table5671
- GCC_except_table5773
- GCC_except_table5814
- GCC_except_table5850
- GCC_except_table5852
- GCC_except_table5854
- GCC_except_table5859
- GCC_except_table5868
- GCC_except_table5869
- GCC_except_table5873
- GCC_except_table5919
- GCC_except_table5938
- GCC_except_table5959
- GCC_except_table5964
- GCC_except_table5983
- GCC_except_table5985
- GCC_except_table5986
- GCC_except_table5991
- GCC_except_table5992
- GCC_except_table5994
- GCC_except_table5995
- GCC_except_table6009
- GCC_except_table6022
- GCC_except_table6025
- GCC_except_table6026
- GCC_except_table6027
- GCC_except_table6028
- GCC_except_table6029
- GCC_except_table6030
- GCC_except_table6031
- GCC_except_table6032
- GCC_except_table6033
- GCC_except_table6035
- GCC_except_table6036
- GCC_except_table6037
- GCC_except_table6038
- GCC_except_table6039
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table6042
- GCC_except_table6043
- GCC_except_table6044
- GCC_except_table6045
- GCC_except_table6046
- GCC_except_table6059
- GCC_except_table6073
- GCC_except_table6079
- GCC_except_table6080
- GCC_except_table6081
- GCC_except_table6083
- GCC_except_table6088
- GCC_except_table6089
- GCC_except_table6093
- GCC_except_table6099
- GCC_except_table6102
- GCC_except_table6110
- GCC_except_table6111
- GCC_except_table6222
- GCC_except_table6226
- GCC_except_table6286
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table6357
- GCC_except_table6363
- GCC_except_table6371
- GCC_except_table6476
- GCC_except_table6488
- GCC_except_table6491
- GCC_except_table6496
- GCC_except_table6512
- GCC_except_table6530
- GCC_except_table6533
- GCC_except_table6534
- GCC_except_table6538
- GCC_except_table6539
- GCC_except_table6643
- GCC_except_table6652
- GCC_except_table6672
- GCC_except_table6689
- GCC_except_table6763
- GCC_except_table6829
- GCC_except_table6834
- GCC_except_table6837
- GCC_except_table6860
- GCC_except_table6904
- GCC_except_table7047
- GCC_except_table7122
- GCC_except_table7137
- GCC_except_table7138
- GCC_except_table7139
- GCC_except_table7152
- GCC_except_table7153
- GCC_except_table7154
- GCC_except_table7155
- GCC_except_table7170
- GCC_except_table7171
- GCC_except_table7185
- GCC_except_table7186
- GCC_except_table7191
- GCC_except_table7231
- GCC_except_table7304
- GCC_except_table7305
- GCC_except_table7309
- GCC_except_table7311
- GCC_except_table7315
- GCC_except_table7317
- GCC_except_table7319
- GCC_except_table7320
- GCC_except_table7324
- GCC_except_table7328
- GCC_except_table7329
- GCC_except_table7332
- GCC_except_table7334
- GCC_except_table7338
- GCC_except_table7408
- GCC_except_table7443
- GCC_except_table7480
- GCC_except_table7481
- GCC_except_table7531
- GCC_except_table8224
- GCC_except_table8227
- GCC_except_table8295
- GCC_except_table8434
- GCC_except_table8437
- GCC_except_table8442
- GCC_except_table8445
- GCC_except_table8447
- GCC_except_table8452
- GCC_except_table8466
- GCC_except_table8469
- GCC_except_table8474
- GCC_except_table8475
- GCC_except_table8502
- GCC_except_table8503
- GCC_except_table8504
- GCC_except_table8505
- GCC_except_table8518
- GCC_except_table8706
- GCC_except_table8753
- GCC_except_table9098
- GCC_except_table9192
- GCC_except_table9370
- GCC_except_table9564
- GCC_except_table9579
- GCC_except_table9616
- GCC_except_table9623
- GCC_except_table9661
- GCC_except_table9662
- GCC_except_table9663
- GCC_except_table9664
- GCC_except_table9669
- GCC_except_table9675
- GCC_except_table9676
- GCC_except_table9683
- GCC_except_table9686
- GCC_except_table9693
- GCC_except_table9695
- GCC_except_table9696
- GCC_except_table9701
- GCC_except_table9706
- GCC_except_table9708
- GCC_except_table9709
- GCC_except_table9710
- GCC_except_table9715
- GCC_except_table9716
- GCC_except_table9718
- GCC_except_table9720
- GCC_except_table9724
- GCC_except_table9730
- GCC_except_table9733
- GCC_except_table9738
- GCC_except_table9740
- GCC_except_table9741
- GCC_except_table9743
- GCC_except_table9748
- GCC_except_table9749
- GCC_except_table9750
- GCC_except_table9753
- GCC_except_table9755
- GCC_except_table9757
- GCC_except_table9759
- GCC_except_table9761
- GCC_except_table9762
- GCC_except_table9763
- GCC_except_table9820
- GCC_except_table9827
- GCC_except_table9905
- GCC_except_table9953
- GCC_except_table9977
- GCC_except_table9978
- GCC_except_table9982
- GCC_except_table9983
- GCC_except_table9984
- GCC_except_table9985
- GCC_except_table9993
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- ___31-[_NUPipeline map:block:error:]_block_invoke
- ___39-[_NUPipeline reduce:with:block:error:]_block_invoke
- ___53+[NUPipelineProcessor processorWithIdentifier:error:]_block_invoke
- ___83-[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]_block_invoke
- ___block_descriptor_56_e8_32s40bs48r_e25_B24?0"_NUPipeline"8^16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e25_B24?0"_NUPipeline"8^16ls32l8s40l8s48l8
- _objc_msgSend$addMapPipeline:error:
- _objc_msgSend$addReducePipeline:error:
- _objc_msgSend$arrayChannel:
- _objc_msgSend$processorForConfiguration:identifier:controlData:error:
- _objc_msgSend$processorWithIdentifier:error:
CStrings:
+ "+[NUPipelineFactory buildPipelineWithBuilder:]"
+ "+[NUPipelineFactory colorVolumePipeline]"
+ "+[NUPipelineFactory computePipelineWithProcessorName:bundleIdentifier:error:]"
+ "+[NUPipelineFactory gainMapComputePipelineWithOptions:]"
+ "+[NUPipelineFactory metadataPipelineWithProcessorName:bundleIdentifier:error:]"
+ "+[NUPipelineFactory renderPipelineWithProcessorName:bundleIdentifier:error:]"
+ "+[NUPipelineProcessor processorWithName:bundleIdentifier:error:]"
+ "-[NUChannelOptionalFormat canAcceptDataWithFormat:]"
+ "-[NUChannelOptionalFormat initWithWrappedFormat:]"
+ "-[NUChannelOptionalFormat init]"
+ "-[NUControlDescriptor canAcceptDataWithDescriptor:]"
+ "-[NUOptionalDescriptor canAcceptDataWithDescriptor:]"
+ "-[NUOptionalDescriptor initWithDescriptor:validatedDefaultValue:]"
+ "-[NUPipelineProcessorCache processorForConfiguration:processor:controlData:error:]"
+ "-[_NUMapPipeline addElementOutputChannel:]"
+ "-[_NUMapPipeline initWithArrayChannel:]"
+ "-[_NUPipeline addPipelineWithBuilder:]"
+ "-[_NUReducePipeline initWithArrayChannel:accumulatorChannel:]"
+ "<%@:%p optional:%@>"
+ "Duplicate input name: %@"
+ "Failed to build colorVolumePipeline: %@"
+ "Failed to build gainMapComputePipeline: %@"
+ "Failed to build pipeline"
+ "Failed to copy the processor instance"
+ "Failed to look up metadata processor by name"
+ "Failed to look up processor by name"
+ "Invalid default value: %@, error: %@"
+ "accumulatorChannel != nil"
+ "arrayChannel != nil"
+ "arrayChannel.format.isArray"
+ "elementChannel != nil"
+ "initialInput != nil"
- "+[NUPipelineFactory computePipelineWithProcessorIdentifier:error:]"
- "+[NUPipelineFactory metadataPipelineWithProcessorIdentifier:error:]"
- "+[NUPipelineFactory renderPipelineWithProcessorIdentifier:error:]"
- "+[NUPipelineProcessor processorWithIdentifier:error:]"
- "-[NUPipelineProcessorCache processorForConfiguration:identifier:controlData:error:]"
- "Cardinality mismatch"
- "Failed to create the processor instance"
- "Failed to look up metadata processor by identifier"
- "Failed to look up processor by identifier"
- "Initial value should not be an array"
- "Missing input (initial value) channel for output channel"
- "Nothing to map"
- "Nothing to reduce"
- "channel"
- "com.apple.coreimage"
- "com.apple.neutrino.main"
```

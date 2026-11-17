## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-920.7.110.0.0
-  __TEXT.__text: 0x32ab44
-  __TEXT.__objc_methlist: 0x21dd4
+920.12.210.0.0
+  __TEXT.__text: 0x330070
+  __TEXT.__objc_methlist: 0x22224
   __TEXT.__const: 0x2980
   __TEXT.__dlopen_cstrs: 0x45
   __TEXT.__constg_swiftt: 0x178

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x4033a
+  __TEXT.__cstring: 0x4068e
   __TEXT.__swift5_capture: 0x390
   __TEXT.__gcc_except_tab: 0x8200
-  __TEXT.__oslogstring: 0x590b
+  __TEXT.__oslogstring: 0x5941
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xa640
+  __TEXT.__unwind_info: 0xa768
   __TEXT.__eh_frame: 0x700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4178
+  __DATA_CONST.__const: 0x41b8
   __DATA_CONST.__objc_classlist: 0x1640
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x4e8
+  __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb9e0
+  __DATA_CONST.__objc_selrefs: 0xbab8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x1040
+  __DATA_CONST.__objc_superrefs: 0x1048
   __DATA_CONST.__objc_arraydata: 0xb30
   __DATA_CONST.__got: 0x2308
-  __AUTH_CONST.__const: 0x55a0
-  __AUTH_CONST.__cfstring: 0x1dbe0
-  __AUTH_CONST.__objc_const: 0x38640
+  __AUTH_CONST.__const: 0x55c0
+  __AUTH_CONST.__cfstring: 0x1de40
+  __AUTH_CONST.__objc_const: 0x38820
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_intobj: 0x9a8

   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__auth_got: 0x10f0
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1ad4
-  __DATA.__data: 0x2f0
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x1ae4
+  __DATA.__data: 0x350
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__objc_data: 0xdb60
+  __DATA_DIRTY.__objc_data: 0xdb10
   __DATA_DIRTY.__data: 0x3780
   __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12300
-  Symbols:   21280
-  CStrings:  7468
+  Functions: 12389
+  Symbols:   21384
+  CStrings:  7494
 
Symbols:
+ +[NUChannelPortRef parseLocation:pipelinePath:portMatching:isInput:isConnectedInput:isUnwrapped:error:]
+ +[NUPipelineFactory selectorPipelineWithFormat:]
+ +[_NUMediaGeometry geometryDescriptor]
+ +[_NUMediaGeometry geometryIdentifier]
+ -[NSNull(NUControlDataRepresentable) nu_subdataForKey:format:error:]
+ -[NSObject(NUControlDataRepresentable) nu_checkDigestibility:]
+ -[NUArrayDescriptor hash]
+ -[NUChannel nonOptionalChannel]
+ -[NUChannel optionalChannel]
+ -[NUChannel unwrappedSubchannel]
+ -[NUChannelConstantExpression nu_checkDigestibility:]
+ -[NUChannelContainerMediaFormat componentsDescription]
+ -[NUChannelControlData dataWithFormat:error:]
+ -[NUChannelControlFormat unwrappedChannel]
+ -[NUChannelData checkDigestibility:]
+ -[NUChannelData dataWithFormat:error:]
+ -[NUChannelData nu_updateDigest:]
+ -[NUChannelElementFormat nonOptionalFormat]
+ -[NUChannelElementFormat optionalFormat]
+ -[NUChannelExpression nu_checkDigestibility:]
+ -[NUChannelForceUnwrapExpression subexpressionForKey:]
+ -[NUChannelFormat compactDescription]
+ -[NUChannelFormat unwrappedChannel]
+ -[NUChannelMediaData dataWithFormat:error:]
+ -[NUChannelNilCoalesceExpression subexpressionForKey:]
+ -[NUChannelOptionalFormat unwrappedChannel]
+ -[NUChannelPortRef isUnwrapped]
+ -[NUChannelPortRef unwrappedRef]
+ -[NUChannelStaticExpression nu_checkDigestibility:]
+ -[NUChannelUnwrappedFormat .cxx_destruct]
+ -[NUChannelUnwrappedFormat arrayItemFormat]
+ -[NUChannelUnwrappedFormat canAcceptDataWithFormat:]
+ -[NUChannelUnwrappedFormat canSpecializeFormat:]
+ -[NUChannelUnwrappedFormat channelType]
+ -[NUChannelUnwrappedFormat compactDescription]
+ -[NUChannelUnwrappedFormat debugDescription]
+ -[NUChannelUnwrappedFormat description]
+ -[NUChannelUnwrappedFormat elementChannel]
+ -[NUChannelUnwrappedFormat genericFormat]
+ -[NUChannelUnwrappedFormat hash]
+ -[NUChannelUnwrappedFormat initWithOptionalFormat:]
+ -[NUChannelUnwrappedFormat init]
+ -[NUChannelUnwrappedFormat isArray]
+ -[NUChannelUnwrappedFormat isComparableToChannelFormat:]
+ -[NUChannelUnwrappedFormat isComputedData]
+ -[NUChannelUnwrappedFormat isEqualToChannelFormat:]
+ -[NUChannelUnwrappedFormat isEqualToUnwrappedFormat:]
+ -[NUChannelUnwrappedFormat isGeneric]
+ -[NUChannelUnwrappedFormat isOptional]
+ -[NUChannelUnwrappedFormat nonOptionalFormat]
+ -[NUChannelUnwrappedFormat optionalFormat]
+ -[NUChannelUnwrappedFormat specializedWithFormat:]
+ -[NUChannelUnwrappedFormat subchannelFormatForKey:]
+ -[NUChannelUnwrappedFormat subchannelKeys]
+ -[NUCompoundDescriptor hash]
+ -[NUCompoundDescriptor initWithProperties:identifier:buildable:]
+ -[NUCompoundDescriptor initWithProperties:identifier:valueType:buildable:]
+ -[NUCompoundDescriptor isBuildable]
+ -[NUCompoundDescriptor subdescriptorForKey:]
+ -[NUCompoundDescriptor subvalueForKey:value:]
+ -[NUControlDescriptor subdescriptorForKey:]
+ -[NUControlDescriptor subvalueForKey:value:]
+ -[NUEnumDescriptor hash]
+ -[NUGlobalSettings rendererContextUseMemoryLimit]
+ -[NUGlobalSettings setRendererContextUseMemoryLimit:]
+ -[NULivePhotoExportRequest setVideoOutputSettings:]
+ -[NULivePhotoExportRequest videoOutputSettings]
+ -[NUNumberDescriptor hash]
+ -[NUOpaqueDescriptor hash]
+ -[NUOptionalDescriptor availability]
+ -[NUOptionalDescriptor hash]
+ -[NUOptionalDescriptor initWithDescriptor:availability:validatedDefaultValue:]
+ -[NUOptionalDescriptor subdescriptorForKey:]
+ -[NUOptionalDescriptor subvalueForKey:value:]
+ -[NURectDescriptor hash]
+ -[NURectDescriptor subdescriptorForKey:]
+ -[NUTimeDescriptor hash]
+ -[NUVectorDescriptor hash]
+ -[_NUAssetPipeline assetMediaWithOriginalStyle:]
+ -[_NUAssetPipeline containerMediaWithOriginalStyle:error:]
+ -[_NUAssetPipeline primaryMediaWithOriginalStyle:deltaMedia:metadataMedia:revertToOriginalStyle:error:]
+ -[_NUAuxiliaryMetadata formatIdentifier]
+ -[_NUAuxiliaryMetadata metadataWithIdentifier:]
+ -[_NUAuxiliaryMetadata nu_updateDigest:]
+ -[_NUCachedComputedMedia mediaWithFormat:error:]
+ -[_NUCachedMedia initWithBaseMedia:cacheNode:format:]
+ -[_NUChannelPort _elementSubportWithChannel:]
+ -[_NUChannelPort isUnwrapped]
+ -[_NUChannelPort nonOptionalElementSubport]
+ -[_NUChannelPort optionalElementSubport]
+ -[_NUChannelPort unwrappedSubport]
+ -[_NUCompositeMedia mediaWithFormat:error:]
+ -[_NUComputedMedia mediaWithFormat:error:]
+ -[_NUCropPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUCropPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUHDRColorVolumePipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUHDRColorVolumePipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUHDRGainMapComputePipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUHDRGainMapComputePipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUHDRToneMapApplyPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUHDRToneMapApplyPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NUImageMetadata formatIdentifier]
+ -[_NUImageMetadata metadataWithIdentifier:]
+ -[_NUImageMetadata nu_updateDigest:]
+ -[_NUMedia mediaWithFormat:error:]
+ -[_NUMediaGeometry valueForKey:]
+ -[_NUOrientationPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUOrientationPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NURenderMedia mediaWithFormat:error:]
+ -[_NUVideoMetadata formatIdentifier]
+ -[_NUVideoMetadata metadataWithIdentifier:]
+ -[_NUVideoMetadata nu_updateDigest:]
+ GCC_except_table10033
+ GCC_except_table10095
+ GCC_except_table10102
+ GCC_except_table10107
+ GCC_except_table10109
+ GCC_except_table10227
+ GCC_except_table10466
+ GCC_except_table10473
+ GCC_except_table1066
+ GCC_except_table10683
+ GCC_except_table10721
+ GCC_except_table10725
+ GCC_except_table10943
+ GCC_except_table11223
+ GCC_except_table11226
+ GCC_except_table11381
+ GCC_except_table11389
+ GCC_except_table1139
+ GCC_except_table11390
+ GCC_except_table11395
+ GCC_except_table11400
+ GCC_except_table11405
+ GCC_except_table11425
+ GCC_except_table11432
+ GCC_except_table11433
+ GCC_except_table11434
+ GCC_except_table11435
+ GCC_except_table11638
+ GCC_except_table11650
+ GCC_except_table11653
+ GCC_except_table11658
+ GCC_except_table11674
+ GCC_except_table11692
+ GCC_except_table11695
+ GCC_except_table11696
+ GCC_except_table11700
+ GCC_except_table11701
+ GCC_except_table11811
+ GCC_except_table11836
+ GCC_except_table11838
+ GCC_except_table11934
+ GCC_except_table11936
+ GCC_except_table11938
+ GCC_except_table11943
+ GCC_except_table11952
+ GCC_except_table11953
+ GCC_except_table1302
+ GCC_except_table2054
+ GCC_except_table2169
+ GCC_except_table2389
+ GCC_except_table2540
+ GCC_except_table2556
+ GCC_except_table2570
+ GCC_except_table2595
+ GCC_except_table2618
+ GCC_except_table2621
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2629
+ GCC_except_table2630
+ GCC_except_table2641
+ GCC_except_table2645
+ GCC_except_table2647
+ GCC_except_table2667
+ GCC_except_table2670
+ GCC_except_table2675
+ GCC_except_table2678
+ GCC_except_table2680
+ GCC_except_table2685
+ GCC_except_table2699
+ GCC_except_table2701
+ GCC_except_table2702
+ GCC_except_table2707
+ GCC_except_table2708
+ GCC_except_table2720
+ GCC_except_table2954
+ GCC_except_table2955
+ GCC_except_table2956
+ GCC_except_table2957
+ GCC_except_table2958
+ GCC_except_table2960
+ GCC_except_table2962
+ GCC_except_table2977
+ GCC_except_table2992
+ GCC_except_table2993
+ GCC_except_table2994
+ GCC_except_table2995
+ GCC_except_table3010
+ GCC_except_table3011
+ GCC_except_table3025
+ GCC_except_table3026
+ GCC_except_table3031
+ GCC_except_table3071
+ GCC_except_table3100
+ GCC_except_table3101
+ GCC_except_table3882
+ GCC_except_table3889
+ GCC_except_table3890
+ GCC_except_table3898
+ GCC_except_table3907
+ GCC_except_table3917
+ GCC_except_table3923
+ GCC_except_table3925
+ GCC_except_table3928
+ GCC_except_table3930
+ GCC_except_table3933
+ GCC_except_table3934
+ GCC_except_table3935
+ GCC_except_table3951
+ GCC_except_table3953
+ GCC_except_table3971
+ GCC_except_table4023
+ GCC_except_table4027
+ GCC_except_table4055
+ GCC_except_table4173
+ GCC_except_table4257
+ GCC_except_table4263
+ GCC_except_table4271
+ GCC_except_table4348
+ GCC_except_table4356
+ GCC_except_table4357
+ GCC_except_table4365
+ GCC_except_table4366
+ GCC_except_table4367
+ GCC_except_table4369
+ GCC_except_table4386
+ GCC_except_table4392
+ GCC_except_table4401
+ GCC_except_table4402
+ GCC_except_table4411
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4419
+ GCC_except_table4421
+ GCC_except_table4422
+ GCC_except_table4423
+ GCC_except_table4425
+ GCC_except_table4427
+ GCC_except_table4428
+ GCC_except_table4429
+ GCC_except_table4434
+ GCC_except_table4435
+ GCC_except_table4436
+ GCC_except_table4437
+ GCC_except_table4438
+ GCC_except_table4440
+ GCC_except_table4441
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table4444
+ GCC_except_table4445
+ GCC_except_table4446
+ GCC_except_table4447
+ GCC_except_table4452
+ GCC_except_table4453
+ GCC_except_table4454
+ GCC_except_table4455
+ GCC_except_table4456
+ GCC_except_table4457
+ GCC_except_table4511
+ GCC_except_table4533
+ GCC_except_table4537
+ GCC_except_table4538
+ GCC_except_table4543
+ GCC_except_table4544
+ GCC_except_table4547
+ GCC_except_table4548
+ GCC_except_table4549
+ GCC_except_table4550
+ GCC_except_table4551
+ GCC_except_table4552
+ GCC_except_table4553
+ GCC_except_table4555
+ GCC_except_table4561
+ GCC_except_table4565
+ GCC_except_table4569
+ GCC_except_table4570
+ GCC_except_table4571
+ GCC_except_table4573
+ GCC_except_table4580
+ GCC_except_table4582
+ GCC_except_table4583
+ GCC_except_table4634
+ GCC_except_table4635
+ GCC_except_table4833
+ GCC_except_table4912
+ GCC_except_table4913
+ GCC_except_table4917
+ GCC_except_table4919
+ GCC_except_table4923
+ GCC_except_table4925
+ GCC_except_table4927
+ GCC_except_table4928
+ GCC_except_table4932
+ GCC_except_table4937
+ GCC_except_table4938
+ GCC_except_table4988
+ GCC_except_table4989
+ GCC_except_table4990
+ GCC_except_table4991
+ GCC_except_table4999
+ GCC_except_table5000
+ GCC_except_table5001
+ GCC_except_table5014
+ GCC_except_table5015
+ GCC_except_table5021
+ GCC_except_table5028
+ GCC_except_table5029
+ GCC_except_table5031
+ GCC_except_table5032
+ GCC_except_table5033
+ GCC_except_table5034
+ GCC_except_table5040
+ GCC_except_table5041
+ GCC_except_table5042
+ GCC_except_table5043
+ GCC_except_table5045
+ GCC_except_table5046
+ GCC_except_table5050
+ GCC_except_table5051
+ GCC_except_table5052
+ GCC_except_table5053
+ GCC_except_table5054
+ GCC_except_table5055
+ GCC_except_table5056
+ GCC_except_table5057
+ GCC_except_table5059
+ GCC_except_table5061
+ GCC_except_table5064
+ GCC_except_table5065
+ GCC_except_table5066
+ GCC_except_table5067
+ GCC_except_table5068
+ GCC_except_table5070
+ GCC_except_table5072
+ GCC_except_table5073
+ GCC_except_table5074
+ GCC_except_table5075
+ GCC_except_table5083
+ GCC_except_table5177
+ GCC_except_table5268
+ GCC_except_table5506
+ GCC_except_table5521
+ GCC_except_table5533
+ GCC_except_table5557
+ GCC_except_table5569
+ GCC_except_table5574
+ GCC_except_table5665
+ GCC_except_table5668
+ GCC_except_table5677
+ GCC_except_table5702
+ GCC_except_table5768
+ GCC_except_table5776
+ GCC_except_table5791
+ GCC_except_table5899
+ GCC_except_table5906
+ GCC_except_table5907
+ GCC_except_table5910
+ GCC_except_table5913
+ GCC_except_table5917
+ GCC_except_table5920
+ GCC_except_table5921
+ GCC_except_table5927
+ GCC_except_table5928
+ GCC_except_table5930
+ GCC_except_table5932
+ GCC_except_table5942
+ GCC_except_table5954
+ GCC_except_table5970
+ GCC_except_table5971
+ GCC_except_table5976
+ GCC_except_table5977
+ GCC_except_table5979
+ GCC_except_table5982
+ GCC_except_table5983
+ GCC_except_table5987
+ GCC_except_table5990
+ GCC_except_table5991
+ GCC_except_table5993
+ GCC_except_table5994
+ GCC_except_table5997
+ GCC_except_table5999
+ GCC_except_table6001
+ GCC_except_table6002
+ GCC_except_table6003
+ GCC_except_table6004
+ GCC_except_table6005
+ GCC_except_table6009
+ GCC_except_table6015
+ GCC_except_table6218
+ GCC_except_table6811
+ GCC_except_table7124
+ GCC_except_table7132
+ GCC_except_table7137
+ GCC_except_table7138
+ GCC_except_table7142
+ GCC_except_table7212
+ GCC_except_table7241
+ GCC_except_table7247
+ GCC_except_table7260
+ GCC_except_table7315
+ GCC_except_table7383
+ GCC_except_table7393
+ GCC_except_table7420
+ GCC_except_table7421
+ GCC_except_table7471
+ GCC_except_table7636
+ GCC_except_table7670
+ GCC_except_table7679
+ GCC_except_table7702
+ GCC_except_table7708
+ GCC_except_table7709
+ GCC_except_table7710
+ GCC_except_table7734
+ GCC_except_table7807
+ GCC_except_table7810
+ GCC_except_table7817
+ GCC_except_table7819
+ GCC_except_table7820
+ GCC_except_table7822
+ GCC_except_table7823
+ GCC_except_table7824
+ GCC_except_table7825
+ GCC_except_table7830
+ GCC_except_table7832
+ GCC_except_table7833
+ GCC_except_table7834
+ GCC_except_table7835
+ GCC_except_table7839
+ GCC_except_table7840
+ GCC_except_table7842
+ GCC_except_table7844
+ GCC_except_table7846
+ GCC_except_table7848
+ GCC_except_table7854
+ GCC_except_table7857
+ GCC_except_table7861
+ GCC_except_table7862
+ GCC_except_table7864
+ GCC_except_table7865
+ GCC_except_table7866
+ GCC_except_table7867
+ GCC_except_table7868
+ GCC_except_table7870
+ GCC_except_table7871
+ GCC_except_table7872
+ GCC_except_table7873
+ GCC_except_table7874
+ GCC_except_table7875
+ GCC_except_table7876
+ GCC_except_table7877
+ GCC_except_table7878
+ GCC_except_table7879
+ GCC_except_table7880
+ GCC_except_table7881
+ GCC_except_table7882
+ GCC_except_table7883
+ GCC_except_table7884
+ GCC_except_table7885
+ GCC_except_table7886
+ GCC_except_table7887
+ GCC_except_table7987
+ GCC_except_table8016
+ GCC_except_table8101
+ GCC_except_table8295
+ GCC_except_table8310
+ GCC_except_table8347
+ GCC_except_table8354
+ GCC_except_table8405
+ GCC_except_table8450
+ GCC_except_table8594
+ GCC_except_table8599
+ GCC_except_table8602
+ GCC_except_table8625
+ GCC_except_table8669
+ GCC_except_table8966
+ GCC_except_table8970
+ GCC_except_table9006
+ GCC_except_table9010
+ GCC_except_table9012
+ GCC_except_table9087
+ GCC_except_table9127
+ GCC_except_table9142
+ GCC_except_table9160
+ GCC_except_table9161
+ GCC_except_table9229
+ GCC_except_table9418
+ GCC_except_table9428
+ GCC_except_table9429
+ GCC_except_table9431
+ GCC_except_table9432
+ GCC_except_table9593
+ GCC_except_table9620
+ GCC_except_table9644
+ GCC_except_table9652
+ GCC_except_table9776
+ GCC_except_table9815
+ _NUControlAvailabilityDescription
+ _NUMediaMetadataFormatIdentifierAuxiliary
+ _NUMediaMetadataFormatIdentifierImage
+ _NUMediaMetadataFormatIdentifierVideo
+ _NUSanitizedRenderDestinationLabel
+ _OBJC_CLASS_$_NUChannelUnwrappedFormat
+ _OBJC_IVAR_$_NUChannelPortRef._isUnwrapped
+ _OBJC_IVAR_$_NUChannelUnwrappedFormat._optionalFormat
+ _OBJC_IVAR_$_NUCompoundDescriptor._isBuildable
+ _OBJC_IVAR_$_NULivePhotoExportRequest._videoOutputSettings
+ _OBJC_IVAR_$_NUOptionalDescriptor._availability
+ _OBJC_METACLASS_$_NUChannelUnwrappedFormat
+ __OBJC_$_CLASS_METHODS__NUMediaGeometry
+ __OBJC_$_CLASS_PROP_LIST__NUMediaGeometry
+ __OBJC_$_INSTANCE_METHODS_NUChannelData
+ __OBJC_$_INSTANCE_METHODS_NUChannelUnwrappedFormat
+ __OBJC_$_INSTANCE_VARIABLES_NUChannelUnwrappedFormat
+ __OBJC_$_PROP_LIST_NUMediaMetadataPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NUMediaMetadataPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NUMediaMetadataPrivate
+ __OBJC_$_PROTOCOL_REFS_NUMediaMetadataPrivate
+ __OBJC_CLASS_RO_$_NUChannelUnwrappedFormat
+ __OBJC_LABEL_PROTOCOL_$_NUMediaMetadataPrivate
+ __OBJC_METACLASS_RO_$_NUChannelUnwrappedFormat
+ __OBJC_PROTOCOL_$_NUMediaMetadataPrivate
+ ___34-[_NUChannelPort unwrappedSubport]_block_invoke
+ ___45-[NUChannelExpression nu_checkDigestibility:]_block_invoke
+ ___45-[_NUChannelPort _elementSubportWithChannel:]_block_invoke
+ ___49-[NUGlobalSettings rendererContextUseMemoryLimit]_block_invoke
+ ___54-[NUChannelContainerMediaFormat componentsDescription]_block_invoke
+ ___block_descriptor_40_e29_B16?0"NUChannelExpression"8l
+ ___block_descriptor_40_e8_32s_e42_v32?0"NSString"8"NUChannelFormat"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e42_v32?0"NSString"8"NUChannelFormat"16^B24ls32l8r40l8
- +[NUChannelPortRef parseLocation:pipelinePath:portMatching:isInput:isConnectedInput:error:]
- +[NUGlobalSettings rendererContextUseMemoryLimit]
- +[NUGlobalSettings setRendererContextUseMemoryLimit:]
- +[NUMediaGeometryExpression geometryDescriptor]
- -[NUChannelData(NUDigest) nu_updateDigest:]
- -[NUCompoundDescriptor descriptorForKey:]
- -[NUCompoundDescriptor initWithProperties:identifier:valueType:]
- -[NUCompoundDescriptor valueForKey:data:]
- -[NUControlDescriptor descriptorForKey:]
- -[NUControlDescriptor valueForKey:data:]
- -[NUMediaGeometryDescriptor controlType]
- -[NUMediaGeometryDescriptor defaultValueType]
- -[NUMediaGeometryDescriptor descriptorWithValueType:]
- -[NUMediaGeometryDescriptor initWithProperties:]
- -[NUMediaGeometryDescriptor initWithProperties:identifier:]
- -[NUMediaGeometryDescriptor initWithProperties:identifier:valueType:]
- -[NUMediaGeometryDescriptor initWithValueType:]
- -[NUMediaGeometryDescriptor init]
- -[NUMediaGeometryDescriptor valueForKey:data:]
- -[NUOptionalDescriptor descriptorForKey:]
- -[NUOptionalDescriptor initWithDescriptor:optionality:validatedDefaultValue:]
- -[NUOptionalDescriptor optionality]
- -[NUOptionalDescriptor valueForKey:data:]
- -[NURectDescriptor descriptorForKey:]
- -[_NUStyleRevertPipeline buildWithOptions:error:]
- -[_NUStyleRevertPipeline containerMediaWithOriginalStyle:error:]
- -[_NUStyleRevertPipeline primaryMediaWithOriginalStyle:deltaMedia:metadataMedia:revertToOriginalStyle:error:]
- GCC_except_table10007
- GCC_except_table10014
- GCC_except_table10019
- GCC_except_table10021
- GCC_except_table10139
- GCC_except_table1035
- GCC_except_table10378
- GCC_except_table10385
- GCC_except_table10595
- GCC_except_table10633
- GCC_except_table10637
- GCC_except_table10855
- GCC_except_table1107
- GCC_except_table11134
- GCC_except_table11137
- GCC_except_table11292
- GCC_except_table11300
- GCC_except_table11301
- GCC_except_table11306
- GCC_except_table11311
- GCC_except_table11316
- GCC_except_table11336
- GCC_except_table11343
- GCC_except_table11344
- GCC_except_table11345
- GCC_except_table11346
- GCC_except_table11549
- GCC_except_table11561
- GCC_except_table11564
- GCC_except_table11569
- GCC_except_table11585
- GCC_except_table11603
- GCC_except_table11606
- GCC_except_table11607
- GCC_except_table11611
- GCC_except_table11612
- GCC_except_table11722
- GCC_except_table11747
- GCC_except_table11749
- GCC_except_table11774
- GCC_except_table11845
- GCC_except_table11847
- GCC_except_table11849
- GCC_except_table11854
- GCC_except_table11864
- GCC_except_table1249
- GCC_except_table1261
- GCC_except_table2018
- GCC_except_table2133
- GCC_except_table2350
- GCC_except_table2493
- GCC_except_table2509
- GCC_except_table2523
- GCC_except_table2526
- GCC_except_table2536
- GCC_except_table2548
- GCC_except_table2553
- GCC_except_table2571
- GCC_except_table2574
- GCC_except_table2579
- GCC_except_table2580
- GCC_except_table2582
- GCC_except_table2594
- GCC_except_table2598
- GCC_except_table2623
- GCC_except_table2628
- GCC_except_table2631
- GCC_except_table2633
- GCC_except_table2638
- GCC_except_table2652
- GCC_except_table2654
- GCC_except_table2655
- GCC_except_table2660
- GCC_except_table2661
- GCC_except_table2673
- GCC_except_table2907
- GCC_except_table2908
- GCC_except_table2909
- GCC_except_table2910
- GCC_except_table2911
- GCC_except_table2913
- GCC_except_table2915
- GCC_except_table2930
- GCC_except_table2931
- GCC_except_table2932
- GCC_except_table2945
- GCC_except_table2946
- GCC_except_table2947
- GCC_except_table2948
- GCC_except_table2963
- GCC_except_table2964
- GCC_except_table2984
- GCC_except_table3024
- GCC_except_table3053
- GCC_except_table3054
- GCC_except_table3835
- GCC_except_table3836
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3842
- GCC_except_table3843
- GCC_except_table3851
- GCC_except_table3860
- GCC_except_table3870
- GCC_except_table3876
- GCC_except_table3877
- GCC_except_table3878
- GCC_except_table3881
- GCC_except_table3886
- GCC_except_table3904
- GCC_except_table3906
- GCC_except_table3976
- GCC_except_table3980
- GCC_except_table4008
- GCC_except_table4126
- GCC_except_table4210
- GCC_except_table4216
- GCC_except_table4224
- GCC_except_table4301
- GCC_except_table4302
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4307
- GCC_except_table4308
- GCC_except_table4309
- GCC_except_table4310
- GCC_except_table4312
- GCC_except_table4315
- GCC_except_table4316
- GCC_except_table4318
- GCC_except_table4319
- GCC_except_table4320
- GCC_except_table4322
- GCC_except_table4323
- GCC_except_table4333
- GCC_except_table4334
- GCC_except_table4339
- GCC_except_table4340
- GCC_except_table4341
- GCC_except_table4342
- GCC_except_table4344
- GCC_except_table4345
- GCC_except_table4346
- GCC_except_table4347
- GCC_except_table4350
- GCC_except_table4351
- GCC_except_table4358
- GCC_except_table4364
- GCC_except_table4371
- GCC_except_table4372
- GCC_except_table4374
- GCC_except_table4375
- GCC_except_table4376
- GCC_except_table4378
- GCC_except_table4382
- GCC_except_table4390
- GCC_except_table4395
- GCC_except_table4407
- GCC_except_table4408
- GCC_except_table4463
- GCC_except_table4485
- GCC_except_table4486
- GCC_except_table4489
- GCC_except_table4490
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4499
- GCC_except_table4500
- GCC_except_table4501
- GCC_except_table4502
- GCC_except_table4503
- GCC_except_table4504
- GCC_except_table4505
- GCC_except_table4507
- GCC_except_table4513
- GCC_except_table4517
- GCC_except_table4521
- GCC_except_table4522
- GCC_except_table4523
- GCC_except_table4525
- GCC_except_table4532
- GCC_except_table4535
- GCC_except_table4586
- GCC_except_table4587
- GCC_except_table4785
- GCC_except_table4864
- GCC_except_table4865
- GCC_except_table4869
- GCC_except_table4871
- GCC_except_table4875
- GCC_except_table4877
- GCC_except_table4879
- GCC_except_table4880
- GCC_except_table4884
- GCC_except_table4888
- GCC_except_table4889
- GCC_except_table4890
- GCC_except_table4891
- GCC_except_table4892
- GCC_except_table4894
- GCC_except_table4895
- GCC_except_table4897
- GCC_except_table4898
- GCC_except_table4908
- GCC_except_table4910
- GCC_except_table4941
- GCC_except_table4944
- GCC_except_table4947
- GCC_except_table4949
- GCC_except_table4950
- GCC_except_table4951
- GCC_except_table4952
- GCC_except_table4953
- GCC_except_table4954
- GCC_except_table4955
- GCC_except_table4957
- GCC_except_table4959
- GCC_except_table4960
- GCC_except_table4961
- GCC_except_table4966
- GCC_except_table4967
- GCC_except_table4973
- GCC_except_table4974
- GCC_except_table4979
- GCC_except_table4980
- GCC_except_table4981
- GCC_except_table4983
- GCC_except_table4985
- GCC_except_table4986
- GCC_except_table5011
- GCC_except_table5013
- GCC_except_table5016
- GCC_except_table5017
- GCC_except_table5018
- GCC_except_table5019
- GCC_except_table5020
- GCC_except_table5024
- GCC_except_table5025
- GCC_except_table5026
- GCC_except_table5129
- GCC_except_table5218
- GCC_except_table5451
- GCC_except_table5465
- GCC_except_table5477
- GCC_except_table5500
- GCC_except_table5512
- GCC_except_table5517
- GCC_except_table5607
- GCC_except_table5610
- GCC_except_table5619
- GCC_except_table5644
- GCC_except_table5709
- GCC_except_table5717
- GCC_except_table5732
- GCC_except_table5831
- GCC_except_table5838
- GCC_except_table5839
- GCC_except_table5840
- GCC_except_table5841
- GCC_except_table5842
- GCC_except_table5845
- GCC_except_table5846
- GCC_except_table5849
- GCC_except_table5852
- GCC_except_table5853
- GCC_except_table5855
- GCC_except_table5858
- GCC_except_table5859
- GCC_except_table5860
- GCC_except_table5861
- GCC_except_table5862
- GCC_except_table5863
- GCC_except_table5864
- GCC_except_table5865
- GCC_except_table5873
- GCC_except_table5874
- GCC_except_table5879
- GCC_except_table5886
- GCC_except_table5902
- GCC_except_table5903
- GCC_except_table5911
- GCC_except_table5915
- GCC_except_table5919
- GCC_except_table5922
- GCC_except_table5925
- GCC_except_table5934
- GCC_except_table5935
- GCC_except_table5936
- GCC_except_table5937
- GCC_except_table6150
- GCC_except_table6735
- GCC_except_table7037
- GCC_except_table7045
- GCC_except_table7050
- GCC_except_table7051
- GCC_except_table7055
- GCC_except_table7125
- GCC_except_table7154
- GCC_except_table7160
- GCC_except_table7173
- GCC_except_table7228
- GCC_except_table7296
- GCC_except_table7306
- GCC_except_table7333
- GCC_except_table7334
- GCC_except_table7384
- GCC_except_table7549
- GCC_except_table7583
- GCC_except_table7592
- GCC_except_table7615
- GCC_except_table7619
- GCC_except_table7621
- GCC_except_table7622
- GCC_except_table7623
- GCC_except_table7647
- GCC_except_table7698
- GCC_except_table7699
- GCC_except_table7700
- GCC_except_table7701
- GCC_except_table7712
- GCC_except_table7713
- GCC_except_table7720
- GCC_except_table7723
- GCC_except_table7730
- GCC_except_table7732
- GCC_except_table7733
- GCC_except_table7735
- GCC_except_table7736
- GCC_except_table7737
- GCC_except_table7738
- GCC_except_table7743
- GCC_except_table7745
- GCC_except_table7746
- GCC_except_table7747
- GCC_except_table7748
- GCC_except_table7752
- GCC_except_table7753
- GCC_except_table7755
- GCC_except_table7757
- GCC_except_table7759
- GCC_except_table7761
- GCC_except_table7767
- GCC_except_table7770
- GCC_except_table7774
- GCC_except_table7775
- GCC_except_table7777
- GCC_except_table7778
- GCC_except_table7779
- GCC_except_table7780
- GCC_except_table7781
- GCC_except_table7783
- GCC_except_table7784
- GCC_except_table7789
- GCC_except_table7790
- GCC_except_table7791
- GCC_except_table7792
- GCC_except_table7794
- GCC_except_table7795
- GCC_except_table7796
- GCC_except_table7797
- GCC_except_table7798
- GCC_except_table7900
- GCC_except_table7929
- GCC_except_table8014
- GCC_except_table8208
- GCC_except_table8223
- GCC_except_table8260
- GCC_except_table8267
- GCC_except_table8318
- GCC_except_table8363
- GCC_except_table8507
- GCC_except_table8512
- GCC_except_table8515
- GCC_except_table8538
- GCC_except_table8582
- GCC_except_table8879
- GCC_except_table8883
- GCC_except_table8919
- GCC_except_table8923
- GCC_except_table8925
- GCC_except_table8986
- GCC_except_table9000
- GCC_except_table9040
- GCC_except_table9072
- GCC_except_table9141
- GCC_except_table9330
- GCC_except_table9340
- GCC_except_table9341
- GCC_except_table9343
- GCC_except_table9344
- GCC_except_table9505
- GCC_except_table9532
- GCC_except_table9556
- GCC_except_table9564
- GCC_except_table9688
- GCC_except_table9727
- GCC_except_table9945
- _NUControlOptionalityDescription
- _OBJC_CLASS_$_NUMediaGeometryDescriptor
- _OBJC_IVAR_$_NUOptionalDescriptor._optionality
- _OBJC_METACLASS_$_NUMediaGeometryDescriptor
- __OBJC_$_CLASS_METHODS_NUMediaGeometryExpression
- __OBJC_$_INSTANCE_METHODS_NUChannelData(NUDigest)
- __OBJC_$_INSTANCE_METHODS_NUMediaGeometryDescriptor
- __OBJC_CLASS_RO_$_NUMediaGeometryDescriptor
- __OBJC_METACLASS_RO_$_NUMediaGeometryDescriptor
- ___32-[_NUChannelPort elementSubport]_block_invoke
- ___44-[NUChannelContainerMediaFormat description]_block_invoke
- ___49+[NUGlobalSettings rendererContextUseMemoryLimit]_block_invoke
- ___block_descriptor_40_e8_32r_e47_v32?0"NSString"8"NUChannelMediaFormat"16^B24lr32l8
- ___block_descriptor_48_e8_32s40r_e47_v32?0"NSString"8"NUChannelMediaFormat"16^B24ls32l8r40l8
CStrings:
+ "%@!"
+ "-[NUChannelControlData dataWithFormat:error:]"
+ "-[NUChannelData dataWithFormat:error:]"
+ "-[NUChannelMediaData dataWithFormat:error:]"
+ "-[NUChannelStaticExpression nu_checkDigestibility:]"
+ "-[NUChannelStaticExpression nu_updateDigest:]"
+ "-[NUChannelUnwrappedFormat canAcceptDataWithFormat:]"
+ "-[NUChannelUnwrappedFormat initWithOptionalFormat:]"
+ "-[NUChannelUnwrappedFormat init]"
+ "-[NUCompoundDescriptor initWithProperties:identifier:valueType:buildable:]"
+ "-[NUCompoundDescriptor subdescriptorForKey:]"
+ "-[NUOptionalDescriptor initWithDescriptor:availability:validatedDefaultValue:]"
+ "-[NURenderSession waitForTermination]_block_invoke"
+ "-[_NUAssetPipeline primaryMediaWithOriginalStyle:deltaMedia:metadataMedia:revertToOriginalStyle:error:]"
+ "-[_NUCachedComputedMedia mediaWithFormat:error:]"
+ "-[_NUCachedMedia initWithBaseMedia:cacheNode:format:]"
+ "-[_NUChannelPort _elementSubportWithChannel:]"
+ "-[_NUCompositeMedia mediaWithFormat:error:]"
+ "-[_NUComputedMedia mediaWithFormat:error:]"
+ "-[_NURenderMedia mediaWithFormat:error:]"
+ "<%@:%p unwrapped:%@>"
+ "AuxiliaryMetadata"
+ "CLAP %@ should be contained in scaled extent size %@"
+ "Cannot convert control data"
+ "Control data is not digestible"
+ "Element subport already exists with another format: %@"
+ "Failed to convert control data"
+ "Failed to format media component"
+ "Failed to format output data"
+ "Failed to revert asset style, using the plain asset media: %{public}@"
+ "ImageMetadata"
+ "Incompatible computed media format"
+ "MediaGeometry"
+ "Missing gainMap input"
+ "NUAuxiliaryMetadata<"
+ "NUImageMetadata<"
+ "NUVideoMetadata<"
+ "Optional primary component"
+ "Port is not optional"
+ "Session is not terminating"
+ "Session was terminated"
+ "Static expressions are not digestible"
+ "Target format cannot accept a null described by the source format"
+ "Unwrapped data is nil"
+ "VideoMetadata"
+ "defaultValue == nil || availability != NUControlAvailabilityRequired"
+ "format.descriptor.controlType == NUControlTypeOptional"
+ "media!"
+ "optionalFormat != nil"
+ "optionalFormat.isOptional"
+ "sourceFormat"
+ "targetFormat"
+ "unwrapped"
+ "value!"
- "%@[%@]"
- ")<"
- "-[NUCompoundDescriptor descriptorForKey:]"
- "-[NUCompoundDescriptor initWithProperties:identifier:valueType:]"
- "-[NUMediaGeometryDescriptor initWithProperties:]"
- "-[NUMediaGeometryDescriptor initWithProperties:identifier:]"
- "-[NUMediaGeometryDescriptor initWithProperties:identifier:valueType:]"
- "-[NUMediaGeometryDescriptor valueForKey:data:]"
- "-[NUOptionalDescriptor initWithDescriptor:optionality:validatedDefaultValue:]"
- "-[_NUChannelPort specializeWithInputFormat:]"
- "-[_NUChannelPort specializeWithOutputFormat:]"
- "-[_NUStyleRevertPipeline primaryMediaWithOriginalStyle:deltaMedia:metadataMedia:revertToOriginalStyle:error:]"
- "Cannot expose computed media as control data"
- "Failed to revert asset style"
- "Missing crop rect input"
- "Missing end data"
- "Missing start data"
- "NUChannelData("
- "Unsupported media geometry key: '%@'"
- "cleanApertureRect"
- "defaultValue == nil || optionality != NUControlOptionalityRequired"
- "format.descriptor.isOptional"
- "geometry"
- "inputFormat != nil"
- "outputFormat != nil"
- "session '%{public}@' terminated"
- "useCleanRect"
- "v32@?0@\"NSString\"8@\"NUChannelMediaFormat\"16^B24"
```

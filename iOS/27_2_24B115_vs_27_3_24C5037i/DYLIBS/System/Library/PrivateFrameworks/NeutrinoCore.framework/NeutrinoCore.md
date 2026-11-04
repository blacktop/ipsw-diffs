## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x3236cc
-  __TEXT.__objc_methlist: 0x216fc
-  __TEXT.__const: 0x27a8
+920.7.110.0.0
+  __TEXT.__text: 0x32ab44
+  __TEXT.__objc_methlist: 0x21dd4
+  __TEXT.__const: 0x2980
   __TEXT.__dlopen_cstrs: 0x45
-  __TEXT.__swift5_typeref: 0x52b
+  __TEXT.__constg_swiftt: 0x178
+  __TEXT.__swift5_typeref: 0x569
+  __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0x93
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__constg_swiftt: 0x158
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_fieldmd: 0x15c
-  __TEXT.__swift5_proto: 0x64
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x3f687
-  __TEXT.__swift5_capture: 0x350
-  __TEXT.__gcc_except_tab: 0x8170
-  __TEXT.__oslogstring: 0x58cd
-  __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0xa450
-  __TEXT.__eh_frame: 0x678
+  __TEXT.__swift5_fieldmd: 0x178
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_proto: 0x84
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__cstring: 0x4033a
+  __TEXT.__swift5_capture: 0x390
+  __TEXT.__gcc_except_tab: 0x8200
+  __TEXT.__oslogstring: 0x590b
+  __TEXT.__ustring: 0x3e
+  __TEXT.__unwind_info: 0xa640
+  __TEXT.__eh_frame: 0x700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40e8
-  __DATA_CONST.__objc_classlist: 0x1618
+  __DATA_CONST.__const: 0x4178
+  __DATA_CONST.__objc_classlist: 0x1640
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x4e0
+  __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb860
-  __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1028
-  __DATA_CONST.__objc_arraydata: 0xaf0
-  __DATA_CONST.__got: 0x22d8
-  __AUTH_CONST.__const: 0x5468
-  __AUTH_CONST.__cfstring: 0x1d4e0
-  __AUTH_CONST.__objc_const: 0x37ed0
+  __DATA_CONST.__objc_selrefs: 0xb9e0
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x1040
+  __DATA_CONST.__objc_arraydata: 0xb30
+  __DATA_CONST.__got: 0x2308
+  __AUTH_CONST.__const: 0x55a0
+  __AUTH_CONST.__cfstring: 0x1dbe0
+  __AUTH_CONST.__objc_const: 0x38640
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_dictobj: 0x370
-  __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x9a8
+  __AUTH_CONST.__objc_doubleobj: 0x1f0
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__auth_got: 0x10f0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x1aa8
-  __DATA.__data: 0x248
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x1ad4
+  __DATA.__data: 0x2f0
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xdb60
   __DATA_DIRTY.__data: 0x3780

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12140
-  Symbols:   21069
-  CStrings:  7379
+  Functions: 12300
+  Symbols:   21280
+  CStrings:  7468
 
Symbols:
+ +[CIVector(NUControlDataRepresentable) nu_valueFromControlData:error:]
+ +[NSArray(NUControlDataRepresentable) nu_valueFromControlData:error:]
+ +[NSDictionary(NUControlDataRepresentable) nu_valueFromControlData:error:]
+ +[NSNumber(NUControlDataRepresentable) nu_valueFromControlData:error:]
+ +[NSString(NUControlDataRepresentable) nu_valueFromControlData:error:]
+ +[NUAssetCapability capabilityMarkerFormat]
+ +[NUAssetCapability(NURawDecode) rawDecode]
+ +[NUChannelControlData opaqueDataWithValue:identifier:]
+ +[NUChannelControlFormat opaqueFormat:]
+ +[NUChannelData opaque:identifier:]
+ +[NUChannelData orientation:]
+ +[NUChannelExpression forceUnwrap:]
+ +[NUEnumDescriptor orientationDescriptor]
+ +[NUEnumDescriptor orientationIdentifier]
+ +[NUOptionalDescriptor requiredOptionalWithDescriptor:]
+ +[NUOptionalDescriptor unavailableOptionalWithDescriptor:]
+ +[NUOptionalDescriptor unavailableOptionalWithDescriptor:defaultValue:]
+ +[NUPipelineProcessor identifier]
+ +[NUStyleTransferPipeline colorSpaceFormat]
+ +[_NURawDecodeCapability rawDecodeCapabilityFormat]
+ +[_NUStyleEngineMemoryResource usingSharedMemoryResourceForMetalCommandQueue:withDescriptor:perform:]
+ -[NSArray(NUControlDataRepresentable) nu_convertedFromFormat:toFormat:error:]
+ -[NSDictionary(NUControlDataRepresentable) nu_convertedFromFormat:toFormat:error:]
+ -[NUArrayDescriptor descriptorWithValueType:]
+ -[NUArrayDescriptor initWithElement:min:max:valueType:]
+ -[NUArrayDescriptor initWithValueType:]
+ -[NUAssetCapability format]
+ -[NUChannelArrayData _untypedValue]
+ -[NUChannelContainsExpression compactDescription]
+ -[NUChannelContainsExpression description]
+ -[NUChannelContainsExpression evaluateWithLeftData:rightData:outputFormat:error:]
+ -[NUChannelContainsExpression formatWithLeftData:rightData:error:]
+ -[NUChannelContainsExpression hash]
+ -[NUChannelContainsExpression isEqualToContainsExpression:]
+ -[NUChannelContainsExpression isEqualToExpression:]
+ -[NUChannelControlData _untypedValue]
+ -[NUChannelControlData opaqueValue]
+ -[NUChannelControlData valueOfType:]
+ -[NUChannelControlFormat descriptor]
+ -[NUChannelControlFormat shortDescription]
+ -[NUChannelData _opaqueValueOfClass:]
+ -[NUChannelData _untypedValue]
+ -[NUChannelData arrayValue]
+ -[NUChannelData dictionaryValue]
+ -[NUChannelData geometryValue]
+ -[NUChannelData mediaValue]
+ -[NUChannelData metadataValue]
+ -[NUChannelData numberValue]
+ -[NUChannelData opaqueArrayValue]
+ -[NUChannelData opaqueDataValue]
+ -[NUChannelData opaqueDictionaryValue]
+ -[NUChannelData opaqueStringValue]
+ -[NUChannelData opaqueValue]
+ -[NUChannelData rectangleValue]
+ -[NUChannelData stringEnumValue]
+ -[NUChannelData timeValue]
+ -[NUChannelData valueOfType:]
+ -[NUChannelElementData _untypedValue]
+ -[NUChannelExpression contains:]
+ -[NUChannelExpressionData _untypedValue]
+ -[NUChannelForceUnwrapExpression compactDescription]
+ -[NUChannelForceUnwrapExpression description]
+ -[NUChannelForceUnwrapExpression evaluateWithData:outputFormat:error:]
+ -[NUChannelForceUnwrapExpression formatWithData:error:]
+ -[NUChannelForceUnwrapExpression hash]
+ -[NUChannelForceUnwrapExpression isEqualToExpression:]
+ -[NUChannelFormat canAcceptOptionalDataWithFormat:]
+ -[NUChannelFormat shortDescription]
+ -[NUChannelMediaData _untypedValue]
+ -[NUChannelMediaData mediaValue]
+ -[NUChannelMediaFormat componentMediaType]
+ -[NUChannelMetadata _untypedValue]
+ -[NUChannelMetadata metadataValue]
+ -[NUChannelNilCoalesceExpression compactDescription]
+ -[NUChannelNilCoalesceExpression description]
+ -[NUChannelNilCoalesceExpression evaluateWithLeftData:rightData:outputFormat:error:]
+ -[NUChannelNilCoalesceExpression formatWithLeftData:rightData:error:]
+ -[NUChannelNilCoalesceExpression hash]
+ -[NUChannelNilCoalesceExpression isEqualToExpression:]
+ -[NUChannelNilCoalesceExpression isEqualToNilCoalesceExpression:]
+ -[NUChannelNullData _untypedValue]
+ -[NUCompoundDescriptor descriptorWithValueType:]
+ -[NUCompoundDescriptor identifier]
+ -[NUCompoundDescriptor initWithProperties:identifier:]
+ -[NUCompoundDescriptor initWithProperties:identifier:valueType:]
+ -[NUCompoundDescriptor initWithValueType:]
+ -[NUCompoundDescriptor shortDescription]
+ -[NUControlDescriptor defaultValue]
+ -[NUControlDescriptor descriptorWithObjectType:]
+ -[NUControlDescriptor descriptorWithValueType:]
+ -[NUControlDescriptor enforceValidValue:]
+ -[NUControlDescriptor initWithValueType:]
+ -[NUControlDescriptor isValue:equalToValue:]
+ -[NUControlDescriptor shortDescription]
+ -[NUControlDescriptor validate:error:]
+ -[NUControlDescriptor valueType]
+ -[NUCoreImageFilterPipelineProcessor identifier]
+ -[NUEnumDescriptor debugDescription]
+ -[NUEnumDescriptor descriptorWithValueType:]
+ -[NUEnumDescriptor enumValueType]
+ -[NUEnumDescriptor identifier]
+ -[NUEnumDescriptor initWithEnumValueType:values:identifier:valueType:]
+ -[NUEnumDescriptor initWithIntegerValues:identifier:]
+ -[NUEnumDescriptor initWithStringValues:identifier:]
+ -[NUEnumDescriptor initWithValueType:]
+ -[NUEnumDescriptor initWithValues:valueType:]
+ -[NUEnumDescriptor isEqualToEnumDescriptor:]
+ -[NUGlobalSettings setStandardPreviewSizeInMegapixels:]
+ -[NUGlobalSettings standardPreviewSizeInMegapixels]
+ -[NUMediaGeometryDescriptor controlType]
+ -[NUMediaGeometryDescriptor defaultValueType]
+ -[NUMediaGeometryDescriptor descriptorWithValueType:]
+ -[NUMediaGeometryDescriptor initWithProperties:identifier:]
+ -[NUMediaGeometryDescriptor initWithProperties:identifier:valueType:]
+ -[NUMediaGeometryDescriptor initWithValueType:]
+ -[NUNumberDescriptor descriptorWithValueType:]
+ -[NUNumberDescriptor enforceValidValue:]
+ -[NUNumberDescriptor initWithNumberType:min:max:precision:]
+ -[NUNumberDescriptor initWithNumberType:min:max:precision:valueType:]
+ -[NUNumberDescriptor initWithValueType:]
+ -[NUNumberDescriptor isValue:equalToValue:]
+ -[NUNumberDescriptor precision]
+ -[NUNumberDescriptor validBoolValue:]
+ -[NUNumberDescriptor validDoubleValue:]
+ -[NUNumberDescriptor validIntegerValue:]
+ -[NUOpaqueDescriptor canAcceptDataWithDescriptor:]
+ -[NUOpaqueDescriptor descriptorWithValueType:]
+ -[NUOpaqueDescriptor initWithIdentifier:valueType:]
+ -[NUOpaqueDescriptor initWithValueType:]
+ -[NUOptionalDescriptor canAcceptDataWithNonOptionalDescriptor:]
+ -[NUOptionalDescriptor canAcceptDataWithOptionalDescriptor:]
+ -[NUOptionalDescriptor descriptorWithValueType:]
+ -[NUOptionalDescriptor enforceValidValue:]
+ -[NUOptionalDescriptor initWithDescriptor:optionality:validatedDefaultValue:]
+ -[NUOptionalDescriptor initWithValueType:]
+ -[NUOptionalDescriptor optionality]
+ -[NUOptionalDescriptor valueType]
+ -[NUPipelineProcessor identifier]
+ -[NURectDescriptor descriptorWithValueType:]
+ -[NURunQueue synchronize:]
+ -[NURunQueueLane synchronize:]
+ -[NUStandardPreviewScalePolicy .cxx_destruct]
+ -[NUStandardPreviewScalePolicy init]
+ -[NUStandardPreviewScalePolicy scaleForImageGeometry:]
+ -[NUStandardPreviewScalePolicy scaleForImageSize:]
+ -[NUTimeDescriptor descriptorWithValueType:]
+ -[NUVectorDescriptor descriptorWithValueType:]
+ -[NUVectorDescriptor initWithElement:size:valueType:]
+ -[NUVectorDescriptor initWithValueType:]
+ -[_NUAsset addCapability:value:]
+ -[_NUContainerPipeline .cxx_destruct]
+ -[_NUContainerPipeline componentFormat]
+ -[_NUContainerPipeline componentInputPort]
+ -[_NUContainerPipeline componentOutputPort]
+ -[_NUContainerPipeline initWithContainerFormat:componentFormat:]
+ -[_NUHDRToneMapLearnPipeline _genericInputPortsMatchingOutputPort:]
+ -[_NUHDRToneMapLearnPipeline _genericOutputPortsMatchingInputPort:]
+ -[_NULivePhotoRenderResult image]
+ -[_NULivePhotoRenderResult setImage:]
+ -[_NUPipeline addContainerPipelineWithContainerFormat:componentFormat:block:]
+ -[_NUPipeline addContainerPipelineWithContainerFormat:componentFormat:block:error:]
+ -[_NUPipeline insertContainerMapAt:containerFormat:componentFormat:block:error:]
+ -[_NUPipeline insertContainerMapAt:input:componentFormat:block:error:]
+ -[_NUPipeline processContainer:componentFormat:forEachComponent:error:]
+ -[_NUPipeline processContainerPort:componentFormat:forEachComponentPort:error:]
+ -[_NURawDecodeCapability format]
+ -[_NURawDecodePipeline rawForceDraftModeWithOptions:]
+ -[_NURenderNodePipeline _formatForInput:]
+ -[_NUStyleEngineMemoryResource metalCommandQueue]
+ -[_NUStyleEngineMemoryResource setMetalCommandQueue:]
+ GCC_except_table10007
+ GCC_except_table10014
+ GCC_except_table10019
+ GCC_except_table10021
+ GCC_except_table10139
+ GCC_except_table1035
+ GCC_except_table10378
+ GCC_except_table10385
+ GCC_except_table10595
+ GCC_except_table10855
+ GCC_except_table1107
+ GCC_except_table11134
+ GCC_except_table11137
+ GCC_except_table11292
+ GCC_except_table11300
+ GCC_except_table11301
+ GCC_except_table11306
+ GCC_except_table11311
+ GCC_except_table11316
+ GCC_except_table11336
+ GCC_except_table11343
+ GCC_except_table11344
+ GCC_except_table11345
+ GCC_except_table11346
+ GCC_except_table11549
+ GCC_except_table11561
+ GCC_except_table11564
+ GCC_except_table11569
+ GCC_except_table11585
+ GCC_except_table11603
+ GCC_except_table11606
+ GCC_except_table11607
+ GCC_except_table11611
+ GCC_except_table11612
+ GCC_except_table11722
+ GCC_except_table11747
+ GCC_except_table11749
+ GCC_except_table11774
+ GCC_except_table11845
+ GCC_except_table11847
+ GCC_except_table11849
+ GCC_except_table11854
+ GCC_except_table11863
+ GCC_except_table11864
+ GCC_except_table1249
+ GCC_except_table1261
+ GCC_except_table132
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table2018
+ GCC_except_table232
+ GCC_except_table2350
+ GCC_except_table24
+ GCC_except_table2493
+ GCC_except_table2509
+ GCC_except_table2523
+ GCC_except_table2526
+ GCC_except_table2536
+ GCC_except_table2548
+ GCC_except_table2553
+ GCC_except_table2571
+ GCC_except_table2573
+ GCC_except_table2574
+ GCC_except_table2579
+ GCC_except_table2580
+ GCC_except_table2582
+ GCC_except_table2583
+ GCC_except_table2594
+ GCC_except_table2598
+ GCC_except_table26
+ GCC_except_table2600
+ GCC_except_table2620
+ GCC_except_table2623
+ GCC_except_table2628
+ GCC_except_table2631
+ GCC_except_table2633
+ GCC_except_table2638
+ GCC_except_table2652
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2660
+ GCC_except_table2661
+ GCC_except_table2673
+ GCC_except_table2907
+ GCC_except_table2908
+ GCC_except_table2909
+ GCC_except_table2910
+ GCC_except_table2911
+ GCC_except_table2913
+ GCC_except_table2915
+ GCC_except_table2930
+ GCC_except_table2931
+ GCC_except_table2932
+ GCC_except_table2945
+ GCC_except_table2946
+ GCC_except_table2947
+ GCC_except_table2948
+ GCC_except_table2963
+ GCC_except_table2964
+ GCC_except_table2978
+ GCC_except_table2979
+ GCC_except_table2984
+ GCC_except_table3024
+ GCC_except_table3053
+ GCC_except_table3054
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table3835
+ GCC_except_table3836
+ GCC_except_table3840
+ GCC_except_table3841
+ GCC_except_table3842
+ GCC_except_table3843
+ GCC_except_table3851
+ GCC_except_table3860
+ GCC_except_table3870
+ GCC_except_table3876
+ GCC_except_table3877
+ GCC_except_table3878
+ GCC_except_table3881
+ GCC_except_table3883
+ GCC_except_table3886
+ GCC_except_table3887
+ GCC_except_table3888
+ GCC_except_table3904
+ GCC_except_table3906
+ GCC_except_table3924
+ GCC_except_table3976
+ GCC_except_table3980
+ GCC_except_table4008
+ GCC_except_table4126
+ GCC_except_table4210
+ GCC_except_table4216
+ GCC_except_table4224
+ GCC_except_table4301
+ GCC_except_table4305
+ GCC_except_table4306
+ GCC_except_table4308
+ GCC_except_table4310
+ GCC_except_table4312
+ GCC_except_table4315
+ GCC_except_table4316
+ GCC_except_table4318
+ GCC_except_table4319
+ GCC_except_table4320
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4333
+ GCC_except_table4334
+ GCC_except_table4339
+ GCC_except_table4340
+ GCC_except_table4341
+ GCC_except_table4342
+ GCC_except_table4344
+ GCC_except_table4345
+ GCC_except_table4346
+ GCC_except_table4347
+ GCC_except_table4349
+ GCC_except_table4350
+ GCC_except_table4351
+ GCC_except_table4352
+ GCC_except_table4353
+ GCC_except_table4354
+ GCC_except_table4355
+ GCC_except_table4358
+ GCC_except_table4359
+ GCC_except_table4362
+ GCC_except_table4363
+ GCC_except_table4364
+ GCC_except_table4370
+ GCC_except_table4371
+ GCC_except_table4372
+ GCC_except_table4374
+ GCC_except_table4375
+ GCC_except_table4376
+ GCC_except_table4378
+ GCC_except_table4380
+ GCC_except_table4381
+ GCC_except_table4382
+ GCC_except_table4387
+ GCC_except_table4388
+ GCC_except_table4389
+ GCC_except_table4390
+ GCC_except_table4391
+ GCC_except_table4393
+ GCC_except_table4394
+ GCC_except_table4395
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4398
+ GCC_except_table4399
+ GCC_except_table4400
+ GCC_except_table4405
+ GCC_except_table4406
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4409
+ GCC_except_table4410
+ GCC_except_table4463
+ GCC_except_table4485
+ GCC_except_table4486
+ GCC_except_table4489
+ GCC_except_table4490
+ GCC_except_table4495
+ GCC_except_table4496
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4501
+ GCC_except_table4502
+ GCC_except_table4504
+ GCC_except_table4505
+ GCC_except_table4507
+ GCC_except_table4513
+ GCC_except_table4517
+ GCC_except_table4521
+ GCC_except_table4522
+ GCC_except_table4523
+ GCC_except_table4525
+ GCC_except_table4532
+ GCC_except_table4534
+ GCC_except_table4535
+ GCC_except_table4587
+ GCC_except_table472
+ GCC_except_table4785
+ GCC_except_table4864
+ GCC_except_table4865
+ GCC_except_table4869
+ GCC_except_table4871
+ GCC_except_table4875
+ GCC_except_table4877
+ GCC_except_table4879
+ GCC_except_table4880
+ GCC_except_table4884
+ GCC_except_table4888
+ GCC_except_table4889
+ GCC_except_table4890
+ GCC_except_table4891
+ GCC_except_table4892
+ GCC_except_table4894
+ GCC_except_table4895
+ GCC_except_table4897
+ GCC_except_table4898
+ GCC_except_table4908
+ GCC_except_table491
+ GCC_except_table4910
+ GCC_except_table492
+ GCC_except_table493
+ GCC_except_table4936
+ GCC_except_table4939
+ GCC_except_table4940
+ GCC_except_table4941
+ GCC_except_table4942
+ GCC_except_table4943
+ GCC_except_table4944
+ GCC_except_table4945
+ GCC_except_table4946
+ GCC_except_table4947
+ GCC_except_table4949
+ GCC_except_table4950
+ GCC_except_table4951
+ GCC_except_table4952
+ GCC_except_table4953
+ GCC_except_table4954
+ GCC_except_table4955
+ GCC_except_table4956
+ GCC_except_table4957
+ GCC_except_table4958
+ GCC_except_table4959
+ GCC_except_table496
+ GCC_except_table4960
+ GCC_except_table4961
+ GCC_except_table4966
+ GCC_except_table4967
+ GCC_except_table497
+ GCC_except_table4973
+ GCC_except_table4974
+ GCC_except_table4979
+ GCC_except_table498
+ GCC_except_table4980
+ GCC_except_table4981
+ GCC_except_table4983
+ GCC_except_table4984
+ GCC_except_table4985
+ GCC_except_table4986
+ GCC_except_table4987
+ GCC_except_table4992
+ GCC_except_table4993
+ GCC_except_table4994
+ GCC_except_table4995
+ GCC_except_table4997
+ GCC_except_table4998
+ GCC_except_table5002
+ GCC_except_table5003
+ GCC_except_table5004
+ GCC_except_table5005
+ GCC_except_table5006
+ GCC_except_table5007
+ GCC_except_table5008
+ GCC_except_table5009
+ GCC_except_table5011
+ GCC_except_table5013
+ GCC_except_table5016
+ GCC_except_table5017
+ GCC_except_table5018
+ GCC_except_table5019
+ GCC_except_table5020
+ GCC_except_table5022
+ GCC_except_table5024
+ GCC_except_table5025
+ GCC_except_table5026
+ GCC_except_table5027
+ GCC_except_table5035
+ GCC_except_table5129
+ GCC_except_table515
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table5218
+ GCC_except_table522
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table534
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table538
+ GCC_except_table540
+ GCC_except_table5451
+ GCC_except_table5465
+ GCC_except_table5477
+ GCC_except_table5500
+ GCC_except_table5512
+ GCC_except_table5517
+ GCC_except_table5607
+ GCC_except_table5610
+ GCC_except_table5619
+ GCC_except_table5644
+ GCC_except_table5709
+ GCC_except_table5717
+ GCC_except_table5732
+ GCC_except_table576
+ GCC_except_table5831
+ GCC_except_table5838
+ GCC_except_table5839
+ GCC_except_table5840
+ GCC_except_table5841
+ GCC_except_table5842
+ GCC_except_table5845
+ GCC_except_table5846
+ GCC_except_table5849
+ GCC_except_table5852
+ GCC_except_table5853
+ GCC_except_table5855
+ GCC_except_table5858
+ GCC_except_table5859
+ GCC_except_table5860
+ GCC_except_table5861
+ GCC_except_table5862
+ GCC_except_table5863
+ GCC_except_table5864
+ GCC_except_table5865
+ GCC_except_table5873
+ GCC_except_table5874
+ GCC_except_table5879
+ GCC_except_table5886
+ GCC_except_table5902
+ GCC_except_table5903
+ GCC_except_table5909
+ GCC_except_table5911
+ GCC_except_table5914
+ GCC_except_table5915
+ GCC_except_table5919
+ GCC_except_table5922
+ GCC_except_table5923
+ GCC_except_table5925
+ GCC_except_table5926
+ GCC_except_table5929
+ GCC_except_table5931
+ GCC_except_table5933
+ GCC_except_table5934
+ GCC_except_table5935
+ GCC_except_table5936
+ GCC_except_table5937
+ GCC_except_table5941
+ GCC_except_table5947
+ GCC_except_table6150
+ GCC_except_table643
+ GCC_except_table65
+ GCC_except_table652
+ GCC_except_table672
+ GCC_except_table6735
+ GCC_except_table689
+ GCC_except_table7037
+ GCC_except_table7045
+ GCC_except_table7050
+ GCC_except_table7051
+ GCC_except_table7055
+ GCC_except_table7125
+ GCC_except_table7154
+ GCC_except_table7160
+ GCC_except_table7173
+ GCC_except_table7228
+ GCC_except_table7296
+ GCC_except_table7306
+ GCC_except_table7333
+ GCC_except_table7334
+ GCC_except_table7384
+ GCC_except_table7549
+ GCC_except_table7583
+ GCC_except_table7592
+ GCC_except_table7615
+ GCC_except_table7619
+ GCC_except_table7621
+ GCC_except_table7622
+ GCC_except_table7623
+ GCC_except_table763
+ GCC_except_table7647
+ GCC_except_table7698
+ GCC_except_table7699
+ GCC_except_table7700
+ GCC_except_table7701
+ GCC_except_table7706
+ GCC_except_table7712
+ GCC_except_table7713
+ GCC_except_table7720
+ GCC_except_table7723
+ GCC_except_table7730
+ GCC_except_table7732
+ GCC_except_table7733
+ GCC_except_table7735
+ GCC_except_table7736
+ GCC_except_table7737
+ GCC_except_table7738
+ GCC_except_table7743
+ GCC_except_table7745
+ GCC_except_table7746
+ GCC_except_table7747
+ GCC_except_table7748
+ GCC_except_table7752
+ GCC_except_table7753
+ GCC_except_table7755
+ GCC_except_table7757
+ GCC_except_table7759
+ GCC_except_table7761
+ GCC_except_table7767
+ GCC_except_table7770
+ GCC_except_table7774
+ GCC_except_table7775
+ GCC_except_table7777
+ GCC_except_table7778
+ GCC_except_table7779
+ GCC_except_table7780
+ GCC_except_table7781
+ GCC_except_table7783
+ GCC_except_table7784
+ GCC_except_table7785
+ GCC_except_table7786
+ GCC_except_table7787
+ GCC_except_table7788
+ GCC_except_table7789
+ GCC_except_table7790
+ GCC_except_table7791
+ GCC_except_table7792
+ GCC_except_table7793
+ GCC_except_table7794
+ GCC_except_table7795
+ GCC_except_table7796
+ GCC_except_table7797
+ GCC_except_table7798
+ GCC_except_table7799
+ GCC_except_table7800
+ GCC_except_table7900
+ GCC_except_table7929
+ GCC_except_table8014
+ GCC_except_table8208
+ GCC_except_table8223
+ GCC_except_table8260
+ GCC_except_table8267
+ GCC_except_table8318
+ GCC_except_table8363
+ GCC_except_table8507
+ GCC_except_table8512
+ GCC_except_table8515
+ GCC_except_table8538
+ GCC_except_table8879
+ GCC_except_table8883
+ GCC_except_table8919
+ GCC_except_table8923
+ GCC_except_table8925
+ GCC_except_table8986
+ GCC_except_table9000
+ GCC_except_table9040
+ GCC_except_table9072
+ GCC_except_table9073
+ GCC_except_table9141
+ GCC_except_table9330
+ GCC_except_table9341
+ GCC_except_table9343
+ GCC_except_table9344
+ GCC_except_table9505
+ GCC_except_table9532
+ GCC_except_table9556
+ GCC_except_table9564
+ GCC_except_table9688
+ GCC_except_table9945
+ _NUAssetPipelineOptionRawDecodeDraftMode
+ _NUControlOptionalityDescription
+ _NUEnumValueClassForValueType
+ _NUEnumValueTypeDescription
+ _NURawDecodeDraftModeAuto
+ _NURawDecodeDraftModeDisabled
+ _NURawDecodeDraftModeEnabled
+ _OBJC_CLASS_$_NUChannelContainsExpression
+ _OBJC_CLASS_$_NUChannelForceUnwrapExpression
+ _OBJC_CLASS_$_NUChannelNilCoalesceExpression
+ _OBJC_CLASS_$_NUStandardPreviewScalePolicy
+ _OBJC_CLASS_$__NURawDecodeCapability
+ _OBJC_IVAR_$_NUChannelControlFormat._descriptor
+ _OBJC_IVAR_$_NUCompoundDescriptor._identifier
+ _OBJC_IVAR_$_NUControlDescriptor._valueType
+ _OBJC_IVAR_$_NUEnumDescriptor._enumValueType
+ _OBJC_IVAR_$_NUEnumDescriptor._identifier
+ _OBJC_IVAR_$_NUNumberDescriptor._precision
+ _OBJC_IVAR_$_NUOptionalDescriptor._defaultValue
+ _OBJC_IVAR_$_NUOptionalDescriptor._optionality
+ _OBJC_IVAR_$_NUStandardPreviewScalePolicy._actualPolicy
+ _OBJC_IVAR_$__NUContainerPipeline._componentFormat
+ _OBJC_IVAR_$__NUContainerPipeline._componentInputPort
+ _OBJC_IVAR_$__NUContainerPipeline._componentOutputPort
+ _OBJC_IVAR_$__NULivePhotoRenderResult._image
+ _OBJC_IVAR_$__NUStyleEngineMemoryResource._metalCommandQueue
+ _OBJC_METACLASS_$_NUChannelContainsExpression
+ _OBJC_METACLASS_$_NUChannelForceUnwrapExpression
+ _OBJC_METACLASS_$_NUChannelNilCoalesceExpression
+ _OBJC_METACLASS_$_NUStandardPreviewScalePolicy
+ _OBJC_METACLASS_$__NURawDecodeCapability
+ _OUTLINED_FUNCTION_38
+ __OBJC_$_CATEGORY_CIVector_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_CLASS_METHODS_CIVector_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSArray_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSNumber_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSArray_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSDictionary_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSNull_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSNumber_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSObject_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSString_$_NUControlDataRepresentable
+ __OBJC_$_CATEGORY_NSValue_$_NUControlDataRepresentable
+ __OBJC_$_CLASS_METHODS_NSObject(NUControlDataRepresentable|NUDigest|NURenderPipelineFunction|NUUtilities)
+ __OBJC_$_CLASS_METHODS_NSValue(NUControlDataRepresentable|NUDigest|NUGeometryExtensions)
+ __OBJC_$_CLASS_METHODS_NUAssetCapability(NURawDecode)
+ __OBJC_$_CLASS_METHODS_NUEnumDescriptor
+ __OBJC_$_CLASS_METHODS__NURawDecodeCapability
+ __OBJC_$_CLASS_PROP_LIST_NUEnumDescriptor
+ __OBJC_$_INSTANCE_METHODS_CIVector(NUControlDataRepresentable|NUDigest)
+ __OBJC_$_INSTANCE_METHODS_NSArray(NUControlDataRepresentable|NUDigest|NURenderPipelineFunction)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(NUControlDataRepresentable|NUDigest|NURenderPipelineFunction)
+ __OBJC_$_INSTANCE_METHODS_NSNull(NUControlDataRepresentable|NUDigest)
+ __OBJC_$_INSTANCE_METHODS_NSNumber(NUControlDataRepresentable|NUEnumValueRepresentable|NUSchemaAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSObject(NUControlDataRepresentable|NUDigest|NURenderPipelineFunction|NUUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSString(NUControlDataRepresentable|NUEnumValueRepresentable|NUDigest)
+ __OBJC_$_INSTANCE_METHODS_NSValue(NUControlDataRepresentable|NUDigest|NUGeometryExtensions)
+ __OBJC_$_INSTANCE_METHODS_NUCIImageSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS_NUChannelContainsExpression
+ __OBJC_$_INSTANCE_METHODS_NUChannelForceUnwrapExpression
+ __OBJC_$_INSTANCE_METHODS_NUChannelNilCoalesceExpression
+ __OBJC_$_INSTANCE_METHODS_NUFileSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS_NULivePhotoSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS_NUMultipleSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS_NURenderJob(DebugAdditions|Media|RendererSupport)
+ __OBJC_$_INSTANCE_METHODS_NUSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS_NUStandardPreviewScalePolicy
+ __OBJC_$_INSTANCE_METHODS_NUVideoDataSourceDefinition(NUAssetLoader|NodeProvider)
+ __OBJC_$_INSTANCE_METHODS__NURawDecodeCapability
+ __OBJC_$_INSTANCE_VARIABLES_NUStandardPreviewScalePolicy
+ __OBJC_$_INSTANCE_VARIABLES__NUContainerPipeline
+ __OBJC_$_PROP_LIST_NSObject_$_NUControlDataRepresentable
+ __OBJC_$_PROP_LIST_NUStandardPreviewScalePolicy
+ __OBJC_$_PROP_LIST__NUContainerPipeline
+ __OBJC_$_PROTOCOL_REFS_NUEnumValueRepresentable
+ __OBJC_CATEGORY_PROTOCOLS_$_NSObject_$_NUControlDataRepresentable
+ __OBJC_CLASS_PROTOCOLS_$_NSNumber(NUControlDataRepresentable|NUEnumValueRepresentable|NUSchemaAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_NSString(NUControlDataRepresentable|NUEnumValueRepresentable|NUDigest)
+ __OBJC_CLASS_PROTOCOLS_$_NUStandardPreviewScalePolicy
+ __OBJC_CLASS_RO_$_NUChannelContainsExpression
+ __OBJC_CLASS_RO_$_NUChannelForceUnwrapExpression
+ __OBJC_CLASS_RO_$_NUChannelNilCoalesceExpression
+ __OBJC_CLASS_RO_$_NUStandardPreviewScalePolicy
+ __OBJC_CLASS_RO_$__NURawDecodeCapability
+ __OBJC_LABEL_PROTOCOL_$_NUEnumValueRepresentable
+ __OBJC_METACLASS_RO_$_NUChannelContainsExpression
+ __OBJC_METACLASS_RO_$_NUChannelForceUnwrapExpression
+ __OBJC_METACLASS_RO_$_NUChannelNilCoalesceExpression
+ __OBJC_METACLASS_RO_$_NUStandardPreviewScalePolicy
+ __OBJC_METACLASS_RO_$__NURawDecodeCapability
+ __OBJC_PROTOCOL_$_NUEnumValueRepresentable
+ ___101+[_NUStyleEngineMemoryResource usingSharedMemoryResourceForMetalCommandQueue:withDescriptor:perform:]_block_invoke
+ ___26-[NURunQueue synchronize:]_block_invoke
+ ___41-[NURenderContext _dequeueRateLimitedJob]_block_invoke
+ ___51-[NUGlobalSettings standardPreviewSizeInMegapixels]_block_invoke
+ ___51-[_NURawProfilePipeline_v0 buildWithOptions:error:]_block_invoke_2
+ ___51-[_NURawProfilePipeline_v1 buildWithOptions:error:]_block_invoke_2
+ ___67-[_NUHDRToneMapLearnPipeline _genericInputPortsMatchingOutputPort:]_block_invoke
+ ___67-[_NUHDRToneMapLearnPipeline _genericOutputPortsMatchingInputPort:]_block_invoke
+ ___70-[NUEnumDescriptor initWithEnumValueType:values:identifier:valueType:]_block_invoke
+ ___71-[_NUPipeline processContainer:componentFormat:forEachComponent:error:]_block_invoke
+ ___77-[_NUPipeline addContainerPipelineWithContainerFormat:componentFormat:block:]_block_invoke
+ ___79-[_NUPipeline processContainerPort:componentFormat:forEachComponentPort:error:]_block_invoke
+ ___block_descriptor_32_e28_B32?0"NURenderJob"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e73_"NUChannelPortRef"32?0"_NUContainerPipeline"8"NUChannelPortRef"16^24ls32l8
+ ___block_descriptor_40_e8_32s_e35_"_NUChannelPort"16?0"NUChannel"8ls32l8
+ ___block_descriptor_40_e8_B16?08lu32l8
+ ___block_descriptor_56_e8_32s40r48r_e42_v32?0"NSString"8"NUChannelFormat"16^B24lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ _associated conformance So20NURawDecodeDraftModeaSHSCSQ
+ _associated conformance So20NURawDecodeDraftModeas12CaseIterable12NeutrinoCore8AllCasessACP_Sl
+ _associated conformance So20NURawDecodeDraftModeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So20NURawDecodeDraftModeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _kCMMetadataBaseDataType_ISOLatin1
+ _kCMMetadataBaseDataType_MacRoman
+ _kCMMetadataBaseDataType_RawData
+ _kCMMetadataBaseDataType_UTF16
+ _kCMMetadataBaseDataType_UTF8
+ _symbolic Say_____G So20NURawDecodeDraftModea
+ _symbolic _____ So20NURawDecodeDraftModea
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So20NURawDecodeDraftModea
+ _type_layout_string So20NURawDecodeDraftModea
+ _type_layout_string So7NUScalea
- +[NUAssetCapability rawDecodeCapabilityFormat]
- +[NUAssetCapability rawDecode]
- +[NUChannel controlChannelWithSchema:]
- +[NUChannel controlChannelWithSchema:name:]
- +[NUChannel controlChannelWithSetting:name:]
- +[NUChannelControlData controlDataWithAdjustment:]
- +[NUChannelControlData controlDataWithComposition:]
- +[NUChannelControlData controlDataWithSetting:value:]
- +[NUChannelControlData controlDataWithSource:]
- +[NUChannelControlFormat controlFormatWithSchema:]
- +[NUChannelControlFormat controlFormatWithSetting:]
- +[NUChannelData adjustment:]
- +[NUChannelData composition:]
- +[_NUStyleEngineMemoryResource usingSharedMemoryResourceForDevice:withDescriptor:perform:]
- -[NUChannelArrayData value]
- -[NUChannelControlData initWithData:schema:]
- -[NUChannelControlData initWithSetting:value:]
- -[NUChannelControlData value]
- -[NUChannelControlFormat controlType]
- -[NUChannelControlFormat dataModel]
- -[NUChannelControlFormat descriptor:canAcceptSetting:]
- -[NUChannelControlFormat initWithControlType:dataModel:]
- -[NUChannelControlFormat initWithControlType:dataModel:valueType:]
- -[NUChannelControlFormat setting:canAcceptDescriptor:]
- -[NUChannelData value]
- -[NUChannelElementData value]
- -[NUChannelExpressionData value]
- -[NUChannelMediaData value]
- -[NUChannelMetadata value]
- -[NUChannelNullData value]
- -[NUControlDescriptor initWithAttributes:]
- -[NUOptionalDescriptor descriptorDefault]
- -[_NUAsset addCapability:data:]
- -[_NUContainerPipeline init]
- -[_NUPipeline addContainerPipeline:]
- -[_NUPipeline addContainerPipeline:error:]
- -[_NUPipeline processContainer:forEachComponent:error:]
- -[_NUPipeline processContainerPort:forEachComponentPort:error:]
- GCC_except_table10053
- GCC_except_table10101
- GCC_except_table10125
- GCC_except_table10126
- GCC_except_table10130
- GCC_except_table10131
- GCC_except_table10132
- GCC_except_table10133
- GCC_except_table10141
- GCC_except_table10150
- GCC_except_table10160
- GCC_except_table10166
- GCC_except_table10167
- GCC_except_table10168
- GCC_except_table10171
- GCC_except_table10173
- GCC_except_table10176
- GCC_except_table10177
- GCC_except_table10178
- GCC_except_table10252
- GCC_except_table10262
- GCC_except_table10477
- GCC_except_table10478
- GCC_except_table10484
- GCC_except_table10485
- GCC_except_table10487
- GCC_except_table10488
- GCC_except_table105
- GCC_except_table10585
- GCC_except_table10586
- GCC_except_table10589
- GCC_except_table10590
- GCC_except_table10591
- GCC_except_table10592
- GCC_except_table10593
- GCC_except_table10594
- GCC_except_table10596
- GCC_except_table10599
- GCC_except_table106
- GCC_except_table10600
- GCC_except_table10602
- GCC_except_table10603
- GCC_except_table10604
- GCC_except_table10606
- GCC_except_table10607
- GCC_except_table10617
- GCC_except_table10618
- GCC_except_table10623
- GCC_except_table10624
- GCC_except_table10625
- GCC_except_table10626
- GCC_except_table10628
- GCC_except_table10629
- GCC_except_table10630
- GCC_except_table10631
- GCC_except_table10634
- GCC_except_table10635
- GCC_except_table10636
- GCC_except_table10638
- GCC_except_table10639
- GCC_except_table10642
- GCC_except_table10643
- GCC_except_table10646
- GCC_except_table10647
- GCC_except_table10648
- GCC_except_table10654
- GCC_except_table10655
- GCC_except_table10656
- GCC_except_table10657
- GCC_except_table10658
- GCC_except_table10659
- GCC_except_table10661
- GCC_except_table10663
- GCC_except_table10664
- GCC_except_table10665
- GCC_except_table10670
- GCC_except_table10671
- GCC_except_table10672
- GCC_except_table10673
- GCC_except_table10674
- GCC_except_table10676
- GCC_except_table10677
- GCC_except_table10678
- GCC_except_table10679
- GCC_except_table10680
- GCC_except_table10681
- GCC_except_table10682
- GCC_except_table10683
- GCC_except_table10688
- GCC_except_table10689
- GCC_except_table10690
- GCC_except_table10691
- GCC_except_table10692
- GCC_except_table10693
- GCC_except_table10739
- GCC_except_table10790
- GCC_except_table108
- GCC_except_table1083
- GCC_except_table10867
- GCC_except_table10871
- GCC_except_table109
- GCC_except_table11377
- GCC_except_table11538
- GCC_except_table11540
- GCC_except_table11586
- GCC_except_table11638
- GCC_except_table11646
- GCC_except_table11651
- GCC_except_table11652
- GCC_except_table11656
- GCC_except_table1278
- GCC_except_table1282
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1292
- GCC_except_table1295
- GCC_except_table1296
- GCC_except_table1297
- GCC_except_table1318
- GCC_except_table1327
- GCC_except_table1350
- GCC_except_table1354
- GCC_except_table1356
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1368
- GCC_except_table1418
- GCC_except_table1420
- GCC_except_table1638
- GCC_except_table1652
- GCC_except_table1664
- GCC_except_table1687
- GCC_except_table1699
- GCC_except_table1704
- GCC_except_table173
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table1806
- GCC_except_table1831
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1923
- GCC_except_table2049
- GCC_except_table2050
- GCC_except_table2051
- GCC_except_table2052
- GCC_except_table2053
- GCC_except_table2055
- GCC_except_table2080
- GCC_except_table2243
- GCC_except_table2244
- GCC_except_table2720
- GCC_except_table2800
- GCC_except_table2944
- GCC_except_table2956
- GCC_except_table3119
- GCC_except_table3266
- GCC_except_table3346
- GCC_except_table335
- GCC_except_table3353
- GCC_except_table3354
- GCC_except_table3355
- GCC_except_table3356
- GCC_except_table3357
- GCC_except_table3360
- GCC_except_table3361
- GCC_except_table3364
- GCC_except_table3367
- GCC_except_table3368
- GCC_except_table3370
- GCC_except_table3373
- GCC_except_table3374
- GCC_except_table3375
- GCC_except_table3376
- GCC_except_table3377
- GCC_except_table3378
- GCC_except_table3379
- GCC_except_table3380
- GCC_except_table3388
- GCC_except_table3391
- GCC_except_table3392
- GCC_except_table3397
- GCC_except_table3404
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3426
- GCC_except_table3427
- GCC_except_table3429
- GCC_except_table343
- GCC_except_table3432
- GCC_except_table3433
- GCC_except_table3437
- GCC_except_table3440
- GCC_except_table3441
- GCC_except_table3443
- GCC_except_table3444
- GCC_except_table3447
- GCC_except_table3449
- GCC_except_table3451
- GCC_except_table3452
- GCC_except_table3453
- GCC_except_table3454
- GCC_except_table3455
- GCC_except_table3459
- GCC_except_table3465
- GCC_except_table358
- GCC_except_table398
- GCC_except_table4031
- GCC_except_table4102
- GCC_except_table4106
- GCC_except_table4108
- GCC_except_table4248
- GCC_except_table4256
- GCC_except_table4257
- GCC_except_table426
- GCC_except_table4262
- GCC_except_table4267
- GCC_except_table4272
- GCC_except_table4295
- GCC_except_table432
- GCC_except_table4436
- GCC_except_table4437
- GCC_except_table4438
- GCC_except_table4441
- GCC_except_table4442
- GCC_except_table4443
- GCC_except_table4448
- GCC_except_table4450
- GCC_except_table4455
- GCC_except_table4456
- GCC_except_table4457
- GCC_except_table4459
- GCC_except_table4461
- GCC_except_table4476
- GCC_except_table4478
- GCC_except_table4539
- GCC_except_table4540
- GCC_except_table4543
- GCC_except_table4544
- GCC_except_table4549
- GCC_except_table4550
- GCC_except_table4553
- GCC_except_table4554
- GCC_except_table4555
- GCC_except_table4556
- GCC_except_table4557
- GCC_except_table4558
- GCC_except_table4559
- GCC_except_table4561
- GCC_except_table4567
- GCC_except_table4571
- GCC_except_table4575
- GCC_except_table4576
- GCC_except_table4577
- GCC_except_table4579
- GCC_except_table4588
- GCC_except_table4589
- GCC_except_table4664
- GCC_except_table479
- GCC_except_table4982
- GCC_except_table5098
- GCC_except_table5104
- GCC_except_table5107
- GCC_except_table5117
- GCC_except_table5121
- GCC_except_table5122
- GCC_except_table5136
- GCC_except_table5245
- GCC_except_table5347
- GCC_except_table5350
- GCC_except_table5352
- GCC_except_table5389
- GCC_except_table5471
- GCC_except_table566
- GCC_except_table5763
- GCC_except_table5867
- GCC_except_table593
- GCC_except_table5944
- GCC_except_table5946
- GCC_except_table5948
- GCC_except_table5953
- GCC_except_table5962
- GCC_except_table5963
- GCC_except_table5967
- GCC_except_table6013
- GCC_except_table6034
- GCC_except_table6055
- GCC_except_table6060
- GCC_except_table6079
- GCC_except_table6081
- GCC_except_table6082
- GCC_except_table6087
- GCC_except_table6088
- GCC_except_table6090
- GCC_except_table6091
- GCC_except_table6105
- GCC_except_table6118
- GCC_except_table6121
- GCC_except_table6122
- GCC_except_table6123
- GCC_except_table6124
- GCC_except_table6125
- GCC_except_table6126
- GCC_except_table6127
- GCC_except_table6128
- GCC_except_table6129
- GCC_except_table6131
- GCC_except_table6132
- GCC_except_table6133
- GCC_except_table6134
- GCC_except_table6135
- GCC_except_table6136
- GCC_except_table6137
- GCC_except_table6138
- GCC_except_table6139
- GCC_except_table6140
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6143
- GCC_except_table6148
- GCC_except_table6149
- GCC_except_table6155
- GCC_except_table6156
- GCC_except_table6161
- GCC_except_table6162
- GCC_except_table6163
- GCC_except_table6165
- GCC_except_table6166
- GCC_except_table6167
- GCC_except_table6168
- GCC_except_table6169
- GCC_except_table617
- GCC_except_table6174
- GCC_except_table6175
- GCC_except_table6176
- GCC_except_table6177
- GCC_except_table6179
- GCC_except_table6180
- GCC_except_table6184
- GCC_except_table6185
- GCC_except_table6186
- GCC_except_table6187
- GCC_except_table6188
- GCC_except_table6189
- GCC_except_table6190
- GCC_except_table6191
- GCC_except_table6193
- GCC_except_table6195
- GCC_except_table6198
- GCC_except_table6199
- GCC_except_table6200
- GCC_except_table6201
- GCC_except_table6202
- GCC_except_table6204
- GCC_except_table6206
- GCC_except_table6207
- GCC_except_table6209
- GCC_except_table6210
- GCC_except_table625
- GCC_except_table6318
- GCC_except_table6322
- GCC_except_table6382
- GCC_except_table6414
- GCC_except_table6415
- GCC_except_table6453
- GCC_except_table6459
- GCC_except_table6467
- GCC_except_table6492
- GCC_except_table6572
- GCC_except_table6584
- GCC_except_table6587
- GCC_except_table6592
- GCC_except_table6608
- GCC_except_table6626
- GCC_except_table6629
- GCC_except_table6630
- GCC_except_table6634
- GCC_except_table6635
- GCC_except_table6739
- GCC_except_table6748
- GCC_except_table6768
- GCC_except_table6785
- GCC_except_table6859
- GCC_except_table6925
- GCC_except_table6930
- GCC_except_table6933
- GCC_except_table6956
- GCC_except_table7000
- GCC_except_table7143
- GCC_except_table7219
- GCC_except_table7234
- GCC_except_table7235
- GCC_except_table7236
- GCC_except_table7249
- GCC_except_table7250
- GCC_except_table7251
- GCC_except_table7252
- GCC_except_table7267
- GCC_except_table7268
- GCC_except_table7282
- GCC_except_table7283
- GCC_except_table7288
- GCC_except_table7328
- GCC_except_table7401
- GCC_except_table7402
- GCC_except_table7406
- GCC_except_table7408
- GCC_except_table7412
- GCC_except_table7414
- GCC_except_table7416
- GCC_except_table7417
- GCC_except_table7421
- GCC_except_table7425
- GCC_except_table7426
- GCC_except_table7427
- GCC_except_table7428
- GCC_except_table7429
- GCC_except_table7431
- GCC_except_table7432
- GCC_except_table7434
- GCC_except_table7435
- GCC_except_table7505
- GCC_except_table7540
- GCC_except_table7577
- GCC_except_table7578
- GCC_except_table7628
- GCC_except_table8338
- GCC_except_table8341
- GCC_except_table8409
- GCC_except_table8548
- GCC_except_table8551
- GCC_except_table8556
- GCC_except_table8559
- GCC_except_table8561
- GCC_except_table8566
- GCC_except_table8580
- GCC_except_table8583
- GCC_except_table8588
- GCC_except_table8589
- GCC_except_table8609
- GCC_except_table8616
- GCC_except_table8617
- GCC_except_table8618
- GCC_except_table8619
- GCC_except_table8632
- GCC_except_table8820
- GCC_except_table8867
- GCC_except_table9246
- GCC_except_table95
- GCC_except_table9518
- GCC_except_table9712
- GCC_except_table9764
- GCC_except_table9771
- GCC_except_table9809
- GCC_except_table9810
- GCC_except_table9811
- GCC_except_table9812
- GCC_except_table9817
- GCC_except_table9823
- GCC_except_table9824
- GCC_except_table9831
- GCC_except_table9834
- GCC_except_table9841
- GCC_except_table9843
- GCC_except_table9844
- GCC_except_table9846
- GCC_except_table9847
- GCC_except_table9848
- GCC_except_table9849
- GCC_except_table9854
- GCC_except_table9856
- GCC_except_table9857
- GCC_except_table9858
- GCC_except_table9859
- GCC_except_table9863
- GCC_except_table9864
- GCC_except_table9866
- GCC_except_table9868
- GCC_except_table9870
- GCC_except_table9872
- GCC_except_table9878
- GCC_except_table9881
- GCC_except_table9885
- GCC_except_table9886
- GCC_except_table9888
- GCC_except_table9889
- GCC_except_table9890
- GCC_except_table9891
- GCC_except_table9892
- GCC_except_table9894
- GCC_except_table9895
- GCC_except_table9896
- GCC_except_table9897
- GCC_except_table9898
- GCC_except_table9899
- GCC_except_table9900
- GCC_except_table9901
- GCC_except_table9902
- GCC_except_table9903
- GCC_except_table9904
- GCC_except_table9905
- GCC_except_table9906
- GCC_except_table9907
- GCC_except_table9908
- GCC_except_table9909
- GCC_except_table9910
- GCC_except_table9911
- GCC_except_table9968
- GCC_except_table9975
- _NUChannelControlTypeDescription
- _OBJC_CLASS_$_NSOrderedSet
- _OBJC_IVAR_$_NUChannelControlFormat._controlType
- _OBJC_IVAR_$_NUChannelControlFormat._dataModel
- _OBJC_IVAR_$_NUOptionalDescriptor._descriptorDefault
- __OBJC_$_CATEGORY_CIVector_$_NUDigest
- __OBJC_$_CATEGORY_INSTANCE_METHODS_CIVector_$_NUDigest
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSNumber_$_NUSchemaAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_NUDigest
- __OBJC_$_CATEGORY_NSArray_$_NUDigest
- __OBJC_$_CATEGORY_NSDictionary_$_NUDigest
- __OBJC_$_CATEGORY_NSNull_$_NUDigest
- __OBJC_$_CATEGORY_NSNumber_$_NUSchemaAdditions
- __OBJC_$_CATEGORY_NSObject_$_NUDigest
- __OBJC_$_CATEGORY_NSString_$_NUDigest
- __OBJC_$_CATEGORY_NSValue_$_NUDigest
- __OBJC_$_CLASS_METHODS_NSObject(NUDigest|NURenderPipelineFunction|NUControlDataRepresentable|NUUtilities)
- __OBJC_$_CLASS_METHODS_NSValue(NUDigest|NUGeometryExtensions|NUControlDataRepresentable)
- __OBJC_$_CLASS_METHODS_NUAssetCapability
- __OBJC_$_CLASS_PROP_LIST_NUAssetCapability
- __OBJC_$_INSTANCE_METHODS_NSArray(NUDigest|NURenderPipelineFunction|NUControlDataRepresentable)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(NUDigest|NURenderPipelineFunction)
- __OBJC_$_INSTANCE_METHODS_NSNull(NUDigest|NUControlDataRepresentable)
- __OBJC_$_INSTANCE_METHODS_NSObject(NUDigest|NURenderPipelineFunction|NUControlDataRepresentable|NUUtilities)
- __OBJC_$_INSTANCE_METHODS_NSValue(NUDigest|NUGeometryExtensions|NUControlDataRepresentable)
- __OBJC_$_INSTANCE_METHODS_NUCIImageSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_$_INSTANCE_METHODS_NUFileSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_$_INSTANCE_METHODS_NULivePhotoSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_$_INSTANCE_METHODS_NUMultipleSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_$_INSTANCE_METHODS_NURenderJob(Media|RendererSupport|DebugAdditions)
- __OBJC_$_INSTANCE_METHODS_NUSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_$_INSTANCE_METHODS_NUVideoDataSourceDefinition(NodeProvider|NUAssetLoader)
- __OBJC_CLASS_PROTOCOLS_$_NSObject(NUDigest|NURenderPipelineFunction|NUControlDataRepresentable|NUUtilities)
- __OBJC_PROTOCOL_REFERENCE_$_NUMediaGeometry
- ___36-[_NUPipeline addContainerPipeline:]_block_invoke
- ___46+[NUAssetCapability rawDecodeCapabilityFormat]_block_invoke
- ___54-[NUChannelControlFormat setting:canAcceptDescriptor:]_block_invoke
- ___55-[_NUPipeline processContainer:forEachComponent:error:]_block_invoke
- ___63-[_NUPipeline processContainerPort:forEachComponentPort:error:]_block_invoke
- ___90+[_NUStyleEngineMemoryResource usingSharedMemoryResourceForDevice:withDescriptor:perform:]_block_invoke
- ___block_descriptor_32_e36_24?0"NSString"8"NUChannelData"16l
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_ea8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_ea8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e42_v32?0"NSString"8"NUChannelFormat"16^B24lr56l8r64l8s32l8s40l8s48l8
- _rawDecodeCapabilityFormat.format
- _rawDecodeCapabilityFormat.onceToken
- _type_layout_string So12NUPixelPointa
- _type_layout_string So13NUChannelNamea
CStrings:
+ "%@(%@, default:%@)"
+ "(%@!)"
+ "(%@??%@)"
+ "(%@∋%@)"
+ "+[CIVector(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSArray(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSDictionary(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSNumber(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSObject(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSString(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NSValue(NUControlDataRepresentable) nu_valueFromControlData:error:]"
+ "+[NUChannelControlData opaqueDataWithValue:identifier:]"
+ "+[NUChannelData orientation:]"
+ "+[NUChannelExpression forceUnwrap:]"
+ "+[NUOptionalDescriptor unavailableOptionalWithDescriptor:defaultValue:]"
+ "-[NUArrayDescriptor initWithElement:min:max:valueType:]"
+ "-[NUArrayDescriptor initWithValueType:]"
+ "-[NUChannelContainsExpression evaluateWithLeftData:rightData:outputFormat:error:]"
+ "-[NUChannelControlData valueOfType:]"
+ "-[NUChannelControlFormat initWithDescriptor:valueType:]"
+ "-[NUChannelData _untypedValue]"
+ "-[NUChannelData valueOfType:]"
+ "-[NUChannelFormat canAcceptOptionalDataWithFormat:]"
+ "-[NUCompoundDescriptor initWithProperties:identifier:valueType:]"
+ "-[NUCompoundDescriptor initWithValueType:]"
+ "-[NUControlDescriptor descriptorWithValueType:]"
+ "-[NUControlDescriptor validate:error:]"
+ "-[NUEnumDescriptor initWithEnumValueType:values:identifier:valueType:]"
+ "-[NUEnumDescriptor initWithValueType:]"
+ "-[NUMediaGeometryDescriptor initWithProperties:identifier:]"
+ "-[NUMediaGeometryDescriptor initWithProperties:identifier:valueType:]"
+ "-[NUNumberDescriptor initWithNumberType:min:max:precision:valueType:]"
+ "-[NUNumberDescriptor initWithValueType:]"
+ "-[NUNumberDescriptor isValue:equalToValue:]"
+ "-[NUOpaqueDescriptor initWithIdentifier:valueType:]"
+ "-[NUOpaqueDescriptor initWithValueType:]"
+ "-[NUOptionalDescriptor initWithDescriptor:optionality:validatedDefaultValue:]"
+ "-[NUOptionalDescriptor initWithValueType:]"
+ "-[NUVectorDescriptor initWithElement:size:valueType:]"
+ "-[NUVectorDescriptor initWithValueType:]"
+ "-[_NUContainerPipeline _addInputChannel:]"
+ "-[_NUContainerPipeline _addOutputChannel:]"
+ "-[_NUContainerPipeline initWithContainerFormat:componentFormat:]"
+ "-[_NUPipeline addContainerPipelineWithContainerFormat:componentFormat:block:]"
+ "-[_NUPipeline insertContainerMapAt:containerFormat:componentFormat:block:error:]"
+ "-[_NUPipeline insertContainerMapAt:input:componentFormat:block:error:]"
+ "-[_NUPipeline processContainer:componentFormat:forEachComponent:error:]"
+ "-[_NUPipeline processContainerPort:componentFormat:forEachComponentPort:error:]"
+ "<%@: %p identifier: %@ properties: %@>"
+ "<%@: %p identifier: %@ type: %@ values: %@>"
+ "<%@:%p descriptor:%@>"
+ "@\"NUChannelPortRef\"32@?0@\"_NUContainerPipeline\"8@\"NUChannelPortRef\"16^@24"
+ "@\"_NUChannelPort\"16@?0@\"NUChannel\"8"
+ "A descriptor is required"
+ "AVCameraCalibrationData"
+ "AVMetadataItems"
+ "Abstract descriptor"
+ "Array elements cannot be compared with right data"
+ "B32@?0@\"NURenderJob\"8Q16^B24"
+ "CGColorSpace"
+ "CGImageMetadata"
+ "CGImageProperties"
+ "CGImagePropertyOrientation"
+ "CVPixelFormatType"
+ "CancellationCheck"
+ "Cannot add input channels to a container pipeline"
+ "Cannot add output channels to a container pipeline"
+ "Cannot read %{public}@ as %{public}@: %{public}@"
+ "Cannot read %{public}@ as an opaque value: %{public}@"
+ "Cannot read %{public}@ as an opaque value: its descriptor describes %{public}@"
+ "Converted %@ is not a %@"
+ "Converted value is not an instance of the specified value type"
+ "Data"
+ "Descriptor does not describe a number"
+ "Descriptor does not describe a value type"
+ "Descriptor does not describe a vector"
+ "Descriptor does not describe an enum"
+ "Dictionary"
+ "Every value must be distinct"
+ "Every value must match the enumeration type"
+ "Expected container media input"
+ "Expression format is not compatible"
+ "Failed to connect container pipeline contents"
+ "Failed to convert array element"
+ "Failed to convert compound property"
+ "Failed to convert property value"
+ "Failed to get value for key"
+ "Failed to read array element"
+ "Failed to read compound property"
+ "Generic"
+ "Incompatible enum value type"
+ "Incompatible left input format, expected an array"
+ "Input array is optional"
+ "Invalid processor result"
+ "Invalid value (unavailable)"
+ "Missing data for input channel: %@"
+ "Missing required value"
+ "NU_STANDARD_PREVIEW_SIZE"
+ "String"
+ "Transform"
+ "Unexpectedly found nil while unwrapping an optional value"
+ "Value is not a dictionary"
+ "Value is not a number"
+ "Value is not a string"
+ "Value is not a value type"
+ "Value is not a vector"
+ "Value is not an array"
+ "Value must be nil"
+ "Vector does not have the expected number of components"
+ "Vector must have 4 components (rect)"
+ "`"
+ "add<%@,%@>"
+ "array<%@>"
+ "array[%@..%@]<%@>"
+ "array[%@..]<%@>"
+ "array[%@]<%@>"
+ "array[..%@]<%@>"
+ "availableVersions"
+ "com.apple.coreimage:"
+ "componentFormat != nil"
+ "componentFormat.componentMediaType != NUChannelMediaTypeUnspecified || componentFormat.temporality != NUChannelMediaTemporalityUnspecified"
+ "componentFormat.mediaType != NUChannelMediaTypeContainer"
+ "compound(%@)"
+ "compound(%@)=%@"
+ "containerFormat != nil"
+ "containerFormat.mediaType == NUChannelMediaTypeContainer"
+ "contains<%@,%@>"
+ "defaultValue != nil"
+ "defaultValue == nil || optionality != NUControlOptionalityRequired"
+ "disabled"
+ "enabled"
+ "enum:%@(%@)"
+ "expressionFormat"
+ "forceDraftMode"
+ "forceUnwrap<%@>"
+ "format.descriptor.isOptional"
+ "geometry"
+ "integer"
+ "nilCoalesce<%@,%@>"
+ "number:%@"
+ "number:%@[%@..%@]"
+ "number:%@[%@..]"
+ "number:%@[..%@]"
+ "opaque(%@)"
+ "optionalExpression != nil"
+ "otherValue != nil"
+ "otherwise"
+ "precision == nil || numberType == NUNumberTypeReal"
+ "rawDecodeDraftMode"
+ "resultData"
+ "string"
+ "unavailable"
+ "valueType != Nil"
+ "vector%lu[%@]"
- "((NUControlDescriptor *)format.dataModel).isOptional"
- "+[NUChannel controlChannelWithSchema:]"
- "+[NUChannel controlChannelWithSchema:name:]"
- "+[NUChannel controlChannelWithSetting:name:]"
- "+[NUChannelControlData controlDataWithAdjustment:]"
- "+[NUChannelControlData controlDataWithComposition:]"
- "+[NUChannelControlData controlDataWithSetting:value:]"
- "+[NUChannelControlData controlDataWithSource:]"
- "-[NUArrayDescriptor initWithElement:min:max:]"
- "-[NUChannelControlData initWithData:schema:]"
- "-[NUChannelControlData initWithSetting:value:]"
- "-[NUChannelControlFormat initWithControlType:dataModel:valueType:]"
- "-[NUChannelData value]"
- "-[NUCompoundDescriptor initWithProperties:]"
- "-[NUControlDescriptor initWithAttributes:]"
- "-[NUEnumDescriptor initWithValues:]"
- "-[NUNumberDescriptor initWithNumberType:min:max:]"
- "-[NUOpaqueDescriptor initWithIdentifier:]"
- "-[NUOptionalDescriptor initWithDescriptor:validatedDefaultValue:]"
- "-[NUVectorDescriptor initWithElement:size:]"
- "-[_NUPipeline addContainerPipeline:]"
- "-[_NUPipeline addContainerPipeline:error:]"
- "-[_NUPipeline processContainer:forEachComponent:error:]"
- "-[_NUPipeline processContainerPort:forEachComponentPort:error:]"
- "<%@: %p properties: %@>"
- "<%@:%p type:%@ model:%@>"
- "??"
- "Data format is not compatible"
- "Either a descriptor or a setting is required"
- "Failed to add RAW output channels"
- "Failed to connect RAW output channel"
- "Failed to convert subkey"
- "Failed to read intensity channel data"
- "Incompatible output format"
- "Invalid control format"
- "Invalid value is not of type string"
- "Mixed control formats"
- "Multiple inputs matching output component"
- "Object is not of a supported rect type"
- "Unsupported subchannel format %@:%@"
- "[format.dataModel isKindOfClass:NUControlDescriptor.class]"
- "add(%@,%@>"
- "dataModel != nil"
- "descriptor:%@"
- "descriptor:%@[%@..%@]"
- "descriptor:%@[%@..]"
- "descriptor:%@[..%@]"
- "descriptor:array"
- "descriptor:compound"
- "descriptor:enum%@"
- "descriptor:opaque(%@)"
- "descriptor:optional"
- "descriptor:rect"
- "descriptor:time"
- "descriptor:unknown"
- "descriptor:unknownNumber"
- "descriptor:vector[%@, %lu]"
- "faces"
- "inputFactor"
- "numberType != NUNumberTypeUnknown"
- "scheduler '%{public}@' coalescing job #%llu (stage: WaitDependencies, older of two)"
- "schema"
- "schema:%@"
- "setting != nil"
- "setting:%@"
```

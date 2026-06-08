## MPSHost

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSHost.framework/MPSHost`

```diff

-129.5.1.0.0
-  __TEXT.__text: 0x2b84
-  __TEXT.__auth_stubs: 0x70
+130.0.10.2.0
+  __TEXT.__text: 0x3018
   __TEXT.__objc_methlist: 0x4d4
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x50
   __TEXT.__cstring: 0x43a
   __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x40b
-  __TEXT.__objc_methname: 0x989
-  __TEXT.__objc_methtype: 0x148
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x40
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__objc_const: 0x1420
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__auth_got: 0x40
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_DIRTY.__objc_data: 0x8c0
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5FAB668-57EB-36C1-9AC7-3AC72BAE7D9E
+  UUID: A41DCB47-84BC-35AF-B0E4-688E230EFAED
   Functions: 88
   Symbols:   79
-  CStrings:  243
+  CStrings:  83
 
Functions:
~ sub_2a939764c -> sub_243b995b4 : 452 -> 456
~ sub_2a9397820 -> sub_243b9978c : 1392 -> 2200
~ sub_2a9397e68 -> sub_243b9a0fc : 208 -> 216
~ sub_2a9397fbc -> sub_243b9a258 : 192 -> 200
~ sub_2a939807c -> sub_243b9a320 : 268 -> 260
~ sub_2a9398698 -> sub_243b9a934 : 2236 -> 2572
~ sub_2a9398f54 -> sub_243b9b340 : 444 -> 448
~ sub_2a93992b8 -> sub_243b9b6a8 : 1192 -> 1204
CStrings:
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8I16@20"
- "@28@0:8I16B20B24"
- "@28@0:8I16Q20"
- "@36@0:8I16Q20^Q28"
- "@92@0:8I16Q2028"
- "B"
- "B16@0:8"
- "B32@0:8Q16Q24"
- "B40@0:8Q16Q24@32"
- "B56@0:8Q16Q24@32@40@48"
- "B64@0:8Q16Q24@32@40@48@56"
- "I"
- "I16@0:8"
- "I48@0:8Q16Q24@32@40"
- "MPSNDArrayAffineQuantizationDescriptorHost"
- "MPSNDArrayBinaryKernelHost"
- "MPSNDArrayBinaryPrimaryGradientKernelHost"
- "MPSNDArrayBinarySecondaryGradientKernelHost"
- "MPSNDArrayConvolution2DDescriptorHost"
- "MPSNDArrayConvolution2DGradientWithInputHost"
- "MPSNDArrayConvolution2DGradientWithWeightsHost"
- "MPSNDArrayConvolution2DHost"
- "MPSNDArrayDepthwiseConvolutionKernelHost"
- "MPSNDArrayDescriptorHost"
- "MPSNDArrayGatherMatrixMultiplicationHost"
- "MPSNDArrayHammingDistanceKernelHost"
- "MPSNDArrayLUTQuantizationDescriptorHost"
- "MPSNDArrayMatrixMultiplicationGradientHost"
- "MPSNDArrayMatrixMultiplicationHost"
- "MPSNDArrayMultiaryBaseHost"
- "MPSNDArrayMultiaryGradientKernelHost"
- "MPSNDArrayMultiaryKernelHost"
- "MPSNDArrayQuantizationDescriptorHost"
- "MPSNDArrayQuantizedConvolutionHost"
- "MPSNDArrayQuantizedGatherMatrixMultiplicationHost"
- "MPSNDArrayQuantizedMatrixMultiplicationHost"
- "MPSNDArrayQuantizedScaledDotProductAttentionHost"
- "MPSNDArrayResampleHost"
- "MPSNDArrayScaledDotProductAttentionHost"
- "MPSNDArrayStencilKernelHost"
- "MPSNDArrayTileKernelHost"
- "MPSNDArrayUnaryKernelHost"
- "NSCopying"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "TB,N,V_hasMinValue"
- "TB,N,V_hasZeroPoint"
- "TB,N,V_preferPackedRows"
- "TI,N,V_dataFormat"
- "TI,N,V_dataType"
- "TI,N,V_weightsFormat"
- "TI,R,N,V_quantizationDataType"
- "TQ,N,V_dilationRateInX"
- "TQ,N,V_dilationRateInY"
- "TQ,N,V_groups"
- "TQ,N,V_inputFeatureChannels"
- "TQ,N,V_kernelHeight"
- "TQ,N,V_kernelWidth"
- "TQ,N,V_numberOfDimensions"
- "TQ,N,V_outputFeatureChannels"
- "TQ,N,V_strideInPixelsX"
- "TQ,N,V_strideInPixelsY"
- "TQ,R,N,V_quantizationScheme"
- "UTF8String"
- "_dataFormat"
- "_dataType"
- "_dilationRateInX"
- "_dilationRateInY"
- "_dimensionLengths"
- "_dimensionOrder"
- "_groups"
- "_hasMinValue"
- "_hasZeroPoint"
- "_inputFeatureChannels"
- "_kernelHeight"
- "_kernelWidth"
- "_numberOfDimensions"
- "_outputFeatureChannels"
- "_preferPackedRows"
- "_quantizationDataType"
- "_quantizationScheme"
- "_rowBytes"
- "_strideInPixelsX"
- "_strideInPixelsY"
- "_vectorAxis"
- "_weightsFormat"
- "allocWithZone:"
- "copyWithZone:"
- "count"
- "dataFormat"
- "dataType"
- "descriptorWithDataType:dimensionCount:dimensionSizes:"
- "descriptorWithDataType:dimensionSizes:"
- "descriptorWithDataType:shape:"
- "dilationRateInX"
- "dilationRateInY"
- "getConvolutionAlgorithmForDevice:environment:ndArrayConvolution2DDescriptor:srcNDArrayDescriptors:"
- "getMinValIndex"
- "getNDArrayCount"
- "getScaleIndex"
- "getZeroPointIndex"
- "groups"
- "hasFusedKernelSupportForDevice:environment:dataQuantizationDescriptor:weightsQuantizationDescriptor:srcNDArrayDescriptors:"
- "hasFusedKernelSupportForDevice:environment:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:srcNDArrayDescriptors:"
- "hasFusedKernelSupportForDevice:environment:srcNDArrayDescriptors:"
- "hasMinValue"
- "hasZeroPoint"
- "init"
- "initWithDataType:"
- "initWithDataType:dimensions:sizes:"
- "initWithDataType:hasZeroPoint:hasMinValue:"
- "initWithDataType:quantizationScheme:"
- "initWithDataType:vectorAxis:"
- "inputFeatureChannels"
- "kernelHeight"
- "kernelWidth"
- "lengthOfDimension:"
- "numberOfDimensions"
- "objectAtIndexedSubscript:"
- "outputFeatureChannels"
- "permuteWithDimensionOrder:"
- "preferPackedRows"
- "q16@0:8"
- "quantizationDataType"
- "quantizationScheme"
- "setDataFormat:"
- "setDataType:"
- "setDilationRateInX:"
- "setDilationRateInY:"
- "setGroups:"
- "setHasMinValue:"
- "setHasZeroPoint:"
- "setInputFeatureChannels:"
- "setKernelHeight:"
- "setKernelWidth:"
- "setLengthOfDimension:atIndex:"
- "setNumberOfDimensions:"
- "setOutputFeatureChannels:"
- "setPreferPackedRows:"
- "setQuantizationDataType:"
- "setStrideInPixelsX:"
- "setStrideInPixelsY:"
- "setWeightsFormat:"
- "strideInPixelsX"
- "strideInPixelsY"
- "subarrayWithRange:"
- "supportsPostfixForDevice:environment:"
- "supportsPrefixForDevice:environment:"
- "transposeDimension:withDimension:"
- "unsignedIntegerValue"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8Q16"
- "v24@0:8^Q16"
- "v32@0:8Q16Q24"
- "weightsFormat"

```

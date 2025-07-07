## MPSCore

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`

```diff

-127.1.3.0.0
-  __TEXT.__text: 0x5cd68
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x1ca0
-  __TEXT.__const: 0x2454
-  __TEXT.__cstring: 0x9399
+127.4.8.0.0
+  __TEXT.__text: 0x8b228
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x1df0
+  __TEXT.__const: 0x2474
+  __TEXT.__cstring: 0x9a98
   __TEXT.__oslogstring: 0x79
-  __TEXT.__gcc_except_tab: 0x4210
-  __TEXT.__unwind_info: 0x25a0
-  __TEXT.__eh_frame: 0x114
-  __TEXT.__objc_classname: 0x45f
-  __TEXT.__objc_methname: 0x4dc2
-  __TEXT.__objc_methtype: 0x2612
-  __TEXT.__objc_stubs: 0x26a0
+  __TEXT.__gcc_except_tab: 0x48e4
+  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__eh_frame: 0x38
+  __TEXT.__objc_classname: 0x4d6
+  __TEXT.__objc_methname: 0x522e
+  __TEXT.__objc_methtype: 0x26d4
+  __TEXT.__objc_stubs: 0x28a0
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x23a0
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__const: 0x2380
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6f78
-  __DATA_CONST.__objc_selrefs: 0xee0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x3460
-  __AUTH_CONST.__const: 0x2a8
-  __AUTH_CONST.__auth_got: 0x4f8
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x158
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x960
-  __DATA.__bss: 0x214
-  __DATA_DIRTY.__const: 0x5210
+  __DATA_CONST.__objc_const: 0x6958
+  __DATA_CONST.__objc_selrefs: 0xfb8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x180
+  __AUTH_CONST.__const: 0xb08
+  __AUTH_CONST.__objc_const: 0x168
+  __AUTH_CONST.__cfstring: 0x3620
+  __AUTH_CONST.__auth_got: 0x508
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x304
+  __DATA.__data: 0x958
+  __DATA.__bss: 0x1c
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__const: 0x5200
   __DATA_DIRTY.__objc_const: 0x1488
+  __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA103A5C-9876-3699-BE12-23BD4C627A45
-  Functions: 1876
-  Symbols:   697
-  CStrings:  2360
+  UUID: 8989A7B2-0728-3026-9F66-2E3A88268C94
+  Functions: 1674
+  Symbols:   760
+  CStrings:  2452
 
Symbols:
+ OBJC_IVAR_$_MPSNDArray._rowElements
+ _MPSDisableMatrixUnit
+ _MPSForceMatrixUnit
+ _NSSelectorFromString
+ _OBJC_CLASS_$_MPSKernelUserDAGInfo
+ _OBJC_CLASS_$_MPSKernelUserDAGObject
+ _OBJC_CLASS_$_MPSUserDAGStitchableOperation
+ _OBJC_CLASS_$_MPSUserDAGVisibleOperation
+ _OBJC_CLASS_$_MTLFunctionStitchingAttributeAlwaysInline
+ _OBJC_CLASS_$_MTLFunctionStitchingFunctionNode
+ _OBJC_CLASS_$_MTLFunctionStitchingGraph
+ _OBJC_CLASS_$_MTLFunctionStitchingInputNode
+ _OBJC_CLASS_$_MTLStitchedLibraryDescriptor
+ _OBJC_METACLASS_$_MPSKernelUserDAGInfo
+ _OBJC_METACLASS_$_MPSKernelUserDAGObject
+ _OBJC_METACLASS_$_MPSUserDAGStitchableOperation
+ _OBJC_METACLASS_$_MPSUserDAGVisibleOperation
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
+ __ZN12MPSAutoCache14GetTempTextureEPK12MPSPixelInfoPK7MTLSizeP20MTLTextureDescriptorbP19TextureSizeAndAlignb
+ __ZN12MPSKernelDAG12denaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG12dequantizeOpEP10BaseTensorRKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14novenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14octonaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14undenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG15duodenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG15septenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG5padOpEP10BaseTensorDv4_ib16MPSImageEdgeModeRKNSt3__16vectorIlNS4_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG6tileOpEP10BaseTensorDv4_iRKNSt3__16vectorIlNS3_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN16MPSKernelUserDAG10addOpToDAGEP18MPSKernelUserDAGOp
+ __ZN16MPSKernelUserDAG10constantOpEf11MPSDataType
+ __ZN16MPSKernelUserDAG10constantOpEx11MPSDataType
+ __ZN16MPSKernelUserDAG11assignStateEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG11greaterThanEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG11subtractionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG12toValueCoordEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG14fromValueCoordEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG14multiplicationEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG17reverseSquareRootEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG22readStateFromReferenceEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG25assignStateFromValueCoordEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG25getMTLStitchingInputNodesEm
+ __ZN16MPSKernelUserDAG3expEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG6selectEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG8additionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG8divisionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG9readStateEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAGD0Ev
+ __ZN16MPSKernelUserDAGD1Ev
+ __ZN16MPSKernelUserDAGD2Ev
+ __ZN18MPSKernelUserDAGOp17functionConstantsEv
+ __ZN18MPSKernelUserDAGOp20getMTLStitchingNodesEv
+ __ZN18MPSKernelUserDAGOpC1ERKNSt3__16vectorIP20MPSKernelUserDAGNodeNS0_9allocatorIS3_EEEENS0_12basic_stringIcNS0_11char_traitsIcEENS4_IcEEEESD_
+ __ZN18MPSKernelUserDAGOpC2ERKNSt3__16vectorIP20MPSKernelUserDAGNodeNS0_9allocatorIS3_EEEENS0_12basic_stringIcNS0_11char_traitsIcEENS4_IcEEEESD_
+ __ZN18MPSKernelUserDAGOpD0Ev
+ __ZN18MPSKernelUserDAGOpD1Ev
+ __ZN18MPSKernelUserDAGOpD2Ev
+ __ZN20MPSKernelUserDAGNodeC1EPU35objcproto24MTLFunctionStitchingNode11objc_object
+ __ZN20MPSKernelUserDAGNodeC2EPU35objcproto24MTLFunctionStitchingNode11objc_object
+ __ZN20MPSKernelUserDAGNodeD0Ev
+ __ZN20MPSKernelUserDAGNodeD1Ev
+ __ZN20MPSKernelUserDAGNodeD2Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZTV16MPSKernelUserDAG
+ __ZTV18MPSKernelUserDAGOp
+ __ZTV20MPSKernelUserDAGNode
+ _strcmp
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_m
- __ZN12MPSAutoCache14GetTempTextureEPK12MPSPixelInfoPK7MTLSizeP20MTLTextureDescriptorbP19TextureSizeAndAlign
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelUserDAG.mm"
+ "1"
+ "@\"MTLFunctionConstantValues\""
+ "@24@0:8^v16"
+ "@76@0:8@16I24Q28r^q36r^q44r^q52Q60r^q68"
+ "B24@0:8q16"
+ "Cannot calculate strideBytes for sub byte data type"
+ "Cannot calculate strideBytes for sub byte data type. Please use makeStrideElementsImpl"
+ "Dont use dataTypeSize for sub-byte datatype. Use dataTypeSizeInBits instead"
+ "Failed to stitch function with error: %s"
+ "MPSDataTypeInt2"
+ "MPSDataTypeInt4"
+ "MPSDataTypeUInt2"
+ "MPSDataTypeUInt4"
+ "MPSKernelUserDAGInfo"
+ "MPSKernelUserDAGObject"
+ "MPSNDARRAY_USE_REFERENCE_DEQUANTIZE_DAG"
+ "MPSParavirtDevice"
+ "MPSUserDAGStitchableOperation"
+ "MPSUserDAGVisibleOperation"
+ "Paravirtual device"
+ "T@\"MTLFunctionConstantValues\",R,N,V_functionConstants"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_functionName"
+ "T@\"NSString\",R,N,V_specializedName"
+ "T@\"NSString\",R,N,V_visibleName"
+ "[%@ %@] Error: invalid `permutation` provided"
+ "_cachedHash"
+ "_functionConstants"
+ "_functionName"
+ "_gpuFamily"
+ "_kernelUserDAGSharedPtr"
+ "_rowElements"
+ "_specializedName"
+ "_stitchedMTLFunctions"
+ "_stitchingGraphs"
+ "_userStitchedFunctions"
+ "_userStitchedHash%llu"
+ "_userVisibleFunctions"
+ "_visibleName"
+ "addObjectsFromArray:"
+ "arrayByAddingObjectsFromArray:"
+ "arrayView doesn't support sub byte data type"
+ "arrayView doesn't support sub byte data type without aliasing"
+ "checkNDArray does not support sub type data type"
+ "constantScalar"
+ "copyDataWithCommandBuffer doesn't support sub byte data type"
+ "dataTypeSizeInBits"
+ "dequantize"
+ "dequantize op only supports fp32 inputs currently"
+ "dequantize op only supports i8 or ui8 outputs currently"
+ "dequantizeRef"
+ "emptyValueCoordSize"
+ "encodeCopyWithCommandBuffer doesn't support sub byte data type"
+ "encodeReshapedMatrixWithCommandBuffer doesn't support sub byte data type"
+ "extractValueCoordSizeValue"
+ "functionConstants"
+ "functionName"
+ "getMTLStitchingGraph"
+ "getReductionState"
+ "getReductionStateReference"
+ "getStitchedFunction:"
+ "getVisibleFunction:"
+ "getVisibleFunctions"
+ "hostGPUFamily"
+ "i20@0:8I16"
+ "importDataWithCommandBuffer doesn't support sub byte data type"
+ "initWithArgumentIndex:"
+ "initWithBuffer:dataType:numDimensions:dimSizes:strides:offsets:sizePermutation:permutation:"
+ "initWithFunctionName:"
+ "initWithFunctionName:nodes:outputNode:attributes:"
+ "initWithKernelUserDAG:"
+ "initWithMTLStitchingGraphs:visibleFunctions:stitchedFunctions:"
+ "initWithName:arguments:controlDependencies:"
+ "initWithVisibleName:specializedName:functionConstants:"
+ "makeStrideBytesInArray doesn't support sub byte data type"
+ "methodForSelector:"
+ "newLibraryWithStitchedDescriptor:error:"
+ "nodes"
+ "outputNode"
+ "printNDArrayToFile does not support sub type data type"
+ "productName"
+ "readBytes doesn't support sub byte data type with user provided strides"
+ "setCompressionMode:"
+ "setFunctionGraphs:"
+ "setFunctions:"
+ "setOwnerWithIdentity:"
+ "setReductionState"
+ "setReductionStateValueCoord"
+ "specializedName"
+ "stitchedFunction is not a visible function!"
+ "tileOp"
+ "visibleName"
+ "writeBytes with user strides cannot be called for sub-byte data type"
+ "{shared_ptr<MPSKernelUserDAG>=\"__ptr_\"^{MPSKernelUserDAG}\"__cntrl_\"^{__shared_weak_count}}"
- "MPSCNNConvolution"
- "MPSCNNConvolutionGradient"
- "MPSCNNNeuron"
- "MPSCNNPooling"
- "MPSCNNPoolingGradient"
- "MPSCNNSoftMax"
- "MPSMatrixVectorMultiplication"
- "_%@"
- "absolute"
- "cast"
- "isFinite"
- "lessThan"
- "nand"
- "negative"
- "or"
- "unnamed"
- "xnor"

```

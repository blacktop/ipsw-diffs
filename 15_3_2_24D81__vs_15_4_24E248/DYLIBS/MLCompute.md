## MLCompute

> `/System/Library/Frameworks/MLCompute.framework/Versions/A/MLCompute`

```diff

-80.0.0.0.0
-  __TEXT.__text: 0x145de0
+82.0.0.0.0
+  __TEXT.__text: 0x14592c
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x9c50
-  __TEXT.__const: 0x560
+  __TEXT.__objc_methlist: 0xae74
+  __TEXT.__const: 0x5b0
   __TEXT.__oslogstring: 0x8ee6
   __TEXT.__cstring: 0x5160
   __TEXT.__gcc_except_tab: 0xc0
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x1d80
+  __TEXT.__unwind_info: 0x1dc0
   __TEXT.__objc_classname: 0xd00
   __TEXT.__objc_methname: 0x1d611
   __TEXT.__objc_methtype: 0x4a08

   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48d0
+  __DATA_CONST.__objc_selrefs: 0x4d18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x5e0
   __AUTH_CONST.__const: 0x790
   __AUTH_CONST.__cfstring: 0x4300
-  __AUTH_CONST.__objc_const: 0x19d50
+  __AUTH_CONST.__objc_const: 0x17a48
   __AUTH_CONST.__objc_intobj: 0x840
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A90B172-4033-31B9-B253-26DF45C69274
-  Functions: 4215
-  Symbols:   9398
+  UUID: E8B0BD9F-2FAA-3FA7-B988-EECCDA4C8521
+  Functions: 4224
+  Symbols:   9433
   CStrings:  6438
 
Symbols:
+ +[MLCDeviceANE hasANE].cold.1
+ +[MLCLog execution].cold.1
+ +[MLCLog framework].cold.1
+ +[MLCLog test].cold.1
+ +[MLCPlatformInfo aneGraphPartitioningConfigEnvVariable].cold.1
+ +[MLCPlatformInfo aneKeepPlistEnvVariable].cold.1
+ +[MLCPlatformInfo aneSaveGraphPartitioningConfig].cold.1
+ +[MLCPlatformInfo aneSubType].cold.1
+ +[MLCPlatformInfo buildVersion].cold.1
+ +[MLCPlatformInfo gpuUseMPSGraphConvolution].cold.1
+ +[MLCPlatformInfo isInternalBuild].cold.1
+ +[MLCPlatformInfo isRNGSeeded].cold.1
+ +[MLCPlatformInfo mpsGraphConvolutionEnvVariable].cold.1
+ +[MLCPlatformInfo seedEnvVariable].cold.1
+ +[MLCTensor initialize].cold.1
+ +[_MLCANEIOSurface initialize].cold.1
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.2
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.3
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.4
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.5
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.6
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.7
+ -[MLCDeviceANE procedureInformationWithModelAttributes:procedureName:procedureID:procedureInputSymbols:procedureInputSymbolIndices:procedureOutputSymbols:procedureOutputSymbolIndices:].cold.8
+ ANE_ValidateArgMinMaxUnit.cold.5
+ ANE_ValidateBroadcastUnit.cold.6
+ ANE_ValidateConcatUnit.cold.5
+ ANE_ValidateConvolutionUnit.cold.5
+ ANE_ValidateElementWiseUnit.cold.5
+ ANE_ValidateGOCUnit.cold.5
+ ANE_ValidateInputViewUnit.cold.5
+ ANE_ValidateInstanceNormUnit.cold.5
+ ANE_ValidateLayerNormUnit.cold.5
+ ANE_ValidateMatrixMultUnit.cold.5
+ ANE_ValidateNeuronUnit.cold.5
+ ANE_ValidatePoolingUnit.cold.5
+ ANE_ValidateReductionUnit.cold.5
+ ANE_ValidateReshapeUnit.cold.5
+ ANE_ValidateSoftmaxUnit.cold.5
+ ANE_ValidateTransposeUnit.cold.5
+ __22+[MLCDeviceANE hasANE]_block_invoke.cold.1
+ __22+[MLCDeviceANE hasANE]_block_invoke.cold.2
+ __29+[MLCPlatformInfo aneSubType]_block_invoke.cold.1
+ __30+[_MLCANEIOSurface initialize]_block_invoke.cold.1
+ __ANE_ValidateArgMinMaxUnit_block_invoke.cold.1
+ __ANE_ValidateBroadcastUnit_block_invoke.cold.1
+ __ANE_ValidateConcatUnit_block_invoke.cold.1
+ __ANE_ValidateConvolutionUnit_block_invoke.cold.1
+ __ANE_ValidateElementWiseUnit_block_invoke.cold.1
+ __ANE_ValidateGOCUnit_block_invoke.cold.1
+ __ANE_ValidateInputViewUnit_block_invoke.cold.1
+ __ANE_ValidateInstanceNormUnit_block_invoke.cold.1
+ __ANE_ValidateLayerNormUnit_block_invoke.cold.1
+ __ANE_ValidateMatrixMultUnit_block_invoke.cold.1
+ __ANE_ValidateNeuronUnit_block_invoke.cold.1
+ __ANE_ValidatePoolingUnit_block_invoke.cold.1
+ __ANE_ValidateReductionUnit_block_invoke.cold.1
+ __ANE_ValidateReshapeUnit_block_invoke.cold.1
+ __ANE_ValidateSoftmaxUnit_block_invoke.cold.1
+ __ANE_ValidateTransposeUnit_block_invoke.cold.1
+ __isAppleNeuralEngineAPIAvailable_block_invoke.cold.2
+ __softLinkClass_ANEDeviceInfo_block_invoke.cold.1
+ __softLinkClass_ANEIOSurfaceObject_block_invoke.cold.1
+ __softLinkClass_ANEInMemoryModelDescriptor_block_invoke.cold.1
+ __softLinkClass_ANEInMemoryModel_block_invoke.cold.1
+ __softLinkClass_ANEQoSMapper_block_invoke.cold.1
+ __softLinkClass_ANERequest_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelDescriptionKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelInputSymbolIndexArrayKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelInputSymbolsArrayKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelOutputSymbolIndexArrayKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelOutputSymbolsArrayKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelProcedureNameToIDMapKey_block_invoke.cold.1
+ __softLinkObjcConstantkANEFModelProceduresArrayKey_block_invoke.cold.1
+ _getMPSLossType
+ softLinkClass_ANEDeviceInfo.cold.1
+ softLinkClass_ANEIOSurfaceObject.cold.1
+ softLinkClass_ANEInMemoryModel.cold.1
+ softLinkClass_ANEInMemoryModelDescriptor.cold.1
+ softLinkClass_ANEQoSMapper.cold.1
+ softLinkClass_ANERequest.cold.1
- ANE_CompilePoolingLayer.cold.7
- CPU_CreateNormalizationLayer.cold.2
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13

```

## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

 9.201.1.0.0
-  __TEXT.__text: 0x1467868
+  __TEXT.__text: 0x1467898
   __TEXT.__auth_stubs: 0x2180
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x878f4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: 45F171EA-8AA2-332C-984B-6A811020B00E
-  Functions: 81422
-  Symbols:   239394
+  UUID: 6ED3151E-3F59-3418-A5F7-3C45DAF94882
+  Functions: 81430
+  Symbols:   239404
   CStrings:  19704
 
Symbols:
+ _OUTLINED_FUNCTION_201
+ _OUTLINED_FUNCTION_209
+ _OUTLINED_FUNCTION_218
- _OUTLINED_FUNCTION_203
- _OUTLINED_FUNCTION_210
Functions:
~ __ZN37ZinReinterpretInnermostDimensionLayerC2ENSt3__110shared_ptrI11ZinIrTensorEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE.cold.1 : 76 -> 72
~ __ZNSt3__110__function6__funcIZN14MILOpConverterL20ConvertFP8DequantizeERKN3MIL11IROperationERKNS3_10IRDataTypeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEER17ZinMILUnitBuilderR15MILFunctionInfoE3$_1NSD_ISM_EEFNS_6vectorIfNSD_IfEEEERKNSO_IPKNS3_7IRValueENSD_IST_EEEEEEclESX_.cold.1 : 44 -> 40
+ _OUTLINED_FUNCTION_0
~ __ZN6MirOptL10PerformOptEP17ZinIrOpLayerGraphP12ZinIrOpLayermmR16ZinTransformInfo.cold.9 : 80 -> 72
+ _OUTLINED_FUNCTION_1
~ __ZN10ZinBuilder16CreateActivationEP12ZinIrContextR20ZinObjectNameFactoryRKNSt3__16vectorI15ZinIrTensorInfoNS4_9allocatorIS6_EEEERK21ZinIrActivationParams15ZinTensorFormatNS4_10unique_ptrIN11ZinIrTensor7MirInfoENS4_14default_deleteISI_EEEE.cold.1 : 104 -> 96
~ __ZN23ZinStochasticRoundLayerC2EONSt3__110unique_ptrI24ZinIrStochasticRoundInfoNS0_14default_deleteIS2_EEEENS0_10shared_ptrI11ZinIrTensorEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE.cold.1 : 72 -> 60
+ _OUTLINED_FUNCTION_7
~ __Z41ANECHandleProgramKernelsAndMetadataToFileR31ZinComputeMutableProgramWrapperRK23ZinIrCompilerParametersPK11ZinIrTargetR17ZinIrConstManagerRKNSt3__16vectorItNS9_9allocatorItEEEE.cold.3 : 72 -> 80
~ _ANECCompile.cold.9 : 76 -> 72
+ __ZN16ZinNEBypassLayerC2ENSt3__110shared_ptrI11ZinIrTensorEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP17ZinBroadcastLayerP17ZinTransposeLayer.cold.1
~ __ZNK15MILFunctionInfo13GetTensorNameERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb.cold.1 : 44 -> 36
~ __ZN9ZinSerial33DeserializeMirTransposeUnitFieldsERNS_12DeserializerERNSt3__110unique_ptrI19ZinMirTransposeUnitNS2_14default_deleteIS4_EEEE.cold.1 : 68 -> 64
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_14
~ __ZN18ZinIrLocalRegAlloc25SetResidentSymbolToLayersEP11ZinIrTensor.cold.2 : 76 -> 72
~ __ZN18ZinIrLocalRegAlloc25SetResidentSymbolToLayersEP11ZinIrTensor.cold.3 : 76 -> 72
~ __ZN18ZinIrLocalRegAlloc28SetL2CachedSymbolToConsumersEP11ZinIrTensor.cold.1 : 84 -> 72
~ __ZN18ZinIrLocalRegAlloc28SetL2CachedSymbolToConsumersEP11ZinIrTensor.cold.2 : 84 -> 72
~ __ZNK18ZinIrLocalRegAlloc16VerifyDMABuffersEv.cold.4 : 80 -> 72
~ __ZN18ZinIrLocalRegAlloc27AllocateUncompressedLiveIOsERKNSt3__110unique_ptrI13ZinIrBindingsNS0_14default_deleteIS2_EEEERKNS0_3mapIhP12ZinIrSectionNS0_4lessIhEENS0_9allocatorINS0_4pairIKhSA_EEEEEE.cold.1 : 84 -> 80
+ _OUTLINED_FUNCTION_8
~ __ZN18ZinIrLiveIOManager32PrepareBindingsForLiveInsWith4CCE6IOTypeP12ZinIrContextRNSt3__110unique_ptrI13ZinIrBindingsNS3_14default_deleteIS5_EEEEP18ZinIrNetworkStatus.cold.2 : 76 -> 72
~ __ZN18ZinIrLiveIOManager32PrepareBindingsForLiveInsWith4CCE6IOTypeP12ZinIrContextRNSt3__110unique_ptrI13ZinIrBindingsNS3_14default_deleteIS5_EEEEP18ZinIrNetworkStatus.cold.4 : 76 -> 72
~ __ZN18ZinIrLiveIOManager14PrepareLiveOutEP18ZinIrNetworkStatus.cold.2 : 76 -> 72
+ _OUTLINED_FUNCTION_96
- _OUTLINED_FUNCTION_31
~ _OUTLINED_FUNCTION_200 : 36 -> 20
+ _OUTLINED_FUNCTION_201
~ __ZN4mlir12matchThroughINS_4anec20TensorBufferToTensorEJNS_26UnrealizedConversionCastOpEEEEbPNS_9OperationEPT_ : 200 -> 196
~ __ZN4mlir4impl19foldCastInterfaceOpEPNS_9OperationEN4llvm8ArrayRefINS_9AttributeEEERNS3_15SmallVectorImplINS_12OpFoldResultEEE : 476 -> 464
~ __ZN4mlir2OpINS_3mps17PoolMaxGradientOpEJNS_7OpTrait11ZeroRegionsENS3_9OneResultENS3_14OneTypedResultINS_4TypeEE4ImplENS3_14ZeroSuccessorsENS3_16AtLeastNOperandsILj1EE4ImplENS3_24AttrSizedOperandSegmentsENS3_12OpInvariantsENS_19BytecodeOpInterface5TraitENS_23MemoryEffectOpInterface5TraitENS_20InferTypeOpInterface5TraitENS_30CompatibleReturnTypesInterface5TraitEEE16verifyInvariantsEPNS_9OperationE.cold.1 : 108 -> 96

```

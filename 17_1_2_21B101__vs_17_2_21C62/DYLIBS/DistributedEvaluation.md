## DistributedEvaluation

> `/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation`

```diff

-101.1.0.0.0
-  __TEXT.__text: 0x35698
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x22bc
+101.4.0.0.0
+  __TEXT.__text: 0x369ac
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x2324
   __TEXT.__const: 0x280
-  __TEXT.__cstring: 0x356e
-  __TEXT.__oslogstring: 0x31b8
+  __TEXT.__cstring: 0x3626
+  __TEXT.__oslogstring: 0x34f8
   __TEXT.__gcc_except_tab: 0x764
   __TEXT.__dlopen_cstrs: 0x6e
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__objc_classname: 0x5cc
-  __TEXT.__objc_methname: 0x6521
-  __TEXT.__objc_methtype: 0x1366
-  __TEXT.__objc_stubs: 0x4c20
+  __TEXT.__unwind_info: 0xaf8
+  __TEXT.__objc_classname: 0x5df
+  __TEXT.__objc_methname: 0x6621
+  __TEXT.__objc_methtype: 0x1377
+  __TEXT.__objc_stubs: 0x4d20
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xd30
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4ca0
-  __DATA_CONST.__objc_selrefs: 0x1858
-  __AUTH_CONST.__cfstring: 0x3ee0
-  __AUTH_CONST.__objc_const: 0x1608
-  __AUTH_CONST.__const: 0x310
+  __DATA_CONST.__objc_const: 0x4d28
+  __DATA_CONST.__objc_selrefs: 0x18a0
+  __AUTH_CONST.__cfstring: 0x4020
+  __AUTH_CONST.__objc_const: 0x1650
+  __AUTH_CONST.__const: 0x330
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0xa50
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x8
   __DATA.__got_weak: 0x8
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x348
+  __DATA.__objc_classrefs: 0x350
   __DATA.__objc_superrefs: 0x130
   __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x5b0
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C1E765E-EE41-33A6-B291-587053B0EB45
-  Functions: 1140
-  Symbols:   4095
-  CStrings:  2694
+  UUID: 01D25D0D-2F7F-377E-94BC-897ABC3812E0
+  Functions: 1167
+  Symbols:   4174
+  CStrings:  2738
 
Symbols:
+ +[DESBitacoraEventManager allowEventForBundleID:]
+ +[DESFederatedBuffer computeApproximateStaleness:stalenessScale:stalenessBias:]
+ +[DESFederatedBuffer computeApproximateStaleness:stalenessScale:stalenessBias:].cold.1
+ +[DESFederatedBuffer computeApproximateStaleness:stalenessScale:stalenessBias:].cold.2
+ +[DESFederatedBuffer computeApproximateStaleness:stalenessScale:stalenessBias:].cold.3
+ +[DESFederatedBuffer computeApproximateStaleness:stalenessScale:stalenessBias:].cold.4
+ +[DESFederatedBuffer computeDownScalingFactor:approximateStaleness:]
+ +[DESFederatedBuffer computeDownScalingFactor:approximateStaleness:].cold.1
+ +[DESFederatedBuffer computeDownScalingFactor:approximateStaleness:].cold.2
+ -[DESDediscoUploader donateResult:dediscoMetadata:recorder:].cold.6
+ -[DESRecipe approximateStaleness]
+ -[DESRecipe approximateStaleness].cold.1
+ -[DESRecipe federatedBufferDownScalingFactor]
+ -[DESRecipe federatedBufferDownScalingFactor].cold.1
+ -[DESRecipe federatedBufferDownScalingFactor].cold.2
+ -[DESRecipe federatedBufferDownScalingFactor].cold.3
+ -[DESRecipe isFederatedBufferStaled:]
+ -[DESRecipe isFederatedBufferStaled:].cold.1
+ -[DESRecipe isFederatedBufferStaled:].cold.2
+ -[DESRecipe isFederatedBufferStaled]
+ -[DESRecipe useFederatedBuffer]
+ _OBJC_CLASS_$_DESFederatedBuffer
+ _OBJC_METACLASS_$_DESFederatedBuffer
+ __OBJC_$_CLASS_METHODS_DESFederatedBuffer
+ __OBJC_CLASS_RO_$_DESFederatedBuffer
+ __OBJC_METACLASS_RO_$_DESFederatedBuffer
+ ___49+[DESBitacoraEventManager allowEventForBundleID:]_block_invoke
+ ___81-[DESDodMLServer _runJSONOrMultipartPOSTRequest:path:uploadTransport:completion:]_block_invoke.234
+ ___87-[DESDodMLServer _downloadAttachments:signatures:certificate:relativePaths:completion:]_block_invoke.177
+ ___87-[DESDodMLServer _downloadAttachments:signatures:certificate:relativePaths:completion:]_block_invoke.177.cold.1
+ _kCurrentModelVersionKey
+ _kDownScalingOrderKey
+ _kFederatedBufferContextKey
+ _kIterationStartTimeKey
+ _kMaximumStalenessKey
+ _kRamsayRecipeIDKey
+ _kStalenessBiasKey
+ _kStalenessScaleKey
+ _objc_msgSend$approximateStaleness
+ _objc_msgSend$computeApproximateStaleness:stalenessScale:stalenessBias:
+ _objc_msgSend$computeDownScalingFactor:approximateStaleness:
+ _objc_msgSend$federatedBufferDownScalingFactor
+ _objc_msgSend$isFederatedBufferStaled:
+ _objc_msgSend$now
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$useFederatedBuffer
+ _pow
- ___81-[DESDodMLServer _runJSONOrMultipartPOSTRequest:path:uploadTransport:completion:]_block_invoke.228
- ___87-[DESDodMLServer _downloadAttachments:signatures:certificate:relativePaths:completion:]_block_invoke.171
- ___87-[DESDodMLServer _downloadAttachments:signatures:certificate:relativePaths:completion:]_block_invoke.171.cold.1
CStrings:
+ "@40@0:8d16@24@32"
+ "Approximate staleness for Federated Buffer: %@"
+ "Approximate staleness scale should be greater than zero"
+ "DESFederatedBuffer"
+ "Down-scaling factor for Federated Buffer: %@"
+ "Failed to compute down-scaling factor or staleness is too large"
+ "Failed to compute federated buffer down-scaling factor due to approximate staleness is larger or equal than the limit"
+ "Failed to compute federated buffer down-scaling factor due to invalid approximate staleness"
+ "Federated buffer down-scaling order is malformed: %@"
+ "Invalid approximate staleness: %@"
+ "Invalid down-scaling factor %@"
+ "Invalid time delta for approximate staleness: %@"
+ "Maximum staleness for rejecting staled donation is malformed: %@"
+ "Recipe content for approximating staleness iterationStartTime=%@ or scale=%@ or bias=%@ is malformed"
+ "Rejecting recipe since the staleness %@ is larger or equal than the limit %@"
+ "approximateStaleness"
+ "approximate_staleness"
+ "computeApproximateStaleness:stalenessScale:stalenessBias:"
+ "computeDownScalingFactor:approximateStaleness:"
+ "currentModelVersion"
+ "current_model_version"
+ "downScalingOrder"
+ "federatedBufferContext"
+ "federatedBufferDownScalingFactor"
+ "isFederatedBufferStaled"
+ "isFederatedBufferStaled:"
+ "iterationStartTime"
+ "maximumStaleness"
+ "now"
+ "ramsayRecipeID"
+ "stalenessBias"
+ "stalenessScale"
+ "timeIntervalSince1970"
+ "useFederatedBuffer"

```

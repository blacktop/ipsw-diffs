## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-167.100.107.502.1
-  __TEXT.__text: 0x11b194
-  __TEXT.__auth_stubs: 0x2e10
+167.100.115.0.0
+  __TEXT.__text: 0x12ec50
+  __TEXT.__auth_stubs: 0x2e00
   __TEXT.__objc_methlist: 0x158
-  __TEXT.__const: 0x2aa8
-  __TEXT.__cstring: 0x2564
-  __TEXT.__swift5_typeref: 0x1b2c
-  __TEXT.__swift5_capture: 0xba0
+  __TEXT.__const: 0x2ab8
+  __TEXT.__cstring: 0x25f4
+  __TEXT.__swift5_typeref: 0x1b84
+  __TEXT.__swift5_capture: 0xbc8
   __TEXT.__objc_methname: 0x499
-  __TEXT.__oslogstring: 0x6ef5
+  __TEXT.__oslogstring: 0x7145
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1f04
+  __TEXT.__constg_swiftt: 0x1f24
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x1733
-  __TEXT.__swift5_fieldmd: 0x14d4
+  __TEXT.__swift5_fieldmd: 0x14ec
   __TEXT.__swift5_types: 0x12c
   __TEXT.__objc_classname: 0x6a
   __TEXT.__objc_methtype: 0x191
-  __TEXT.__swift_as_entry: 0x658
-  __TEXT.__swift_as_ret: 0x820
+  __TEXT.__swift_as_entry: 0x664
+  __TEXT.__swift_as_ret: 0x830
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x230
   __TEXT.__swift5_protos: 0x5c
-  __TEXT.__unwind_info: 0x5248
-  __TEXT.__eh_frame: 0x10ad8
-  __DATA_CONST.__auth_got: 0x1708
-  __DATA_CONST.__got: 0xbe8
-  __DATA_CONST.__auth_ptr: 0xa78
-  __DATA_CONST.__const: 0x2fb0
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0x5268
+  __TEXT.__eh_frame: 0x11038
+  __DATA_CONST.__auth_got: 0x1700
+  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__auth_ptr: 0x948
+  __DATA_CONST.__const: 0x3040
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x2b38
+  __DATA.__objc_const: 0x2bf0
   __DATA.__objc_selrefs: 0x220
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x5408
+  __DATA.__data: 0x54e8
   __DATA.__common: 0x4e8
   __DATA.__bss: 0x3ca0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5454
-  Symbols:   1302
-  CStrings:  815
+  Functions: 5666
+  Symbols:   1300
+  CStrings:  830
 
Symbols:
+ _$s20ModelManagerServices9StateDumpV05AssetD0V10descriptor4path4cost11isCacheable18dynamicModeAllowed018useEnergyEfficientM017inferenceProvider04loadD00J6Locked20timeLastRequestEnded0vw17ForegroundSessionY021requiredByOtherAssets18foregroundSessions8requestsAeA09InferencesF10DescriptorV_SSAA0F4CostVS3bAA09InferenceS10DescriptorVAA04LoadD0OSb10Foundation4DateVA2_ShySSGShyAA14UUIDIdentifierVyAA7SessionCGGShyA5_yAA0X8MetadataVGGtcfC
+ _$ss6ResultOMn
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocPartialClassInstance
- _$s20ModelManagerServices9StateDumpV05AssetD0V10descriptor4path4cost11isCacheable18dynamicModeAllowed018useEnergyEfficientM017inferenceProvider04loadD020timeLastRequestEnded0uv17ForegroundSessionX021requiredByOtherAssets18foregroundSessions8requestsAeA09InferencesF10DescriptorV_SSAA0F4CostVS3bAA09InferenceS10DescriptorVAA04LoadD0O10Foundation4DateVA1_ShySSGShyAA14UUIDIdentifierVyAA0Z0CGGShyA4_yAA0W8MetadataVGGtcfC
- _$sScg17makeAsyncIteratorScg0C0Vyxq__GyF
- _$sScg8IteratorV4next9isolationxSgScA_pSgYi_tYaq_YKF
- _$sScg8IteratorV4next9isolationxSgScA_pSgYi_tYaq_YKFTu
- _$sScg8IteratorVMn
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "Invalidating and removing asset for force version change: %s"
+ "Lock deinited for %s while locked [%u]"
+ "Locking %s [%u]"
+ "Locking NonAssetBackedResourceVersionLock %s"
+ "ModelManager failed to switch assets after assetVersionMismatch"
+ "Resolved %s assets to: %s"
+ "Unlocking %s [%u]"
+ "Unlocking NonAssetBackedResourceVersionLock %s"
+ "_TtC13modelmanagerd30AssetBackedResourceVersionLock"
+ "assetFromModelCatalogAsset found existing: %s"
+ "assetFromModelCatalogAsset resolving new asset for: %s with version: %s"
+ "assetFromModelCatalogAsset unable to lock existing asset: %s"
+ "finishPendingTransitionTask failed to lock asset: %s"
+ "lockWithState"
+ "updateAvailable for %s returned: [%{bool}d"

```

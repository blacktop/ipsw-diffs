## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1499.100.48.0.0
-  __TEXT.__text: 0x83c24
-  __TEXT.__auth_stubs: 0x13c0
+1624.0.0.0.0
+  __TEXT.__text: 0x8af30
   __TEXT.__const: 0x1ff0
-  __TEXT.__cstring: 0x21f7b
+  __TEXT.__cstring: 0x232a6
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x1138
-  __TEXT.__objc_methname: 0x81
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x840
+  __TEXT.__unwind_info: 0x1210
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x9f0
-  __AUTH_CONST.__const: 0x950
-  __AUTH_CONST.__cfstring: 0xf220
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x9b8
+  __AUTH_CONST.__cfstring: 0xfa60
+  __AUTH_CONST.__auth_got: 0xa08
   __DATA.__data: 0x160
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCE46D9E-4FD3-3861-87FF-3FBF91BC7158
-  Functions: 4395
-  Symbols:   9614
-  CStrings:  5985
+  UUID: 05F8D0F7-1D85-3958-A820-83A9EE378827
+  Functions: 4610
+  Symbols:   10059
+  CStrings:  6171
 
Symbols:
+ _AMFDRDataLocalEncodeImplementatation
+ _AMFDRDataLocalEncodeImplementatation.cold.1
+ _AMFDRDataLocalEncodeImplementatation.cold.2
+ _AMFDRDataLocalSignManifestForMultiData
+ _AMFDRDataLocalSignManifestForMultiData.cold.1
+ _AMFDRDataLocalSignManifestForMultiData.cold.10
+ _AMFDRDataLocalSignManifestForMultiData.cold.11
+ _AMFDRDataLocalSignManifestForMultiData.cold.12
+ _AMFDRDataLocalSignManifestForMultiData.cold.13
+ _AMFDRDataLocalSignManifestForMultiData.cold.14
+ _AMFDRDataLocalSignManifestForMultiData.cold.15
+ _AMFDRDataLocalSignManifestForMultiData.cold.16
+ _AMFDRDataLocalSignManifestForMultiData.cold.17
+ _AMFDRDataLocalSignManifestForMultiData.cold.2
+ _AMFDRDataLocalSignManifestForMultiData.cold.3
+ _AMFDRDataLocalSignManifestForMultiData.cold.4
+ _AMFDRDataLocalSignManifestForMultiData.cold.5
+ _AMFDRDataLocalSignManifestForMultiData.cold.6
+ _AMFDRDataLocalSignManifestForMultiData.cold.7
+ _AMFDRDataLocalSignManifestForMultiData.cold.8
+ _AMFDRDataLocalSignManifestForMultiData.cold.9
+ _AMFDRDataVerifyImg4Integrity.cold.8
+ _AMFDRDataVerifyInternal.cold.23
+ _AMFDRDataVerifySealingManifest
+ _AMFDRDataVerifySealingManifest.cold.1
+ _AMFDRDataVerifySealingManifest.cold.2
+ _AMFDRDataVerifySealingManifest.cold.3
+ _AMFDRDataVerifySealingManifest.cold.4
+ _AMFDRDataVerifySealingManifest.cold.5
+ _AMFDRDataVerifySealingManifest.cold.6
+ _AMFDRDataVerifySealingManifest.cold.7
+ _AMFDRDataVerifySealingManifest.cold.8
+ _AMFDRDecodeManifestBodyInfoCreate
+ _AMFDRDecodeManifestBodyInfoDestroy
+ _AMFDRDecodeManifestBodyInfoGetComponentType
+ _AMFDRDecodeManifestBodyInfoGetDataClass
+ _AMFDRDecodeManifestBodyInfoGetDataInstance
+ _AMFDRDecodeManifestBodyInfoNext
+ _AMFDRDecodeManifestBodyInfoNext.cold.1
+ _AMFDRDecodeManifestBodyInfoNext.cold.2
+ _AMFDRDecodeManifestBodyInfoNext.cold.3
+ _AMFDREncodeManifestContextAddImg4Context
+ _AMFDREncodeManifestContextCreateSignedManifest
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.1
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.2
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.3
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.4
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.5
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.6
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.7
+ _AMFDREncodeManifestContextCreateSignedManifest.cold.8
+ _AMFDREncodeProducerIDContextDestroy
+ _AMFDRGetComponentTypeForClassInstance
+ _AMFDRGetComponentTypeForClassInstance.cold.1
+ _AMFDRGetComponentTypeForClassInstance.cold.2
+ _AMFDRGetComponentTypeForClassInstance.cold.3
+ _AMFDRGetComponentTypeForClassInstance.cold.4
+ _AMFDRGetComponentTypeForClassInstance.cold.5
+ _AMFDRSealedDataClearMultiManifest
+ _AMFDRSealedDataClearMultiManifest.cold.1
+ _AMFDRSealedDataGetMultiManifest
+ _AMFDRSealedDataGetMultiManifest.cold.1
+ _AMFDRSealedDataPopulatePairedSoCs
+ _AMFDRSealedDataPopulatePairedSoCs.cold.1
+ _AMFDRSealedDataPopulatePairedSoCs.cold.2
+ _AMFDRSealedDataPopulatePairedSoCs.cold.3
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.1
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.10
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.11
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.12
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.2
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.3
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.4
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.5
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.6
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.7
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.8
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo.cold.9
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.1
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.2
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.3
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.4
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.5
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.1
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.10
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.2
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.3
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.4
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.5
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.6
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.7
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.8
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass.cold.9
+ _AMFDRSealingMapCallMGCopyAnswerInternal.cold.8
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.1
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.10
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.11
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.12
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.13
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.14
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.15
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.16
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.2
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.3
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.4
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.5
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.6
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.7
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.8
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo.cold.9
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddDataClass.cold.6
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.1
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.2
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.3
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.4
+ _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData.cold.5
+ _AMFDRSealingMapCopyLocalMultiCombinedDataEnd.cold.8
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.1
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.10
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.11
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.12
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.13
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.2
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.3
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.4
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.5
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.6
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.7
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.8
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass.cold.9
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.1
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.10
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.11
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.12
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.2
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.3
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.4
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.5
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.6
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.7
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.8
+ _AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance.cold.9
+ _AMFDRSealingMapCreateRepairConfigurationAsidMetadataInternalBlob.cold.37
+ _AMFDRSealingMapCreateRepairConfigurationAsidMetadataInternalBlob.cold.38
+ _AMFDRSealingMapRegisterCustomQueryProvider
+ _AMFDRSealingMapRegisterCustomQueryProvider.cold.1
+ _AMFDRSealingMapRegisterCustomQueryProvider.cold.2
+ _AMFDRSealingMapRegisterCustomQueryProvider.cold.3
+ _AMFDRSealingMapRegisterCustomQueryProvider.cold.4
+ _AMFDRSetComponentTypeForClassInstance
+ _AMFDRSetComponentTypeForClassInstance.cold.1
+ _AMFDRSetComponentTypeForClassInstance.cold.2
+ _AMFDRSetComponentTypeForClassInstance.cold.3
+ _AMFDRSetComponentTypeForClassInstance.cold.4
+ _AMFDRSetComponentTypeForClassInstance.cold.5
+ _CFAllocatorAllocateTyped
+ _CFAllocatorDeallocate
+ _FDREncodeManifestContextDestroy
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_123
+ __AMFDRCopyChipIDNumberFromChipIDECIDDataInstance
+ __AMFDRCopyChipIDNumberFromChipIDECIDDataInstance.cold.1
+ __AMFDRCopyChipIDNumberFromChipIDECIDDataInstance.cold.2
+ __AMFDRCopyChipIDNumberFromChipIDECIDDataInstance.cold.3
+ __AMFDRCopyChipIDNumberFromChipIDECIDDataInstance.cold.4
+ __AMFDRDataLocalCreateSubCCDigestObjP
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.1
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.2
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.3
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.4
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.5
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.6
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.7
+ __AMFDRDataLocalCreateSubCCDigestObjP.cold.8
+ __AMFDRDataLocalSignContextCopyDescription
+ __AMFDRDataLocalSignContextEqual
+ __AMFDRDataLocalSignContextRelease
+ __AMFDRDataLocalSignContextRetain
+ __AMFDRDecodeGetDataInfoCallback
+ __AMFDREncodeCreatePayload
+ __AMFDREncodeCreatePayload.cold.1
+ __AMFDREncodeCreateProducerIDFromPEMCert
+ __AMFDRHttpRequestSendSync.cold.10
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.27
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.28
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.29
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.30
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.31
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.32
+ __AMFDRSealingManifestCopyDataClassesAndInstances.cold.33
+ __AMFDRSealingMapCompareRepairConfigurationEntryWithSealingMapEntry
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.1
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.2
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.3
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.4
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.5
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.6
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.7
+ __AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance.cold.8
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.1
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.2
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.3
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.4
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.5
+ __AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext.cold.6
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.1
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.2
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.3
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.4
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.5
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.6
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.7
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.8
+ __AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry.cold.9
+ __AMFDRSealingMapInfoSetValue
+ __AMFDRSealingMapInfoSetValue.cold.1
+ __AMFDRSealingMapInfoSetValue.cold.2
+ __AMFDRSealingMapInfoSetValue.cold.3
+ __AMFDRSealingMapInfoSetValue.cold.4
+ __AMFDRSealingMapInfoSetValue.cold.5
+ ___AMFDRSealingMapCallMGCopyAnswerInternal_block_invoke
+ ___AMFDRSealingMapCallMGCopyAnswerInternal_block_invoke.cold.1
+ ___AMFDRSealingMapRegisterCustomQueryProvider_block_invoke
+ ____getCustomQueryProviderRegistryQueue_block_invoke
+ ____getCustomQueryProviderRegistry_block_invoke
+ ___block_descriptor_tmp.1333
+ ___block_descriptor_tmp.1337
+ ___block_descriptor_tmp.1368
+ ___block_descriptor_tmp.1372
+ ___block_descriptor_tmp.1376
+ ___block_descriptor_tmp.1378
+ ___block_descriptor_tmp.1387
+ ___block_descriptor_tmp.1467
+ ___block_descriptor_tmp.1489
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.1562
+ ___block_descriptor_tmp.1565
+ ___block_descriptor_tmp.1740
+ ___block_descriptor_tmp.182
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.199
+ ___block_descriptor_tmp.220
+ ___block_literal_global.1335
+ ___block_literal_global.1339
+ ___block_literal_global.1370
+ ___block_literal_global.1374
+ ___block_literal_global.1389
+ ___block_literal_global.1469
+ ___block_literal_global.154
+ ___block_literal_global.1564
+ ___block_literal_global.1567
+ ___block_literal_global.184
+ ___block_literal_global.222
+ __dispatch_queue_attr_concurrent
+ __getCustomQueryProviderRegistry.onceToken
+ __getCustomQueryProviderRegistry.registry
+ __getCustomQueryProviderRegistryQueue.onceToken
+ __getCustomQueryProviderRegistryQueue.queue
+ __providerInfoReleaseCallback
+ __providerInfoRetainCallback
+ _dispatch_barrier_sync
+ _kAMFDRDataLocalSignContextCFArrayCallbacks
+ _kAMFDRSealingMapInfoQueryAttribute
+ _kAMFDRSealingMapInfoQueryComponentType
+ _kAMFDRSealingMapInfoQueryOptionDataClassOnly
+ _kAMFDRSealingMapRepairConfigurationComponentType
+ _kAMFDRSealingMapRepairConfigurationOptionAsid
+ _kAMFDRSealingMapRepairConfigurationOptionDataClass
+ _kAMFDRSealingMapRepairConfigurationOptionDataInstance
+ _kCFNull
+ _kImg4DecodeSecureBootG7Rsa4kSha384IM4C
+ _malloc_type_realloc
- _AMFDRDataCopyRawDataAndManifests
- _AMFDRDataCopyRawDataAndManifests.cold.1
- _AMFDRDataCopyRawDataAndManifests.cold.2
- _AMFDRDataCopyRawDataAndManifests.cold.3
- _AMFDRDataCopyRawDataAndManifests.cold.4
- _AMFDRDataCopyRawDataAndManifests.cold.5
- _AMFDRDataCopyRawDataAndManifests.cold.6
- _AMFDRDataCopyRawDataAndManifests.cold.7
- _AMFDRDataCopyRawDataAndManifests.cold.8
- _AMFDRDataCopyRawDataAndManifests.cold.9
- _AMFDRDataCreateRepairConfigurationAsidMetadata.cold.32
- _AMFDRDataLocalSign.cold.28
- _AMFDRDataLocalSign.cold.29
- _AMFDRDataLocalSign.cold.30
- _AMFDRDataLocalSign.cold.31
- _AMFDRDataLocalSign.cold.32
- _AMFDRDataLocalSign.cold.33
- _AMFDRDataLocalSign.cold.34
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.10
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.11
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.12
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.4
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.5
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.6
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.7
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.8
- _AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass.cold.9
- _AMFDRSealingMapGetPairedSoCs
- _AMSupportDigestMd5
- __AMFDRDecodeGetDataInstCallback
- ___block_descriptor_tmp.1246
- ___block_descriptor_tmp.1250
- ___block_descriptor_tmp.1254
- ___block_descriptor_tmp.1256
- ___block_descriptor_tmp.1265
- ___block_descriptor_tmp.1348
- ___block_descriptor_tmp.1370
- ___block_descriptor_tmp.1443
- ___block_descriptor_tmp.1446
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.1602
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.210
- ___block_literal_global.1248
- ___block_literal_global.1252
- ___block_literal_global.1267
- ___block_literal_global.1350
- ___block_literal_global.1445
- ___block_literal_global.1448
- ___block_literal_global.153
- ___block_literal_global.183
- ___block_literal_global.212
- _kAMFDRSealingMapRepairConfigurationAsid
- _kAMFDRSealingMapRepairConfigurationDataClassInstance
- _kAMFDRSealingMapRepairConfigurationTypeSecondary
CStrings:
+ "%@-%@:%@"
+ "'%@' sealing map entry does not have %@"
+ "*outManifest is NULL"
+ "<AMFDRLocalDataSignContext: (null)>"
+ "<AMFDRLocalDataSignContext: dataClass: %@, dataInstance: %@, data: %@, assembly ID: %@, subCC digest list: %@>"
+ "AMFDRDataHTTPMultiSign error [%ld] for %@: %ld"
+ "AMFDRDataLocalSignManifestForMultiData"
+ "AMFDRDataVerifySealingManifest"
+ "AMFDRDecodeManifestBodyInfoGetComponentType failed"
+ "AMFDRDecodeManifestBodyInfoGetDataClass failed"
+ "AMFDRDecodeManifestBodyInfoGetDataInstance failed"
+ "AMFDRDecodeManifestBodyInfoNext"
+ "AMFDREncodeManifestContextAddImg4Context failed"
+ "AMFDREncodeManifestContextCreateSignedManifest"
+ "AMFDREncodeManifestContextCreateSignedManifest failed"
+ "AMFDRGetComponentTypeForClassInstance"
+ "AMFDRSealedDataClearMultiManifest"
+ "AMFDRSealedDataGetMultiManifest"
+ "AMFDRSealedDataPopulatePairedSoCs"
+ "AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo"
+ "AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData"
+ "AMFDRSealingManifestCopyMultiInstanceAndInfoForClass"
+ "AMFDRSealingMapCallMGCopyAnswerDefault"
+ "AMFDRSealingMapCopyDataClassesInstancesAndInfo"
+ "AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData"
+ "AMFDRSealingMapCopyMultiInstanceAndInfoForClass"
+ "AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance"
+ "AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance failed for %@:%@"
+ "AMFDRSealingMapRegisterCustomQueryProvider"
+ "AMFDRSetComponentTypeForClassInstance"
+ "AMFDRSetComponentTypeForClassInstance failed"
+ "Allow unsealed, just return true..."
+ "Attribute/"
+ "CFStringCreateExternalRepresentation(componentTypeData) failed"
+ "Cannot convert CFNumber %@"
+ "Cannot parse data instance %@ to obtain the chipID"
+ "ComponentAttributeComponentIndex"
+ "ComponentType"
+ "ComponentType/"
+ "ComponentTypes"
+ "Could not get UniqueDeviceID"
+ "DEREncoderAddData failed for component index"
+ "DataClass"
+ "DataInstance"
+ "Failed to allocate memory for digests"
+ "Failed to compute digest for %s:%s"
+ "Failed to create an unsealed manifest for multiple data"
+ "Failed to find any of the subCCs: %@ for %@"
+ "Failed to find any of the subCCs: %@ from %@:%@"
+ "Force commit is enabled, continue to populate data anyway"
+ "Image4SecureBootCertificateFormat"
+ "Img4DecodeGetPropertyData(0x%x) failed."
+ "Img4DecodeGetPropertyData(kFDRTag_cptp) failed."
+ "InfoQueryAttribute"
+ "InfoQueryComponentType"
+ "InfoQueryOptionDataClassOnly"
+ "LynxSerialNumber"
+ "No data was found for %@"
+ "No digest and no data to compute it from"
+ "Offline signing is not implemented in AMFDRDataLocalSignManifestForMultiData yet"
+ "Overriding query for %@"
+ "Skip verifying type info"
+ "There's no signContext"
+ "Unable to get the sealing manifest"
+ "Unable to get trust object"
+ "_AMFDRCopyChipIDNumberFromChipIDECIDDataInstance"
+ "_AMFDRDataLocalSignContextToImg4Context"
+ "_AMFDRDataLocalSignContextToImg4Context failed"
+ "_AMFDRDecodeGetDataInfoCallback"
+ "_AMFDRDecodeManifestBodyNext failed"
+ "_AMFDREncodeCreatePayload"
+ "_AMFDREncodeCreatePayload failed to return a payload"
+ "_AMFDREncodeCreateProducerIDFromPEMCert"
+ "_AMFDREncodeCreateProducerIDFromPEMCert failed %d"
+ "_AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForDataClassInstance"
+ "_AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext"
+ "_AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry"
+ "_AMFDRSealingMapInfoSetValue"
+ "_AMFDRSealingMapInfoSetValue attribute failed"
+ "_AMFDRSealingMapInfoSetValue componentType failed"
+ "amfdr->componentTypeDict is NULL"
+ "amfdrCopy is NULL"
+ "amfdrCopy->optionsDict is NULL"
+ "amfdrOptions is NULL"
+ "asidExceptionDict has wrong type %@"
+ "cannot create subCCData"
+ "cannot determine paired SoC if sealedDataInstance is missing"
+ "cannot populate paired SoC if dataClassArray (%@) or dataInstanceArray (%@) is malformed"
+ "com.apple.libfdr.customQueryProviderRegistryQueue"
+ "componentType is invalid: %@"
+ "componentTypeData is NULL"
+ "componentTypeDict queried from sealing map is %@"
+ "copied localData is NULL for %@:%@"
+ "dataClass cannot be empty"
+ "dataClass or dataInstance is NULL"
+ "dataClassArray allocation failed"
+ "dataClassComponentType is NULL"
+ "dataInstanceArray CFArrayCreateMutableCopy failed"
+ "dataInstanceArray allocation failed"
+ "dataInstanceCreated is NULL"
+ "exceptionDataClass has wrong type %@"
+ "failed copy componentTypeDict from amfdrRemote to amfdrLocal"
+ "failed to add ComponentIndex attribute"
+ "failed to add subCC %@ for %@:%@"
+ "failed to allocate memory for signContextArray"
+ "failed to allocate mutableComponentTypes arrays"
+ "failed to copy chipIDNum from %@"
+ "failed to copy data for %@-%@"
+ "failed to create componentTypeStr"
+ "failed to create dataVersion"
+ "failed to find corresponding component type"
+ "failed to get component type of %@:%@"
+ "failed to get custom query provider queue/registry"
+ "im4c"
+ "info allocation failed"
+ "info is malformed"
+ "infoKey allocation failed"
+ "infoValue allocation failed"
+ "kFDRTag_cptp property != fdrDecode->componentType"
+ "kFDRTag_cptp property length != fdrDecode->componentType.length"
+ "keySuffix is malformed"
+ "localSignContext is NULL"
+ "localSignContext->_subCCDigestObjPData is NULL"
+ "localSignContext->dataInstanceData is NULL"
+ "malformed componentType: %@"
+ "malformed dataClasses: %@, dataInstances:%@, componentTypes:%@"
+ "malformed kAMFDRCertifyComponentAttributeComponentIndex, expected CFData."
+ "manifestBodyInfo is NULL"
+ "missingDataIdentifiers"
+ "missingDataIdentifiers allocation failed"
+ "no key to register"
+ "outChipIDNumber is NULL"
+ "outComponentType is NULL"
+ "outManifest is NULL."
+ "outSignedManifest is NULL"
+ "pManifestBodyInfo is NULL"
+ "pairedSoCArray cannot be allocated"
+ "repairConfiguration not supported for this product"
+ "sealingMapEntry is malformed: %@"
+ "sealingMapEntry malformed:'%@'"
+ "signContextArray is empty"
+ "subCC %@ is missing for %@:%@"
+ "subCC digest encoding failed for %@:%@"
+ "value is malformed"
- " AMFDRDataCopyExtraManifests failed to copy manifest for %@-%@"
- "AMFDRDataCopyExtraManifests failed to copy device manifest for %@-%@"
- "AMFDRDataCopyRawDataAndManifests"
- "AMFDRDataHTTPMultiSign error for %@: %ld"
- "Could not split dataClassInstance"
- "DataClassInstance"
- "PairedSoC"
- "_AMFDRDecodeGetDataInstCallback"
- "_AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveManifest"
- "currently don't support creating manifest from multiple data"
- "data"
- "dataClassInstance has wrong type %@"
- "failed to copy %@-%@"
- "failed to copy data and manifest"
- "failed to copy data payload for %@-%@"
- "failed to copy device manifest for %@-%@"
- "initWithBytesNoCopy:length:deallocator:"
- "initWithBytesNoCopy:length:encoding:deallocator:"
- "instancesRespondToSelector:"
- "manifestArray is empty"
- "outDeviceManifest is NULL"
- "r5pA2qLgR86BQKwgMjPWzg"
- "string"
- "subCC %@ is missing"

```

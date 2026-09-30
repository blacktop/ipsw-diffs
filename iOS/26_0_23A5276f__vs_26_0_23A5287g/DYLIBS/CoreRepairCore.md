## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.0.65.0.0
-  __TEXT.__text: 0x80e74
+921.0.82.0.0
+  __TEXT.__text: 0x813bc
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x396c
+  __TEXT.__objc_methlist: 0x39a4
   __TEXT.__const: 0x7f0
-  __TEXT.__oslogstring: 0x8d80
-  __TEXT.__cstring: 0x567e
+  __TEXT.__oslogstring: 0x8d93
+  __TEXT.__cstring: 0x57cb
   __TEXT.__gcc_except_tab: 0x1524
-  __TEXT.__unwind_info: 0x1138
+  __TEXT.__unwind_info: 0x1158
   __TEXT.__objc_classname: 0x7d0
-  __TEXT.__objc_methname: 0x7dd0
+  __TEXT.__objc_methname: 0x7df9
   __TEXT.__objc_methtype: 0x14ba
-  __TEXT.__objc_stubs: 0x62c0
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0x8e0
+  __TEXT.__objc_stubs: 0x62e0
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f50
+  __DATA_CONST.__objc_selrefs: 0x1f60
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x868
+  __DATA_CONST.__objc_arraydata: 0x8b0
   __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x6de0
   __AUTH_CONST.__objc_const: 0x57e8
-  __AUTH_CONST.__objc_arrayobj: 0x570
+  __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0xeb0
   __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x690
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd8
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: B3D5332A-B696-3F06-89A7-B41BE0D8AD41
-  Functions: 2228
-  Symbols:   7368
-  CStrings:  4642
+  UUID: BC0ABB90-0F89-3E0B-8EBC-FCA25E26C1CB
+  Functions: 2229
+  Symbols:   7366
+  CStrings:  4670
 
Symbols:
+ +[CRBatteryController sharedInstance]
+ +[CRBatteryController sharedInstance].cold.1
+ +[CRFDRUtils(ComponentState) hasMesaUnsealedData]
+ +[CRFDRUtils(ComponentState) hasMesaUnsealedData].cold.1
+ +[CRPearlController powerCycleSensor:]
+ -[CRBatteryController getBMUType]
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.25
+ -[CRFDRBaseDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.2
+ __OBJC_$_CLASS_METHODS_CRPearlController
+ __OBJC_$_INSTANCE_METHODS_CRBatteryController
+ ___37+[CRBatteryController sharedInstance]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0i8"NSError"12ls32l8r48l8r56l8s40l8
+ ___block_literal_global.103
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.203
+ ___block_literal_global.206
+ ___block_literal_global.229
+ _generateVeridianFWRequestWithOptions_block_invoke_7.cold.5
+ _objc_msgSend$getBMUType
+ _objc_msgSend$getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:
+ _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.3
- +[CRUtils powerCycleSensor:]
- -[CRFDRBaseDeviceHandler getCurrentMinimalManifestsWithVersions:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.1
- -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.1
- -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.2
- -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.3
- -[CRFDRBaseDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
- -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0i8"NSError"12lr40l8r48l8s32l8
- ___block_literal_global.102
- ___block_literal_global.167
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.202
- ___block_literal_global.205
- ___block_literal_global.213
- _objc_msgSend$getUpdateDataClassesAndInstancesWithPartSPC:withError:
- _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.1
- _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.2
- _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.3
- _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.4
- _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.5
CStrings:
+ "+[CRPearlController powerCycleSensor:]"
+ ",FirmwareMap"
+ ",Ticket"
+ "AMFDRSealingManifestCopyMinimalManifestClassesAndInstancesVersions failed"
+ "BMU"
+ "BMU type: %@"
+ "Could not delete value for key %@: %08x"
+ "Could not delete value for key %@: %08x\n"
+ "Could not read value for key %@"
+ "Could not set value for key %@: %08x"
+ "Could not set value for key %@: %08x\n"
+ "Decode KBB sealing manifest failed"
+ "Failed to init CRBatteryController"
+ "Get component state of %@"
+ "Got component state of %@: %@"
+ "Issue"
+ "Mismatch"
+ "Original"
+ "ServicePart"
+ "Unexpected loop count: %d"
+ "Unsupported"
+ "UsedPart"
+ "getBMUType"
+ "getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:"
+ "hasMesaUnsealedData"
+ "updaterOptions missing or invalid"
- "+[CRUtils powerCycleSensor:]"
- "BMU,FirmwareMap"
- "BMU,Ticket"
- "Could not delete value. Error: 0x%08x"
- "Could not delete value:%08x\n"
- "Could not read value"
- "Could not save value:%08x\n"
- "Could not set value. Error: 0x%08x"
- "Get state of component %d"
- "Got state: %d"
- "component %d"
- "getUpdateDataClassesAndInstancesWithPartSPC:withError:"

```

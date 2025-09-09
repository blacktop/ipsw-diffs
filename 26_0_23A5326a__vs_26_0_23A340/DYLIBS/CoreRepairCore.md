## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 921.0.120.0.0
-  __TEXT.__text: 0x82504
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x3a3c
+  __TEXT.__text: 0x84530
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_methlist: 0x3a8c
   __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x8fa4
-  __TEXT.__cstring: 0x57ea
+  __TEXT.__oslogstring: 0x912f
+  __TEXT.__cstring: 0x5aa0
   __TEXT.__gcc_except_tab: 0x1750
-  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__unwind_info: 0x11c8
   __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methname: 0x7f3d
+  __TEXT.__objc_methname: 0x7fc0
   __TEXT.__objc_methtype: 0x1538
-  __TEXT.__objc_stubs: 0x63c0
+  __TEXT.__objc_stubs: 0x6540
   __DATA_CONST.__got: 0x560
-  __DATA_CONST.__const: 0x908
+  __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc8
+  __DATA_CONST.__objc_selrefs: 0x1ff8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x8b0
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x6e00
+  __DATA_CONST.__objc_arraydata: 0xa60
+  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__const: 0x520
+  __AUTH_CONST.__cfstring: 0x7280
   __AUTH_CONST.__objc_const: 0x58b8
-  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__objc_arrayobj: 0x660
+  __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x690
   __DATA.__common: 0x30
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: F0F597BD-84DB-399C-9D46-1168FCF3DF59
-  Functions: 2247
-  Symbols:   7422
-  CStrings:  4706
+  UUID: FFEED41E-A266-3EDA-B533-D646A4F75069
+  Functions: 2260
+  Symbols:   7470
+  CStrings:  4800
 
Symbols:
+ +[CRBatteryController psimPresent]
+ +[CRBatteryController psimPresent].cold.1
+ +[CRBatteryController supportMultiBatteryTypes]
+ +[CRBatteryController supportMultiBatteryTypes].cold.1
+ +[CRDeviceMap supportMLBOnlyRepair]
+ -[CRBatteryController _psimPresent]
+ -[CRBatteryController _psimPresent].cold.1
+ -[CRBatteryController _supportMultiBatteryTypes]
+ -[CRBatteryController _supportMultiBatteryTypes].cold.1
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.8
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.9
+ -[CRUtils getPathForAriesFirmwareWithError:]
+ _AMFDRSealingMapCopyMinimalManifestClassesAndInstancesWithAttribute
+ _OUTLINED_FUNCTION_37
+ __OBJC_$_INSTANCE_METHODS_CRBatteryController
+ ___34+[CRBatteryController psimPresent]_block_invoke
+ ___47+[CRBatteryController supportMultiBatteryTypes]_block_invoke
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.256
+ ___block_literal_global.106
+ ___block_literal_global.17
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.209
+ ___block_literal_global.232
+ ___block_literal_global.32
+ ___block_literal_global.37
+ ___block_literal_global.50
+ ___block_literal_global.72
+ ___block_literal_global.92
+ _objc_msgSend$_psimPresent
+ _objc_msgSend$_supportMultiBatteryTypes
+ _objc_msgSend$currentDataClasses
+ _objc_msgSend$currentDataInstances
+ _objc_msgSend$getCurrentMinimalManifestsWithVersions:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:
+ _objc_msgSend$getDataClassesAndInstancesOfKBBWith:dataClasses:dataInstances:propertiesDict:fdrError:
+ _objc_msgSend$getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:
+ _objc_msgSend$getPathForAriesFirmwareWithError:
+ _objc_msgSend$initWithType:locKey:superModule:fdrKeys:
+ _objc_msgSend$psimPresent
+ _objc_msgSend$supportMLBOnlyRepair
+ _objc_msgSend$supportMultiBatteryTypes
+ _psimPresent.onceToken
+ _psimPresent.psimPresent
+ _supportMultiBatteryTypes.hasMultiBatteryTypes
+ _supportMultiBatteryTypes.onceToken
- _OUTLINED_FUNCTION_38
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.244
- ___block_literal_global.103
- ___block_literal_global.168
- ___block_literal_global.170
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.196
- ___block_literal_global.198
- ___block_literal_global.203
- ___block_literal_global.229
- ___block_literal_global.34
- ___block_literal_global.44
- ___block_literal_global.69
- ___block_literal_global.86
CStrings:
+ "/usr/standalone/update/Aries/"
+ "/usr/standalone/update/Summerville/"
+ "0x5068"
+ "AMFDRSealingMapCopyMinimalManifestClassesAndInstancesWithAttribute failed"
+ "Aries"
+ "BMU2"
+ "BWCl"
+ "Current MinimalManifests: %@, %@"
+ "Current pearl instance: %@"
+ "Failed to get current pearl instance"
+ "Failed to get kbb pearl instance"
+ "FwPatch"
+ "Get KBB info failed"
+ "IODeviceTree:/product"
+ "IPHONE COMP MLB"
+ "IPHONE ENCLOSURE"
+ "JasmineIR1,BoardID"
+ "JasmineIR1,ChipID"
+ "JasmineIR1,PatchEpoch"
+ "JasmineIR1,Ticket"
+ "KBB MinimalManifests: %@, %@"
+ "KBB pearl instance: %@"
+ "KGB isServicePart without MTUB SPC"
+ "LiDAR"
+ "LidAngleSensor"
+ "Localizable-V53"
+ "Merged MinimalManifests: %@, %@"
+ "No"
+ "No bmu-num-enabled data"
+ "No bmu-num-supported data"
+ "No psim-present data"
+ "Original MinimalManifests: %@, %@"
+ "PART_LIDAR"
+ "PART_LOGIC_BOARD"
+ "Support multi battery types: %@"
+ "TBCl"
+ "TopCase"
+ "Unable to find /product node"
+ "VideoPatch"
+ "Wireless"
+ "_psimPresent"
+ "_supportMultiBatteryTypes"
+ "bmu-num-enabled"
+ "bmu-num-supported"
+ "cCfg"
+ "getCurrentMinimalManifestsWithVersions failed"
+ "getKBBMinimalManifestsWithVersions failed"
+ "getPathForAriesFirmwareWithError:"
+ "mCfg"
+ "psim is present"
+ "psim is present: %@"
+ "psim-present"
+ "psimPresent"
+ "supportMLBOnlyRepair"
+ "supportMultiBatteryTypes"
+ "tCfg"
+ "transferring property %@: %@"

```

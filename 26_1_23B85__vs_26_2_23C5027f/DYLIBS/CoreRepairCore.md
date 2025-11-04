## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.40.62.0.0
-  __TEXT.__text: 0x86200
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x3b04
+921.60.24.0.0
+  __TEXT.__text: 0x8844c
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_methlist: 0x3be4
   __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x92d9
-  __TEXT.__cstring: 0x5b0c
+  __TEXT.__oslogstring: 0x9504
+  __TEXT.__cstring: 0x5b96
   __TEXT.__gcc_except_tab: 0x1758
-  __TEXT.__unwind_info: 0x11d8
-  __TEXT.__objc_classname: 0x806
-  __TEXT.__objc_methname: 0x816e
+  __TEXT.__unwind_info: 0x1210
+  __TEXT.__objc_classname: 0x821
+  __TEXT.__objc_methname: 0x81fb
   __TEXT.__objc_methtype: 0x154e
-  __TEXT.__objc_stubs: 0x66c0
-  __DATA_CONST.__got: 0x560
+  __TEXT.__objc_stubs: 0x6780
+  __DATA_CONST.__got: 0x568
   __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2060
+  __DATA_CONST.__objc_selrefs: 0x2090
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0xaa0
-  __AUTH_CONST.__auth_got: 0xb48
+  __DATA_CONST.__objc_arraydata: 0xb10
+  __AUTH_CONST.__auth_got: 0xb58
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x7360
-  __AUTH_CONST.__objc_const: 0x5948
-  __AUTH_CONST.__objc_arrayobj: 0x6a8
+  __AUTH_CONST.__cfstring: 0x73c0
+  __AUTH_CONST.__objc_const: 0x5a50
+  __AUTH_CONST.__objc_arrayobj: 0x738
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x2e8
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0x2f0
   __DATA.__data: 0x690
   __DATA.__common: 0x30
   __DATA.__bss: 0x98

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: BB0D6790-B0D0-3F03-BEC0-B2BB6249DE14
-  Functions: 2275
-  Symbols:   7518
-  CStrings:  4843
+  UUID: 8C906B3A-9958-3B6F-A23B-9CA2E3849360
+  Functions: 2301
+  Symbols:   7601
+  CStrings:  4871
 
Symbols:
+ +[CRFDRDisplay2DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRDisplay2DeviceHandler isDisplay2ProductType:]
+ -[CRFDRDisplay2DeviceHandler .cxx_destruct]
+ -[CRFDRDisplay2DeviceHandler KBBMLBSerialNumber]
+ -[CRFDRDisplay2DeviceHandler KBBTransferProperties]
+ -[CRFDRDisplay2DeviceHandler copyWithZone:]
+ -[CRFDRDisplay2DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:]
+ -[CRFDRDisplay2DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:].cold.1
+ -[CRFDRDisplay2DeviceHandler getExcludedPropertiesForFactoryReset]
+ -[CRFDRDisplay2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRDisplay2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRDisplay2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRDisplay2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRDisplay2DeviceHandler mlbRepairChecks]
+ -[CRFDRDisplay2DeviceHandler performPostSealingStage:]
+ -[CRFDRDisplay2DeviceHandler setKBBMLBSerialNumber:]
+ -[CRFDRDisplay2DeviceHandler setKBBTransferProperties:]
+ -[CRFDRDisplay2DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:]
+ -[CRFDRDisplay2DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.1
+ -[CRFDRDisplay2DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.2
+ -[CRFDRDisplay2DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.3
+ -[CRPersonalizationManager _init:].cold.4
+ -[CRPreflight componentsWithPrimary:]
+ -[CRPreflight componentsWithRepairable:]
+ -[CoreRepairHelper ensurePrebootPathIsWritable:]
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.1
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.2
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.3
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.4
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.5
+ -[CoreRepairHelper ensurePrebootPathIsWritable:].cold.6
+ GCC_except_table9
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_CRFDRDisplay2DeviceHandler
+ _OBJC_IVAR_$_CRFDRDisplay2DeviceHandler.KBBMLBSerialNumber
+ _OBJC_IVAR_$_CRFDRDisplay2DeviceHandler._KBBTransferProperties
+ _OBJC_METACLASS_$_CRFDRDisplay2DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRDisplay2DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRDisplay2DeviceHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRDisplay2DeviceHandler
+ __OBJC_$_PROP_LIST_CRFDRDisplay2DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRDisplay2DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRDisplay2DeviceHandler
+ ___block_literal_global.108
+ _access
+ _generateSavageFWRequestWithOptions_block_invoke_9
+ _objc_msgSend$_mount:withFlag:
+ _objc_msgSend$componentsWithPrimary:
+ _objc_msgSend$componentsWithRepairable:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$isDisplay2ProductType:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeObjectsInArray:
+ _parsePersonalizationResponseForVeridianFW_block_invoke_8
+ _parsePersonalizationResponseForVeridianFW_block_invoke_8.cold.1
+ _parsePersonalizationResponseForVeridianFW_block_invoke_8.cold.2
+ _statfs
- -[CRPreflight componentsWithPrimaryKeys:]
- ___block_literal_global.171
- _generateSavageFWRequestWithOptions_block_invoke_8
- _objc_msgSend$componentsWithPrimaryKeys:
- _parsePersonalizationResponseForVeridianFW_block_invoke_9
- _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.1
- _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.2
CStrings:
+ "%@ already writable"
+ "%@ is now writable"
+ "%@ not writable, remounting"
+ "%@ still not writable after remounting"
+ "%s remounting failed, error: %@"
+ "CRFDRDisplay2DeviceHandler"
+ "Client is not entitled to remount preboot"
+ "Failed to get prebootPath: %@, error: %@"
+ "MLB SPC ignored when not service parts"
+ "Suppress unknown battery status"
+ "Unable to copy current identifier for data classes:%@ error:%@"
+ "Unable to copy current identifier for dataClass: %@"
+ "Updated unsealed with primary components: %@"
+ "Updated unsealed with repairable components: %@"
+ "[WARNING]: Preboot remounting not allowed on external build"
+ "com.apple.private.corerepair.prebootremount"
+ "componentsWithPrimary:"
+ "componentsWithRepairable:"
+ "ensurePrebootPathIsWritable:"
+ "fileSystemRepresentation"
+ "isDisplay2ProductType:"
+ "mount point: %s"
+ "removeObjectForKey:"
+ "removeObjectsInArray:"
+ "restoreSystemPartition :%@"
+ "statfs failed for %@: %@"
- "Updated unsealed: %@"
- "componentsWithPrimaryKeys:"

```

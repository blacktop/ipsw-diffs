## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.0.98.0.0
-  __TEXT.__text: 0x813e4
+921.0.119.0.0
+  __TEXT.__text: 0x824d4
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x39a4
-  __TEXT.__const: 0x7f0
-  __TEXT.__oslogstring: 0x8d93
-  __TEXT.__cstring: 0x57cb
-  __TEXT.__gcc_except_tab: 0x1524
-  __TEXT.__unwind_info: 0x1158
-  __TEXT.__objc_classname: 0x7d0
-  __TEXT.__objc_methname: 0x7df9
-  __TEXT.__objc_methtype: 0x14ba
-  __TEXT.__objc_stubs: 0x62e0
-  __DATA_CONST.__got: 0x558
+  __TEXT.__objc_methlist: 0x3a3c
+  __TEXT.__const: 0x7f8
+  __TEXT.__oslogstring: 0x8fa4
+  __TEXT.__cstring: 0x57ea
+  __TEXT.__gcc_except_tab: 0x1750
+  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__objc_classname: 0x7f0
+  __TEXT.__objc_methname: 0x7f3d
+  __TEXT.__objc_methtype: 0x1538
+  __TEXT.__objc_stubs: 0x63c0
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x908
-  __DATA_CONST.__objc_classlist: 0x2b0
-  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f60
+  __DATA_CONST.__objc_selrefs: 0x1fc8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x8b0
   __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x6de0
-  __AUTH_CONST.__objc_const: 0x57e8
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x6e00
+  __AUTH_CONST.__objc_const: 0x58b8
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0xeb0
+  __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x690
-  __DATA.__bss: 0xd8
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x100
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: EEDFB6A8-D383-3309-A8F0-007E8AC23354
-  Functions: 2229
-  Symbols:   7366
-  CStrings:  4670
+  UUID: DC5B6D70-E001-32E1-923F-ADC5EBC12756
+  Functions: 2247
+  Symbols:   7422
+  CStrings:  4706
 
Symbols:
+ +[CRBatteryController getBMUType]
+ +[CRComponentSigning sharedInstance]
+ +[CRComponentSigning sharedInstance].cold.1
+ +[NSUserDefaults(CoreRepairGroup) groupStandardUserDefaults]
+ +[NSUserDefaults(CoreRepairGroup) groupUserDefaultsWithSuiteName:]
+ -[CRFDRBaseDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRSmcController closeAppleSMC:]
+ -[CRSmcController isSMCKeyAvailable:keyName:]
+ -[CRSmcController isSMCKeyAvailable:keyName:].cold.1
+ -[CRSmcController isSMCKeyAvailable:keyName:].cold.2
+ -[CRSmcController openAppleSMC:port:]
+ -[CRSmcController openAppleSMC:withRetry:]
+ -[CRSmcController readSMCKey:key:readData:dataSize:oSize:]
+ -[CRSmcController readSMCKey:keyName:rval:]
+ -[CRSmcController readSMCKey:keyName:rval:].cold.1
+ -[CRSmcController readSMCKey:keyName:rval:].cold.2
+ -[CRSmcController readSMCKey:keyName:rval:].cold.3
+ -[CRSmcController writeSMCKey:key:writeData:dataSize:]
+ -[CRSmcController writeSMCKey:keyName:data:size:]
+ -[CRSmcController writeSMCKey:keyName:data:size:].cold.1
+ -[CRSmcController writeSMCKey:keyName:data:size:].cold.2
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table9
+ _OBJC_CLASS_$_CRSmcController
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_CRSmcController
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSUserDefaults_$_CoreRepairGroup
+ __OBJC_$_CATEGORY_NSUserDefaults_$_CoreRepairGroup
+ __OBJC_$_CLASS_METHODS_CRComponentSigning
+ __OBJC_$_INSTANCE_METHODS_CRSmcController
+ __OBJC_CLASS_RO_$_CRSmcController
+ __OBJC_METACLASS_RO_$_CRSmcController
+ ___36+[CRComponentSigning sharedInstance]_block_invoke
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.244
+ _objc_msgSend$getUpdateDataClassesAndInstancesWithPartSPC:withError:
+ _objc_msgSend$groupUserDefaultsWithSuiteName:
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$openAppleSMC:port:
+ _objc_msgSend$readSMCKey:key:readData:dataSize:oSize:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$writeSMCKey:key:writeData:dataSize:
- -[CRBatteryController getBMUType]
- -[CRFDRBaseDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:]
- -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.1
- -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:].cold.2
- GCC_except_table7
- __OBJC_$_INSTANCE_METHODS_CRBatteryController
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.241
- _generateVeridianFWRequestWithOptions_block_invoke_7.cold.5
- _objc_msgSend$getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:
- _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.3
CStrings:
+ "AllowPropertyMismatch"
+ "AppleSMC"
+ "CRSmcController"
+ "CoreRepairGroup"
+ "Failed to covert from valueBuffer to byteData"
+ "Failed to open SMC, error: %d, retrying..."
+ "Failed to read SMC key %@, error: %d"
+ "Failed to write data to key %@, error: 0x%x"
+ "Missing properties: %@"
+ "No info found for key '%s' (0x%X, 0x%X)\n"
+ "Properties from manifest: %@"
+ "Read failed for key '%s' (0x%X, 0x%X)\n"
+ "SMC key(%@) reading failed, error: 0x%x"
+ "Write failed for key '%s' (0x%X, 0x%X)\n"
+ "Write succeed for key '%s', value returned = 0x%X"
+ "buffer overflow on string/key conversion"
+ "closeAppleSMC:"
+ "destination for key read does not match expected size (Key: '%s', Expected Size: %u, Supplied Size: %lu)\n"
+ "getUpdateDataClassesAndInstancesWithPartSPC:withError:"
+ "groupStandardUserDefaults"
+ "groupUserDefaultsWithSuiteName:"
+ "i20@0:8I16"
+ "i28@0:8^I16S24"
+ "i28@0:8i16^I20"
+ "i36@0:8I16@20^@28"
+ "i40@0:8I16I20^v24Q32"
+ "i44@0:8I16@20^v28Q36"
+ "i48@0:8I16I20^v24Q32^I40"
+ "isSMCKeyAvailable:keyName:"
+ "numberWithChar:"
+ "openAppleSMC:port:"
+ "openAppleSMC:withRetry:"
+ "readSMCKey:key:readData:dataSize:oSize:"
+ "readSMCKey:keyName:rval:"
+ "sleepForTimeInterval:"
+ "standardUserDefaults"
+ "writeSMCKey:key:writeData:dataSize:"
+ "writeSMCKey:keyName:data:size:"
- "Failed to init CRBatteryController"
- "Properties: %@"
- "getUpdateDataClassesAndInstancesWithPartSPC:fdrRemote:withError:"

```

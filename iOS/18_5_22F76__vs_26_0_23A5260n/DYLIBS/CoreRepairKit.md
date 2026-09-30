## CoreRepairKit

> `/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x25f4
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2a7
+921.0.34.0.0
+  __TEXT.__text: 0x18c4
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x173
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__oslogstring: 0x43d
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__oslogstring: 0x28f
+  __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methname: 0x858
-  __TEXT.__objc_methtype: 0x235
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_methname: 0x746
+  __TEXT.__objc_methtype: 0x25d
+  __TEXT.__objc_stubs: 0x500
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x4e8
+  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__cfstring: 0x1c0
+  __AUTH_CONST.__objc_const: 0x4f8
   __AUTH.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 96A98985-72E8-3355-95E8-4CA8F1C403EC
-  Functions: 58
-  Symbols:   91
-  CStrings:  238
+  UUID: 0F06D2AA-29EC-3E86-A32B-409DB3BEABEC
+  Functions: 35
+  Symbols:   230
+  CStrings:  175
 
Symbols:
+ +[CRRepairStatus _wasRepairedWithSysCfg:]
+ +[CRRepairStatus _wasRepairedWithSysCfg:].cold.1
+ +[CRRepairStatus _wasRepairedWithSysCfg:].cold.2
+ +[CRRepairStatus _wasRepairedWithSysCfg:].cold.3
+ +[CRRepairStatus _wasRepairedWithSysCfg:].cold.4
+ +[CRRepairStatus getVeridianFWVersionInfo]
+ +[CRRepairStatus getVeridianFWVersionInfo].cold.1
+ +[CRRepairStatus isCoverGlassRepaired]
+ +[CRRepairStatus isDeviceStagedSealed]
+ +[CRRepairStatus isServicePartWithError:]
+ +[CRRepairStatus isVeridianFWUpdateRequiredLite]
+ +[CRRepairStatus isVeridianFWUpdateRequired]
+ +[CRRepairStatus isVolumeButtonRepaired]
+ +[CRURLSessionDelegate trustIsValidWithProtectionSpace:]
+ +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.1
+ +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.2
+ +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.3
+ +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.4
+ +[MRDataCollectionNotice didShowDataCollectionNoticeForComponent:]
+ +[MRDataCollectionNotice shouldShowDataCollectionNoticeForComponent:]
+ -[CRPluginsController isApplicationInstalledWithMaxRetries:bundleName:]
+ -[CRPluginsController isApplicationInstalledWithMaxRetries:bundleName:].cold.1
+ -[CRPluginsController rebuildApplicationDataBase]
+ -[CRPluginsController rebuildApplicationDataBase].cold.1
+ -[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]
+ -[CRURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:]
+ -[CRURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:].cold.1
+ -[MRLocalization localizedStringWithKey:defaultString:]
+ <redacted>
+ GCC_except_table0
+ _OBJC_METACLASS_$_CRPluginsController
+ _OBJC_METACLASS_$_CRRepairStatus
+ _OBJC_METACLASS_$_CRSystemHealthStatus
+ _OBJC_METACLASS_$_CRURLSessionDelegate
+ _OBJC_METACLASS_$_MRDataCollectionNotice
+ _OBJC_METACLASS_$_MRLocalization
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_METHODS_CRRepairStatus
+ __OBJC_$_CLASS_METHODS_CRURLSessionDelegate
+ __OBJC_$_CLASS_METHODS_MRDataCollectionNotice
+ __OBJC_$_INSTANCE_METHODS_CRPluginsController
+ __OBJC_$_INSTANCE_METHODS_CRSystemHealthStatus
+ __OBJC_$_INSTANCE_METHODS_CRURLSessionDelegate
+ __OBJC_$_INSTANCE_METHODS_MRLocalization
+ __OBJC_$_PROP_LIST_CRURLSessionDelegate
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSystemHealthProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSystemHealthProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CRURLSessionDelegate
+ __OBJC_CLASS_RO_$_CRPluginsController
+ __OBJC_CLASS_RO_$_CRRepairStatus
+ __OBJC_CLASS_RO_$_CRSystemHealthStatus
+ __OBJC_CLASS_RO_$_CRURLSessionDelegate
+ __OBJC_CLASS_RO_$_MRDataCollectionNotice
+ __OBJC_CLASS_RO_$_MRLocalization
+ __OBJC_LABEL_PROTOCOL_$_CRSystemHealthProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_METACLASS_RO_$_CRPluginsController
+ __OBJC_METACLASS_RO_$_CRRepairStatus
+ __OBJC_METACLASS_RO_$_CRSystemHealthStatus
+ __OBJC_METACLASS_RO_$_CRURLSessionDelegate
+ __OBJC_METACLASS_RO_$_MRDataCollectionNotice
+ __OBJC_METACLASS_RO_$_MRLocalization
+ __OBJC_PROTOCOL_$_CRSystemHealthProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_CRSystemHealthProtocol
+ ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke
+ ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke.11
+ ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8r48l8r56l8
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$SHA256DigestString
+ _objc_msgSend$_LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:
+ _objc_msgSend$applicationIsInstalled:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$credentialForTrust:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$getCurrentSystemHealthStatusForComponentsInternal:WithReply:
+ _objc_msgSend$host
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isDcSignedComponent:error:
+ _objc_msgSend$isDeviceStagedSealed
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isServicePartWithError:
+ _objc_msgSend$isVeridianFWUpdateRequired
+ _objc_msgSend$isVeridianFWUpdateRequiredLite
+ _objc_msgSend$length
+ _objc_msgSend$localizations
+ _objc_msgSend$localizedStringForKey:value:table:localization:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$protectionSpace
+ _objc_msgSend$resume
+ _objc_msgSend$serverTrust
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$synchronize
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$trustIsValidWithProtectionSpace:
- _CFDictionaryCreate
- _CFDictionaryGetValue
- _CFDictionarySetValue
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- _IOServiceMatching
- _MGGetProductType
- _OBJC_CLASS_$_CRFDRBaseDeviceHandler
- _getDeviceChemID
- _hasHadBatteryRepair
- _hasHadBatteryRepairUsingCBCC
- _kCFAllocatorDefault
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _kIOMainPortDefault
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "deviceHasReducedBootPolicyWithReply:"
+ "getCurrentSystemHealthStatusForComponentsInternal Error:%@"
+ "isBatteryInServiceState:"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
- "%@ not found in battery data; looking for %@"
- "0"
- "0100000075100000CDFFFFFFDCFFFFFFA0100000D6FFFFFFE0FFFFFF"
- "01000000DB000000B1FFFFFFCEFFFFFF91000000CBFFFFFFE6FFFFFF"
- "AlgoChemID"
- "AppleSPUHIDInterface"
- "BatteryData"
- "CBCC attribute is %@"
- "Cannot find entry %@ in battery data"
- "Cannot find matching service to %s"
- "Cannot find matching service to %s with name:compass"
- "Cannot find property \"compass-battery-compensation\" in compass node"
- "Cannot find property entry to %@"
- "ChemID"
- "CmCl"
- "Component %llu in MRComponentType enum is not supported for authorized repair for this device"
- "Error:%@"
- "Found %@; returning chemID with value %@"
- "IOPMPowerSource"
- "IOPropertyMatch"
- "Localizable-J481"
- "NBCl"
- "Product type %lx is not the expected product type %x"
- "SrvP"
- "_wasRepaired"
- "_wasRepairedWithCombinedDataClass:"
- "_wasRepairedWithDataClass:"
- "bCfg"
- "bcrt"
- "compass"
- "compass-battery-compensation"
- "convertToHexString"
- "getLocalSealingManifest"
- "getSsrBootIntentWithError:"
- "hasHadAuthorizedRepair"
- "hasHadAuthorizedRepairForComponent:"
- "hop0"
- "intValue"
- "isDcSignedCombinedDataClass:error:"
- "isDcSignedDataClass:instance:error:"
- "isDcSignedSealingManifest:"
- "isFDRDataClassSupported:"
- "name"
- "prpc"
- "psd2"
- "tcrt"
- "vcrt"

```

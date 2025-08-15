## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-4146.5.13.0.0
-  __TEXT.__text: 0x4b178
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x3350
+4146.6.10.0.0
+  __TEXT.__text: 0x4c398
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x33f8
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x4e56
-  __TEXT.__gcc_except_tab: 0x7fc
-  __TEXT.__oslogstring: 0x58d4
+  __TEXT.__gcc_except_tab: 0x81c
+  __TEXT.__cstring: 0x4f26
+  __TEXT.__oslogstring: 0x5955
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x10f8
-  __TEXT.__objc_classname: 0xfc1
-  __TEXT.__objc_methname: 0xcfde
-  __TEXT.__objc_methtype: 0x2190
-  __TEXT.__objc_stubs: 0x7fc0
+  __TEXT.__unwind_info: 0x1140
+  __TEXT.__objc_classname: 0xfe9
+  __TEXT.__objc_methname: 0xd4aa
+  __TEXT.__objc_methtype: 0x224d
+  __TEXT.__objc_stubs: 0x82c0
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1768
-  __DATA_CONST.__objc_classlist: 0x270
-  __DATA_CONST.__objc_catlist: 0x58
+  __DATA_CONST.__const: 0x17e8
+  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5940
-  __DATA_CONST.__objc_selrefs: 0x29a0
+  __DATA_CONST.__objc_const: 0x5a90
+  __DATA_CONST.__objc_selrefs: 0x2a80
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x690
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_classrefs: 0x6a8
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x238
-  __AUTH_CONST.__cfstring: 0x2d20
-  __AUTH_CONST.__objc_const: 0x2048
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__objc_const: 0x20d0
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x590
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x2fc
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x30c
   __DATA.__data: 0xfc0
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E972DA15-3E65-3498-8B0A-4F23A32EA52B
-  Functions: 1604
-  Symbols:   5894
-  CStrings:  3149
+  UUID: 4DA0284A-A0F4-3618-B4D2-B36827ABEE31
+  Functions: 1627
+  Symbols:   5987
+  CStrings:  3204
 
Symbols:
+ +[HKMedicationsDeviceInfo(HealthMedicationsDaemonPlugin) deviceInfoFromStorageGroup:syncIdentityManager:]
+ +[HKMedicationsDeviceInfo(HealthMedicationsDaemonPlugin) localDeviceInfo]
+ -[HDHealthMedicationsProfileExtension deviceScopedStorageManager]
+ -[HDMedicationControlTaskServer remote_accountDevicesInfoTriggeringUpdate:completion:]
+ -[HDMedicationControlTaskServer remote_updateLocalDeviceValuesNowWithCompletion:]
+ -[HDMedicationsDeviceScopedStorageManager .cxx_destruct]
+ -[HDMedicationsDeviceScopedStorageManager _updateLocalDeviceValuesNowWithError:]
+ -[HDMedicationsDeviceScopedStorageManager accountDevicesInfoTriggeringUpdate:error:]
+ -[HDMedicationsDeviceScopedStorageManager accountDevicesInfoTriggeringUpdate:error:].cold.1
+ -[HDMedicationsDeviceScopedStorageManager initWithProfile:]
+ -[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]
+ -[HDMedicationsDeviceScopedStorageManager setUnitTest_accountDevicesInfo:]
+ -[HDMedicationsDeviceScopedStorageManager unitTest_accountDevicesInfo]
+ -[HDMedicationsDeviceScopedStorageManager updateLocalDeviceValuesNowWithError:]
+ _HDMedicationsDeviceKeyValueStoreDomain
+ _HKNSOperatingSystemVersionFromString
+ _HKNSOperatingSystemVersionString
+ _OBJC_CLASS_$_HDMedicationsDeviceScopedStorageManager
+ _OBJC_CLASS_$_HKMedicationsAccountDevicesInfo
+ _OBJC_CLASS_$_HKMedicationsDeviceInfo
+ _OBJC_IVAR_$_HDHealthMedicationsProfileExtension._deviceScopedStorageManager
+ _OBJC_IVAR_$_HDMedicationsDeviceScopedStorageManager._keyValueStore
+ _OBJC_IVAR_$_HDMedicationsDeviceScopedStorageManager._syncIdentityManager
+ _OBJC_IVAR_$_HDMedicationsDeviceScopedStorageManager._unitTest_accountDevicesInfo
+ _OBJC_METACLASS_$_HDMedicationsDeviceScopedStorageManager
+ __OBJC_$_CATEGORY_HKMedicationsDeviceInfo_$_HealthMedicationsDaemonPlugin
+ __OBJC_$_CLASS_METHODS_HKMedicationsDeviceInfo(HealthMedicationsDaemonPlugin)
+ __OBJC_$_INSTANCE_METHODS_HDMedicationsDeviceScopedStorageManager
+ __OBJC_$_INSTANCE_VARIABLES_HDMedicationsDeviceScopedStorageManager
+ __OBJC_$_PROP_LIST_HDMedicationsDeviceScopedStorageManager
+ __OBJC_CLASS_PROTOCOLS_$_HDMedicationsDeviceScopedStorageManager
+ __OBJC_CLASS_RO_$_HDMedicationsDeviceScopedStorageManager
+ __OBJC_METACLASS_RO_$_HDMedicationsDeviceScopedStorageManager
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.260
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.cold.1
+ ___80-[HDMedicationsDeviceScopedStorageManager _updateLocalDeviceValuesNowWithError:]_block_invoke
+ ___84-[HDMedicationsDeviceScopedStorageManager accountDevicesInfoTriggeringUpdate:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e63_"HKMedicationsDeviceInfo"16?0"HDDeviceKeyValueStorageGroup"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e14_v16?0?<v?>8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e25_v32?0"NSString"816^B24lr40l8s32l8r48l8
+ _objc_msgSend$_initLocalDeviceWithName:model:operatingSystemVersion:scheduleCompatibilityVersion:
+ _objc_msgSend$accountDevicesInfoTriggeringUpdate:error:
+ _objc_msgSend$currentDeviceDisplayName
+ _objc_msgSend$currentDeviceProductType
+ _objc_msgSend$currentOSVersionStruct
+ _objc_msgSend$deviceContext
+ _objc_msgSend$deviceInfoFromStorageGroup:syncIdentityManager:
+ _objc_msgSend$deviceKeyValueStoreManager
+ _objc_msgSend$deviceScopedStorageManager
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$fetchEntriesForDomain:key:protectionCategory:error:
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$initWithHardwareIdentifier:name:model:operatingSystemVersion:scheduleCompatibilityVersion:localDevice:
+ _objc_msgSend$initWithMedicationFeatureDevicesInfo:localDeviceInfo:
+ _objc_msgSend$localDeviceInfo
+ _objc_msgSend$model
+ _objc_msgSend$numberValue:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$scheduleCompatibilityVersion
+ _objc_msgSend$setNumber:forKey:domainName:protectionCategory:error:
+ _objc_msgSend$setString:forKey:domainName:protectionCategory:error:
+ _objc_msgSend$storageEntries
+ _objc_msgSend$stringValue:
+ _objc_msgSend$updateLocalDeviceValuesNowWithError:
CStrings:
+ "\x01\x17"
+ "@\"HDDeviceKeyValueStoreManager\""
+ "@\"HDMedicationsDeviceScopedStorageManager\""
+ "@\"HKMedicationsAccountDevicesInfo\""
+ "@\"HKMedicationsDeviceInfo\"16@?0@\"HDDeviceKeyValueStorageGroup\"8"
+ "@28@0:8B16^@20"
+ "HDMedicationsDeviceScopedStorageManager"
+ "HDMedicationsDeviceScopedStorageManger"
+ "T@\"HDMedicationsDeviceScopedStorageManager\",R,N,V_deviceScopedStorageManager"
+ "T@\"HKMedicationsAccountDevicesInfo\",C,N,V_unitTest_accountDevicesInfo"
+ "[%{public}@]: Error updating local device values: %{public}@"
+ "[%{public}@]: Finished local device update as maintenance operation"
+ "_Model"
+ "_Name"
+ "_OperatingSystemVersion"
+ "_ScheduleCompatibilityVersion"
+ "_deviceScopedStorageManager"
+ "_initLocalDeviceWithName:model:operatingSystemVersion:scheduleCompatibilityVersion:"
+ "_keyValueStore"
+ "_unitTest_accountDevicesInfo"
+ "accountDevicesInfoTriggeringUpdate:error:"
+ "currentDeviceDisplayName"
+ "currentDeviceProductType"
+ "currentOSVersionStruct"
+ "deviceContext"
+ "deviceInfoFromStorageGroup:syncIdentityManager:"
+ "deviceKeyValueStoreManager"
+ "deviceScopedStorageManager"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "fetchEntriesForDomain:key:protectionCategory:error:"
+ "hardwareIdentifier"
+ "initWithHardwareIdentifier:name:model:operatingSystemVersion:scheduleCompatibilityVersion:localDevice:"
+ "initWithMedicationFeatureDevicesInfo:localDeviceInfo:"
+ "localDeviceInfo"
+ "model"
+ "numberValue:"
+ "operatingSystemVersion"
+ "remote_accountDevicesInfoTriggeringUpdate:completion:"
+ "remote_updateLocalDeviceValuesNowWithCompletion:"
+ "scheduleCompatibilityVersion"
+ "setNumber:forKey:domainName:protectionCategory:error:"
+ "setString:forKey:domainName:protectionCategory:error:"
+ "setUnitTest_accountDevicesInfo:"
+ "storageEntries"
+ "stringValue:"
+ "unitTest_accountDevicesInfo"
+ "updateLocalDeviceValuesNowWithError:"
+ "v28@0:8B16@?<v@?@\"HKMedicationsAccountDevicesInfo\"@\"NSError\">20"
+ "v32@?0@\"NSString\"8@16^B24"
- "\x01\x16"

```

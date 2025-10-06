## HealthMedications

> `/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications`

```diff

-4146.5.13.0.0
-  __TEXT.__text: 0x14b94
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x1ba8
+4146.6.10.0.0
+  __TEXT.__text: 0x158b8
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x1d28
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x2843
+  __TEXT.__cstring: 0x296a
   __TEXT.__oslogstring: 0x722
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x718
-  __TEXT.__objc_classname: 0x6e9
-  __TEXT.__objc_methname: 0x58bf
-  __TEXT.__objc_methtype: 0xcaf
-  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__unwind_info: 0x764
+  __TEXT.__objc_classname: 0x721
+  __TEXT.__objc_methname: 0x5caf
+  __TEXT.__objc_methtype: 0xd84
+  __TEXT.__objc_stubs: 0x2de0
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2e98
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_const: 0x30e8
+  __DATA_CONST.__objc_selrefs: 0x11d0
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0x238
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__cfstring: 0x2d60
-  __AUTH_CONST.__objc_const: 0x13f8
+  __DATA_CONST.__objc_classrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x110
+  __AUTH_CONST.__cfstring: 0x2e80
+  __AUTH_CONST.__objc_const: 0x1518
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x258
+  __AUTH_CONST.__auth_got: 0x298
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x278
   __DATA.__data: 0x788
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x870

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48CA8954-C806-3228-B4C2-93C0C572B775
-  Functions: 688
-  Symbols:   2562
-  CStrings:  1762
+  UUID: 60072AC0-9563-3222-801E-55D486FF19D2
+  Functions: 720
+  Symbols:   2661
+  CStrings:  1818
 
Symbols:
+ +[HKMedicationsAccountDevicesInfo supportsSecureCoding]
+ +[HKMedicationsDeviceInfo supportsSecureCoding]
+ -[HKMedicationControl accountDevicesInfoTriggeringUpdate:completion:]
+ -[HKMedicationControl updateLocalDeviceValuesNowWithCompletion:]
+ -[HKMedicationsAccountDevicesInfo .cxx_destruct]
+ -[HKMedicationsAccountDevicesInfo copyWithZone:]
+ -[HKMedicationsAccountDevicesInfo encodeWithCoder:]
+ -[HKMedicationsAccountDevicesInfo hash]
+ -[HKMedicationsAccountDevicesInfo initWithCoder:]
+ -[HKMedicationsAccountDevicesInfo initWithMedicationFeatureDevicesInfo:localDeviceInfo:]
+ -[HKMedicationsAccountDevicesInfo isEqual:]
+ -[HKMedicationsAccountDevicesInfo localDeviceInfo]
+ -[HKMedicationsAccountDevicesInfo medicationFeatureDevicesInfo]
+ -[HKMedicationsDeviceInfo .cxx_destruct]
+ -[HKMedicationsDeviceInfo _initLocalDeviceWithName:model:operatingSystemVersion:scheduleCompatibilityVersion:]
+ -[HKMedicationsDeviceInfo copyWithZone:]
+ -[HKMedicationsDeviceInfo description]
+ -[HKMedicationsDeviceInfo encodeWithCoder:]
+ -[HKMedicationsDeviceInfo hardwareIdentifier]
+ -[HKMedicationsDeviceInfo hash]
+ -[HKMedicationsDeviceInfo initWithCoder:]
+ -[HKMedicationsDeviceInfo initWithHardwareIdentifier:name:model:operatingSystemVersion:scheduleCompatibilityVersion:localDevice:]
+ -[HKMedicationsDeviceInfo isEqual:]
+ -[HKMedicationsDeviceInfo isLocalDevice]
+ -[HKMedicationsDeviceInfo model]
+ -[HKMedicationsDeviceInfo name]
+ -[HKMedicationsDeviceInfo operatingSystemVersion]
+ -[HKMedicationsDeviceInfo scheduleCompatibilityVersion]
+ _HKNSOperatingSystemVersionFromString
+ _HKNSOperatingSystemVersionString
+ _HKNSOperatingSystemVersionsEqual
+ _OBJC_CLASS_$_HKMedicationsAccountDevicesInfo
+ _OBJC_CLASS_$_HKMedicationsDeviceInfo
+ _OBJC_IVAR_$_HKMedicationsAccountDevicesInfo._localDeviceInfo
+ _OBJC_IVAR_$_HKMedicationsAccountDevicesInfo._medicationFeatureDevicesInfo
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._hardwareIdentifier
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._localDevice
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._model
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._name
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._operatingSystemVersion
+ _OBJC_IVAR_$_HKMedicationsDeviceInfo._scheduleCompatibilityVersion
+ _OBJC_METACLASS_$_HKMedicationsAccountDevicesInfo
+ _OBJC_METACLASS_$_HKMedicationsDeviceInfo
+ __OBJC_$_CLASS_METHODS_HKMedicationsAccountDevicesInfo
+ __OBJC_$_CLASS_METHODS_HKMedicationsDeviceInfo
+ __OBJC_$_CLASS_PROP_LIST_HKMedicationsAccountDevicesInfo
+ __OBJC_$_CLASS_PROP_LIST_HKMedicationsDeviceInfo
+ __OBJC_$_INSTANCE_METHODS_HKMedicationsAccountDevicesInfo
+ __OBJC_$_INSTANCE_METHODS_HKMedicationsDeviceInfo
+ __OBJC_$_INSTANCE_VARIABLES_HKMedicationsAccountDevicesInfo
+ __OBJC_$_INSTANCE_VARIABLES_HKMedicationsDeviceInfo
+ __OBJC_$_PROP_LIST_HKMedicationsAccountDevicesInfo
+ __OBJC_$_PROP_LIST_HKMedicationsDeviceInfo
+ __OBJC_CLASS_PROTOCOLS_$_HKMedicationsAccountDevicesInfo
+ __OBJC_CLASS_PROTOCOLS_$_HKMedicationsDeviceInfo
+ __OBJC_CLASS_RO_$_HKMedicationsAccountDevicesInfo
+ __OBJC_CLASS_RO_$_HKMedicationsDeviceInfo
+ __OBJC_METACLASS_RO_$_HKMedicationsAccountDevicesInfo
+ __OBJC_METACLASS_RO_$_HKMedicationsDeviceInfo
+ ___64-[HKMedicationControl updateLocalDeviceValuesNowWithCompletion:]_block_invoke
+ ___64-[HKMedicationControl updateLocalDeviceValuesNowWithCompletion:]_block_invoke_2
+ ___69-[HKMedicationControl accountDevicesInfoTriggeringUpdate:completion:]_block_invoke
+ ___69-[HKMedicationControl accountDevicesInfoTriggeringUpdate:completion:]_block_invoke_2
+ ___block_descriptor_41_e8_32bs_e46_v16?0"<HKMedicationControlServerInterface>"8ls32l8
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$remote_accountDevicesInfoTriggeringUpdate:completion:
+ _objc_msgSend$remote_updateLocalDeviceValuesNowWithCompletion:
CStrings:
+ "<%@ name:%@, model:%@, operating system:%@, compatibility version: %@, localDevice: %@, hardware identifier: %@"
+ "@\"HKMedicationsDeviceInfo\""
+ "@64@0:8@16@24{?=qqq}32q56"
+ "@76@0:8@16@24@32{?=qqq}40q64B72"
+ "HKMedicationsAccountDevicesInfo"
+ "HKMedicationsDeviceInfo"
+ "HKMedicationsDeviceInfo.m"
+ "HardwareIdentifier"
+ "LocalDevice"
+ "MedicationFeatureDevices"
+ "Model"
+ "Operating system version should not be nil"
+ "OperatingSystemVersion"
+ "ScheduleCompatibilityVersion"
+ "T@\"HKMedicationsDeviceInfo\",R,N,V_localDeviceInfo"
+ "T@\"NSArray\",R,N,V_medicationFeatureDevicesInfo"
+ "T@\"NSString\",R,C,N,V_model"
+ "T@\"NSUUID\",R,C,N,V_hardwareIdentifier"
+ "TB,R,N,GisLocalDevice,V_localDevice"
+ "Tq,R,N,V_scheduleCompatibilityVersion"
+ "T{?=qqq},R,N,V_operatingSystemVersion"
+ "_hardwareIdentifier"
+ "_initLocalDeviceWithName:model:operatingSystemVersion:scheduleCompatibilityVersion:"
+ "_localDevice"
+ "_localDeviceInfo"
+ "_medicationFeatureDevicesInfo"
+ "_model"
+ "_operatingSystemVersion"
+ "_scheduleCompatibilityVersion"
+ "accountDevicesInfoTriggeringUpdate:completion:"
+ "hardwareIdentifier"
+ "initWithHardwareIdentifier:name:model:operatingSystemVersion:scheduleCompatibilityVersion:localDevice:"
+ "initWithMedicationFeatureDevicesInfo:localDeviceInfo:"
+ "isEqualToArray:"
+ "isLocalDevice"
+ "localDevice"
+ "localDeviceInfo"
+ "medicationFeatureDevicesInfo"
+ "model"
+ "operatingSystemVersion"
+ "remote_accountDevicesInfoTriggeringUpdate:completion:"
+ "remote_updateLocalDeviceValuesNowWithCompletion:"
+ "scheduleCompatibilityVersion"
+ "updateLocalDeviceValuesNowWithCompletion:"
+ "v28@0:8B16@?<v@?@\"HKMedicationsAccountDevicesInfo\"@\"NSError\">20"
+ "{?=\"majorVersion\"q\"minorVersion\"q\"patchVersion\"q}"
+ "{?=qqq}16@0:8"

```

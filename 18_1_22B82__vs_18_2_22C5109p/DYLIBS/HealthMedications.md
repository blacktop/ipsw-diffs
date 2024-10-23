## HealthMedications

> `/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x1c240
+5200.2.4.1.5
+  __TEXT.__text: 0x1dc80
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x2374
+  __TEXT.__objc_methlist: 0x25b4
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x36c6
+  __TEXT.__cstring: 0x39f2
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__oslogstring: 0x8d8
-  __TEXT.__unwind_info: 0x968
-  __TEXT.__objc_classname: 0x89b
-  __TEXT.__objc_methname: 0x6e34
-  __TEXT.__objc_methtype: 0x1005
-  __TEXT.__objc_stubs: 0x3520
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0xe30
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0xa08
+  __TEXT.__objc_classname: 0x8eb
+  __TEXT.__objc_methname: 0x724c
+  __TEXT.__objc_methtype: 0x101c
+  __TEXT.__objc_stubs: 0x3680
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1470
+  __DATA_CONST.__objc_selrefs: 0x1520
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x3840
-  __AUTH_CONST.__objc_const: 0x51e0
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__objc_const: 0x5590
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x2d8
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x848
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x870

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 896
-  Symbols:   1225
-  CStrings:  1693
+  Functions: 954
+  Symbols:   1289
+  CStrings:  1747
 
Symbols:
+ _NRDevicePropertyMedicationScheduleCompatibilityVersion
+ _OBJC_CLASS_$_HKDismissedRemoteScheduleUnavailableRecord
+ _OBJC_CLASS_$_HKRemoteScheduleUnavailableRecord
+ _OBJC_METACLASS_$_HKDismissedRemoteScheduleUnavailableRecord
+ _OBJC_METACLASS_$_HKRemoteScheduleUnavailableRecord
+ __HKDismissedRemoteScheduleUnavailableRecordDeviceSeparator
CStrings:
+ "\x01\""
+ "<%!@(MISSING):%!p(MISSING) (Concept ID: %!l(MISSING)d, Schedule Type: %!@(MISSING), Schedule Compatibility Version: v%!l(MISSING)d, Devices: %!@(MISSING))>"
+ "<%!@(MISSING):%!p(MISSING) (Medication: %!l(MISSING)d, Schedule Type: %!@(MISSING), Schedule Compatibility Version: v%!l(MISSING)d, Creation Date: %!@(MISSING), Devices: %!@(MISSING))>"
+ "@16@?0@\"HKMedicationsDeviceInfo\"8"
+ "@16@?0@\"NSUUID\"8"
+ "@56@0:8@16q24q32@40@48"
+ "Device identifiers should not be nil"
+ "DeviceIdentifiers"
+ "Devices"
+ "Devices should not be nil"
+ "HKDismissedRemoteScheduleUnavailableRecord"
+ "HKDismissedRemoteScheduleUnavailableRecord.m"
+ "HKRemoteScheduleUnavailableRecord"
+ "HKRemoteScheduleUnavailableRecord.m"
+ "Schedule should not be nil"
+ "ScheduleType"
+ "T@\"NSArray\",C,N,V_devices"
+ "T@\"NSArray\",R,C,N,V_deviceIdentifiers"
+ "T@\"NSArray\",R,C,N,V_medicationFeatureDevicesInfo"
+ "T@\"NSDate\",R,C,N,V_creationDate"
+ "_deviceIdentifiers"
+ "_devices"
+ "_devicesByIdentifier"
+ "_initWithMedicationIdentifier:scheduleType:scheduleCompatibilityVersion:deviceIdentifiers:creationDate:"
+ "_unitTest_newAccountInfoWithAddedDevice:"
+ "allDismissedRemoteScheduleUnavailableRecordsWithCompletion:"
+ "arrayByAddingObject:"
+ "deleteDismissedRemoteScheduleUnavailableForMedication:completion:"
+ "deviceForIdentifier:"
+ "deviceIdentifiers"
+ "deviceIdentifiers != nil"
+ "deviceIdentifiersDatabaseString"
+ "deviceIdentifiersDescriptionString"
+ "devices != nil"
+ "dismissedRecord"
+ "initWithLocalPairedDevice:"
+ "initWithMedication:schedule:devices:"
+ "isCompatibleWithScheduleCompatibilityVersion:"
+ "isEqualToDate:"
+ "localizedCaseInsensitiveCompare:"
+ "markRemoteScheduleUnavailableRecordsAsDismissed:completion:"
+ "medicationIdentifier != nil"
+ "remoteDeviceIdentifiers"
+ "remoteRecords != nil"
+ "remoteRecords.count > 0"
+ "remote_allDismissedRemoteScheduleUnavailableRecordsWithCompletion:"
+ "remote_deleteDismissedRemoteScheduleUnavailableForMedication:completion:"
+ "remote_markRemoteScheduleUnavailableRecordsAsDismissed:completion:"
+ "schedule != nil"
+ "scheduleCompatibilityVersion >= HKMedicationScheduleCompatibilityUnsupported"
+ "scheduleType <= upperScheduleTypeBound"
+ "scheduleType >= lowerScheduleTypeBound"
+ "setDevices:"
+ "sortedArrayUsingSelector:"
+ "v24@?0@\"HKMedicationsDeviceInfo\"8@?<v@?@\"NSUUID\"@\"HKMedicationsDeviceInfo\">16"
+ "|$|"
- "T@\"NSArray\",R,N,V_medicationFeatureDevicesInfo"
- "hardwareIdentifier != nil"

```

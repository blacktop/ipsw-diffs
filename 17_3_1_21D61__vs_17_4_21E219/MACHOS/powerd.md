## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1630.60.6.0.0
-  __TEXT.__text: 0x5e28c
-  __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_stubs: 0x40c0
-  __TEXT.__objc_methlist: 0x1af8
+1630.100.21.0.0
+  __TEXT.__text: 0x5f694
+  __TEXT.__auth_stubs: 0x1a80
+  __TEXT.__objc_stubs: 0x42a0
+  __TEXT.__objc_methlist: 0x1b28
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x5b0f
-  __TEXT.__objc_methname: 0x473b
-  __TEXT.__oslogstring: 0x9d7c
-  __TEXT.__objc_classname: 0x2bf
-  __TEXT.__objc_methtype: 0x736
+  __TEXT.__cstring: 0x5be0
+  __TEXT.__objc_methname: 0x4894
+  __TEXT.__oslogstring: 0xa0a1
+  __TEXT.__objc_classname: 0x2c8
+  __TEXT.__objc_methtype: 0x768
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__dlopen_cstrs: 0x256
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x1070
-  __DATA_CONST.__auth_got: 0xd18
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0xd50
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x22e0
-  __DATA_CONST.__cfstring: 0x6240
+  __DATA_CONST.__const: 0x2320
+  __DATA_CONST.__cfstring: 0x6360
   __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__objc_dictobj: 0x140
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_intobj: 0x2d0
+  __DATA_CONST.__objc_arraydata: 0x200
+  __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x2b8
-  __DATA.__objc_const: 0x3e90
-  __DATA.__objc_selrefs: 0x1218
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x188
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_const: 0x3f20
+  __DATA.__objc_selrefs: 0x12a0
+  __DATA.__objc_ivar: 0x290
   __DATA.__objc_data: 0x550
-  __DATA.__data: 0x95c
+  __DATA.__data: 0x9bc
   __DATA.__common: 0x1120
-  __DATA.__bss: 0xa78
+  __DATA.__bss: 0xa98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2076
-  Symbols:   524
-  CStrings:  3040
+  Functions: 2097
+  Symbols:   541
+  CStrings:  3093
 
Symbols:
+ _IOPSGetYearAndWeekOfManufactureFromBatterySerial
+ _MAEGetActivationStateWithError
+ _MGCopyAnswer
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSUUID
+ _TMGetReferenceTime
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_INTERVAL_1_HOUR
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_UTILITY
+ _XPC_ACTIVITY_REQUIRES_BUDDY_COMPLETE
+ _kMAActivationStateActivated
+ _strtoul
+ _xpc_activity_register
+ _xpc_activity_unregister
CStrings:
+ "2"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "@\"NSUUID\""
+ "@24@0:8@\"NSCoder\"16"
+ "CoreSmartPowerNap: PL Log CSPN End %@"
+ "CoreSmartPowerNap: PL Log CSPN Start %@"
+ "Current boot session UUID: %@"
+ "DOFU-monitor triggered\n"
+ "DOFU-monitor: No reliable time\n"
+ "DOFU-monitor: time:%f uncertainty:%f reliability:%d ret:%u\n"
+ "DeviceSupportsBatteryInformation"
+ "Failed to get activation state: %@\n."
+ "Failed to read bootsessionuuid (%u)\n"
+ "Failed to retrieve gestalt key '%@'."
+ "Failed to set battery DOFU: %@\n"
+ "Fetched yww from IOKit: %@"
+ "Invalid auth condition: recoveredflags:0x%x"
+ "Invalid auth flags detected: authOk:%d flags:0x%x"
+ "NSCoding"
+ "No policy found for token %@ from %u\n"
+ "Restoring state from disk:%@\n"
+ "Setting DOFU requires an activated device: %@.\n"
+ "Skipping battery health loop due to missing auth [0x%x]"
+ "SmartPowerNap session did not engage because inactivity was shorter than delta-to-query"
+ "SmartPowerNap: Initialized predictor. Evaluate SPN %llu"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",R,V_token"
+ "UUID"
+ "UUIDString"
+ "Unable to get year and week from IOPSGetYearAndWeekOfManufactureFromBatterySerial"
+ "_token"
+ "archivedDataWithRootObject:"
+ "bootSessionUUID"
+ "cancelModelQuery"
+ "caseInsensitiveCompare:"
+ "com.apple.powerd.charging"
+ "com.apple.powerd.dofu-monitor"
+ "decodeBoolForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectForKey:"
+ "dossier"
+ "encodeBool:forKey:"
+ "encodeInt64:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "initWithCoder:"
+ "initWithUUIDString:"
+ "kern.bootsessionuuid"
+ "numberWithLongLong:"
+ "policies"
+ "processAssertionActivityUpdateResp: Reply type isn't XPC_TYPE_DICTIONARY from pid: %d\n"
+ "processAssertionActivityUpdateResp: Unexpected response from pid %d. token: %u expected: %u\n"
+ "sendAssertionActivityUpdateMsg: Sending token: %u to pid: %d\n"
+ "setWeekOfYear:"
+ "setWeekday:"
+ "setYear:"
+ "soclimit"
+ "stringWithUTF8String:"
+ "token"
+ "unarchiveObjectWithData:"
+ "v24@0:8@\"NSCoder\"16"
- "%02ld"
- "%ld"
- "1"
- "CoreSmartPowerNap: PL Log %@"
- "Extracted DOM %@; converted to %@"
- "No policy found for token %llu from %u\n"
- "Reply from pid:%d not considered pending. Reply likely from a previous request.\n"
- "Skipping PL Logging, CSPN doesn't support PL yet."
- "SmartPowerNap session did not engage because inactivity was shorter than delta-to- query"
- "calendarWithIdentifier:"
- "substringFromIndex:"
- "weekOfYear"
- "yearForWeekOfYear"

```

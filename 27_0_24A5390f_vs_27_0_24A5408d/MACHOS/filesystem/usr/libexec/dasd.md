## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-2467.0.23.502.1
-  __TEXT.__text: 0x175bc4
-  __TEXT.__auth_stubs: 0x2210
-  __TEXT.__objc_stubs: 0x1ade0
-  __TEXT.__objc_methlist: 0x13024
+2467.2.1.0.0
+  __TEXT.__text: 0x1779b8
+  __TEXT.__auth_stubs: 0x2230
+  __TEXT.__objc_stubs: 0x1af80
+  __TEXT.__objc_methlist: 0x131b4
   __TEXT.__const: 0x1568
-  __TEXT.__objc_methname: 0x2e0ad
-  __TEXT.__cstring: 0x103d6
-  __TEXT.__oslogstring: 0x16949
-  __TEXT.__objc_classname: 0x1c88
-  __TEXT.__objc_methtype: 0x41a1
-  __TEXT.__gcc_except_tab: 0x4ecc
+  __TEXT.__objc_methname: 0x2e49d
+  __TEXT.__cstring: 0x10566
+  __TEXT.__oslogstring: 0x16be9
+  __TEXT.__objc_classname: 0x1ca8
+  __TEXT.__objc_methtype: 0x41c1
+  __TEXT.__gcc_except_tab: 0x4f78
   __TEXT.__dlopen_cstrs: 0x552
   __TEXT.__swift5_typeref: 0x966
   __TEXT.__swift5_capture: 0x220

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4ff0
+  __TEXT.__unwind_info: 0x5050
   __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__const: 0x4ed8
-  __DATA_CONST.__cfstring: 0x11740
-  __DATA_CONST.__objc_classlist: 0x700
+  __DATA_CONST.__const: 0x4f00
+  __DATA_CONST.__cfstring: 0x118e0
+  __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x5c0
   __DATA_CONST.__objc_intobj: 0x17b8
-  __DATA_CONST.__objc_arraydata: 0x480
+  __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA_CONST.__objc_dictobj: 0x230
+  __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA_CONST.__auth_got: 0x1118
-  __DATA_CONST.__got: 0xe20
+  __DATA_CONST.__auth_got: 0x1128
+  __DATA_CONST.__got: 0xe38
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x33c08
-  __DATA.__objc_selrefs: 0x9c28
-  __DATA.__objc_ivar: 0x1608
-  __DATA.__objc_data: 0x48b8
+  __DATA.__objc_const: 0x33ed8
+  __DATA.__objc_selrefs: 0x9cc0
+  __DATA.__objc_ivar: 0x1630
+  __DATA.__objc_data: 0x4908
   __DATA.__data: 0x2190
-  __DATA.__bss: 0x1240
+  __DATA.__bss: 0x1250
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8302
-  Symbols:   1010
-  CStrings:  12387
+  Functions: 8343
+  Symbols:   1014
+  CStrings:  12437
 
Symbols:
+ _BMDeviceKeybagLockedIdentifier
+ _IOObjectRelease
+ _NSFileHandleOperationException
+ _objc_exception_rethrow
CStrings:
+ "%@::DeviceNotIdle"
+ "%@::UserAbsentWithDisplay"
+ "/device/keybagLocked"
+ "@\"_CDContextualChangeRegistration\""
+ "Device Active"
+ "Getting distinct PPSTimeSeries for subsystem: %@ category: %@ with valueFilter: %@ & metrics: %@ & timeFilter:%@"
+ "RequiredMinimumBatteryLevel"
+ "T@\"MLModel\",&,V_model"
+ "T@\"_CDContextualChangeRegistration\",&,N,V_batteryStatusRegistration"
+ "T@\"_CDContextualChangeRegistration\",&,N,V_pluginRegistration"
+ "T@\"_DASDataProtectionStateMonitor\",&,N,V_dataProtectionMonitor"
+ "TB,N,V_prohibitTasksOnTLC"
+ "TB,V_hitTLCDuringCurrentSession"
+ "TLC hit during current plugged-in session"
+ "Trigger: %{public}@ is now [%@]"
+ "Unable to create stream for %@: %@"
+ "_DASChargingSessionMonitor"
+ "_batteryStatusRegistration"
+ "_hitTLCDuringCurrentSession"
+ "_pluginRegistration"
+ "_prohibitTasksOnTLC"
+ "auxiliaryType"
+ "batteryLevel == %@ AND temperature == %@"
+ "batteryStatusRegistration"
+ "chargingSessionMonitor"
+ "com.apple.das.chargingSession.batteryStatus"
+ "com.apple.das.chargingSession.plugin"
+ "com.apple.dasd.chargingSessionMonitorQueue"
+ "com.apple.duetactivityscheduler.chargingSession"
+ "convertKeybagLockedStream:toKnowledgeStoreStream:"
+ "deviceWarm == %@"
+ "getDistinctPPSTimeSeries: metrics must be non-empty for %@/%@"
+ "getDistinctPPSTimeSeries:category:valueFilter:metrics:timeFilter:filepath:error:"
+ "handleBatteryStatusChange"
+ "handlePluginStatusChange"
+ "hitTLCDuringCurrentSession"
+ "initWithMetrics:predicate:timeFilter:limitCount:offsetCount:readDirection:returnsDistinctEntities:"
+ "isPrioritizedIdleStackTask"
+ "markTLCHit"
+ "performWriteExperiments:atFileName:withTask:"
+ "pluginRegistration"
+ "prohibitTasksOnTLC"
+ "prohibitTasksOnTLC is %{BOOL}u"
+ "refreshStaleStringInterning: %lu active StringIDs from %lu successful queries (%lu failed)"
+ "refreshStaleStringInterning: all stale StringIDs confirmed active, skipping remaining categories"
+ "refreshStaleStringInterning: error querying array columns for %{public}@: %{public}@"
+ "refreshStaleStringInterning: error querying scalar columns for %{public}@: %{public}@"
+ "refreshStaleTaskMetadata: %{public}@ returned %lu events, %lu TaskIDs still pending"
+ "refreshStaleTaskMetadata: all stale TaskIDs confirmed active, skipping remaining categories"
+ "registerForContextChanges"
+ "setBatteryStatusRegistration:"
+ "setDataProtectionMonitor:"
+ "setHitTLCDuringCurrentSession:"
+ "setPluginRegistration:"
+ "setProhibitTasksOnTLC:"
+ "unfailActivityForIdentifier:"
+ "writeExperiments: file I/O aborted (%{public}@: %{public}@); dropping partial write"
- "T@\"MLModel\",&,N,V_model"
- "Trigger: %@ is now [%@]"
- "Unable create stream for %@: %@"
- "isPrioritizedIdleStackTasks"
- "refreshStaleStringInterning: %lu active StringIDs from %lu categories (%lu failed)"
- "refreshStaleStringInterning: error querying %{public}@: %{public}@"
- "refreshStaleTaskMetadata: %{public}@ returned %lu events"
```

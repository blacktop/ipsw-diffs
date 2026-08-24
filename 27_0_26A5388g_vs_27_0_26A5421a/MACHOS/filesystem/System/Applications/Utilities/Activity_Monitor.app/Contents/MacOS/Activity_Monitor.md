## Activity Monitor

> `/System/Applications/Utilities/Activity Monitor.app/Contents/MacOS/Activity Monitor`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_ivar`

```diff

-1139.0.0.0.0
-  __TEXT.__text: 0x44f78
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_stubs: 0xc580
-  __TEXT.__objc_methlist: 0x6230
-  __TEXT.__const: 0x1f8
-  __TEXT.__gcc_except_tab: 0xca0
-  __TEXT.__objc_methname: 0x1252c
-  __TEXT.__cstring: 0x34dc
-  __TEXT.__objc_classname: 0x68e
-  __TEXT.__objc_methtype: 0x3010
-  __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x10f0
-  __DATA_CONST.__const: 0x1440
-  __DATA_CONST.__cfstring: 0x4a40
-  __DATA_CONST.__objc_classlist: 0x208
+1140.0.0.0.0
+  __TEXT.__text: 0x4580c
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_stubs: 0xca60
+  __TEXT.__objc_methlist: 0x6308
+  __TEXT.__const: 0x248
+  __TEXT.__gcc_except_tab: 0xc90
+  __TEXT.__objc_methname: 0x1296f
+  __TEXT.__cstring: 0x356f
+  __TEXT.__objc_classname: 0x6dc
+  __TEXT.__objc_methtype: 0x309f
+  __TEXT.__ustring: 0x3a8
+  __TEXT.__unwind_info: 0x1118
+  __DATA_CONST.__const: 0x1430
+  __DATA_CONST.__cfstring: 0x4be0
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150

   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x748
-  __DATA_CONST.__got: 0x4e0
-  __DATA.__objc_const: 0xb1d8
-  __DATA.__objc_selrefs: 0x4550
+  __DATA_CONST.__auth_got: 0x700
+  __DATA_CONST.__got: 0x528
+  __DATA.__objc_const: 0xb380
+  __DATA.__objc_selrefs: 0x46b0
   __DATA.__objc_ivar: 0xad8
-  __DATA.__objc_data: 0x1450
-  __DATA.__data: 0x790
-  __DATA.__bss: 0x1a0
+  __DATA.__objc_data: 0x14f0
+  __DATA.__data: 0x7f0
+  __DATA.__bss: 0x1b0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa

   - /usr/lib/libquit.dylib
   - /usr/lib/libsysmon.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 1992
+  Functions: 2004
   Symbols:   413
-  CStrings:  4477
+  CStrings:  4539
 
Symbols:
+ _OBJC_CLASS_$_NSMeasurement
+ _OBJC_CLASS_$_NSMeasurementFormatter
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUnitInformationStorage
+ _OBJC_CLASS_$_NWStatsManager
+ _OBJC_CLASS_$_NWStatsProtocolSnapshot
+ ___error
+ _if_indextoname
+ _kNWStatsParameterReportOpen
+ _kNWStatsSelectInterfaceCellular
+ _kNWStatsSelectInterfaceCompanionLinkBluetooth
+ _kNWStatsSelectInterfaceWiFi
+ _kNWStatsSelectInterfaceWired
+ _snprintf
- _CFRetain
- _NStatManagerAddAllTCP
- _NStatManagerAddAllUDP
- _NStatManagerCreate
- _NStatManagerDestroy
- _NStatManagerQueryAllSourcesUpdate
- _NStatSourceCopyCounts
- _NStatSourceCopyProperties
- _NStatSourceSetDescriptionBlock
- _NStatSourceSetRemovedBlock
- _kNStatSrcKeyInterface
- _kNStatSrcKeyPID
- _remote_device_copy_property
- _remote_device_copy_unique_of_type
CStrings:
+ "## Unhandled hw.perflevel#.name: %s."
+ "### Error getting %s: errno = %d. Falling back to empty string."
+ "### Error getting hw.nperflevels: %i"
+ "### NWStatsManager configure: failed with %d"
+ "### Skip updating app memory size due to corrupted sysmon report."
+ "### System uptime decreased. This should never happen!!"
+ "%@/s"
+ "@\"NSMeasurementFormatter\""
+ "@\"NWStatsManager\""
+ "@\"SMNetworkSpeedFormatter\""
+ "Could not get IODeviceTree for cpus service: %i."
+ "LOC %s"
+ "NWStatsManagerDelegate"
+ "SMNetworkSpeedFormatter"
+ "SMNetworkSpeedValueTransformer"
+ "T@\"NSArray\",&,N,V_orderedCoreTypeNames"
+ "T@\"NSMeasurementFormatter\",&,N,V_fileSizeInBitsFormatter"
+ "T@\"NSMutableDictionary\",&,V_cumulativeStats"
+ "T@\"NWStatsManager\",&,V_statsManager"
+ "T@\"SMNetworkSpeedFormatter\",R,V_networkSpeedFormatter"
+ "[System Disk] data read counter reset: %llu → %llu"
+ "[System Disk] data written counter reset: %llu → %llu"
+ "[System Disk] read ops counter reset: %llu → %llu"
+ "[System Disk] write ops counter reset: %llu → %llu"
+ "[System Network] data received counter reset: %llu → %llu"
+ "[System Network] data sent counter reset: %llu → %llu"
+ "[System Network] packets-in counter reset: %llu → %llu"
+ "[System Network] packets-out counter reset: %llu → %llu"
+ "[System Uptime] %g → %g "
+ "_accumulateProtocolSnapshot:"
+ "_cumulativeStats"
+ "_fileSizeInBitsFormatter"
+ "_leadingEdgeForView:"
+ "_networkSpeedFormatter"
+ "_orderedCoreTypeNames"
+ "_resolvedParentPIDForProcess:proposedPID:"
+ "_statsManager"
+ "bits"
+ "configure:"
+ "cumulativeStats"
+ "deltaAccountingRxAlternateBytes"
+ "deltaAccountingRxCellularBytes"
+ "deltaAccountingRxCompanionLinkBluetoothBytes"
+ "deltaAccountingRxWiFiBytes"
+ "deltaAccountingRxWiredBytes"
+ "deltaAccountingTxAlternateBytes"
+ "deltaAccountingTxCellularBytes"
+ "deltaAccountingTxCompanionLinkBluetoothBytes"
+ "deltaAccountingTxWiFiBytes"
+ "deltaAccountingTxWiredBytes"
+ "deltaRxPackets"
+ "deltaTxPackets"
+ "epid"
+ "exabits"
+ "fileSizeInBitsFormatter"
+ "gigabits"
+ "hw.nperflevels"
+ "hw.perflevel%u.name"
+ "initWithDoubleValue:unit:"
+ "initWithQueue:"
+ "kilobits"
+ "measurementByConvertingToUnit:"
+ "megabits"
+ "networkSpeedFormatter"
+ "orderedCoreTypeNames"
+ "petabits"
+ "processID"
+ "pruneStaleProcessMetricsForGPUMetric:liveProcesses:"
+ "refreshUsingBlock:completionBlock:"
+ "removeStatsForPIDs:"
+ "setCumulativeStats:"
+ "setFileSizeInBitsFormatter:"
+ "setNumberFormatter:"
+ "setOrderedCoreTypeNames:"
+ "setStatsManager:"
+ "setUnitOptions:"
+ "setUnitStyle:"
+ "setWithObject:"
+ "statsManager"
+ "statsManager:didDetectMigration:"
+ "statsManager:didReceiveNWSnapshot:"
+ "statsManager:thresholdReachedOn:"
+ "stringFromBytesPerSecond:"
+ "stringFromMeasurement:"
+ "sysctlOrderedCoreTypeNames"
+ "terabits"
+ "v16@?0@\"NWStatsSnapshot\"8"
+ "v28@0:8@\"NWStatsManager\"16I24"
+ "v28@0:8@16I24"
+ "v32@0:8@\"NWStatsManager\"16@\"NWStatsMigrationEvent\"24"
+ "v32@0:8@\"NWStatsManager\"16@\"NWStatsSnapshot\"24"
+ "yottabits"
+ "zettabits"
- "## Skip updating app memory size due to corrupted sysmon report."
- "### Error getting hw.cpufamily: %i"
- "### Unknown cluster type!!"
- "1OA"
- "Could not get IODeviceTree for cpus service."
- "InterfaceIndex"
- "OA"
- "T@\"NSMutableDictionary\",&,V_cachedStats"
- "T@\"NSMutableDictionary\",&,V_destroyedStats"
- "TB,V_hasLocalCoprocessor"
- "TQ,V_localCoprocessorIndex"
- "T^{__NStatManager=},V_netStatManager"
- "^{__NStatManager=}"
- "^{__NStatManager=}16@0:8"
- "_cachedStats"
- "_destroyedStats"
- "_hasLocalCoprocessor"
- "_localCoprocessorIndex"
- "cachedStats"
- "destroyedStats"
- "hasLocalCoprocessor"
- "hw.cpufamily"
- "hw.cpufamily: 0x%x"
- "localCoprocessorIndex"
- "setCachedStats:"
- "setDestroyedStats:"
- "setHasLocalCoprocessor:"
- "setLocalCoprocessorIndex:"
- "v16@?0^{__CFDictionary=}8"
- "v16@?0^{__NStatSource=}8"
- "v24@0:8^{__NStatManager=}16"
```

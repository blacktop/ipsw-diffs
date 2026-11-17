## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-499.40.4.0.1
-  __TEXT.__text: 0x3f198
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x7700
-  __TEXT.__objc_methlist: 0x2f60
+499.60.3.0.0
+  __TEXT.__text: 0x3fb04
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x7840
+  __TEXT.__objc_methlist: 0x2fd8
   __TEXT.__const: 0x228
   __TEXT.__gcc_except_tab: 0x15e0
-  __TEXT.__cstring: 0x36c0
-  __TEXT.__oslogstring: 0x592a
+  __TEXT.__cstring: 0x371d
+  __TEXT.__oslogstring: 0x5a73
   __TEXT.__objc_classname: 0x2f4
-  __TEXT.__objc_methname: 0x8a6c
-  __TEXT.__objc_methtype: 0x1192
-  __TEXT.__unwind_info: 0x1420
+  __TEXT.__objc_methname: 0x8c79
+  __TEXT.__objc_methtype: 0x11a6
+  __TEXT.__unwind_info: 0x1440
   __DATA_CONST.__const: 0x1808
-  __DATA_CONST.__cfstring: 0x2e00
+  __DATA_CONST.__cfstring: 0x2e60
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x518
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x45b0
-  __DATA.__objc_selrefs: 0x2340
-  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_const: 0x4670
+  __DATA.__objc_selrefs: 0x2390
+  __DATA.__objc_ivar: 0x380
   __DATA.__objc_data: 0xd70
   __DATA.__data: 0x250
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1476
-  Symbols:   246
-  CStrings:  2792
+  Functions: 1492
+  Symbols:   247
+  CStrings:  2824
 
Symbols:
+ _setiopolicy_np
CStrings:
+ "%s: No counters output pointer was provided"
+ "%s: No path was provided"
+ "+[SASupport getAtimeUpdateCountersForPath:info:]"
+ "A-Time"
+ "FAILED to send A-Time counters telemetry\n"
+ "FSyncUpdateCount"
+ "Failed to GET atime update counters for %s with error %d (%s)"
+ "Failed to set IOPOL_ATIME_UPDATES_OFF: %s"
+ "Initial run. Set initial lastEventId, atime counters and abort."
+ "No kFSyncUpdateCount found"
+ "No kReclaimUpdateCount found"
+ "ReclaimUpdateCount"
+ "T@\"NSMutableDictionary\",&,V_fsyncUpdateCount"
+ "T@\"NSMutableDictionary\",&,V_lastFsyncUpdateCount"
+ "T@\"NSMutableDictionary\",&,V_lastReclaimUpdateCount"
+ "T@\"NSMutableDictionary\",&,V_reclaimUpdateCount"
+ "_fsyncUpdateCount"
+ "_lastFsyncUpdateCount"
+ "_lastReclaimUpdateCount"
+ "_reclaimUpdateCount"
+ "fsyncUpdateCount"
+ "fsyncUpdateCount %@"
+ "getAtimeUpdateCountersForPath:info:"
+ "i32@0:8@16^{?=QQ}24"
+ "lastFsyncUpdateCount"
+ "lastReclaimUpdateCount"
+ "reclaimUpdateCount"
+ "reclaimUpdateCount %@"
+ "setFsyncUpdateCount:"
+ "setLastFsyncUpdateCount:"
+ "setLastReclaimUpdateCount:"
+ "setReclaimUpdateCount:"
+ "updateATimeCountersForVolPath:reset:"
- "Initial run. Set initial lastEventId and abort."
```

## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1400.53.0.0.0
-  __TEXT.__text: 0x30914
+1400.57.0.0.0
+  __TEXT.__text: 0x30988
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_stubs: 0x4c80
-  __TEXT.__objc_methlist: 0x3018
+  __TEXT.__objc_stubs: 0x4ca0
+  __TEXT.__objc_methlist: 0x3028
   __TEXT.__const: 0x170
-  __TEXT.__oslogstring: 0x3541
-  __TEXT.__cstring: 0x27cf
-  __TEXT.__gcc_except_tab: 0x1194
-  __TEXT.__objc_methname: 0x8179
+  __TEXT.__oslogstring: 0x3660
+  __TEXT.__cstring: 0x273a
+  __TEXT.__gcc_except_tab: 0x11ac
+  __TEXT.__objc_methname: 0x81d0
   __TEXT.__objc_classname: 0x45c
   __TEXT.__objc_methtype: 0x14fc
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xc78
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0xca0
-  __DATA_CONST.__cfstring: 0x2420
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__cfstring: 0x23c0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x5810
-  __DATA.__objc_selrefs: 0x19a8
-  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_const: 0x5870
+  __DATA.__objc_selrefs: 0x19b0
+  __DATA.__objc_ivar: 0x49c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x360
   __DATA.__bss: 0x138

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F82FBAA7-1CDE-31BD-B786-516E980A5668
-  Functions: 1272
+  UUID: E9D5CBF2-435B-3A27-9A88-60CD4CBC51D1
+  Functions: 1271
   Symbols:   202
-  CStrings:  2396
+  CStrings:  2400
 
CStrings:
+ "1400.57"
+ "External sync session took %llu nanoseconds to lock"
+ "Failed to get monotonic time while calculating clock session runtime"
+ "Failed to get monotonic time while calculating sync session runtime"
+ "Failed to get monotonic time while calculating time to lock"
+ "Failed to get sync session start time"
+ "TQ,R,N,V_threadRestarts"
+ "TQ,R,N,V_timeToLockNs"
+ "TQ,R,N,V_triggerLostCnt"
+ "_timeToLockNs"
+ "_triggerLostCnt"
+ "com.apple.TimeSync.MSG.clock-session"
+ "com.apple.TimeSync.MSG.external-sync-session"
+ "isSimulation"
+ "nominalSyncRate"
+ "nominalTriggerRate"
+ "sessionRunTimeMicros"
+ "syncMultiplier"
+ "timeToLockMicros"
+ "timeToLockNs"
+ "timeoutMicros"
+ "toleranceExternalTriggerMicros"
+ "toleranceSyncOutputMicros"
+ "triggerLostCnt"
- "1400.53"
- "TQ,N,V_threadRestarts"
- "com.apple.TimeSync.MSG.message"
- "com.apple.TimeSync.MSG.restore-clock-session"
- "com.apple.TimeSync.MSG.start-clock-session"
- "com.apple.TimeSync.MSG.start-external-sync"
- "com.apple.TimeSync.MSG.stop-clock-session"
- "com.apple.TimeSync.MSG.stop-external-sync"
- "isSimulation:"
- "msgType"
- "nominalTriggerDurationDen"
- "nominalTriggerDurationNum"
- "sessionRunTimeNs:"
- "setThreadRestarts:"
- "syncConfig"
- "syncMultiplierDen"
- "syncMultiplierNum"
- "timeoutNs"
- "toleranceExternalTriggerNs"
- "toleranceSyncOutputNs"

```

## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-378.0.0.0.0
-  __TEXT.__text: 0x1502c
+380.0.0.0.0
+  __TEXT.__text: 0x1503c
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x968
-  __TEXT.__const: 0x168
+  __TEXT.__const: 0x170
   __TEXT.__cstring: 0x41f6
   __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__oslogstring: 0x27fb
+  __TEXT.__oslogstring: 0x279d
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x508
+  __TEXT.__unwind_info: 0x528
   __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methname: 0x398f
   __TEXT.__objc_methtype: 0x759
   __TEXT.__objc_stubs: 0x1440
   __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x1628
+  __DATA_CONST.__const: 0x1650
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x938

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2454BBE8-40DB-37FA-B700-9A1A3C62D4E2
+  UUID: F2166393-B7CA-36EF-9447-99B7969C7D41
   Functions: 527
-  Symbols:   1945
-  CStrings:  2211
+  Symbols:   1950
+  CStrings:  2209
 
Symbols:
+ GCC_except_table14
+ _HTForegroundTrackingEnd.cold.2
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_3
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_3.cold.1
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- GCC_except_table13
- _HTForegroundTrackingBegin.cold.3
- ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_2.cold.1
CStrings:
+ "App with bundleID:%{public}s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
+ "HTInitializeHangTracerMonitor: XPC_TYPE_ERR for appConnection with pid %d: %{public}s"
+ "Received RB Notification for state change of pid %d with bundleID '%{public}@'. State changed from %d to %d"
- "App with bundleID:%s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
- "HTInitializeHangTracerMonitor: XPC_TYPE_ERR for appConnection: %s"
- "Received RB Notification for state change of process '%s'. State changed from %d to %d"
- "Started os_signpost_interval_begin for newSignpostID:%llu and bundleID:%s"
- "Started os_signpost_interval_end for signpostID:%llu and bundleID:%s"

```

## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-378.0.0.0.0
+380.0.0.0.0
   __TEXT.__text: 0x11350
   __TEXT.__auth_stubs: 0x990
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0xb24
-  __TEXT.__const: 0x158
+  __TEXT.__const: 0x160
   __TEXT.__cstring: 0x2476
-  __TEXT.__oslogstring: 0x1892
+  __TEXT.__oslogstring: 0x1820
   __TEXT.__gcc_except_tab: 0x1cc
   __TEXT.__objc_methname: 0x4032
   __TEXT.__objc_classname: 0xb2

   __TEXT.__unwind_info: 0x3a8
   __DATA_CONST.__auth_got: 0x4d8
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__const: 0xc10
   __DATA_CONST.__cfstring: 0x2380
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8069B0D1-6606-304D-A6F2-A3255A8B65A1
+  UUID: 961C4306-83A9-33F9-B75B-E70F2A5FA362
   Functions: 414
   Symbols:   434
-  CStrings:  1414
+  CStrings:  1412
 
CStrings:
+ "App with bundleID:%{public}s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
+ "Received RB Notification for state change of pid %d with bundleID '%{public}@'. State changed from %d to %d"
- "App with bundleID:%s is no longer foreground at time=%llu, attempting to emit telemetry with emission type: %@"
- "Received RB Notification for state change of process '%s'. State changed from %d to %d"
- "Started os_signpost_interval_begin for newSignpostID:%llu and bundleID:%s"
- "Started os_signpost_interval_end for signpostID:%llu and bundleID:%s"

```

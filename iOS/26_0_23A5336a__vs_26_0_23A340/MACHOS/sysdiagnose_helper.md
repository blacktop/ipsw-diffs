## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 1527.0.4.0.0
-  __TEXT.__text: 0x395bc
+  __TEXT.__text: 0x399f8
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x57c
-  __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x7f4
-  __TEXT.__oslogstring: 0x228e
-  __TEXT.__cstring: 0x2f18a
+  __TEXT.__objc_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x58c
+  __TEXT.__const: 0x3f0
+  __TEXT.__gcc_except_tab: 0x830
+  __TEXT.__oslogstring: 0x238e
+  __TEXT.__cstring: 0x2f1d6
   __TEXT.__objc_classname: 0xc4
-  __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x15c1
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__objc_methtype: 0x2ac
+  __TEXT.__objc_methname: 0x15ee
+  __TEXT.__unwind_info: 0x578
   __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x1b60
+  __DATA_CONST.__auth_ptr: 0xa0
+  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__cfstring: 0x1b80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x5f0
+  __DATA.__objc_selrefs: 0x5f8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/WirelessInsights.framework/WirelessInsights
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
+  - /System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 6C804104-E04D-33AF-AD07-08DC8034AA10
-  Functions: 338
+  UUID: 1BE1F3DF-AA4A-36D9-85BE-DF4CF09904E2
+  Functions: 343
   Symbols:   257
-  CStrings:  4323
+  CStrings:  4334
 
Symbols:
+ _collectClientLogsWithSizeAndOverride
+ _objc_retain_x25
- _objc_retain_x24
- _objc_retain_x3
CStrings:
+ "B40@0:8@16d24@32"
+ "BTProfileInstalled"
+ "CentauriDiagnostic SPI error. Finished: %d, return success: %d"
+ "CentauriDiagnostic framework not found on this platform, failing centauriTaskWithDir"
+ "Error: got 0 for container size cap for centauri task!"
+ "TASK_TYPE_CENTAURI"
+ "Using size: %lld and flags %d for CentauriDiagnostic"
+ "centauriTaskWithDir:withTimeout:withRequest:"
+ "containerSizeCap"
+ "wifiProfileInstalled"

```

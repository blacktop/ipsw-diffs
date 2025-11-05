## BridgeOSInstall

> `/System/Library/PrivateFrameworks/BridgeOSInstall.framework/Versions/A/BridgeOSInstall`

```diff

 89.0.0.0.0
-  __TEXT.__text: 0x33254
+  __TEXT.__text: 0x334f4
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x1a38
+  __TEXT.__objc_methlist: 0x1c04
   __TEXT.__const: 0xf8
   __TEXT.__oslogstring: 0x26be
   __TEXT.__cstring: 0x43e8
   __TEXT.__gcc_except_tab: 0xbc0
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_classname: 0x2f7
   __TEXT.__objc_methname: 0x4eb2
   __TEXT.__objc_methtype: 0x6a4

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1288
+  __DATA_CONST.__objc_selrefs: 0x1320
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__cfstring: 0x3640
-  __AUTH_CONST.__objc_const: 0x31f0
+  __AUTH_CONST.__objc_const: 0x2e78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x1b4

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3275AC50-289A-3451-ADE1-7C1CD9A50F32
-  Functions: 732
-  Symbols:   1901
+  UUID: 548108DA-AA0D-30B8-A2D8-9DC88D10405B
+  Functions: 741
+  Symbols:   1909
   CStrings:  2071
 
Symbols:
+ +[BOSNVRAM sharedInstance].cold.1
+ +[BOSPackageAnalyzer sharedAnalyzer].cold.1
+ -[BOSConfigureRequestOperation _extractFirmwareBundleComponent:error:].cold.1
+ -[BOSTelemetry _submitToInstallerDiagnostics].cold.1
+ BOSLogObject.cold.1
+ BOSLogSerial.cold.1
+ BOSShouldLogToInstallLog.cold.1
+ BOSShouldLogToStderr.cold.1
+ _weak_BOSReporterServiceController.cold.1
+ standardErrorDateFormatter.cold.1
- _OUTLINED_FUNCTION_3

```

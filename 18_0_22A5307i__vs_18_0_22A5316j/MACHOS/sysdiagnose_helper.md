## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1424.0.0.0.0
-  __TEXT.__text: 0x33e1c
+1431.0.0.0.0
+  __TEXT.__text: 0x34344
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x4fc
+  __TEXT.__objc_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x508
   __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x750
-  __TEXT.__oslogstring: 0x1e35
-  __TEXT.__cstring: 0x2b3ac
+  __TEXT.__gcc_except_tab: 0x7c0
+  __TEXT.__oslogstring: 0x1f17
+  __TEXT.__cstring: 0x2b3f8
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x13a2
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__objc_methname: 0x13eb
+  __TEXT.__unwind_info: 0x4e8
   __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x618
-  __DATA_CONST.__cfstring: 0x1a00
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__cfstring: 0x1a40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x718
-  __DATA.__objc_selrefs: 0x548
+  __DATA.__objc_selrefs: 0x558
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  Functions: 304
-  Symbols:   239
-  CStrings:  3743
+  Functions: 307
+  Symbols:   240
+  CStrings:  3751
 
Symbols:
+ _OBJC_CLASS_$_GESysdiagnoseXPCClient
+ _TSPDumpOptions_Symbolicate
- _TSPDumpOptions_NoSymbolicate
CStrings:
+ "GEAvailability task SPI not available, timed out or couldn't create the dest file"
+ "GEAvailability task encountered error when calling diagnosticsWithCompletionHandler: %!@(MISSING)"
+ "GEAvailability.log"
+ "GEAvailabilityTaskWithDir:withTimeout:"
+ "GESysdiagnoseXPCClient class not found on this platform"
+ "TASK_TYPE_GE_AVAILABILITY"
+ "diagnosticsWithCompletionHandler:"
+ "v24@?0@\"NSString\"8@\"NSError\"16"

```

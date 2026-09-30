## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-323.0.0.0.0
-  __TEXT.__text: 0xa3b4
-  __TEXT.__auth_stubs: 0x740
+326.0.0.0.0
+  __TEXT.__text: 0xa3d4
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x7f8
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x159d
-  __TEXT.__oslogstring: 0x1005
+  __TEXT.__cstring: 0x159f
+  __TEXT.__oslogstring: 0x1012
   __TEXT.__objc_methname: 0x31d9
   __TEXT.__objc_classname: 0x5c
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__objc_methtype: 0x688
-  __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__auth_got: 0x3b0
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x17a0
+  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18

   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x90
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xa8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 241
-  Symbols:   322
-  CStrings:  804
+  Functions: 242
+  Symbols:   319
+  CStrings:  805
 
Symbols:
+ _HTTelemetryHasRunThisBoot
+ _sem_close
+ _sem_open
- _HTGetBootSessionUUID
- _HTTelemetryIsForCurrentBoot
- _kHTPrefsTelemetryBootSessionUUID
- _objc_opt_class
- _objc_opt_isKindOfClass
- _sysctlbyname
CStrings:
+ "Updating telemetry"
+ "com.apple.hangtracer.prefsqueue"
+ "hangtelemetryd.onceatboot"
+ "sem_open() failed: %!{(MISSING)errno}d"
- "HangTracerTelemetryBootSessionUUID"
- "Unable to get boot UUID: %!{(MISSING)errno}d"
- "kern.bootsessionuuid"

```

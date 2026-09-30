## splashboardd

> `/usr/libexec/splashboardd`

```diff

-308.3.1.0.0
-  __TEXT.__text: 0x53b0
-  __TEXT.__auth_stubs: 0x6b0
+308.4.1.0.0
+  __TEXT.__text: 0x5af4
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_stubs: 0x16e0
   __TEXT.__objc_methlist: 0x4e4
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x411
-  __TEXT.__gcc_except_tab: 0x354
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0x43a
+  __TEXT.__gcc_except_tab: 0x360
   __TEXT.__objc_methname: 0x16cb
   __TEXT.__objc_classname: 0xcb
   __TEXT.__objc_methtype: 0x36d
-  __TEXT.__oslogstring: 0x922
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x218
+  __TEXT.__oslogstring: 0xa40
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x270
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56DEC5B6-0837-3E72-8DCC-CC510178E3D1
-  Functions: 133
-  Symbols:   189
-  CStrings:  434
+  UUID: 6113A483-D094-3B0A-B1DB-6F83E3373A18
+  Functions: 138
+  Symbols:   186
+  CStrings:  439
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _XBLaunchImageProviderMessageKeyWithTimeout
+ _objc_retain_x25
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "BundleIdOverride=%{public, signpost.description:attribute}@ elapsed=%{signpost.telemetry:number1, public}f timeout=%{signpost.telemetry:number2, public}f enableTelemetry=YES "
+ "LayoutTimeout"
+ "[%@] Layout time (%f) is over limit (%f)"
+ "[%@] layout time (%f) is over limit (%f); but proceeding to capture anyway (timeout %d debug %d)"

```

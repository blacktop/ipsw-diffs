## com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x21e64
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x62e0
-  __TEXT.__objc_methlist: 0x1eac
+916.51.202.0.0
+  __TEXT.__text: 0x2220c
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x6480
+  __TEXT.__objc_methlist: 0x1edc
   __TEXT.__dlopen_cstrs: 0xbe
   __TEXT.__const: 0x1c0
   __TEXT.__gcc_except_tab: 0xb68
-  __TEXT.__objc_methname: 0x827c
-  __TEXT.__oslogstring: 0x3008
-  __TEXT.__cstring: 0x3627
+  __TEXT.__objc_methname: 0x83dd
+  __TEXT.__oslogstring: 0x30db
+  __TEXT.__cstring: 0x3899
   __TEXT.__objc_classname: 0x3d5
   __TEXT.__objc_methtype: 0xd26
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x8f8
   __DATA_CONST.__const: 0xc20
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__cfstring: 0x28a0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0x7c8
-  __DATA.__objc_const: 0x2dd8
-  __DATA.__objc_selrefs: 0x1d80
-  __DATA.__objc_ivar: 0x254
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x7e0
+  __DATA.__objc_const: 0x2e18
+  __DATA.__objc_selrefs: 0x1de0
+  __DATA.__objc_ivar: 0x258
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 695
-  Symbols:   431
-  CStrings:  1928
+  Functions: 699
+  Symbols:   436
+  CStrings:  1952
 
Symbols:
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_PFRadarComponent
+ _OBJC_CLASS_$_PFTapToRadarDraft
+ _PFOSVariantHasInternalDiagnostics
+ _PFTapToRadarCreateDraft
CStrings:
+ "A video conversion stopped reporting progress, so VideoConversionService force-crashed itself. The crash report records only that deliberate crash. What the conversion and the rest of the system were stuck on is in the spindump inside the attached sysdiagnose.\n\nSource resources: %@\nSource sizes: %@\nDestination: %@\nConversion task: %@ %@\nHang detector: %@\nQueue entry: %@\nRequest reason: %@\n"
+ "Photos Backend Media Conversion Services"
+ "Photos Video Conversion"
+ "T@\"NSString\",R,V_hangDetectionSummary"
+ "Tap-to-Radar is gathering diagnostics for the stalled conversion, staying alive %.0f s so its spindump can sample us"
+ "Unable to create output image destination of type %{public}@"
+ "Unable to open a Tap-to-Radar draft for the stalled conversion: %{public}@"
+ "VideoConversionService: video conversion made no progress for an hour"
+ "_captureVideoConversionHangDiagnosticsForQueueEntry:conversionTask:"
+ "_hangDetectionSummary"
+ "all"
+ "currentStateSummary"
+ "hangDetectionSummary"
+ "initWithIdentifier:name:version:"
+ "progress %.4f unchanged for %.0f s, threshold %.0f s"
+ "setCapturesPerformanceTrace:"
+ "setClassification:"
+ "setComponent:"
+ "setDisplayReason:"
+ "setProblemDescription:"
+ "setProcessName:"
+ "setTitle:"
+ "sleepForTimeInterval:"
+ "video conversion stopped making progress"
+ "\xf0!"
- "Unable to create output image destination"
```

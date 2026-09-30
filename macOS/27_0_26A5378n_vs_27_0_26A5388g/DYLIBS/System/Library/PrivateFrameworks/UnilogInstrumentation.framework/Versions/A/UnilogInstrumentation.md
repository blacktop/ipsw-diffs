## UnilogInstrumentation

> `/System/Library/PrivateFrameworks/UnilogInstrumentation.framework/Versions/A/UnilogInstrumentation`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-2.0.2.0.0
-  __TEXT.__text: 0x18e4c
+2.0.3.0.0
+  __TEXT.__text: 0x1a220
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x1010
+  __TEXT.__const: 0x1050
   __TEXT.__constg_swiftt: 0x69c
-  __TEXT.__swift5_typeref: 0x5f8
+  __TEXT.__swift5_typeref: 0x60e
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x215
   __TEXT.__swift5_fieldmd: 0x47c
   __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_proto: 0x8c
-  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__swift_as_cont: 0x34
-  __TEXT.__oslogstring: 0x2f1
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__oslogstring: 0x311
   __TEXT.__cstring: 0x1f1
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0xe4
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x688
-  __TEXT.__eh_frame: 0xa70
+  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__eh_frame: 0xaf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __DATA_CONST.__got: 0x230
-  __AUTH_CONST.__const: 0x908
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x9a8
   __AUTH_CONST.__objc_const: 0x710
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x810
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x8a8
-  __DATA.__data: 0x640
+  __DATA.__data: 0x650
   __DATA.__bss: 0xe90
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/PrivateFrameworks/Dendrite.framework/Versions/A/Dendrite
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/Versions/A/UnilogCommonLibrary
+  - /System/Library/PrivateFrameworks/UnilogPlatformLibrary.framework/Versions/A/UnilogPlatformLibrary
+  - /System/Library/PrivateFrameworks/UnilogTelemetry.framework/Versions/A/UnilogTelemetry
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 474
-  Symbols:   314
-  CStrings:  36
+  Functions: 486
+  Symbols:   316
+  CStrings:  37
 
Symbols:
+ _symbolic _____ 19UnilogCommonLibrary12StagingEventV0D12PayloadUnionO
+ _symbolic _____Sg 21UnilogPlatformLibrary14TelemetryErrorV
+ _symbolic _____Sg 21UnilogPlatformLibrary7VersionV
- __swift_closure_destructor.29Tm
CStrings:
+ "Telemetry not available"
```

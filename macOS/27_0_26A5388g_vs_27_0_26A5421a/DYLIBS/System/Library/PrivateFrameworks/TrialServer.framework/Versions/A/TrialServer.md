## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-508.0.0.0.0
-  __TEXT.__text: 0x16a4d8
+511.0.0.0.0
+  __TEXT.__text: 0x16a654
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa28
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc73c
+  __TEXT.__objc_methlist: 0xc734
   __TEXT.__const: 0xefc
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__cstring: 0x16e2a

   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1df13
-  __TEXT.__gcc_except_tab: 0x7ecc
+  __TEXT.__oslogstring: 0x1df73
+  __TEXT.__gcc_except_tab: 0x7f0c
   __TEXT.__unwind_info: 0x44c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 5110
   Symbols:   12418
-  CStrings:  4251
+  CStrings:  4252
 
Symbols:
+ +[TRITaskUtils prevTelemetryFieldsFromActivationEventDatabase:deactivatedRecord:]
- +[TRIDeactivateTreatmentTask prevTelemetryFieldsFromActivationEventDatabase:deactivatedRecord:]
CStrings:
+ "Aug 10 2026"
+ "Failed to log deactivation post-launch event for outgoing treatment %@ of experiment %{public}@"
+ "TrialXP-511"
- "Jul 10 2026"
- "TrialXP-508"
```

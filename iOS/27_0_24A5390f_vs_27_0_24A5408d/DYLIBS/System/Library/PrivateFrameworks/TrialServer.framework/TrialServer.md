## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-508.0.0.0.0
-  __TEXT.__text: 0x151768
+511.0.0.0.0
+  __TEXT.__text: 0x1518cc
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x794
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc7b4
+  __TEXT.__objc_methlist: 0xc7ac
   __TEXT.__const: 0xeec
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__cstring: 0x16925

   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1de95
-  __TEXT.__gcc_except_tab: 0x7ee8
-  __TEXT.__unwind_info: 0x4378
+  __TEXT.__oslogstring: 0x1def5
+  __TEXT.__gcc_except_tab: 0x7f28
+  __TEXT.__unwind_info: 0x43a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 4979
   Symbols:   12210
-  CStrings:  4226
+  CStrings:  4227
 
Symbols:
+ +[TRITaskUtils prevTelemetryFieldsFromActivationEventDatabase:deactivatedRecord:]
- +[TRIDeactivateTreatmentTask prevTelemetryFieldsFromActivationEventDatabase:deactivatedRecord:]
CStrings:
+ "Failed to log deactivation post-launch event for outgoing treatment %@ of experiment %{public}@"
+ "TrialXP-511"
- "TrialXP-508"
```

## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

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
+ "Aug  4 2026"
+ "Failed to log deactivation post-launch event for outgoing treatment %@ of experiment %{public}@"
+ "TrialXP-511"
- "Jul 10 2026"
- "TrialXP-508"
```

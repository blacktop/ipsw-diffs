## FitnessIntelligencePlugin

> `/System/Library/Health/Plugins/FitnessIntelligencePlugin.bundle/FitnessIntelligencePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-2027.0.71.0.0
-  __TEXT.__text: 0x80554
+2027.0.74.0.0
+  __TEXT.__text: 0x810f8
   __TEXT.__auth_stubs: 0x1f30
   __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__const: 0x15e8
+  __TEXT.__const: 0x1618
   __TEXT.__cstring: 0x1b0f
-  __TEXT.__constg_swiftt: 0xbbc
+  __TEXT.__constg_swiftt: 0xbc4
   __TEXT.__swift5_typeref: 0x130e
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x77f
   __TEXT.__swift5_fieldmd: 0x7f0
-  __TEXT.__swift5_capture: 0x1110
+  __TEXT.__swift5_capture: 0x1134
   __TEXT.__objc_methtype: 0xb8b
-  __TEXT.__oslogstring: 0x142f
+  __TEXT.__oslogstring: 0x14cf
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_proto: 0xbc
   __TEXT.__swift5_types: 0x9c
   __TEXT.__objc_classname: 0x936
   __TEXT.__objc_methname: 0x16c9
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x8
-  __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1328
-  __TEXT.__eh_frame: 0x1d18
-  __DATA_CONST.__const: 0x4318
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__swift_as_cont: 0x18
+  __TEXT.__unwind_info: 0x1348
+  __TEXT.__eh_frame: 0x1de8
+  __DATA_CONST.__const: 0x4368
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_ptr: 0x468
   __DATA.__objc_const: 0x15f8
   __DATA.__objc_selrefs: 0x4d0
-  __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0x1708
+  __DATA.__objc_data: 0x12b0
+  __DATA.__data: 0x1718
   __DATA.__bss: 0x1790
   __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1813
-  Symbols:   237
-  CStrings:  519
+  Functions: 1821
+  Symbols:   236
+  CStrings:  523
 
Symbols:
- _notify_post
CStrings:
+ "[%s] Active Workout going on, cancelling snapshot processing"
+ "[%s] Failed to cancel snapshot processing: %@."
+ "[%s] Failed to invalidate OSTransaction: %@."
+ "isReadyToProcess = %{bool}d"
+ "isReadyToProcess = false: workout is active"
+ "isReadyToProcessWithCompletion:"
- "[%s] Failed to invalidate OSTransaction: %@. Sending Darwin Notification"
- "hasDataToProcessWithCompletion:"
```

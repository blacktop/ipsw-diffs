## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_classname`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3039.42.2.0.0
-  __TEXT.__text: 0x241bec
+3039.60.4.0.0
+  __TEXT.__text: 0x241e20
   __TEXT.__auth_stubs: 0x32a0
-  __TEXT.__objc_stubs: 0x281c0
-  __TEXT.__objc_methlist: 0x15ee4
+  __TEXT.__objc_stubs: 0x28200
+  __TEXT.__objc_methlist: 0x15ef4
   __TEXT.__const: 0x1820
   __TEXT.__objc_classname: 0x2156
-  __TEXT.__objc_methname: 0x3782a
+  __TEXT.__objc_methname: 0x3784a
   __TEXT.__objc_methtype: 0x65c4
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_typeref: 0xcfa

   __TEXT.__swift5_fieldmd: 0xca0
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__cstring: 0x68aaf
+  __TEXT.__cstring: 0x68afb
   __TEXT.__swift5_proto: 0x98
   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_capture: 0x3cc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__oslogstring: 0x316d2
+  __TEXT.__oslogstring: 0x316e0
   __TEXT.__gcc_except_tab: 0xa0cc
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x7410
   __TEXT.__eh_frame: 0x1cd8
   __DATA_CONST.__const: 0x7de8
-  __DATA_CONST.__cfstring: 0x1aea0
+  __DATA_CONST.__cfstring: 0x1aee0
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x270

   __DATA_CONST.__got: 0xf30
   __DATA_CONST.__auth_ptr: 0x2a0
   __DATA.__objc_const: 0x237b8
-  __DATA.__objc_selrefs: 0xb7d8
+  __DATA.__objc_selrefs: 0xb7e0
   __DATA.__objc_ivar: 0x19a0
   __DATA.__objc_data: 0x6b30
   __DATA.__data: 0x2378

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8930
+  Functions: 8931
   Symbols:   1316
-  CStrings:  18420
+  CStrings:  18423
 
CStrings:
+ "=scheduler= Not rescheduling the next WiFi backup at %@ because there is already a DAS backup scheduled at %@"
+ "=scheduler= Not rescheduling the next battery backup at %@ because there is already a DAS backup scheduled at %@"
+ "=scheduler= Not rescheduling the next cellular backup at %@ because there is already a DAS backup scheduled at %@"
+ "Unexpected attempt summary plist root: %@"
+ "canReuseActivityScheduledFor:"
+ "repairedDomainCount"
- "=scheduler= Not scheduling the next WiFi backup at %@ because there is already a DAS backup scheduled at %@"
- "=scheduler= Not scheduling the next battery backup at %@ because there is already a DAS backup scheduled at %@"
- "=scheduler= Not scheduling the next cellular backup at %@ because there is a DAS backup scheduled at %@"
```

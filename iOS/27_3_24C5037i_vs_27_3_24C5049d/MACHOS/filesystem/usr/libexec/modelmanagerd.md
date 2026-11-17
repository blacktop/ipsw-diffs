## modelmanagerd

> `/usr/libexec/modelmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-714.60.14.0.0
-  __TEXT.__text: 0x1af67c
+714.60.17.0.0
+  __TEXT.__text: 0x1af430
   __TEXT.__auth_stubs: 0x40a0
   __TEXT.__objc_stubs: 0x700
   __TEXT.__objc_methlist: 0x1c0
-  __TEXT.__const: 0x69b6
-  __TEXT.__swift5_typeref: 0x2969
-  __TEXT.__cstring: 0x2030
-  __TEXT.__swift5_capture: 0x283c
-  __TEXT.__oslogstring: 0xa6d9
+  __TEXT.__const: 0x6996
+  __TEXT.__swift5_typeref: 0x2949
+  __TEXT.__cstring: 0x2010
+  __TEXT.__swift5_capture: 0x2800
+  __TEXT.__oslogstring: 0xa639
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2f14
+  __TEXT.__constg_swiftt: 0x2ec4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x2863
-  __TEXT.__swift5_fieldmd: 0x22d4
+  __TEXT.__swift5_reflstr: 0x2823
+  __TEXT.__swift5_fieldmd: 0x22b0
   __TEXT.__swift5_types: 0x1d4
   __TEXT.__objc_classname: 0xb90
-  __TEXT.__objc_methname: 0x1b13
+  __TEXT.__objc_methname: 0x1ae3
   __TEXT.__objc_methtype: 0x395
-  __TEXT.__swift_as_entry: 0x984
-  __TEXT.__swift_as_ret: 0xb34
-  __TEXT.__swift_as_cont: 0x12f0
+  __TEXT.__swift_as_entry: 0x97c
+  __TEXT.__swift_as_ret: 0xb30
+  __TEXT.__swift_as_cont: 0x12cc
   __TEXT.__swift5_proto: 0x318
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_assocty: 0x1b8
-  __TEXT.__unwind_info: 0x7920
-  __TEXT.__eh_frame: 0x1740c
-  __DATA_CONST.__const: 0x8b38
+  __TEXT.__unwind_info: 0x78d8
+  __TEXT.__eh_frame: 0x172ec
+  __DATA_CONST.__const: 0x8af0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x2058
   __DATA_CONST.__got: 0xf88
   __DATA_CONST.__auth_ptr: 0xd98
-  __DATA.__objc_const: 0x45a0
+  __DATA.__objc_const: 0x4540
   __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_data: 0x7a0
-  __DATA.__data: 0x6690
-  __DATA.__common: 0x6c0
+  __DATA.__data: 0x6620
+  __DATA.__common: 0x6b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9473
+  Functions: 9442
   Symbols:   1748
-  CStrings:  1260
+  CStrings:  1253
 
CStrings:
+ "Conclave bootstrap hit a terminated provider, retrying after its cleanup"
+ "Discovered %ld new extensions and removed %ld (%ld total)"
+ "onChange"
- "Discovered %ld new extensions and removed %ld"
- "Handling exclave unload for asset %s"
- "assertionRequestID"
- "bootstrapsInFlight"
- "markAsInactive removed jetsam floor (synthetic request %s)"
- "markAsInactive skipped — connection still in use (bootstrap in flight or sibling loaded)"
- "markAsInactive skipped — not currently active"
- "markAsInactive(connection:)"
- "onAssetDidUnload"
- "onUpdate"
```

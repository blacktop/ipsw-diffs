## FedStatsEncoder

> `/System/Library/PrivateFrameworks/FedStatsEncoder.framework/Versions/A/FedStatsEncoder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x416f8
+38.0.0.0.0
+  __TEXT.__text: 0x41f9c
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x1a40
-  __TEXT.__cstring: 0x66b
-  __TEXT.__oslogstring: 0x1caf
+  __TEXT.__const: 0x1a70
+  __TEXT.__cstring: 0x65b
+  __TEXT.__oslogstring: 0x1cff
   __TEXT.__constg_swiftt: 0xc4c
   __TEXT.__swift5_typeref: 0x7db
-  __TEXT.__swift5_reflstr: 0x85b
-  __TEXT.__swift5_fieldmd: 0xb00
+  __TEXT.__swift5_reflstr: 0x89f
+  __TEXT.__swift5_fieldmd: 0xb18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0xe0
   __TEXT.__swift5_proto: 0xc4
   __TEXT.__swift5_types: 0xe8
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0xd48
-  __TEXT.__eh_frame: 0x22c0
+  __TEXT.__unwind_info: 0xd58
+  __TEXT.__eh_frame: 0x22f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x18b0
   __AUTH_CONST.__objc_const: 0x1bf8
-  __AUTH_CONST.__auth_got: 0x870
+  __AUTH_CONST.__auth_got: 0x878
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x1520
-  __DATA.__data: 0x598
+  __DATA.__data: 0x5a8
   __DATA.__bss: 0xe00
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1008
-  Symbols:   517
-  CStrings:  177
+  Functions: 1012
+  Symbols:   518
+  CStrings:  179
 
Symbols:
+ _sqlite3_bind_text
CStrings:
+ "Cannot bind parameter at index %d: %s"
+ "Cannot prepare command: %s"
+ "SELECT %@ FROM '%@' WHERE %@ == ? ORDER BY RANDOM() LIMIT 1"
+ "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == ?"
+ "SELECT COUNT(1) AS %@ FROM '%@' WHERE ? LIKE '%%' || \"%@\" || '%%'"
- "SELECT %@ FROM '%@' WHERE %@ == \"%@\" ORDER BY RANDOM() LIMIT 1"
- "SELECT COUNT(1) AS %@ FROM '%@' WHERE \"%@\" LIKE '%%' || \"%@\" || '%%'"
- "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == \"%@\""
```

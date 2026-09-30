## com.apple.datamigrator

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2858.0.0.0.0
-  __TEXT.__text: 0x12874
-  __TEXT.__auth_stubs: 0xa00
+2858.1.3.0.0
+  __TEXT.__text: 0x128c4
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_stubs: 0x3300
   __TEXT.__objc_methlist: 0x1404
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x9f8
   __TEXT.__objc_methname: 0x429f
-  __TEXT.__cstring: 0x3b64
+  __TEXT.__cstring: 0x3b63
   __TEXT.__objc_classname: 0x301
   __TEXT.__objc_methtype: 0x84b
   __TEXT.__dlopen_cstrs: 0xfe

   __TEXT.__oslogstring: 0xfe
   __TEXT.__unwind_info: 0x5e0
   __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__cfstring: 0x2a60
+  __DATA_CONST.__cfstring: 0x2a80
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0x1d0
   __DATA.__objc_const: 0x3240
   __DATA.__objc_selrefs: 0xf48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 470
-  Symbols:   307
-  CStrings:  1227
+  Symbols:   306
+  CStrings:  1228
 
Symbols:
- _xpc_transaction_exit_clean
Functions:
~ sub_1000014d0 : 400 -> 396
~ sub_10000eec0 -> sub_10000eebc : 692 -> 776
CStrings:
+ "DMMigratorProxy did end transaction for event %p msgID %@ from client pid %@."
+ "DMMigratorProxy did send response for event %p msgID %@ to client pid %@. will end transaction."
+ "Terminating Preboard in mode: %@"
- "DMMigratorProxy did end transaction for event %p msgID %@ from client pid %@. will attempt to exit clean."
- "DMMigratorProxy did send response for event %p msgID %@ to client pid %@. will attempt to exit clean."
```

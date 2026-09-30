## biomesyncd

> `usr/libexec/biomesyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__linkguard`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-209.21.0.0.0
-  __TEXT.__text: 0x5425c
+209.22.0.0.0
+  __TEXT.__text: 0x54720
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x88a0
+  __TEXT.__objc_stubs: 0x8940
   __TEXT.__objc_methlist: 0x3c0c
-  __TEXT.__const: 0x1348
+  __TEXT.__const: 0x1358
   __TEXT.__gcc_except_tab: 0xa00
-  __TEXT.__objc_methname: 0xa2bd
-  __TEXT.__cstring: 0x59dc
+  __TEXT.__objc_methname: 0xa3b3
+  __TEXT.__cstring: 0x5a22
   __TEXT.__objc_classname: 0x83d
   __TEXT.__objc_methtype: 0x16fe
-  __TEXT.__oslogstring: 0x6574
-  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__oslogstring: 0x65b2
+  __TEXT.__unwind_info: 0x11c8
   __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x1280
-  __DATA_CONST.__cfstring: 0x4720
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x12d0
+  __DATA_CONST.__cfstring: 0x4740
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__linkguard: 0xf
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x7708
-  __DATA.__objc_selrefs: 0x28b8
+  __DATA.__objc_selrefs: 0x28e0
   __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1682
-  Symbols:   323
-  CStrings:  3075
+  Functions: 1686
+  Symbols:   324
+  CStrings:  3084
 
Symbols:
+ _OBJC_CLASS_$_BMPersonaUtilities
CStrings:
+ " with persona: %@"
+ "-[BMSyncServiceServer cascadeRapportSyncWithReply:]"
+ "Failed to assume persona %@ with error %@"
+ "Starting sync server for event: %s%@"
+ "cascadeRapportSync called%@"
+ "currentPersonaIdentifierLoggingDescription"
+ "handleIncomingSyncRequestsWithReason:completionHandler:"
+ "runAsPersonaIdentifier:block:"
+ "syncAllPersonasNowWithReason:activity:completionHandler:"
+ "syncCurrentPersonaNowWithReason:activity:completionHandler:"
- "activity \"%s\" not supported on this platform"
```

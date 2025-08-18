## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-829.0.54.0.0
-  __TEXT.__text: 0x4afd8c
+829.2.2.0.0
+  __TEXT.__text: 0x4b06fc
   __TEXT.__auth_stubs: 0x5520
-  __TEXT.__objc_methlist: 0x6b10
+  __TEXT.__objc_methlist: 0x6b40
   __TEXT.__const: 0x290e8
-  __TEXT.__cstring: 0x1be77
-  __TEXT.__oslogstring: 0xc462
+  __TEXT.__cstring: 0x1bf07
+  __TEXT.__oslogstring: 0xc532
   __TEXT.__gcc_except_tab: 0x1404
-  __TEXT.__swift5_typeref: 0x9968
+  __TEXT.__swift5_typeref: 0x9970
   __TEXT.__swift5_fieldmd: 0xb950
   __TEXT.__constg_swiftt: 0xd868
   __TEXT.__swift5_builtin: 0x230

   __TEXT.__swift_as_entry: 0xefc
   __TEXT.__swift_as_ret: 0x11d0
   __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x117d0
-  __TEXT.__eh_frame: 0x2e1a4
+  __TEXT.__unwind_info: 0x117e8
+  __TEXT.__eh_frame: 0x2e1ec
   __TEXT.__objc_classname: 0xdfc
-  __TEXT.__objc_methname: 0xfdff
+  __TEXT.__objc_methname: 0xfe2c
   __TEXT.__objc_methtype: 0x3639
-  __TEXT.__objc_stubs: 0x9720
+  __TEXT.__objc_stubs: 0x97a0
   __DATA_CONST.__got: 0x1898
   __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__objc_classlist: 0xb78
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4720
+  __DATA_CONST.__objc_selrefs: 0x4740
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x340
-  __DATA_CONST.__objc_arraydata: 0x480
+  __DATA_CONST.__objc_arraydata: 0x488
   __AUTH_CONST.__auth_got: 0x2aa8
   __AUTH_CONST.__const: 0x12ea8
-  __AUTH_CONST.__cfstring: 0x5020
+  __AUTH_CONST.__cfstring: 0x5100
   __AUTH_CONST.__objc_const: 0x19a98
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_arrayobj: 0x210

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB5E33CE-AC02-3001-9C78-9B4C1D8F52A5
-  Functions: 19101
-  Symbols:   13500
-  CStrings:  9032
+  UUID: B895DDA2-201B-323C-B60A-BA90D4994009
+  Functions: 19106
+  Symbols:   13521
+  CStrings:  9053
 
Symbols:
+ -[MKMessageMigrator deleteKV:]
+ -[MKMessageMigrator deleteKV:].cold.1
+ -[MKMessageMigrator deleteKV:].cold.2
+ -[MKMessageMigrator deleteKV]
+ -[MKMessageMigrator dropTrigger:]
+ -[MKMessageMigrator dropTrigger:].cold.1
+ -[MKMessageMigrator dropTrigger:].cold.2
+ -[MKMessageMigrator dropTriggers]
+ _objc_msgSend$_import:
+ _objc_msgSend$deleteKV
+ _objc_msgSend$deleteKV:
+ _objc_msgSend$dropTrigger:
+ _objc_msgSend$dropTriggers
+ _symbolic _____Sg 6IMCore12ImportExportO11ParticipantV
- _objc_msgSend$_import2:
CStrings:
+ "DELETE FROM kvtable WHERE key = ?"
+ "DROP TRIGGER IF EXISTS %@"
+ "chatLookupVersion"
+ "chatVersion"
+ "deleteKV"
+ "deleteKV:"
+ "dropTrigger:"
+ "dropTriggers"
+ "failed to create a particiant and will skip it"
+ "is_filtered"
+ "verify_chat_insert"
+ "verify_chat_update"
+ "will create a participant. address=%s, is_self=%{bool}d, sequence_id=%lld, service=%s"
+ "will feed participants to IMCore. participant_count=%ld"

```

## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-5168.60.14.0.0
-  __TEXT.__text: 0x3031d8
+5168.60.18.0.0
+  __TEXT.__text: 0x303618
   __TEXT.__objc_methlist: 0x1c20c
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x84a28
-  __TEXT.__oslogstring: 0x3ef0f
+  __TEXT.__cstring: 0x84a7a
+  __TEXT.__oslogstring: 0x3efd7
   __TEXT.__gcc_except_tab: 0x17c1c
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xd588
+  __TEXT.__unwind_info: 0xd5a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf330
+  __DATA_CONST.__objc_selrefs: 0xf338
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x968
   __DATA_CONST.__objc_arraydata: 0xeb8
-  __DATA_CONST.__got: 0x17c0
-  __AUTH_CONST.__const: 0x2d28
-  __AUTH_CONST.__cfstring: 0x23b20
+  __DATA_CONST.__got: 0x17c8
+  __AUTH_CONST.__const: 0x2d78
+  __AUTH_CONST.__cfstring: 0x23b40
   __AUTH_CONST.__objc_const: 0x423a8
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__auth_got: 0xda0
+  __AUTH_CONST.__auth_got: 0xdb0
   __AUTH.__objc_data: 0x2698
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x2054

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14328
-  Symbols:   18408
-  CStrings:  12270
+  Functions: 14336
+  Symbols:   18415
+  CStrings:  12275
 
Symbols:
+ -[PQLConnection(BRCAdditions) registerFunction:nArgs:directOnly:handler:error:]
+ _NSFileProviderCloudDocsContainerIdentifier
+ ___br_reingest_cloudocs_container_fixup_block_invoke
+ _br_reingest_cloudocs_container_fixup
+ _br_update_tables_34_105
+ _brc_destroy_xfunc
+ _brc_invoke_xfunc
+ _sqlite3_create_function_v2
+ _sqlite3_user_data
- -[PQLConnection(BRCAdditions) registerFunction:nArgs:handler:error:]
- GCC_except_table211
CStrings:
+ "-[PQLConnection(BRCAdditions) registerFunction:nArgs:directOnly:handler:error:]"
+ "[CRIT] Assertion failed: self.dbHandle%@"
+ "[DEBUG] Done force ingestion of the CloudDocs container to update its capabilities%@"
+ "[ERROR] Force ingestion of the CloudDocs container failed with error %@%@"
+ "br_reingest_cloudocs_container_fixup_block_invoke"
+ "connection is closed"
- "-[PQLConnection(BRCAdditions) registerFunction:nArgs:handler:error:]"
```

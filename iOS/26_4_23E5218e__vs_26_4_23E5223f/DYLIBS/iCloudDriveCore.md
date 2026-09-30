## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4479.100.89.0.3
-  __TEXT.__text: 0x3215a0
+4479.100.98.0.2
+  __TEXT.__text: 0x321658
   __TEXT.__auth_stubs: 0x1a90
-  __TEXT.__objc_methlist: 0x1aa64
+  __TEXT.__objc_methlist: 0x1aa7c
   __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x7dfe2
+  __TEXT.__cstring: 0x7e0ab
   __TEXT.__oslogstring: 0x3b6dc
   __TEXT.__gcc_except_tab: 0x19f70
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0xa7e0
+  __TEXT.__unwind_info: 0xa7e8
   __TEXT.__objc_classname: 0x2ae4
-  __TEXT.__objc_methname: 0x45bbe
+  __TEXT.__objc_methname: 0x45c08
   __TEXT.__objc_methtype: 0x94d2
-  __TEXT.__objc_stubs: 0x2fc60
+  __TEXT.__objc_stubs: 0x2fca0
   __DATA_CONST.__got: 0x1728
   __DATA_CONST.__const: 0x9500
   __DATA_CONST.__objc_classlist: 0xa58
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeaf8
+  __DATA_CONST.__objc_selrefs: 0xeb08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x910
   __DATA_CONST.__objc_arraydata: 0xe98
   __AUTH_CONST.__auth_got: 0xd58
-  __AUTH_CONST.__const: 0x2bc0
-  __AUTH_CONST.__cfstring: 0x229c0
-  __AUTH_CONST.__objc_const: 0x3d8e8
+  __AUTH_CONST.__const: 0x2bd0
+  __AUTH_CONST.__cfstring: 0x22a00
+  __AUTH_CONST.__objc_const: 0x3d8f8
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6854D774-36C4-3DE1-84F8-3AB896D26E5D
-  Functions: 13775
-  Symbols:   45365
-  CStrings:  27846
+  UUID: B009B0A0-B25D-31D0-A84D-8ACB652CC74D
+  Functions: 13778
+  Symbols:   45373
+  CStrings:  27852
 
Symbols:
+ -[BRCPQLConnection flushWithoutPersonaCheck]
+ -[BRCUserDefaults skipEvictUploadedItemsForUninstalledAppLibraries]
+ GCC_except_table300
+ ___42-[BRCAppLibrary _activateState:origState:]_block_invoke.36
+ ___block_literal_global.2265
+ ___block_literal_global.2291
+ ___block_literal_global.2313
+ ___block_literal_global.2322
+ ___block_literal_global.2331
+ _br_update_tables_34_102
+ _objc_msgSend$flushWithoutPersonaCheck
+ _objc_msgSend$skipEvictUploadedItemsForUninstalledAppLibraries
- GCC_except_table572
- ___42-[BRCAppLibrary _activateState:origState:]_block_invoke.35
- ___block_literal_global.2262
- ___block_literal_global.2288
- ___block_literal_global.2307
- ___block_literal_global.2319
- ___block_literal_global.2328
Functions:
+ -[BRCPQLConnection flushWithoutPersonaCheck]
~ -[BRCAppLibrary _activateState:origState:] : 1812 -> 1852
+ _br_update_tables_34_102
+ -[BRCUserDefaults skipEvictUploadedItemsForUninstalledAppLibraries]
CStrings:
+ "CREATE INDEX \"client_sync_up/sync_up_enumerator\" ON client_sync_up(zone_rowid, retry_count) WHERE throttle_state = 50 AND in_flight_diffs IS NULL"
+ "flushWithoutPersonaCheck"
+ "skip-evict-uploaded-items-for-uninstalled-AppLibraries"
+ "skipEvictUploadedItemsForUninstalledAppLibraries"

```

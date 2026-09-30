## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x325a0c
+  __TEXT.__text: 0x325b34
   __TEXT.__auth_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x1ac2c
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x7f189
+  __TEXT.__cstring: 0x7f3ff
   __TEXT.__oslogstring: 0x3bb17
   __TEXT.__gcc_except_tab: 0x1a1a4
   __TEXT.__ustring: 0x36

   __TEXT.__objc_methtype: 0x9570
   __TEXT.__objc_stubs: 0x2fee0
   __DATA_CONST.__got: 0x1730
-  __DATA_CONST.__const: 0x96e8
+  __DATA_CONST.__const: 0x9748
   __DATA_CONST.__objc_classlist: 0xa68
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x2a0

   __DATA_CONST.__objc_arraydata: 0xea0
   __AUTH_CONST.__auth_got: 0xd50
   __AUTH_CONST.__const: 0x2bc0
-  __AUTH_CONST.__cfstring: 0x22f00
+  __AUTH_CONST.__cfstring: 0x22f20
   __AUTH_CONST.__objc_const: 0x3e1f8
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__objc_arrayobj: 0x270

   - /usr/lib/libz.1.dylib
   Functions: 13822
   Symbols:   23882
-  CStrings:  23121
+  CStrings:  23128
 
Functions:
~ -[BRCClientDatabaseFacade getSyncStatusBitMask] : 812 -> 1108
CStrings:
+ "SELECT COUNT(*), COALESCE(SUM(si.recursive_child_count), 0) FROM client_items AS ci INNER JOIN server_items AS si ON ci.item_id = si.item_id AND ci.zone_rowid = si.zone_rowid WHERE ci.item_localsyncupstate = 4   AND ci.item_min_supported_os_rowid IS NULL   AND ci.item_state = 1   AND ci.item_trash_put_back_parent_id IS NOT NULL   AND si.item_trash_put_back_parent_id IS NOT NULL"
+ "SELECT COUNT(*), SUM(item_type IN (0, 9, 10)) FROM client_items WHERE item_localsyncupstate = 4   AND item_min_supported_os_rowid IS NULL   AND item_state = 1"
+ "tombstoneNeedsSyncUpInTrash"
+ "tombstoneNeedsSyncUpInTrashMoreThan25Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan50Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan75Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan90Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan95Percent"
- "SELECT COUNT(*) FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 4 AND item_state = 1 AND NOT item_id_is_documents(item_id) LIMIT 1"
```

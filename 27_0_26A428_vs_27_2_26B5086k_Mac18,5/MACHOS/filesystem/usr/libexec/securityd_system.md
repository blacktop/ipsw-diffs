## securityd_system

> `/usr/libexec/securityd_system`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x3fd8c
+62460.40.49.501.1
+  __TEXT.__text: 0x406c8
   __TEXT.__auth_stubs: 0x1aa0
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0xf44
   __TEXT.__const: 0x270
   __TEXT.__objc_classname: 0x2f6
   __TEXT.__objc_methtype: 0xcb2
-  __TEXT.__cstring: 0x868d
+  __TEXT.__cstring: 0x896d
   __TEXT.__objc_methname: 0x207f
-  __TEXT.__oslogstring: 0x4330
+  __TEXT.__oslogstring: 0x4369
   __TEXT.__gcc_except_tab: 0x304
-  __TEXT.__unwind_info: 0x1080
-  __DATA_CONST.__const: 0xb558
-  __DATA_CONST.__cfstring: 0x7fc0
+  __TEXT.__unwind_info: 0x1098
+  __DATA_CONST.__const: 0xb5f0
+  __DATA_CONST.__cfstring: 0x8120
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__auth_got: 0xd60
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1ba8
   __DATA.__objc_selrefs: 0x948
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x690
-  __DATA.__data: 0x1580
+  __DATA.__data: 0x1588
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x10
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1130
-  Symbols:   728
-  CStrings:  2113
+  Functions: 1137
+  Symbols:   732
+  CStrings:  2126
 
Symbols:
+ _kSecItemCountNonSyncableLive
+ _kSecItemCountNonSyncableTombstone
+ _kSecItemCountSyncableLive
+ _kSecItemCountSyncableTombstone
CStrings:
+ " AND agrp IN (?"
+ " GROUP BY agrp"
+ " WHERE agrp IN (?"
+ " WHERE musr = ?"
+ "CREATE INDEX IF NOT EXISTS cert_agrp_musr_sync_tomb ON cert(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS genp_agrp_musr_sync_tomb ON genp(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS inet_agrp_musr_sync_tomb ON inet(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS keys_agrp_musr_sync_tomb ON keys(agrp, musr, sync, tomb);"
+ "SELECT agrp, SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) FROM %@"
+ "SecServerItemCountAllWithAccessGroups query template: %@"
+ "accessGroups must be a non-empty CFArray, got %@"
+ "applicationID"
+ "item-counts"
+ "sec_count_all_with_access_groups_id"
- "unknown"
```

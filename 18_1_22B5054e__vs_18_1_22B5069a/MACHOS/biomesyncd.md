## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-153.9.0.1.0
-  __TEXT.__text: 0x448c8
+153.10.0.0.0
+  __TEXT.__text: 0x44d30
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x7780
-  __TEXT.__objc_methlist: 0x354c
+  __TEXT.__objc_stubs: 0x77e0
+  __TEXT.__objc_methlist: 0x356c
   __TEXT.__const: 0x10c8
-  __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__objc_methname: 0x954f
-  __TEXT.__cstring: 0x4a20
+  __TEXT.__gcc_except_tab: 0x9a4
+  __TEXT.__objc_methname: 0x95b0
+  __TEXT.__cstring: 0x4a62
   __TEXT.__objc_classname: 0x844
   __TEXT.__objc_methtype: 0x18e7
-  __TEXT.__oslogstring: 0x520a
-  __TEXT.__unwind_info: 0xed8
+  __TEXT.__oslogstring: 0x534b
+  __TEXT.__unwind_info: 0xee8
   __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0xff0
-  __DATA_CONST.__cfstring: 0x4100
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0xff8
+  __DATA_CONST.__cfstring: 0x4140
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x8000
-  __DATA.__objc_selrefs: 0x2490
+  __DATA.__objc_const: 0x8010
+  __DATA.__objc_selrefs: 0x24a0
   __DATA.__objc_ivar: 0x3d0
   __DATA.__objc_data: 0x1130
   __DATA.__data: 0x8a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1493
-  Symbols:   342
-  CStrings:  2899
+  Functions: 1496
+  Symbols:   344
+  CStrings:  2908
 
Symbols:
+ _NSDebugDescriptionErrorKey
+ __os_log_default
CStrings:
+ "BMSyncDatabase%!@(MISSING) clearing cached statements"
+ "BMSyncDatabaseErrorDomain"
+ "Could not enable WAL and foreign_keys on sync database"
+ "Failed to decode CKDistributedSiteIdentifier from site %!@(MISSING)"
+ "T@\"BMDistributedSyncMultiStreamManager\",R,N,V_primarySyncManager"
+ "_tryLogSqliteColumnError:"
+ "activeLocationsInClockVector:inStream:error:"
+ "error fetching active locations for clockVector: %!@(MISSING) stream: %!@(MISSING) error: %!@(MISSING)"
+ "fmdb: error: %!@(MISSING) errCode: %!u(MISSING) extendedErrCode: %!u(MISSING) while fetching column %!u(MISSING) for statement: %!@(MISSING)"
+ "primarySyncManager"
+ "received nil CRDTLocation while enumerating active locations for stream: %!@(MISSING)"
- "activeLocationsInClockVector:inStream:enumerateWithBlock:"
- "v24@?0@\"BMSyncCRDTLocationRow\"8^B16"

```

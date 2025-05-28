## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-123.9.0.1.0
-  __TEXT.__text: 0x40d04
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x7340
-  __TEXT.__objc_methlist: 0x3314
+123.10.0.1.0
+  __TEXT.__text: 0x41074
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__objc_methlist: 0x334c
   __TEXT.__const: 0x1038
-  __TEXT.__objc_methname: 0x90cf
-  __TEXT.__oslogstring: 0x4e9a
-  __TEXT.__cstring: 0x45df
-  __TEXT.__objc_classname: 0x6f3
+  __TEXT.__objc_methname: 0x914f
+  __TEXT.__oslogstring: 0x4ee3
+  __TEXT.__cstring: 0x461c
+  __TEXT.__objc_classname: 0x709
   __TEXT.__objc_methtype: 0x161f
   __TEXT.__gcc_except_tab: 0x6bc
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xe5c
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0xe54
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__cfstring: 0x3ae0
+  __DATA_CONST.__cfstring: 0x3b40
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x3d0
+  __DATA_CONST.__objc_classrefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x4a8
   __DATA_CONST.__objc_arrayobj: 0x708
-  __DATA_CONST.__objc_intobj: 0x1f8
+  __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x62f8
-  __DATA.__objc_selrefs: 0x2378
+  __DATA.__objc_selrefs: 0x23a0
   __DATA.__objc_ivar: 0x384
   __DATA.__objc_data: 0x1090
   __DATA.__data: 0x600

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1457
-  Symbols:   331
-  CStrings:  2761
+  Functions: 1461
+  Symbols:   334
+  CStrings:  2772
 
Symbols:
+ _BMUseCaseNone
+ _OBJC_CLASS_$_BMAccountManager
+ _dispatch_get_current_queue
CStrings:
+ "BMSyncDatabase+Creation.m"
+ "MetricsCollectionTask"
+ "Migrating database to version %u"
+ "accounts"
+ "enumerateAccountSpecificDatabasesWithBlock:"
+ "failed to open database for account: %@"
+ "migration_Schema27ToSchema28"
+ "runMetricsCollectionTask:"
+ "runVacuumingTask:"

```

## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-166.22.1.100.0
-  __TEXT.__text: 0x4d76c
+166.23.0.1.0
+  __TEXT.__text: 0x4d954
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x44cc
+  __TEXT.__objc_methlist: 0x44dc
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x1128
-  __TEXT.__cstring: 0x392d
-  __TEXT.__oslogstring: 0x4725
+  __TEXT.__cstring: 0x3968
+  __TEXT.__oslogstring: 0x4765
   __TEXT.__dlopen_cstrs: 0x278
   __TEXT.__unwind_info: 0x1338
   __TEXT.__objc_classname: 0xac2
-  __TEXT.__objc_methname: 0x9af1
+  __TEXT.__objc_methname: 0x9b18
   __TEXT.__objc_methtype: 0x1da1
-  __TEXT.__objc_stubs: 0x6a80
-  __DATA_CONST.__got: 0x480
+  __TEXT.__objc_stubs: 0x6ac0
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__const: 0x1210
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_selrefs: 0x2300
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x508
   __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__cfstring: 0x31e0
   __AUTH_CONST.__objc_const: 0xa9e0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1784
-  Symbols:   6286
-  CStrings:  2818
+  Symbols:   6295
+  CStrings:  2823
 
Symbols:
+ +[CCDataResource _databaseExistsAtURL:error:]
+ -[CCDataResource databaseFileExists:]
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:]
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.1
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.2
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.3
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.4
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.5
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.6
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.7
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.8
+ -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.9
+ -[CCSetsAccessDaemonDelegate incrementResourceGenerationCounter].cold.2
+ _NSLocalizedFailureReasonErrorKey
+ _objc_msgSend$_createDatabaseWithLocalDeviceSite:
+ _objc_msgSend$_databaseExistsAtURL:error:
+ _objc_msgSend$databaseFileExists:
+ _objc_msgSend$localizedFailureReason
- +[CCDataResource databaseExistsAtURL:]
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:]
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.1
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.10
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.2
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.3
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.4
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.5
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.6
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.7
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.8
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.9
- _objc_msgSend$_createDatabaseIfNotExistsWithLocalDeviceSite:
- _objc_msgSend$databaseExistsAtURL:
CStrings:
+ "%@ Could not prepare resource: %@"
+ "%@ Prepared resource: %@"
+ "%@ Resource %@ has not been prepared yet (%@)"
+ "%@ Resource generation counter incremented to %@"
+ "(%@) Database not found: %@"
+ "Database does not exist at path: %s error: %s"
+ "Database: %s"
+ "_createDatabaseWithLocalDeviceSite:"
+ "_databaseExistsAtURL:error:"
+ "databaseFileExists:"
+ "localizedFailureReason"
- "(%@) Database already exists at path: %@"
- "(%@) Database not found"
- "Could not prepare resource: %@"
- "Prepared resource: %@"
- "_createDatabaseIfNotExistsWithLocalDeviceSite:"
- "databaseExistsAtURL:"

```

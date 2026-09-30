## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-154.1.4.0.0
-  __TEXT.__text: 0x7f150
-  __TEXT.__objc_methlist: 0x641c
+154.1.5.0.0
+  __TEXT.__text: 0x80014
+  __TEXT.__objc_methlist: 0x6484
   __TEXT.__const: 0xac0
   __TEXT.__gcc_except_tab: 0xe0c
-  __TEXT.__cstring: 0x67f2
-  __TEXT.__oslogstring: 0x7f20
+  __TEXT.__cstring: 0x69c2
+  __TEXT.__oslogstring: 0x8270
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__constg_swiftt: 0x164
   __TEXT.__swift5_fieldmd: 0x88

   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x40
   __TEXT.__swift5_capture: 0x98
-  __TEXT.__unwind_info: 0x2038
+  __TEXT.__unwind_info: 0x2098
   __TEXT.__eh_frame: 0x658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1890
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__const: 0x18b8
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32e0
+  __DATA_CONST.__objc_selrefs: 0x3330
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x1958
-  __AUTH_CONST.__const: 0x15f8
-  __AUTH_CONST.__cfstring: 0x6ea0
-  __AUTH_CONST.__objc_const: 0xa7b0
-  __AUTH_CONST.__objc_intobj: 0x18f0
+  __DATA_CONST.__got: 0x1968
+  __AUTH_CONST.__const: 0x1638
+  __AUTH_CONST.__cfstring: 0x6fa0
+  __AUTH_CONST.__objc_const: 0xa858
+  __AUTH_CONST.__objc_intobj: 0x1968
   __AUTH_CONST.__objc_arrayobj: 0x4f8
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0xb78
+  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH.__objc_data: 0xbc8
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x74c
   __DATA.__data: 0x548

   __DATA_DIRTY.__bss: 0x650
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2902
-  Symbols:   986
-  CStrings:  1542
+  Functions: 2923
+  Symbols:   989
+  CStrings:  1562
 
Symbols:
+ _CBCentralManagerOptionShowPowerAlertKey
+ _OBJC_CLASS_$_CBCentralManager
+ _objc_retain_x6
CStrings:
+ "A1603"
+ "A2051"
+ "A2538"
+ "A3085"
+ "BEGIN TRANSACTION;DROP TABLE IF EXISTS %1$@;CREATE TABLE %1$@ (date TEXT NOT NULL, pencilVersion INTEGER NOT NULL, usageType INTEGER NOT NULL, appInfo TEXT NOT NULL, inUseDisplay INTEGER NOT NULL, activeMinutes INTEGER, activeSeconds INTEGER, lastActivityTimestamp INTEGER, PRIMARY KEY (date, pencilVersion, usageType, appInfo, inUseDisplay));COMMIT;"
+ "Cannot migrate the pencil usage table: no database."
+ "Column lookup for the pencil usage table migration returned no row: %{private}s"
+ "Could not determine the pencil usage table's on-disk version. Leaving the table alone."
+ "Failed to bind the column name for the pencil usage table migration: %{private}s"
+ "Failed to get pencil version from CoreBluetooth. Falling back to the self.pencilVersion (last known pencil version)."
+ "Failed to migrate the pencil usage table to v2 with error %{private}s"
+ "Failed to prepare the column lookup for the pencil usage table migration: %{private}s"
+ "Migrated the pencil usage table to v2 (dropped the old table, added the inUseDisplay column)."
+ "No Apple Pencil among the %lu paired bluetooth device(s)."
+ "No migration defined to take the pencil usage table to version %ld."
+ "ROLLBACK;"
+ "SELECT COUNT(*) FROM pragma_table_info('%@') WHERE name = ?"
+ "inUseDisplay"
+ "pairedPencilVersion failed to get a pairing agent."
+ "pairingState"
```

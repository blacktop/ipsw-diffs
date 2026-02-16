## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-858.0.5.0.0
-  __TEXT.__text: 0x66464
-  __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_stubs: 0x9260
-  __TEXT.__objc_methlist: 0x44dc
-  __TEXT.__cstring: 0xc7ab
+858.0.7.0.0
+  __TEXT.__text: 0x6ae60
+  __TEXT.__auth_stubs: 0x1490
+  __TEXT.__objc_stubs: 0x93a0
+  __TEXT.__objc_methlist: 0x4614
+  __TEXT.__cstring: 0xc8a0
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x1b70
-  __TEXT.__objc_methname: 0xf573
-  __TEXT.__oslogstring: 0xb288
-  __TEXT.__objc_classname: 0x5df
-  __TEXT.__objc_methtype: 0x1e2f
+  __TEXT.__gcc_except_tab: 0x1d70
+  __TEXT.__objc_methname: 0xf68f
+  __TEXT.__oslogstring: 0xb31c
+  __TEXT.__objc_classname: 0x5f0
+  __TEXT.__objc_methtype: 0x1e6f
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x1418
-  __DATA_CONST.__auth_got: 0xa90
+  __TEXT.__unwind_info: 0x16e8
+  __DATA_CONST.__auth_got: 0xa58
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x1ed0
-  __DATA_CONST.__cfstring: 0x6f00
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__const: 0x1e68
+  __DATA_CONST.__cfstring: 0x6fe0
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x4f8
-  __DATA_CONST.__objc_arraydata: 0x1188
-  __DATA_CONST.__objc_dictobj: 0xd48
+  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_intobj: 0x510
+  __DATA_CONST.__objc_arraydata: 0x1200
+  __DATA_CONST.__objc_dictobj: 0xdc0
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_const: 0x8728
-  __DATA.__objc_selrefs: 0x2cc0
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__objc_data: 0x1040
+  __DATA.__objc_const: 0x8c60
+  __DATA.__objc_selrefs: 0x2d08
+  __DATA.__objc_ivar: 0x5f4
+  __DATA.__objc_data: 0x1090
   __DATA.__data: 0x660
   __DATA.__bss: 0x389
   __DATA.__common: 0x28

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8C115758-B0A1-39F1-A9D8-EC1678CD4CA5
-  Functions: 2333
-  Symbols:   469
-  CStrings:  5624
+  UUID: ABB06E52-66C6-3B68-B926-21326EC77BF2
+  Functions: 2364
+  Symbols:   462
+  CStrings:  5659
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "-[TCCDMainDatabase migration:]"
+ "@\"TCCDMainDatabase\""
+ "@\"TCCDSQLDatabase\""
+ "AccessoryNotifications"
+ "D5834418-332F-481C-B7DE-7E80973B07BF"
+ "DELETE FROM access WHERE service = 'kTCCServicePhotos' AND auth_value = 3"
+ "E7B1CD81-332F-481C-B7DE-7E80973B07BF"
+ "Failed to commit due to nil db for %@"
+ "SELECT COUNT(*) FROM access"
+ "T@\"TCCDMainDatabase\",&,V_database"
+ "T@\"TCCDSQLDatabase\",&,V_sqlDatabase"
+ "TCCDMainDatabase"
+ "TCCDMainDatabase created for path: %@ "
+ "_createDatabase:initialSetup:"
+ "_database"
+ "_migrateDatabaseVersFrom15To16"
+ "_sqlDatabase"
+ "client_count"
+ "currentDatabaseVersion"
+ "currentDatabaseVersionLocked"
+ "database"
+ "graphic-icon.notifications"
+ "i24@0:8@16"
+ "i32@0:8@16@24"
+ "initWithDatabasePath:initialSQL:"
+ "kTCCServiceAccessoryAutomaticAudioSwitching"
+ "kTCCServiceAccessoryLiveActivities"
+ "kTCCServiceSensorKitHeadphoneMotion"
+ "migration:"
+ "setDatabase:"
+ "setSqlDatabase:"
+ "sqlDatabase"
+ "tccd MainDatabase closed"
+ "tccd MainDatabase opened"
+ "tccd migration setup"
- "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
- "E7B1CD81-445C-4840-9F24-3A32B510B6A1"
- "_createDatabase"
- "_db_eval"
- "com.apple.tcc.db_queue"
- "db_open"
- "failed to create db_queue"

```

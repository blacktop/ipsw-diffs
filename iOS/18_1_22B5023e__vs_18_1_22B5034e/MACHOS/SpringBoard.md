## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

```diff

-4496.1.1.0.0
-  __TEXT.__text: 0xcedc
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x14f9
+4501.0.0.0.0
+  __TEXT.__text: 0xcf58
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x1940
+  __TEXT.__objc_methlist: 0x4e4
+  __TEXT.__cstring: 0x14de
   __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x1993
+  __TEXT.__objc_methname: 0x1945
   __TEXT.__oslogstring: 0x1136
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x310
+  __TEXT.__unwind_info: 0x238
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1218
-  __DATA_CONST.__cfstring: 0xd20
+  __DATA_CONST.__const: 0x1238
+  __DATA_CONST.__cfstring: 0xd00
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xf58
-  __DATA.__objc_selrefs: 0x728
+  __DATA.__objc_selrefs: 0x718
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
-  __DATA.__bss: 0x260
+  __DATA.__bss: 0x270
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x590
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 405
-  Symbols:   347
-  CStrings:  648
+  Symbols:   346
+  CStrings:  646
 
Symbols:
+ _SBLogShellScene
- _WGTodayViewArchiveMigrateArchiveFromLegacy
- _WGWidgetPersistentStateResetHasContent
CStrings:
+ "ShellScene"
- "com.apple.BatteryCenter.BatteryWidget"
- "performBatteryWidgetMigration"
- "performNotificationCenterTodayViewDataMigration"

```

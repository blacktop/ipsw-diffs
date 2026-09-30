## CalendarMigration

> `/System/Library/PrivateFrameworks/CalendarMigration.framework/Versions/A/CalendarMigration`

```diff

-1253.3.2.0.0
-  __TEXT.__text: 0x31684
+1253.5.4.0.0
+  __TEXT.__text: 0x319cc
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x24ec
+  __TEXT.__objc_methlist: 0x2b5c
   __TEXT.__const: 0x148
   __TEXT.__cstring: 0x32ac
-  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__gcc_except_tab: 0x58c
   __TEXT.__oslogstring: 0x5418
   __TEXT.__dlopen_cstrs: 0x150
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__unwind_info: 0xa40
   __TEXT.__objc_classname: 0x917
   __TEXT.__objc_methname: 0x8bbf
   __TEXT.__objc_methtype: 0x1868

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e8
+  __DATA_CONST.__objc_selrefs: 0x1a78
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0x8b0
   __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x5f30
+  __AUTH_CONST.__objc_const: 0x53b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xe60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F3526F7E-2D15-3213-8399-66DD15F74644
-  Functions: 1024
-  Symbols:   3163
+  UUID: 700B121B-A6E5-35B4-8477-E462C010484E
+  Functions: 1036
+  Symbols:   3164
   CStrings:  2396
 
Symbols:
+ +[CalDefaultCalendarMigrationDefaultsProvider sharedInstance].cold.1
+ +[CalDefaultMigrationABCReporter sharedInstance].cold.1
+ +[CalDefaultMigrationAnalyticsSender sharedInstance].cold.1
+ +[CalDefaultReminderKitProvider sharedInstance].cold.1
+ +[CalDefaultReminderMigrationDefaultsProvider sharedInstance].cold.1
+ +[CalMigrationLog calendar].cold.1
+ +[CalMigrationLog defaultCategory].cold.1
+ +[CalMigrationLog reminders].cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11

```

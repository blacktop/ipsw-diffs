## CallHistoryDataMigrator

> `/System/Library/DataClassMigrators/CallHistoryDataMigrator.migrator/CallHistoryDataMigrator`

```diff

-1253.100.1.0.0
+1255.100.11.0.0
   __TEXT.__text: 0xa00
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x3a0

   __TEXT.__gcc_except_tab: 0x40
   __TEXT.__objc_methname: 0x475
   __TEXT.__cstring: 0xf5
-  __TEXT.__oslogstring: 0x103
+  __TEXT.__oslogstring: 0x123
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methtype: 0x132
   __TEXT.__unwind_info: 0xa0
CStrings:
+ "Removing user defaults related to the current iCloud container %!{(MISSING)public}@"
+ "Removing user defaults related to the legacy iCloud container %!{(MISSING)public}@"
+ "Reset call timers request completed %!{(MISSING)public}@"
+ "Reset call timers request failed due to connection error %!{(MISSING)public}@"
- "Removing user defaults related to the current iCloud container %!@(MISSING)"
- "Removing user defaults related to the legacy iCloud container %!@(MISSING)"
- "Reset call timers request completed %!@(MISSING)"
- "Reset call timers request failed due to connection error %!@(MISSING)"

```

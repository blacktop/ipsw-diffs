## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1251.0.0.0.0
-  __TEXT.__text: 0xd7b54
-  __TEXT.__auth_stubs: 0x1f90
+1252.0.0.0.0
+  __TEXT.__text: 0xd8f54
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x19f0
-  __TEXT.__cstring: 0x1dfe9
+  __TEXT.__cstring: 0x1e053
   __TEXT.__const: 0x74c
-  __TEXT.__gcc_except_tab: 0x1880
-  __TEXT.__oslogstring: 0xc122
+  __TEXT.__gcc_except_tab: 0x19a8
+  __TEXT.__oslogstring: 0xc6e9
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x2b88
+  __TEXT.__unwind_info: 0x2b98
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8cea
+  __TEXT.__objc_methname: 0x8dad
   __TEXT.__objc_methtype: 0x4513
-  __TEXT.__objc_stubs: 0x8100
-  __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0xdff8
+  __TEXT.__objc_stubs: 0x8240
+  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__const: 0xe020
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2398
+  __DATA_CONST.__objc_selrefs: 0x23e8
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xfd8
+  __AUTH_CONST.__auth_got: 0xfd0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x2150
-  __AUTH_CONST.__cfstring: 0xc520
+  __AUTH_CONST.__cfstring: 0xc560
   __AUTH_CONST.__objc_const: 0x3cb0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x820
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x700
-  __DATA.__bss: 0x2d0
+  __DATA.__bss: 0x2c8
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__data: 0x250
+  __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4117
-  Symbols:   5608
-  CStrings:  4624
+  Functions: 4120
+  Symbols:   5615
+  CStrings:  4660
 
Symbols:
+ _NSCocoaErrorDomain
+ _CDBAppEntityHandle
+ _EKWeakLinkClass
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_CalRateLimitingQueue
+ _CalDatabasePerformMigrationBetweenDirectoriesIfNeeded
+ _CDBGroupContainerMigrationHandle
+ _NSURLIsPackageKey
- _dispatch_time
- _dispatch_after
- _kCalCalendarDirectoryRelativeToHome
CStrings:
+ "/Library/Calendar/"
+ "notifyObservers"
+ "App Entity Observation: no observers"
+ "domain"
+ "Notifying app entity observers because of changeType %!{(MISSING)public}@ for event"
+ "executeBlock"
+ "Notifying app entity observers for changeType %!{(MISSING)public}@ because store has dirty instance attributes"
+ "_CalDatabaseChangesMayAffectAppEntities: failed to get recordID for updated record with rowid [%!d(MISSING)], deleted: %!{(MISSING)BOOL}d"
+ "Skipping migrating file %!{(MISSING)public}@ because the file already exists in the destination"
+ "Skipping migration because %!@(MISSING) is already migrated"
+ "Error migrating %!{(MISSING)public}@: %!@(MISSING)"
+ "Finished migration. Successfully moved %!i(MISSING) files. Skipped %!i(MISSING) files or directories that already existed in the destination directory. Skipped %!i(MISSING) subdirectories. Failed to move %!i(MISSING) files."
+ "Notifying app entity observers because of changeType %!{(MISSING)public}@ for recurrence rule"
+ "Beginning migration of up to %!l(MISSING)u directories and %!l(MISSING)u files from %!@(MISSING) to %!@(MISSING)"
+ "Error removing source directory %!{(MISSING)public}@: %!@(MISSING)"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1932"
+ "Migrated file %!{(MISSING)public}@"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4788"
+ "Notifying app entity observers because of changeType %!{(MISSING)public}@ for color"
+ "isObserved"
+ "checkResourceIsReachableAndReturnError:"
+ "CalendarLinkAppEntityNotifier"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3052"
+ "Notifying app entity observers for changeType %!{(MISSING)public}@ because calendar has dirty instance attributes"
+ "relativePath"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1888"
+ "Error migrating %!{(MISSING)public}@; encountered error for %!@(MISSING): %!@(MISSING)"
+ "Skipped unexpected file %!@(MISSING)"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2815"
+ "Error migrating: can't create new directory %!@(MISSING): %!@(MISSING)"
+ "sharedNotifier"
+ "AppEntity"
+ "initWithQueue:minimumInterval:andBlock:"
+ "Removed successfully migrated directory %!{(MISSING)public}@"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3080"
+ "GroupContainerMigration"
+ "app_entity_observation"
+ "Beginning migration for directory %!{(MISSING)public}@"
+ "resourceValuesForKeys:error:"
+ "Skipped removing migrated directory %!{(MISSING)public}@ because there are unmigrated files in it"
+ "nextObject"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3054"
+ "Error migrating directory %!{(MISSING)public}@: can't create target directory: %!@(MISSING)"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1879"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3004"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4709"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1923"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2976"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2978"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2739"

```

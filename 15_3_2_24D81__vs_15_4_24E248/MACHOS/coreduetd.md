## coreduetd

> `/usr/libexec/coreduetd`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x14cc4
+1892.20.1.0.0
+  __TEXT.__text: 0x14bf4
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x3400
-  __TEXT.__objc_methlist: 0xc74
+  __TEXT.__objc_stubs: 0x33c0
+  __TEXT.__objc_methlist: 0x1080
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1440
-  __TEXT.__oslogstring: 0x1998
-  __TEXT.__objc_methname: 0x3c1e
+  __TEXT.__cstring: 0x11e5
+  __TEXT.__oslogstring: 0x19e4
+  __TEXT.__objc_methname: 0x3bf0
   __TEXT.__objc_classname: 0xff
   __TEXT.__objc_methtype: 0xe71
-  __TEXT.__gcc_except_tab: 0x304
+  __TEXT.__gcc_except_tab: 0x420
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x4b0
   __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x9d0
-  __DATA_CONST.__cfstring: 0x1140
+  __DATA_CONST.__cfstring: 0xf80
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1b28
-  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_const: 0x13b0
+  __DATA.__objc_selrefs: 0xe88
   __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 55C9D465-5ACB-31A8-B6F1-79A20ACFCC6B
-  Functions: 432
-  Symbols:   212
-  CStrings:  1232
+  UUID: D3A24900-9E93-3A24-8814-B4AB55E85ED5
+  Functions: 442
+  Symbols:   211
+  CStrings:  1202
 
Symbols:
- _OBJC_CLASS_$__CDDiagnosticDataReporter
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/CDD.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/Knowledge/CDKnowledgeDaemon.m:605"
+ "CoreDuet: CDDataMigrator dkcMigration"
+ "CoreDuet: CDDataMigrator logMigration"
+ "CoreDuet: CDDataMigrator performMigration"
+ "CoreDuet: CDDataMigrator spotlightViewerEventsMigration"
+ "CoreDuet: com.apple.coreduet.people.CDPeopleDaemon"
+ "CoreDuet: com.apple.coreduet.people.maintainPrivacy"
+ "CoreDuet: com.apple.coreduet.people.refreshPeopleSuggesterCaches"
+ "CoreDuet: com.apple.coreduet.people.repopulate"
+ "CoreDuet: com.apple.coreduetd.cloudfamily.task"
+ "CoreDuet: com.apple.coreduetd.datacollection.task"
+ "CoreDuet: com.apple.coreduetd.feedback.cna.task"
+ "CoreDuet: com.apple.coreduetd.maintainPrivacy"
+ "CoreDuet: com.apple.coreduetd.mediaanalysis.proc.task"
+ "CoreDuet: com.apple.coreduetd.populateAppSharesCache"
+ "CoreDuet: com.apple.coreduetd.populateAppUsageCache"
+ "CoreDuet: com.apple.coreduetd.populatePeopleSuggesterCaches"
+ "CoreDuet: com.apple.coreduetd.reportEventStatistics"
+ "CoreDuet: com.apple.coreduetd.reportPeopleStatistics"
+ "CoreDuet: com.apple.coreduetd.startSanitizingKnowledgeStore"
+ "reportShareSheetTimeoutWithError:"
+ "reportShareSheetTimeoutWithReply:"
- "%@.%@"
- "%@.total"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/CDD.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/Knowledge/CDKnowledgeDaemon.m:613"
- "Duet: CDDataMigrator dkcMigration"
- "Duet: CDDataMigrator logMigration"
- "Duet: CDDataMigrator performMigration"
- "Duet: CDDataMigrator spotlightViewerEventsMigration"
- "Duet: com.apple.coreduet.people.CDPeopleDaemon"
- "Duet: com.apple.coreduet.people.maintainPrivacy"
- "Duet: com.apple.coreduet.people.refreshPeopleSuggesterCaches"
- "Duet: com.apple.coreduet.people.repopulate"
- "Duet: com.apple.coreduetd.cloudfamily.task"
- "Duet: com.apple.coreduetd.datacollection.task"
- "Duet: com.apple.coreduetd.feedback.cna.task"
- "Duet: com.apple.coreduetd.maintainPrivacy"
- "Duet: com.apple.coreduetd.mediaanalysis.proc.task"
- "Duet: com.apple.coreduetd.populateAppSharesCache"
- "Duet: com.apple.coreduetd.populateAppUsageCache"
- "Duet: com.apple.coreduetd.populatePeopleSuggesterCaches"
- "Duet: com.apple.coreduetd.reportEventStatistics"
- "Duet: com.apple.coreduetd.reportPeopleStatistics"
- "Duet: com.apple.coreduetd.startSanitizingKnowledgeStore"
- "addValue:forScalarKey:"
- "com.apple.coreduet.deletedDB.knowledgebase.corrupted"
- "com.apple.coreduet.deletedDB.people.corrupted"
- "com.apple.coreduet.deletedDB.people.versionMismatched"
- "com.apple.coreduet.interactionStore"
- "com.apple.coreduet.interactionStore.databaseSize"
- "com.apple.coreduet.knowledgeStore.databaseSize"
- "com.apple.coreduet.knowledgeStore.deleteObjectsCount"
- "com.apple.coreduet.knowledgeStore.eventCount"
- "com.apple.coreduet.knowledgeStore.executeQueryCount"
- "com.apple.coreduet.knowledgeStore.saveObjectsCount"
- "com.apple.coreduet.knowledgeStore.syncDatabaseSize"
- "com.apple.coreduet.knowledgeStore.userDatabaseSize"
- "interactionCountPerMechanism"
- "setValue:forScalarKey:"
- "setValue:forScalarKey:limitingSigDigs:"

```

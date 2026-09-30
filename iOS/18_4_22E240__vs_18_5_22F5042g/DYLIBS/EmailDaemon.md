## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.500.181.2.5
-  __TEXT.__text: 0x255060
+3826.600.15.2.1
+  __TEXT.__text: 0x255d18
   __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_methlist: 0x15a6c
+  __TEXT.__objc_methlist: 0x15a8c
   __TEXT.__const: 0x1eec
-  __TEXT.__gcc_except_tab: 0x4bee4
-  __TEXT.__cstring: 0x21f17
-  __TEXT.__oslogstring: 0x190d6
+  __TEXT.__gcc_except_tab: 0x4c0b0
+  __TEXT.__cstring: 0x220c7
+  __TEXT.__oslogstring: 0x191c6
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x951

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x10630
+  __TEXT.__unwind_info: 0x105a0
   __TEXT.__eh_frame: 0xd60
   __TEXT.__objc_classname: 0x2e91
-  __TEXT.__objc_methname: 0x3986d
-  __TEXT.__objc_methtype: 0x8518
-  __TEXT.__objc_stubs: 0x24f60
-  __DATA_CONST.__got: 0x1b40
-  __DATA_CONST.__const: 0x9218
+  __TEXT.__objc_methname: 0x3996c
+  __TEXT.__objc_methtype: 0x852f
+  __TEXT.__objc_stubs: 0x25000
+  __DATA_CONST.__got: 0x1b58
+  __DATA_CONST.__const: 0x9220
   __DATA_CONST.__objc_classlist: 0x998
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb990
+  __DATA_CONST.__objc_selrefs: 0xb9a0
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x688
   __AUTH_CONST.__auth_got: 0x13c0
   __AUTH_CONST.__auth_ptr: 0x2e8
   __AUTH_CONST.__const: 0x40f8
-  __AUTH_CONST.__cfstring: 0x11360
-  __AUTH_CONST.__objc_const: 0x24a08
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__cfstring: 0x11460
+  __AUTH_CONST.__objc_const: 0x24a68
+  __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x4d0
   __AUTH.__data: 0x170
-  __DATA.__objc_ivar: 0x16c4
+  __DATA.__objc_ivar: 0x16cc
   __DATA.__data: 0x3390
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2480

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10685
-  Symbols:   11650
-  CStrings:  14554
+  Functions: 10692
+  Symbols:   11660
+  CStrings:  14574
 
Symbols:
+ _EDSearchableIndexDiagnosticsSnapshotKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyRemoteMessagesToRedonate
+ _XPC_ACTIVITY_POWER_NAP
- _OBJC_CLASS_$_EFProcessBoost
CStrings:
+ "\x055\x11\x11!#!"
+ "   SELECT message_id     FROM searchable_messages    WHERE transaction_id > :transaction      AND message_id > :after_id      AND NOT message_body_indexed ORDER BY message_id ASC    LIMIT :limit"
+ "-[EDSearchableIndexPersistence assignIndexingType:forIdentifiers:]"
+ "-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]"
+ ":after_id"
+ ":transaction"
+ "@52@0:8@16@24@32@40B48"
+ "Could not load unindexed bodies from searchable_messages table"
+ "EDClientState-%p"
+ "EDSearchableIndexPersistenceUnindexedBodies"
+ "Found %@ messages with unindexed bodies in %0.2f seconds. %@ are available locally."
+ "MessagesToRedonate"
+ "Network not available, stopping download and verification."
+ "T@\"NSDate\",R,N,V_date"
+ "T@\"NSNumber\",R,N,V_indexableMessages"
+ "T@\"NSNumber\",R,N,V_messagesIndexed"
+ "T@\"NSNumber\",R,N,V_messagesToRedonate"
+ "TB,R,N,V_turboMode"
+ "_messagesToRedonate"
+ "_redonatedItems"
+ "_sendAnalyticsForRedonatingItems:"
+ "assignIndexingType:forIdentifiers:"
+ "com.apple.mail.searchableIndex.redonateItems"
+ "duration: %g, unindexed: %llu , available: %llu"
+ "initWithDate:indexableMessages:messagesIndexed:messagesToRedonate:turboMode:"
+ "isAvailable"
+ "itemCount"
+ "messagesToRedonate"
+ "performMaintenancePreWork"
+ "queueRedonationForDownloadedMessagesWithUnindexedBodies"
+ "tokenWithLabel:invocationBlock:"
+ "\xf0R"
- "\x055\x11\x11\x11#!"
- "-[EDSearchableIndexPersistence searchableIndex:assignIndexingType:forIdentifiers:]"
- "T@\"NSNumber\",&,N,V_indexableMessages"
- "T@\"NSNumber\",&,N,V_messagesIndexed"
- "TB,N,V_turboMode"
- "drop"
- "initWithBoost:"
- "initWithDate:indexableMessages:messagesIndexed:turboMode:"
- "setIndexableMessages:"
- "setMessagesIndexed:"
- "setTurboMode:"
- "\xf0B"

```

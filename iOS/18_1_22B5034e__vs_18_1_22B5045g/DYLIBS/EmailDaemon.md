## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.200.46.2.1
-  __TEXT.__text: 0x217350
+3826.200.67.0.0
+  __TEXT.__text: 0x2189f8
   __TEXT.__auth_stubs: 0x2380
-  __TEXT.__objc_methlist: 0x11c64
-  __TEXT.__gcc_except_tab: 0x43154
+  __TEXT.__objc_methlist: 0x11d34
+  __TEXT.__gcc_except_tab: 0x435c0
   __TEXT.__const: 0x1cf8
-  __TEXT.__cstring: 0x1e547
-  __TEXT.__oslogstring: 0x15316
+  __TEXT.__cstring: 0x1e637
+  __TEXT.__oslogstring: 0x154a6
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x715

   __TEXT.__swift5_types: 0xbc
   __TEXT.__swift5_capture: 0x128
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xebe0
+  __TEXT.__unwind_info: 0xec98
   __TEXT.__eh_frame: 0x860
   __TEXT.__objc_classname: 0x2b42
-  __TEXT.__objc_methname: 0x3492a
-  __TEXT.__objc_methtype: 0x792c
-  __TEXT.__objc_stubs: 0x22040
+  __TEXT.__objc_methname: 0x34c9c
+  __TEXT.__objc_methtype: 0x7944
+  __TEXT.__objc_stubs: 0x22220
   __DATA_CONST.__got: 0x19c0
-  __DATA_CONST.__const: 0x8200
+  __DATA_CONST.__const: 0x8250
   __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa18
+  __DATA_CONST.__objc_selrefs: 0xaa98
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x630
-  __DATA_CONST.__objc_arraydata: 0x610
+  __DATA_CONST.__objc_arraydata: 0x628
   __AUTH_CONST.__auth_got: 0x11d0
   __AUTH_CONST.__auth_ptr: 0x2b8
   __AUTH_CONST.__const: 0x3828
-  __AUTH_CONST.__cfstring: 0xfee0
-  __AUTH_CONST.__objc_const: 0x248b8
-  __AUTH_CONST.__objc_intobj: 0x888
-  __AUTH_CONST.__objc_arrayobj: 0x258
+  __AUTH_CONST.__cfstring: 0xff00
+  __AUTH_CONST.__objc_const: 0x24998
+  __AUTH_CONST.__objc_intobj: 0x8d0
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x1514
+  __DATA.__objc_ivar: 0x1520
   __DATA.__data: 0x2d50
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2850

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9732
-  Symbols:   10501
-  CStrings:  13297
+  Functions: 9752
+  Symbols:   10521
+  CStrings:  13328
 
CStrings:
+ "_registerAuthStateMigrationTask"
+ "T@\"EDMessageAuthenticationStateMigrator\",&,N,V_nonInboxMessageAuthenticator"
+ "Failed to increment categorization version due to error %!{(MISSING)public}@"
+ "\x1f"
+ "-[EDCategoryPersistence prepareToChangeCategoryType:messages:]"
+ "persistenceWillChangeCategorizationForMessages:"
+ "Registering Non-Inbox Message Authentication task."
+ "Migration in progress with token:%!p(MISSING) and task %!{(MISSING)public}@. Skipping Non-Inbox message authentication."
+ "-[EDCategoryPersistence prepareToPersistCategorizationResultMap:]"
+ "%!{(MISSING)public}@ - %!{(MISSING)public}@"
+ "persistenceWillChangeCategoryForAddressIDs:"
+ "_majorAndMinorVersionFrom:"
+ "recategorizeAllMessagesIfModelVersionChangedFrom:to:"
+ "T@\"NSString\",R,V_pendingCategorizationChangesKey"
+ "countOfUserOverridesWithCompletionHandler:"
+ "persistenceDidNotChangeCategorizationForMessages:"
+ "_startNonInboxMessageAuthenticationnWithBGTask:"
+ "Starting Non-Inbox message authentication."
+ "_migrateCategoryForQuery:cancelationToken:reason:completion:"
+ "_registerCoreAnalyticsLoggerTask"
+ "migrateCategoryForQuery:cancelationToken:reason:completion:"
+ "prepareToChangeCategoryType:messages:"
+ "_registerInboxMigrationTasks"
+ "ef_cancelledError"
+ "persistenceDidNotChangeCategoryForAddressIDs:"
+ "_systemTaskLock"
+ "originalContentMessagesForPersistedMessages:condenseEmptyLines:preserveQuotedForwardedContent:htmlStringFromMessage:"
+ "pendingCategorizationChangesKey"
+ "com.apple.mail.messageauthentication"
+ "Recategorizing all messages due to model version change from %!@(MISSING) to %!@(MISSING)"
+ "prepareToPersistCategorizationResultMap:"
+ "queryForNonInboxMessagesToAuthenticate"
+ "@40@0:8@16B24B28@?32"
+ "\x12!%!\(MISSING)x19"
+ "nonInboxMessageAuthenticator"
+ "queryForInboxMessagesToAuthenticate"
+ "-[EDBusinessPersistence countOfUserOverridesWithCompletionHandler:]"
+ "v48@0:8@16@24q32@?40"
+ "BlackPearl disabled - Task %!{(MISSING)public}@ being marked as complete"
+ "_nonInboxMessageAuthenticator"
+ "_categorizeMessagesForQuery:cancelationToken:completion:"
+ "setNonInboxMessageAuthenticator:"
+ "originalContentMessageForPersistedMessage:condenseEmptyLines:preserveQuotedForwardedContent:htmlStringFromMessage:"
- "recategorizeMessageSinceDate:"
- "migrateCategoryForQuery:cancelationToken:reason:"
- "originalContentMessageForPersistedMessage:condenseEmptyLines:htmlStringFromMessage:"
- "_categorizeMessagesForQuery:cancelationToken:"
- "%!{(MISSING)public}@ - %!{(MISSING)publiC}@"
- "\x12!%!\(MISSING)x18"
- "@36@0:8@16B24@?28"
- "_migrateCategoryForQuery:cancelationToken:reason:"
- "queryForMessagesToAuthenticate"
- "predicateForMessagesNewerThanDisplayDate:"
- "\x0e"
- "originalContentMessagesForPersistedMessages:condenseEmptyLines:htmlStringFromMessage:"

```

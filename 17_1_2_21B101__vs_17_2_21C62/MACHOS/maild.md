## maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0xb6e54
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_stubs: 0x161a0
-  __TEXT.__objc_methlist: 0x95fc
-  __TEXT.__gcc_except_tab: 0x17450
-  __TEXT.__objc_methname: 0x1bcc6
-  __TEXT.__cstring: 0x7ff3
+3774.300.61.2.4
+  __TEXT.__text: 0xb7530
+  __TEXT.__auth_stubs: 0x11d0
+  __TEXT.__objc_stubs: 0x15f80
+  __TEXT.__objc_methlist: 0x94dc
+  __TEXT.__gcc_except_tab: 0x17484
+  __TEXT.__objc_methname: 0x1b9a4
+  __TEXT.__cstring: 0x8087
   __TEXT.__objc_classname: 0x1a92
-  __TEXT.__objc_methtype: 0x3899
+  __TEXT.__objc_methtype: 0x388e
   __TEXT.__const: 0x130
-  __TEXT.__oslogstring: 0x85b7
+  __TEXT.__oslogstring: 0x8683
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x66e8
-  __DATA_CONST.__auth_got: 0x8f0
+  __TEXT.__unwind_info: 0x6710
+  __DATA_CONST.__auth_got: 0x8f8
   __DATA_CONST.__got: 0xa40
   __DATA_CONST.__const: 0x47a0
   __DATA_CONST.__cfstring: 0x6d80

   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x15210
-  __DATA.__objc_selrefs: 0x6960
+  __DATA.__objc_const: 0x151b0
+  __DATA.__objc_selrefs: 0x68b0
   __DATA.__objc_protorefs: 0x68
   __DATA.__objc_classrefs: 0xc30
   __DATA.__objc_superrefs: 0x418
-  __DATA.__objc_ivar: 0xbf0
+  __DATA.__objc_ivar: 0xbf4
   __DATA.__objc_data: 0x3750
   __DATA.__data: 0x22a0
-  __DATA.__bss: 0x7cc
+  __DATA.__bss: 0x7ec
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4073
-  Symbols:   877
-  CStrings:  7226
+  Functions: 4067
+  Symbols:   878
+  CStrings:  7205
 
Symbols:
+ _EFContentProtectionGetObservedState
CStrings:
+ "\x01)"
+ "Apply rule:%@ to messages: %@"
+ "Re-trying performFetchOfType:%i uids for %@"
+ "Successfully moved %lu messages from blocked sender to trash"
+ "Will retry."
+ "com.apple.email.DaemonFetchController"
+ "com.apple.email.ProcessSQLQueryPerformanceData"
+ "com.apple.mail.mailboxPersistence.statisticsReportingScheduler"
+ "performFetchOfType:%i (%{BOOL}d) failed to find uids for %@"
+ "performFetchOfType:%i (%{BOOL}d), uids for %@"
+ "persistedMessagesMatchingQuery:limit:requireProtectedData:"
+ "predicateForMessagesWithSenders:"
- "\x01("
- "T@\"<EFScheduler>\",&,N,V_pendingFetchOTCScheduler"
- "T@\"FetchXPCActivityScheduler\",&,N,V_compactScheduler"
- "T@\"FetchXPCActivityScheduler\",&,N,V_periodicScheduler"
- "T@\"FetchXPCActivityScheduler\",&,N,V_powerNapScheduler"
- "T@\"NSObject\",R,N,V_backFillScheduler"
- "T@\"NSSet\",&,N,V_currentAlertContexts"
- "T@\"NSSet\",&,N,V_currentAlertSuppresionContexts"
- "_cancelPeriodicFetches"
- "_cancelThrottleTimer"
- "_delayFetchOTCInterval"
- "_fetchTypeForSchedulerType:"
- "_findMailboxWithName:inAccounts:"
- "_mailboxWithName:forAccount:"
- "_periodicFetchInterval"
- "_powernapFetchInterval"
- "_schedulePowernapFetches"
- "_updatePushState"
- "_updatePushStateThrottled"
- "backFillScheduler"
- "compactScheduler"
- "currentAlertContexts"
- "i20@0:8i16"
- "messagesMatchingCriterion:options:success:"
- "pendingFetchOTCScheduler"
- "performFetchOfType:%i failed to find uids for %@"
- "periodicScheduler"
- "powerNapScheduler"
- "setCompactScheduler:"
- "setCurrentAlertContexts:"
- "setPendingFetchOTCScheduler:"
- "setPeriodicScheduler:"
- "setPowerNapScheduler:"

```

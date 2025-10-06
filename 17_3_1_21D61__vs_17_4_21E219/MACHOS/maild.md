## maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0xb7530
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_stubs: 0x15f80
-  __TEXT.__objc_methlist: 0x94dc
-  __TEXT.__gcc_except_tab: 0x17484
-  __TEXT.__objc_methname: 0x1b9a4
-  __TEXT.__cstring: 0x8087
-  __TEXT.__objc_classname: 0x1a92
-  __TEXT.__objc_methtype: 0x388e
-  __TEXT.__const: 0x130
-  __TEXT.__oslogstring: 0x8683
+3774.500.171.2.2
+  __TEXT.__text: 0xb7a44
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_stubs: 0x15cc0
+  __TEXT.__objc_methlist: 0x93c4
+  __TEXT.__gcc_except_tab: 0x174e4
+  __TEXT.__objc_methname: 0x1b77e
+  __TEXT.__cstring: 0x8139
+  __TEXT.__objc_classname: 0x1a62
+  __TEXT.__objc_methtype: 0x37ea
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x887d
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x6710
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0xa40
-  __DATA_CONST.__const: 0x47a0
-  __DATA_CONST.__cfstring: 0x6d80
-  __DATA_CONST.__objc_classlist: 0x588
+  __TEXT.__unwind_info: 0x6694
+  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__const: 0x47b8
+  __DATA_CONST.__cfstring: 0x6da0
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x2b8
+  __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x4c8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0xc00
+  __DATA_CONST.__objc_superrefs: 0x410
+  __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x151b0
-  __DATA.__objc_selrefs: 0x68b0
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0xc30
-  __DATA.__objc_superrefs: 0x418
-  __DATA.__objc_ivar: 0xbf4
-  __DATA.__objc_data: 0x3750
-  __DATA.__data: 0x22a0
-  __DATA.__bss: 0x7ec
+  __DATA.__objc_const: 0x14ff0
+  __DATA.__objc_selrefs: 0x67d0
+  __DATA.__objc_ivar: 0xc04
+  __DATA.__objc_data: 0x3700
+  __DATA.__data: 0x2240
+  __DATA.__bss: 0x7cc
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBE73A92-C642-3A66-8416-43B1710B1A73
-  Functions: 4067
-  Symbols:   878
-  CStrings:  8081
+  UUID: 1CE0E1B3-D5EF-38F0-A8DC-E401A2628FA8
+  Functions: 4055
+  Symbols:   864
+  CStrings:  8061
 
Symbols:
+ _EFProtectedDataAvailable
+ _EMUserDefaultSimulateDelayedFreeSpaceStatusTime
+ _MSSharedContactStore
+ _sleep
- _AWDPostMetric
- _MSMailAccountStatisticsKindAOL
- _MSMailAccountStatisticsKindExchange
- _MSMailAccountStatisticsKindGmail
- _MSMailAccountStatisticsKindHotmail
- _MSMailAccountStatisticsKindICloud
- _MSMailAccountStatisticsKindIMAP
- _MSMailAccountStatisticsKindNetease
- _MSMailAccountStatisticsKindPOP
- _MSMailAccountStatisticsKindQQ
- _MSMailAccountStatisticsKindYahoo
- _OBJC_CLASS_$_AWDMailCannotGetMailErrorReport
- _OBJC_CLASS_$_AWDMailError
- _OBJC_CLASS_$_EDLocalizableStrings
- _OBJC_CLASS_$_MSAccountToEmailProvider
- _OBJC_CLASS_$_MSDiagnosticManager
- _OBJC_CLASS_$_MSFetchMetricsController
- _OBJC_METACLASS_$_MSDiagnosticManager
CStrings:
+ "\x04!\"A"
+ "\x11\x1f\t"
+ "@16@?0@\"UNNotification\"8"
+ "Checking free space status"
+ "Could not update summary for RemindMe notification %@, message %@"
+ "Failed to find persisted message, skipping updates for RemindMe notification %@, message %@"
+ "No summary for message=%{public}@ isRemindMe=%{public}d"
+ "Not performing cleanup for RemindMe notifications. Protected data is not available."
+ "Not updating counts - hasAdequateDiskSpace:%lu"
+ "Scheduling fetch for %@ new accounts"
+ "Simulate delayed free space is enabled: waiting %lu seconds before returning status"
+ "Skipping update to notification %@"
+ "Summary for RemindMe will load on unlock"
+ "T@\"EFLocked\",&,N,V_remindMeNotificationsNeedingSummaries"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_contentProtectionQueue"
+ "T@\"NSString\",?,R,C"
+ "TQ,N,V_hasAdequateFreeSpace"
+ "Updating summary for RemindMe notification %@, message %@"
+ "_freeSpaceStatusDelay"
+ "_performCleanupForRemindMeNotifications:"
+ "_remindMeNotificationsNeedingSummaries"
+ "_shouldDelayFreeSpace"
+ "_uniqueIDAndDisplayName"
+ "com.apple.email.MFUserNotificationCenterController.contentProtectionQueue"
+ "contentProtectionQueue"
+ "initWithAccountsProvider:favoritesPersistence:hookRegistry:"
+ "localizedRemindMeNotificationTitleNoSender"
+ "persistedMessagesForDatabaseIDs:requireProtectedData:temporarilyUnavailableDatabaseIDs:"
+ "remindMeNotificationsNeedingSummaries"
+ "setHasAdequateFreeSpace:"
+ "setRemindMeNotificationsNeedingSummaries:"
+ "uniqueIDAndDisplayName"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v32@?0@\"NSString\"8@\"EFPair\"16^B24"
- "\x05!\"A"
- "\x11\x1f\a"
- "@\"AWDMailError\"16@0:8"
- "@\"MSDiagnosticManager\"16@0:8"
- "@\"MSFetchMetricsController\""
- "@\"PBCodable\"8@?0"
- "MFDiagnostic"
- "MSFetchMetricsControllerDataSource"
- "No summary for message=%{public}@"
- "Not updating counts - hasAdequateDiskSpace:%d"
- "_metricsController"
- "_statisticsKindFromAccount:"
- "awdNetworkDiagnosticReport"
- "awdServerConnection"
- "diagnosticManager"
- "didTimeout"
- "emailProvider"
- "emailProviderFromAccountStatisticsKind:"
- "i24@0:8q16"
- "initWithAccountsProvider:favoritesPersistence:"
- "initWithDataSource:"
- "localNonDeletedCount"
- "mailError"
- "mailErrorCodeFromErrorDomainCode:"
- "mailErrorFromErrorDomainCode:"
- "mailErrorReportProtocolFromAccount:"
- "mailErrorReportProtocolFromAccountStatisticsKind:"
- "mailErrorReportProviderFromAccount:"
- "noSenderTitle"
- "numMessagesFetched"
- "registerMetrics"
- "registerQueriableMetric:callback:"
- "setErrorCode:"
- "setGenericErrorCode:"
- "setMailError:"
- "setProtocol:"
- "setProvider:"
- "shouldReport"
- "stopAndSubmitWithOptions:fetchSize:"
- "submitMailCannotGetMailError:forAccount:submitNetworkDiags:"
- "submitMailCannotGetMailErrorDueToErrorDomainCode:submitNetworkDiags:"
- "submitMailCannotGetMailErrorDueToMailErrorCode:submitNetworkDiags:"
- "submitMailCannotGetMailErrorForHostname:protocol:emailProvider:mailError:submitNetworkDiags:"
- "submitMailCannotGetMailErrorForHostname:protocol:emailProvider:mfErrorDomainCode:submitNetworkDiags:"
- "submitMailMessageDisplayErrorReport:"
- "submitMailNetworkDiagnosticsReport"
- "submitWithIdentifier:metricGenerator:"
- "totalBytesReceived"
- "totalBytesSent"
- "trigger"
- "v12@?0I8"
- "v24@0:8i16B20"
- "v28@0:8q16B24"
- "v44@0:8@16i24i28@32B40"
- "v44@0:8@16i24i28q32B40"

```

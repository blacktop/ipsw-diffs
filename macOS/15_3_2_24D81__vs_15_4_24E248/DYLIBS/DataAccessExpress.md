## DataAccessExpress

> `/System/Library/PrivateFrameworks/DataAccessExpress.framework/Versions/A/DataAccessExpress`

```diff

-2673.0.0.0.0
-  __TEXT.__text: 0x2c79c
+2673.5.2.0.0
+  __TEXT.__text: 0x2ca78
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x20dc
-  __TEXT.__gcc_except_tab: 0x100c
+  __TEXT.__objc_methlist: 0x212c
+  __TEXT.__gcc_except_tab: 0x1014
   __TEXT.__cstring: 0x3731
   __TEXT.__const: 0xc0
   __TEXT.__oslogstring: 0x2c1b
-  __TEXT.__unwind_info: 0x998
+  __TEXT.__unwind_info: 0x9d0
   __TEXT.__objc_classname: 0x3be
   __TEXT.__objc_methname: 0x5de1
   __TEXT.__objc_methtype: 0x71f

   __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0xb20
   __AUTH_CONST.__cfstring: 0x40c0
-  __AUTH_CONST.__objc_const: 0x41f0
+  __AUTH_CONST.__objc_const: 0x4178
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xb40

   - /System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8EFA941F-24FA-3515-844B-A2AF8B044595
-  Functions: 925
-  Symbols:   2814
+  UUID: 77D752AD-DF08-3E12-8507-9BCB81B38932
+  Functions: 968
+  Symbols:   2881
   CStrings:  2490
 
Symbols:
+ +[CalDAVOfficeHour _gregorianGMTCalendar].cold.1
+ +[CalDAVOfficeHour icsFromOfficeHours:].cold.1
+ +[CalDAVOfficeHour logHandle].cold.1
+ +[DADConnection sharedConnection].cold.1
+ +[DASharedAccountProperties leafAccountTypesToCheckForEquality].cold.1
+ +[DASharedAccountProperties leafAccountTypes].cold.1
+ +[DASharedAccountProperties parentAccountTypes].cold.1
+ -[DAAccountChangeInfo initWithCoder:].cold.1
+ -[DACPLogDFile _startNewFile].cold.1
+ -[DACPLogShared _getUUIDForFolder:baseName:].cold.1
+ -[DAECalendarAvailabilitySpan initWithStartDate:endDate:type:].cold.1
+ -[DAECalendarAvailabilitySpan initWithStartDate:endDate:type:].cold.2
+ -[DAECalendarAvailabilitySpan initWithStartDate:endDate:type:].cold.3
+ -[DAFolderChange encodeWithCoder:].cold.1
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.1
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.2
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.3
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.4
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.5
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.6
+ -[DAFolderChange initFolderChangeWithChangeType:folderId:parentFolderId:displayName:dataclass:consumer:].cold.7
+ -[DAFolderChange initWithCoder:].cold.1
+ DACPLoggingAddCustomLogConfiguration.cold.11
+ DACPLoggingAddCustomLogConfiguration.cold.12
+ DACPLoggingAddCustomLogConfiguration.cold.13
+ DACPLoggingAddCustomLogConfiguration.cold.14
+ DACPLoggingAppendDataToLogFile.cold.1
+ DACPLoggingAppendDataToLogFile.cold.2
+ DACPLoggingAppendDataToLogFile.cold.3
+ DACPLoggingAppendDataToLogFile.cold.4
+ DACPLoggingAppendDataToLogFile.cold.5
+ DACPLoggingCustomMaxConsoleLevel.cold.1
+ DACPLoggingCustomMaxLogFileLevel.cold.1
+ DACPLoggingFlush.cold.1
+ DACPLoggingFlush.cold.2
+ DACPLoggingSetCustomMaxConsoleLevel.cold.1
+ DACPLoggingSetCustomMaxConsoleLevel.cold.2
+ DACPLoggingSetCustomMaxLogFileLevel.cold.1
+ DACPLoggingSetCustomMaxLogFileLevel.cold.2
+ DACPLoggingSlurpFileIntoLogFile.cold.1
+ DACPLoggingSlurpFileIntoLogFile.cold.2
+ DACPLoggingSlurpFileIntoLogFile.cold.3
+ DACPLoggingSlurpFileIntoLogFile.cold.4
+ DACustomLogDirectory.cold.1
+ DALoggingwithCategory.cold.2
+ DAMigrateLogsIfNeeded.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __DACPLoggingAppendDataToLogFile_block_invoke_2.cold.1
+ __DAMigrateLogsIfNeeded_block_invoke.cold.1
+ ___initLogging_block_invoke.cold.1
+ ___initLogging_block_invoke.cold.2
+ ___initLogging_block_invoke_2.cold.1
+ ___initLogging_block_invoke_3.cold.1
+ ___init_block_invoke.cold.1
+ ___startObservingDefaultChanges_block_invoke.cold.1
+ ___startObservingDefaultChanges_block_invoke.cold.2
+ _allDALogFacilities.cold.1
+ _configurationQueueRereadAllDefaults.cold.1
+ _configurationQueueRereadDefaultsForSetting.cold.1
+ _fileOpsQueue.cold.1
+ _setCustomCreateLogFormatBlock.cold.1
+ getDALogLevel.cold.1
+ getDAOutputLevel.cold.1
+ setDALogLevel.cold.1
+ setDALogOutputLevel.cold.1

```

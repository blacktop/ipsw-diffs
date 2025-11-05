## CDDataAccessExpress

> `/System/Library/PrivateFrameworks/CDDataAccessExpress.framework/Versions/A/CDDataAccessExpress`

```diff

-1205.0.0.0.0
-  __TEXT.__text: 0x1edf0
+1225.1.0.0.0
+  __TEXT.__text: 0x1f044
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x154c
+  __TEXT.__objc_methlist: 0x159c
   __TEXT.__cstring: 0x2a92
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xafc
+  __TEXT.__gcc_except_tab: 0xb04
   __TEXT.__oslogstring: 0x1b6e
-  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__unwind_info: 0x6e8
   __TEXT.__objc_classname: 0x203
   __TEXT.__objc_methname: 0x3ff7
   __TEXT.__objc_methtype: 0x58e

   __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x2560
+  __AUTH_CONST.__objc_const: 0x24e8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x5f0

   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63E5A311-8408-3370-9B37-B4ABF87A0652
-  Functions: 630
-  Symbols:   1965
+  UUID: 68EDAE66-5B1A-3C99-92EF-C2C8CF826AF0
+  Functions: 666
+  Symbols:   2024
   CStrings:  1819
 
Symbols:
+ +[CDDADConnection sharedConnection].cold.1
+ +[DABehaviorOptions _daManagedDefaultsPath].cold.1
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
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __DACPLoggingAppendDataToLogFile_block_invoke_2.cold.1
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

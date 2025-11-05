## AppSupport

> `/System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport`

```diff

-2637.0.0.0.0
-  __TEXT.__text: 0x2cb68
-  __TEXT.__auth_stubs: 0x1eb0
-  __TEXT.__objc_methlist: 0x1268
-  __TEXT.__cstring: 0x4df8
-  __TEXT.__const: 0x4de0
+2646.0.0.0.0
+  __TEXT.__text: 0x2c8dc
+  __TEXT.__auth_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x12a0
+  __TEXT.__cstring: 0x4df5
+  __TEXT.__const: 0x4e10
   __TEXT.__oslogstring: 0xb87
   __TEXT.__gcc_except_tab: 0x1dc
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xb80
+  __TEXT.__unwind_info: 0xbb8
   __TEXT.__objc_classname: 0x2dc
   __TEXT.__objc_methname: 0x371b
   __TEXT.__objc_methtype: 0x8a2
   __TEXT.__objc_stubs: 0x2d20
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0xf70
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0xf68
+  __AUTH_CONST.__auth_got: 0xf60
   __AUTH_CONST.__const: 0xe90
   __AUTH_CONST.__cfstring: 0x38e0
-  __AUTH_CONST.__objc_const: 0x28e8
+  __AUTH_CONST.__objc_const: 0x2880
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x244

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EA56B2FA-00F8-38CB-826D-340CD344B07B
-  Functions: 1102
-  Symbols:   2815
-  CStrings:  2019
+  UUID: 9FAB8DAC-4D06-3DBF-BBF4-B3A92B97011E
+  Functions: 1149
+  Symbols:   2942
+  CStrings:  2018
 
Symbols:
+ +[ALCityManager sharedManager].cold.1
+ +[ALCityManager willApplyTimeZoneChanges1].cold.1
+ +[CPDistributedNotificationCenter _serverPortToNotificationCenterMapDispatchQueue].cold.1
+ +[CPDistributedNotificationCenter _serverPortToNotificationCenterMap].cold.1
+ +[_CPInhibitorManager sharedInstance].cold.1
+ -[CPDistributedMessagingCenter _setSendPort:].cold.1
+ -[CPDistributedMessagingCenter _setupInvalidationSource].cold.1
+ -[CPDistributedNotificationCenter _receivedCheckIn:auditToken:].cold.1
+ -[CPLRUDictionary initWithMaximumCapacity:].cold.1
+ -[CPMemoryPoolFile nextSlotWithBytes:length:].cold.1
+ CPBitmapWriterCreateWithFileDescriptor.cold.1
+ CPBitmapWriterGetTypeID.cold.1
+ CPCanSendMail.cold.1
+ CPDateFormatStringForFormatType.cold.1
+ CPDateFormatStringForFormatType.cold.2
+ CPDeleteTree.cold.10
+ CPDeleteTree.cold.6
+ CPDeleteTree.cold.7
+ CPDeleteTree.cold.8
+ CPDeleteTree.cold.9
+ CPFreeSpaceRequestBytesAtPathWithCompletionBlock.cold.3
+ CPGetDeviceRegionCode.cold.1
+ CPIsInternalDevice.cold.1
+ CPLogV.cold.1
+ CPLoggingAddCustomLogConfiguration.cold.1
+ CPLoggingAddCustomLogConfiguration.cold.2
+ CPLoggingAddCustomLogConfiguration.cold.3
+ CPLoggingAddCustomLogConfiguration.cold.4
+ CPLoggingAppendDataToLogFile.cold.1
+ CPLoggingAppendDataToLogFile.cold.2
+ CPLoggingAppendDataToLogFile.cold.3
+ CPLoggingAppendDataToLogFile.cold.4
+ CPLoggingAppendDataToLogFile.cold.5
+ CPLoggingCopyCustomLogDirectory.cold.1
+ CPLoggingCopyCustomLogName.cold.1
+ CPLoggingCustomConsoleUsesRealLevels.cold.1
+ CPLoggingCustomMaxConsoleLevel.cold.1
+ CPLoggingCustomMaxLogFileCount.cold.1
+ CPLoggingCustomMaxLogFileLevel.cold.1
+ CPLoggingCustomMaxLogFileSize.cold.1
+ CPLoggingCustomWantsCompressedFiles.cold.1
+ CPLoggingFlush.cold.1
+ CPLoggingFlush.cold.2
+ CPLoggingFlushWithCompletion.cold.1
+ CPLoggingIsFacilityDefined.cold.1
+ CPLoggingSetCustomConsoleLevelDefaults.cold.1
+ CPLoggingSetCustomConsoleLevelDefaults.cold.2
+ CPLoggingSetCustomConsoleLevelDefaults.cold.3
+ CPLoggingSetCustomConsoleUsesRealLevels.cold.1
+ CPLoggingSetCustomDidCreateNewFileBlock.cold.1
+ CPLoggingSetCustomLogDirectory.cold.1
+ CPLoggingSetCustomLogDirectory.cold.2
+ CPLoggingSetCustomLogFileLevelDefaults.cold.1
+ CPLoggingSetCustomLogFileLevelDefaults.cold.2
+ CPLoggingSetCustomLogFileLevelDefaults.cold.3
+ CPLoggingSetCustomLogName.cold.1
+ CPLoggingSetCustomLogName.cold.2
+ CPLoggingSetCustomMaxConsoleLevel.cold.1
+ CPLoggingSetCustomMaxConsoleLevel.cold.2
+ CPLoggingSetCustomMaxLogFileCount.cold.1
+ CPLoggingSetCustomMaxLogFileLevel.cold.1
+ CPLoggingSetCustomMaxLogFileLevel.cold.2
+ CPLoggingSetCustomMaxLogFileSize.cold.1
+ CPLoggingSetCustomWantsCompressedFiles.cold.1
+ CPLoggingSetCustomWillLogToConsoleBlock.cold.1
+ CPLoggingSetCustomWillLogToLogFileBlock.cold.1
+ CPLoggingSlurpFileIntoLogFile.cold.1
+ CPLoggingSlurpFileIntoLogFile.cold.2
+ CPLoggingSlurpFileIntoLogFile.cold.3
+ CPLoggingSlurpFileIntoLogFile.cold.4
+ CPLoggingStartNewLogFile.cold.1
+ CPLoggingStartNewLogFile.cold.2
+ CPLoggingStartNewLogFile.cold.3
+ CPLoggingStartNewLogFileNextLine.cold.1
+ CPPathUtils_MakePath.cold.2
+ CPSqliteConnectionStatementForSQLAndIgnoreErrors.cold.1
+ CPSystemRootDirectory.cold.1
+ _CPLog.cold.1
+ _CPLogLine.cold.1
+ _CPRecordStoreGetChangesAndChangeIndicesAndSequenceNumbersForClassWithPropertiesA.cold.1
+ _CPTimeFormatIs24HourMode.cold.1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __56-[CPDistributedMessagingCenter _setupInvalidationSource]_block_invoke.68.cold.1
+ __63-[CPDistributedNotificationCenter _receivedCheckIn:auditToken:]_block_invoke_2.cold.1
+ __CPCanSendMail_block_invoke.cold.1
+ __CPFreeSpaceRequestBytesAtPathWithCompletionBlock_block_invoke.9.cold.2
+ __CPLoggingAppendDataToLogFile_block_invoke_2.cold.1
+ __CPLoggingSlurpFileIntoLogFile_block_invoke_2.cold.1
+ __CPLoggingSlurpFileIntoLogFile_block_invoke_2.cold.2
+ __CPLoggingSlurpFileIntoLogFile_block_invoke_2.cold.3
+ __CPLoggingStartNewLogFile_block_invoke.cold.1
+ __CPLoggingStartNewLogFile_block_invoke.cold.2
+ __CPLoggingStartNewLogFile_block_invoke.cold.3
+ ___init_block_invoke.cold.1
+ ___startObservingDefaultChanges_block_invoke.cold.1
+ ___startObservingDefaultChanges_block_invoke.cold.2
+ ___workQueueCopyConnection_block_invoke_3.cold.1
+ ___workQueueCopyConnection_block_invoke_5.cold.1
+ _configurationQueueRereadAllDefaults.cold.1
+ _configurationQueueRereadDefaultsForSetting.cold.1
+ _createStandardFileLogLine.cold.1
+ _format_bitmapinfo
+ _logV.cold.1
+ _logV.cold.2
+ _logV.cold.3
+ _logV.cold.4
+ _obfuscatedRepresentation.cold.1
+ _obfuscatedRepresentation.cold.2
+ _obfuscatedRepresentation.cold.3
+ _releaseObfuscatedStrings.cold.1
+ _releaseObfuscatedStrings.cold.2
+ _setCustomCreateLogFormatBlock.cold.1
+ _workQueueAppendDataToLogFile.cold.1
+ _workQueueAppendDataToLogFile.cold.2
+ _workQueueAppendDataToLogFile.cold.3
+ _workQueueCopyConnection.cold.1
+ _workQueueRefreshUUIDForWorkSettings.cold.1
+ _workQueueRefreshUUIDForWorkSettings.cold.2
+ _workQueueRefreshUUIDForWorkSettings.cold.3
- _fmod
CStrings:
- "ok"

```

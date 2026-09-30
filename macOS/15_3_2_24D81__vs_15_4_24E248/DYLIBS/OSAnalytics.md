## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x410f0
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x18d0
-  __TEXT.__oslogstring: 0x2dc1
-  __TEXT.__cstring: 0x8c4f
+758.100.43.0.0
+  __TEXT.__text: 0x41a08
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_methlist: 0x1a48
+  __TEXT.__oslogstring: 0x2e98
+  __TEXT.__cstring: 0x8dbe
   __TEXT.__const: 0x5b0
-  __TEXT.__gcc_except_tab: 0x10a0
+  __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__dlopen_cstrs: 0xed
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__unwind_info: 0xa68
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x4b44
-  __TEXT.__objc_methtype: 0xc55
-  __TEXT.__objc_stubs: 0x4280
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x7b8
+  __TEXT.__objc_methname: 0x4bad
+  __TEXT.__objc_methtype: 0xc6e
+  __TEXT.__objc_stubs: 0x42c0
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f8
+  __DATA_CONST.__objc_selrefs: 0x1490
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xbd0
-  __AUTH_CONST.__auth_got: 0x930
-  __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0x9b80
-  __AUTH_CONST.__objc_const: 0x38f0
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__const: 0xf00
+  __AUTH_CONST.__cfstring: 0x9ca0
+  __AUTH_CONST.__objc_const: 0x36a0
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0x168
-  __DATA.__bss: 0x380
+  __DATA.__bss: 0x388
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7EFA8BCB-16FD-374F-87D6-9963539F6D70
-  Functions: 949
-  Symbols:   2627
-  CStrings:  4073
+  UUID: 53BB4635-07ED-3BEA-99D2-4BF1B91C14FA
+  Functions: 970
+  Symbols:   2670
+  CStrings:  4099
 
Symbols:
+ +[OSABridgeLinkProxy transfer:key:].cold.1
+ +[OSALog markDescriptor:withPairs:andOptions:].cold.1
+ +[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]
+ +[OSALog randomlySelectForRetention:].cold.1
+ +[OSALogTrackerObject sharedTrackers].cold.1
+ +[OSAReport findBundleAtPath:withKeys:bundleURL:].cold.1
+ +[OSAStateMonitor evaluateState].cold.1
+ +[OSASystemConfiguration sharedInstance].cold.1
+ -[OSABinaryImageCatalog init].cold.1
+ -[OSALog initWithPath:forRouting:usingConfig:options:error:].cold.2
+ -[OSAReport getSyslogForPids:andOptionalSenders:additionalPredicates:].cold.5
+ -[OSAStackShotReport decodeKCDataWithBlock:withTuning:usingCatalog:].cold.28
+ -[OSAStackShotReport initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:].cold.1
+ -[OSASystemConfiguration factoryDevice]
+ -[OSASystemConfiguration pairedWatchOS].cold.1
+ -[OSASystemConfiguration submissionsDisabled]
+ -[OSASystemConfiguration submissionsDisabled].cold.1
+ -[OSASystemConfiguration submissionsDisabled].cold.2
+ -[OSASystemConfiguration(optIn) optIn3rdParty].cold.1
+ -[OSASystemConfiguration(optIn) optInApple].cold.1
+ GCC_except_table97
+ OBJC_IVAR_$_OSASystemConfiguration._factoryDevice
+ OSAIsACDCDevice.cold.1
+ OSARTCIsProcessOfInterest.cold.1
+ OSASanitizePath.cold.1
+ OSA_OSX_Legacy_GetUserUUID.cold.1
+ OSAnalyticsHelperServiceConnection.cold.1
+ _MGGetBoolAnswer
+ _OSAIsConfiguredRSDDevice
+ _OSAIsConfiguredRSDHost
+ __32+[OSALog scanLogs:from:options:]_block_invoke.389
+ __35-[OSAExclaveContainer parseKCdata:]_block_invoke.81
+ __37-[OSASystemConfiguration internalKey]_block_invoke.322
+ __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.1
+ __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.2
+ __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.3
+ __44+[OSALog iterateLogsWithOptions:usingBlock:]_block_invoke.408
+ __61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.281
+ __61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.282
+ __61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.386
+ __76+[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]_block_invoke_2.cold.1
+ __76+[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]_block_invoke_2.cold.2
+ __76+[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]_block_invoke_2.cold.3
+ ___35-[OSAExclaveContainer parseKCdata:]_block_invoke
+ ___39-[OSASystemConfiguration factoryDevice]_block_invoke
+ ___76+[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]_block_invoke
+ ___76+[OSALog purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e13_v20?0I8r^Q12l
+ ___block_descriptor_40_e8_32s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12l
+ ___block_descriptor_49_e8_32bs_e13_v24?0r*8r*16l
+ __block_literal_global.197
+ __block_literal_global.266
+ __block_literal_global.318
+ __block_literal_global.364
+ __block_literal_global.392
+ __block_literal_global.400
+ _kOSALogCleanupOptionFilterByHeaders
+ _kOSALogCleanupOptionFilterByLogAge
+ _objc_msgSend$factoryDevice
+ _objc_msgSend$setDeleteOnRetire:
+ factoryDevice.pred
+ getRules.cold.1
+ rtc_internal.cold.1
+ rtcsc_send_base.cold.2
- +[OSALog purgeLogs:]
- GCC_except_table91
- _OSAIsDebugEnabledForRSD
- _OUTLINED_FUNCTION_5
- __20+[OSALog purgeLogs:]_block_invoke.cold.1
- __20+[OSALog purgeLogs:]_block_invoke.cold.2
- __20+[OSALog purgeLogs:]_block_invoke.cold.3
- __32+[OSALog scanLogs:from:options:]_block_invoke.383
- __37-[OSASystemConfiguration internalKey]_block_invoke.309
- __37-[OSASystemConfiguration internalKey]_block_invoke.309.cold.1
- __37-[OSASystemConfiguration internalKey]_block_invoke.309.cold.2
- __37-[OSASystemConfiguration internalKey]_block_invoke.309.cold.3
- __44+[OSALog iterateLogsWithOptions:usingBlock:]_block_invoke.401
- __61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.270
- __61+[OSALog createForSubmission:metadata:options:error:writing:]_block_invoke.275
- __61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.374
- ___20+[OSALog purgeLogs:]_block_invoke
- ___block_descriptor_40_e8_32s_e13_v24?0r*8r*16l
- __block_literal_global.191
- __block_literal_global.252
- __block_literal_global.312
- __block_literal_global.358
- __block_literal_global.386
CStrings:
+ "\nIncident Identifier: $(metadata:incident_id)\n^(!isBeta)CrashReporter Key:   $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nProcess:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\n^(!*translated)Code Type:           $(cpuType) (Native)\n^(*translated)Code Type:           $(cpuType) (Translated)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n^(systemID)UDID:                $(systemID)\nReport Version:      104\n\n^(exception.signal)Exception Type:  $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:  $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes: $(exception.rawCodes)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(simulatedCaller)Exception Note:  SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:  SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:  EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:  NON-FATAL CONDITION (this is NOT a crash)\n^(termination)Termination Reason: $(termination.namespace) $(termination.code) $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(faultingThread)Triggered by Thread:  $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread:  $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread:  Unknown\n\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered syslog:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)\nEOF\n"
+ "/System/Library/CoreServices/GroundhogTestStationBaseImage.plist"
+ "Configured value for submissionsDisabledSince key is not in the expected format: deleting key"
+ "Error creating log at %s/%s while purging: %@"
+ "Error deleting non-retirable log at %s/%s while purging: %@"
+ "Error retiring %s/%s while purging logs"
+ "GroundhogEnabled"
+ "GroundhogFactoryTrain"
+ "Not purging %s/%s: log did not meet criteria"
+ "Submissions were disabled over a week ago: re-enabling submissions"
+ "_factoryDevice"
+ "codeSigningAuxiliaryInfo"
+ "com.apple.osanalytics.factoryproxysync"
+ "configureProxyDevice"
+ "configureProxyHost"
+ "factoryDevice"
+ "filterByHeaders"
+ "filterByLogAge"
+ "purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:"
+ "submissionsDisabled"
+ "submissionsDisabledSince"
+ "v20@?0I8r^Q12"
+ "v20@?0I8r^{exclave_textlayout_segment=[16C]Q}12"
+ "v48@0:8@16r*24B32B36@?40"
- "\nIncident Identifier: $(metadata:incident_id)\n^(!isBeta)CrashReporter Key:   $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\nHardware Model:      $(modelCode)\n^(codeName)Device Model:        $(codeName)\nProcess:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleShortVersionString) ($(bundleInfo.CFBundleVersion|\"???\"))\n^(!bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.CFBundleVersion|\"???\")\n^(bundleInfo.DTAppStoreToolsBuild)AppStoreTools:       $(bundleInfo.DTAppStoreToolsBuild)\n^(storeInfo.applicationVariant)AppVariant:          $(storeInfo.applicationVariant)\n^(isBeta)Beta:                YES\nCode Type:           $(cpuType) (Native)\nRole:                $(procRole|\"Unspecified\")\nParent Process:      $(parentProc|\"???\") [$(parentPid|\"Unknown\")]\nCoalition:           $(coalitionName|\"<none>\") [$(coalitionID)]\n^(responsiblePid)Responsible Process: $(responsibleProc) [$(responsiblePid)]\n\nDate/Time:           $(captureTime)\nLaunch Time:         $(procLaunch)\nOS Version:          $(osVersion.train) ($(osVersion.build))\nRelease Type:        $(osVersion.releaseType)\n^(basebandVersion)Baseband Version:    $(basebandVersion)\n^(systemID)UDID:                $(systemID)\nReport Version:      104\n\n^(exception.signal)Exception Type:  $(exception.type) ($(exception.signal))\n^(!exception.signal)Exception Type:  $(exception.type)\n^(exception.subtype)Exception Subtype: $(exception.subtype)\n^(exception.message)Exception Message: $(exception.message)\n^(exception.rawCodes)Exception Codes: $(exception.rawCodes)\n^(vmRegionInfo)VM Region Info: $(vmRegionInfo)\n^(simulatedCaller)Exception Note:  SIMULATED (this is NOT a crash) requested by $(simulatedCaller)\n^(!simulatedCaller&isSimulated)Exception Note:  SIMULATED (this is NOT a crash)\n^(!isSimulated&isCorpse)Exception Note:  EXC_CORPSE_NOTIFY\n^(!isSimulated&isNonFatal)Exception Note:  NON-FATAL CONDITION (this is NOT a crash)\n^(termination)Termination Reason: $(termination.namespace) $(termination.code) $(termination.indicator)\n^(termination.reasons)$(termination.reasons)\n^(termination.details)$(termination.details)\n^(termination.byPid)Terminating Process: $(termination.byProc|\"<unknown>\") [$(termination.byPid)]\n^(termination)\n^(faultingThread)Triggered by Thread:  $(faultingThread)\n^(!faultingThread&legacyInfo.threadHighlighted)Highlighted by Thread:  $(legacyInfo.threadHighlighted)\n^(!faultingThread&!legacyInfo.threadHighlighted)Triggered by Thread:  Unknown\n\n^(asi)Application Specific Information:\n#(format_asi\n$(<value>)\n)#\n^(asi)$(format_asi#asi)\n^(asi)\n^(dyldMessages)Dyld Error Message:$(dyldMessages)\n^(dyldMessages)\n^(lastExceptionBacktrace)Last Exception Backtrace:\n^(lastExceptionBacktrace)$(lastExceptionBacktrace)\n^(lastExceptionBacktrace)\n^(ktriageinfo)Kernel Triage:\n^(ktriageinfo)$(ktriageinfo)\n^(ktriageinfo)\n$(threads|\"Backtrace not available\")\n\n$(threadState|\"No thread state (register information) available\")\n\nBinary Images:\n$(usedImages|\"Binary images description not available\")\n\n^(reportNotes)Error Formulating Crash Report:\n^(reportNotes)$(reportNotes)\n^(reportNotes)\n^(filteredLog)Filtered syslog:\n^(filteredLog)$(filteredLog)\n^(filteredLog)\n#(format_diagnosticOutput\nDiagnostic Output: $(<key>)\n$(<value>)\n)#\n^(diagnosticOutput)$(format_diagnosticOutput#diagnosticOutput)\n^(diagnosticOutput)\nEOF\n"
- "Error creating log at %s while purging: %@"
- "Error deleting non-retirable log at %s while purging: %@"
- "Error retiring %s while purging logs"
- "enableDebugProxySync"
- "opt-changed"
- "purgeLogs:"

```

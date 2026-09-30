## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x82a0
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0xe20
+314.100.8.0.0
+  __TEXT.__text: 0x91dc
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x14
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0xa35
-  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0xea0
+  __TEXT.__const: 0xe8
   __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methtype: 0x31
-  __TEXT.__oslogstring: 0x1a44
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__objc_methname: 0x9c7
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x368
+  __TEXT.__oslogstring: 0x1bb2
+  __TEXT.__gcc_except_tab: 0x70
+  __TEXT.__objc_methname: 0xa5a
+  __TEXT.__unwind_info: 0x170
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x3c8
-  __DATA_CONST.__cfstring: 0x9a0
+  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__cfstring: 0x1160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_selrefs: 0x3c0
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x58
+  __DATA.__data: 0x2a0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE24EF26-9B67-3D7B-B0E5-600F9E38AEDA
-  Functions: 49
-  Symbols:   159
-  CStrings:  385
+  UUID: FD4F7FF6-6211-3763-BD55-024FE1C11DAC
+  Functions: 62
+  Symbols:   867
+  CStrings:  520
 
Symbols:
+ 
+ +[RMETelemetry emitTelemetryForExecName:bundleID:exceptionType:footprint:footprintPeak:jetsamLimit:memgraphAttempted:memgraphSkippedReason:memgraphSucceeded:memgraphFailedReason:diagFilePath:isMSLEnabled:isGcoreCapture:]
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/0.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/1.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/2.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/3.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/4.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/5.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Binaries/footprint/install/TempContent/Objects/footprint.build/ReportMemoryException.build/Objects-normal/arm64e/ReportMemoryException_lto.o/6.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Sources/footprint/ReportMemoryException/
+ /Library/Caches/com.apple.xbs/B59CB6FB-7F7A-4447-9E74-FC0C78A27A50/TemporaryDirectory.cq744I/Sources/footprint/shared/
+ FPCorpseUtils.m
+ GCC_except_table19
+ GCC_except_table3
+ GCoreFrameworkLibraryCore.frameworkLibrary
+ MREConstants.m
+ RMEDaemon.m
+ RMEDaemon_embeddedOS.m
+ RMEMain.m
+ RMEPrefs.m
+ RMETelemetry.m
+ _FPExtractCorpseInfoWithBlock
+ _GCoreFrameworkLibraryCore
+ _MREBundleStringForUnbundledProcess
+ _MRECRBinaryInfoArchitectureKey
+ _MRECRStackFrameAddressKey
+ _MRECRStackFrameSourceFilenameKey
+ _MRECRStackFrameSourceLineKey
+ _MRECRStackFrameSymbolAddressRangeLocationKey
+ _MRECRStackFrameSymbolKey
+ _MRECRStackFrameUUIDKey
+ _MREErrorDomain
+ _MREExecutionStackBacktracesKey
+ _MREExecutionStackBinaryImagesKey
+ _MREExecutionStackCrashedThreadKey
+ _MREExecutionStackThreadNamesKey
+ _MREIOAccelMemoryInfoCachedCopyKey
+ _MREIOAccelMemoryInfoDescriptionsKey
+ _MREIOAccelMemoryInfoDirtySizeKey
+ _MREIOAccelMemoryInfoIsPurgeableKey
+ _MREIOAccelMemoryInfoIsWiredKey
+ _MREIOAccelMemoryInfoMemoryPoolKey
+ _MREIOAccelMemoryInfoResidentSizeKey
+ _MREIOAccelMemoryInfoSizeKey
+ _MREIOAccelMemoryInfoSurfaceIDKey
+ _MREIOSurfaceInfoHeightKey
+ _MREIOSurfaceInfoNameKey
+ _MREIOSurfaceInfoPixelFormatKey
+ _MREIOSurfaceInfoSizeKey
+ _MREIOSurfaceInfoSurfaceIDKey
+ _MREIOSurfaceInfoWidthKey
+ _MREMetaDataBundleIDKey
+ _MREMetaDataCoalitionBundleIDKey
+ _MREMetaDataDirtyFlagsKey
+ _MREMetaDataExceptionTypeKey
+ _MREMetaDataExecNameKey
+ _MREMetaDataExecPathKey
+ _MREMetaDataExecutionStackKey
+ _MREMetaDataFootprintToolKey
+ _MREMetaDataHWModelKey
+ _MREMetaDataIOAccelMemoryInfoErrorsKey
+ _MREMetaDataIOAccelMemoryInfoKey
+ _MREMetaDataIOSurfaceInfoKey
+ _MREMetaDataIs64BitKey
+ _MREMetaDataLedgerAlternateAccountingCompressedKey
+ _MREMetaDataLedgerAlternateAccountingKey
+ _MREMetaDataLedgerIOKitMappedKey
+ _MREMetaDataLedgerInternalCompressedKey
+ _MREMetaDataLedgerInternalKey
+ _MREMetaDataLedgerNetworkNonvolatileCompressedKey
+ _MREMetaDataLedgerNetworkNonvolatileKey
+ _MREMetaDataLedgerPageTableKey
+ _MREMetaDataLedgerPhysFootprintKey
+ _MREMetaDataLedgerPhysFootprintPeakKey
+ _MREMetaDataLedgerPurgeableNonvolatileCompressedKey
+ _MREMetaDataLedgerPurgeableNonvolatileKey
+ _MREMetaDataLedgerWiredMemKey
+ _MREMetaDataLimitValueKey
+ _MREMetaDataMSLEnabledKey
+ _MREMetaDataMemgraphErrorKey
+ _MREMetaDataName
+ _MREMetaDataOSLogsKey
+ _MREMetaDataOSVersionKey
+ _MREMetaDataPIDKey
+ _MREMetaDataPPIDKey
+ _MREMetaDataUpTimeKey
+ _MREMetaDataVersionKey
+ _OBJC_CLASS_$_RMETelemetry
+ _OBJC_METACLASS_$_RMETelemetry
+ _RMEExtractExecNameForFilename
+ _RMEGCoreDiagFilenameIndicator
+ _RMEGetCriticalProcesses
+ _RMEGetDefaultCriticalProcesses
+ _RMEGetDefaultLargeExemptedProcesses
+ _RMEGetLiteLimitForExecName
+ _RMEGetMemgraphLimitForExecName
+ _RMEGetPrefs
+ _RMEGetPrefsWithProfileDicts
+ _RMEGetTimeOrderedLogPathsMatchingPrefs
+ _RMEIsAutoSubmitEnabled
+ _RMEIsCriticalProcess
+ _RMEMSLFullDiagFileSuffix
+ _RMEPopulateDefaultPrefs
+ _RMEPrefAllowInSysdiagnoseKey
+ _RMEPrefBoostCriticalProcessKey
+ _RMEPrefCollectIOAccelMemInfoKey
+ _RMEPrefCriticalProcessesKey
+ _RMEPrefExecNamesKey
+ _RMEPrefExpirationDateKey
+ _RMEPrefFullContentExecNamesListKey
+ _RMEPrefFullDiagLimitKey
+ _RMEPrefFullPerProcessLimitKey
+ _RMEPrefGCoreDiagLimitKey
+ _RMEPrefLargeExemptedProcessesKey
+ _RMEPrefLiteDiagLimitKey
+ _RMEPrefLitePerProcessLimitKey
+ _RMEPrefMSLFullDiagLimitKey
+ _RMEPrefPerCriticalProcessLimitKey
+ _RMEPrefProcessSpecificLimitsKey
+ _RMEPrefSysdiagnoseListKey
+ _RMEPrefThresholdFullDiagLimitKey
+ _RMEShouldIncludeDiagInSysdiagnose
+ _RMEShouldLogThirdPartyProcesses
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_RMETelemetry
+ __OBJC_CLASS_RO_$_RMETelemetry
+ __OBJC_METACLASS_RO_$_RMETelemetry
+ ___220+[RMETelemetry emitTelemetryForExecName:bundleID:exceptionType:footprint:footprintPeak:jetsamLimit:memgraphAttempted:memgraphSkippedReason:memgraphSucceeded:memgraphFailedReason:diagFilePath:isMSLEnabled:isGcoreCapture:]_block_invoke
+ ___GCoreFrameworkLibraryCore_block_invoke
+ ___RMEGetTimeOrderedLogPathsMatchingPrefs_block_invoke
+ ___RMEIsAutoSubmitEnabled_block_invoke
+ ___RMEShouldLogThirdPartyProcesses_block_invoke
+ ___block_descriptor_108_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_32_e25_q24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_69_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_77_e8_32s40s48s56bs64r_e5_v8?0ls32l8r64l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40r48w56w_e5_v8?0lr40l8w48l8w56l8s32l8
+ ___block_descriptor_84_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s48l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_95_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_literal_global
+ ___checkForTimeout_block_invoke
+ ___createABCCase_block_invoke
+ ___emitSignpostWithExceptionInfo_block_invoke
+ ___getTaskFootprintLimit_block_invoke
+ ___getcreate_gcore_with_optionsSymbolLoc_block_invoke
+ ___gregorianCalendar_block_invoke
+ ___handleAnalyzeRequestAsync_block_invoke
+ ___handleAnalyzeRequestAsync_block_invoke_2
+ ___handleRequestMemgraphWriteToFileAsync_block_invoke
+ ___handleRequestMemgraphWriteToFileAsync_block_invoke_2
+ ___handleRequest_block_invoke
+ ___liteAnalysisMemgraphOnly_block_invoke
+ ___liteAnalysisMemgraphOnly_block_invoke_2
+ ___liteAnalysisMemgraphOnly_block_invoke_3
+ ___liteAnalysisMemgraphOnly_block_invoke_4
+ ___liteAnalysis_block_invoke
+ ___main_block_invoke
+ ___saveLogFile_block_invoke
+ ___scheduleForceExitCheck_block_invoke
+ __block_literal_global.102
+ __block_literal_global.104
+ __block_literal_global.129
+ __block_literal_global.135
+ __block_literal_global.32
+ __block_literal_global.34
+ __block_literal_global.40
+ __block_literal_global.91
+ __isFileQuotaAvailable
+ __liteAnalysisMemgraphOnly_block_invoke.137
+ __main_block_invoke.6
+ __main_block_invoke.8
+ _audit_stringGCoreFramework
+ _checkForTimeout
+ _createFilePathTemplate
+ _criticalAnalysisAggregateTimeout
+ _deleteOldGcoreFiles
+ _emitSignpostWithExceptionInfo
+ _gCRAnnotations
+ _getMaxBulkRequestsInFlight
+ _getcreate_gcore_with_optionsSymbolLoc
+ _handleAnalyzeRequestAsync
+ _handleRequestMemgraphWriteToFileAsync
+ _isValidLimitVal
+ _main
+ _mergePrefsFromInput
+ _mergePrefsFromInputProcessList
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_generateMemgraphWithContentLevel:timeoutSecs:memgraphFailedReasonOut:
+ _objc_msgSend$_populateAddtionalMetadataWithOptions:timeoutSecs:
+ _objc_msgSend$_saveLogFileWithHandle:error:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allKeys
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleID
+ _objc_msgSend$cachedMetaDataDict
+ _objc_msgSend$closeFile
+ _objc_msgSend$coalitionBundleID
+ _objc_msgSend$code
+ _objc_msgSend$compare:
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createMetaDataDict
+ _objc_msgSend$currentTime
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$day
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$domain
+ _objc_msgSend$emitTelemetryForExecName:bundleID:exceptionType:footprint:footprintPeak:jetsamLimit:memgraphAttempted:memgraphSkippedReason:memgraphSucceeded:memgraphFailedReason:diagFilePath:isMSLEnabled:isGcoreCapture:
+ _objc_msgSend$enumeratorAtPath:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$exceptionType
+ _objc_msgSend$execName
+ _objc_msgSend$extractExecNameAndBundleIDMinimal:execNameOut:bundleIDOut:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileSize
+ _objc_msgSend$gcoreCapture
+ _objc_msgSend$generateMemoryGraphWithContentLevel:memgraphFailedReasonOut:
+ _objc_msgSend$getEPLProfilePath
+ _objc_msgSend$getGcoreSpoolWithCreateIfNecessary:
+ _objc_msgSend$getLogContainer:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hour
+ _objc_msgSend$initCacheEnumerator
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithFileDescriptor:
+ _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithObjectsAndKeys:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isFirstParty
+ _objc_msgSend$isMSLEnabled
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$ledgerAlternateAccounting
+ _objc_msgSend$ledgerAlternateAccountingCompressed
+ _objc_msgSend$ledgerIOKitMapped
+ _objc_msgSend$ledgerInternal
+ _objc_msgSend$ledgerInternalCompressed
+ _objc_msgSend$ledgerNetworkNonvolatile
+ _objc_msgSend$ledgerNetworkNonvolatileCompressed
+ _objc_msgSend$ledgerPageTable
+ _objc_msgSend$ledgerPhysFootprint
+ _objc_msgSend$ledgerPhysFootprintPeak
+ _objc_msgSend$ledgerPurgeableNonvolatile
+ _objc_msgSend$ledgerPurgeableNonvolatileCompressed
+ _objc_msgSend$ledgerWiredMem
+ _objc_msgSend$length
+ _objc_msgSend$limitValue
+ _objc_msgSend$liteDiagFilePath
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$memoryGraph
+ _objc_msgSend$minute
+ _objc_msgSend$month
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$nextValidURL
+ _objc_msgSend$null
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$path
+ _objc_msgSend$pid
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$releaseAnalyzedTask
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$resourceExceptionFromTask:error:
+ _objc_msgSend$second
+ _objc_msgSend$set
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setGcoreCapture:
+ _objc_msgSend$setGcoreFilePath:
+ _objc_msgSend$setLiteDiagFilePath:
+ _objc_msgSend$setMemgraphError:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:
+ _objc_msgSend$snapshotWithSignature:duration:events:payload:actions:reply:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$task
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$upTime
+ _objc_msgSend$year
+ _objc_retain_x28
+ _saveLogFile
+ _scheduleForceExitCheck
+ _setCrashReporterInfoForMRE
+ _setPermissionsForDiagFile
+ _shouldBoostCriticalProcesses
+ _task_map_corpse_info_64
+ _vm_deallocate
+ checkIfShouldForceExitAndRescheduleIfNeeded.currTimeoutCount
+ getcreate_gcore_with_optionsSymbolLoc.ptr
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- radr://5614542
CStrings:
+ "<UnbundledProcess>"
+ "Address"
+ "AddressRangeLocationKey"
+ "BinaryInfoArchitectureKey"
+ "CachedCopy"
+ "Descriptions"
+ "DirtySize"
+ "Height"
+ "IsPurgeable"
+ "IsWired"
+ "MRE_BundleID"
+ "MRE_CoalitionBundleID"
+ "MRE_DirtyFlags"
+ "MRE_ExceptionType"
+ "MRE_ExecName"
+ "MRE_ExecPath"
+ "MRE_ExecutionStack"
+ "MRE_ExecutionStack_Backtraces"
+ "MRE_ExecutionStack_BinaryImages"
+ "MRE_ExecutionStack_CrashedThread"
+ "MRE_ExecutionStack_ThreadNames"
+ "MRE_FootprintTool"
+ "MRE_HWModel"
+ "MRE_IOAccelMemoryInfo"
+ "MRE_IOAccelMemoryInfoErrors"
+ "MRE_IOSurfaceInfo"
+ "MRE_LedgerAlternateAccounting"
+ "MRE_LedgerAlternateAccountingCompressed"
+ "MRE_LedgerIOKitMapped"
+ "MRE_LedgerInternal"
+ "MRE_LedgerInternalCompressed"
+ "MRE_LedgerNetworkNonvolatile"
+ "MRE_LedgerNetworkNonvolatileCompressed"
+ "MRE_LedgerPageTable"
+ "MRE_LedgerPhysFootprint"
+ "MRE_LedgerPhysFootprintPeak"
+ "MRE_LedgerPurgeableNonvolatile"
+ "MRE_LedgerPurgeableNonvolatileCompressed"
+ "MRE_LedgerWiredMem"
+ "MRE_LimitValue"
+ "MRE_MSLEnabled"
+ "MRE_MemgraphError"
+ "MRE_OSLogs"
+ "MRE_OSVersion"
+ "MRE_PID"
+ "MRE_PPID"
+ "MRE_UpTime"
+ "MRE_Version"
+ "MRE_is64Bit"
+ "MemoryPool"
+ "MemoryResourceExceptionMetaData"
+ "Name"
+ "PixelFormat"
+ "ResidentSize"
+ "Size"
+ "SourceFilename"
+ "SourceLine"
+ "SurfaceID"
+ "Symbol"
+ "UUID"
+ "Width"
+ "_"
+ "checkForTimeout critical process extension #%i: analysis of critical process is not underway, run timeout operations"
+ "checkForTimeout critical process extension #%i: critical process diagnostic generation is underway, check timeout again in %i seconds"
+ "checkForTimeout critical process extension #%i: timeout extension count hit max value (%i), run timeout operations"
+ "dateWithTimeIntervalSinceNow:"
+ "keysSortedByValueUsingComparator:"
+ "path"
+ "q24@?0@\"NSURL\"8@\"NSURL\"16"
+ "rangeOfString:"
+ "sortUsingComparator:"
+ "stringWithUTF8String:"
+ "substringWithRange:"

```

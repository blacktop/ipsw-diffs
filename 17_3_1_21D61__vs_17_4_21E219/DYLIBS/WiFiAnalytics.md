## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-503.2.0.0.0
-  __TEXT.__text: 0xe6874
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0xbee4
-  __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xd71b
+510.16.0.0.0
+  __TEXT.__text: 0xe6654
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0xbf0c
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0xd9b2
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__constg_swiftt: 0x158
   __TEXT.__swift5_reflstr: 0x61
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x90a6
-  __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__unwind_info: 0x20e4
+  __TEXT.__oslogstring: 0x9346
+  __TEXT.__gcc_except_tab: 0xba8
+  __TEXT.__unwind_info: 0x20d4
   __TEXT.__eh_frame: 0x630
   __TEXT.__objc_classname: 0xa5c
-  __TEXT.__objc_methname: 0x17599
+  __TEXT.__objc_methname: 0x175e7
   __TEXT.__objc_methtype: 0x3461
-  __TEXT.__objc_stubs: 0x8ac0
+  __TEXT.__objc_stubs: 0x8ae0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x18a0
+  __DATA_CONST.__const: 0x17a0
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe858
-  __DATA_CONST.__objc_selrefs: 0x6a00
+  __DATA_CONST.__objc_const: 0xe868
+  __DATA_CONST.__objc_selrefs: 0x6a20
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__const: 0x3d0
+  __AUTH_CONST.__const: 0x390
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__cfstring: 0xab20
+  __AUTH_CONST.__cfstring: 0xab80
   __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x4d8
   __AUTH.__data: 0x28
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x418
-  __DATA.__objc_superrefs: 0x228
-  __DATA.__objc_ivar: 0xc48
-  __DATA.__data: 0x9b8
-  __DATA.__common: 0x11d8
+  __DATA.__objc_ivar: 0xc4c
+  __DATA.__data: 0xbb8
+  __DATA.__common: 0x11e8
   __DATA.__bss: 0xc
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4435
-  Symbols:   12003
-  CStrings:  7779
+  Functions: 4437
+  Symbols:   12009
+  CStrings:  7813
 
Symbols:
+ +[WAUtil initialize]
+ +[WAUtil isInternalInstall]
+ -[AnalyticsProcessor performPruneTestBSSes:]
+ -[AnalyticsStoreMOHandler pruneTestBSSes:]
+ -[WAClient allowPurgeJSONFilesAfterSec]
+ -[WAClient setAllowPurgeJSONFilesAfterSec:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table182
+ GCC_except_table93
+ _OBJC_IVAR_$_WAClient._allowPurgeJSONFilesAfterSec
+ _WALogCategoryDefaultHandle
+ _WALogCategoryDefaultHandle.defaultHandle
+ _WALogCategoryDefaultHandle.onceTokenDefault
+ ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.72
+ ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.75
+ ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.80
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.179
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.181
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.184
+ ___38-[WAClient _establishDaemonConnection]_block_invoke_2.180
+ ___38-[WAClient _establishDaemonConnection]_block_invoke_2.182
+ ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.155
+ ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.156
+ ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.150
+ ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.153
+ ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.235
+ ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.238
+ ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.157
+ ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.158
+ ___60-[WAClient _registerMessageGroup:andReply:queuedInvocation:]_block_invoke.84
+ ___63-[WAClient _submitMessage:groupType:andReply:queuedInvocation:]_block_invoke.90
+ ___63-[WAClient _submitMessage:groupType:andReply:queuedInvocation:]_block_invoke.93
+ ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.163
+ ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.164
+ ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.135
+ ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.138
+ ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.159
+ ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.162
+ ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.216
+ ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.219
+ ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.230
+ ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.233
+ ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.212
+ ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.215
+ ___74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.133
+ ___74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.134
+ ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.225
+ ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.228
+ ___78-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:]_block_invoke.86
+ ___78-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:]_block_invoke.89
+ ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.204
+ ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.207
+ ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.221
+ ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.224
+ ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.208
+ ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.211
+ ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.200
+ ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.203
+ ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.145
+ ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.148
+ ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.140
+ ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.143
+ ___Block_byref_object_copy_.57
+ ___Block_byref_object_dispose_.58
+ ___WALogCategoryDefaultHandle_block_invoke
+ ___block_descriptor_48_e8_32s_e20_v24?08"NSError"16ls32l8
+ ___block_literal_global.142
+ ___block_literal_global.147
+ ___block_literal_global.152
+ ___block_literal_global.161
+ ___block_literal_global.202
+ ___block_literal_global.223
+ ___block_literal_global.232
+ ___block_literal_global.237
+ ___block_literal_global.6
+ ___block_literal_global.88
+ ___block_literal_global.9
+ ___block_literal_global.92
+ ___error
+ __isInternalInstall
+ _clock_gettime_nsec_np
+ _fsctl
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$description
+ _objc_msgSend$groupTypeToString:
+ _objc_msgSend$hasChanges
+ _objc_msgSend$pruneTestBSSes:
+ _objc_retainAutoreleasedReturnValue
+ _strerror
+ _swift_release_n
- -[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]
- -[WAClient submitWiFiAnalyticsMessage:andReply:]
- -[WAXPCConnection submitWiFiAnalyticsMessage:andReply:]
- GCC_except_table106
- GCC_except_table111
- GCC_except_table115
- GCC_except_table119
- GCC_except_table123
- GCC_except_table124
- GCC_except_table128
- GCC_except_table183
- GCC_except_table188
- GCC_except_table47
- GCC_except_table97
- GCC_except_table99
- ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.73
- ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.76
- ___100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.81
- ___38-[WAClient _establishDaemonConnection]_block_invoke.185
- ___38-[WAClient _establishDaemonConnection]_block_invoke.187
- ___38-[WAClient _establishDaemonConnection]_block_invoke.188
- ___38-[WAClient _establishDaemonConnection]_block_invoke_2.184
- ___38-[WAClient _establishDaemonConnection]_block_invoke_2.186
- ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.159
- ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.160
- ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.157
- ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.158
- ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.242
- ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.243
- ___55-[WAXPCConnection submitWiFiAnalyticsMessage:andReply:]_block_invoke
- ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.161
- ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.162
- ___60-[WAClient _registerMessageGroup:andReply:queuedInvocation:]_block_invoke_2
- ___63-[WAClient _submitMessage:groupType:andReply:queuedInvocation:]_block_invoke.89
- ___63-[WAClient _submitMessage:groupType:andReply:queuedInvocation:]_block_invoke.92
- ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.167
- ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.168
- ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.142
- ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.143
- ___66-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]_block_invoke
- ___66-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]_block_invoke.135
- ___66-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]_block_invoke.138
- ___66-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]_block_invoke_2
- ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.163
- ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.166
- ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.223
- ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.224
- ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.237
- ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.238
- ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.216
- ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.219
- ___74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.129
- ___74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.132
- ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.232
- ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.233
- ___78-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:]_block_invoke.85
- ___78-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:]_block_invoke.88
- ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.208
- ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.211
- ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.225
- ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.228
- ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.212
- ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.215
- ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.204
- ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.207
- ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.152
- ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.153
- ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.147
- ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.148
- ___Block_byref_object_copy_.58
- ___Block_byref_object_dispose_.59
- ___block_descriptor_32_e20_v24?08"NSError"16l
- ___block_literal_global.131
- ___block_literal_global.134
- ___block_literal_global.141
- ___block_literal_global.146
- ___block_literal_global.151
- ___block_literal_global.156
- ___block_literal_global.165
- ___block_literal_global.222
- ___block_literal_global.231
- ___block_literal_global.236
- ___block_literal_global.241
- ___block_literal_global.7
- ___block_literal_global.87
- ___block_literal_global.91
- _objc_msgSend$_submitWiFiAnalyticsMessage:andReply:queuedInvocation:
- _objc_msgSend$deriveBadRoams:
- _objc_msgSend$predictPath:
- _objc_msgSend$submitWiFiAnalyticsMessage:andReply:
- _objc_msgSend$xpcConnection:submitWiFiAnalyticsMessage:andReply:
CStrings:
+ "%{public}s::%d:Deleting all %@ older than %ld days"
+ "%{public}s::%d:Deleting all %@ older than:%ld days"
+ "%{public}s::%d:Deleting all %@ where %@"
+ "%{public}s::%d:Deleting all %@ with no BSSes"
+ "%{public}s::%d:Failed to mark %s as purgeable with flags 0x%llx, supplemental 0x%llx, notBeforeDate:%@: (%d) %s\n"
+ "%{public}s::%d:Marked %s purgeable with flags 0x%llx (supplemental 0x%llx notBeforeDate:%@)\n"
+ "%{public}s::%d:No changes to be saved"
+ "%{public}s::%d:ProcessJournalImmediately"
+ "%{public}s::%d:Saved context"
+ "%{public}s::%d:Successfully Sent %@"
+ "%{public}s::%d:WAClient - FAILED to submitWiFiAnalyticsMessageAdvanced:%@ - error: %@"
+ "%{public}s::%d:XPC: Daemon connection not valid, connection establishment about to be initiated... (%@ has been written on disk but XPC won't be called)"
+ "%{public}s::%d:XPC: WAClient - registerMessageGroup - %@ - DONE"
+ "%{public}s::%d:XPC: WAClient - submitWiFiAnalyticsMessageAdvanced:%@ - error: %@"
+ "%{public}s::%d:[BSS:%@ SSID:%@] Added Channel %@ Band %@"
+ "%{public}s::%d:[BSS:%@ SSID:%@] Updated neighborChannels: %@"
+ "%{public}s::%d:[moc: %@] Inserted new %@"
+ "%{public}s::%d:message(%@)[%@]:%@"
+ "+[AnalyticsStoreProxy createEntity:moc:]_block_invoke"
+ "-[AnalyticsStoreMOHandler ageOutManagedObjectsOlderThan:]"
+ "-[AnalyticsStoreMOHandler pruneTestBSSes:]"
+ "CODE FIX NEEDED! Field cannot be sent to CoreAnalytics, removing CA option from field %@ (%@): %@"
+ "Can't construct Array with count < 0"
+ "Insufficient space allocated to copy string contents"
+ "InternalBuild"
+ "SELF.bssid == %@"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Td,N,V_allowPurgeJSONFilesAfterSec"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_allowPurgeJSONFilesAfterSec"
+ "allowPurgeJSONFilesAfterSec"
+ "cStringUsingEncoding:"
+ "dateWithTimeIntervalSince1970:"
+ "initialize"
+ "invalid Collection: less than 'count' elements in collection"
+ "performPruneTestBSSes:"
+ "pruneTestBSSes:"
+ "setAllowPurgeJSONFilesAfterSec:"
+ "xctests"
- "%{public}s::%d:Cannot send field %@ (%@) to CA, removing CA option from field"
- "%{public}s::%d:WAClient - FAILED to submitWiFiAnalyticsMessageAdvanced - error: %@"
- "%{public}s::%d:XPC: Daemon connection not valid, connection establishment about to be initiated..."
- "%{public}s::%d:XPC: WAClient - submitWiFiAnalyticsMessage - error: %@"
- "%{public}s::%d:XPC: WAClient - submitWiFiAnalyticsMessageAdvanced - error: %@"
- "%{public}s::%d:backgroundReadingMOC nil"
- "%{public}s::%d:message[%@]:%@"
- "%{public}s::%d:processJournalsImmediately:%@ (message[%@]:%@)"
- "-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]"
- "-[WAClient _submitWiFiAnalyticsMessage:andReply:queuedInvocation:]_block_invoke"
- "-[WAMessage addFieldsFromDictionary:options:]"
- "DiffifIfStats_txLatencyBE_"
- "_submitWiFiAnalyticsMessage:andReply:queuedInvocation:"
- "submitWiFiAnalyticsMessage:andReply:"
- "xpcConnection:submitWiFiAnalyticsMessage:andReply:"

```

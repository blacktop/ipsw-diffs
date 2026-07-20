## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-174.0.0.0.0
-  __TEXT.__text: 0x56c98
-  __TEXT.__objc_methlist: 0x412c
-  __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x5e07
-  __TEXT.__oslogstring: 0xeffa
-  __TEXT.__gcc_except_tab: 0x106c
-  __TEXT.__unwind_info: 0xfa0
+177.0.8.502.1
+  __TEXT.__text: 0x5aeec
+  __TEXT.__objc_methlist: 0x4634
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x6075
+  __TEXT.__gcc_except_tab: 0x10c4
+  __TEXT.__oslogstring: 0xf32a
+  __TEXT.__unwind_info: 0x1088
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2710
+  __DATA_CONST.__objc_selrefs: 0x2a20
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x2200
-  __DATA_CONST.__got: 0x310
-  __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x5fe0
-  __AUTH_CONST.__objc_const: 0x59b0
+  __DATA_CONST.__got: 0x328
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x6300
+  __AUTH_CONST.__objc_const: 0x61b0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x4b4
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x530
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xc0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x208

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 1951
-  Symbols:   3324
-  CStrings:  1831
+  Functions: 2065
+  Symbols:   3586
+  CStrings:  1872
 
Symbols:
+ +[CSBoostMonitorConfig alwaysWatchProcessNames]
+ +[CSBoostObserver sharedObserver]
+ -[CSBoostCounters .cxx_destruct]
+ -[CSBoostCounters bumpKind:]
+ -[CSBoostCounters currentWindowBypassTicks]
+ -[CSBoostCounters currentWindowImportanceOnlyTicks]
+ -[CSBoostCounters currentWindowIsPartial]
+ -[CSBoostCounters currentWindowPImpTicks]
+ -[CSBoostCounters currentWindowPThrTicks]
+ -[CSBoostCounters currentWindowStartTime]
+ -[CSBoostCounters eventCountsAfterMitigation]
+ -[CSBoostCounters eventCountsBeforeFirstMitigation]
+ -[CSBoostCounters eventCountsDuringMitigation]
+ -[CSBoostCounters firstMitigation]
+ -[CSBoostCounters firstSeen]
+ -[CSBoostCounters importanceOnlyTicks]
+ -[CSBoostCounters init]
+ -[CSBoostCounters isCurrentlyMitigated]
+ -[CSBoostCounters isWatched]
+ -[CSBoostCounters lastEvent]
+ -[CSBoostCounters lastMitigation]
+ -[CSBoostCounters mutableAfter]
+ -[CSBoostCounters mutableBefore]
+ -[CSBoostCounters mutableCallerPids]
+ -[CSBoostCounters mutableDuring]
+ -[CSBoostCounters mutablePromotion]
+ -[CSBoostCounters pid]
+ -[CSBoostCounters processName]
+ -[CSBoostCounters promotionQosHistogram]
+ -[CSBoostCounters recordCallerPid:]
+ -[CSBoostCounters recordPromotionQos:]
+ -[CSBoostCounters setCurrentWindowBypassTicks:]
+ -[CSBoostCounters setCurrentWindowImportanceOnlyTicks:]
+ -[CSBoostCounters setCurrentWindowIsPartial:]
+ -[CSBoostCounters setCurrentWindowPImpTicks:]
+ -[CSBoostCounters setCurrentWindowPThrTicks:]
+ -[CSBoostCounters setCurrentWindowStartTime:]
+ -[CSBoostCounters setFirstMitigation:]
+ -[CSBoostCounters setFirstSeen:]
+ -[CSBoostCounters setImportanceOnlyTicks:]
+ -[CSBoostCounters setIsCurrentlyMitigated:]
+ -[CSBoostCounters setIsWatched:]
+ -[CSBoostCounters setLastEvent:]
+ -[CSBoostCounters setLastMitigation:]
+ -[CSBoostCounters setMutableAfter:]
+ -[CSBoostCounters setMutableBefore:]
+ -[CSBoostCounters setMutableCallerPids:]
+ -[CSBoostCounters setMutableDuring:]
+ -[CSBoostCounters setMutablePromotion:]
+ -[CSBoostCounters setPid:]
+ -[CSBoostCounters setProcessName:]
+ -[CSBoostCounters setWatchReasons:]
+ -[CSBoostCounters totalEventsAllPhases]
+ -[CSBoostCounters uniqueCallers]
+ -[CSBoostCounters watchReasons]
+ -[CSBoostObserver .cxx_destruct]
+ -[CSBoostObserver addMonitoredPid:name:]
+ -[CSBoostObserver addRecentlyMitigatedWatchForPid:name:]
+ -[CSBoostObserver addWatchedPid:name:reason:]
+ -[CSBoostObserver allObservedPids]
+ -[CSBoostObserver countersForPidLocked:name:]
+ -[CSBoostObserver finalizeAndRemoveMonitoredPid:issueType:]
+ -[CSBoostObserver findPidForName:]
+ -[CSBoostObserver init]
+ -[CSBoostObserver loadConfigList]
+ -[CSBoostObserver logger]
+ -[CSBoostObserver lookupProcessName:]
+ -[CSBoostObserver pidExited:]
+ -[CSBoostObserver pidIsObservedLocked:]
+ -[CSBoostObserver pollAllObserved]
+ -[CSBoostObserver pollOnePid:]
+ -[CSBoostObserver pollTimer]
+ -[CSBoostObserver qosFromBasepri:]
+ -[CSBoostObserver recordEventLocked:pid:callerPid:promQos:]
+ -[CSBoostObserver removeMonitoredPid:]
+ -[CSBoostObserver removeWatchedPid:reason:]
+ -[CSBoostObserver resetAllCounters]
+ -[CSBoostObserver resetCountersForPid:]
+ -[CSBoostObserver seedMitigatedPid:name:]
+ -[CSBoostObserver setLogger:]
+ -[CSBoostObserver setPollTimer:]
+ -[CSBoostObserver setWorkQueue:]
+ -[CSBoostObserver snapshotForPid:]
+ -[CSBoostObserver snapshot]
+ -[CSBoostObserver startPollTimer]
+ -[CSBoostObserver start]
+ -[CSBoostObserver walkThreadsForPid:]
+ -[CSBoostObserver watchedPids]
+ -[CSBoostObserver workQueue]
+ -[CSRestrictionManager addBoostWatchForPid:name:reason:reply:]
+ -[CSRestrictionManager getBoostObservationsForPid:reply:]
+ -[CSRestrictionManager removeBoostWatchForPid:reason:reply:]
+ -[CSRestrictionManager resetBoostCountersForPid:reply:]
+ -[CSRestrictionManager stringifyCountDict:]
+ -[CSTriggerManager _clearSysdiagnoseSuppressionForGeneration:]
+ -[CSTriggerManager setSysdiagnoseEventGeneration:]
+ -[CSTriggerManager sysdiagnoseEventGeneration]
+ -[NSDictionary(CSNullSafe) cs_numberForKey:]
+ -[NSDictionary(CSNullSafe) cs_stringForKey:]
+ GCC_except_table104
+ GCC_except_table15
+ GCC_except_table153
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table178
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table59
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table87
+ GCC_except_table91
+ GCC_except_table99
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_CSBoostCounters
+ _OBJC_CLASS_$_CSBoostMonitorConfig
+ _OBJC_CLASS_$_CSBoostObserver
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowBypassTicks
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowImportanceOnlyTicks
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowIsPartial
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowPImpTicks
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowPThrTicks
+ _OBJC_IVAR_$_CSBoostCounters._currentWindowStartTime
+ _OBJC_IVAR_$_CSBoostCounters._firstMitigation
+ _OBJC_IVAR_$_CSBoostCounters._firstSeen
+ _OBJC_IVAR_$_CSBoostCounters._importanceOnlyTicks
+ _OBJC_IVAR_$_CSBoostCounters._isCurrentlyMitigated
+ _OBJC_IVAR_$_CSBoostCounters._isWatched
+ _OBJC_IVAR_$_CSBoostCounters._lastEvent
+ _OBJC_IVAR_$_CSBoostCounters._lastMitigation
+ _OBJC_IVAR_$_CSBoostCounters._mutableAfter
+ _OBJC_IVAR_$_CSBoostCounters._mutableBefore
+ _OBJC_IVAR_$_CSBoostCounters._mutableCallerPids
+ _OBJC_IVAR_$_CSBoostCounters._mutableDuring
+ _OBJC_IVAR_$_CSBoostCounters._mutablePromotion
+ _OBJC_IVAR_$_CSBoostCounters._pid
+ _OBJC_IVAR_$_CSBoostCounters._processName
+ _OBJC_IVAR_$_CSBoostCounters._watchReasons
+ _OBJC_IVAR_$_CSBoostObserver._counters
+ _OBJC_IVAR_$_CSBoostObserver._lock
+ _OBJC_IVAR_$_CSBoostObserver._logger
+ _OBJC_IVAR_$_CSBoostObserver._monitoredPids
+ _OBJC_IVAR_$_CSBoostObserver._pollTimer
+ _OBJC_IVAR_$_CSBoostObserver._watchGenerations
+ _OBJC_IVAR_$_CSBoostObserver._watchReasons
+ _OBJC_IVAR_$_CSBoostObserver._watchedPids
+ _OBJC_IVAR_$_CSBoostObserver._workQueue
+ _OBJC_IVAR_$_CSTriggerManager._sysdiagnoseEventGeneration
+ _OBJC_METACLASS_$_CSBoostCounters
+ _OBJC_METACLASS_$_CSBoostMonitorConfig
+ _OBJC_METACLASS_$_CSBoostObserver
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_CSNullSafe
+ __OBJC_$_CATEGORY_NSDictionary_$_CSNullSafe
+ __OBJC_$_CLASS_METHODS_CSBoostMonitorConfig
+ __OBJC_$_CLASS_METHODS_CSBoostObserver
+ __OBJC_$_INSTANCE_METHODS_CSBoostCounters
+ __OBJC_$_INSTANCE_METHODS_CSBoostObserver
+ __OBJC_$_INSTANCE_VARIABLES_CSBoostCounters
+ __OBJC_$_INSTANCE_VARIABLES_CSBoostObserver
+ __OBJC_$_PROP_LIST_CSBoostCounters
+ __OBJC_$_PROP_LIST_CSBoostObserver
+ __OBJC_CLASS_RO_$_CSBoostCounters
+ __OBJC_CLASS_RO_$_CSBoostMonitorConfig
+ __OBJC_CLASS_RO_$_CSBoostObserver
+ __OBJC_METACLASS_RO_$_CSBoostCounters
+ __OBJC_METACLASS_RO_$_CSBoostMonitorConfig
+ __OBJC_METACLASS_RO_$_CSBoostObserver
+ ___24-[CSBoostObserver start]_block_invoke
+ ___27-[CSBoostObserver snapshot]_block_invoke
+ ___33+[CSBoostObserver sharedObserver]_block_invoke
+ ___33-[CSBoostObserver startPollTimer]_block_invoke
+ ___43-[CSRestrictionManager stringifyCountDict:]_block_invoke
+ ___44-[CSTriggerManager handleSysdiagnoseStopped]_block_invoke
+ ___47+[CSBoostMonitorConfig alwaysWatchProcessNames]_block_invoke
+ ___55-[CSRestrictionManager resetBoostCountersForPid:reply:]_block_invoke
+ ___56-[CSBoostObserver addRecentlyMitigatedWatchForPid:name:]_block_invoke
+ ___57-[CSRestrictionManager getBoostObservationsForPid:reply:]_block_invoke
+ ___59-[CSBoostObserver finalizeAndRemoveMonitoredPid:issueType:]_block_invoke
+ ___60-[CSRestrictionManager removeBoostWatchForPid:reason:reply:]_block_invoke
+ ___62-[CSRestrictionManager addBoostWatchForPid:name:reason:reply:]_block_invoke
+ ___block_descriptor_104_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e45_q24?0"CSBoostCounters"8"CSBoostCounters"16ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_52_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_60_e8_32s40w_e5_v8?0lw40l8s32l8
+ _alwaysWatchProcessNames.cached
+ _alwaysWatchProcessNames.once
+ _objc_msgSend$_clearSysdiagnoseSuppressionForGeneration:
+ _objc_msgSend$addMonitoredPid:name:
+ _objc_msgSend$addRecentlyMitigatedWatchForPid:name:
+ _objc_msgSend$addWatchedPid:name:reason:
+ _objc_msgSend$allObservedPids
+ _objc_msgSend$alwaysWatchProcessNames
+ _objc_msgSend$bumpKind:
+ _objc_msgSend$countersForPidLocked:name:
+ _objc_msgSend$cs_numberForKey:
+ _objc_msgSend$cs_stringForKey:
+ _objc_msgSend$currentWindowBypassTicks
+ _objc_msgSend$currentWindowImportanceOnlyTicks
+ _objc_msgSend$currentWindowIsPartial
+ _objc_msgSend$currentWindowPImpTicks
+ _objc_msgSend$currentWindowPThrTicks
+ _objc_msgSend$currentWindowStartTime
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$distantPast
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$eventCountsAfterMitigation
+ _objc_msgSend$eventCountsBeforeFirstMitigation
+ _objc_msgSend$eventCountsDuringMitigation
+ _objc_msgSend$finalizeAndRemoveMonitoredPid:issueType:
+ _objc_msgSend$findPidForName:
+ _objc_msgSend$firstMitigation
+ _objc_msgSend$firstSeen
+ _objc_msgSend$importanceOnlyTicks
+ _objc_msgSend$isCurrentlyMitigated
+ _objc_msgSend$isWatched
+ _objc_msgSend$lastEvent
+ _objc_msgSend$lastMitigation
+ _objc_msgSend$loadConfigList
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$pid
+ _objc_msgSend$pidExited:
+ _objc_msgSend$pidIsObservedLocked:
+ _objc_msgSend$pollAllObserved
+ _objc_msgSend$pollOnePid:
+ _objc_msgSend$pollTimer
+ _objc_msgSend$promotionQosHistogram
+ _objc_msgSend$qosFromBasepri:
+ _objc_msgSend$recordCallerPid:
+ _objc_msgSend$recordEventLocked:pid:callerPid:promQos:
+ _objc_msgSend$recordPromotionQos:
+ _objc_msgSend$removeWatchedPid:reason:
+ _objc_msgSend$resetAllCounters
+ _objc_msgSend$resetCountersForPid:
+ _objc_msgSend$seedMitigatedPid:name:
+ _objc_msgSend$setCurrentWindowBypassTicks:
+ _objc_msgSend$setCurrentWindowImportanceOnlyTicks:
+ _objc_msgSend$setCurrentWindowIsPartial:
+ _objc_msgSend$setCurrentWindowPImpTicks:
+ _objc_msgSend$setCurrentWindowPThrTicks:
+ _objc_msgSend$setCurrentWindowStartTime:
+ _objc_msgSend$setFirstMitigation:
+ _objc_msgSend$setImportanceOnlyTicks:
+ _objc_msgSend$setIsCurrentlyMitigated:
+ _objc_msgSend$setIsWatched:
+ _objc_msgSend$setLastEvent:
+ _objc_msgSend$setLastMitigation:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setPollTimer:
+ _objc_msgSend$setWatchReasons:
+ _objc_msgSend$sharedObserver
+ _objc_msgSend$snapshot
+ _objc_msgSend$snapshotForPid:
+ _objc_msgSend$start
+ _objc_msgSend$startPollTimer
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringifyCountDict:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$totalEventsAllPhases
+ _objc_msgSend$uniqueCallers
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSend$walkThreadsForPid:
+ _objc_msgSend$watchReasons
+ _objc_msgSend$workQueue
+ _os_variant_has_internal_content
+ _proc_listallpids
+ _proc_name
+ _sharedObserver.inst
+ _sharedObserver.once
+ _strcmp
- -[CSProcessManager getPollPIDsCount]
- GCC_except_table102
- GCC_except_table152
- GCC_except_table154
- GCC_except_table158
- GCC_except_table20
- GCC_except_table25
- GCC_except_table29
- GCC_except_table45
- GCC_except_table47
- GCC_except_table56
- GCC_except_table58
- GCC_except_table80
- GCC_except_table82
- GCC_except_table89
- GCC_except_table97
- _CFBooleanGetValue
- _MGCopyAnswer
- _objc_msgSend$getPollPIDsCount
CStrings:
+ "/Library/Preferences/com.apple.powerexceptions/boost-watch.plist"
+ "?"
+ "Active"
+ "AlwaysWatch"
+ "BoostObserver"
+ "BypassActiveSeconds"
+ "BypassFractionPct"
+ "BypassIntensityTicks"
+ "ImportanceHeldSeconds"
+ "ImportanceOnlyPct"
+ "ImportanceOnlySeconds"
+ "MitigationDurationSeconds"
+ "SELECT timestamp, Active FROM PLDisplayAgent_EventPoint_Display WHERE Block = 'Backlight' AND timestamp >= %f - 300 AND timestamp <= %f ORDER BY timestamp"
+ "SELECT timestamp, Start FROM ConfigMetrics_SysdiagnoseEvent_1_2 WHERE timestamp >= %f - %f AND timestamp < %f ORDER by timestamp"
+ "SYSDIAGNOSE: Sysdiagnose stopped — keeping detection suppressed for %d s TTR extension"
+ "SYSDIAGNOSE: TTR extension clear superseded by newer event — ignoring"
+ "SYSDIAGNOSE: TTR extension elapsed — resuming detection"
+ "addMonitoredPid: pid=%d (%{public}@)"
+ "com.apple.computesafeguards.boost-observer"
+ "com.apple.powerexceptions"
+ "com.apple.powerexceptions.boost_observation"
+ "countsAfter"
+ "countsBefore"
+ "countsDuring"
+ "finalizeAndRemoveMonitoredPid: pid=%d (%{public}@) issueType=%ld dur=%llds pImp=%llu bypass=%llu (%lld%%) pThr=%llu impOnly=%llu (%lld%%)"
+ "firstMitigation"
+ "firstSeen"
+ "handleProcessStart: no tracked PIDs for coalitionID %lld and could not discover current PID for process:%@, pending mitigation will retry on next relaunch"
+ "handleProcessStart: no tracked PIDs for coalitionID %lld on relaunch for process:%@, registering discovered PID:%d"
+ "importanceOnlyTicks"
+ "isCurrentlyMitigated"
+ "isWatched"
+ "lastEvent"
+ "lastMitigation"
+ "loadConfigList: loaded %lu always-watch entries"
+ "promotionHist"
+ "q24@?0@\"CSBoostCounters\"8@\"CSBoostCounters\"16"
+ "removeMonitoredPid: pid=%d"
+ "seedMitigatedPid: pid=%d (%{public}@)"
+ "startPollTimer: 1Hz poll started"
+ "totalEvents"
+ "uniqueCallers"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "walkThreadsForPid: pid=%d thread list may be truncated at 256"
+ "watchReasons"
- "SELECT timestamp, Start FROM ConfigMetrics_SysdiagnoseEvent_1_2 WHERE timestamp >= %f - 300 AND timestamp < %f ORDER by timestamp"
- "SELECT timestamp, timestampEnd FROM PLDisplayAgent_EventPoint_Display WHERE Active = 1 AND timestampEnd >= %f AND timestamp <= %f ORDER BY timestamp"
- "SYSDIAGNOSE: Sysdiagnose stopped — resuming detection"
- "apple-internal-install"
```

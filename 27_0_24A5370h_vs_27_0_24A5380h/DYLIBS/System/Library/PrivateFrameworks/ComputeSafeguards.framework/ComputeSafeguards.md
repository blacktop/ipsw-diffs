## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-  __TEXT.__text: 0x56250
-  __TEXT.__objc_methlist: 0x3ed4
-  __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x5e0e
-  __TEXT.__oslogstring: 0xe2fa
-  __TEXT.__gcc_except_tab: 0xf10
-  __TEXT.__unwind_info: 0xf38
+  __TEXT.__text: 0x56c98
+  __TEXT.__objc_methlist: 0x412c
+  __TEXT.__const: 0x308
+  __TEXT.__cstring: 0x5e07
+  __TEXT.__oslogstring: 0xeffa
+  __TEXT.__gcc_except_tab: 0x106c
+  __TEXT.__unwind_info: 0xfa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x140
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25f0
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x2530
-  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__objc_selrefs: 0x2710
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x2200
+  __DATA_CONST.__got: 0x310
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x6080
-  __AUTH_CONST.__objc_const: 0x5680
-  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__cfstring: 0x5fe0
+  __AUTH_CONST.__objc_const: 0x59b0
+  __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x550
-  __AUTH_CONST.__objc_arrayobj: 0x318
+  __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x494
-  __DATA.__data: 0x4f8
-  __DATA.__bss: 0xc8
+  __DATA.__objc_ivar: 0x4b4
+  __DATA.__data: 0x5b8
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x910
+  __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 1908
-  Symbols:   5801
-  CStrings:  2578
+  Functions: 1951
+  Symbols:   5943
+  CStrings:  2612
 
Sections:
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ -[CSMitigationManager isInternalBuild]
+ -[CSMitigationManager releaseOrphanedThrottledPIDs]
+ -[CSMitigationManager restorePenaltyBoxFromPowerlog]
+ -[CSNavigationListener .cxx_destruct]
+ -[CSNavigationListener delegate]
+ -[CSNavigationListener initWithDispatchQueue:]
+ -[CSNavigationListener logger]
+ -[CSNavigationListener navigating]
+ -[CSNavigationListener navigationListener:didChangeNavigationState:transportType:]
+ -[CSNavigationListener navigationListener]
+ -[CSNavigationListener queue]
+ -[CSNavigationListener setDelegate:]
+ -[CSNavigationListener setLogger:]
+ -[CSNavigationListener setNavigating:]
+ -[CSNavigationListener setNavigationListener:]
+ -[CSNavigationListener setQueue:]
+ -[CSNavigationListener startMonitoring]
+ -[CSProcessManager getPowerlogRecords]
+ -[CSProcessManager injectPowerlogRecordsForTesting:]
+ -[CSProcessManager pendingRestoreByUUID]
+ -[CSProcessManager seedPendingRestoreForUUID:withData:]
+ -[CSProcessManager setPendingRestoreByUUID:]
+ -[CSProcessManager setTargetProcessRecordsForTesting:withProcessName:]
+ -[CSRestrictionManager _resolveDASCoalitionIDForProcessName:]
+ -[CSRestrictionManager applyNavigatingState:]
+ -[CSRestrictionManager dasExemptCoalitionIDsForSlotStamp]
+ -[CSRestrictionManager liftMitigationsForRestoredDASIntensiveProcesses]
+ -[CSRestrictionManager navigationListener:didChangeNavigatingState:]
+ -[CSRestrictionManager navigationListener]
+ -[CSRestrictionManager previousDASExemptCoalitionIDs]
+ -[CSRestrictionManager setNavigationListener:]
+ -[CSRestrictionManager setPreviousDASExemptCoalitionIDs:]
+ -[CSRestrictionManager startNavigationMonitoring]
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table158
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table69
+ GCC_except_table80
+ GCC_except_table82
+ _OBJC_CLASS_$_CSNavigationListener
+ _OBJC_CLASS_$_GEONavigationListener
+ _OBJC_IVAR_$_CSNavigationListener._delegate
+ _OBJC_IVAR_$_CSNavigationListener._logger
+ _OBJC_IVAR_$_CSNavigationListener._navigating
+ _OBJC_IVAR_$_CSNavigationListener._navigationListener
+ _OBJC_IVAR_$_CSNavigationListener._queue
+ _OBJC_IVAR_$_CSProcessManager._pendingRestoreByUUID
+ _OBJC_IVAR_$_CSRestrictionManager._navigationListener
+ _OBJC_IVAR_$_CSRestrictionManager._previousDASExemptCoalitionIDs
+ _OBJC_METACLASS_$_CSNavigationListener
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ __OBJC_$_INSTANCE_METHODS_CSNavigationListener
+ __OBJC_$_INSTANCE_VARIABLES_CSNavigationListener
+ __OBJC_$_PROP_LIST_CSNavigationListener
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSNavigationListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_GEONavigationListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSNavigationListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEONavigationListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSNavigationListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_GEONavigationListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CSNavigationListener
+ __OBJC_CLASS_RO_$_CSNavigationListener
+ __OBJC_LABEL_PROTOCOL_$_CSNavigationListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_GEONavigationListenerDelegate
+ __OBJC_METACLASS_RO_$_CSNavigationListener
+ __OBJC_PROTOCOL_$_CSNavigationListenerDelegate
+ __OBJC_PROTOCOL_$_GEONavigationListenerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_GEONavigationListenerDelegate
+ ___41-[CSRestrictionManager loadAppExemptions]_block_invoke
+ ___46-[CSRestrictionManager _initWithDataProvider:]_block_invoke
+ ___52-[CSMitigationManager restorePenaltyBoxFromPowerlog]_block_invoke
+ _objc_msgSend$_resolveDASCoalitionIDForProcessName:
+ _objc_msgSend$appMonitor
+ _objc_msgSend$applyNavigatingState:
+ _objc_msgSend$bgDaemonsByBundleID
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$dasExemptCoalitionIDsForSlotStamp
+ _objc_msgSend$fgDaemonsByBundleID
+ _objc_msgSend$getPowerlogRecords
+ _objc_msgSend$initWithDispatchQueue:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$liftMitigationsForRestoredDASIntensiveProcesses
+ _objc_msgSend$navigating
+ _objc_msgSend$navigationListener:didChangeNavigatingState:
+ _objc_msgSend$navigationState
+ _objc_msgSend$releaseOrphanedThrottledPIDs
+ _objc_msgSend$restorePenaltyBoxFromPowerlog
+ _objc_msgSend$seedPendingRestoreForUUID:withData:
+ _objc_msgSend$startNavigationMonitoring
+ _objc_msgSend$stateForBundleID:
+ _objc_msgSend$valueForEntitlement:
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[CSIssueDetector initializeCPUDetectionRulesHardcoded]
- GCC_except_table11
- GCC_except_table149
- GCC_except_table153
- GCC_except_table19
- GCC_except_table24
- GCC_except_table26
- GCC_except_table28
- GCC_except_table30
- GCC_except_table36
- GCC_except_table38
- GCC_except_table41
- GCC_except_table44
- GCC_except_table46
- GCC_except_table51
- GCC_except_table75
- GCC_except_table79
- GCC_except_table81
- _OBJC_CLASS_$_NSPredicate
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$dasExemptCoalitionIDs
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$initializeCPUDetectionRulesHardcoded
- _objc_msgSend$predicateWithFormat:
CStrings:
+ "                             SELECT *                             FROM XPCMetrics_CPUViolations_1_2 WHERE timestamp >= %f AND timestamp <= %f ORDER BY timestamp ASC"
+ "#"
+ "443"
+ "444"
+ "445"
+ "446"
+ "447"
+ "448"
+ "449"
+ "450"
+ "451"
+ "452"
+ "453"
+ "454"
+ "455"
+ "456"
+ "457"
+ "458"
+ "459"
+ "460"
+ "461"
+ "462"
+ "463"
+ "464"
+ "465"
+ "466"
+ "467"
+ "468"
+ "469"
+ "CSNavigationListener"
+ "DAS: '%@' departing without resolvable CID — no carry-forward"
+ "DAS: carry-forward CID %llu for departing '%@'"
+ "ExemptedNavigating"
+ "Failed to load rules from %@: %@. No CPU detection rules will be active."
+ "Initialized %lu primary rules from JSON + hardcoded Rule 3"
+ "NavigationEnded"
+ "Process %d missing %{public}@ entitlement, rejecting connection"
+ "SOUND RECOGNITION: Already running at startup, seeding active state"
+ "applyNavigatingState: %@ not running, skipping"
+ "applyNavigatingState: discovered %@ at pid=%d, registering"
+ "applyNavigatingState: entered navigating=%d"
+ "applyNavigatingState: lifting mitigations for %@"
+ "applyNavigatingState: restoring mitigations for %@"
+ "checkPenaltyBoxProcessesExpiration: %@ has active per-process timer but midnight policy overrides"
+ "com.apple.computesafeguards.managing.allow"
+ "didChangeNavigationState ENTRY: state=%ld transportType=%ld _navigating=%d"
+ "didChangeNavigationState: state=%ld did not change navigating bit (%d), early return"
+ "didChangeNavigationState: state=%ld transportType=%ld navigating=%d"
+ "isProcessAllowed: Process: %@ (%@) is externally exempt for CPUCoalition, respecting trials"
+ "liftMitigationsForRestoredDASIntensiveProcesses: lifting %lu restored DAS-intensive process(es)"
+ "loadAppExemptions: %@ is background-running at startup, lifting restored penalty box mitigations"
+ "loadAppExemptions: %@ is in foreground at startup, lifting restored penalty box mitigations"
+ "navd"
+ "navigating"
+ "navigationListener:didChangeNavigatingState: navigating=%d"
+ "passedStaticChecks"
+ "pollSpecificProcessWithPID: Applied pending fatalCnt=%d to %@ from pre-restart record"
+ "pollSpecificProcessWithPID: Applied pending penaltyBoxEndTime=%llu (%llu seconds remaining) to %@ from pre-restart record"
+ "pollSpecificProcessWithPID: Pending BgQoS restore for %@ has expired (endTime=%llu now=%llu), discarding"
+ "registerUserActivityLevelObserver: user already active at startup, lifting mitigations for %@"
+ "releaseOrphanedThrottledPIDs: PID:%d is in active penalty box, skipping"
+ "releaseOrphanedThrottledPIDs: Released orphaned throttled PID:%d"
+ "releaseOrphanedThrottledPIDs: Sweep complete — %d throttled found, %d orphaned released"
+ "releaseOrphanedThrottledPIDs: Sweep complete — %d throttled found, none orphaned"
+ "releaseOrphanedThrottledPIDs: malloc failed"
+ "releaseOrphanedThrottledPIDs: proc_listpids failed to fill PID list"
+ "releaseOrphanedThrottledPIDs: proc_listpids failed to get buffer size"
+ "releaseOrphanedThrottledPIDs: setpriority failed for PID:%d errno:%d"
+ "restorePenaltyBoxFromPowerlog: %@ not running — issueType=%d durationMins=%ld endTime=%llu now=%llu windowOpen=%s"
+ "restorePenaltyBoxFromPowerlog: Fatal record for %@ (uuid=%@ fatalCnt=%d)"
+ "restorePenaltyBoxFromPowerlog: Flushing powerlog tables"
+ "restorePenaltyBoxFromPowerlog: Missing uuid or name, skipping record: %@"
+ "restorePenaltyBoxFromPowerlog: No powerlog records to restore"
+ "restorePenaltyBoxFromPowerlog: PLQueryRegistered timed out after %lld seconds, continuing without flush"
+ "restorePenaltyBoxFromPowerlog: Restored %@ to penalty box (penaltyBoxEndTime=%llu)"
+ "restorePenaltyBoxFromPowerlog: Restored fatal counters for %@ (cpuFatalCnt=%u)"
+ "restorePenaltyBoxFromPowerlog: Seeded pending BgQoS restore for non-running %@ (windowRemainingSeconds=%llu uuid=%@)"
+ "restorePenaltyBoxFromPowerlog: Seeded pending fatal restore for non-running %@ (fatalCnt=%d uuid=%@)"
+ "restorePenaltyBoxFromPowerlog: Window expired for non-running %@, skipping"
+ "startMonitoring: GEONavigationListener=%p delegate=%p (self) conformsToProtocol=%d respondsToSelector=%d"
+ "startMonitoring: initial navigationState=%ld navigating=%d"
+ "startNavigationMonitoring: navigation already active at launch, lifting navd"
+ "startNavigationMonitoring: no active navigation at launch (synchronous sample)"
- "                             SELECT *                             FROM XPCMetrics_CPUViolations_1_2 where timestamp >= %f AND timestamp <= %f"
- ".*camerad"
- "10"
- "11"
- "12"
- "13"
- "14"
- "15"
- "16"
- "17"
- "18"
- "19"
- "2"
- "20"
- "21"
- "22"
- "23"
- "24"
- "25"
- "26"
- "27"
- "28"
- "29"
- "30"
- "4"
- "5"
- "6"
- "7"
- "8"
- "9"
- "Failed to load rules from %@: %@"
- "Initialized %lu primary rules from JSON + hardcoded Rule 3 + Rule 29 + Rule 30"
- "Invalid charging deny regex pattern: %@, error: %@"
- "Invalid regex pattern: %@, error: %@"
- "NOT SELF IN %@"
- "O"
- "com.apple.Maps"
- "com.apple.navd"
- "com.apple.newsd"
- "com.apple.spotlightknowledged.updater"
- "coreautomationd?\\..*|^com\\.openssh\\.sshd\\."
- "isProcessAllowed: Process:%@ is externally exempt for CPUCoalition, respecting trials"
- "safeguards_json_rules"
- "|^(com\\.apple\\.)?driver\\."

```

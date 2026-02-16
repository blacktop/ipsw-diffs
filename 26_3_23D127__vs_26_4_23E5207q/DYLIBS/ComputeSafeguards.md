## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2973.80.185.0.0
-  __TEXT.__text: 0x30068
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x27e4
+4.100.40.502.2
+  __TEXT.__text: 0x3f1b0
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x3074
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__cstring: 0x34aa
-  __TEXT.__oslogstring: 0x6c01
-  __TEXT.__unwind_info: 0x898
-  __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x71b6
-  __TEXT.__objc_methtype: 0xef9
-  __TEXT.__objc_stubs: 0x3f80
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x698
-  __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x40
+  __TEXT.__cstring: 0x40e1
+  __TEXT.__oslogstring: 0x8cbe
+  __TEXT.__gcc_except_tab: 0x86c
+  __TEXT.__unwind_info: 0xc58
+  __TEXT.__objc_classname: 0x3a1
+  __TEXT.__objc_methname: 0x8c1b
+  __TEXT.__objc_methtype: 0x1574
+  __TEXT.__objc_stubs: 0x4ee0
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17b0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0xaf8
-  __AUTH_CONST.__auth_got: 0x3b0
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x3bd0
-  __AUTH_CONST.__objc_intobj: 0x390
-  __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x1d28
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x1120
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__objc_const: 0x4698
+  __AUTH_CONST.__objc_intobj: 0x3a8
+  __AUTH_CONST.__objc_dictobj: 0x5c8
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x318
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x39c
+  __DATA.__data: 0x498
+  __DATA.__bss: 0x88
   __DATA.__common: 0x48
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__bss: 0x158
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: D6E04B56-A181-3E5A-A916-C0AF1BD45C84
-  Functions: 1170
-  Symbols:   3621
-  CStrings:  2652
+  UUID: 5E2D94F2-307A-3311-A82A-6DA717C14FD4
+  Functions: 1431
+  Symbols:   4491
+  CStrings:  3334
 
Symbols:
+ +[CSIssue supportsSecureCoding]
+ +[CSMitigationManager sharedInstanceWithProcessPolicies:]
+ +[CSPenaltyManager clearAllThermalTimers]
+ +[CSPenaltyManager clearThermalTimerForProcess:]
+ +[CSPenaltyManager clearThermalTimerForProcess:].cold.1
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:]
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.1
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.2
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.3
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.4
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.5
+ +[CSPenaltyManager handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:].cold.6
+ +[CSPenaltyManager initialize]
+ +[CSPenaltyManager initialize].cold.1
+ +[CSPenaltyManager isCPUCoalitionPenaltyBoxActive:withPrevIssue:]
+ +[CSPenaltyManager isCPUCoalitionPenaltyBoxActive:withPrevIssue:].cold.1
+ +[CSPenaltyManager isCPUCoalitionPenaltyBoxActive:withPrevIssue:].cold.2
+ +[CSPenaltyManager isThermalTimerActiveForProcess:]
+ +[CSPenaltyManager restoreStateForProcess:]
+ +[CSPenaltyManager restoreStateForProcess:].cold.1
+ +[CSPenaltyManager restoreStateForProcess:].cold.2
+ +[CSPenaltyManager saveStateForProcess:]
+ +[CSPenaltyManager saveStateForProcess:].cold.1
+ +[CSPenaltyManager saveStateForProcess:].cold.2
+ +[CSPenaltyManager startThermalTimerForProcess:]
+ +[CSPenaltyManager startThermalTimerForProcess:].cold.1
+ +[CSPenaltyManager startThermalTimerForProcess:].cold.2
+ +[CSPenaltyManager stopThermalTimerForProcess:]
+ +[CSPenaltyManager stopThermalTimerForProcess:].cold.1
+ +[CSProcessManager sharedInstanceWithProcessPolicies:andBand95:andBand80:]
+ -[CSDetectionRule initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:]
+ -[CSDetectionRule initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:]
+ -[CSDetectionRule initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:ruleType:]
+ -[CSDetectionRule ruleType]
+ -[CSDetectionRule setRuleType:]
+ -[CSDetectionRule setUnit:]
+ -[CSDetectionRule unit]
+ -[CSDetectionRuleCondition .cxx_destruct]
+ -[CSDetectionRuleCondition additionalMetrics]
+ -[CSDetectionRuleCondition initWithScalarMetric:andNormalizerMetric:andComparator:andValue:andAdditionalMetrics:]
+ -[CSDetectionRuleCondition initWithThermalCondition:andValue:]
+ -[CSDetectionRuleCondition setAdditionalMetrics:]
+ -[CSDetectionService detectWithLookbackDuration:withReply:]
+ -[CSDetectionServiceConnection .cxx_destruct]
+ -[CSDetectionServiceConnection connectionToServer]
+ -[CSDetectionServiceConnection init]
+ -[CSDetectionServiceConnection invalidate]
+ -[CSDetectionServiceConnection service]
+ -[CSDetectionServiceConnection setConnectionToServer:]
+ -[CSIntervalList init]
+ -[CSIntervalList sort]
+ -[CSIssue encodeWithCoder:]
+ -[CSIssue initWithCoder:]
+ -[CSIssue setUnit:]
+ -[CSIssue unit]
+ -[CSIssueDetector detectIssuesFromFirstEndDate:toLastEndDate:]
+ -[CSIssueDetector detectIssuesFromFirstEndDate:toLastEndDate:withRules:]
+ -[CSIssueDetector detectThermalIssuesWithData:]
+ -[CSIssueDetector detectThermalIssuesWithData:].cold.1
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.10
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.11
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.8
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.9
+ -[CSIssueDetector evaluateRuleWithSlidingWindow:withFirstEndDate:andLastEndDate:]
+ -[CSIssueDetector evaluateRuleWithSlidingWindow:withFirstEndDate:andLastEndDate:].cold.1
+ -[CSIssueDetector getProcessesForCoalitionIDUsingDirectPolling:]
+ -[CSIssueDetector getProcessesForCoalitionIDUsingDirectPolling:].cold.1
+ -[CSIssueDetector getProcessesForCoalitionIDUsingDirectPolling:].cold.2
+ -[CSIssueDetector getProcessesForCoalitionIDUsingDirectPolling:].cold.3
+ -[CSIssueDetector getThermalIssueWithMitigationSuggestionForCoalitionID:withRule:withValue:withLaunchdName:fromStartDate:toEndDate:]
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:]
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.1
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.2
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.3
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.4
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.5
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:processName:additionalMetrics:].cold.6
+ -[CSIssueDetector initWithDBReader:]
+ -[CSIssueDetector init]
+ -[CSIssueDetector initializeCPUDetectionRules]
+ -[CSIssueDetector initializeCPUDetectionRules].cold.1
+ -[CSIssueDetector initializeThermalDetectionRules]
+ -[CSIssueDetector primaryDetectors]
+ -[CSIssueDetector setPrimaryDetectors:]
+ -[CSIssueDetector setSpecialRule:]
+ -[CSIssueDetector setThermalDetectionRules:]
+ -[CSIssueDetector specialRule]
+ -[CSIssueDetector thermalDetectionRules]
+ -[CSIssueDetector updateRulesArray]
+ -[CSIssueDetector updateRulesArray].cold.1
+ -[CSIssueDetector updateRulesArray].cold.2
+ -[CSMitigationManager _initWithProcessPolicies:]
+ -[CSMitigationManager _initWithProcessPolicies:].cold.1
+ -[CSMitigationManager _initWithProcessPolicies:].cold.2
+ -[CSMitigationManager allowedProcessesSet]
+ -[CSMitigationManager createNotificationForMitigation:forProcess:pid:reason:]
+ -[CSMitigationManager createThermalCSProcess:withUUID:]
+ -[CSMitigationManager createThermalCSProcess:withUUID:].cold.1
+ -[CSMitigationManager createThermalCSProcess:withUUID:].cold.2
+ -[CSMitigationManager createThermalCSProcess:withUUID:].cold.3
+ -[CSMitigationManager createThermalCSProcess:withUUID:].cold.4
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:]
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.1
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.10
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.11
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.12
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.13
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.2
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.3
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.4
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.5
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.6
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.7
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.8
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:withPrevIssue:].cold.9
+ -[CSMitigationManager executeDelayedFatalMitigation:matchedCoalitionPids:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:]
+ -[CSMitigationManager executeDelayedThrottleMitigation:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:]
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.1
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.2
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.3
+ -[CSMitigationManager handleDetectorViolation:].cold.3
+ -[CSMitigationManager isProcessAllowed:]
+ -[CSMitigationManager killProcess:pid:coalitionID:coalitionName:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager killProcess:pid:coalitionID:coalitionName:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:]
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.1
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.2
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.3
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withCoalitionName:withIssueType:withMitigationType:withReason:]
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withCoalitionName:withIssueType:withMitigationType:withReason:].cold.1
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.2
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.3
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.4
+ -[CSMitigationManager sendNotificationBeforeMitigation:forProcess:pid:reason:]
+ -[CSMitigationManager sendNotificationBeforeMitigation:forProcess:pid:reason:].cold.1
+ -[CSMitigationManager setAllowedProcessesSet:]
+ -[CSPowerlogDBReader fileURL]
+ -[CSPowerlogDBReader getDASActivityIntervalsWithProcessName:andStartDate:andEndDate:]
+ -[CSPowerlogDBReader getDASActivityIntervalsWithProcessName:withStartDate:andEndDate:andCPUIntensive:withTaskName:]
+ -[CSPowerlogDBReader getDisplayOnIntervalListWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader getLastTimestamp]
+ -[CSPowerlogDBReader getLogInterval]
+ -[CSPowerlogDBReader getMaxCoalitionTimestamp]
+ -[CSPowerlogDBReader getMaxCoalitionTimestamp].cold.1
+ -[CSPowerlogDBReader getOngoingRestoreIntervalsWithFastPassName:andStartDate:andEndDate:]
+ -[CSPowerlogDBReader getThermalLimitedChargingIntervalListWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader initWithFileURL:]
+ -[CSPowerlogDBReader initWithFileURL:].cold.1
+ -[CSPowerlogDBReader init]
+ -[CSPowerlogDBReader isThermalLimitedCharging:]
+ -[CSPowerlogDBReader setFileURL:]
+ -[CSProcessManager _initWithProcessPolicies:andBand95:andBand80:]
+ -[CSProcessManager exemptedProcessesDict]
+ -[CSProcessManager registerThermalCSProcess:forIdentifier:]
+ -[CSProcessManager registerThermalCSProcess:forIdentifier:].cold.1
+ -[CSProcessManager registerThermalCSProcess:forIdentifier:].cold.2
+ -[CSProcessManager registerThermalCSProcess:forIdentifier:].cold.3
+ -[CSProcessManager registerThermalCSProcess:forIdentifier:].cold.4
+ -[CSProcessManager setExemptedProcessesDict:]
+ -[CSRestrictionDataProvider _processPolicyDictWithErrors:]
+ -[CSRestrictionManager currentDASIntensiveProcesses]
+ -[CSRestrictionManager disableThermalTriggerWithHandler:]
+ -[CSRestrictionManager enableThermalTriggerWithHandler:]
+ -[CSRestrictionManager forceDetectionWithFirstEndDate:lastEndDate:withHandler:]
+ -[CSRestrictionManager forceDetectionWithFirstEndDate:lastEndDate:withHandler:].cold.1
+ -[CSRestrictionManager forceThermalDetectionWithHandler:]
+ -[CSRestrictionManager getThermalPollingIntervalWithHandler:]
+ -[CSRestrictionManager getThermalSamplingIntervalWithHandler:]
+ -[CSRestrictionManager getThermalTemperatureWithHandler:]
+ -[CSRestrictionManager getThermalTriggerStatusWithHandler:]
+ -[CSRestrictionManager getTriggerParametersWithHandler:]
+ -[CSRestrictionManager isThermalTriggerEnabledWithHandler:]
+ -[CSRestrictionManager liftMitigationsForDASProcesses:]
+ -[CSRestrictionManager modifyThermalPollingInterval:withHandler:]
+ -[CSRestrictionManager modifyThermalSamplingInterval:withHandler:]
+ -[CSRestrictionManager modifyTriggerWithInterval:withLookback:withThreshold:]
+ -[CSRestrictionManager previouslyMitigatedDASProcesses]
+ -[CSRestrictionManager restoreMitigationsForCompletedDASProcesses:]
+ -[CSRestrictionManager setCurrentDASIntensiveProcesses:]
+ -[CSRestrictionManager setPreviouslyMitigatedDASProcesses:]
+ -[CSTriggerManager _collectAndDetect]
+ -[CSTriggerManager _collectTopCoalitions]
+ -[CSTriggerManager _getThermalStateName:]
+ -[CSTriggerManager _machTimeToNanoseconds:]
+ -[CSTriggerManager _startHighTempDataCollection]
+ -[CSTriggerManager _startThermalMonitoring]
+ -[CSTriggerManager _stopHighTempDataCollection]
+ -[CSTriggerManager calculateAverageTemperature:overLast:]
+ -[CSTriggerManager checkCpuPercentageAndInvokeIssueDetection:windowStartDate:coalitionDataBoundary:]
+ -[CSTriggerManager checkDrainAndInvokeIssueDetection:coalitionDataBoundary:]
+ -[CSTriggerManager closeSMCConnection]
+ -[CSTriggerManager coalitionCollectionInterval]
+ -[CSTriggerManager dealloc]
+ -[CSTriggerManager detectAndInvokeIssueDetection:slidingWindowStartDate:].cold.1
+ -[CSTriggerManager disableThermalTrigger]
+ -[CSTriggerManager enableThermalTrigger]
+ -[CSTriggerManager forceThermalDetectionWithHandler:]
+ -[CSTriggerManager generateThermalMetadata:]
+ -[CSTriggerManager generateThermalPayloadWithMetadata:triggeredDetection:triggeredType:]
+ -[CSTriggerManager getCurrentTemperature]
+ -[CSTriggerManager getDetectionLookbackDuration:]
+ -[CSTriggerManager getDetectionLookbackDuration:].cold.1
+ -[CSTriggerManager getTemperatureSamplingInterval]
+ -[CSTriggerManager getThermalPollingInterval]
+ -[CSTriggerManager getThermalPollingInterval].cold.1
+ -[CSTriggerManager getThermalTriggerStatus]
+ -[CSTriggerManager getThermalTriggerStatus].cold.1
+ -[CSTriggerManager getThermalTriggerStatus].cold.2
+ -[CSTriggerManager getTriggerParameters]
+ -[CSTriggerManager invokeIssueDetectionFromFirstEndDate:toLastEndDate:]
+ -[CSTriggerManager isThermalTriggerEnabled]
+ -[CSTriggerManager lastCoalitionDataEnd]
+ -[CSTriggerManager lastTemperatureReading]
+ -[CSTriggerManager lastThermalTimerDate]
+ -[CSTriggerManager logThermalTriggerToPPS:triggeredDetection:triggeredType:]
+ -[CSTriggerManager logThermalTriggerToPPS:triggeredDetection:triggeredType:].cold.1
+ -[CSTriggerManager modifyTemperatureSamplingInterval:]
+ -[CSTriggerManager modifyTemperatureSamplingInterval:].cold.1
+ -[CSTriggerManager modifyThermalPollingInterval:]
+ -[CSTriggerManager modifyThermalPollingInterval:].cold.1
+ -[CSTriggerManager modifyThermalPollingInterval:].cold.2
+ -[CSTriggerManager modifyThermalPollingInterval:].cold.3
+ -[CSTriggerManager modifyThermalPollingInterval:].cold.4
+ -[CSTriggerManager modifyTriggerWithInterval:withLookback:withThreshold:]
+ -[CSTriggerManager openSMCConnection]
+ -[CSTriggerManager openSMCConnection].cold.1
+ -[CSTriggerManager openSMCConnection].cold.2
+ -[CSTriggerManager processDataHistory]
+ -[CSTriggerManager processThermalEvent]
+ -[CSTriggerManager processThermalEvent].cold.1
+ -[CSTriggerManager processThermalEvent].cold.2
+ -[CSTriggerManager rateMonitoringTimer]
+ -[CSTriggerManager readKey:]
+ -[CSTriggerManager readKey:].cold.1
+ -[CSTriggerManager readKey:].cold.10
+ -[CSTriggerManager readKey:].cold.2
+ -[CSTriggerManager readKey:].cold.3
+ -[CSTriggerManager readKey:].cold.4
+ -[CSTriggerManager readKey:].cold.5
+ -[CSTriggerManager readKey:].cold.6
+ -[CSTriggerManager readKey:].cold.7
+ -[CSTriggerManager readKey:].cold.8
+ -[CSTriggerManager readKey:].cold.9
+ -[CSTriggerManager readThermalKey]
+ -[CSTriggerManager readThermalKey].cold.1
+ -[CSTriggerManager readThermalKey].cold.2
+ -[CSTriggerManager savedThermalPollingInterval]
+ -[CSTriggerManager setCoalitionCollectionInterval:]
+ -[CSTriggerManager setLastCoalitionDataEnd:]
+ -[CSTriggerManager setLastTemperatureReading:]
+ -[CSTriggerManager setLastThermalTimerDate:]
+ -[CSTriggerManager setProcessDataHistory:]
+ -[CSTriggerManager setRateMonitoringTimer:]
+ -[CSTriggerManager setSavedThermalPollingInterval:]
+ -[CSTriggerManager setSmcConnection:]
+ -[CSTriggerManager setSmcConnectionOpen:]
+ -[CSTriggerManager setTemperatureHistory:]
+ -[CSTriggerManager setTemperatureSamplingInterval:]
+ -[CSTriggerManager setThermalPollingInterval:]
+ -[CSTriggerManager setThermalTimer:]
+ -[CSTriggerManager setThermalTriggerEnabled:]
+ -[CSTriggerManager setThermalTriggerState:]
+ -[CSTriggerManager setTriggerCPUThreshold:]
+ -[CSTriggerManager setTriggerLookbackDuration:]
+ -[CSTriggerManager smcConnectionOpen]
+ -[CSTriggerManager smcConnection]
+ -[CSTriggerManager temperatureHistory]
+ -[CSTriggerManager temperatureSamplingInterval]
+ -[CSTriggerManager thermalPollingInterval]
+ -[CSTriggerManager thermalTimer]
+ -[CSTriggerManager thermalTriggerEnabled]
+ -[CSTriggerManager thermalTriggerState]
+ -[CSTriggerManager triggerCPUThreshold]
+ -[CSTriggerManager triggerLookbackDuration]
+ -[CSTriggerManager updateTemperatureHistory:]
+ -[PowerCoal callCoalInfoResourceUsage]
+ -[PowerCoal cid]
+ -[PowerCoal setCid:]
+ -[PowerCoal setSz:]
+ -[PowerCoal sz]
+ -[PowerCoalList getCoalIds]
+ -[PowerCoalName cid]
+ -[PowerCoalName getCoalName]
+ -[PowerCoalName setCid:]
+ GCC_except_table11
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table53
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table97
+ _DetectionServiceLog
+ _DetectionServiceLog._logHandle
+ _DetectionServiceLog.cold.1
+ _DetectionServiceLog.onceToken
+ _OBJC_CLASS_$_CSDetectionService
+ _OBJC_CLASS_$_CSDetectionServiceConnection
+ _OBJC_CLASS_$_CSPenaltyManager
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_PEMitigationNotification
+ _OBJC_CLASS_$_PEXPCService
+ _OBJC_CLASS_$_PowerCoal
+ _OBJC_CLASS_$_PowerCoalList
+ _OBJC_CLASS_$_PowerCoalName
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_CSDetectionRule._ruleType
+ _OBJC_IVAR_$_CSDetectionRule._unit
+ _OBJC_IVAR_$_CSDetectionRuleCondition._additionalMetrics
+ _OBJC_IVAR_$_CSDetectionServiceConnection._connectionToServer
+ _OBJC_IVAR_$_CSDetectionServiceConnection._service
+ _OBJC_IVAR_$_CSIssue._unit
+ _OBJC_IVAR_$_CSIssueDetector._primaryDetectors
+ _OBJC_IVAR_$_CSIssueDetector._specialRule
+ _OBJC_IVAR_$_CSIssueDetector._thermalDetectionRules
+ _OBJC_IVAR_$_CSMitigationManager._allowedProcessesSet
+ _OBJC_IVAR_$_CSPowerlogDBReader._fileURL
+ _OBJC_IVAR_$_CSProcessManager._exemptedProcessesDict
+ _OBJC_IVAR_$_CSRestrictionManager._currentDASIntensiveProcesses
+ _OBJC_IVAR_$_CSRestrictionManager._previouslyMitigatedDASProcesses
+ _OBJC_IVAR_$_CSTriggerManager._coalitionCollectionInterval
+ _OBJC_IVAR_$_CSTriggerManager._coalitionIdsToNames
+ _OBJC_IVAR_$_CSTriggerManager._lastCoalitionDataEnd
+ _OBJC_IVAR_$_CSTriggerManager._lastTemperatureReading
+ _OBJC_IVAR_$_CSTriggerManager._lastThermalTimerDate
+ _OBJC_IVAR_$_CSTriggerManager._previousCoalitions
+ _OBJC_IVAR_$_CSTriggerManager._processDataHistory
+ _OBJC_IVAR_$_CSTriggerManager._rateMonitoringTimer
+ _OBJC_IVAR_$_CSTriggerManager._savedThermalPollingInterval
+ _OBJC_IVAR_$_CSTriggerManager._smcConnection
+ _OBJC_IVAR_$_CSTriggerManager._smcConnectionOpen
+ _OBJC_IVAR_$_CSTriggerManager._temperatureHistory
+ _OBJC_IVAR_$_CSTriggerManager._temperatureSamplingInterval
+ _OBJC_IVAR_$_CSTriggerManager._thermalPollingInterval
+ _OBJC_IVAR_$_CSTriggerManager._thermalTimer
+ _OBJC_IVAR_$_CSTriggerManager._thermalTriggerEnabled
+ _OBJC_IVAR_$_CSTriggerManager._thermalTriggerState
+ _OBJC_IVAR_$_CSTriggerManager._triggerCPUThreshold
+ _OBJC_IVAR_$_CSTriggerManager._triggerLookbackDuration
+ _OBJC_IVAR_$_PowerCoal._cid
+ _OBJC_IVAR_$_PowerCoal._sz
+ _OBJC_IVAR_$_PowerCoalName._cid
+ _OBJC_METACLASS_$_CSDetectionService
+ _OBJC_METACLASS_$_CSDetectionServiceConnection
+ _OBJC_METACLASS_$_CSPenaltyManager
+ _OBJC_METACLASS_$_PowerCoal
+ _OBJC_METACLASS_$_PowerCoalList
+ _OBJC_METACLASS_$_PowerCoalName
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _SMCCloseConnection
+ _SMCGetKeyInfo
+ _SMCMakeUInt32Key
+ _SMCOpenConnectionWithDefaultService
+ _SMCReadKey
+ _SMCReadKeyAsNumericWithKnownKeyInfo
+ _XPC_COALITION_INFO_KEY_NAME
+ __OBJC_$_CLASS_METHODS_CSIssue
+ __OBJC_$_CLASS_METHODS_CSPenaltyManager
+ __OBJC_$_CLASS_PROP_LIST_CSIssue
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_CSDetectionService
+ __OBJC_$_INSTANCE_METHODS_CSDetectionServiceConnection
+ __OBJC_$_INSTANCE_METHODS_PowerCoal
+ __OBJC_$_INSTANCE_METHODS_PowerCoalList
+ __OBJC_$_INSTANCE_METHODS_PowerCoalName
+ __OBJC_$_INSTANCE_VARIABLES_CSDetectionServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_PowerCoal
+ __OBJC_$_INSTANCE_VARIABLES_PowerCoalName
+ __OBJC_$_PROP_LIST_CSDetectionServiceConnection
+ __OBJC_$_PROP_LIST_PowerCoal
+ __OBJC_$_PROP_LIST_PowerCoalName
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSDetectionServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPowerlogDBReaderProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ComputeSafeguardsViolationReporting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSDetectionServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPowerlogDBReaderProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ComputeSafeguardsViolationReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_CSPowerlogDBReaderProtocol
+ __OBJC_$_PROTOCOL_REFS_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_$_PROTOCOL_REFS_ComputeSafeguardsViolationReporting
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_CSDetectionService
+ __OBJC_CLASS_PROTOCOLS_$_CSIssue
+ __OBJC_CLASS_PROTOCOLS_$_CSPowerlogDBReader
+ __OBJC_CLASS_RO_$_CSDetectionService
+ __OBJC_CLASS_RO_$_CSDetectionServiceConnection
+ __OBJC_CLASS_RO_$_CSPenaltyManager
+ __OBJC_CLASS_RO_$_PowerCoal
+ __OBJC_CLASS_RO_$_PowerCoalList
+ __OBJC_CLASS_RO_$_PowerCoalName
+ __OBJC_LABEL_PROTOCOL_$_CSDetectionServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_CSPowerlogDBReaderProtocol
+ __OBJC_LABEL_PROTOCOL_$_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_LABEL_PROTOCOL_$_ComputeSafeguardsViolationReporting
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_CSDetectionService
+ __OBJC_METACLASS_RO_$_CSDetectionServiceConnection
+ __OBJC_METACLASS_RO_$_CSPenaltyManager
+ __OBJC_METACLASS_RO_$_PowerCoal
+ __OBJC_METACLASS_RO_$_PowerCoalList
+ __OBJC_METACLASS_RO_$_PowerCoalName
+ __OBJC_PROTOCOL_$_CSDetectionServiceProtocol
+ __OBJC_PROTOCOL_$_CSPowerlogDBReaderProtocol
+ __OBJC_PROTOCOL_$_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_PROTOCOL_$_ComputeSafeguardsViolationReporting
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_CSDetectionServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ComputeSafeguardsScheduledWorkReporting
+ __OBJC_PROTOCOL_REFERENCE_$_ComputeSafeguardsViolationReporting
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.191
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.204
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.205
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.206
+ ___136-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:]_block_invoke.333
+ ___192-[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:]_block_invoke
+ ___192-[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:]_block_invoke.83
+ ___22-[CSIntervalList sort]_block_invoke
+ ___30+[CSPenaltyManager initialize]_block_invoke
+ ___36-[CSDetectionServiceConnection init]_block_invoke
+ ___36-[CSDetectionServiceConnection init]_block_invoke.5
+ ___36-[CSDetectionServiceConnection init]_block_invoke.5.cold.1
+ ___36-[CSDetectionServiceConnection init]_block_invoke.8
+ ___36-[CSDetectionServiceConnection init]_block_invoke.8.cold.1
+ ___36-[CSDetectionServiceConnection init]_block_invoke.cold.1
+ ___40-[CSMitigationManager isProcessAllowed:]_block_invoke
+ ___40-[CSTriggerManager getTriggerParameters]_block_invoke
+ ___41-[CSTriggerManager _collectTopCoalitions]_block_invoke
+ ___41-[CSTriggerManager _collectTopCoalitions]_block_invoke.cold.1
+ ___43-[CSTriggerManager _startThermalMonitoring]_block_invoke
+ ___48+[CSPenaltyManager startThermalTimerForProcess:]_block_invoke
+ ___48+[CSPenaltyManager startThermalTimerForProcess:]_block_invoke.cold.1
+ ___48+[CSPenaltyManager startThermalTimerForProcess:]_block_invoke.cold.2
+ ___48-[CSMitigationManager _initWithProcessPolicies:]_block_invoke
+ ___48-[CSMitigationManager _initWithProcessPolicies:]_block_invoke_2
+ ___48-[CSTriggerManager _startHighTempDataCollection]_block_invoke
+ ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.331
+ ___53-[CSTriggerManager forceThermalDetectionWithHandler:]_block_invoke
+ ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.303
+ ___54-[CSTriggerManager modifyTemperatureSamplingInterval:]_block_invoke
+ ___56-[CSRestrictionManager enableThermalTriggerWithHandler:]_block_invoke
+ ___57+[CSMitigationManager sharedInstanceWithProcessPolicies:]_block_invoke
+ ___57-[CSRestrictionManager disableThermalTriggerWithHandler:]_block_invoke
+ ___57-[CSRestrictionManager forceThermalDetectionWithHandler:]_block_invoke
+ ___57-[CSRestrictionManager getThermalTemperatureWithHandler:]_block_invoke
+ ___59-[CSRestrictionManager getThermalTriggerStatusWithHandler:]_block_invoke
+ ___59-[CSRestrictionManager isThermalTriggerEnabledWithHandler:]_block_invoke
+ ___61-[CSRestrictionManager getThermalPollingIntervalWithHandler:]_block_invoke
+ ___62-[CSRestrictionManager getThermalSamplingIntervalWithHandler:]_block_invoke
+ ___65-[CSRestrictionManager modifyThermalPollingInterval:withHandler:]_block_invoke
+ ___66-[CSRestrictionManager modifyThermalSamplingInterval:withHandler:]_block_invoke
+ ___74+[CSProcessManager sharedInstanceWithProcessPolicies:andBand95:andBand80:]_block_invoke
+ ___76-[CSTriggerManager logThermalTriggerToPPS:triggeredDetection:triggeredType:]_block_invoke
+ ___77-[CSRestrictionManager modifyTriggerWithInterval:withLookback:withThreshold:]_block_invoke
+ ___79-[CSRestrictionManager forceDetectionWithFirstEndDate:lastEndDate:withHandler:]_block_invoke
+ ___DetectionServiceLog_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8r80l8
+ ___block_descriptor_122_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8r88l8
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e35_q24?0"CSInterval"8"CSInterval"16l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e22_v24?0"NSString"8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.11
+ ___block_literal_global.16
+ ___block_literal_global.178
+ ___block_literal_global.318
+ ___block_literal_global.32
+ ___block_literal_global.46
+ ___block_literal_global.7
+ ___block_literal_global.734
+ ___block_literal_global.79
+ ___block_literal_global.99
+ ___getCSProcessPolicies_block_invoke
+ ___getCSRuleMitigationPolicies_block_invoke
+ ___kCFBooleanFalse
+ __machTimeToNanoseconds:.timebaseInfo
+ __xpc_type_dictionary
+ _coalitionIDForPid
+ _dispatch_time
+ _fullProcessNameForPid
+ _getCSProcessPolicies.cold.1
+ _getCSProcessPolicies.onceToken
+ _getCSProcessPolicies.testProcessPolicies
+ _getCSRuleMitigationPolicies
+ _getCSRuleMitigationPolicies.cold.1
+ _getCSRuleMitigationPolicies.onceToken
+ _getCSRuleMitigationPolicies.testRuleMitigationPolicies
+ _getCoalitionName
+ _isThermalMonitoringEnabled
+ _logThermalTriggerToPPS:triggeredDetection:triggeredType:.onceToken
+ _logThermalTriggerToPPS:triggeredDetection:triggeredType:.streamID
+ _logger
+ _mach_timebase_info
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$URLForKey:
+ _objc_msgSend$UUID
+ _objc_msgSend$_collectAndDetect
+ _objc_msgSend$_collectTopCoalitions
+ _objc_msgSend$_getThermalStateName:
+ _objc_msgSend$_initWithProcessPolicies:
+ _objc_msgSend$_initWithProcessPolicies:andBand95:andBand80:
+ _objc_msgSend$_machTimeToNanoseconds:
+ _objc_msgSend$_processPolicyDictWithErrors:
+ _objc_msgSend$_startHighTempDataCollection
+ _objc_msgSend$_startThermalMonitoring
+ _objc_msgSend$_stopHighTempDataCollection
+ _objc_msgSend$additionalMetrics
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$calculateAverageTemperature:overLast:
+ _objc_msgSend$callCoalInfoResourceUsage
+ _objc_msgSend$checkCpuPercentageAndInvokeIssueDetection:windowStartDate:coalitionDataBoundary:
+ _objc_msgSend$cid
+ _objc_msgSend$clearThermalTimerForProcess:
+ _objc_msgSend$closeSMCConnection
+ _objc_msgSend$createNotificationForMitigation:forProcess:pid:reason:
+ _objc_msgSend$decideMitigation:withCoalitionName:withReason:withPrevIssue:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$detectIssuesFromFirstEndDate:toLastEndDate:
+ _objc_msgSend$detectIssuesFromFirstEndDate:toLastEndDate:withRules:
+ _objc_msgSend$detectThermalIssuesWithData:
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$disableThermalTrigger
+ _objc_msgSend$enableThermalTrigger
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$evaluateRuleWithSlidingWindow:withFirstEndDate:andLastEndDate:
+ _objc_msgSend$executeDelayedFatalMitigation:matchedCoalitionPids:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:
+ _objc_msgSend$executeDelayedThrottleMitigation:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:
+ _objc_msgSend$experimentIdentifiersWithNamespaceName:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileValue
+ _objc_msgSend$forceThermalDetectionWithHandler:
+ _objc_msgSend$generateThermalMetadata:
+ _objc_msgSend$generateThermalPayloadWithMetadata:triggeredDetection:triggeredType:
+ _objc_msgSend$getCoalIds
+ _objc_msgSend$getCoalName
+ _objc_msgSend$getCurrentTemperature
+ _objc_msgSend$getDASActivityIntervalsWithProcessName:andStartDate:andEndDate:
+ _objc_msgSend$getDASActivityIntervalsWithProcessName:withStartDate:andEndDate:andCPUIntensive:withTaskName:
+ _objc_msgSend$getDetectionLookbackDuration:
+ _objc_msgSend$getDisplayOnIntervalListWithStartDate:andEndDate:
+ _objc_msgSend$getMaxCoalitionTimestamp
+ _objc_msgSend$getOngoingRestoreIntervalsWithFastPassName:andStartDate:andEndDate:
+ _objc_msgSend$getProcessesForCoalitionIDUsingDirectPolling:
+ _objc_msgSend$getTemperatureSamplingInterval
+ _objc_msgSend$getThermalIssueWithMitigationSuggestionForCoalitionID:withRule:withValue:withLaunchdName:fromStartDate:toEndDate:
+ _objc_msgSend$getThermalLimitedChargingIntervalListWithStartDate:andEndDate:
+ _objc_msgSend$getThermalPollingInterval
+ _objc_msgSend$getThermalTriggerStatus
+ _objc_msgSend$getTriggerParameters
+ _objc_msgSend$getValue:
+ _objc_msgSend$getValueOfMetric:startDate:endDate:processName:additionalMetrics:
+ _objc_msgSend$gracePeriod
+ _objc_msgSend$handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:
+ _objc_msgSend$handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:
+ _objc_msgSend$initWithDBReader:
+ _objc_msgSend$initWithFileURL:
+ _objc_msgSend$initWithScalarMetric:andNormalizerMetric:andComparator:andValue:andAdditionalMetrics:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithThermalCondition:andValue:
+ _objc_msgSend$initWithWarningType:gracePeriod:notificationID:reason:processInfo:
+ _objc_msgSend$initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:
+ _objc_msgSend$initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:
+ _objc_msgSend$initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:ruleType:
+ _objc_msgSend$initializeCPUDetectionRules
+ _objc_msgSend$initializeThermalDetectionRules
+ _objc_msgSend$invalidate
+ _objc_msgSend$invokeIssueDetectionFromFirstEndDate:toLastEndDate:
+ _objc_msgSend$isCPUCoalitionPenaltyBoxActive:withPrevIssue:
+ _objc_msgSend$isProcessAllowed:
+ _objc_msgSend$isProcessRegistered:
+ _objc_msgSend$isThermalLimitedCharging:
+ _objc_msgSend$isThermalTriggerEnabled
+ _objc_msgSend$issueDetector
+ _objc_msgSend$killProcess:pid:coalitionID:coalitionName:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$lastTemperatureReading
+ _objc_msgSend$liftMitigationsForDASProcesses:
+ _objc_msgSend$logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:
+ _objc_msgSend$logMitigationToPowerLogForProcess:withPid:withCoalitionID:withCoalitionName:withIssueType:withMitigationType:withReason:
+ _objc_msgSend$logThermalTriggerToPPS:triggeredDetection:triggeredType:
+ _objc_msgSend$modifyTemperatureSamplingInterval:
+ _objc_msgSend$modifyThermalPollingInterval:
+ _objc_msgSend$modifyTriggerWithInterval:withLookback:withThreshold:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$openSMCConnection
+ _objc_msgSend$path
+ _objc_msgSend$processDataHistory
+ _objc_msgSend$processThermalEvent
+ _objc_msgSend$putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$queueMitigationNotification:forPID:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readKey:
+ _objc_msgSend$readThermalKey
+ _objc_msgSend$reason
+ _objc_msgSend$registerThermalCSProcess:forIdentifier:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$restoreMitigationsForCompletedDASProcesses:
+ _objc_msgSend$restoreStateForProcess:
+ _objc_msgSend$ruleType
+ _objc_msgSend$saveStateForProcess:
+ _objc_msgSend$setCid:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setSmcConnection:
+ _objc_msgSend$setSz:
+ _objc_msgSend$setThermalTriggerState:
+ _objc_msgSend$setValuesForKeysWithDictionary:
+ _objc_msgSend$sharedInstanceWithProcessPolicies:
+ _objc_msgSend$sharedInstanceWithProcessPolicies:andBand95:andBand80:
+ _objc_msgSend$sharedService
+ _objc_msgSend$smcConnection
+ _objc_msgSend$sort
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$startListener
+ _objc_msgSend$startThermalTimerForProcess:
+ _objc_msgSend$stopThermalTimerForProcess:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$sz
+ _objc_msgSend$temperatureHistory
+ _objc_msgSend$thermalDetectionRules
+ _objc_msgSend$thermalTriggerState
+ _objc_msgSend$unit
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateRulesArray
+ _objc_msgSend$updateTemperatureHistory:
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_msgSend$warningType
+ _objc_opt_new
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x9
+ _onceToken
+ _pUUIDForPid
+ _proc_listcoalitions
+ _savedPenaltyBoxDurations
+ _sharedInstanceWithProcessPolicies:._sharedInstance
+ _sharedInstanceWithProcessPolicies:.onceToken
+ _sharedInstanceWithProcessPolicies:andBand95:andBand80:._sharedInstance
+ _sharedInstanceWithProcessPolicies:andBand95:andBand80:.onceToken
+ _thermalTimers
+ _xpc_coalition_copy_info
+ _xpc_dictionary_get_string
+ _xpc_get_type
- +[CSIssueDetector sharedInstance].cold.1
- +[CSMitigationManager sharedInstance].cold.1
- +[CSProcessManager sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]
- -[CSDetectionRule initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:]
- -[CSDetectionRule initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:]
- -[CSIssueDetector _init]
- -[CSIssueDetector _init].cold.1
- -[CSIssueDetector detectIssuesFromStartTime:endDate:withRules:]
- -[CSIssueDetector detectWithLookbackDuration:]
- -[CSIssueDetector evaluateRuleWithSlidingWindow:withStartDate:andEndDate:]
- -[CSIssueDetector evaluateRuleWithSlidingWindow:withStartDate:andEndDate:].cold.1
- -[CSIssueDetector genericCPUDetectorProcessDenyList]
- -[CSIssueDetector genericCPUDetectorProcessDenyRegex]
- -[CSIssueDetector getValueOfMetric:startDate:endDate:]
- -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.1
- -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.2
- -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.3
- -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.4
- -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.5
- -[CSIssueDetector setGenericCPUDetectorProcessDenyList:]
- -[CSIssueDetector setGenericCPUDetectorProcessDenyRegex:]
- -[CSIssueDetector setTriggerTimer:]
- -[CSIssueDetector testDetectWithLookbackDuration]
- -[CSIssueDetector triggerTimer]
- -[CSIssueDetector updateCPUBuffer:]
- -[CSMitigationManager _init]
- -[CSMitigationManager _init].cold.1
- -[CSMitigationManager _init].cold.2
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:]
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.1
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.10
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.11
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.2
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.3
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.4
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.5
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.6
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.7
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.8
- -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.9
- -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]
- -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.1
- -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.2
- -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.3
- -[CSMitigationManager killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:]
- -[CSMitigationManager killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
- -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:]
- -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.1
- -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.2
- -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:]
- -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:].cold.1
- -[CSMitigationManager policyMitigationsEnabled].cold.2
- -[CSMitigationManager policyMitigationsEnabled].cold.3
- -[CSMitigationManager policyMitigationsEnabled].cold.4
- -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:]
- -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
- -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.2
- -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.3
- -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.4
- -[CSPowerlogDBReader _init]
- -[CSPowerlogDBReader getAPWakeIntervalListWithStartDate:andEndDate:].cold.1
- -[CSProcessManager _initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]
- -[CSProcessManager processPoliciesDict]
- -[CSProcessManager setProcessPoliciesDict:]
- -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:]
- -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:].cold.1
- -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:].cold.2
- -[CSRestrictionDataProvider _processesSetWithErrors:]
- -[CSRestrictionDataProvider _processesSetWithErrors:].cold.1
- -[CSRestrictionDataProvider _processesSetWithErrors:].cold.2
- -[CSRestrictionDataProvider _processesSetWithErrors:].cold.3
- -[CSRestrictionDataProvider processesSet]
- -[CSRestrictionDataProvider processes]
- -[CSRestrictionDataProvider setProcesses:]
- -[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:]
- -[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:].cold.1
- -[CSRestrictionManager getTriggerIntervalWithHandler:]
- -[CSRestrictionManager modifyTriggerInterval:]
- -[CSScenarioManager activeScenariosLastEvaluation]
- -[CSScenarioManager activeScenariosLastPublished]
- -[CSScenarioManager setActiveScenariosLastEvaluation:]
- -[CSScenarioManager setActiveScenariosLastPublished:]
- -[CSTriggerManager checkCpuPercentageAndInvokeIssueDetection:windowStartDate:]
- -[CSTriggerManager checkDrainAndInvokeIssueDetection:]
- -[CSTriggerManager getDetectionLookbackDuration]
- -[CSTriggerManager getTriggerInterval]
- -[CSTriggerManager modifyTriggerInterval:]
- GCC_except_table28
- GCC_except_table32
- GCC_except_table34
- GCC_except_table41
- GCC_except_table71
- GCC_except_table75
- GCC_except_table77
- _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessDenyList
- _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessDenyRegex
- _OBJC_IVAR_$_CSIssueDetector._triggerTimer
- _OBJC_IVAR_$_CSProcessManager._processPoliciesDict
- _OBJC_IVAR_$_CSRestrictionDataProvider._processes
- _OBJC_IVAR_$_CSScenarioManager._activeScenariosLastEvaluation
- _OBJC_IVAR_$_CSScenarioManager._activeScenariosLastPublished
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SafeguardsViolationReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_SafeguardsViolationReporting
- __OBJC_$_PROTOCOL_REFS_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_REFS_SafeguardsViolationReporting
- __OBJC_LABEL_PROTOCOL_$_SafeguardsScheduledWorkReporting
- __OBJC_LABEL_PROTOCOL_$_SafeguardsViolationReporting
- __OBJC_PROTOCOL_$_SafeguardsScheduledWorkReporting
- __OBJC_PROTOCOL_$_SafeguardsViolationReporting
- __OBJC_PROTOCOL_REFERENCE_$_SafeguardsScheduledWorkReporting
- __OBJC_PROTOCOL_REFERENCE_$_SafeguardsViolationReporting
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.172
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.185
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.186
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.187
- ___136-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:]_block_invoke.320
- ___28-[CSMitigationManager _init]_block_invoke
- ___28-[CSMitigationManager _init]_block_invoke_2
- ___37+[CSMitigationManager sharedInstance]_block_invoke
- ___38-[CSTriggerManager getTriggerInterval]_block_invoke
- ___42-[CSTriggerManager modifyTriggerInterval:]_block_invoke
- ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.318
- ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.290
- ___63-[CSIssueDetector detectIssuesFromStartTime:endDate:withRules:]_block_invoke
- ___72-[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:]_block_invoke
- ___95+[CSProcessManager sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]_block_invoke
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
- ___block_descriptor_57_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- ___block_literal_global.15
- ___block_literal_global.155
- ___block_literal_global.163
- ___block_literal_global.17
- ___block_literal_global.179
- ___block_literal_global.19
- ___block_literal_global.2
- ___block_literal_global.78
- ___block_literal_global.98
- _getCSProcesses
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:
- _objc_msgSend$_processesPoliciesDictWithErrors:
- _objc_msgSend$_processesSetWithErrors:
- _objc_msgSend$addTimeInterval:
- _objc_msgSend$checkCpuPercentageAndInvokeIssueDetection:windowStartDate:
- _objc_msgSend$decideMitigation:withCoalitionName:withReason:
- _objc_msgSend$detectIssuesFromStartTime:endDate:withRules:
- _objc_msgSend$detectWithLookbackDuration:
- _objc_msgSend$evaluateRuleWithSlidingWindow:withStartDate:andEndDate:
- _objc_msgSend$getDetectionLookbackDuration
- _objc_msgSend$getTriggerInterval
- _objc_msgSend$getValueOfMetric:startDate:endDate:
- _objc_msgSend$handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:
- _objc_msgSend$initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:
- _objc_msgSend$initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:
- _objc_msgSend$killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:
- _objc_msgSend$logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:
- _objc_msgSend$logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:
- _objc_msgSend$maxSlidingLookback
- _objc_msgSend$modifyTriggerInterval:
- _objc_msgSend$processesSet
- _objc_msgSend$putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:
- _objc_msgSend$setDetectAcrossBoots:
- _objc_msgSend$sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:._sharedInstance
- _sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:.onceToken
CStrings:
+ " AND IsCPUIntensive = 1"
+ " AND Name = '%@'"
+ " FORCE THERMAL DETECTION REQUESTED"
+ " Failed to get key info for %@: %d"
+ " Failed to open SMC connection"
+ " Failed to read numeric key %@: %d"
+ " Failed to read sp78 key %@: %d"
+ " Invalid SMC key: %@"
+ " Logging thermal trigger information to PowerLog"
+ " Resuming thermal monitoring and detection logic"
+ " SMC connection closed"
+ " SMC connection not available for key: %@"
+ " SMC connection opened successfully"
+ " THERMAL TRIGGER DISABLED via command line"
+ " THERMAL TRIGGER ENABLED via command line"
+ " Thermal key name is nil"
+ " Thermal monitoring will continue but detection logic is paused"
+ " Thermal trigger already disabled"
+ " Thermal trigger already enabled"
+ "!"
+ "%@: %@"
+ "%d"
+ "++DisplayOnDuration condition meet"
+ "++ThermalLimitedChargingDuration condition meet"
+ "++WallClockDuration condition meet"
+ "++WallClockDurationUnplugged condition meet"
+ "--DASCPUIntensiveDuration condition not meet for any issue candidates"
+ "--DisplayOnDuration condition not meet"
+ "--OngoingRestoreDuration condition not meet for any issue candidates"
+ "--ThermalLimitedChargingDuration condition not meet"
+ "--WallClockDuration condition not meet"
+ "--WallClockDurationUnplugged condition not meet"
+ ".*camerad"
+ "10"
+ "1000"
+ "11"
+ "12"
+ "13"
+ "14"
+ "15"
+ "16"
+ "17"
+ "18"
+ "19"
+ "2"
+ "20"
+ "21"
+ "22"
+ "23"
+ "3"
+ "4"
+ "5"
+ "6"
+ "7"
+ "8"
+ "9"
+ "@\"<CSDetectionServiceProtocol>\""
+ "@\"<CSPowerlogDBReaderProtocol>\""
+ "@\"CSIntervalList\"32@0:8@\"NSDate\"16@\"NSDate\"24"
+ "@\"CSIntervalList\"40@0:8@\"NSString\"16@\"NSDate\"24@\"NSDate\"32"
+ "@\"CSIntervalList\"52@0:8@\"NSString\"16@\"NSDate\"24@\"NSDate\"32B40@\"NSString\"44"
+ "@\"NSArray\"32@0:8@\"NSDate\"16@\"NSDate\"24"
+ "@\"NSArray\"44@0:8i16@\"NSDate\"20@\"NSDate\"28@\"NSDate\"36"
+ "@\"NSArray\"52@0:8i16@\"NSDate\"20@\"NSDate\"28@\"NSDate\"36d44"
+ "@\"NSDate\"16@0:8"
+ "@\"NSDate\"24@0:8@\"NSDate\"16"
+ "@\"NSDateInterval\"16@0:8"
+ "@\"NSMutableDictionary\"52@0:8@\"NSDate\"16@\"NSDate\"24@\"NSArray\"32@\"NSArray\"40B48"
+ "@\"NSURL\""
+ "@\"NSXPCConnection\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8d16"
+ "@24@0:8i16f20"
+ "@40@0:8C16@20i28@32"
+ "@40@0:8i16i20i24f28@32"
+ "@52@0:8@16@24@32B40@44"
+ "@60@0:8i16@20@28@36@44@52"
+ "@76@0:8f16@20@28@36@44@52B60f64i68i72"
+ "@84@0:8f16f20f24@28@36@44@52@60B68f72i76i80"
+ "@88@0:8f16f20f24@28@36@44@52@60B68f72i76i80C84"
+ "All thermal issues should skip first kill. Current policy bitmask: %d"
+ "B24@0:8@\"NSDictionary\"16"
+ "B40@0:8@16@24@32"
+ "B40@0:8C16@20i28@32"
+ "Band80Processes: %@"
+ "Band95Processes: %@"
+ "C44@0:8@16@24^C32C40"
+ "CPUMonDetection"
+ "CSDetectionService"
+ "CSDetectionServiceConnection"
+ "CSDetectionServiceProtocol"
+ "CSPenaltyManager"
+ "CSPowerlogDBReaderProtocol"
+ "Cannot determine coalition data boundary. Using current time."
+ "Clock change detected. Last coalition end (%@) > current coalition end (%@). Resetting state."
+ "ComputeSafeguardsScheduledWorkReporting"
+ "ComputeSafeguardsViolationReporting"
+ "Connection error occurred: %@"
+ "Connection interrupted while service is active."
+ "Connection invalidated while service is active."
+ "DASWorkCompleted"
+ "DiagnosticExtensions.FileArchiverService"
+ "Dropped oldest entries from processDataHistory, now contains %lu entries"
+ "End"
+ "EndDate"
+ "Error when getting DASCPUIntensiveDuration for process %@"
+ "Error when getting DisplayOnDuration"
+ "Error when getting OngoingRestoreDuration for fastPassName %@"
+ "Error when getting ThermalLimitedChargingDuration"
+ "Error when getting WallClockDuration"
+ "Error when getting WallClockDurationUnplugged"
+ "Evaluate rule %d in sliding windows with endDate range [%@, %@]"
+ "Evaluating thermal rule %d with data window from %@ to %@"
+ "Exception getting thermal status"
+ "Executing delayed fatal mitigation for process:%@ with %lu pids"
+ "Executing delayed throttle mitigation for process:%@ coalitionID:%llu"
+ "Failed to get complete thermal status"
+ "Failed to read SMC temperature."
+ "File does not exist: '%@'"
+ "Forcing thermal detection with collected coalition data."
+ "Grace period expired, proceeding with termination for PID %d"
+ "Grace period expired, proceeding with throttling for PID %d"
+ "HIGH_TEMP_ACTIVE"
+ "HIGH_TEMP_ACTIVE: Collecting top coalitions and running detectors."
+ "HIGH_TEMP_ACTIVE: Starting 1-minute data collection timer."
+ "Handling CPUMon violation for process: %@, pid: %llu."
+ "HistoryPoints"
+ "INACTIVE"
+ "INACTIVE: Stopping data collection timer."
+ "Initialized %lu thermal detection rules."
+ "Initializing Rule Based Detection"
+ "Invalid temperature sampling interval provided."
+ "Invoking issue detection with firstEndDate: %@, lastEndDate: %@"
+ "IssuePriority"
+ "LastTimestamp"
+ "Lifting mitigations for DAS intensive processes: %@"
+ "Loading Processes, Scenarios and Restrictions"
+ "Loading from process_policies.plist"
+ "Modified temperature sampling timer to %.1fs interval"
+ "NO"
+ "NSCoding"
+ "NSSecureCoding"
+ "Name"
+ "No name"
+ "NoCoalitionNameFound"
+ "NotChargingReason"
+ "PE_%d_%lu_%@"
+ "PerformanceTrace.PerformanceTraceService"
+ "PollingInterval"
+ "PowerCoal"
+ "PowerCoalList"
+ "PowerCoalName"
+ "Process %@ was not previously mitigated, no restoration needed"
+ "Process %@ was previously mitigated (penaltyBox:%d), tracking for restoration"
+ "Process exceeded power usage limits"
+ "Process will be terminated due to excessive power usage"
+ "Process will be throttled due to excessive power usage"
+ "ProcessNotAllowed"
+ "ProcessPolicies"
+ "ProcessPolicies: %@"
+ "Q24@0:8Q16"
+ "Received CPUMon violation for process: %@, pid: %llu."
+ "Restoring mitigations for completed DAS processes: %@"
+ "Restoring mitigations for process %@ after DAS work completion"
+ "Restrictions: %@"
+ "SELECT * FROM (SELECT * FROM XPCMetrics_OngoingRestore_14_2 WHERE fastPassName = '%@' AND timestamp < %f ORDER BY timestamp DESC LIMIT 1) UNION SELECT * FROM XPCMetrics_OngoingRestore_14_2 WHERE fastPassName = '%@' AND timestamp >= %f AND timestamp < %f ORDER BY timestamp"
+ "SELECT * FROM PLDuetService_EventNone_DASActivityLifecycle WHERE (processName = '%@' OR ',' || InvolvedProcesses || ',' LIKE '%%,%@,%%') AND StartDate < %f AND EndDate > %f"
+ "SELECT MAX(timestampEnd) AS maxTimestamp FROM PLCoalitionAgent_EventInterval_CoalitionInterval"
+ "SELECT max(timestamp) as LastTimestamp from PLBatteryAgent_EventBackward_Battery;"
+ "SELECT min(timestamp) AS Start, max(timestamp) as End from PLBatteryAgent_EventBackward_Battery;"
+ "SELECT timestamp, NotChargingReason, SlowChargingReason, ExternalConnected FROM PLBatteryAgent_EventBackward_Battery WHERE timestamp >= %f - 300 AND timestamp < %f ORDER by timestamp"
+ "SELECT timestamp, timestampEnd FROM PLDisplayAgent_EventPoint_Display WHERE Active = 1 AND timestampEnd >= %f AND timestamp <= %f ORDER BY timestamp"
+ "SMC Read: key=%{public}@, type=sp78, raw=%d, converted=%.2f°C"
+ "SMC library definitions are available. Real hardware will be used."
+ "STATE TRANSITION: HIGH_TEMP_ACTIVE -> INACTIVE (Avg Temp %.1f°C < 35°C)"
+ "STATE TRANSITION: INACTIVE -> HIGH_TEMP_ACTIVE (Avg Temp %.1f°C >= 35°C)"
+ "Scenarios: %@"
+ "Scheduled termination for PID %d after %.1f second grace period"
+ "Scheduled throttling for PID %d after %.1f second grace period"
+ "Skip evaluating rule %d since duration from %@ to %@ is not enough for %f"
+ "Skip evaluating rule %d since firstEndDate %@ is later than lastEndDate %@"
+ "Skip evaluating rule %d since startDate %@ is later than endDate %@"
+ "Skipping rule %d, not enough data (%lu) for window size (%lu)"
+ "SlowChargingReason"
+ "Start"
+ "Start detection for rule %d: Fixed window from %@ to %@"
+ "Start detection for rule %d: Sliding window from firstEndDate %@ to lastEndDate %@"
+ "StartDate"
+ "Started PowerExceptions XPC service"
+ "T@\"<CSDetectionServiceProtocol>\",R,V_service"
+ "T@\"<CSPowerlogDBReaderProtocol>\",&,N,V_powerlogDBReader"
+ "T@\"CSDetectionRule\",&,V_specialRule"
+ "T@\"NSArray\",&,N,V_thermalDetectionRules"
+ "T@\"NSArray\",&,V_primaryDetectors"
+ "T@\"NSDate\",&,V_lastCoalitionDataEnd"
+ "T@\"NSDate\",&,V_lastThermalTimerDate"
+ "T@\"NSDictionary\",&,V_additionalMetrics"
+ "T@\"NSDictionary\",&,V_exemptedProcessesDict"
+ "T@\"NSMutableArray\",&,N,V_processDataHistory"
+ "T@\"NSMutableArray\",&,N,V_temperatureHistory"
+ "T@\"NSMutableSet\",&,V_currentDASIntensiveProcesses"
+ "T@\"NSMutableSet\",&,V_previouslyMitigatedDASProcesses"
+ "T@\"NSNumber\",&,V_lastTemperatureReading"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_rateMonitoringTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_thermalTimer"
+ "T@\"NSSet\",&,V_allowedProcessesSet"
+ "T@\"NSURL\",&,V_fileURL"
+ "T@\"NSXPCConnection\",&,N,V_connectionToServer"
+ "TB,N,V_smcConnectionOpen"
+ "TB,R"
+ "TB,V_thermalTriggerEnabled"
+ "TB,V_trialsMitigationsEnabled"
+ "TC,V_ruleType"
+ "THERMAL TRIGGER: 5-second thermal event timer armed."
+ "THERMAL TRIGGER: Starting thermal monitoring."
+ "THERMAL VIOLATION DETECTED by rule %d: Coalition '%@' (CID: %@) averaged %.2fmW over %lu minutes (Threshold: %.0fmW)"
+ "TQ,N,V_cid"
+ "TQ,N,V_sz"
+ "TQ,N,V_thermalTriggerState"
+ "TVRM"
+ "T^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB},N,V_smcConnection"
+ "Temperature"
+ "Tf,V_coalitionCollectionInterval"
+ "Tf,V_savedThermalPollingInterval"
+ "Tf,V_temperatureSamplingInterval"
+ "Tf,V_thermalPollingInterval"
+ "Tf,V_triggerCPUThreshold"
+ "Tf,V_triggerLookbackDuration"
+ "Thermal"
+ "Thermal Event: Temp=%.1f°C, Avg=%.1f°C, State=%@"
+ "Thermal monitoring disabled, skipping SMC connection"
+ "Thermal monitoring disabled, skipping thermal key read"
+ "Thermal monitoring flag read: %{public}s (from domain: com.apple.computesafeguards)"
+ "Thermal monitoring is disabled by feature flag"
+ "Thermal trigger disabled, skipping processing."
+ "Thermal::%@"
+ "Thermal::%@::%@"
+ "ThermalPenaltyServed"
+ "ThermalTriggerEvents"
+ "Ti,N,V_cid"
+ "Ti,V_unit"
+ "Top offender(not necessarily  rule breaker) by rule %d: Coalition '%@' (CID: %@) averaged %.2fmW over %lu minutes (Threshold: %.0fmW)"
+ "UIKitApplication:"
+ "URLForKey:"
+ "UUID"
+ "Unit"
+ "Unknown numeric SMC type: %d"
+ "Unnamed_launchdName"
+ "Unsupported key size %d for SMC key %@ with Array attribute."
+ "Unsupported key size %d for SMC key %@."
+ "Updated firstEndDate (was %@) to account for deviceBootTime %@"
+ "Updated lastCoalitionDataEnd to %@"
+ "Updated rules array: rule3 added (fatal mitigation list has %lu processes)"
+ "Updated rules array: rule3 removed (fatal mitigation list is empty)"
+ "YES"
+ "["
+ "[Trials] Process policies have been modified: %@"
+ "[Trials] Process policies override not provided, using default process policies..."
+ "[Trials] Using default process policies..."
+ "^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB}"
+ "^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB}16@0:8"
+ "^{coalition_resource_usage=QQQQQQQQQQQQQQQQQQQQQQQQ[7Q]QQQQQQQQQQQQQQ}16@0:8"
+ "_additionalMetrics"
+ "_allowedProcessesSet"
+ "_cid"
+ "_coalitionCollectionInterval"
+ "_coalitionIdsToNames"
+ "_collectAndDetect"
+ "_collectTopCoalitions"
+ "_connectionToServer"
+ "_currentDASIntensiveProcesses"
+ "_exemptedProcessesDict"
+ "_fileURL"
+ "_getThermalStateName:"
+ "_initWithProcessPolicies:"
+ "_initWithProcessPolicies: XPC Services mitigations disabled by feature flag"
+ "_initWithProcessPolicies: mitigations enabled by feature flag"
+ "_initWithProcessPolicies: mitigations while plugged-in enabled by feature flag"
+ "_initWithProcessPolicies: penaltyBox enabled by feature flag"
+ "_initWithProcessPolicies:andBand95:andBand80:"
+ "_lastCoalitionDataEnd"
+ "_lastTemperatureReading"
+ "_lastThermalTimerDate"
+ "_machTimeToNanoseconds:"
+ "_previousCoalitions"
+ "_previouslyMitigatedDASProcesses"
+ "_primaryDetectors"
+ "_processDataHistory"
+ "_processPolicyDictWithErrors:"
+ "_rateMonitoringTimer"
+ "_ruleType"
+ "_savedThermalPollingInterval"
+ "_service"
+ "_smcConnection"
+ "_smcConnectionOpen"
+ "_specialRule"
+ "_startHighTempDataCollection"
+ "_startThermalMonitoring"
+ "_stopHighTempDataCollection"
+ "_sz"
+ "_temperatureHistory"
+ "_temperatureSamplingInterval"
+ "_thermalDetectionRules"
+ "_thermalPollingInterval"
+ "_thermalTimer"
+ "_thermalTriggerEnabled"
+ "_thermalTriggerState"
+ "_triggerCPUThreshold"
+ "_triggerLookbackDuration"
+ "_unit"
+ "additionalMetrics"
+ "allowedProcessesSet"
+ "allowed_processes"
+ "averageTemperature"
+ "boolForKey:"
+ "calculateAverageTemperature:overLast:"
+ "callCoalInfoResourceUsage"
+ "checkCpuPercentageAndInvokeIssueDetection:windowStartDate:coalitionDataBoundary:"
+ "checkDrainAndInvokeIssueDetection:coalitionDataBoundary:"
+ "checkForTrials: default value for mitigationsEnabled: %@"
+ "cid"
+ "clearAllThermalTimers"
+ "clearAllThermalTimers: Cleared all thermal timers"
+ "clearThermalTimerForProcess:"
+ "clearThermalTimerForProcess: Cleared thermal timer for process %@"
+ "closeSMCConnection"
+ "coalitionCollectionInterval"
+ "coalitions"
+ "com.apple.CSDetectionService"
+ "com.apple.ExceptionsInducerAppService"
+ "com.apple.Maps"
+ "com.apple.PerfPowerServices.ExceptionsInducer"
+ "com.apple.PerfPowerServices.ExceptionsInducer-DDI"
+ "com.apple.PerformanceTrace.PerformanceTraceService"
+ "com.apple.communicationtrustd"
+ "com.apple.computesafeguards"
+ "com.apple.computesafeguards.processPolicies"
+ "com.apple.computesafeguards.ruleMitigationPolicies"
+ "com.apple.computesafeguards.thermalMonitoringEnabled"
+ "com.apple.coreautomationd"
+ "com.apple.corecaptured"
+ "com.apple.finhealthd"
+ "com.apple.fitnessintelligenced"
+ "com.apple.healthd.post-install-update.fastpass"
+ "com.apple.heartratecoordinatord"
+ "com.apple.imtool"
+ "com.apple.ind"
+ "com.apple.modelcatalog"
+ "com.apple.perceptiond"
+ "com.apple.sirittsd"
+ "com.apple.soundanalysisd"
+ "com.apple.storekitd"
+ "com.apple.trustd"
+ "connectionToServer"
+ "coreautomationd?\\..*|^com\\.openssh\\.sshd\\."
+ "createNotificationForMitigation:forProcess:pid:reason:"
+ "createThermalCSProcess: Created lightweight CSProcess for thermal violation - process:%@ pid:%d coalitionID:%llu"
+ "createThermalCSProcess: Failed to create CSProcess for %@"
+ "createThermalCSProcess: Invalid parameters"
+ "createThermalCSProcess: Successfully registered thermal CSProcess with ProcessManager for %@"
+ "createThermalCSProcess:withUUID:"
+ "currentDASIntensiveProcesses"
+ "currentTemperature"
+ "decideMitigation:withCoalitionName:withReason:withPrevIssue:"
+ "decodeIntegerForKey:"
+ "decodeObjectForKey:"
+ "defaultManager"
+ "detectIssuesFromFirstEndDate:toLastEndDate:"
+ "detectIssuesFromFirstEndDate:toLastEndDate:withRules:"
+ "detectIssuesFromFirstEndDate:toLastEndDate:withRules: No rule based detection: PowerExceptions/safeguards_rule_detection feature flag is off"
+ "detectThermalIssuesWithData:"
+ "detectThermalIssuesWithData: processDataHistory is empty, skipping detection."
+ "detectWithLookbackDuration:withReply:"
+ "detection"
+ "dictionaryWithContentsOfURL:"
+ "dictionaryWithObjectsAndKeys:"
+ "disableThermalTrigger"
+ "disableThermalTriggerWithHandler:"
+ "disabled"
+ "e"
+ "enableThermalTrigger"
+ "enableThermalTriggerWithHandler:"
+ "enabled"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "enumerateObjectsUsingBlock:"
+ "error"
+ "evaluateRuleWithSlidingWindow:withFirstEndDate:andLastEndDate:"
+ "executeDelayedFatalMitigation: Killed %d out of %d pids that matched coalitionID %llu with final retVal %d for process:%@"
+ "executeDelayedFatalMitigation:matchedCoalitionPids:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:"
+ "executeDelayedThrottleMitigation:coalitionID:coalitionName:issueType:startTime:endTime:mitigationType:mitigationDecisionType:mitigationDecisionReason:withError:"
+ "exemptedProcessesDict"
+ "exempted_processes"
+ "experimentIdentifiersWithNamespaceName:"
+ "fastPassName"
+ "fastPassName is missing in additionalMetrics for OngoingRestoreDuration"
+ "fileExistsAtPath:"
+ "fileURL"
+ "fileURLWithPath:"
+ "fileValue"
+ "forceDetectionWithFirstEndDate:lastEndDate:withHandler"
+ "forceDetectionWithFirstEndDate:lastEndDate:withHandler:"
+ "forceThermalDetectionWithHandler:"
+ "generateThermalMetadata:"
+ "generateThermalPayloadWithMetadata:triggeredDetection:triggeredType:"
+ "getCoalIds"
+ "getCoalName"
+ "getCurrentTemperature"
+ "getDASActivityIntervalsWithProcessName:andStartDate:andEndDate:"
+ "getDASActivityIntervalsWithProcessName:withStartDate:andEndDate:andCPUIntensive:withTaskName:"
+ "getDetectionLookbackDuration:"
+ "getDisplayOnIntervalListWithStartDate:andEndDate:"
+ "getLastTimestamp"
+ "getLogInterval"
+ "getMaxCoalitionTimestamp"
+ "getMaxCoalitionTimestamp: Failed to retrieve max timestamp"
+ "getOngoingRestoreIntervalsWithFastPassName:andStartDate:andEndDate:"
+ "getProcessesForCoalitionIDUsingDirectPolling:"
+ "getProcessesForCoalitionIDUsingDirectPolling: Found %lu processes for coalition %d"
+ "getProcessesForCoalitionIDUsingDirectPolling: Found matching process PID=%d, name=%@, coalition=%llu"
+ "getProcessesForCoalitionIDUsingDirectPolling: Not enough memory to allocate PID buffer"
+ "getProcessesForCoalitionIDUsingDirectPolling: proc_listpids failed to get PID list"
+ "getProcessesForCoalitionIDUsingDirectPolling: proc_listpids failed to get buffer size"
+ "getTemperatureSamplingInterval"
+ "getThermalIssueWithMitigationSuggestionForCoalitionID:withRule:withValue:withLaunchdName:fromStartDate:toEndDate:"
+ "getThermalLimitedChargingIntervalListWithStartDate:andEndDate:"
+ "getThermalPollingInterval"
+ "getThermalPollingInterval: Exception caught: %@"
+ "getThermalPollingIntervalWithHandler:"
+ "getThermalSamplingIntervalWithHandler:"
+ "getThermalTemperatureWithHandler:"
+ "getThermalTriggerStatus"
+ "getThermalTriggerStatus: Exception caught: %@"
+ "getThermalTriggerStatus: Inner exception: %@"
+ "getThermalTriggerStatusWithHandler:"
+ "getTriggerParameters"
+ "getTriggerParametersWithHandler:"
+ "getValue:"
+ "getValueOfMetric:startDate:endDate:processName:additionalMetrics:"
+ "gracePeriod"
+ "handleCPUDetectionViolation:coalitionID:coalitionName:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:"
+ "handleDetectedIssues: Found issues with rule %d (%@) issue for process %@ with coalitionID: %llu from time %s to %s [%@]"
+ "handleDetectionViolation: Mitigations not allowed for process:%@"
+ "handleDetectorViolation: issue.launchdName is Null or empty string, fetching coalitionName"
+ "handlePenaltyState: CPU Coalition penalty box active - using issue priority for thermal issue for process %@"
+ "handlePenaltyState: CPU Coalition penalty box not active - starting thermal timer for process %@"
+ "handlePenaltyState: CPUCoalitionBased issue - clearing thermal timers and enabling penalty box for process %@"
+ "handlePenaltyState: Invalid parameters"
+ "handlePenaltyState: Other issue type %s - using default penalty box logic for process %@"
+ "handlePenaltyState: Processing process %@ with prevIssue %s, current issueType %s"
+ "handlePenaltyState: Result for process %@ - shouldPutInPenaltyBox:%s useIssuePriority:%s"
+ "handlePenaltyState:withPrevIssue:shouldPutInPenaltyBox:useIssuePriority:"
+ "historyPoints"
+ "i64@0:8@16Q24@32^C40^C48^@56"
+ "i76@0:8@16Q24Q32@40C48^C52^C60^@68"
+ "initWithCoder:"
+ "initWithDBReader:"
+ "initWithFileURL:"
+ "initWithScalarMetric:andNormalizerMetric:andComparator:andValue:andAdditionalMetrics:"
+ "initWithServiceName:"
+ "initWithStartDate:endDate:"
+ "initWithSuiteName:"
+ "initWithThermalCondition:andValue:"
+ "initWithWarningType:gracePeriod:notificationID:reason:processInfo:"
+ "initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:"
+ "initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:"
+ "initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:unit:ruleType:"
+ "initializeCPUDetectionRules"
+ "initializeThermalDetectionRules"
+ "interval"
+ "invalidate"
+ "invokeIssueDetectionFromFirstEndDate:toLastEndDate:"
+ "isCPUCoalitionPenaltyBoxActive: Process %@ is in penalty box with CPU Coalition previous issue - ACTIVE"
+ "isCPUCoalitionPenaltyBoxActive: Process %@ not in penalty box but has endTime %llu - saving state"
+ "isCPUCoalitionPenaltyBoxActive:withPrevIssue:"
+ "isProcessAllowed:"
+ "isProcessRegistered:"
+ "isThermalLimitedCharging:"
+ "isThermalTimerActiveForProcess:"
+ "isThermalTriggerEnabled"
+ "isThermalTriggerEnabledWithHandler:"
+ "kernel_coalition"
+ "killProcess:pid:coalitionID:coalitionName:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "lastCoalitionDataEnd"
+ "lastTemperatureReading"
+ "lastThermalTimerDate"
+ "liftMitigationsForDASProcesses:"
+ "liftMitigationsForDASProcesses: Could not locate object for processIdentifier:%@"
+ "logCPUViolationToPowerLog: timestampEnd is before timestampStart, skipping"
+ "logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:"
+ "logMitigationToPowerLogForProcess:withPid:withCoalitionID:withCoalitionName:withIssueType:withMitigationType:withReason:"
+ "logThermalTriggerToPPS:triggeredDetection:triggeredType:"
+ "lookback"
+ "maxTimestamp"
+ "mitigation-allowed"
+ "modifyTemperatureSamplingInterval:"
+ "modifyThermalPollingInterval:"
+ "modifyThermalPollingInterval: Exception caught: %@"
+ "modifyThermalPollingInterval: Inner exception: %@"
+ "modifyThermalPollingInterval: _rateMonitoringTimer is nil"
+ "modifyThermalPollingInterval: interval is nil"
+ "modifyThermalPollingInterval:withHandler:"
+ "modifyThermalSamplingInterval:withHandler:"
+ "modifyTriggerWithInterval:withLookback:withThreshold:"
+ "name"
+ "numberWithInteger:"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedShort:"
+ "openSMCConnection"
+ "path"
+ "pid"
+ "policyMitigationsEnabled: mitigationsEnabled=%@ (gEnableMitigations=%ld, trialsMitigationsEnabled=%d)"
+ "power"
+ "previouslyMitigatedDASProcesses"
+ "primaryDetectors"
+ "processDataHistory"
+ "processThermalEvent"
+ "putIntoPenaltyBoxForCSProcess:coalitionID:coalitionName:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "q24@?0@\"CSInterval\"8@\"CSInterval\"16"
+ "queueMitigationNotification:forPID:"
+ "rangeOfString:"
+ "rateMonitoringTimer"
+ "rateMonitoringTimerActive"
+ "readKey:"
+ "readThermalKey"
+ "readThermalKey: Exception caught: %@"
+ "reason"
+ "registerThermalCSProcess: Invalid parameters - process:%@ identifier:%@"
+ "registerThermalCSProcess: Process %@ already registered, updating existing CSProcess"
+ "registerThermalCSProcess: Successfully registered thermal CSProcess for %@ with UUID %@"
+ "registerThermalCSProcess: Updated existing CSProcess for %@"
+ "registerThermalCSProcess:forIdentifier:"
+ "removeObjectsInRange:"
+ "restoreMitigationsForCompletedDASProcesses:"
+ "restoreStateForProcess:"
+ "restoreStateForProcess: Invalid process"
+ "restoreStateForProcess: No saved state found for process %@"
+ "restoreStateForProcess: Restored penalty box duration to %@ mins for process %@"
+ "ruleType"
+ "saveStateForProcess:"
+ "saveStateForProcess: Invalid process"
+ "saveStateForProcess: Saved penalty box duration %@ mins for process %@"
+ "savedThermalPollingInterval"
+ "sendNotificationBeforeMitigation: Failed to create notification for PID %d"
+ "sendNotificationBeforeMitigation: Process PID %d not registered for notifications"
+ "sendNotificationBeforeMitigation: Sent notification for PID %d, type %lu"
+ "sendNotificationBeforeMitigation:forProcess:pid:reason:"
+ "service"
+ "setAdditionalMetrics:"
+ "setAllowedProcessesSet:"
+ "setCid:"
+ "setCoalitionCollectionInterval:"
+ "setConnectionToServer:"
+ "setCurrentDASIntensiveProcesses:"
+ "setExemptedProcessesDict:"
+ "setFileURL:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setLastCoalitionDataEnd:"
+ "setLastTemperatureReading:"
+ "setLastThermalTimerDate:"
+ "setPreviouslyMitigatedDASProcesses:"
+ "setPrimaryDetectors:"
+ "setProcessDataHistory:"
+ "setRateMonitoringTimer:"
+ "setRemoteObjectInterface:"
+ "setRuleType:"
+ "setSavedThermalPollingInterval:"
+ "setSmcConnection:"
+ "setSmcConnectionOpen:"
+ "setSpecialRule:"
+ "setSz:"
+ "setTemperatureHistory:"
+ "setTemperatureSamplingInterval:"
+ "setThermalDetectionRules:"
+ "setThermalPollingInterval:"
+ "setThermalTimer:"
+ "setThermalTriggerEnabled:"
+ "setThermalTriggerState:"
+ "setTriggerCPUThreshold:"
+ "setTriggerLookbackDuration:"
+ "setUnit:"
+ "setValuesForKeysWithDictionary:"
+ "sharedInstanceWithProcessPolicies:"
+ "sharedInstanceWithProcessPolicies:andBand95:andBand80:"
+ "sharedService"
+ "smcConnection"
+ "smcConnectionOpen"
+ "sort"
+ "sortUsingComparator:"
+ "specialRule"
+ "startListener"
+ "startThermalTimerForProcess:"
+ "startThermalTimerForProcess: Failed to create timer for process %@"
+ "startThermalTimerForProcess: Failed to get CSMitigationManager shared instance for process %@"
+ "startThermalTimerForProcess: Failed to remove process %@ from penalty box with error %d"
+ "startThermalTimerForProcess: Invalid process"
+ "startThermalTimerForProcess: Started thermal timer for process %@ (%d minutes)"
+ "startThermalTimerForProcess: Successfully removed process %@ from penalty box after thermal timer expiration"
+ "startThermalTimerForProcess: Thermal timer expired for process %@, restoring state and removing from penalty box"
+ "stopThermalTimerForProcess:"
+ "stopThermalTimerForProcess: Stopped thermal timer for process %@"
+ "subarrayWithRange:"
+ "supportsSecureCoding"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "sz"
+ "telemetry-only"
+ "temperatureHistory"
+ "temperatureSamplingInterval"
+ "thermalDetectionRules"
+ "thermalPollingInterval"
+ "thermalTimer"
+ "thermalTimerActive"
+ "thermalTriggerEnabled"
+ "thermalTriggerState"
+ "threshold"
+ "triggerCPUThreshold"
+ "triggerLookbackDuration"
+ "unit"
+ "unsignedLongLongValue"
+ "updateRulesArray"
+ "updateTemperatureHistory:"
+ "v116@0:8@16Q24Q32@40{mach_timespec=Ii}48q56q64q72q80B88q92q100@108"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB}16"
+ "v24@?0@\"NSString\"8^B16"
+ "v32@0:8^d16Q24"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSArray\">24"
+ "v32@0:8d16i24i28"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "v44@0:8@16C24^B28^B36"
+ "v56@0:8@16i24Q28@36C44C48C52"
+ "v88@0:8@16Q24@32C40d44d52C60^C64^C72^@80"
+ "v92@0:8@16Q24@32Q40{mach_timespec=Ii}48q56q64q72q80B88"
+ "v96@0:8@16@24Q32@40C48d52d60C68^C72^C80^@88"
+ "valueWithBytes:objCType:"
+ "violationCount"
+ "warningType"
+ "{?=QQ@}"
- "++UnpluggedDuration condition meet"
- "--UnpluggedDuration condition not meet"
- "@36@0:8i16@20@28"
- "@48@0:8@16@24@32@40"
- "@72@0:8f16@20@28@36@44@52B60f64i68"
- "@80@0:8f16f20f24@28@36@44@52@60B68f72i76"
- "Band80Process: %@"
- "Band95Process: %@"
- "C40@0:8@16@24^C32"
- "Could not create processes set from plist"
- "Error when getting UnpluggedDuration"
- "Evaluate rule %d in sliding windows in range [%@, %@]"
- "Exempt Processes plist failure"
- "Loading Processes, ExemptProcesses, Scenarios and Restrictions"
- "Loading process_policies.plist"
- "Loading processes.plist"
- "PerfPowerServices"
- "Prepare detection for rule %d: Waiting for %.0f seconds, without sliding window"
- "Process Policies dictionary missing"
- "Processes Policy plist failure"
- "Processes array missing"
- "Processes plist failure"
- "Received CPU violation for process: %@, pid: %llu."
- "SafeguardsScheduledWorkReporting"
- "SafeguardsViolationReporting"
- "Skip evaluating rule since duration from %@ to %@ is not enough for %f"
- "Skip evaluating rule since startDate %@ is later than endDate %@"
- "Start detection for rule %d: From %@ to %@, with sliding window"
- "Start detection for rule %d: From %@ to %@, without sliding window"
- "Starting Rule Based Detection"
- "T@\"NSArray\",&,V_genericCPUDetectorProcessDenyList"
- "T@\"NSDictionary\",&,V_processPoliciesDict"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_triggerTimer"
- "T@\"NSRegularExpression\",&,V_genericCPUDetectorProcessDenyRegex"
- "T@\"NSSet\",&,N,V_activeScenariosLastEvaluation"
- "T@\"NSSet\",&,N,V_activeScenariosLastPublished"
- "T@\"NSSet\",&,V_processes"
- "Ti,V_trialsMitigationsEnabled"
- "U"
- "_activeScenariosLastEvaluation"
- "_activeScenariosLastPublished"
- "_genericCPUDetectorProcessDenyList"
- "_genericCPUDetectorProcessDenyRegex"
- "_initWithDataProvider: XPC Services mitigations disabled by feature flag"
- "_initWithDataProvider: mitigations enabled by feature flag"
- "_initWithDataProvider: mitigations while plugged-in enabled by feature flag"
- "_initWithDataProvider: penaltyBox enabled by feature flag"
- "_initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:"
- "_processPoliciesDict"
- "_processes"
- "_processesPoliciesDictWithErrors:"
- "_processesSetWithErrors:"
- "activeScenariosLastEvaluation"
- "activeScenariosLastPublished"
- "addTimeInterval:"
- "checkCpuPercentageAndInvokeIssueDetection:windowStartDate:"
- "checkDrainAndInvokeIssueDetection:"
- "com.apple.mediaanalysisd"
- "coreautomation\\.coreautomationd|^com\\.openssh\\.sshd\\."
- "decideMitigation:withCoalitionName:withReason:"
- "detectIssuesFromStartTime:endDate:withRules:"
- "detectWithLookbackDuration:"
- "detectWithLookbackDuration: Finish detection for rule %d: Detected %lu issues"
- "detectWithLookbackDuration: No rule based detection: PerfPowerServices/safeguards_rule_detection feature flag is off"
- "detectWithLookbackDuration: Start detection for rule %d: From %@ to %@, without sliding window"
- "evaluateRuleWithSlidingWindow:withStartDate:andEndDate:"
- "forceDetectionWithStartTime:endTime:withHandler"
- "forceDetectionWithStartTime:endTime:withHandler:"
- "genericCPUDetectorProcessDenyList"
- "genericCPUDetectorProcessDenyRegex"
- "getAPWakeIntervalListWithStartDate Query:%@"
- "getDetectionLookbackDuration"
- "getTriggerInterval"
- "getTriggerIntervalWithHandler:"
- "getValueOfMetric:startDate:endDate:"
- "handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:"
- "handleDetectedIssues: Found issues with rule %d issue %@ for process %@ with coalitionID: %llu from time %s to %s"
- "i56@0:8@16Q24^C32^C40^@48"
- "i68@0:8@16Q24Q32C40^C44^C52^@60"
- "initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:"
- "initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:"
- "killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:"
- "logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:"
- "logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:"
- "modifyTriggerInterval:"
- "policyMitigationsEnabled: Not an internal build so mitigations always disabled"
- "policyMitigationsEnabled: Trials says no mitigations"
- "policyMitigationsEnabled: Trials says to mitigate"
- "policyMitigationsEnabled: invalid _trialsMitigationsEnabled value (%d)"
- "processPoliciesDict"
- "process_policies"
- "process_policies dictionary missing"
- "processes"
- "processesPolicies: %@"
- "processesSet"
- "processesSet: %@"
- "putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:"
- "scenariosSet: %@"
- "setActiveScenariosLastEvaluation:"
- "setActiveScenariosLastPublished:"
- "setGenericCPUDetectorProcessDenyList:"
- "setGenericCPUDetectorProcessDenyRegex:"
- "setProcessPoliciesDict:"
- "setProcesses:"
- "sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:"
- "testDetectWithLookbackDuration"
- "updateCPUBuffer:"
- "v108@0:8@16Q24@32{mach_timespec=Ii}40q48q56q64q72B80q84q92@100"
- "v48@0:8@16i24Q28C36C40C44"
- "v84@0:8@16Q24Q32{mach_timespec=Ii}40q48q56q64q72B80"

```

## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0x110e4
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x120c
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__cstring: 0x17c1
-  __TEXT.__oslogstring: 0x2215
-  __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x448
-  __TEXT.__objc_classname: 0x225
-  __TEXT.__objc_methname: 0x2ec9
-  __TEXT.__objc_methtype: 0x6af
-  __TEXT.__objc_stubs: 0x18e0
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__objc_classlist: 0x90
+2954.0.0.502.3
+  __TEXT.__text: 0x2c8b0
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x24bc
+  __TEXT.__const: 0x240
+  __TEXT.__gcc_except_tab: 0x498
+  __TEXT.__cstring: 0x331f
+  __TEXT.__oslogstring: 0x6468
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__objc_classname: 0x2d9
+  __TEXT.__objc_methname: 0x665c
+  __TEXT.__objc_methtype: 0xdae
+  __TEXT.__objc_stubs: 0x3ac0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0x15d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0xff8
-  __AUTH_CONST.__auth_got: 0x2f0
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1e00
-  __AUTH_CONST.__objc_const: 0x1e70
-  __AUTH_CONST.__objc_intobj: 0x3e40
-  __AUTH_CONST.__objc_dictobj: 0x528
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x898
+  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x3280
+  __AUTH_CONST.__objc_const: 0x38b8
+  __AUTH_CONST.__objc_intobj: 0x3ed0
+  __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_doubleobj: 0xf20
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14c
-  __DATA.__data: 0x300
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x4
-  __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0xf8
+  __AUTH_CONST.__objc_doubleobj: 0xf70
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x2ec
+  __DATA.__data: 0x318
+  __DATA.__common: 0x48
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F4998D0-09C6-30F9-9740-34079A6C88A4
-  Functions: 516
-  Symbols:   1705
-  CStrings:  1266
+  - /usr/lib/libspindump.dylib
+  UUID: C5F006CA-05EF-32E5-93EB-EC9640219A2C
+  Functions: 1077
+  Symbols:   3377
+  CStrings:  2513
 
Symbols:
+ +[CPUEnergySnapshot snapshotCPUEnergy:]
+ +[CPUEnergySnapshot snapshotCPUEnergy:].cold.1
+ +[CPUEnergySnapshot snapshotCPUEnergy:].cold.2
+ +[CPUEnergySnapshot snapshotCPUEnergy:].cold.3
+ +[CSCPUMonitorHelper clearMonitorForPID:].cold.1
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:]
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:].cold.1
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:].cold.2
+ +[CSIssueDetector sharedInstance]
+ +[CSIssueDetector sharedInstance].cold.1
+ +[CSLogger signpostCategory]
+ +[CSMitigationManager sharedInstance]
+ +[CSMitigationManager sharedInstance].cold.1
+ +[CSPowerlogDBReader sharedInstance]
+ +[CSPowerlogDBReader sharedInstance].cold.1
+ +[CSProcessManager coalitionIDForPid:coalitionID:]
+ +[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:]
+ +[CSTriggerManager run]
+ +[CSTriggerManager run].cold.1
+ +[CSTriggerManager sharedInstance]
+ +[CSTriggerManager sharedInstance].cold.1
+ -[CPUEnergySnapshot .cxx_destruct]
+ -[CPUEnergySnapshot computeEnergyDiff:]
+ -[CPUEnergySnapshot computeEnergyDiff:].cold.1
+ -[CPUEnergySnapshot cpuEnergyBilledToMe]
+ -[CPUEnergySnapshot cpuEnergyBilledToOthers]
+ -[CPUEnergySnapshot cpuEnergy]
+ -[CPUEnergySnapshot setCpuEnergy:]
+ -[CPUEnergySnapshot setCpuEnergyBilledToMe:]
+ -[CPUEnergySnapshot setCpuEnergyBilledToOthers:]
+ -[CPUEnergySnapshot setTime:]
+ -[CPUEnergySnapshot time]
+ -[CSDaemon _start].cold.1
+ -[CSDaemon _start].cold.2
+ -[CSDaemon _start].cold.3
+ -[CSDaemon displayStatusNotifyToken]
+ -[CSDaemon handleDisplayStateChanged:]
+ -[CSDaemon handleDisplayStateChanged:].cold.1
+ -[CSDaemon handleDisplayStateChanged:].cold.2
+ -[CSDaemon handlePowerStateChanged]
+ -[CSDaemon handlePowerStateChanged].cold.1
+ -[CSDaemon handlePowerStateChanged].cold.2
+ -[CSDaemon powerStatusNotifyToken]
+ -[CSDaemon setDisplayStatusNotifyToken:]
+ -[CSDaemon setPowerStatusNotifyToken:]
+ -[CSDetectionRule .cxx_destruct]
+ -[CSDetectionRule conditions]
+ -[CSDetectionRule daemonOnly]
+ -[CSDetectionRule description]
+ -[CSDetectionRule detectAcrossBoots]
+ -[CSDetectionRule initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:]
+ -[CSDetectionRule mainThresholdValue]
+ -[CSDetectionRule processesAllowList]
+ -[CSDetectionRule processesDenyList]
+ -[CSDetectionRule processesRegexAllowList]
+ -[CSDetectionRule processesRegexDenyList]
+ -[CSDetectionRule ruleID]
+ -[CSDetectionRule setConditions:]
+ -[CSDetectionRule setDaemonOnly:]
+ -[CSDetectionRule setDetectAcrossBoots:]
+ -[CSDetectionRule setMainThresholdValue:]
+ -[CSDetectionRule setProcessesAllowList:]
+ -[CSDetectionRule setProcessesDenyList:]
+ -[CSDetectionRule setProcessesRegexAllowList:]
+ -[CSDetectionRule setProcessesRegexDenyList:]
+ -[CSDetectionRule setRuleID:]
+ -[CSDetectionRule setSlidingWindowStepSize:]
+ -[CSDetectionRule setUseSlidingWindow:]
+ -[CSDetectionRule setWindowSize:]
+ -[CSDetectionRule slidingWindowStepSize]
+ -[CSDetectionRule useSlidingWindow]
+ -[CSDetectionRule windowSize]
+ -[CSDetectionRuleCondition comparator]
+ -[CSDetectionRuleCondition initWithScalarMetric:andNormalizerMetric:andComparator:andValue:]
+ -[CSDetectionRuleCondition normalizerMetric]
+ -[CSDetectionRuleCondition scalarMetric]
+ -[CSDetectionRuleCondition setComparator:]
+ -[CSDetectionRuleCondition setNormalizerMetric:]
+ -[CSDetectionRuleCondition setScalarMetric:]
+ -[CSDetectionRuleCondition setValue:]
+ -[CSDetectionRuleCondition value]
+ -[CSInterval .cxx_destruct]
+ -[CSInterval description]
+ -[CSInterval endTime]
+ -[CSInterval initWithStartTime:endTime:]
+ -[CSInterval initWithStartTime:endTime:value:]
+ -[CSInterval initWithStartTime:endTime:value:label:]
+ -[CSInterval label]
+ -[CSInterval setEndTime:]
+ -[CSInterval setLabel:]
+ -[CSInterval setStartTime:]
+ -[CSInterval setValue:]
+ -[CSInterval startTime]
+ -[CSInterval value]
+ -[CSIntervalList .cxx_destruct]
+ -[CSIntervalList addInterval:]
+ -[CSIntervalList count]
+ -[CSIntervalList durationInSeconds]
+ -[CSIntervalList firstInterval]
+ -[CSIntervalList initWithIntervals:]
+ -[CSIntervalList intersectWithIntervalList:]
+ -[CSIntervalList intervalArray]
+ -[CSIntervalList intervalAtIndex:]
+ -[CSIntervalList lastInterval]
+ -[CSIntervalList setIntervalArray:]
+ -[CSIntervalList sum]
+ -[CSIntervalList timeWeightedSum]
+ -[CSIssue .cxx_destruct]
+ -[CSIssue coalitionID]
+ -[CSIssue description]
+ -[CSIssue detectorString]
+ -[CSIssue endTime]
+ -[CSIssue errorString]
+ -[CSIssue forceMitigationSuggestion]
+ -[CSIssue identifier]
+ -[CSIssue initWithIdentifier:andLaunchdName:andIssueType:andStartTime:andEndTime:]
+ -[CSIssue initWithIdentifier:andProcessName:andIssueType:andStartTime:andEndTime:]
+ -[CSIssue issueType]
+ -[CSIssue lastPID]
+ -[CSIssue lastPUUID]
+ -[CSIssue launchdName]
+ -[CSIssue mitigationDecisionReason]
+ -[CSIssue mitigationDecisionType]
+ -[CSIssue mitigationSuggestionReason]
+ -[CSIssue mitigationSuggestion]
+ -[CSIssue overridden]
+ -[CSIssue processName]
+ -[CSIssue rule]
+ -[CSIssue setCoalitionID:]
+ -[CSIssue setDetectorString:]
+ -[CSIssue setEndTime:]
+ -[CSIssue setErrorString:]
+ -[CSIssue setForceMitigationSuggestion:]
+ -[CSIssue setIssueType:]
+ -[CSIssue setLastPID:]
+ -[CSIssue setLastPUUID:]
+ -[CSIssue setLaunchdName:]
+ -[CSIssue setMitigationDecisionReason:]
+ -[CSIssue setMitigationDecisionType:]
+ -[CSIssue setMitigationSuggestion:]
+ -[CSIssue setMitigationSuggestionReason:]
+ -[CSIssue setOverridden:]
+ -[CSIssue setProcessName:]
+ -[CSIssue setRule:]
+ -[CSIssue setStartTime:]
+ -[CSIssue setValue:]
+ -[CSIssue startTime]
+ -[CSIssue value]
+ -[CSIssueDetector .cxx_destruct]
+ -[CSIssueDetector _init]
+ -[CSIssueDetector clearFatalMitigatedProcessList]
+ -[CSIssueDetector compareWithValue1:andValue2:andComparator:]
+ -[CSIssueDetector dayChangedNotificationReceived:]
+ -[CSIssueDetector dayChangedNotificationReceived:].cold.1
+ -[CSIssueDetector detectIssuesFromStartTime:endDate:withRules:]
+ -[CSIssueDetector detectWithLookbackDuration:]
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:]
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.1
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.2
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.3
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.4
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.5
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.6
+ -[CSIssueDetector evaluateRuleInFixedWindow:withStartDate:andEndDate:].cold.7
+ -[CSIssueDetector evaluateRuleWithSlidingWindow:withStartDate:andEndDate:]
+ -[CSIssueDetector evaluateRuleWithSlidingWindow:withStartDate:andEndDate:].cold.1
+ -[CSIssueDetector fatalMitigatedProcessList]
+ -[CSIssueDetector forceDetectorViolationForProcess:withHandler:]
+ -[CSIssueDetector genericCPUDetectorProcessDenyList]
+ -[CSIssueDetector genericCPUDetectorProcessRegexDenyList]
+ -[CSIssueDetector getCPUIssueStartEndTime:valueThreshold:]
+ -[CSIssueDetector getCPUIssueWithMitigationSuggestionForCoalitionID:withLaunchdName:fromStartDate:toEndDate:byRule:]
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:]
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.1
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.2
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.3
+ -[CSIssueDetector handleDetectedIssues:]
+ -[CSIssueDetector handleDetectedIssues:].cold.1
+ -[CSIssueDetector logIssuesToPowerLogWithPayload:]
+ -[CSIssueDetector logIssuesToPowerLogWithPayload:].cold.1
+ -[CSIssueDetector logIssuesToPowerLogWithPayload:].cold.2
+ -[CSIssueDetector logger]
+ -[CSIssueDetector powerlogDBReader]
+ -[CSIssueDetector registerForDayChangedNotification]
+ -[CSIssueDetector rules]
+ -[CSIssueDetector setFatalMitigatedProcessList:]
+ -[CSIssueDetector setGenericCPUDetectorProcessDenyList:]
+ -[CSIssueDetector setGenericCPUDetectorProcessRegexDenyList:]
+ -[CSIssueDetector setLogger:]
+ -[CSIssueDetector setPowerlogDBReader:]
+ -[CSIssueDetector setRules:]
+ -[CSIssueDetector setTriggerTimer:]
+ -[CSIssueDetector string:matchesAnyRegexInArray:]
+ -[CSIssueDetector testDetectWithLookbackDuration]
+ -[CSIssueDetector testHandleDetectedIssues]
+ -[CSIssueDetector triggerTimer]
+ -[CSIssueDetector updateCPUBuffer:]
+ -[CSMitigationManager .cxx_destruct]
+ -[CSMitigationManager _init]
+ -[CSMitigationManager _init].cold.1
+ -[CSMitigationManager _init].cold.2
+ -[CSMitigationManager affectedProcesses]
+ -[CSMitigationManager checkForTrials]
+ -[CSMitigationManager checkForTrials].cold.1
+ -[CSMitigationManager checkForTrials].cold.2
+ -[CSMitigationManager checkKnownViolationByProcess:withStartTime:withEndTime:]
+ -[CSMitigationManager checkKnownViolationByProcess:withStartTime:withEndTime:].cold.1
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:]
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.1
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.2
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.3
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.4
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.5
+ -[CSMitigationManager checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:].cold.6
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration]
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.1
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.2
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.3
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.4
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.5
+ -[CSMitigationManager checkPenaltyBoxProcessesExpiration].cold.6
+ -[CSMitigationManager checkPenaltyBoxProcessesLifecycle:withMitigationReason:]
+ -[CSMitigationManager checkPenaltyBoxProcessesLifecycle:withMitigationReason:].cold.1
+ -[CSMitigationManager clearTargetProcessState]
+ -[CSMitigationManager dayChangedNotificationReceived:]
+ -[CSMitigationManager dayChangedNotificationReceived:].cold.1
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:]
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.1
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.10
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.11
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.2
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.3
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.4
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.5
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.6
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.7
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.8
+ -[CSMitigationManager decideMitigation:withCoalitionName:withReason:].cold.9
+ -[CSMitigationManager forceCPUViolationForProcess:withHandler:]
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:].cold.1
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:].cold.2
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:].cold.3
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:].cold.4
+ -[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:].cold.5
+ -[CSMitigationManager generateIPSFileForProcess:]
+ -[CSMitigationManager generateIPSFileForProcess:].cold.1
+ -[CSMitigationManager generateIPSFileForProcess:].cold.2
+ -[CSMitigationManager getMitigationTypeString:withStringSize:withMitigationType:withPenaltyBoxEndTime:]
+ -[CSMitigationManager getProcessPathForPID:]
+ -[CSMitigationManager getProcessPathForPID:].cold.1
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.1
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.2
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.2
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.3
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.4
+ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.5
+ -[CSMitigationManager handleDetectorViolation:]
+ -[CSMitigationManager handleDetectorViolation:].cold.1
+ -[CSMitigationManager handleDetectorViolation:].cold.2
+ -[CSMitigationManager handleProcessStart:withMitigationReason:]
+ -[CSMitigationManager handleProcessStart:withMitigationReason:].cold.1
+ -[CSMitigationManager handleProcessStart:withMitigationReason:].cold.2
+ -[CSMitigationManager handleProcessStart:withMitigationReason:].cold.3
+ -[CSMitigationManager killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:]
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.1
+ -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.2
+ -[CSMitigationManager logCPUViolationToPowerLogWithPayload:]
+ -[CSMitigationManager logCPUViolationToPowerLogWithPayload:].cold.1
+ -[CSMitigationManager logCPUViolationToPowerLogWithPayload:].cold.2
+ -[CSMitigationManager logMitigationAsSignpost:withPid:withIssueType:withMitigationType:withReason:withPenaltyBoxEndTime:]
+ -[CSMitigationManager logMitigationAsSignpost:withPid:withIssueType:withMitigationType:withReason:withPenaltyBoxEndTime:].cold.1
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:]
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:].cold.1
+ -[CSMitigationManager logPenaltyBoxListAsSignposts]
+ -[CSMitigationManager logPenaltyBoxListAsSignposts].cold.1
+ -[CSMitigationManager logPenaltyBoxListAsSignposts].cold.2
+ -[CSMitigationManager logger]
+ -[CSMitigationManager midnightRoutine]
+ -[CSMitigationManager penaltyBoxEnabled]
+ -[CSMitigationManager penaltyBoxPolicy]
+ -[CSMitigationManager penaltyBoxProcesses]
+ -[CSMitigationManager penaltyBoxTimerRunning]
+ -[CSMitigationManager penaltyBoxTimer]
+ -[CSMitigationManager policyMitigationsEnabled]
+ -[CSMitigationManager policyMitigationsEnabled].cold.1
+ -[CSMitigationManager policyMitigationsEnabled].cold.2
+ -[CSMitigationManager policyMitigationsEnabled].cold.3
+ -[CSMitigationManager policyMitigationsEnabled].cold.4
+ -[CSMitigationManager processManager]
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.2
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.3
+ -[CSMitigationManager putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.4
+ -[CSMitigationManager queue]
+ -[CSMitigationManager registerForDayChangedNotification]
+ -[CSMitigationManager removeAllProcessesFromPenaltyBox]
+ -[CSMitigationManager removeAllProcessesFromPenaltyBox].cold.1
+ -[CSMitigationManager removeProcessFromPenaltyBox:forReason:]
+ -[CSMitigationManager resetState]
+ -[CSMitigationManager setAffectedProcesses:]
+ -[CSMitigationManager setLogger:]
+ -[CSMitigationManager setPenaltyBoxEnabled:]
+ -[CSMitigationManager setPenaltyBoxPolicy:]
+ -[CSMitigationManager setPenaltyBoxProcesses:]
+ -[CSMitigationManager setPenaltyBoxTimer:]
+ -[CSMitigationManager setPenaltyBoxTimerRunning:]
+ -[CSMitigationManager setProcessManager:]
+ -[CSMitigationManager setQueue:]
+ -[CSMitigationManager setTrialsMitigationsEnabled:]
+ -[CSMitigationManager trialsMitigationsEnabled]
+ -[CSPowerlogDBReader .cxx_destruct]
+ -[CSPowerlogDBReader _init]
+ -[CSPowerlogDBReader closeConnection]
+ -[CSPowerlogDBReader conn]
+ -[CSPowerlogDBReader getAPWakeIntervalListWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader getAPWakeIntervalListWithStartDate:andEndDate:].cold.1
+ -[CSPowerlogDBReader getCPUPercentageIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:]
+ -[CSPowerlogDBReader getDeviceBootTime]
+ -[CSPowerlogDBReader getDeviceBootTime].cold.1
+ -[CSPowerlogDBReader getMonotonicTime:]
+ -[CSPowerlogDBReader getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:]
+ -[CSPowerlogDBReader getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:andCPURatio:]
+ -[CSPowerlogDBReader getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:andCPURatio:].cold.1
+ -[CSPowerlogDBReader getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:andCPURatio:].cold.2
+ -[CSPowerlogDBReader getSystemTime:]
+ -[CSPowerlogDBReader getTotalBatteryDrainWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader getTotalCPUTimeWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader getUnpluggedIntervalListWithStartDate:andEndDate:]
+ -[CSPowerlogDBReader logger]
+ -[CSPowerlogDBReader openConnection]
+ -[CSPowerlogDBReader performPowerlogQuery:]
+ -[CSPowerlogDBReader setConn:]
+ -[CSPowerlogDBReader setLogger:]
+ -[CSProcess addMitigationEvent:startTime:]
+ -[CSProcess addNewTrackedPID:]
+ -[CSProcess addNewTrackedPID:].cold.1
+ -[CSProcess addPenaltyBoxCoalitionID:]
+ -[CSProcess addViolationEvent:startTime:endTime:]
+ -[CSProcess band80Mitigations]
+ -[CSProcess band95Mitigations]
+ -[CSProcess checkKnownViolationStartTime:endTime:]
+ -[CSProcess computeEnergyDiff:]
+ -[CSProcess cpuFatalCnt]
+ -[CSProcess cpuMonitored]
+ -[CSProcess cpuNonFatalCnt]
+ -[CSProcess energySnapshotNew]
+ -[CSProcess energySnapshot]
+ -[CSProcess estimatedEnergyDiff]
+ -[CSProcess eventHistory]
+ -[CSProcess exitMonitors]
+ -[CSProcess exitsCnt]
+ -[CSProcess getPidsForCoalitionID:]
+ -[CSProcess inPenaltyBox]
+ -[CSProcess lastCoalitionID]
+ -[CSProcess lastPid]
+ -[CSProcess monitorForExitWithPID:]
+ -[CSProcess monitorForExitWithPID:].cold.1
+ -[CSProcess monitorForExitWithPID:].cold.2
+ -[CSProcess penaltyBoxCnt]
+ -[CSProcess penaltyBoxCoalitionIDs]
+ -[CSProcess penaltyBoxDurationMins]
+ -[CSProcess penaltyBoxEndTime]
+ -[CSProcess penaltyBoxPending]
+ -[CSProcess performCleanupOnExitOnPID:]
+ -[CSProcess previousPIDkeys]
+ -[CSProcess previousPIDs]
+ -[CSProcess processName]
+ -[CSProcess removeTrackedPID:]
+ -[CSProcess removeTrackedPID:].cold.1
+ -[CSProcess rootDaemon]
+ -[CSProcess setBand80Mitigations:]
+ -[CSProcess setBand95Mitigations:]
+ -[CSProcess setCpuFatalCnt:]
+ -[CSProcess setCpuMonitored:]
+ -[CSProcess setCpuNonFatalCnt:]
+ -[CSProcess setEnergySnapshot:]
+ -[CSProcess setEnergySnapshotNew:]
+ -[CSProcess setEstimatedEnergyDiff:]
+ -[CSProcess setEventHistory:]
+ -[CSProcess setExitMonitors:]
+ -[CSProcess setExitsCnt:]
+ -[CSProcess setInPenaltyBox:]
+ -[CSProcess setPenaltyBoxCnt:]
+ -[CSProcess setPenaltyBoxCoalitionIDs:]
+ -[CSProcess setPenaltyBoxDurationMins:]
+ -[CSProcess setPenaltyBoxEndTime:]
+ -[CSProcess setPenaltyBoxPending:]
+ -[CSProcess setPreviousPIDkeys:]
+ -[CSProcess setPreviousPIDs:]
+ -[CSProcess setProcessName:]
+ -[CSProcess setRootDaemon:]
+ -[CSProcess setTrackedPIDkeys:]
+ -[CSProcess setTrackedPIDs:]
+ -[CSProcess setUuid:]
+ -[CSProcess setViolationDetectorString:]
+ -[CSProcess setViolationEndTime:]
+ -[CSProcess setViolationLimitValue:]
+ -[CSProcess setViolationLimitWindow:]
+ -[CSProcess setViolationObservationWindow:]
+ -[CSProcess setViolationObservedValue:]
+ -[CSProcess setViolationPath:]
+ -[CSProcess setViolationPid:]
+ -[CSProcess setXpcService:]
+ -[CSProcess snapshotCPUEnergy]
+ -[CSProcess trackedPIDkeys]
+ -[CSProcess trackedPIDs]
+ -[CSProcess uuid]
+ -[CSProcess violationDetectorString]
+ -[CSProcess violationEndTime]
+ -[CSProcess violationLimitValue]
+ -[CSProcess violationLimitWindow]
+ -[CSProcess violationObservationWindow]
+ -[CSProcess violationObservedValue]
+ -[CSProcess violationPath]
+ -[CSProcess violationPid]
+ -[CSProcess xpcService]
+ -[CSProcessManager _initWithEnrolledProcesses:andExemptions:andBand95:andBand80:]
+ -[CSProcessManager band80ProcessesSet]
+ -[CSProcessManager band95ProcessesSet]
+ -[CSProcessManager clearAllCounters]
+ -[CSProcessManager clearTargetProcessState]
+ -[CSProcessManager discoverPidForProcessName:withError:]
+ -[CSProcessManager discoverPidForProcessName:withError:].cold.1
+ -[CSProcessManager discoverPidForProcessName:withError:].cold.2
+ -[CSProcessManager discoverPidForProcessName:withError:].cold.3
+ -[CSProcessManager getMonitoredList]
+ -[CSProcessManager getProcessForProcessName:]
+ -[CSProcessManager getProcessForUUID:]
+ -[CSProcessManager isAppleXPCServiceWithRBS:andPID:]
+ -[CSProcessManager isAppleXPCServiceWithRBS:andPID:].cold.1
+ -[CSProcessManager isXPCServiceExempt:]
+ -[CSProcessManager monitorFilterBitMap]
+ -[CSProcessManager pausePIDPolling]
+ -[CSProcessManager pausePIDPolling].cold.1
+ -[CSProcessManager pollPIDs].cold.2
+ -[CSProcessManager pollPIDs].cold.3
+ -[CSProcessManager pollingTimerActive]
+ -[CSProcessManager pollingTimer]
+ -[CSProcessManager processNameForIdentifier:]
+ -[CSProcessManager resumePIDPolling]
+ -[CSProcessManager resumePIDPolling].cold.1
+ -[CSProcessManager savedPIDPollingInterval]
+ -[CSProcessManager setBand80ProcessesSet:]
+ -[CSProcessManager setBand95ProcessesSet:]
+ -[CSProcessManager setMonitorFilterBitMap:]
+ -[CSProcessManager setPollingTimer:]
+ -[CSProcessManager setPollingTimerActive:]
+ -[CSProcessManager setSavedPIDPollingInterval:]
+ -[CSRestrictionDataProvider _bandRestrictionsSetForThreshold:withErrors:]
+ -[CSRestrictionDataProvider _bandRestrictionsSetForThreshold:withErrors:].cold.1
+ -[CSRestrictionDataProvider _bandRestrictionsSetForThreshold:withErrors:].cold.2
+ -[CSRestrictionDataProvider _bandRestrictionsSetForThreshold:withErrors:].cold.3
+ -[CSRestrictionDataProvider _bandRestrictionsSetForThreshold:withErrors:].cold.4
+ -[CSRestrictionDataProvider _templatesByProcessWithErrors:].cold.4
+ -[CSRestrictionDataProvider _templatesByProcessWithErrors:].cold.5
+ -[CSRestrictionDataProvider band80ProcessesSet]
+ -[CSRestrictionDataProvider band80Processes]
+ -[CSRestrictionDataProvider band95ProcessesSet]
+ -[CSRestrictionDataProvider band95Processes]
+ -[CSRestrictionDataProvider setBand80Processes:]
+ -[CSRestrictionDataProvider setBand95Processes:]
+ -[CSRestrictionManager applyPluggedInRestrictionsToProcess:]
+ -[CSRestrictionManager applyPluggedInRestrictionsToProcess:].cold.1
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:]
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.1
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.2
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.3
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.4
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.5
+ -[CSRestrictionManager applyRestriction:withProcessIdentifier:].cold.6
+ -[CSRestrictionManager band80Restriction]
+ -[CSRestrictionManager band95Restriction]
+ -[CSRestrictionManager checkScheduledIntensiveInNewProcesses:]
+ -[CSRestrictionManager checkScheduledIntensiveInNewProcesses:].cold.1
+ -[CSRestrictionManager clearTargetProcess]
+ -[CSRestrictionManager forceCPUViolationForProcess:withHandler:]
+ -[CSRestrictionManager forceCPUViolationForProcess:withHandler:].cold.1
+ -[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:]
+ -[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:].cold.1
+ -[CSRestrictionManager forceDetectorViolationForProcess:withHandler:]
+ -[CSRestrictionManager forceDetectorViolationForProcess:withHandler:].cold.1
+ -[CSRestrictionManager forceMidnightRoutineWithHandler:]
+ -[CSRestrictionManager forceMidnightRoutineWithHandler:].cold.1
+ -[CSRestrictionManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]
+ -[CSRestrictionManager getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:]
+ -[CSRestrictionManager getDefaultsWithHandler:]
+ -[CSRestrictionManager getInfoForProcess:]
+ -[CSRestrictionManager getInfoForProcess:].cold.1
+ -[CSRestrictionManager getInfoForProcess:withHandler:]
+ -[CSRestrictionManager getInfoForProcess:withHandler:].cold.1
+ -[CSRestrictionManager getMitigationPolicyWithHandler:]
+ -[CSRestrictionManager getMitigationPolicyWithHandler:].cold.1
+ -[CSRestrictionManager getMonitoredListWithHandler:]
+ -[CSRestrictionManager getMonitoredListWithHandler:].cold.1
+ -[CSRestrictionManager getPenaltyListWithHandler:]
+ -[CSRestrictionManager getPenaltyListWithHandler:].cold.1
+ -[CSRestrictionManager getTriggerIntervalWithHandler:]
+ -[CSRestrictionManager issueDetector]
+ -[CSRestrictionManager mitigationManager]
+ -[CSRestrictionManager modifyContextForIdentifier:withState:]
+ -[CSRestrictionManager modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:]
+ -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]
+ -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:].cold.1
+ -[CSRestrictionManager modifyRestrictionsByProcessPerScenario:withHandler:]
+ -[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:]
+ -[CSRestrictionManager modifyTriggerInterval:]
+ -[CSRestrictionManager scheduledIntensiveProcesses]
+ -[CSRestrictionManager setBand80Restriction:]
+ -[CSRestrictionManager setBand95Restriction:]
+ -[CSRestrictionManager setIssueDetector:]
+ -[CSRestrictionManager setMitigationManager:]
+ -[CSRestrictionManager setScheduledIntensiveProcesses:]
+ -[CSRestrictionManager setTriggerManager:]
+ -[CSRestrictionManager setUnknownScheduledIntensiveProcesses:]
+ -[CSRestrictionManager triggerManager]
+ -[CSRestrictionManager unknownScheduledIntensiveProcesses]
+ -[CSRestrictionManager updateCoalitionEntries:withHandler:]
+ -[CSRestrictionManager updateScheduledIntensiveContext:]
+ -[CSRestrictionManager updateScheduledIntensiveContext:].cold.1
+ -[CSTriggerManager .cxx_destruct]
+ -[CSTriggerManager _init]
+ -[CSTriggerManager _start]
+ -[CSTriggerManager checkCpuPercentageAndInvokeIssueDetection:windowStartDate:]
+ -[CSTriggerManager checkDrainAndInvokeIssueDetection:]
+ -[CSTriggerManager cpuPercentageTriggerForWindowEndDate:windowStartDate:score:]
+ -[CSTriggerManager detectAndInvokeIssueDetection:slidingWindowStartDate:]
+ -[CSTriggerManager generateMetadataForDrain:cpuPercentage:detectionLookbackDuration:]
+ -[CSTriggerManager generatePayloadWithMetadata:triggeredDetection:triggeredType:]
+ -[CSTriggerManager getDetectionLookbackDuration]
+ -[CSTriggerManager getDrainPercentage:]
+ -[CSTriggerManager getTriggerInterval]
+ -[CSTriggerManager issueDetector]
+ -[CSTriggerManager lastTriggerTimerDate]
+ -[CSTriggerManager logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:]
+ -[CSTriggerManager logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:].cold.1
+ -[CSTriggerManager logger]
+ -[CSTriggerManager modifyTriggerInterval:]
+ -[CSTriggerManager powerlogDBReader]
+ -[CSTriggerManager processTimerFiredAction]
+ -[CSTriggerManager savedTriggerInterval]
+ -[CSTriggerManager setIssueDetector:]
+ -[CSTriggerManager setLastTriggerTimerDate:]
+ -[CSTriggerManager setLogger:]
+ -[CSTriggerManager setPowerlogDBReader:]
+ -[CSTriggerManager setSavedTriggerInterval:]
+ -[CSTriggerManager setTriggerInterval:]
+ -[CSTriggerManager setTriggerTimer:]
+ -[CSTriggerManager triggerInterval]
+ -[CSTriggerManager triggerTimer]
+ GCC_except_table13
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table63
+ GCC_except_table67
+ _CFPreferencesCopyValue
+ _IOPSDrawingUnlimitedPower
+ _NSCalendarDayChangedNotification
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_CPUEnergySnapshot
+ _OBJC_CLASS_$_CSDetectionRule
+ _OBJC_CLASS_$_CSDetectionRuleCondition
+ _OBJC_CLASS_$_CSInterval
+ _OBJC_CLASS_$_CSIntervalList
+ _OBJC_CLASS_$_CSIssue
+ _OBJC_CLASS_$_CSIssueDetector
+ _OBJC_CLASS_$_CSMitigationManager
+ _OBJC_CLASS_$_CSPowerlogDBReader
+ _OBJC_CLASS_$_CSTriggerManager
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_PLSQLiteConnection
+ _OBJC_CLASS_$_PLUtilities
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_IVAR_$_CPUEnergySnapshot._cpuEnergy
+ _OBJC_IVAR_$_CPUEnergySnapshot._cpuEnergyBilledToMe
+ _OBJC_IVAR_$_CPUEnergySnapshot._cpuEnergyBilledToOthers
+ _OBJC_IVAR_$_CPUEnergySnapshot._time
+ _OBJC_IVAR_$_CSDaemon._displayStatusNotifyToken
+ _OBJC_IVAR_$_CSDaemon._powerStatusNotifyToken
+ _OBJC_IVAR_$_CSDetectionRule._conditions
+ _OBJC_IVAR_$_CSDetectionRule._daemonOnly
+ _OBJC_IVAR_$_CSDetectionRule._detectAcrossBoots
+ _OBJC_IVAR_$_CSDetectionRule._mainThresholdValue
+ _OBJC_IVAR_$_CSDetectionRule._processesAllowList
+ _OBJC_IVAR_$_CSDetectionRule._processesDenyList
+ _OBJC_IVAR_$_CSDetectionRule._processesRegexAllowList
+ _OBJC_IVAR_$_CSDetectionRule._processesRegexDenyList
+ _OBJC_IVAR_$_CSDetectionRule._ruleID
+ _OBJC_IVAR_$_CSDetectionRule._slidingWindowStepSize
+ _OBJC_IVAR_$_CSDetectionRule._useSlidingWindow
+ _OBJC_IVAR_$_CSDetectionRule._windowSize
+ _OBJC_IVAR_$_CSDetectionRuleCondition._comparator
+ _OBJC_IVAR_$_CSDetectionRuleCondition._normalizerMetric
+ _OBJC_IVAR_$_CSDetectionRuleCondition._scalarMetric
+ _OBJC_IVAR_$_CSDetectionRuleCondition._value
+ _OBJC_IVAR_$_CSInterval._endTime
+ _OBJC_IVAR_$_CSInterval._label
+ _OBJC_IVAR_$_CSInterval._startTime
+ _OBJC_IVAR_$_CSInterval._value
+ _OBJC_IVAR_$_CSIntervalList._intervalArray
+ _OBJC_IVAR_$_CSIssue._coalitionID
+ _OBJC_IVAR_$_CSIssue._detectorString
+ _OBJC_IVAR_$_CSIssue._endTime
+ _OBJC_IVAR_$_CSIssue._errorString
+ _OBJC_IVAR_$_CSIssue._forceMitigationSuggestion
+ _OBJC_IVAR_$_CSIssue._identifier
+ _OBJC_IVAR_$_CSIssue._issueType
+ _OBJC_IVAR_$_CSIssue._lastPID
+ _OBJC_IVAR_$_CSIssue._lastPUUID
+ _OBJC_IVAR_$_CSIssue._launchdName
+ _OBJC_IVAR_$_CSIssue._mitigationDecisionReason
+ _OBJC_IVAR_$_CSIssue._mitigationDecisionType
+ _OBJC_IVAR_$_CSIssue._mitigationSuggestion
+ _OBJC_IVAR_$_CSIssue._mitigationSuggestionReason
+ _OBJC_IVAR_$_CSIssue._overridden
+ _OBJC_IVAR_$_CSIssue._processName
+ _OBJC_IVAR_$_CSIssue._rule
+ _OBJC_IVAR_$_CSIssue._startTime
+ _OBJC_IVAR_$_CSIssue._value
+ _OBJC_IVAR_$_CSIssueDetector._fatalMitigatedProcessList
+ _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessDenyList
+ _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessRegexDenyList
+ _OBJC_IVAR_$_CSIssueDetector._logger
+ _OBJC_IVAR_$_CSIssueDetector._powerlogDBReader
+ _OBJC_IVAR_$_CSIssueDetector._rules
+ _OBJC_IVAR_$_CSIssueDetector._triggerTimer
+ _OBJC_IVAR_$_CSMitigationManager._affectedProcesses
+ _OBJC_IVAR_$_CSMitigationManager._logger
+ _OBJC_IVAR_$_CSMitigationManager._penaltyBoxEnabled
+ _OBJC_IVAR_$_CSMitigationManager._penaltyBoxPolicy
+ _OBJC_IVAR_$_CSMitigationManager._penaltyBoxProcesses
+ _OBJC_IVAR_$_CSMitigationManager._penaltyBoxTimer
+ _OBJC_IVAR_$_CSMitigationManager._penaltyBoxTimerRunning
+ _OBJC_IVAR_$_CSMitigationManager._processManager
+ _OBJC_IVAR_$_CSMitigationManager._queue
+ _OBJC_IVAR_$_CSMitigationManager._trialsMitigationsEnabled
+ _OBJC_IVAR_$_CSPowerlogDBReader._conn
+ _OBJC_IVAR_$_CSPowerlogDBReader._logger
+ _OBJC_IVAR_$_CSProcess._band80Mitigations
+ _OBJC_IVAR_$_CSProcess._band95Mitigations
+ _OBJC_IVAR_$_CSProcess._cpuFatalCnt
+ _OBJC_IVAR_$_CSProcess._cpuMonitored
+ _OBJC_IVAR_$_CSProcess._cpuNonFatalCnt
+ _OBJC_IVAR_$_CSProcess._energySnapshot
+ _OBJC_IVAR_$_CSProcess._energySnapshotNew
+ _OBJC_IVAR_$_CSProcess._estimatedEnergyDiff
+ _OBJC_IVAR_$_CSProcess._eventHistory
+ _OBJC_IVAR_$_CSProcess._exitMonitors
+ _OBJC_IVAR_$_CSProcess._exitsCnt
+ _OBJC_IVAR_$_CSProcess._inPenaltyBox
+ _OBJC_IVAR_$_CSProcess._penaltyBoxCnt
+ _OBJC_IVAR_$_CSProcess._penaltyBoxCoalitionIDs
+ _OBJC_IVAR_$_CSProcess._penaltyBoxDurationMins
+ _OBJC_IVAR_$_CSProcess._penaltyBoxEndTime
+ _OBJC_IVAR_$_CSProcess._penaltyBoxPending
+ _OBJC_IVAR_$_CSProcess._previousPIDkeys
+ _OBJC_IVAR_$_CSProcess._previousPIDs
+ _OBJC_IVAR_$_CSProcess._processName
+ _OBJC_IVAR_$_CSProcess._rootDaemon
+ _OBJC_IVAR_$_CSProcess._trackedPIDkeys
+ _OBJC_IVAR_$_CSProcess._trackedPIDs
+ _OBJC_IVAR_$_CSProcess._uuid
+ _OBJC_IVAR_$_CSProcess._violationDetectorString
+ _OBJC_IVAR_$_CSProcess._violationEndTime
+ _OBJC_IVAR_$_CSProcess._violationLimitValue
+ _OBJC_IVAR_$_CSProcess._violationLimitWindow
+ _OBJC_IVAR_$_CSProcess._violationObservationWindow
+ _OBJC_IVAR_$_CSProcess._violationObservedValue
+ _OBJC_IVAR_$_CSProcess._violationPath
+ _OBJC_IVAR_$_CSProcess._violationPid
+ _OBJC_IVAR_$_CSProcess._xpcService
+ _OBJC_IVAR_$_CSProcessManager._band80ProcessesSet
+ _OBJC_IVAR_$_CSProcessManager._band95ProcessesSet
+ _OBJC_IVAR_$_CSProcessManager._monitorFilterBitMap
+ _OBJC_IVAR_$_CSProcessManager._pollingTimer
+ _OBJC_IVAR_$_CSProcessManager._pollingTimerActive
+ _OBJC_IVAR_$_CSProcessManager._savedPIDPollingInterval
+ _OBJC_IVAR_$_CSRestrictionDataProvider._band80Processes
+ _OBJC_IVAR_$_CSRestrictionDataProvider._band95Processes
+ _OBJC_IVAR_$_CSRestrictionManager._band80Restriction
+ _OBJC_IVAR_$_CSRestrictionManager._band95Restriction
+ _OBJC_IVAR_$_CSRestrictionManager._issueDetector
+ _OBJC_IVAR_$_CSRestrictionManager._mitigationManager
+ _OBJC_IVAR_$_CSRestrictionManager._scheduledIntensiveProcesses
+ _OBJC_IVAR_$_CSRestrictionManager._triggerManager
+ _OBJC_IVAR_$_CSRestrictionManager._unknownScheduledIntensiveProcesses
+ _OBJC_IVAR_$_CSTriggerManager._issueDetector
+ _OBJC_IVAR_$_CSTriggerManager._lastTriggerTimerDate
+ _OBJC_IVAR_$_CSTriggerManager._logger
+ _OBJC_IVAR_$_CSTriggerManager._powerlogDBReader
+ _OBJC_IVAR_$_CSTriggerManager._savedTriggerInterval
+ _OBJC_IVAR_$_CSTriggerManager._triggerInterval
+ _OBJC_IVAR_$_CSTriggerManager._triggerTimer
+ _OBJC_METACLASS_$_CPUEnergySnapshot
+ _OBJC_METACLASS_$_CSDetectionRule
+ _OBJC_METACLASS_$_CSDetectionRuleCondition
+ _OBJC_METACLASS_$_CSInterval
+ _OBJC_METACLASS_$_CSIntervalList
+ _OBJC_METACLASS_$_CSIssue
+ _OBJC_METACLASS_$_CSIssueDetector
+ _OBJC_METACLASS_$_CSMitigationManager
+ _OBJC_METACLASS_$_CSPowerlogDBReader
+ _OBJC_METACLASS_$_CSTriggerManager
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ _PEIssueTypeString
+ _PEMitigationTypeString
+ _PEReasonString
+ _PESuggestionReasonString
+ _PLQueryRegistered
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ _SPReportPowerException
+ __OBJC_$_CLASS_METHODS_CPUEnergySnapshot
+ __OBJC_$_CLASS_METHODS_CSIssueDetector
+ __OBJC_$_CLASS_METHODS_CSMitigationManager
+ __OBJC_$_CLASS_METHODS_CSPowerlogDBReader
+ __OBJC_$_CLASS_METHODS_CSTriggerManager
+ __OBJC_$_INSTANCE_METHODS_CPUEnergySnapshot
+ __OBJC_$_INSTANCE_METHODS_CSDetectionRule
+ __OBJC_$_INSTANCE_METHODS_CSDetectionRuleCondition
+ __OBJC_$_INSTANCE_METHODS_CSInterval
+ __OBJC_$_INSTANCE_METHODS_CSIntervalList
+ __OBJC_$_INSTANCE_METHODS_CSIssue
+ __OBJC_$_INSTANCE_METHODS_CSIssueDetector
+ __OBJC_$_INSTANCE_METHODS_CSMitigationManager
+ __OBJC_$_INSTANCE_METHODS_CSPowerlogDBReader
+ __OBJC_$_INSTANCE_METHODS_CSTriggerManager
+ __OBJC_$_INSTANCE_VARIABLES_CPUEnergySnapshot
+ __OBJC_$_INSTANCE_VARIABLES_CSDetectionRule
+ __OBJC_$_INSTANCE_VARIABLES_CSDetectionRuleCondition
+ __OBJC_$_INSTANCE_VARIABLES_CSInterval
+ __OBJC_$_INSTANCE_VARIABLES_CSIntervalList
+ __OBJC_$_INSTANCE_VARIABLES_CSIssue
+ __OBJC_$_INSTANCE_VARIABLES_CSIssueDetector
+ __OBJC_$_INSTANCE_VARIABLES_CSMitigationManager
+ __OBJC_$_INSTANCE_VARIABLES_CSPowerlogDBReader
+ __OBJC_$_INSTANCE_VARIABLES_CSTriggerManager
+ __OBJC_$_PROP_LIST_CPUEnergySnapshot
+ __OBJC_$_PROP_LIST_CSDetectionRule
+ __OBJC_$_PROP_LIST_CSDetectionRuleCondition
+ __OBJC_$_PROP_LIST_CSInterval
+ __OBJC_$_PROP_LIST_CSIntervalList
+ __OBJC_$_PROP_LIST_CSIssue
+ __OBJC_$_PROP_LIST_CSIssueDetector
+ __OBJC_$_PROP_LIST_CSMitigationManager
+ __OBJC_$_PROP_LIST_CSPowerlogDBReader
+ __OBJC_$_PROP_LIST_CSTriggerManager
+ __OBJC_CLASS_RO_$_CPUEnergySnapshot
+ __OBJC_CLASS_RO_$_CSDetectionRule
+ __OBJC_CLASS_RO_$_CSDetectionRuleCondition
+ __OBJC_CLASS_RO_$_CSInterval
+ __OBJC_CLASS_RO_$_CSIntervalList
+ __OBJC_CLASS_RO_$_CSIssue
+ __OBJC_CLASS_RO_$_CSIssueDetector
+ __OBJC_CLASS_RO_$_CSMitigationManager
+ __OBJC_CLASS_RO_$_CSPowerlogDBReader
+ __OBJC_CLASS_RO_$_CSTriggerManager
+ __OBJC_METACLASS_RO_$_CPUEnergySnapshot
+ __OBJC_METACLASS_RO_$_CSDetectionRule
+ __OBJC_METACLASS_RO_$_CSDetectionRuleCondition
+ __OBJC_METACLASS_RO_$_CSInterval
+ __OBJC_METACLASS_RO_$_CSIntervalList
+ __OBJC_METACLASS_RO_$_CSIssue
+ __OBJC_METACLASS_RO_$_CSIssueDetector
+ __OBJC_METACLASS_RO_$_CSMitigationManager
+ __OBJC_METACLASS_RO_$_CSPowerlogDBReader
+ __OBJC_METACLASS_RO_$_CSTriggerManager
+ ___109-[CSTriggerManager logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:]_block_invoke
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.166
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.179
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.180
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.181
+ ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke
+ ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke.307
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.1
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.2
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.3
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.4
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.5
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.6
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.7
+ ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.8
+ ___18-[CSDaemon _start]_block_invoke.5
+ ___18-[CSDaemon _start]_block_invoke.6
+ ___18-[CSDaemon _start]_block_invoke.6.cold.1
+ ___209-[CSRestrictionManager modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:]_block_invoke
+ ___23+[CSTriggerManager run]_block_invoke
+ ___26-[CSTriggerManager _start]_block_invoke
+ ___28-[CSMitigationManager _init]_block_invoke
+ ___28-[CSMitigationManager _init]_block_invoke_2
+ ___33+[CSIssueDetector sharedInstance]_block_invoke
+ ___34+[CSTriggerManager sharedInstance]_block_invoke
+ ___36+[CSPowerlogDBReader sharedInstance]_block_invoke
+ ___37+[CSMitigationManager sharedInstance]_block_invoke
+ ___38-[CSTriggerManager getTriggerInterval]_block_invoke
+ ___39-[CSPowerlogDBReader getDeviceBootTime]_block_invoke
+ ___40-[CSIssueDetector handleDetectedIssues:]_block_invoke
+ ___42-[CSRestrictionManager clearTargetProcess]_block_invoke
+ ___42-[CSTriggerManager modifyTriggerInterval:]_block_invoke
+ ___46-[CSRestrictionManager modifyPollingInterval:]_block_invoke
+ ___47-[CSRestrictionManager getDefaultsWithHandler:]_block_invoke
+ ___49-[CSIssueDetector clearFatalMitigatedProcessList]_block_invoke
+ ___49-[CSIssueDetector clearFatalMitigatedProcessList]_block_invoke.cold.1
+ ___50-[CSIssueDetector dayChangedNotificationReceived:]_block_invoke
+ ___50-[CSIssueDetector logIssuesToPowerLogWithPayload:]_block_invoke
+ ___50-[CSRestrictionManager getPenaltyListWithHandler:]_block_invoke
+ ___50-[CSRestrictionManager getPenaltyListWithHandler:]_block_invoke.cold.1
+ ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke
+ ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.305
+ ___54-[CSMitigationManager dayChangedNotificationReceived:]_block_invoke
+ ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke
+ ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.277
+ ___55-[CSRestrictionManager getMitigationPolicyWithHandler:]_block_invoke
+ ___56-[CSRestrictionManager forceMidnightRoutineWithHandler:]_block_invoke
+ ___60-[CSMitigationManager logCPUViolationToPowerLogWithPayload:]_block_invoke
+ ___63-[CSIssueDetector detectIssuesFromStartTime:endDate:withRules:]_block_invoke
+ ___63-[CSMitigationManager forceCPUViolationForProcess:withHandler:]_block_invoke
+ ___63-[CSMitigationManager forceCPUViolationForProcess:withHandler:]_block_invoke.cold.1
+ ___63-[CSMitigationManager forceCPUViolationForProcess:withHandler:]_block_invoke.cold.2
+ ___63-[CSMitigationManager forceCPUViolationForProcess:withHandler:]_block_invoke.cold.3
+ ___63-[CSMitigationManager handleProcessStart:withMitigationReason:]_block_invoke
+ ___64-[CSIssueDetector forceDetectorViolationForProcess:withHandler:]_block_invoke
+ ___64-[CSIssueDetector forceDetectorViolationForProcess:withHandler:]_block_invoke.cold.1
+ ___64-[CSIssueDetector forceDetectorViolationForProcess:withHandler:]_block_invoke.cold.2
+ ___64-[CSRestrictionManager reportScheduledIntensiveWorkByProcesses:]_block_invoke
+ ___72-[CSRestrictionManager forceDetectionWithStartTime:endTime:withHandler:]_block_invoke
+ ___75-[CSRestrictionManager modifyRestrictionsByProcessPerScenario:withHandler:]_block_invoke
+ ___78-[CSRestrictionManager queueChangeForActivatedScenarios:deactivatedScenarios:]_block_invoke.cold.5
+ ___78-[CSRestrictionManager queueChangeForActivatedScenarios:deactivatedScenarios:]_block_invoke.cold.6
+ ___88-[CSRestrictionManager getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:]_block_invoke
+ ___90+[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:]_block_invoke
+ ___94-[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_104_e8_32r40r48r56r64r72r80r88r96r_e5_v8?0lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_105_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e5_v8?0lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e29_q24?0"CSIssue"8"CSIssue"16l
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_90_e8_32s40s48s56s64bs72r80r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
+ ___block_literal_global.141
+ ___block_literal_global.142
+ ___block_literal_global.15
+ ___block_literal_global.157
+ ___block_literal_global.17
+ ___block_literal_global.19
+ ___block_literal_global.2
+ ___block_literal_global.78
+ ___block_literal_global.85
+ ___getDateFormatter_block_invoke
+ __dispatch_main_q
+ __os_signpost_emit_with_name_impl
+ _clock_get_time
+ _coalition_info_resource_usage
+ _convertXPCServiceName
+ _dispatch_assert_queue$V2
+ _dispatch_walltime
+ _gEnableMitigations
+ _gEnablePenaltyBox
+ _gGlobalOverrideCPUPercentage
+ _gGlobalOverrideCPUTimeWindow
+ _gGlobalOverridePenaltyBoxDurationMins
+ _gMaxNumberOfKills
+ _gMaxNumberOfNonfatal
+ _gMitigateXPCServices
+ _gMitigationsWhilePluggedIn
+ _gTargetCPUPercentage
+ _gTargetCPUTimeWindow
+ _gTargetPenaltyBoxDurationMins
+ _gTargetProcess
+ _getCSBandsRestrictions
+ _getCoalitionID
+ _getCoalitionID.cold.1
+ _getCurrentTime
+ _getDateFormatter
+ _getDateFormatter.cold.1
+ _getDateFormatter.formatter
+ _getDateFormatter.onceToken
+ _getDeviceBootTime.bootTime
+ _getDeviceBootTime.onceToken
+ _getProcessUUID
+ _getProcessUUID.cold.1
+ _getpriority
+ _host_get_clock_service
+ _kCFPreferencesCurrentHost
+ _logIssuesToPowerLogWithPayload:.onceToken
+ _logIssuesToPowerLogWithPayload:.streamID
+ _logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:.onceToken
+ _logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:.streamID
+ _mach_host_self
+ _mobileUserADG
+ _notify_get_state
+ _notify_post
+ _notify_register_dispatch
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_copyStruct
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_bandRestrictionsSetForThreshold:withErrors:
+ _objc_msgSend$_initWithEnrolledProcesses:andExemptions:andBand95:andBand80:
+ _objc_msgSend$addInterval:
+ _objc_msgSend$addMitigationEvent:startTime:
+ _objc_msgSend$addNewTrackedPID:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addPenaltyBoxCoalitionID:
+ _objc_msgSend$addViolationEvent:startTime:endTime:
+ _objc_msgSend$allKeysForObject:
+ _objc_msgSend$applyPluggedInRestrictionsToProcess:
+ _objc_msgSend$applyRestriction:withProcessIdentifier:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$band80Mitigations
+ _objc_msgSend$band80ProcessesSet
+ _objc_msgSend$band95Mitigations
+ _objc_msgSend$band95ProcessesSet
+ _objc_msgSend$booleanValue
+ _objc_msgSend$bundle
+ _objc_msgSend$checkCpuPercentageAndInvokeIssueDetection:windowStartDate:
+ _objc_msgSend$checkForTrials
+ _objc_msgSend$checkKnownViolationByProcess:withStartTime:withEndTime:
+ _objc_msgSend$checkKnownViolationStartTime:endTime:
+ _objc_msgSend$checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:
+ _objc_msgSend$checkPenaltyBoxProcessesExpiration
+ _objc_msgSend$checkPenaltyBoxProcessesLifecycle:withMitigationReason:
+ _objc_msgSend$checkScheduledIntensiveInNewProcesses:
+ _objc_msgSend$clearAllCounters
+ _objc_msgSend$clearFatalMitigatedProcessList
+ _objc_msgSend$clearTargetProcessState
+ _objc_msgSend$clientWithIdentifier:
+ _objc_msgSend$closeConnection
+ _objc_msgSend$coalitionID
+ _objc_msgSend$comparator
+ _objc_msgSend$compare:
+ _objc_msgSend$compareWithValue1:andValue2:andComparator:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$computeEnergyDiff:
+ _objc_msgSend$conditions
+ _objc_msgSend$containerPath
+ _objc_msgSend$cpuEnergy
+ _objc_msgSend$cpuEnergyBilledToMe
+ _objc_msgSend$cpuEnergyBilledToOthers
+ _objc_msgSend$cpuFatalCnt
+ _objc_msgSend$cpuMonitored
+ _objc_msgSend$cpuNonFatalCnt
+ _objc_msgSend$cpuPercentageTriggerForWindowEndDate:windowStartDate:score:
+ _objc_msgSend$daemonJobLabel
+ _objc_msgSend$daemonOnly
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decideMitigation:withCoalitionName:withReason:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$defaultRestriction
+ _objc_msgSend$detectAcrossBoots
+ _objc_msgSend$detectAndInvokeIssueDetection:slidingWindowStartDate:
+ _objc_msgSend$detectIssuesFromStartTime:endDate:withRules:
+ _objc_msgSend$detectWithLookbackDuration:
+ _objc_msgSend$detectorString
+ _objc_msgSend$discoverPidForProcessName:withError:
+ _objc_msgSend$durationInSeconds
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$endTime
+ _objc_msgSend$energySnapshot
+ _objc_msgSend$energySnapshotNew
+ _objc_msgSend$errorString
+ _objc_msgSend$estimatedEnergyDiff
+ _objc_msgSend$evaluateRuleInFixedWindow:withStartDate:andEndDate:
+ _objc_msgSend$evaluateRuleWithSlidingWindow:withStartDate:andEndDate:
+ _objc_msgSend$exitMonitors
+ _objc_msgSend$exitsCnt
+ _objc_msgSend$fatalMitigatedProcessList
+ _objc_msgSend$fatalMitigation
+ _objc_msgSend$firstObject
+ _objc_msgSend$forceCPUViolationForProcess:withHandler:
+ _objc_msgSend$forceDetectorViolationForProcess:withHandler:
+ _objc_msgSend$forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:
+ _objc_msgSend$forceMitigationSuggestion
+ _objc_msgSend$generateIPSFileForProcess:
+ _objc_msgSend$generateMetadataForDrain:cpuPercentage:detectionLookbackDuration:
+ _objc_msgSend$generatePayloadWithMetadata:triggeredDetection:triggeredType:
+ _objc_msgSend$getAPWakeIntervalListWithStartDate:andEndDate:
+ _objc_msgSend$getCPUIssueStartEndTime:valueThreshold:
+ _objc_msgSend$getCPUIssueWithMitigationSuggestionForCoalitionID:withLaunchdName:fromStartDate:toEndDate:byRule:
+ _objc_msgSend$getCPUPercentageIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:
+ _objc_msgSend$getDetectionLookbackDuration
+ _objc_msgSend$getDeviceBootTime
+ _objc_msgSend$getDrainPercentage:
+ _objc_msgSend$getInfoForProcess:
+ _objc_msgSend$getMitigationTypeString:withStringSize:withMitigationType:withPenaltyBoxEndTime:
+ _objc_msgSend$getMonitoredList
+ _objc_msgSend$getMonotonicTime:
+ _objc_msgSend$getPidsForCoalitionID:
+ _objc_msgSend$getProcessForProcessName:
+ _objc_msgSend$getProcessForUUID:
+ _objc_msgSend$getProcessPathForPID:
+ _objc_msgSend$getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:
+ _objc_msgSend$getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:andCPURatio:
+ _objc_msgSend$getSystemTime:
+ _objc_msgSend$getTotalCPUTimeWithStartDate:andEndDate:
+ _objc_msgSend$getTriggerInterval
+ _objc_msgSend$getUnpluggedIntervalListWithStartDate:andEndDate:
+ _objc_msgSend$getValueOfMetric:startDate:endDate:
+ _objc_msgSend$handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:
+ _objc_msgSend$handleDetectedIssues:
+ _objc_msgSend$handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$handleDetectorViolation:
+ _objc_msgSend$handleDisplayStateChanged:
+ _objc_msgSend$handlePowerStateChanged
+ _objc_msgSend$handleProcessStart:withMitigationReason:
+ _objc_msgSend$inPenaltyBox
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithFilePath:
+ _objc_msgSend$initWithIdentifier:andLaunchdName:andIssueType:andStartTime:andEndTime:
+ _objc_msgSend$initWithIdentifier:andProcessName:andIssueType:andStartTime:andEndTime:
+ _objc_msgSend$initWithIntervals:
+ _objc_msgSend$initWithScalarMetric:andNormalizerMetric:andComparator:andValue:
+ _objc_msgSend$initWithStartTime:endTime:
+ _objc_msgSend$initWithStartTime:endTime:value:
+ _objc_msgSend$initWithStartTime:endTime:value:label:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:
+ _objc_msgSend$intersectWithIntervalList:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$intervalArray
+ _objc_msgSend$isAppleXPCServiceWithRBS:andPID:
+ _objc_msgSend$isXPCService
+ _objc_msgSend$isXPCServiceExempt:
+ _objc_msgSend$killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$lastCoalitionID
+ _objc_msgSend$lastInterval
+ _objc_msgSend$lastObject
+ _objc_msgSend$lastPID
+ _objc_msgSend$lastPUUID
+ _objc_msgSend$lastPid
+ _objc_msgSend$laterDate:
+ _objc_msgSend$launchdName
+ _objc_msgSend$length
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:
+ _objc_msgSend$logIssuesToPowerLogWithPayload:
+ _objc_msgSend$logMitigationAsSignpost:withPid:withIssueType:withMitigationType:withReason:withPenaltyBoxEndTime:
+ _objc_msgSend$logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:
+ _objc_msgSend$logPenaltyBoxListAsSignposts
+ _objc_msgSend$logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:
+ _objc_msgSend$mainThresholdValue
+ _objc_msgSend$midnightRoutine
+ _objc_msgSend$mitigationDecisionReason
+ _objc_msgSend$mitigationDecisionType
+ _objc_msgSend$mitigationManager
+ _objc_msgSend$mitigationSuggestion
+ _objc_msgSend$mitigationSuggestionReason
+ _objc_msgSend$modifyTriggerInterval:
+ _objc_msgSend$monitorForExitWithPID:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$normalizerMetric
+ _objc_msgSend$now
+ _objc_msgSend$null
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$openConnection
+ _objc_msgSend$overridden
+ _objc_msgSend$penaltyBoxCnt
+ _objc_msgSend$penaltyBoxCoalitionIDs
+ _objc_msgSend$penaltyBoxDurationMins
+ _objc_msgSend$penaltyBoxEndTime
+ _objc_msgSend$penaltyBoxPending
+ _objc_msgSend$penaltyBoxPolicy
+ _objc_msgSend$penaltyBoxProcesses
+ _objc_msgSend$performCleanupOnExitOnPID:
+ _objc_msgSend$performQuery:
+ _objc_msgSend$policyMitigationsEnabled
+ _objc_msgSend$powerlogDBReader
+ _objc_msgSend$previousPIDkeys
+ _objc_msgSend$previousPIDs
+ _objc_msgSend$processManager
+ _objc_msgSend$processName
+ _objc_msgSend$processNameForIdentifier:
+ _objc_msgSend$processTimerFiredAction
+ _objc_msgSend$processesAllowList
+ _objc_msgSend$processesDenyList
+ _objc_msgSend$processesRegexAllowList
+ _objc_msgSend$processesRegexDenyList
+ _objc_msgSend$putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$rangeOfFirstMatchInString:options:range:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$registerForDayChangedNotification
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeAllProcessesFromPenaltyBox
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeProcessFromPenaltyBox:forReason:
+ _objc_msgSend$removeTrackedPID:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$rootDaemon
+ _objc_msgSend$rule
+ _objc_msgSend$ruleID
+ _objc_msgSend$rules
+ _objc_msgSend$scalarMetric
+ _objc_msgSend$setBand80Mitigations:
+ _objc_msgSend$setBand95Mitigations:
+ _objc_msgSend$setCoalitionID:
+ _objc_msgSend$setCpuEnergy:
+ _objc_msgSend$setCpuEnergyBilledToMe:
+ _objc_msgSend$setCpuEnergyBilledToOthers:
+ _objc_msgSend$setCpuFatalCnt:
+ _objc_msgSend$setCpuMonitored:
+ _objc_msgSend$setCpuNonFatalCnt:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDetectAcrossBoots:
+ _objc_msgSend$setDetectorString:
+ _objc_msgSend$setEndTime:
+ _objc_msgSend$setEnergySnapshot:
+ _objc_msgSend$setEnergySnapshotNew:
+ _objc_msgSend$setErrorString:
+ _objc_msgSend$setEstimatedEnergyDiff:
+ _objc_msgSend$setEventHistory:
+ _objc_msgSend$setExitsCnt:
+ _objc_msgSend$setForceMitigationSuggestion:
+ _objc_msgSend$setInPenaltyBox:
+ _objc_msgSend$setLastPID:
+ _objc_msgSend$setLastPUUID:
+ _objc_msgSend$setMitigationDecisionReason:
+ _objc_msgSend$setMitigationDecisionType:
+ _objc_msgSend$setMitigationSuggestion:
+ _objc_msgSend$setMitigationSuggestionReason:
+ _objc_msgSend$setOverridden:
+ _objc_msgSend$setPenaltyBoxCnt:
+ _objc_msgSend$setPenaltyBoxDurationMins:
+ _objc_msgSend$setPenaltyBoxEndTime:
+ _objc_msgSend$setPenaltyBoxPending:
+ _objc_msgSend$setProcessName:
+ _objc_msgSend$setRootDaemon:
+ _objc_msgSend$setRule:
+ _objc_msgSend$setStartTime:
+ _objc_msgSend$setThreshold:overTimeWindow:forPID:withFatalEffect:
+ _objc_msgSend$setTime:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setUuid:
+ _objc_msgSend$setValue:
+ _objc_msgSend$setViolationDetectorString:
+ _objc_msgSend$setViolationEndTime:
+ _objc_msgSend$setViolationLimitValue:
+ _objc_msgSend$setViolationLimitWindow:
+ _objc_msgSend$setViolationObservationWindow:
+ _objc_msgSend$setViolationObservedValue:
+ _objc_msgSend$setViolationPath:
+ _objc_msgSend$setViolationPid:
+ _objc_msgSend$setXpcService:
+ _objc_msgSend$sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:
+ _objc_msgSend$signpostCategory
+ _objc_msgSend$slidingWindowStepSize
+ _objc_msgSend$snapshotCPUEnergy
+ _objc_msgSend$snapshotCPUEnergy:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$startTime
+ _objc_msgSend$string:matchesAnyRegexInArray:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$time
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeWeightedSum
+ _objc_msgSend$trackedPIDkeys
+ _objc_msgSend$trackedPIDs
+ _objc_msgSend$updateContextForIdentifier:withState:
+ _objc_msgSend$updateScheduledIntensiveContext:
+ _objc_msgSend$useSlidingWindow
+ _objc_msgSend$uuid
+ _objc_msgSend$value
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$violationDetectorString
+ _objc_msgSend$violationEndTime
+ _objc_msgSend$violationObservationWindow
+ _objc_msgSend$violationPath
+ _objc_msgSend$violationPid
+ _objc_msgSend$windowSize
+ _objc_msgSend$xpcService
+ _objc_msgSend$xpcServiceIdentifier
+ _objc_release_x10
+ _objc_retain_x25
+ _objc_retain_x26
+ _os_signpost_enabled
+ _proc_pidinfo
+ _setpriority
+ _sharedInstance.__sharedInstance
+ _sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:._sharedInstance
+ _sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:.onceToken
+ _signpostLog
+ _snprintf
+ _sysctl
+ _terminate_with_payload
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:]
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:].cold.1
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:].cold.2
- +[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:]
- -[CSCPUTimeRestriction applyToProcess:].cold.3
- -[CSCPUTimeRestriction applyToProcess:].cold.4
- -[CSCPUTimeRestriction applyToProcess:].cold.5
- -[CSCPUTimeRestriction enableLimitCPUUsage]
- -[CSCPUTimeRestriction globalOverrideCPUPercentage]
- -[CSCPUTimeRestriction globalOverrideCPUTimeWindow]
- -[CSCPUTimeRestriction globalOverrideLimitCPUPercentage]
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.1
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.2
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.3
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.4
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.5
- -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.6
- -[CSCPUTimeRestriction maxNumberOfKills]
- -[CSCPUTimeRestriction maxNumberOfNonfatal]
- -[CSCPUTimeRestriction setEnableLimitCPUUsage:]
- -[CSCPUTimeRestriction setGlobalOverrideCPUPercentage:]
- -[CSCPUTimeRestriction setGlobalOverrideCPUTimeWindow:]
- -[CSCPUTimeRestriction setGlobalOverrideLimitCPUPercentage:]
- -[CSCPUTimeRestriction setMaxNumberOfKills:]
- -[CSCPUTimeRestriction setMaxNumberOfNonfatal:]
- -[CSDaemon runInternalOnly]
- -[CSDaemon setRunInternalOnly:]
- -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.2
- -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.3
- -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.4
- -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.5
- -[CSExcessiveCPUViolationHandler logCPUViolationToPowerLogWithPayload:]
- -[CSExcessiveCPUViolationHandler logCPUViolationToPowerLogWithPayload:].cold.1
- -[CSExcessiveCPUViolationHandler logCPUViolationToPowerLogWithPayload:].cold.2
- -[CSProcess cpuIsFatal]
- -[CSProcess cpuUsageLimitSet]
- -[CSProcess cpu_fatal_cnt]
- -[CSProcess cpu_nonfatal_cnt]
- -[CSProcess currentPID]
- -[CSProcess exits_cnt]
- -[CSProcess monitorForExit]
- -[CSProcess monitorForExit].cold.1
- -[CSProcess monitorForExit].cold.2
- -[CSProcess monitorForExit].cold.3
- -[CSProcess performCleanupOnExit]
- -[CSProcess performCleanupOnExit].cold.1
- -[CSProcess processExitMonitor]
- -[CSProcess setCpuIsFatal:]
- -[CSProcess setCpuUsageLimitSet:]
- -[CSProcess setCpu_fatal_cnt:]
- -[CSProcess setCpu_nonfatal_cnt:]
- -[CSProcess setCurrentPID:]
- -[CSProcess setCurrentPID:].cold.1
- -[CSProcess setExits_cnt:]
- -[CSProcess setProcessExitMonitor:]
- -[CSProcessManager _initWithEnrolledProcesses:andExemptions:]
- -[CSProcessManager onlyMonitorDaemons]
- -[CSProcessManager setOnlyMonitorDaemons:]
- -[CSProcessManager setTimer:]
- -[CSProcessManager timer]
- -[CSRestrictionManager applyRestrictionsToProcess:forScenario:].cold.7
- -[CSRestrictionManager forceMitigation:forProcess:withHandler:]
- -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.1
- -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.2
- -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.3
- -[CSRestrictionManager getCountsForProcess:WithHandler:]
- -[CSRestrictionManager getCountsForProcess:WithHandler:].cold.1
- -[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]
- -[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:].cold.1
- -[CSRestrictionManager modifyRestrictionsByProcessPerScenario:]
- -[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withLimit:]
- -[CSRestrictionManager reportScheduledIntensiveWorkByProcesses:].cold.1
- GCC_except_table10
- GCC_except_table11
- GCC_except_table18
- GCC_except_table19
- GCC_except_table22
- GCC_except_table24
- GCC_except_table26
- GCC_except_table33
- GCC_except_table46
- GCC_except_table5
- _OBJC_CLASS_$_PLDefaults
- _OBJC_IVAR_$_CSCPUTimeRestriction._enableLimitCPUUsage
- _OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideCPUPercentage
- _OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideCPUTimeWindow
- _OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideLimitCPUPercentage
- _OBJC_IVAR_$_CSCPUTimeRestriction._maxNumberOfKills
- _OBJC_IVAR_$_CSCPUTimeRestriction._maxNumberOfNonfatal
- _OBJC_IVAR_$_CSDaemon._runInternalOnly
- _OBJC_IVAR_$_CSProcess._cpuIsFatal
- _OBJC_IVAR_$_CSProcess._cpuUsageLimitSet
- _OBJC_IVAR_$_CSProcess._cpu_fatal_cnt
- _OBJC_IVAR_$_CSProcess._cpu_nonfatal_cnt
- _OBJC_IVAR_$_CSProcess._currentPID
- _OBJC_IVAR_$_CSProcess._exits_cnt
- _OBJC_IVAR_$_CSProcess._processExitMonitor
- _OBJC_IVAR_$_CSProcessManager._onlyMonitorDaemons
- _OBJC_IVAR_$_CSProcessManager._timer
- _PowerLogLibrary
- _PowerLogLibraryCore.frameworkLibrary
- ___103-[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]_block_invoke
- ___103-[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]_block_invoke.149
- ___37-[CSProcessManager identiferForName:]_block_invoke
- ___42-[CSProcessManager modifyPollingInterval:]_block_invoke
- ___44-[CSProcessManager recordTerminationForPID:]_block_invoke
- ___56-[CSRestrictionManager getCountsForProcess:WithHandler:]_block_invoke
- ___56-[CSRestrictionManager getCountsForProcess:WithHandler:]_block_invoke.138
- ___63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke
- ___63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.152
- ___63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.153
- ___63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.163
- ___63-[CSRestrictionManager modifyRestrictionsByProcessPerScenario:]_block_invoke
- ___70+[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:]_block_invoke
- ___71-[CSExcessiveCPUViolationHandler logCPUViolationToPowerLogWithPayload:]_block_invoke
- ___71-[CSExcessiveCPUViolationHandler logCPUViolationToPowerLogWithPayload:]_block_invoke.cold.1
- ___74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke.cold.4
- ___81-[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withLimit:]_block_invoke
- ___PowerLogLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_58_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8w56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8
- ___block_literal_global.56
- ___block_literal_global.60
- ___block_literal_global.9
- ___getPPSCreateTelemetryIdentifierSymbolLoc_block_invoke
- ___getPPSSendTelemetrySymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringPowerLog
- _dispatch_time
- _dlerror
- _dlsym
- _gOverrideCPUPercentage
- _gOverrideCPUTimeWindow
- _gOverrideLimitCPUPercentage
- _gOverrideProcess
- _getPPSCreateTelemetryIdentifierSymbolLoc.ptr
- _getPPSSendTelemetrySymbolLoc.ptr
- _kPowerExceptionEnableLimitCPUUsage
- _kPowerExceptionGlobalCPUPercentage
- _kPowerExceptionGlobalCPUTimeWindow
- _kPowerExceptionGlobalLimitCPUPercentage
- _kPowerExceptionMaxKills
- _kPowerExceptionMaxNonFatal
- _objc_msgSend$_initWithEnrolledProcesses:andExemptions:
- _objc_msgSend$cpuIsFatal
- _objc_msgSend$cpu_fatal_cnt
- _objc_msgSend$cpu_nonfatal_cnt
- _objc_msgSend$currentPID
- _objc_msgSend$exits_cnt
- _objc_msgSend$identiferForPID:
- _objc_msgSend$incrementCPUViolationCounter:fatal:
- _objc_msgSend$longForKey:ifNotSet:
- _objc_msgSend$monitorForExit
- _objc_msgSend$name
- _objc_msgSend$performCleanupOnExit
- _objc_msgSend$processNameIdentiferByPID
- _objc_msgSend$setCpuIsFatal:
- _objc_msgSend$setCpuUsageLimitSet:
- _objc_msgSend$setCpu_fatal_cnt:
- _objc_msgSend$setCpu_nonfatal_cnt:
- _objc_msgSend$setCurrentPID:
- _objc_msgSend$setExits_cnt:
- _objc_msgSend$setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:
- _objc_msgSend$sharedInstanceWithEnrolledProcesses:andExemptions:
- _proc_set_cpumon_params_fatal
- _proc_setcpu_percentage
- _sharedInstanceWithEnrolledProcesses:andExemptions:._sharedInstance
- _sharedInstanceWithEnrolledProcesses:andExemptions:.onceToken
CStrings:
+ "\n%{public, name=processName0}s\n"
+ "\n%{public, name=processName0}s\n%{public, name=processName1}s\n"
+ "\n%{public, name=processName0}s\n%{public, name=processName1}s\n%{public, name=processName2}s\n"
+ "\n%{public, name=processName0}s\n%{public, name=processName1}s\n%{public, name=processName2}s\n%{public, name=processName3}s\n"
+ "\n%{public, name=processName0}s\n%{public, name=processName1}s\n%{public, name=processName2}s\n%{public, name=processName3}s\n%{public, name=processName4}s\n"
+ "                             SELECT sum (cpu_time) AS %@                              FROM PLCoalitionAgent_EventInterval_CoalitionInterval where timestamp >= %f AND timestamp <= %f"
+ "                             SELECT timestamp AS %@,                              Level AS %@,                              energyConsumed AS %@                             FROM PLBatteryAgent_Aggregate_UILevel WHERE timestamp >= %f AND timestamp <= %f ORDER BY timestamp DESC"
+ " AND LaunchdName in (\"%@\")"
+ " AND LaunchdName not in (\"%@\")"
+ " ORDER by timestamp"
+ " getTotalCPUDrainBetweenTimeInterval Query %@"
+ " getTotalCPUTimeWithStartDate Query %@"
+ "\",\""
+ "%@:%@"
+ "%s (%d)"
+ "%s (for %lld seconds)"
+ "%s (until midnight)"
+ "+"
+ "++APAwakeDurationUnplugged condition meet"
+ "++APWakeDuration condition meet"
+ "++CPU threshold matches process %@"
+ "++CPU unplugged threshold matches process %@"
+ "++UnpluggedDuration condition meet"
+ ","
+ "--APAwakeDurationUnplugged condition not meet"
+ "--APWakeDuration condition not meet"
+ "--UnpluggedDuration condition not meet"
+ ".*coreautomation.coreautomationd.*"
+ "/Library/BatteryLife/CurrentPowerlog.PLSQL"
+ "1"
+ "5"
+ ":"
+ "@\"CPUEnergySnapshot\""
+ "@\"CSDetectionRule\""
+ "@\"CSIssueDetector\""
+ "@\"CSMitigationManager\""
+ "@\"CSPowerlogDBReader\""
+ "@\"CSTriggerManager\""
+ "@\"NSDate\""
+ "@\"NSMutableArray\""
+ "@\"NSUUID\""
+ "@\"PLSQLiteConnection\""
+ "@24@0:8Q16"
+ "@28@0:8@16f24"
+ "@28@0:8i16@20"
+ "@28@0:8i16i20i24"
+ "@32@0:8@16i24i28"
+ "@32@0:8i16i20i24f28"
+ "@36@0:8i16@20@28"
+ "@40@0:8@16@24d32"
+ "@44@0:8i16@20@28@36"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8@16@24d32@40"
+ "@52@0:8@16@24@32@40B48"
+ "@52@0:8@16@24i32@36@44"
+ "@52@0:8i16@20@28@36@44"
+ "@52@0:8i16@20@28@36d44"
+ "@72@0:8f16@20@28@36@44@52B60f64i68"
+ "AlreadyBackgroundQoS"
+ "Applying restrictions:%@ to processIdentifier:%@"
+ "Attempted applying thresholds on process:%@ with no current tracked pids"
+ "AutomatedDeviceGroup"
+ "B28@0:8@16C24"
+ "B28@0:8@16i24"
+ "B28@0:8f16f20i24"
+ "B32@0:8d16d24"
+ "B40@0:8@16@24^d32"
+ "B40@0:8@16d24d32"
+ "BackgroundQoSDisabled"
+ "BackgroundQoSEnabled"
+ "BackgroundQoSFailed"
+ "Band 9%d) Processes array missing"
+ "Band80"
+ "Band80Process: %@"
+ "Band95"
+ "Band95Process: %@"
+ "BatteryDrain"
+ "BundleID"
+ "C"
+ "C16@0:8"
+ "C40@0:8@16@24^C32"
+ "CPU"
+ "CPU Percentage: %{public, name=percentage}d\n"
+ "CPU Violation"
+ "CPU::%@"
+ "CPU::process1"
+ "CPU::process2"
+ "CPUCoalition"
+ "CPUEnergySnapshot"
+ "CPUPercentage"
+ "CSDetectionRule"
+ "CSDetectionRule: id: %d, windowSize: %.0f"
+ "CSDetectionRuleCondition"
+ "CSInterval"
+ "CSInterval:\nstartTime:%@, \nendTime:%@, \nvalue:%f, \nlabel:%@,"
+ "CSIntervalList"
+ "CSIssue"
+ "CSIssue with nameIdentifier: %@, \nlaunchdName:%@, \nstartTime:%@, \nendTime:%@, \nvalue:%.4f \nprocessName:%@, \npid: %d, \npuuid: %@, \ncoalitionID: %llu, \nmitigationSuggestion: %d, \nforceMitigationSuggestion: %d, \nmitigationSuggestionReason: %d, \noverridden: %d, \nruleID: %d, \nmitigationDecisionType: %d, \nmitigationDecisionReason:%d"
+ "CSIssueDetector"
+ "CSMitigationManager"
+ "CSPowerlogDBReader"
+ "CSProcess with nameIdentifier: %@"
+ "CSTriggerManager"
+ "Clear current restrictions %@ for processIdentifier:%@ in scenario:%@"
+ "Cleared fatalMitigatedProcessList at midnight."
+ "Clearing current restrictions for processIdentifier:%@"
+ "CoalitionID"
+ "CoalitionName"
+ "Configuring cpuMonitor with cpuThreshold: %@, timeWindow:%@ for process:%@ (%d)"
+ "Could not create band (%d) process set from plist"
+ "Could not find band_restrictions plist"
+ "Could not locate Scenario:%@ for processIdentifier:%@ in _restrictionsByProcessPerScenario"
+ "Could not locate object corresponding to processIdentifier:%@"
+ "Could not locate processIdentifier: %@ in _restrictionsByProcessPerScenario"
+ "Default"
+ "DetectionLookbackDuration"
+ "Determining restrictions for processIdentifier:%@ in scenario:%@"
+ "Do not apply any restriction to processIdentifier:%@ while temporarily exempted"
+ "Drain Percentage: %{public, name=drainPercentage}d\n"
+ "DrainPercentage"
+ "EndTime"
+ "EnergyConsumed"
+ "Error totalApWakeTime is 0"
+ "Error when getting APAwakeDuration"
+ "Error when getting APAwakeDurationUnplugged"
+ "Error when getting UnpluggedDuration"
+ "Error when getting normalizer value from metric %d"
+ "ErrorString"
+ "EstimatedEnergy"
+ "Evaluate rule %d in sliding windows in range [%@, %@]"
+ "Evaluating rule %d in a fixed window [%@, %@]"
+ "Event"
+ "ExemptedCPUMon"
+ "ExemptedDAS"
+ "ExemptedPluggedIn"
+ "ExemptedProcess"
+ "ExemptedRootDaemon"
+ "ExternalConnected"
+ "FALSE"
+ "Fail to find a process name with higher than %f CPU ratio"
+ "Fail to get last PID for process name %@"
+ "Failed %d to get initial Display state"
+ "Failed %d to release restriction:%@ for processIdentifier:%@"
+ "Failed %d to release restriction:%@ for processIdentifier:%@, skipping any further restrictions"
+ "Failed to apply restriction:%@ to processIdentifier:%@, skipping any further restrictions"
+ "Failed to get CSProcessManager"
+ "FatalLimitReached"
+ "FatalSkipped"
+ "FeatureFlagOff"
+ "Finish detection for rule %d: Detected %lu issues"
+ "Flushing powerlog tables"
+ "ForceMitigationSuggestion"
+ "ForcedMitigation"
+ "Found issue with IssueType:%s in Rule: %d for process: %s with coalitionID: %llu from time %s to %s"
+ "FromRestriction"
+ "I"
+ "I16@0:8"
+ "IllegalValue"
+ "Interval: %{public, name=interval}f\n"
+ "Invalid regex pattern: %@, error: %@"
+ "InvalidArgument"
+ "Issue Detected"
+ "Issue on %@ already detected in a previous sliding window."
+ "KQ$"
+ "KillFailed"
+ "KnownViolation"
+ "LaunchdCoalitionID"
+ "LaunchdName"
+ "Loading bands_restrictions.plist for Band%d"
+ "Logging trigger information in powerlog"
+ "Metadata"
+ "Metric Type ?? (%d) is not support"
+ "Metric Type CPUSecond (%d) doesn't output a single value"
+ "Metric Type CPUSecondUnplugged (%d) doesn't output a single value"
+ "Mitigation Applied"
+ "MitigationDecisionReason"
+ "MitigationDecisionType"
+ "MitigationFailed"
+ "MitigationSuggestion"
+ "MitigationSuggestionReason"
+ "MitigationsEnabled"
+ "MoreThanOneProcesses"
+ "No rule based detection: PerfPowerServices/safeguards_rule_detection feature flag is off"
+ "No scenarioName to use, logging empty scenario name for violation for process:%@."
+ "No scenarios available for processIdentifier: %@. Proceeding to apply default policy."
+ "NoCoalitionPids"
+ "NoProcess"
+ "NoProcessData"
+ "NoProcessIdentifier"
+ "NoProcessName"
+ "NonFatalLimitReached"
+ "NonFatalMonitorOnly"
+ "Normalizer Metric Type %d is zero"
+ "NotDaemon"
+ "NullString"
+ "OffCharger"
+ "Overridden"
+ "OverriddenByOtherRules"
+ "PID"
+ "PLPowerExceptionsExemptionsSyncNotification"
+ "POWER_EXCEPTIONS_MITIGATIONS"
+ "PUUID"
+ "PartialMitigation"
+ "Penalty Box List"
+ "PenaltyBoxDurationMins"
+ "PenaltyBoxIn"
+ "PenaltyBoxOut"
+ "PendingBackgroundQoS"
+ "Power Exceptions Kill - issueType:%s, mitigationType:%s mitigationReason:%s"
+ "PowerExceptions"
+ "PowerExceptionsDetection"
+ "PowerExceptionsRelaunched"
+ "Prepare detection for rule %d: Waiting for %.0f seconds, without sliding window"
+ "Process name: %{public, name=processName}s\nSignpost ID is PID\nCoalition ID: %{public, name=coalitionID}llu\nIssue Type: %{public, name=issueType}s\nMitigation Type: %{public, name=mitigationType}s\nMitigation Reason: %{public, name=mitigationReason}s\n"
+ "Process name: %{public, name=processName}s\nSignpost ID is PID\nCoalition name: %{public, name=coalitionName}s\nScenario Identifier: %{public, name=scenarioIdentifier}s\nTime Stamp End: %{public, name=timeStampEnd}f\nCPU Threshold: %{public, name=cpuThreshold}lld\nTime Window Size: %{public, name=timeWindowSize}lld\nObserved CPU Usage: %{public, name=observedCPUUsage}f\nObserved CPU Usage Duration: %{public, name=observedCPUUsageDuration}f\nIssue Type: %{public, name=issueType}s\nMitigation Type: %{public, name=mitigationType}s\nMitigation Reason: %{public, name=mitigationReason}s\nError String: %{public, name=errorString}s\nFrom Power Exceptions: %{public, name=fromPowerExceptions}d\nFatal Count: %{public, name=fatalCount}d\nNon Fatal Count: %{public, name=nonFatalCount}d\n"
+ "Process name: %{public, name=processName}s\nSignpost ID is PID\nTime Stamp Start: %{public, name=timeStampStart}s\nTime Stamp End: %{public, name=timeStampEnd}s\nIssue Type: %{public, name=issueType}s\nValue: %{public, name=value}d\nCoalition ID: %{public, name=coalitionID}lld\nCoalition name: %{public, name=coalitionName}s\nRule ID: %{public, name=ruleID}d\nMitigation Suggestion: %{public, name=mitigationSuggestion}s\nMitigation Suggestion Reason: %{public, name=mitigationSuggestionReason}s\nForce Mitigation Suggestion: %{public, name=forceMitigationSuggestion}d\nOverridden: %{public, name=overridden}d\nMitigation Decision Type: %{public, name=mitigationDecisionType}s\nMitigation Decision Reason: %{public, name=mitigationDecisionReason}s\nError String: %{public, name=errorString}s\n"
+ "ProcessNotRunning"
+ "ProcessRelaunched"
+ "Q32@0:8@16@24"
+ "Received CPU violation: %s[%llu] (%@) used %.2f seconds of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2f seconds over %lld seconds."
+ "Repeating timer for PID polling disarmed."
+ "Repeating timer for Trigger polling armed."
+ "Restrictions are unchanged for processIdentifier:%@ for scenario:%@"
+ "RuleID"
+ "S"
+ "S16@0:8"
+ "SELECT LaunchdName AS %@, LaunchdCoalitionID AS %@, BundleId AS %@, CASE WHEN timestamp > %f THEN timestamp ELSE %f END AS %@, CASE WHEN timestampEnd < %f THEN timestampEnd ELSE %f END AS %@, cpu_time / (timestampEnd - timestamp) AS %@ FROM PLCoalitionAgent_EventInterval_CoalitionInterval WHERE timestampEnd >= %f AND timestamp <= %f"
+ "SELECT ProcessName AS %@, SUM(value) AS %@ from PLProcessMonitorAgent_EventInterval_ProcessMonitorInterval AS a JOIN PLProcessMonitorAgent_EventInterval_ProcessMonitorInterval_Dynamic AS b ON a.ID = b.FK_ID WHERE PID in (%@) AND timestamp <= %f AND timestampEnd >= %f GROUP BY ProcessName"
+ "SELECT system FROM PLStorageOperator_EventForward_TimeOffset WHERE timestamp + system <= %f ORDER BY timestamp DESC LIMIT 1;"
+ "SELECT system FROM PLStorageOperator_EventForward_TimeOffset WHERE timestamp + system > %f ORDER BY timestamp LIMIT 1;"
+ "SELECT system FROM PLStorageOperator_EventForward_TimeOffset WHERE timestamp <= %f ORDER BY timestamp DESC LIMIT 1;"
+ "SELECT system FROM PLStorageOperator_EventForward_TimeOffset WHERE timestamp > %f ORDER BY timestamp LIMIT 1;"
+ "SELECT timestamp, Event FROM PLSleepWakeAgent_EventForward_PowerState WHERE timestamp <= %f AND timestamp >= %f ORDER by timestamp"
+ "SELECT timestamp, ExternalConnected FROM PLBatteryAgent_EventBackward_Battery WHERE timestamp >= %f - 300 AND timestamp < %f ORDER by timestamp"
+ "SELECT timestamp, PID, ProcessName, PUUID FROM PLProcessMonitorAgent_EventForward_ProcessID WHERE CoalitionID=%d AND timestamp >= %f AND timestamp <= %f;"
+ "Scalar Metric Type %d is not supported"
+ "Scenarios that remain active after debounce: %@"
+ "Skip evaluating rule since duration from %@ to %@ is not enough for %f"
+ "Skip evaluating rule since startDate %@ is later than endDate %@"
+ "Skip evaluting rule since duration from %@ to %@ is not enough for %f"
+ "Skip evaluting rule since startDate %@ is later than endDate %@"
+ "Skipping pid: %d since we could not get daemonJobLabel, bundleIDidentifier or name"
+ "Skipping process:%@ (%d) since could not create CSProcess"
+ "Source"
+ "Start detection for rule %d: From %@ to %@, with sliding window"
+ "Start detection for rule %d: From %@ to %@, without sliding window"
+ "StartTime"
+ "Started CSTriggerManagerService"
+ "Starting Rule Based Detection"
+ "Successfully applied restriction: %@ to processIdentifier: %@"
+ "T@\"<CSRestriction>\",&,V_band80Restriction"
+ "T@\"<CSRestriction>\",&,V_band95Restriction"
+ "T@\"CPUEnergySnapshot\",&,V_energySnapshot"
+ "T@\"CPUEnergySnapshot\",&,V_energySnapshotNew"
+ "T@\"CSDetectionRule\",&,V_rule"
+ "T@\"CSIssueDetector\",&,V_issueDetector"
+ "T@\"CSMitigationManager\",&,V_mitigationManager"
+ "T@\"CSPowerlogDBReader\",&,V_powerlogDBReader"
+ "T@\"CSProcessManager\",&,N,V_processManager"
+ "T@\"CSTriggerManager\",&,V_triggerManager"
+ "T@\"NSArray\",&,V_conditions"
+ "T@\"NSArray\",&,V_genericCPUDetectorProcessDenyList"
+ "T@\"NSArray\",&,V_genericCPUDetectorProcessRegexDenyList"
+ "T@\"NSArray\",&,V_processesAllowList"
+ "T@\"NSArray\",&,V_processesDenyList"
+ "T@\"NSArray\",&,V_processesRegexAllowList"
+ "T@\"NSArray\",&,V_processesRegexDenyList"
+ "T@\"NSArray\",&,V_rules"
+ "T@\"NSDate\",&,V_endTime"
+ "T@\"NSDate\",&,V_lastTriggerTimerDate"
+ "T@\"NSDate\",&,V_startTime"
+ "T@\"NSDate\",&,V_time"
+ "T@\"NSMutableArray\",&,N,V_affectedProcesses"
+ "T@\"NSMutableArray\",&,V_eventHistory"
+ "T@\"NSMutableArray\",&,V_fatalMitigatedProcessList"
+ "T@\"NSMutableArray\",&,V_intervalArray"
+ "T@\"NSMutableArray\",&,V_previousPIDkeys"
+ "T@\"NSMutableArray\",&,V_trackedPIDkeys"
+ "T@\"NSMutableDictionary\",&,N,V_penaltyBoxProcesses"
+ "T@\"NSMutableDictionary\",&,V_allProcessesMap"
+ "T@\"NSMutableDictionary\",&,V_currentPIDList"
+ "T@\"NSMutableDictionary\",&,V_exitMonitors"
+ "T@\"NSMutableDictionary\",&,V_penaltyBoxCoalitionIDs"
+ "T@\"NSMutableDictionary\",&,V_previousPIDs"
+ "T@\"NSMutableDictionary\",&,V_processNameIdentiferByName"
+ "T@\"NSMutableDictionary\",&,V_processNameIdentiferByPID"
+ "T@\"NSMutableDictionary\",&,V_trackedPIDs"
+ "T@\"NSMutableSet\",&,V_observers"
+ "T@\"NSMutableSet\",&,V_scheduledIntensiveProcesses"
+ "T@\"NSNumber\",&,V_cpuThreshold"
+ "T@\"NSNumber\",&,V_cpuTimeWindow"
+ "T@\"NSNumber\",&,V_value"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_penaltyBoxTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_triggerTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_pollingTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_triggerTimer"
+ "T@\"NSSet\",&,V_band80Processes"
+ "T@\"NSSet\",&,V_band80ProcessesSet"
+ "T@\"NSSet\",&,V_band95Processes"
+ "T@\"NSSet\",&,V_band95ProcessesSet"
+ "T@\"NSSet\",&,V_enrolledProcessesSet"
+ "T@\"NSSet\",&,V_exemptProcessesSet"
+ "T@\"NSString\",&,V_detectorString"
+ "T@\"NSString\",&,V_errorString"
+ "T@\"NSString\",&,V_label"
+ "T@\"NSString\",&,V_lastPUUID"
+ "T@\"NSString\",&,V_launchdName"
+ "T@\"NSString\",&,V_processName"
+ "T@\"NSString\",&,V_violationDetectorString"
+ "T@\"NSString\",&,V_violationPath"
+ "T@\"NSString\",R,V_identifier"
+ "T@\"NSUUID\",&,V_uuid"
+ "T@\"PLSQLiteConnection\",&,V_conn"
+ "TB,N,V_penaltyBoxEnabled"
+ "TB,V_band80Mitigations"
+ "TB,V_band95Mitigations"
+ "TB,V_cpuMonitored"
+ "TB,V_daemonOnly"
+ "TB,V_detectAcrossBoots"
+ "TB,V_exemptFromMitigations"
+ "TB,V_forceMitigationSuggestion"
+ "TB,V_inPenaltyBox"
+ "TB,V_needClearRestrictions"
+ "TB,V_overridden"
+ "TB,V_penaltyBoxPending"
+ "TB,V_pollingTimerActive"
+ "TB,V_resetNonFatalCPUMonitor"
+ "TB,V_rootDaemon"
+ "TB,V_unknownScheduledIntensiveProcesses"
+ "TB,V_useSlidingWindow"
+ "TB,V_xpcService"
+ "TC,V_cpuFatalCnt"
+ "TC,V_issueType"
+ "TC,V_mitigationDecisionReason"
+ "TC,V_mitigationDecisionType"
+ "TC,V_mitigationReason"
+ "TC,V_mitigationSuggestion"
+ "TC,V_mitigationType"
+ "TC,V_penaltyBoxCnt"
+ "TI,V_estimatedEnergyDiff"
+ "TQ,V_coalitionID"
+ "TQ,V_cpuEnergy"
+ "TQ,V_cpuEnergyBilledToMe"
+ "TQ,V_cpuEnergyBilledToOthers"
+ "TQ,V_penaltyBoxEndTime"
+ "TRUE"
+ "TS,V_cpuNonFatalCnt"
+ "TS,V_exitsCnt"
+ "Td,V_value"
+ "Tf,V_PIDPollingInterval"
+ "Tf,V_mainThresholdValue"
+ "Tf,V_savedPIDPollingInterval"
+ "Tf,V_savedTriggerInterval"
+ "Tf,V_slidingWindowStepSize"
+ "Tf,V_triggerInterval"
+ "Tf,V_value"
+ "Tf,V_windowSize"
+ "Ti,N,V_penaltyBoxPolicy"
+ "Ti,V_comparator"
+ "Ti,V_displayStatusNotifyToken"
+ "Ti,V_lastPID"
+ "Ti,V_mitigationSuggestionReason"
+ "Ti,V_monitorFilterBitMap"
+ "Ti,V_normalizerMetric"
+ "Ti,V_powerStatusNotifyToken"
+ "Ti,V_ruleID"
+ "Ti,V_scalarMetric"
+ "Ti,V_trialsMitigationsEnabled"
+ "Ti,V_violationPid"
+ "TimeLimitExpired"
+ "Timestamp"
+ "TimestampEnd"
+ "TimestampStart"
+ "Total"
+ "Total CPU time %f from ProcessMonitor is less than threshold %f"
+ "Tq,N,V_penaltyBoxTimerRunning"
+ "Tq,V_penaltyBoxDurationMins"
+ "Tq,V_violationLimitValue"
+ "Tq,V_violationLimitWindow"
+ "Tq,V_violationObservationWindow"
+ "Tq,V_violationObservedValue"
+ "Trigger DB query returned non empty results. Processing"
+ "Trigger Detection"
+ "Trigger Fired"
+ "Trigger NonDetection"
+ "TriggerEvents"
+ "TriggeredDetection"
+ "T{mach_timespec=Ii},V_violationEndTime"
+ "UUIDString"
+ "Unknown penalty box policy:%d"
+ "UnknownProcessName"
+ "Updated startDate (was %@) to deviceBootTime %@"
+ "Use step size %.1f instead of %.1f in rule %d since it was too small"
+ "Using bundleID:%@ for pid: %d"
+ "Using daemonJobLabel:%@ for pid: %d"
+ "Using name:%@ for pid: %d"
+ "Using xpcServiceIdentifier:%@ for pid: %d"
+ "Value"
+ "ViolationType"
+ "Wrong format of launchdNameAndCID: %@"
+ "XPCCacheFlush"
+ "_affectedProcesses"
+ "_band80Mitigations"
+ "_band80Processes"
+ "_band80ProcessesSet"
+ "_band80Restriction"
+ "_band95Mitigations"
+ "_band95Processes"
+ "_band95ProcessesSet"
+ "_band95Restriction"
+ "_bandRestrictionsSetForThreshold: Band (%d) Processes array missing"
+ "_bandRestrictionsSetForThreshold: Could not create band (%d) process set from plist"
+ "_bandRestrictionsSetForThreshold: Could not find band_restrictions plist"
+ "_bandRestrictionsSetForThreshold: Unknown threshold of %d"
+ "_bandRestrictionsSetForThreshold:withErrors:"
+ "_coalitionID"
+ "_comparator"
+ "_conditions"
+ "_conn"
+ "_cpuEnergy"
+ "_cpuEnergyBilledToMe"
+ "_cpuEnergyBilledToOthers"
+ "_cpuFatalCnt"
+ "_cpuMonitored"
+ "_cpuNonFatalCnt"
+ "_daemonOnly"
+ "_detectAcrossBoots"
+ "_detectorString"
+ "_displayStatusNotifyToken"
+ "_endTime"
+ "_energySnapshot"
+ "_energySnapshotNew"
+ "_errorString"
+ "_estimatedEnergyDiff"
+ "_eventHistory"
+ "_exitMonitors"
+ "_exitsCnt"
+ "_fatalMitigatedProcessList"
+ "_forceMitigationSuggestion"
+ "_genericCPUDetectorProcessDenyList"
+ "_genericCPUDetectorProcessRegexDenyList"
+ "_inPenaltyBox"
+ "_initWithDataProvider: XPC Services mitigations disabled by feature flag"
+ "_initWithDataProvider: mitigations enabled by feature flag"
+ "_initWithDataProvider: mitigations while plugged-in enabled by feature flag"
+ "_initWithDataProvider: penaltyBox enabled by feature flag"
+ "_initWithEnrolledProcesses:andExemptions:andBand95:andBand80:"
+ "_intervalArray"
+ "_issueDetector"
+ "_label"
+ "_lastPID"
+ "_lastPUUID"
+ "_lastTriggerTimerDate"
+ "_launchdName"
+ "_mainThresholdValue"
+ "_mitigationDecisionReason"
+ "_mitigationDecisionType"
+ "_mitigationManager"
+ "_mitigationSuggestion"
+ "_mitigationSuggestionReason"
+ "_monitorFilterBitMap"
+ "_normalizerMetric"
+ "_overridden"
+ "_penaltyBoxCnt"
+ "_penaltyBoxCoalitionIDs"
+ "_penaltyBoxDurationMins"
+ "_penaltyBoxEnabled"
+ "_penaltyBoxEndTime"
+ "_penaltyBoxPending"
+ "_penaltyBoxPolicy"
+ "_penaltyBoxProcesses"
+ "_penaltyBoxTimer"
+ "_penaltyBoxTimerRunning"
+ "_pollingTimer"
+ "_pollingTimerActive"
+ "_powerStatusNotifyToken"
+ "_powerlogDBReader"
+ "_previousPIDkeys"
+ "_previousPIDs"
+ "_processName"
+ "_processesAllowList"
+ "_processesDenyList"
+ "_processesRegexAllowList"
+ "_processesRegexDenyList"
+ "_rootDaemon"
+ "_rule"
+ "_ruleID"
+ "_rules"
+ "_savedPIDPollingInterval"
+ "_savedTriggerInterval"
+ "_scalarMetric"
+ "_scheduledIntensiveProcesses"
+ "_slidingWindowStepSize"
+ "_startTime"
+ "_time"
+ "_trackedPIDkeys"
+ "_trackedPIDs"
+ "_trialsMitigationsEnabled"
+ "_triggerInterval"
+ "_triggerManager"
+ "_triggerTimer"
+ "_unknownScheduledIntensiveProcesses"
+ "_useSlidingWindow"
+ "_uuid"
+ "_value"
+ "_violationDetectorString"
+ "_violationEndTime"
+ "_violationLimitValue"
+ "_violationLimitWindow"
+ "_violationObservationWindow"
+ "_violationObservedValue"
+ "_violationPath"
+ "_violationPid"
+ "_windowSize"
+ "_xpcService"
+ "addInterval:"
+ "addMitigationEvent:startTime:"
+ "addNewTrackedPID:"
+ "addNewTrackedPID: Too many pids (> %d) so remove tracked pid %d from process %@"
+ "addObjectsFromArray:"
+ "addObserver:selector:name:object:"
+ "addPenaltyBoxCoalitionID:"
+ "addViolationEvent:startTime:endTime:"
+ "affectedProcesses"
+ "allKeysForObject:"
+ "applyDefaultRestrictionsToProcess: Applying default restrictions for processIdentifier:%@"
+ "applyDefaultRestrictionsToProcess: Clear current restrictions %@ for processIdentifier:%@"
+ "applyDefaultRestrictionsToProcess: Failed %d to release restriction:%@ for processIdentifier:%@, skipping any further restrictions"
+ "applyDefaultRestrictionsToProcess: Failed to apply restriction:%@ to processIdentifier:%@."
+ "applyDefaultRestrictionsToProcess: Successfully applied restriction:%@ restriction to processIdentifier: %@"
+ "applyPluggedInRestrictionsToProcess:"
+ "applyRestriction: Could not find CSProcess for process:%@"
+ "applyRestriction: IssueType:%s MitigationType:%s MitigationReason:%s cpuFatalCnt:%u cpu_non_fatal_cnt:%u exitsCnt:%u penaltyBoxCnt:%u for process %@"
+ "applyRestriction: Process:%@ has no currently tracked pids"
+ "applyRestriction: Process:%@ is an exempt root daemon so no mitigations"
+ "applyRestriction: Process:%@ is on exempt list so no mitigations"
+ "applyRestriction: device is plugged in so no mitigations"
+ "applyRestriction:withProcessIdentifier:"
+ "arrayWithObjects:count:"
+ "band80Mitigations"
+ "band80Processes"
+ "band80ProcessesSet"
+ "band80Restriction"
+ "band95Mitigations"
+ "band95Processes"
+ "band95ProcessesSet"
+ "band95Restriction"
+ "booleanValue"
+ "bundle"
+ "bundleId"
+ "changedScenarios:%@ currentActiveScenarios%@"
+ "checkCpuPercentageAndInvokeIssueDetection:windowStartDate:"
+ "checkDrainAndInvokeIssueDetection:"
+ "checkForTrials"
+ "checkForTrials: The user is in the experimental group with mitigationsEnabled: %@"
+ "checkForTrials: Think this is a test device so leave mitigations off"
+ "checkForTrials: getting trialClient failed"
+ "checkForTrials: getting trialMitigationsEnabled failed"
+ "checkKnownViolationByProcess: process is NULL???"
+ "checkKnownViolationByProcess:withStartTime:withEndTime:"
+ "checkKnownViolationStartTime:endTime:"
+ "checkOverridesForProcess: Global overriding cpu threshold to be (%ld) for process:%@"
+ "checkOverridesForProcess: Global overriding cpu time window to be (%ld) for process:%@"
+ "checkOverridesForProcess: Global overriding penalty box duration to be (%ld) minutes for process:%@"
+ "checkOverridesForProcess: Target cpu threshold set to (%ld) for process:%@"
+ "checkOverridesForProcess: Target cpu time window set to (%ld) for process:%@"
+ "checkOverridesForProcess: Target penalty box duration set to (%ld) minutes for process:%@"
+ "checkOverridesForProcess:penaltyBoxDuration:cpuThreshold:timeWindow:"
+ "checkPenaltyBoxProcessesExpiration"
+ "checkPenaltyBoxProcessesExpiration: Checking process:%@"
+ "checkPenaltyBoxProcessesExpiration: Process:%@ has no currently tracked pids"
+ "checkPenaltyBoxProcessesExpiration: Resuming penalty box timer"
+ "checkPenaltyBoxProcessesExpiration: Unknown penalty box policy:%d"
+ "checkPenaltyBoxProcessesExpiration: Why is penalty box timer still running?"
+ "checkPenaltyBoxProcessesExpiration: done with serving time (%llu >= %llu) in penalty box for process:%@. Clearing backgroundQoS for this process."
+ "checkPenaltyBoxProcessesExpiration: empty process list"
+ "checkPenaltyBoxProcessesExpiration: leaving with empty process list so halting timer"
+ "checkPenaltyBoxProcessesExpiration: process is nil for nsUUID:%@?"
+ "checkPenaltyBoxProcessesLifecycle: Put process:%@ back into penalty box for remaining %llu seconds"
+ "checkPenaltyBoxProcessesLifecycle: process is Null?"
+ "checkPenaltyBoxProcessesLifecycle:withMitigationReason:"
+ "checkScheduledIntensiveInNewProcesses:"
+ "checkScheduledIntensiveProcesses: found missing processes"
+ "checkScheduledIntensiveProcesses: unrecognized process name: %@"
+ "clearAllCounters"
+ "clearFatalMitigatedProcessList"
+ "clearMonitorForPID: Error disabling CPU monitoring: %d (%s) for pid %d"
+ "clearTargetProcess"
+ "clearTargetProcessState"
+ "clientWithIdentifier:"
+ "closeConnection"
+ "coalitionID"
+ "coalitionID is nil"
+ "coalitionIDForPid:coalitionID:"
+ "coalition_info_resource_usage failed with error: %d"
+ "com.apple"
+ "com.apple."
+ "com.apple.CommCenterMobileHelper"
+ "com.apple.CommCenterRootHelper"
+ "com.apple.DTServiceHub"
+ "com.apple.MobileSoftwareUpdate.UpdateBrainService"
+ "com.apple.NRD.UpdateBrainService"
+ "com.apple.NRDUpdated"
+ "com.apple.ReportMemoryException"
+ "com.apple.abm-helper"
+ "com.apple.applebbproxy"
+ "com.apple.appleh10camerad"
+ "com.apple.bbswbypass"
+ "com.apple.computesafeguards.mitigationmanager"
+ "com.apple.da"
+ "com.apple.diagnosticpipeline"
+ "com.apple.diskimagesiod"
+ "com.apple.filesystems.fskitd"
+ "com.apple.filesystems.lifs.userfsd.UVFSService"
+ "com.apple.filesystems.smbclientd"
+ "com.apple.filesystems.userfsd"
+ "com.apple.hangreporter"
+ "com.apple.hangtracerd"
+ "com.apple.iokit.hid.displayStatus"
+ "com.apple.launchd.development"
+ "com.apple.mediaanalysisd-service"
+ "com.apple.mediaserverd"
+ "com.apple.memoryanalyticsd"
+ "com.apple.metrickitd"
+ "com.apple.mobile.NRDUpdated"
+ "com.apple.mobile.softwareupdated"
+ "com.apple.powerexceptionsd"
+ "com.apple.spindump"
+ "com.apple.symptomsd"
+ "com.apple.symptomsd-diag"
+ "com.apple.symptomsd-helper"
+ "com.apple.syncdefaultsd<"
+ "com.apple.sysdiagnose_helper"
+ "com.apple.sysdiagnosed"
+ "com.apple.system.powersources.source"
+ "com.apple.tailspind"
+ "com\\.openssh\\.sshd\\..*"
+ "comparator"
+ "compare:"
+ "compareWithValue1:andValue2:andComparator:"
+ "componentsJoinedByString:"
+ "computeEnergyDiff:"
+ "conditions"
+ "conn"
+ "containerPath"
+ "cpuEnergy"
+ "cpuEnergyBilledToMe"
+ "cpuEnergyBilledToOthers"
+ "cpuFatalCnt"
+ "cpuMonitored"
+ "cpuNonFatalCnt"
+ "cpuPercentageTrigger: cpuTimeS: %f, apWakeTimeS %f"
+ "cpuPercentageTriggerForWindowEndDate:windowStartDate:score:"
+ "currentTimeSecs"
+ "cusg is nil"
+ "d"
+ "d16@0:8"
+ "d24@0:8@16"
+ "d32@0:8@16@24"
+ "daemonJobLabel"
+ "daemonOnly"
+ "dataWithJSONObject:options:error:"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSince1970:"
+ "dateWithTimeIntervalSinceNow:"
+ "dayChangedNotificationReceived."
+ "dayChangedNotificationReceived:"
+ "decideMitigation: Fatal counts %u maxKills %ld nonFatalCount %d maxNonFatal %ld enablePenaltyBox %ld for process:%@"
+ "decideMitigation: Fatal violation count (%u >= %ld) so setting non fatal for process:%@"
+ "decideMitigation: IssueType:%s MitigationType:%s MitigationReason:%s cpuFatalCnt:%u cpu_non_fatal_cnt:%u exitsCnt:%u penaltyBoxCnt:%u for process %@"
+ "decideMitigation: No scenarioName to use, logging empty scenario name for violation."
+ "decideMitigation: Non fatal violation count (%u >= %ld) so penalty box time for process:%@"
+ "decideMitigation: Process:%@ is an XPC Service and coalitionName:%@ matches an exempt process so no mitigation"
+ "decideMitigation: Process:%@ is an XPC Service so no mitigations for cpu mon violation"
+ "decideMitigation: Process:%@ is an exempt root daemon so no mitigations"
+ "decideMitigation: Process:%@ is on exempt list so no mitigations"
+ "decideMitigation: Restriction specifies fatal:%d for process:%@"
+ "decideMitigation: process is NULL?"
+ "decideMitigation:withCoalitionName:withReason:"
+ "defaultCenter"
+ "detectAcrossBoots"
+ "detectAndInvokeIssueDetection:slidingWindowStartDate:"
+ "detectIssuesFromStartTime:endDate:withRules:"
+ "detectWithLookbackDuration:"
+ "detectWithLookbackDuration: Finish detection for rule %d: Detected %lu issues"
+ "detectWithLookbackDuration: No rule based detection: PerfPowerServices/safeguards_rule_detection feature flag is off"
+ "detectWithLookbackDuration: Start detection for rule %d: From %@ to %@, without sliding window"
+ "detectorString"
+ "discoverPidForProcessName: Not enough memory"
+ "discoverPidForProcessName: found pid: %d"
+ "discoverPidForProcessName: proc_listpids return negative"
+ "discoverPidForProcessName: unknown pid"
+ "discoverPidForProcessName:withError:"
+ "displayStatusNotifyToken"
+ "durationInSeconds"
+ "earlierDate:"
+ "enableMitigations"
+ "enablePenaltyBox"
+ "endTime"
+ "energySnapshot"
+ "energySnapshotNew"
+ "errorString"
+ "estimatedEnergyDiff"
+ "evaluateRuleInFixedWindow:withStartDate:andEndDate:"
+ "evaluateRuleWithSlidingWindow:withStartDate:andEndDate:"
+ "eventHistory"
+ "exempt"
+ "exitMonitorCount"
+ "exitMonitors"
+ "exitsCnt"
+ "fatalMitigatedProcessList"
+ "firstInterval"
+ "firstObject"
+ "forceCPUViolationForProcess"
+ "forceCPUViolationForProcess: found known pid: %d"
+ "forceCPUViolationForProcess: getProcessUUID() failed %d for pid %d"
+ "forceCPUViolationForProcess: unknown pid"
+ "forceCPUViolationForProcess:withHandler:"
+ "forceDetectionWithStartTime:endTime:withHandler"
+ "forceDetectionWithStartTime:endTime:withHandler:"
+ "forceDetectorViolationForProcess"
+ "forceDetectorViolationForProcess: cannot find process name identifier for processName: %@"
+ "forceDetectorViolationForProcess: cannot find processManager"
+ "forceDetectorViolationForProcess:withHandler:"
+ "forceMidnightRoutineWithHandler"
+ "forceMidnightRoutineWithHandler:"
+ "forceMitigation: Force mitigation %@, cpuThreshold %@, cpuTimeWindow %@ penaltyBoxDuration %@ for process: %@"
+ "forceMitigation: Penalty box not enabled for process:%@"
+ "forceMitigation: process: %@ already in penalty box"
+ "forceMitigation: process: %@ already out of penalty box"
+ "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:"
+ "forceMitigationSuggestion"
+ "generateIPSFileForProcess:"
+ "generateIPSFileForProcess: Generating ips file for process:%@ (%d)"
+ "generateIPSFileForProcess: unknown mitigationType %lld for process:%@ (%d)"
+ "generateIPSFileForProcess: violation path not found for process:%@ (%d)"
+ "generateMetadataForDrain:cpuPercentage:detectionLookbackDuration:"
+ "generatePayloadWithMetadata:triggeredDetection:triggeredType:"
+ "genericCPUDetectorProcessDenyList"
+ "genericCPUDetectorProcessRegexDenyList"
+ "getAPWakeIntervalListWithStartDate Query:%@"
+ "getAPWakeIntervalListWithStartDate:andEndDate:"
+ "getCPUIssueStartEndTime:valueThreshold:"
+ "getCPUIssueWithMitigationSuggestionForCoalitionID:withLaunchdName:fromStartDate:toEndDate:byRule:"
+ "getCPUPercentageIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:"
+ "getCoalitionID: proc_pidinfo(PROC_PIDCOALITIONINFO) failed %d for pid %d"
+ "getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:"
+ "getDefaultsWithHandler:"
+ "getDetectionLookbackDuration"
+ "getDeviceBootTime"
+ "getDrainPercentage:"
+ "getInfoForProcess:"
+ "getInfoForProcess: Could not locate CSProcess for process:%@"
+ "getInfoForProcess: getpriority(PRIO_DARWIN_RUNAWAY_MITIGATION) failed %d (%s) for process:%@ (%d)"
+ "getInfoForProcess: nil process passed in?"
+ "getInfoForProcess:withHandler:"
+ "getMitigationPolicyWithHandler"
+ "getMitigationPolicyWithHandler:"
+ "getMitigationTypeString:withStringSize:withMitigationType:withPenaltyBoxEndTime:"
+ "getMonitoredList"
+ "getMonitoredListWithHandler:"
+ "getMonitoredListWithHandler: Could not locate CSProcess for process:%@"
+ "getMonitoredListWithHandler: getInfoForProcess returned NULL for process:%@"
+ "getMonitoredListWithHandler: monitoredList is NULL?"
+ "getMonotonicTime:"
+ "getPenaltyListWithHandler:"
+ "getPenaltyListWithHandler: Could not locate CSProcess for nsUUID:%@"
+ "getPenaltyListWithHandler: getInfoForProcess returned NULL for process:%@"
+ "getPenaltyListWithHandler: penaltyList is NULL?"
+ "getPidsForCoalitionID:"
+ "getProcessForPID: Skipping processNameIdentifier: %@ because its CSProcess is NULL?"
+ "getProcessForProcessName:"
+ "getProcessForUUID:"
+ "getProcessPathForPID:"
+ "getProcessPathForPID: proc_pidinfo failed with errno %d for pid %d"
+ "getProcessUUID: proc_pidinfo(PROC_PIDUNIQIDENTIFIERINFO) failed %d for pid %d"
+ "getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:"
+ "getProcessesForCoalitionID:withStartDate:andEndDate:andDeviceBootDate:andCPURatio:"
+ "getSystemTime:"
+ "getTotalBatteryDrainWithStartDate:andEndDate:"
+ "getTotalCPUTimeWithStartDate:andEndDate:"
+ "getTriggerInterval"
+ "getTriggerIntervalWithHandler:"
+ "getUnpluggedIntervalListWithStartDate:andEndDate:"
+ "getValueOfMetric:startDate:endDate:"
+ "globalOverridePenaltyBoxDuration"
+ "handleCPUDetectionViolation: process is NULL?"
+ "handleCPUDetectionViolation: start:%f end:%f"
+ "handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:"
+ "handleDetectedIssues:"
+ "handleDetectedIssues: Found issues with rule %d issue %@ for process %@ with coalitionID: %llu from time %s to %s"
+ "handleDetectedIssues: Skip CSMitigationManager to handleDetectorViolation for this issue with reasion: %d"
+ "handleDetectedIssues: handleDetectorViolation() returned an error. MitigationDecisionType: %s MitigationDecisionReason: %s errorString <%@> for process %@"
+ "handleDetectionViolation: Killed %d out of %d pids that matched coalitionID %llu with final retVal %d for process:%@"
+ "handleDetectionViolation: No mitigations for process:%@"
+ "handleDetectionViolation: Pending backgroundQoS for process:%@ because no pids match coalitionID %lld"
+ "handleDetectionViolation: Pending backgroundQoS for process:%@ because process not running"
+ "handleDetectionViolation: Skip kill for process:%@ because no pids match coalitionID %lld"
+ "handleDetectionViolation: Skip kill for process:%@ because process not running"
+ "handleDetectionViolation: known violation for process:%@"
+ "handleDetectionViolation: no mitigation for scheduled intensive activity for process:%@."
+ "handleDetectionViolation: no mitigation while charging for process:%@"
+ "handleDetectionViolation: process is NULL?"
+ "handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "handleDetectorViolation:"
+ "handleDetectorViolation: Could not find CSProcess for process:%@"
+ "handleDetectorViolation: Invalid time stamps (endTime:%f < startTime:%f) for process:%@"
+ "handleDetectorViolation: Updating issue.lastPID from %d to %d for process:%@"
+ "handleDetectorViolation: issue.lastPUUID is Null or empty string?"
+ "handleDisplayStateChanged:"
+ "handleDisplayStateChanged: Display change to OFF"
+ "handleDisplayStateChanged: Display change to ON"
+ "handlePowerStateChanged"
+ "handlePowerStateChanged: Charging change to OFF"
+ "handlePowerStateChanged: Charging change to ON"
+ "handleProcessStart: Could not find CSProcess for process:%@"
+ "handleProcessStart: IssueType:%s MitigationType:%s MitigationReason:%s cpuFatalCnt:%u cpu_non_fatal_cnt:%u exitsCnt:%u penaltyBoxCnt:%u for process %@"
+ "handleProcessStart:withMitigationReason:"
+ "handleViolationByProcess: Failed to get CSProcess for logging violation for pid %llu???"
+ "handleViolationByProcess: Failed to get CSProcessManager for logging violation for pid %llu???"
+ "handleViolationByProcess: Failed to get mitigationManager for process %@ (%llu)???"
+ "handleViolationByProcess: IssueType:%s MitigationType:%s MitigationReason:%s cpuFatalCnt:%u cpu_non_fatal_cnt:%u exitsCnt:%u penaltyBoxCnt:%u estimatedEnergyDiff:%u date:%@ for process %@ (%llu)"
+ "handleViolationByProcess: No ProcessIdentifier for process %@ (%llu)???"
+ "handleViolationByProcess: No procName to use for logging violation."
+ "handleViolationByProcess: No scenarioName to use, logging empty scenario name for violation for pid %llu."
+ "handleViolationByProcess: Received %sCPU violation: %@[%llu] (%@) used %.2f seconds of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2f seconds over %lld seconds."
+ "handleViolationByProcess: Violation not from us? isFatal (%d), savedTimeWindow (%lld) == limitWindow (%lld), savedThreshold (%llu) == limitValue (%lld) for process %@ (%llu)"
+ "handleViolationByProcess: getProcessUUID() failed %d for pid %llu"
+ "handleViolationByProcess: ignore violation for exempt scheduled activity for process %@ (%llu)."
+ "handleViolationByProcess: ignore violation in plugged-in state for process %@ (%llu)."
+ "i24@0:8@\"CSProcess\"16"
+ "i24@0:8@16"
+ "i28@0:8@16C24"
+ "i28@0:8i16^Q20"
+ "i32@0:8@16^@24"
+ "i32@0:8f16f20i24B28"
+ "i56@0:8@16Q24^C32^C40^@48"
+ "i60@0:8@16Q24C32^C36^C44^@52"
+ "identiferForPID: Skipping processNameIdentifier: %@ because its CSProcess is NULL?"
+ "inPenaltyBox"
+ "initWithBytes:length:encoding:"
+ "initWithData:encoding:"
+ "initWithFilePath:"
+ "initWithIdentifier:andLaunchdName:andIssueType:andStartTime:andEndTime:"
+ "initWithIdentifier:andProcessName:andIssueType:andStartTime:andEndTime:"
+ "initWithIntervals:"
+ "initWithScalarMetric:andNormalizerMetric:andComparator:andValue:"
+ "initWithStartTime:endTime:"
+ "initWithStartTime:endTime:value:"
+ "initWithStartTime:endTime:value:label:"
+ "initWithUUIDBytes:"
+ "initWithUUIDString:"
+ "initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:"
+ "intersectWithIntervalList:"
+ "intersectsSet:"
+ "intervalArray"
+ "intervalAtIndex:"
+ "isAppleXPCServiceWithRBS: Error grabbing RBSProcessHandle (pid%i) to perform XPC Service check %@"
+ "isAppleXPCServiceWithRBS:andPID:"
+ "isXPCService"
+ "isXPCServiceExempt:"
+ "issueDetector"
+ "killProcess: Killing process:%@ (%llu)"
+ "killProcess: terminate_with_payload failed %d (%s) for process:%@ (%llu)"
+ "killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "label"
+ "lastCoalitionID"
+ "lastInterval"
+ "lastObject"
+ "lastPID"
+ "lastPUUID"
+ "lastPid"
+ "lastTriggerTimerDate"
+ "laterDate:"
+ "launchdName"
+ "length"
+ "levelForFactor:withNamespaceName:"
+ "localTimeZone"
+ "logCPUViolationToPowerLog: No scenarioName to use, logging empty scenario name for violation."
+ "logCPUViolationToPowerLog: Sending %s violation fromPowerExceptions (%s) for process %@ (%llu) to Power Log"
+ "logCPUViolationToPowerLog: process is NULL?"
+ "logCPUViolationToPowerLog:pid:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:"
+ "logCPUViolationToPowerLogWithPayload payload: %@"
+ "logIssuesToPowerLogWithPayload payload: %@"
+ "logIssuesToPowerLogWithPayload:"
+ "logMitigationAsSignpost Unknown mitigationType: %d for process:%s"
+ "logMitigationAsSignpost:withPid:withIssueType:withMitigationType:withReason:withPenaltyBoxEndTime:"
+ "logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:"
+ "logPenaltyBoxListAsSignposts"
+ "logPenaltyBoxListAsSignposts: Could not locate CSProcess for nsUUID:%@"
+ "logPenaltyBoxListAsSignposts: Unexpected count %d"
+ "logPenaltyBoxListAsSignposts: penaltyList is NULL?"
+ "logPenaltyBoxToPowerLogForProcess: No scenarioName to use, logging empty scenario name for violation."
+ "logTriggerToPPS:cpuPercentage:triggeredDetection:triggeredType:detectionLookbackDuration:"
+ "mainThresholdValue"
+ "maxNumberKills"
+ "midnightRoutine"
+ "mitigateXPCServices"
+ "mitigationDecisionReason"
+ "mitigationDecisionType"
+ "mitigationManager"
+ "mitigationSuggestion"
+ "mitigationSuggestionReason"
+ "mitigationsWhilePluggedIn"
+ "mobile"
+ "modifyContextForIdentifier:withState:"
+ "modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:"
+ "modifyProcessInfo: Could not locate CSProcess for process:%@"
+ "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:"
+ "modifyRestrictionsByProcessPerScenario: process:%@"
+ "modifyRestrictionsByProcessPerScenario:withHandler:"
+ "modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:"
+ "modifyTriggerInterval:"
+ "monitorFilterBitMap"
+ "monitorForExitWithPID:"
+ "mutableCopy"
+ "normalizerMetric"
+ "notify_register_dispatch(displayStatus) failed %d"
+ "notify_register_dispatch(kIOPSNotifyPowerSource) failed %d"
+ "now"
+ "numberWithLong:"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLong:"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "openConnection"
+ "overridden"
+ "pausePIDPolling"
+ "penaltyBoxCnt"
+ "penaltyBoxCoalitionIDs"
+ "penaltyBoxCoalitionIDs/timeStamp"
+ "penaltyBoxDurationMins"
+ "penaltyBoxEnabled"
+ "penaltyBoxEndTime"
+ "penaltyBoxPending"
+ "penaltyBoxPolicy"
+ "penaltyBoxProcesses"
+ "penaltyBoxRemainingTimeSecs"
+ "penaltyBoxTimer"
+ "penaltyBoxTimerRunning"
+ "performCleanupOnExitOnPID:"
+ "performPowerlogQuery:"
+ "performQuery:"
+ "pid/priority"
+ "policyMitigationsEnabled"
+ "policyMitigationsEnabled: Not an internal build so mitigations always disabled"
+ "policyMitigationsEnabled: Trials says no mitigations"
+ "policyMitigationsEnabled: Trials says to mitigate"
+ "policyMitigationsEnabled: invalid _trialsMitigationsEnabled value (%d)"
+ "pollPIDs: Allowing target process of %@ (%d)"
+ "pollPIDs: Allowing target process of %@ (%d) in newProcessesList"
+ "pollPIDs: Auto exempting root process: %@ (%d)"
+ "pollPIDs: Not enough memory"
+ "pollPIDs: Process %@ was PID: %d before and no exit handler, assume pid exited"
+ "pollPIDs: Process %@ was PID: %d before. CSProcess exit handler should fire soon."
+ "pollPIDs: Process:%@ found another new duplicate process with pid:%d"
+ "pollPIDs: Process:%@ found duplicate process with pid:%d"
+ "pollPIDs: Process:%@ seems to have relaunched with pid:%d"
+ "pollPIDs: Releasing process:%@ (%d) since it was left in penalty box"
+ "pollPIDs: Skipping pid: %d since it does not match current filter map 0x%x"
+ "pollPIDs: Skipping processNameIdentifier: %@ because its CSProcess is NULL?"
+ "pollPIDs: Start, interval: %f"
+ "pollPIDs: fullProcessNameForPid failed for pid: %i"
+ "pollPIDs: getProcessUUID() failed %d, so skipping pid: %d"
+ "pollPIDs: proc_listpids return negative"
+ "pollPIDs: setpriority(PRIO_DARWIN_RUNAWAY_MITIGATION) failed %d (%s) for process:%@ (%d)"
+ "pollPIDs: totalPIDs: %d skippedPIDs: %d queryRBSPIDs: %d monitorPIDs: %d xpcServicesPIDs: %d"
+ "pollingTimer"
+ "pollingTimerActive"
+ "powerStatusNotifyToken"
+ "powerlogDBReader"
+ "previousPIDkeys"
+ "previousPIDs"
+ "previousPIDs/CoalitionID"
+ "process1"
+ "process2"
+ "processName"
+ "processNameForIdentifier:"
+ "processTimerFiredAction"
+ "processTimerFiredAction: Querying DB with time window from: %@ to %@"
+ "processesAllowList"
+ "processesDenyList"
+ "processesRegexAllowList"
+ "processesRegexDenyList"
+ "putIntoPenaltyBoxForCSProcess:coalitionID:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "putIntoPenaltyBoxForProcess: PenaltyBox for %d out of %d pids that matched coalitionID %llu with final ret %d for process:%@"
+ "putIntoPenaltyBoxForProcess: Process:%@ already in penalty box"
+ "putIntoPenaltyBoxForProcess: Put process:%@ into penalty box. Reason: %s"
+ "putIntoPenaltyBoxForProcess: Resuming penalty box timer in 60 seconds"
+ "putIntoPenaltyBoxForProcess: no pids matching coalitionID for process:%@"
+ "putIntoPenaltyBoxForProcess: process is NULL?"
+ "putIntoPenaltyBoxForProcess: setpriority(PRIO_DARWIN_RUNAWAY_MITIGATION) failed %d (%s) for process:%@ (%d)"
+ "q24@?0@\"CSIssue\"8@\"CSIssue\"16"
+ "rangeOfFirstMatchInString:options:range:"
+ "rangeOfString:options:"
+ "recordTerminationForPID: Process not found for exited pid (%d)"
+ "recordTerminationForPID: Process:%@ (%d) exited"
+ "registerForDayChangedNotification"
+ "regularExpressionWithPattern:options:error:"
+ "releaseForProcess: clearMonitorForPID failed %d on process:%@ (%d)"
+ "removeAllObjects"
+ "removeAllProcessesFromPenaltyBox"
+ "removeObjectAtIndex:"
+ "removeProcessFromPenaltyBox: Remove process:%@ from penalty box. Reason: %s"
+ "removeProcessFromPenaltyBox: getpriority(PRIO_DARWIN_RUNAWAY_MITIGATION) failed %d (%s) priority %d for process:%@ (%d)"
+ "removeProcessFromPenaltyBox: setpriority(PRIO_DARWIN_RUNAWAY_MITIGATION) failed %d (%s) for process:%@ (%d)"
+ "removeProcessFromPenaltyBox:forReason:"
+ "removeTrackedPID:"
+ "removeTrackedPID: Too many pids (> %d) so remove previous pid %d from process %@"
+ "resetState"
+ "resumePIDPolling"
+ "reverseObjectEnumerator"
+ "rootDaemon"
+ "rule"
+ "ruleID"
+ "rules"
+ "safeguards_disable_XPCServices"
+ "safeguards_mitigation_pluggedin"
+ "safeguards_penaltybox"
+ "safeguards_rule_detection"
+ "savedPIDPollingInterval"
+ "savedTriggerInterval"
+ "scalarMetric"
+ "scheduledIntensiveProcesses"
+ "select distinct AppBundleId as bundleId from PLApplicationAgent_EventNone_AllApps"
+ "setAffectedProcesses:"
+ "setBand80Mitigations:"
+ "setBand80Processes:"
+ "setBand80ProcessesSet:"
+ "setBand80Restriction:"
+ "setBand95Mitigations:"
+ "setBand95Processes:"
+ "setBand95ProcessesSet:"
+ "setBand95Restriction:"
+ "setCoalitionID:"
+ "setComparator:"
+ "setConditions:"
+ "setConn:"
+ "setCpuEnergy:"
+ "setCpuEnergyBilledToMe:"
+ "setCpuEnergyBilledToOthers:"
+ "setCpuFatalCnt:"
+ "setCpuMonitored:"
+ "setCpuNonFatalCnt:"
+ "setDaemonOnly:"
+ "setDateFormat:"
+ "setDetectAcrossBoots:"
+ "setDetectorString:"
+ "setDisplayStatusNotifyToken:"
+ "setEndTime:"
+ "setEnergySnapshot:"
+ "setEnergySnapshotNew:"
+ "setErrorString:"
+ "setEstimatedEnergyDiff:"
+ "setEventHistory:"
+ "setExitMonitors:"
+ "setExitsCnt:"
+ "setFatalMitigatedProcessList:"
+ "setForceMitigationSuggestion:"
+ "setGenericCPUDetectorProcessDenyList:"
+ "setGenericCPUDetectorProcessRegexDenyList:"
+ "setInPenaltyBox:"
+ "setIntervalArray:"
+ "setIssueDetector:"
+ "setLabel:"
+ "setLastPID:"
+ "setLastPUUID:"
+ "setLastTriggerTimerDate:"
+ "setLaunchdName:"
+ "setMainThresholdValue:"
+ "setMitigationDecisionReason:"
+ "setMitigationDecisionType:"
+ "setMitigationManager:"
+ "setMitigationSuggestion:"
+ "setMitigationSuggestionReason:"
+ "setMonitorFilterBitMap:"
+ "setNormalizerMetric:"
+ "setOverridden:"
+ "setPenaltyBoxCnt:"
+ "setPenaltyBoxCoalitionIDs:"
+ "setPenaltyBoxDurationMins:"
+ "setPenaltyBoxEnabled:"
+ "setPenaltyBoxEndTime:"
+ "setPenaltyBoxPending:"
+ "setPenaltyBoxPolicy:"
+ "setPenaltyBoxProcesses:"
+ "setPenaltyBoxTimer:"
+ "setPenaltyBoxTimerRunning:"
+ "setPollingTimer:"
+ "setPollingTimerActive:"
+ "setPowerStatusNotifyToken:"
+ "setPowerlogDBReader:"
+ "setPreviousPIDkeys:"
+ "setPreviousPIDs:"
+ "setProcessName:"
+ "setProcessesAllowList:"
+ "setProcessesDenyList:"
+ "setProcessesRegexAllowList:"
+ "setProcessesRegexDenyList:"
+ "setRootDaemon:"
+ "setRule:"
+ "setRuleID:"
+ "setRules:"
+ "setSavedPIDPollingInterval:"
+ "setSavedTriggerInterval:"
+ "setScalarMetric:"
+ "setScheduledIntensiveProcesses:"
+ "setSlidingWindowStepSize:"
+ "setStartTime:"
+ "setThreshold:overTimeWindow:forPID:withFatalEffect:"
+ "setTime:"
+ "setTimeZone:"
+ "setTrackedPIDkeys:"
+ "setTrackedPIDs:"
+ "setTrialsMitigationsEnabled:"
+ "setTriggerInterval:"
+ "setTriggerManager:"
+ "setTriggerTimer:"
+ "setUnknownScheduledIntensiveProcesses:"
+ "setUseSlidingWindow:"
+ "setUuid:"
+ "setValue:"
+ "setViolationDetectorString:"
+ "setViolationEndTime:"
+ "setViolationLimitValue:"
+ "setViolationLimitWindow:"
+ "setViolationObservationWindow:"
+ "setViolationObservedValue:"
+ "setViolationPath:"
+ "setViolationPid:"
+ "setWindowSize:"
+ "setXpcService:"
+ "sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:"
+ "signpostCategory"
+ "slidingWindowStepSize"
+ "snapshotCPUEnergy"
+ "snapshotCPUEnergy:"
+ "sortedArrayUsingComparator:"
+ "startTime"
+ "string:matchesAnyRegexInArray:"
+ "stringByAppendingString:"
+ "stringByStandardizingPath"
+ "stringFromDate:"
+ "stringValue"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "sum"
+ "system"
+ "testDetectWithLookbackDuration"
+ "testHandleDetectedIssues"
+ "time"
+ "timeIntervalSince1970"
+ "timeIntervalSinceDate:"
+ "timeWeightedSum"
+ "timestamp"
+ "timestampStart"
+ "trackedPIDkeys"
+ "trackedPIDs"
+ "trackedPIDs/CoalitionID"
+ "trialsMitigationsEnabled"
+ "triggerInterval"
+ "triggerManager"
+ "triggerTimer"
+ "unexpected cpuEnergyTotal: %f < 0"
+ "unexpected energy values: %f %f %f"
+ "unknownScheduledIntensiveProcesses"
+ "updateCPUBuffer:"
+ "updateCoalitionEntries:withHandler:"
+ "updateScheduledIntensiveContext:"
+ "useSlidingWindow"
+ "uuid"
+ "v108@0:8@16Q24@32{mach_timespec=Ii}40q48q56q64q72B80q84q92@100"
+ "v12@?0i8"
+ "v20@0:8C16"
+ "v20@0:8I16"
+ "v20@0:8S16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8d16"
+ "v24@0:8{mach_timespec=Ii}16"
+ "v28@0:8@16C24"
+ "v28@0:8C16d20"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v36@0:8C16d20d28"
+ "v36@0:8i16i20i24i28i32"
+ "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?Bd@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16i24C28C32C36"
+ "v48@0:8*16Q24q32Q40"
+ "v48@0:8@16^q24^q32^q40"
+ "v52@0:8@16Q24C32C36C40Q44"
+ "v64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v84@0:8@16Q24Q32{mach_timespec=Ii}40q48q56q64q72B80"
+ "v96@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80@?<v@?@\"NSError\">88"
+ "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
+ "v96@0:8C16@20Q28@36Q44d52d60C68^C72^C80^@88"
+ "value"
+ "valueForKey:"
+ "violationDetectorString"
+ "violationEndTime"
+ "violationLimitValue"
+ "violationLimitWindow"
+ "violationObservationWindow"
+ "violationObservedValue"
+ "violationPath"
+ "violationPid"
+ "windowSize"
+ "xpc.%@"
+ "xpcService"
+ "xpcServiceIdentifier"
+ "yyyy-MM-dd HH:mm:ss"
+ "{mach_timespec=\"tv_sec\"I\"tv_nsec\"i}"
+ "{mach_timespec=Ii}16@0:8"
- "\f"
- "!21"
- "Applying default restrictions for process:%@"
- "Applying restrictions:%@ to process:%@"
- "Attempted applying thresholds on invalid PID for process:%@ (%d)"
- "Attempted cleanup on Process:%@ with no currentPID"
- "Attempted monitoring on invalid PID:%d for process %@"
- "Attempted setting invalid PID for Process:%@"
- "B24@0:8@\"CSProcess\"16"
- "CPULimit"
- "CSProcess with nameIdentifier: %@, pid: %d"
- "Clearing current restrictions for process:%@"
- "Configuring cpuMonitor with cpuThreshold: %@, timeWindow:%@, fatal:%s, limit_cpu_usage:%s for process:%@ (%d)"
- "Could not locate CSProcess object for processName:%@ so ignoring this violation"
- "Could not locate Process: %@ in _restrictionsByProcessPerScenario"
- "Could not locate Scenario:%@ for Process:%@ in _restrictionsByProcessPerScenario"
- "Determining restrictions for process:%@ in scenario:%@"
- "Failed to apply default restriction:%@ to process:%@."
- "Failed to apply default restrictions to process:%@ (restrictions already exists)"
- "Failed to apply restriction:%@ to process:%@, skipping any further restrictions"
- "Failed to get CSProcessManager for logging violation???"
- "Failed to release restriction:%@ for process:%@"
- "Failed to release restriction:%@ for process:%@, skipping any further restrictions"
- "Fatal violation count (%llu >= %ld) so setting non fatal for process:%@ (%d)"
- "Global CPU monitoring percentage has been changed to %ld"
- "Global CPU monitoring time window has been changed to %ld"
- "Global Max cpu usage limit percentage has been changed to %ld"
- "Global overriding cpu threshold to be (%ld) for process:%@ (%d)"
- "Global overriding cpu time window to be (%ld) for process:%@ (%d)"
- "Global overriding cpu usage limit threshold to be (%ld) for process:%@ (%d)"
- "IssueType:%lld MitigationType:%lld MitigationReason:%lld cpu_fatal_cnt:%llu cpu_non_fatal_cnt:%llu exits_cnt:%llu for process %@ (%llu)"
- "LimitCPUTimeWindow"
- "Max cpu usage limit has been enabled with %ld"
- "Max number of fatal violations has been changed to %ld"
- "Max number of non fatal violations has been changed to %ld"
- "No procName to use for logging violation."
- "No scenarioName to use, logging empty scenario name for violation."
- "Non fatal violation count (%llu >= %ld) so setting max cpu limit for process:%@ (%d)"
- "Not an internal build, Safeguards are currenlty internal-only"
- "Overriding cpu threshold to be (%ld) for process:%@ (%d)"
- "Overriding cpu time window to be (%ld) for process:%@ (%d)"
- "Overriding cpu usage limit threshold to be (%ld) for process:%@ (%d)"
- "PPSCreateTelemetryIdentifier"
- "PPSSendTelemetry"
- "PowerExceptionEnableLimitCPUUsage"
- "PowerExceptionGlobalCPUPercentage"
- "PowerExceptionGlobalCPUTimeWindow"
- "PowerExceptionGlobalLimitCPUPercentage"
- "PowerExceptionMaxKills"
- "PowerExceptionMaxNonFatal"
- "Process %d exited"
- "Process:%@ (%d) exited"
- "ProcessIdentifier lookup failed. Ignoring report since this process isn't tracked by the system."
- "Received %sCPU violation: %@[%llu] (%@) used %.2f seconds of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2f seconds over %lld seconds."
- "Restrictions are unchanged for process:%@ for scenario:%@"
- "Scenarios that remain active after deounce: %@"
- "Successfully applied default restriction to process: %@"
- "Successfully applied restriction: %@ to process: %@"
- "T@\"NSMutableDictionary\",&,N,V_allProcessesMap"
- "T@\"NSMutableDictionary\",&,N,V_currentPIDList"
- "T@\"NSMutableDictionary\",&,N,V_processNameIdentiferByName"
- "T@\"NSMutableDictionary\",&,N,V_processNameIdentiferByPID"
- "T@\"NSNumber\",&,N,V_cpuThreshold"
- "T@\"NSNumber\",&,N,V_cpuTimeWindow"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_processExitMonitor"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
- "T@\"NSSet\",&,N,V_enrolledProcessesSet"
- "T@\"NSSet\",&,N,V_exemptProcessesSet"
- "TB,N,V_cpuIsFatal"
- "TB,N,V_cpuUsageLimitSet"
- "TB,N,V_exemptFromMitigations"
- "TB,N,V_needClearRestrictions"
- "TB,N,V_onlyMonitorDaemons"
- "TB,N,V_resetNonFatalCPUMonitor"
- "TB,N,V_runInternalOnly"
- "TQ,N,V_cpu_fatal_cnt"
- "TQ,N,V_cpu_nonfatal_cnt"
- "TQ,N,V_exits_cnt"
- "TQ,N,V_issueType"
- "TQ,N,V_mitigationReason"
- "TQ,N,V_mitigationType"
- "Tf,N,V_PIDPollingInterval"
- "Ti,N,V_currentPID"
- "Tq,V_enableLimitCPUUsage"
- "Tq,V_globalOverrideCPUPercentage"
- "Tq,V_globalOverrideCPUTimeWindow"
- "Tq,V_globalOverrideLimitCPUPercentage"
- "Tq,V_maxNumberOfKills"
- "Tq,V_maxNumberOfNonfatal"
- "Violation not from us? savedFatal (%d) == isFatal (%d), savedTimeWindow (%lld) == limitWindow (%lld), savedThreshold (%llu) == limitValue (%lld) for processName:%@"
- "_cpuIsFatal"
- "_cpuUsageLimitSet"
- "_cpu_fatal_cnt"
- "_cpu_nonfatal_cnt"
- "_currentPID"
- "_enableLimitCPUUsage"
- "_exits_cnt"
- "_globalOverrideCPUPercentage"
- "_globalOverrideCPUTimeWindow"
- "_globalOverrideLimitCPUPercentage"
- "_initWithEnrolledProcesses:andExemptions:"
- "_maxNumberOfKills"
- "_maxNumberOfNonfatal"
- "_onlyMonitorDaemons"
- "_processExitMonitor"
- "_runInternalOnly"
- "_timer"
- "com.apple.cloudphotod "
- "com.apple.computesafeguards"
- "com.apple.findmy.findmybeaconingd"
- "com.apple.itunesstored"
- "com.apple.mediaanalysisd.service"
- "com.apple.nanomapscd"
- "com.apple.storekitd"
- "com.apple.syncdefaultsd"
- "com.apple.wirelessinsightsd "
- "cpuIsFatal"
- "cpuUsageLimitSet"
- "cpu_fatal_cnt"
- "cpu_hog"
- "cpu_nonfatal_cnt"
- "currentPID"
- "enableLimitCPUUsage"
- "exits_cnt"
- "forceMitigation: Force mitigation %@ for process: %@"
- "forceMitigation:forProcess:withHandler:"
- "getCountsForProcess: Could not locate CSProcess for process:%@"
- "getCountsForProcess:WithHandler:"
- "globalOverrideLimitCPUPercentage"
- "i36@0:8f16f20i24B28B32"
- "longForKey:ifNotSet:"
- "maxNumberOfKills"
- "modifyProcessCounts: Could not locate CSProcess for process:%@"
- "modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:"
- "modifyRestrictionsByProcessPerScenario:"
- "modifyTargetProcess:withPercentage:withSeconds:withLimit:"
- "monitorForExit"
- "name"
- "onlyMonitorDaemons"
- "performCleanupOnExit"
- "pollPIDs: %@ was PID: %d before, is %d now. CSProcess exit handler should fire soon."
- "pollPIDs: Allowing _overrideProcess of %@ (%d)"
- "pollPIDs: Process:%@ (%d) is not explicitly enrolled, it will get default restrictions."
- "pollPIDs: Process:%@ (%d) seems to have relaunched since saved pid is PID_NOT_RUNNING"
- "pollPIDs: Skipping pid: %d since fullProcessNameForPid failed"
- "pollPIDs: Skipping pid: %d since it is not a daemon"
- "pollPIDs: totalPIDs: %d skippedPIDs: %d queryRBSPIDs: %d monitorPIDs: %d"
- "processExitMonitor"
- "runInternalOnly"
- "setCpuIsFatal:"
- "setCpuUsageLimitSet:"
- "setCpu_fatal_cnt:"
- "setCpu_nonfatal_cnt:"
- "setCurrentPID:"
- "setEnableLimitCPUUsage:"
- "setExits_cnt:"
- "setGlobalOverrideCPUPercentage:"
- "setGlobalOverrideCPUTimeWindow:"
- "setGlobalOverrideLimitCPUPercentage:"
- "setMaxNumberOfKills:"
- "setMaxNumberOfNonfatal:"
- "setOnlyMonitorDaemons:"
- "setProcessExitMonitor:"
- "setRunInternalOnly:"
- "setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:"
- "setTimer:"
- "sharedInstanceWithEnrolledProcesses:andExemptions:"
- "softlink:r:path:/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
- "timer"
- "v24@0:8@\"NSDictionary\"16"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"

```

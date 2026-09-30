## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2964.0.64.0.0
-  __TEXT.__text: 0x2f628
+2964.0.107.502.1
+  __TEXT.__text: 0x30040
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x2754
+  __TEXT.__objc_methlist: 0x27e4
   __TEXT.__const: 0x260
   __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__cstring: 0x345c
-  __TEXT.__oslogstring: 0x6a71
-  __TEXT.__unwind_info: 0x890
+  __TEXT.__cstring: 0x34aa
+  __TEXT.__oslogstring: 0x6c01
+  __TEXT.__unwind_info: 0x898
   __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x700c
-  __TEXT.__objc_methtype: 0xe4a
-  __TEXT.__objc_stubs: 0x3e80
+  __TEXT.__objc_methname: 0x71b6
+  __TEXT.__objc_methtype: 0xef9
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1768
+  __DATA_CONST.__objc_selrefs: 0x17b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0xac8
+  __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x3b30
-  __AUTH_CONST.__objc_intobj: 0x378
+  __AUTH_CONST.__objc_const: 0x3bd0
+  __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x31c
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x318
   __DATA.__common: 0x48
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x148
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: FB72F3B4-298D-35AA-AFEF-3026B8D3552E
-  Functions: 1152
-  Symbols:   3569
-  CStrings:  2627
+  UUID: 6CB0985D-95B9-31A7-AB5E-FDE9BCA2D008
+  Functions: 1170
+  Symbols:   3620
+  CStrings:  2652
 
Symbols:
+ +[CSProcessManager sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]
+ -[CSDetectionRule initDaemonOnly]
+ -[CSDetectionRule initMaxSlidingLookback]
+ -[CSDetectionRule initSlidingWindowStepSize]
+ -[CSDetectionRule initWindowSize]
+ -[CSDetectionRule setInitDaemonOnly:]
+ -[CSDetectionRule setInitMaxSlidingLookback:]
+ -[CSDetectionRule setInitSlidingWindowStepSize:]
+ -[CSDetectionRule setInitWindowSize:]
+ -[CSIssueDetector resetRuleParameters:withHandler:]
+ -[CSIssueDetector resetRuleParameters:withHandler:].cold.1
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:]
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:].cold.1
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:].cold.2
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:].cold.3
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:].cold.4
+ -[CSIssueDetector setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:].cold.5
+ -[CSProcess policyBitMask]
+ -[CSProcess setPolicyBitMask:]
+ -[CSProcessManager _initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]
+ -[CSProcessManager processPoliciesDict]
+ -[CSProcessManager setProcessPoliciesDict:]
+ -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:]
+ -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:].cold.1
+ -[CSRestrictionDataProvider _processesPoliciesDictWithErrors:].cold.2
+ -[CSRestrictionDataProvider processPolicies]
+ -[CSRestrictionDataProvider processPolicyDict]
+ -[CSRestrictionDataProvider setProcessPolicies:]
+ -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:]
+ -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:].cold.1
+ -[CSRestrictionManager resetRuleParameters:withHandler:]
+ -[CSRestrictionManager setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:]
+ _OBJC_IVAR_$_CSDetectionRule._initDaemonOnly
+ _OBJC_IVAR_$_CSDetectionRule._initMaxSlidingLookback
+ _OBJC_IVAR_$_CSDetectionRule._initSlidingWindowStepSize
+ _OBJC_IVAR_$_CSDetectionRule._initWindowSize
+ _OBJC_IVAR_$_CSProcess._policyBitMask
+ _OBJC_IVAR_$_CSProcessManager._processPoliciesDict
+ _OBJC_IVAR_$_CSRestrictionDataProvider._processPolicies
+ ___136-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:]_block_invoke
+ ___136-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:]_block_invoke.320
+ ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.318
+ ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.290
+ ___95+[CSProcessManager sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:]_block_invoke
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e5_v8?0lr80l8s32l8r88l8s40l8s48l8s56l8s64l8s72l8
+ _getCSProcessPolicies
+ _objc_msgSend$_initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:
+ _objc_msgSend$_processesPoliciesDictWithErrors:
+ _objc_msgSend$initDaemonOnly
+ _objc_msgSend$initMaxSlidingLookback
+ _objc_msgSend$initSlidingWindowStepSize
+ _objc_msgSend$initWindowSize
+ _objc_msgSend$policyBitMask
+ _objc_msgSend$processPolicyDict
+ _objc_msgSend$resetRuleParameters:withHandler:
+ _objc_msgSend$setDaemonOnly:
+ _objc_msgSend$setMaxSlidingLookback:
+ _objc_msgSend$setPolicyBitMask:
+ _objc_msgSend$setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:
+ _objc_msgSend$setSlidingWindowStepSize:
+ _objc_msgSend$setWindowSize:
+ _objc_msgSend$sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:
+ _sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:._sharedInstance
+ _sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:.onceToken
- +[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:]
- -[CSProcess exemptBitMask]
- -[CSProcess exemptFromMitigations]
- -[CSProcess setExemptBitMask:]
- -[CSProcess setExemptFromMitigations:]
- -[CSProcessManager _initWithEnrolledProcesses:andExemptions:andBand95:andBand80:]
- -[CSProcessManager exemptProcessesDict]
- -[CSProcessManager setExemptProcessesDict:]
- -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:]
- -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:].cold.1
- -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:].cold.2
- -[CSRestrictionDataProvider exemptProcessesDict]
- -[CSRestrictionDataProvider exemptProcesses]
- -[CSRestrictionDataProvider setExemptProcesses:]
- -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]
- -[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:].cold.1
- _OBJC_IVAR_$_CSProcess._exemptBitMask
- _OBJC_IVAR_$_CSProcess._exemptFromMitigations
- _OBJC_IVAR_$_CSProcessManager._exemptProcessesDict
- _OBJC_IVAR_$_CSRestrictionDataProvider._exemptProcesses
- ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke
- ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke.318
- ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.316
- ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.288
- ___90+[CSProcessManager sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:]_block_invoke
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8
- _getCSExemptProcesses
- _objc_msgSend$_exemptProcessesDictWithErrors:
- _objc_msgSend$_initWithEnrolledProcesses:andExemptions:andBand95:andBand80:
- _objc_msgSend$exemptBitMask
- _objc_msgSend$exemptFromMitigations
- _objc_msgSend$exemptProcessesDict
- _objc_msgSend$setExemptBitMask:
- _objc_msgSend$setExemptFromMitigations:
- _objc_msgSend$sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:
- _sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:._sharedInstance
- _sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:.onceToken
CStrings:
+ "ExemptedCoalitionName"
+ "Loading process_policies.plist"
+ "Process Policies dictionary missing"
+ "Processes Policy plist failure"
+ "SkipFirstKill"
+ "T@\"NSDictionary\",&,V_processPolicies"
+ "T@\"NSDictionary\",&,V_processPoliciesDict"
+ "TB,V_initDaemonOnly"
+ "TI,V_policyBitMask"
+ "Tf,V_initMaxSlidingLookback"
+ "Tf,V_initSlidingWindowStepSize"
+ "Tf,V_initWindowSize"
+ "U"
+ "_initDaemonOnly"
+ "_initMaxSlidingLookback"
+ "_initSlidingWindowStepSize"
+ "_initWindowSize"
+ "_initWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:"
+ "_policyBitMask"
+ "_processPolicies"
+ "_processPoliciesDict"
+ "_processesPoliciesDictWithErrors:"
+ "com.apple.mobile.installd"
+ "decideMitigation: Fatal counts %u maxKills %ld nonFatalCount %d maxNonFatal %ld enablePenaltyBox %ld policyBitMask 0x%x for process:%@"
+ "decideMitigation: Unknown issueType %d for policyBitMask for Process:%@, assuming exempt "
+ "initDaemonOnly"
+ "initMaxSlidingLookback"
+ "initSlidingWindowStepSize"
+ "initWindowSize"
+ "isXPCServiceExempt: Unknown issueType %d for policyBitMask for coalitionName:%@, assuming exempt "
+ "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:"
+ "policyBitMask"
+ "processPolicies"
+ "processPoliciesDict"
+ "processPolicyDict"
+ "process_policies"
+ "process_policies dictionary missing"
+ "processesPolicies: %@"
+ "resetRuleParameters:withHandler:"
+ "setInitDaemonOnly:"
+ "setInitMaxSlidingLookback:"
+ "setInitSlidingWindowStepSize:"
+ "setInitWindowSize:"
+ "setPolicyBitMask:"
+ "setProcessPolicies:"
+ "setProcessPoliciesDict:"
+ "setRuleParameters: cannot find rule with ID: %@"
+ "setRuleParameters: cannot set daemon only for rule %d to %d, which must be 0 or 1"
+ "setRuleParameters: cannot set max lookback for rule %d to %d, below the min of %d"
+ "setRuleParameters: cannot set window size for rule %d to %d, below the min of %d"
+ "setRuleParameters: cannot set window step size for rule %d to %d, below the min of %d"
+ "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:"
+ "sharedInstanceWithEnrolledProcesses:andProcessPolicies:andBand95:andBand80:"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
+ "v64@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v72@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "xpc.com.apple.PerfPowerServicesSignpostReader"
- "5"
- "Exempt Processes dictionary missing"
- "Loading exempt_processes.plist"
- "T@\"NSDictionary\",&,V_exemptProcesses"
- "T@\"NSDictionary\",&,V_exemptProcessesDict"
- "TB,V_exemptFromMitigations"
- "TI,V_exemptBitMask"
- "_exemptBitMask"
- "_exemptFromMitigations"
- "_exemptProcesses"
- "_exemptProcessesDict"
- "_exemptProcessesDictWithErrors:"
- "_initWithEnrolledProcesses:andExemptions:andBand95:andBand80:"
- "com.apple.sysdiagnosed"
- "decideMitigation: Fatal counts %u maxKills %ld nonFatalCount %d maxNonFatal %ld enablePenaltyBox %ld for process:%@"
- "decideMitigation: Unknown issueType %d for exemptBitMask for Process:%@, assuming exempt "
- "exempt"
- "exemptBitMask"
- "exemptFromMitigations"
- "exemptProcesses"
- "exemptProcesses: %@"
- "exemptProcessesDict"
- "exempt_processes"
- "exempt_processes dictionary missing"
- "isXPCServiceExempt: Unknown issueType %d for exemptBitMask for coalitionName:%@, assuming exempt "
- "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:"
- "setExemptBitMask:"
- "setExemptFromMitigations:"
- "setExemptProcesses:"
- "setExemptProcessesDict:"
- "sharedInstanceWithEnrolledProcesses:andExemptions:andBand95:andBand80:"
- "v64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"

```

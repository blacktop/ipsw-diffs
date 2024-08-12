## HumanUnderstandingEvidence

> `/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence`

```diff

-108.1.0.0.0
+111.0.2.0.0
   __TEXT.__text: 0x4c04
   __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_methlist: 0x14c

   __TEXT.__objc_methtype: 0x746
   __TEXT.__objc_stubs: 0x200
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 164
-  Symbols:   125
-  CStrings:  0
+  Symbols:   133
+  CStrings:  124
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "N,V_scenarioCriteria"
+ "SDictionary\",&,V_scenarios"
+ "T@\"<CSRestriction>\",&,V_defaultRestriction"
+ "T@\"CSContextStore\",&,N,V_contextStore"
+ "T@\"CSProcessManager\",&,V_processManager"
+ "T@\"CSRestrictionManager\",&,N,V_restrictionsManager"
+ "T@\"NSArray\",&,N,V_restrictions"
+ "T@\"NSDictionary\",&,V_restrictionsByProcessPerScenario"
+ "T@\"NSDictionary\",&,V_scenariosMap"
+ "T@\"NSMutableDictionary\",&,N,V_affectedScenarioByContextIdentifier"
+ "T@\"NSMutableDictionary\",&,N,V_allProcessesMap"
+ "T@\"NSMutableDictionary\",&,N,V_allScenariosByIdentifier"
+ "T@\"NSMutableDictionary\",&,N,V_currentContext"
+ "T@\"NSMutableDictionary\",&,N,V_processNameIdentiferByPID"
+ "T@\"NSMutableDictionary\",&,V_currentRestrictionsByProcess"
+ "T@\"NSMutableDictionary\",&,V_processesAffectedByScenarioMap"
+ "T@\"NSMutableSet\",&,N,V_activeScenarios"
+ "T@\"NSMutableSet\",&,V_monitors"
+ "T@\"NSNumber\",R,N,V_timeWindow"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_mainQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_processMonitor"
+ "T@\"NSSet\",&,N,V_activeScenariosLastEvaluation"
+ "T@\"NSSet\",&,N,V_activeScenariosLastPublished"
+ "T@\"NSSet\",&,N,V_enrolledProcessesSet"
+ "T@\"NSSet\",&,N,V_exemptProcessesSet"
+ "T@\"NSSet\",&,V_currentActiveScenarios"
+ "T@\"NSSet\",&,V_exemptProcesses"
+ "T@\"NSSet\",&,V_processes"
+ "TB,N,V_onlyMonitorDaemons"
+ "TB,N,V_runInternalOnly"
+ "Ti,N,V_currentPID"
+ "WithPlatformKeyCredentialAssertion:"
+ "_activeScenariosLastEvaluation"
+ "_activeScenariosLastPublished"
+ "_addContextStoreObserverForIdentifier:"
+ "_affectedScenarioByContextIdentifier"
+ "_allProcessesMap"
+ "_allScenariosByIdentifier"
+ "_buildScenariosMap"
+ "_cpuThreshold"
+ "_cpuTimeRestrictionWithBand:errors:"
+ "_cpuTimeRestrictionWithProperties:errors:"
+ "_cpuViolationHandler"
+ "_currentActiveScenarios"
+ "_currentPID"
+ "_currentRestrictionsByProcess"
+ "_defaultRestriction"
+ "_enrolledProcessesSet"
+ "_exemptFromMitigations"
+ "_exemptProcesses"
+ "_exemptProcessesSet"
+ "_exemptProcessesSetWithErrors:"
+ "_initWithDataProvider:"
+ "_initWithEnrolledProcesses:andExemptions:"
+ "_isAKnownScenario:"
+ "_onlyMonitorDaemons"
+ "_processNameIdentiferByPID"
+ "_processesAffectedByScenarioMap"
+ "_processesSetWithErrors:"
+ "_restrictionDataProvider"
+ "_restrictionsByProcessForScenario"
+ "_restrictionsByProcessPerScenario"
+ "_restrictionsManager"
+ "_runInternalOnly"
+ "_scenarioCriteria"
+ "_scenarioManager"
+ "_scenariosDictWithErrors:"
+ "_scenariosMap"
+ "_shouldBeFatalOnViolation"
+ "_shouldRunSafeguards"
+ "_templatesByProcessWithErrors:"
+ "_templatesByScenarioForProcess:errors:"
+ "activeScenariosLastEvaluation"
+ "activeScenariosLastPublished"
+ "addObserver:forContextIdentifier:"
+ "affectedScenarioByContextIdentifier"
+ "allProcessesMap"
+ "allScenariosByIdentifier"
+ "applyDefaultRestrictionsToProcess:"
+ "applyRestrictionsToProcess:forScenario:"
+ "approversAppleAccountAltDSIDs"
+ "authenticationResult"
+ "authenticationSessionDeviceStartedAuthentication:"
+ "authenticationSessionDeviceTappedNotification:"
+ "authenticationSessionDidFailWithError:"
+ "authenticationSessionDidFinishWithResponse:"
+ "clearMonitorForPID:"
+ "configureRestrictionsFromTemplateDictionary:errors:"
+ "cpuThreshold"
+ "cpuViolationHandler"
+ "currentActiveScenarios"
+ "currentActiveScenarios:previousActiveScenarios:"
+ "currentPID"
+ "currentRestrictionsByProcess"
+ "customAuthenticationMethods"
+ "customSharingMethods"
+ "dedicatedCameraRequest"
+ "defaultRestriction"
+ "delegatePurchaseRequest"
+ "determineScenarioForProcess:"
+ "deviceAcceptedNotificationHandler"
+ "deviceStartedAuthenticationHandler"
+ "enrolledProcessesSet"
+ "evaluateScenarios:"
+ "evaluateScenariosPostInit"
+ "executeSFIWithEffort:forPID:"
+ "exemptFromMitigations"
+ "exemptProcesses"
+ "exemptProcessesSet"
+ "fetchDaemonStatusWithCompletionHandler:"
+ "getProcessForPID:"
+ "getSFIWindow"
+ "getStateForIdentifier:"
+ "handlerInterface"
+ "hasAnyNonPasskeyRegistrationRequest"
+ "initWithAppleIDAuthorization:"
+ "initWithAppleIDRequest:passwordReqeust:platformKeyCredentialAssertionOptions:platformKeyCredentialRegistrationOptions:"
+ "initWithAppleIDRequest:passwordRequest:platformKeyCredentialAssertionOptions:platformKeyCredentialRegistrationOptions:"
+ "initWithAuthenticationResult:"
+ "initWithIdentifier:andCriteria:"
+ "pleIDRequest"
+ "runInternalOnly"
+ "scenarioManager"
+ "sharedInstanceWithDataProvider:"

```

## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.40.16.0.0
-  __TEXT.__text: 0x72b0c
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x2634
-  __TEXT.__cstring: 0x3d8b
-  __TEXT.__gcc_except_tab: 0x41cc
-  __TEXT.__oslogstring: 0x7625
-  __TEXT.__dlopen_cstrs: 0x126
+508.40.50.0.0
+  __TEXT.__text: 0x6ceb0
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x2474
+  __TEXT.__cstring: 0x398b
+  __TEXT.__gcc_except_tab: 0x3ff0
+  __TEXT.__oslogstring: 0x6f55
   __TEXT.__const: 0x3a0
   __TEXT.__constg_swiftt: 0xfc
   __TEXT.__swift5_typeref: 0x1d0

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x70
-  __TEXT.__unwind_info: 0xc98
+  __TEXT.__unwind_info: 0xba8
   __TEXT.__eh_frame: 0x1e8
-  __TEXT.__objc_classname: 0x64e
-  __TEXT.__objc_methname: 0x6fc4
-  __TEXT.__objc_methtype: 0x1a54
-  __TEXT.__objc_stubs: 0x4220
-  __DATA_CONST.__got: 0x888
-  __DATA_CONST.__const: 0x75d0
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__objc_classname: 0x5f8
+  __TEXT.__objc_methname: 0x6a42
+  __TEXT.__objc_methtype: 0x1974
+  __TEXT.__objc_stubs: 0x3c20
+  __DATA_CONST.__got: 0x860
+  __DATA_CONST.__const: 0x75a0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_selrefs: 0x1600
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x7a98
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xbd0
+  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__objc_const: 0x7550
+  __AUTH.__objc_data: 0xb80
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x234
-  __DATA.__data: 0xcb0
-  __DATA.__bss: 0x360
+  __DATA.__objc_ivar: 0x218
+  __DATA.__data: 0xc50
+  __DATA.__bss: 0x310
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1ED2BD5D-92C3-35A4-8770-C63F25DB58BE
-  Functions: 921
-  Symbols:   6875
-  CStrings:  2077
+  UUID: 38F20A31-D25F-31BC-892B-632D28405EDB
+  Functions: 866
+  Symbols:   6648
+  CStrings:  1963
 
Symbols:
+ GCC_except_table30
+ GCC_except_table42
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table76
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileAutomationManager
+ ___block_descriptor_65_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ _objc_msgSend$addType:
+ _objc_msgSend$removeType:
+ _objc_msgSend$setScanForSplatIfNecessary:
- +[SUUIMobileUserDefaultsBasedTestSession current]
- -[SUUIMobileAutomationManager .cxx_destruct]
- -[SUUIMobileAutomationManager dealloc]
- -[SUUIMobileAutomationManager init]
- -[SUUIMobileAutomationManager notifyObserversOfAutomationStateChange:]
- -[SUUIMobileAutomationManager observeValueForKeyPath:ofObject:change:context:]
- -[SUUIMobileAutomationManager resolveStoredXCUISession:]
- -[SUUIMobileAutomationManager setupAutomationForStoredSession:]
- -[SUUIMobileAutomationManager startObserving]
- -[SUUIMobileAutomationManager stopObserving]
- -[SUUIMobileAutomationManager(SoftwareUpdateServices) createSUManagerClientForAutomationSession]
- -[SUUIMobileUserDefaultsBasedTestSession .cxx_destruct]
- -[SUUIMobileUserDefaultsBasedTestSession beginTestAndReturnError:]
- -[SUUIMobileUserDefaultsBasedTestSession correlationId]
- -[SUUIMobileUserDefaultsBasedTestSession currentExecutionResult]
- -[SUUIMobileUserDefaultsBasedTestSession currentPhase]
- -[SUUIMobileUserDefaultsBasedTestSession dealloc]
- -[SUUIMobileUserDefaultsBasedTestSession endTestWithResult:error:]
- -[SUUIMobileUserDefaultsBasedTestSession handleChangedPhase:]
- -[SUUIMobileUserDefaultsBasedTestSession handlePhaseConfigurationSealed]
- -[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]
- -[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]
- -[SUUIMobileUserDefaultsBasedTestSession initWithStoredSession:]
- -[SUUIMobileUserDefaultsBasedTestSession init]
- -[SUUIMobileUserDefaultsBasedTestSession observeValueForKeyPath:ofObject:change:context:]
- -[SUUIMobileUserDefaultsBasedTestSession strategyClassForServiceType:]
- -[SUUIMobileUserDefaultsBasedTestSession strategyForServiceType:]
- GCC_except_table18
- GCC_except_table23
- GCC_except_table29
- GCC_except_table75
- _NSClassFromString
- _NSKeyValueChangeNewKey
- _NSSelectorFromString
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSHashTable
- _OBJC_CLASS_$_NSProcessInfo
- _OBJC_CLASS_$_SUUIMobileUserDefaultsBasedTestSession
- _OBJC_EHTYPE_$_NSException
- _OBJC_IVAR_$_SUUIMobileAutomationManager._currentSession
- _OBJC_IVAR_$_SUUIMobileAutomationManager._lock
- _OBJC_IVAR_$_SUUIMobileAutomationManager._observers
- _OBJC_IVAR_$_SUUIMobileAutomationManager._observing
- _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._services
- _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._servicesClasses
- _OBJC_IVAR_$_SUUIMobileUserDefaultsBasedTestSession._session
- _OBJC_METACLASS_$_SUUIMobileUserDefaultsBasedTestSession
- _SoftwareUpdateSettingsMockingKitLibrary
- _SoftwareUpdateSettingsMockingKitLibraryCore
- _SoftwareUpdateSettingsMockingKitLibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_$_INSTANCE_METHODS_SUUIMobileAutomationManager(SoftwareUpdateServices)
- __OBJC_$_INSTANCE_METHODS_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_$_INSTANCE_VARIABLES_SUUIMobileAutomationManager
- __OBJC_$_INSTANCE_VARIABLES_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_$_PROP_LIST_SUSMKTestCaseSession
- __OBJC_$_PROP_LIST_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_$_PROTOCOL_CLASS_METHODS_SUSMKTestCaseSession
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUAutoInstallOperationDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUSMKTestCaseSession
- __OBJC_$_PROTOCOL_METHOD_TYPES_SUSMKTestCaseSession
- __OBJC_$_PROTOCOL_REFS_SUSMKTestCaseSession
- __OBJC_CLASS_PROTOCOLS_$_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_CLASS_RO_$_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_LABEL_PROTOCOL_$_SUSMKTestCaseSession
- __OBJC_METACLASS_RO_$_SUUIMobileUserDefaultsBasedTestSession
- __OBJC_PROTOCOL_$_SUSMKTestCaseSession
- ___60-[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]_block_invoke
- ___61-[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]_block_invoke
- ___SoftwareUpdateSettingsMockingKitLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___getSUSMKMockedServiceTypeUtilityClass_block_invoke
- ___getSUSMKSUManagerClientClass_block_invoke
- ___getSUSMKTestCaseSessionPhaseUtilityClass_block_invoke
- ___getSUSMKUserDefaultsCodedMockedStrategyClass_block_invoke
- ___getSUSMKUserDefaultsCodedTestCaseSessionClass_block_invoke
- ___getSUSUIUserDefaultsKeysClass_block_invoke
- ___os_log_helper_16_2_2_8_32_8_64
- ___os_log_helper_16_2_2_8_34_4_0
- ___os_log_helper_16_2_3_8_32_8_64_8_64
- ___os_log_helper_16_2_3_8_32_8_64_8_66
- ___os_log_helper_16_2_4_8_32_8_64_8_64_8_64
- ___os_log_helper_16_2_4_8_34_8_0_8_0_8_0
- __dispatch_main_q
- __os_log_debug_impl
- __sl_dlopen
- _abort_report_np
- _audit_stringSoftwareUpdateSettingsMockingKit
- _dispatch_after
- _getSUSMKMockedServiceTypeUtilityClass
- _getSUSMKMockedServiceTypeUtilityClass.softClass
- _getSUSMKSUManagerClientClass
- _getSUSMKSUManagerClientClass.softClass
- _getSUSMKTestCaseSessionPhaseUtilityClass
- _getSUSMKTestCaseSessionPhaseUtilityClass.softClass
- _getSUSMKUserDefaultsCodedMockedStrategyClass
- _getSUSMKUserDefaultsCodedMockedStrategyClass.softClass
- _getSUSMKUserDefaultsCodedTestCaseSessionClass
- _getSUSMKUserDefaultsCodedTestCaseSessionClass.softClass
- _getSUSUIUserDefaultsKeysClass
- _getSUSUIUserDefaultsKeysClass.softClass
- _objc_begin_catch
- _objc_end_catch
- _objc_getClass
- _objc_msgSend$SoftwareUpdateSettingsSuiteName
- _objc_msgSend$UIUnitTestingCurrentPhase
- _objc_msgSend$UIUnitTestingCurrentSession
- _objc_msgSend$UIUnitTestingKeys
- _objc_msgSend$acceptibleStrategyClassName:forType:
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$allCases
- _objc_msgSend$allOptionClasses
- _objc_msgSend$correlationId
- _objc_msgSend$currentExecutionResult
- _objc_msgSend$currentPhase
- _objc_msgSend$defaultStrategyClassHandlerForType:
- _objc_msgSend$descriptionForPhase:
- _objc_msgSend$descriptionForType:
- _objc_msgSend$didEndWithResult:
- _objc_msgSend$enabled
- _objc_msgSend$getReturnValue:
- _objc_msgSend$handleChangedPhase:
- _objc_msgSend$handlePhaseConfigurationSealed
- _objc_msgSend$handlePhaseFinished
- _objc_msgSend$handlePhaseRunning
- _objc_msgSend$initForSession:usingOptions:
- _objc_msgSend$initWithSet:
- _objc_msgSend$initWithStoredSession:
- _objc_msgSend$instantiateDefaultStrategyHandlerForType:withSession:
- _objc_msgSend$isRunning:
- _objc_msgSend$mockedService
- _objc_msgSend$mockedStrategyClassName
- _objc_msgSend$mockedStrategyOptions
- _objc_msgSend$notifyObserversOfAutomationStateChange:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$onAutomationEnabledStateChanged:
- _objc_msgSend$processId
- _objc_msgSend$processStartTime
- _objc_msgSend$processStartTime:
- _objc_msgSend$removeObserver:forKeyPath:
- _objc_msgSend$resolveStoredXCUISession:
- _objc_msgSend$setUnitTestingCurrentPhase:
- _objc_msgSend$setupAutomationForStoredSession:
- _objc_msgSend$shouldKeepPreviousMockingKitSession
- _objc_msgSend$shouldSkipMockingKitPIDValidation
- _objc_msgSend$shouldSkipMockingKitPIDValidation:
- _objc_msgSend$softwareUpdateShared
- _objc_msgSend$startObserving
- _objc_msgSend$stopObserving
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- _objc_msgSend$unitTestingCurrentPhase
- _objc_msgSend$unitTestingCurrentTestResult
- _objc_msgSend$unitTestingRegisteredServicesDictionary
- _objc_msgSend$weakObjectsHashTable
- _objc_msgSend$willBegin
- _objc_opt_respondsToSelector
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "%s [%p]: Dropping a 3rd party scan results notification: the results contains a SPLAT update for both the preferred and alternate descriptors."
+ "%s [%p]: Dropping a 3rd party scan results notification: the results contains only a SPLAT alternate descriptor."
+ "%s [%p]: Dropping a 3rd party scan results notification: the results contains only a SPLAT preferred descriptor."
+ "%s [%p]: Modifying the 3rd party scan pipeline: One of the 3rd party scan results was a SPLAT update, while the other wasn't. Requesting a fresh background full scan."
+ "BackgroundSecurityImprovement"
+ "T@,R,N"
+ "addType:"
+ "removeType:"
+ "setScanForSplatIfNecessary:"
- "#24@0:8q16"
- "%s"
- "%s [XCUI correlationId: %@]: Changed XCUI testing session phase into: %{public}@"
- "%s [XCUI correlationId: %@]: Could not fetch an NSClass instance from the class name string: '%@' for type: '%@'"
- "%s [XCUI correlationId: %@]: Could not instantiate SUSMKUserDefaultsCodedMockedStrategy for type: '%@'.\nError: %@"
- "%s [XCUI correlationId: %@]: Creating mocked service class: %@ for service '%@'"
- "%s [XCUI correlationId: %@]: Failed to decode the changed phase into an NSNumber. Got: %@"
- "%s [XCUI correlationId: %@]: Registering the default implementation for service type: %@"
- "%s [XCUI correlationId: %@]: Sending the didEnd event to service type: %@"
- "%s [XCUI correlationId: %@]: Sending the willBegin event to service type: %@"
- "%s [XCUI correlationId: %@]: The supplied strategy class name '%@' for type '%@' is not acceptible. Each strategy must be manually registered in the Service Type class."
- "%s: %{public}@ exists in Production. Auto-disables."
- "%s: Automation is enabled. Initializing session: %{public}@"
- "%s: Could not load SUSMKManagerClient."
- "%s: Initializing %@"
- "%s: Manager doesn't respond to initWithSession:"
- "%s: Property \"%{public}@\" changed to: %{public}@"
- "%s: Start to observe for Unit Testing requests.\nNSUserDefaults Automation enabled? %{public}@"
- "%s: Stops observing for Unit Testing requests."
- "%{public}s: Found a UTs session stored in NSUserDefaults. However, the process '%d' isn't running anymore. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, incorrect, PID."
- "%{public}s: Found a UTs session stored in NSUserDefaults. However, the process '%d' isn't running anymore. Killing the session."
- "%{public}s: Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %ld, %ld, different than the start time of the current process with this pid, %ld. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, corrupted, PID."
- "%{public}s: Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %ld, %ld, different than the start time of the current process with this pid, %ld. Killing the session."
- "-[SUUIMobileAutomationManager initialize]"
- "-[SUUIMobileAutomationManager observeValueForKeyPath:ofObject:change:context:]"
- "-[SUUIMobileAutomationManager resolveStoredXCUISession:]"
- "-[SUUIMobileAutomationManager setupAutomationForStoredSession:]"
- "-[SUUIMobileAutomationManager startObserving]"
- "-[SUUIMobileAutomationManager stopObserving]"
- "-[SUUIMobileAutomationManager(SoftwareUpdateServices) createSUManagerClientForAutomationSession]"
- "-[SUUIMobileUserDefaultsBasedTestSession handleChangedPhase:]"
- "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseConfigurationSealed]"
- "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseFinished]_block_invoke"
- "-[SUUIMobileUserDefaultsBasedTestSession handlePhaseRunning]_block_invoke"
- "-[SUUIMobileUserDefaultsBasedTestSession observeValueForKeyPath:ofObject:change:context:]"
- "@\"<SUSMKMockingStrategy>\"24@0:8q16"
- "@\"<SUSMKTestCaseSession>\"16@0:8"
- "@\"NSHashTable\""
- "@\"SUSMKUserDefaultsCodedTestCaseSession\""
- "@\"SUUIMobileUserDefaultsBasedTestSession\""
- "B24@0:8^@16"
- "B32@0:8q16^@24"
- "Failed to decode the saved automation session into an SUSMKUserDefaultsCodedTestCaseSession object. Error: %{public}@"
- "SUSMKMockedServiceTypeUtility"
- "SUSMKSUManagerClient"
- "SUSMKTestCaseSession"
- "SUSMKTestCaseSessionPhaseUtility"
- "SUSMKUserDefaultsCodedMockedStrategy"
- "SUSMKUserDefaultsCodedTestCaseSession"
- "SUSUIUserDefaultsKeys"
- "SUUIMobileUserDefaultsBasedTestSession"
- "SoftwareUpdateServices"
- "SoftwareUpdateSettingsSuiteName"
- "T@\"NSString\",R,C,N"
- "T@,R,N,V_currentSession"
- "Tq,R,N"
- "UIUnitTestingCurrentPhase"
- "UIUnitTestingCurrentSession"
- "UIUnitTestingKeys"
- "Unable to find class %s"
- "_currentSession"
- "_observers"
- "_observing"
- "_services"
- "_servicesClasses"
- "_session"
- "acceptibleStrategyClassName:forType:"
- "addObserver:forKeyPath:options:context:"
- "allCases"
- "allOptionClasses"
- "beginTestAndReturnError:"
- "com.apple.SoftwareUpdateUI"
- "correlationId"
- "current"
- "currentExecutionResult"
- "currentPhase"
- "defaultStrategyClassHandlerForType:"
- "descriptionForPhase:"
- "descriptionForType:"
- "didEndWithResult:"
- "endTestWithResult:error:"
- "getReturnValue:"
- "handleChangedPhase:"
- "handlePhaseConfigurationSealed"
- "handlePhaseFinished"
- "handlePhaseRunning"
- "initForSession:usingOptions:"
- "initWithSession:"
- "initWithSet:"
- "initWithStoredSession:"
- "instantiateDefaultStrategyHandlerForType:withSession:"
- "isRunning:"
- "mockedService"
- "mockedStrategyClassName"
- "mockedStrategyOptions"
- "notifyObserversOfAutomationStateChange:"
- "numberWithInt:"
- "observeValueForKeyPath:ofObject:change:context:"
- "processId"
- "processStartTime"
- "processStartTime:"
- "removeObserver:forKeyPath:"
- "resolveStoredXCUISession:"
- "setUnitTestingCurrentPhase:"
- "setupAutomationForStoredSession:"
- "shouldKeepPreviousMockingKitSession"
- "shouldSkipMockingKitPIDValidation"
- "shouldSkipMockingKitPIDValidation:"
- "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/SoftwareUpdateSettingsMockingKit.framework/SoftwareUpdateSettingsMockingKit"
- "softwareUpdateShared"
- "startObserving"
- "stopObserving"
- "strategyClassForServiceType:"
- "strategyForServiceType:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unitTestingCurrentPhase"
- "unitTestingCurrentTestResult"
- "unitTestingRegisteredServicesDictionary"
- "v48@0:8@16@24@32^v40"
- "weakObjectsHashTable"
- "willBegin"

```

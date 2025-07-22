## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit`

```diff

-103.7.0.0.0
-  __TEXT.__text: 0xaf808
+104.4.0.0.0
+  __TEXT.__text: 0xb1c60
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x1083c
+  __TEXT.__objc_methlist: 0x10bec
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x88de
-  __TEXT.__oslogstring: 0x4017
+  __TEXT.__cstring: 0x899f
+  __TEXT.__oslogstring: 0x40aa
   __TEXT.__gcc_except_tab: 0x708
   __TEXT.__ustring: 0x37e
   __TEXT.__dlopen_cstrs: 0x44
-  __TEXT.__unwind_info: 0x365c
-  __TEXT.__objc_classname: 0x4392
-  __TEXT.__objc_methname: 0x23324
-  __TEXT.__objc_methtype: 0x5d20
-  __TEXT.__objc_stubs: 0x15ac0
+  __TEXT.__unwind_info: 0x370c
+  __TEXT.__objc_classname: 0x4462
+  __TEXT.__objc_methname: 0x23b42
+  __TEXT.__objc_methtype: 0x5daf
+  __TEXT.__objc_stubs: 0x16160
   __DATA_CONST.__got: 0x528
-  __DATA_CONST.__const: 0x2910
-  __DATA_CONST.__objc_classlist: 0xef0
+  __DATA_CONST.__const: 0x2970
+  __DATA_CONST.__objc_classlist: 0xf20
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d6f8
-  __DATA_CONST.__objc_selrefs: 0x6a48
+  __DATA_CONST.__objc_const: 0x1db10
+  __DATA_CONST.__objc_selrefs: 0x6bf0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0xdb8
+  __DATA_CONST.__objc_superrefs: 0xc08
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __AUTH_CONST.__cfstring: 0x8f00
-  __AUTH_CONST.__objc_const: 0xcf50
-  __AUTH_CONST.__const: 0x17a0
+  __AUTH_CONST.__cfstring: 0x8fe0
+  __AUTH_CONST.__objc_const: 0xd190
+  __AUTH_CONST.__const: 0x1800
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x798
-  __AUTH.__objc_data: 0x7030
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0xd88
-  __DATA.__objc_superrefs: 0xbf0
-  __DATA.__objc_ivar: 0x12a4
+  __AUTH.__objc_data: 0x7210
+  __DATA.__objc_ivar: 0x12d0
   __DATA.__data: 0x3368
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1e8
   __DATA_DIRTY.__objc_data: 0x2530
-  __DATA_DIRTY.__bss: 0x600
+  __DATA_DIRTY.__bss: 0x610
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8833378F-74BD-301C-B682-649BDDBDCFBF
-  Functions: 5905
-  Symbols:   21646
-  CStrings:  9559
+  UUID: F000AA78-4848-3391-B290-2D0D0C3FD866
+  Functions: 5987
+  Symbols:   21932
+  CStrings:  9654
 
Symbols:
+ +[CRKASMClassicAdHocSwitchReadingRosterProvider currentUserProviderObservedKeyPaths]
+ +[CRKClassKitFacadeFactory currentPlatformRequiresPersonaAdoption]
+ +[CRKClassKitFacadeFactory dataSeparationEnabled]
+ +[CRKClassKitFacadeFactory makeBaseClassKitFacadeWithPersonaAdoption:]
+ +[CRKClassKitFacadeFactory makeInstructorClassKitFacadeWithPersonaAdoption:]
+ +[CRKClassKitFacadeFactory makeStudentClassKitFacade]
+ +[CRKFeatureDataStoreDefaults_MCX defaultAskValueForFeature:]
+ +[CRKFeatureDataStoreDefaults_MCX defaultValueForFeature:]
+ +[CRKFeatureDataStoreDefaults_MCX restrictionDefaultValues]
+ +[CRKFeatureDataStoreHeuristics_MCX overrideFeaturesByFeature]
+ +[CRKFeatureDataStoreHeuristics_MCX overrideIsForcedByFeature]
+ +[CRKNotifyDaemonOfSettingsPaneActivationRequest supportsSecureCoding]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider .cxx_destruct]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider currentUserDidChange]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider currentUserProvider]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider dealloc]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider initWithClassKitFacade:rosterProviderGenerator:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider isClassicAdHocModeEnabledForUser:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider isPopulated]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider observeValueForKeyPath:ofObject:change:context:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider overrideIsPopulatedToYES]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider overridingIsPopulatedToYES]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider previousValueOfAdHocModeEnabled]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider processAdHocModeEnabled:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider setOverridingIsPopulatedToYES:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider setPreviousValueOfAdHocModeEnabled:]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider startObservingCurrentUserProvider]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider stopObservingCurrentUserProvider]
+ -[CRKASMClassicAdHocSwitchReadingRosterProvider suspendableProvider]
+ -[CRKASMEasyMAIDSignInRosterProvider isEasyStudentSignInDisabledByServer]
+ -[CRKASMRosterProviderConfiguration classKitFacade]
+ -[CRKASMRosterProviderConfiguration initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:]
+ -[CRKASMRosterProviderConfiguration initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:]
+ -[CRKASMRosterProviderFactory makeClassicAdHocSwitchReadingRosterProviderWithConfiguration:]
+ -[CRKClassKitFacadeDecoratorBase syncServerConfigWithCompletion:]
+ -[CRKConcreteClassKitFacade syncServerConfigWithCompletion:]
+ -[CRKConcreteClassKitRosterRequirements generalObserverConstituentsRegistered]
+ -[CRKConcreteClassKitRosterRequirements registerGeneralObserverConstituents]
+ -[CRKConcreteClassKitRosterRequirements setGeneralObserverConstituentsRegistered:]
+ -[CRKConcreteClassKitRosterRequirements syncServerConfigWithCompletion:]
+ -[CRKConcreteClassKitRosterRequirements unregisterForCurrentUserChangeNotification]
+ -[CRKConcreteClassKitRosterRequirements unregisterGeneralObserverConstituents]
+ -[CRKCourseEnrollmentController isSignedInToStudentMAID]
+ -[CRKCourseEnrollmentController notifyDaemonOfSettingsPaneActivationOperationDidFail:]
+ -[CRKCourseEnrollmentController notifyDaemonOfSettingsPaneActivationOperationDidFail:].cold.1
+ -[CRKCourseEnrollmentController setSignedInToStudentMAID:]
+ -[CRKCourseEnrollmentController userDidActivateSettingsPane]
+ -[CRKFeatureDataStoreHeuristics_MCX .cxx_destruct]
+ -[CRKFeatureDataStoreHeuristics_MCX applyHeuristicsToFeature:boolType:]
+ -[CRKFeatureDataStoreHeuristics_MCX applyIsForcedHeuristicsToFeature:isForced:]
+ -[CRKFeatureDataStoreHeuristics_MCX dataStore]
+ -[CRKFeatureDataStoreHeuristics_MCX initWithDataStore:]
+ -[CRKFeatureDataStoreHeuristics_MCX setDataStore:]
+ -[CRKFeatureDataStore_MCX .cxx_destruct]
+ -[CRKFeatureDataStore_MCX MCXPrimitives]
+ -[CRKFeatureDataStore_MCX activeClassroomRoles]
+ -[CRKFeatureDataStore_MCX addActiveClassroomRole:]
+ -[CRKFeatureDataStore_MCX boolRestrictionForFeature:]
+ -[CRKFeatureDataStore_MCX effectiveBoolValueForSetting:outAsk:]
+ -[CRKFeatureDataStore_MCX effectiveValueForSetting:configurationUUID:outAsk:]
+ -[CRKFeatureDataStore_MCX heuristicsManager]
+ -[CRKFeatureDataStore_MCX initWithMCXPrimitives:]
+ -[CRKFeatureDataStore_MCX isClassroomAutomaticClassJoiningForced]
+ -[CRKFeatureDataStore_MCX isClassroomInstructorRoleEnabled]
+ -[CRKFeatureDataStore_MCX isClassroomRequestPermissionToLeaveClassesForced]
+ -[CRKFeatureDataStore_MCX isClassroomStudentRoleEnabled]
+ -[CRKFeatureDataStore_MCX isClassroomUnpromptedScreenObservationForced]
+ -[CRKFeatureDataStore_MCX isFeatureForced:]
+ -[CRKFeatureDataStore_MCX isRoleEnabled:]
+ -[CRKFeatureDataStore_MCX keyForFeature:configurationUUID:ask:]
+ -[CRKFeatureDataStore_MCX removeActiveClassroomRole:]
+ -[CRKFeatureDataStore_MCX removeDuplicateEntriesFromStoredClassroomRoles]
+ -[CRKFeatureDataStore_MCX setActiveClassroomRoles:]
+ -[CRKFeatureDataStore_MCX setBoolValue:ask:forSetting:]
+ -[CRKFeatureDataStore_MCX setBoolValue:ask:forSetting:configurationUUID:]
+ -[CRKFeatureDataStore_MCX setClassroomInstructorRoleEnabled:]
+ -[CRKFeatureDataStore_MCX setClassroomStudentRoleEnabled:]
+ -[CRKFeatureDataStore_MCX setHeuristicsManager:]
+ -[CRKFeatureDataStore_MCX setRole:enabled:]
+ -[CRKFetchConfigurationTypeResultObject isSignedInToStudentMAID]
+ -[CRKFetchConfigurationTypeResultObject setSignedInToStudentMAID:]
+ -[CRKPersonaAdoptingClassKitFacade syncServerConfigWithCompletion:]
+ _CRKClassroomSettingsPaneDidActivateNotificationName
+ _OBJC_CLASS_$_CRKASMClassicAdHocSwitchReadingRosterProvider
+ _OBJC_CLASS_$_CRKClassKitFacadeFactory
+ _OBJC_CLASS_$_CRKFeatureDataStoreDefaults_MCX
+ _OBJC_CLASS_$_CRKFeatureDataStoreHeuristics_MCX
+ _OBJC_CLASS_$_CRKFeatureDataStore_MCX
+ _OBJC_CLASS_$_CRKNotifyDaemonOfSettingsPaneActivationRequest
+ _OBJC_IVAR_$_CRKASMClassicAdHocSwitchReadingRosterProvider._currentUserProvider
+ _OBJC_IVAR_$_CRKASMClassicAdHocSwitchReadingRosterProvider._overridingIsPopulatedToYES
+ _OBJC_IVAR_$_CRKASMClassicAdHocSwitchReadingRosterProvider._previousValueOfAdHocModeEnabled
+ _OBJC_IVAR_$_CRKASMClassicAdHocSwitchReadingRosterProvider._suspendableProvider
+ _OBJC_IVAR_$_CRKASMRosterProviderConfiguration._classKitFacade
+ _OBJC_IVAR_$_CRKConcreteClassKitRosterRequirements._generalObserverConstituentsRegistered
+ _OBJC_IVAR_$_CRKCourseEnrollmentController._signedInToStudentMAID
+ _OBJC_IVAR_$_CRKFeatureDataStoreHeuristics_MCX._dataStore
+ _OBJC_IVAR_$_CRKFeatureDataStore_MCX._MCXPrimitives
+ _OBJC_IVAR_$_CRKFeatureDataStore_MCX._heuristicsManager
+ _OBJC_IVAR_$_CRKFetchConfigurationTypeResultObject._signedInToStudentMAID
+ _OBJC_METACLASS_$_CRKASMClassicAdHocSwitchReadingRosterProvider
+ _OBJC_METACLASS_$_CRKClassKitFacadeFactory
+ _OBJC_METACLASS_$_CRKFeatureDataStoreDefaults_MCX
+ _OBJC_METACLASS_$_CRKFeatureDataStoreHeuristics_MCX
+ _OBJC_METACLASS_$_CRKFeatureDataStore_MCX
+ _OBJC_METACLASS_$_CRKNotifyDaemonOfSettingsPaneActivationRequest
+ __OBJC_$_CLASS_METHODS_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_$_CLASS_METHODS_CRKClassKitFacadeFactory
+ __OBJC_$_CLASS_METHODS_CRKFeatureDataStoreDefaults_MCX
+ __OBJC_$_CLASS_METHODS_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_$_CLASS_METHODS_CRKNotifyDaemonOfSettingsPaneActivationRequest
+ __OBJC_$_INSTANCE_METHODS_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_$_INSTANCE_METHODS_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_$_INSTANCE_METHODS_CRKFeatureDataStore_MCX
+ __OBJC_$_INSTANCE_VARIABLES_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_$_INSTANCE_VARIABLES_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_$_INSTANCE_VARIABLES_CRKFeatureDataStore_MCX
+ __OBJC_$_PROP_LIST_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_$_PROP_LIST_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_$_PROP_LIST_CRKFeatureDataStore_MCX
+ __OBJC_CLASS_PROTOCOLS_$_CRKFeatureDataStore_MCX
+ __OBJC_CLASS_RO_$_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_CLASS_RO_$_CRKClassKitFacadeFactory
+ __OBJC_CLASS_RO_$_CRKFeatureDataStoreDefaults_MCX
+ __OBJC_CLASS_RO_$_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_CLASS_RO_$_CRKFeatureDataStore_MCX
+ __OBJC_CLASS_RO_$_CRKNotifyDaemonOfSettingsPaneActivationRequest
+ __OBJC_METACLASS_RO_$_CRKASMClassicAdHocSwitchReadingRosterProvider
+ __OBJC_METACLASS_RO_$_CRKClassKitFacadeFactory
+ __OBJC_METACLASS_RO_$_CRKFeatureDataStoreDefaults_MCX
+ __OBJC_METACLASS_RO_$_CRKFeatureDataStoreHeuristics_MCX
+ __OBJC_METACLASS_RO_$_CRKFeatureDataStore_MCX
+ __OBJC_METACLASS_RO_$_CRKNotifyDaemonOfSettingsPaneActivationRequest
+ ___59+[CRKFeatureDataStoreDefaults_MCX restrictionDefaultValues]_block_invoke
+ ___62+[CRKFeatureDataStoreHeuristics_MCX overrideFeaturesByFeature]_block_invoke
+ ___62+[CRKFeatureDataStoreHeuristics_MCX overrideIsForcedByFeature]_block_invoke
+ ___67-[CRKPersonaAdoptingClassKitFacade syncServerConfigWithCompletion:]_block_invoke
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_4
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_5
+ ___92-[CRKASMRosterProviderFactory makeClassicAdHocSwitchReadingRosterProviderWithConfiguration:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e30_"<CRKASMRosterProviding>"8?0ls32l8s40l8
+ ___block_literal_global.105
+ ___block_literal_global.120
+ ___block_literal_global.142
+ ___block_literal_global.156
+ ___block_literal_global.160
+ ___block_literal_global.234
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.294
+ ___block_literal_global.298
+ ___block_literal_global.329
+ ___block_literal_global.42
+ ___block_literal_global.45
+ ___block_literal_global.61
+ ___block_literal_global.91
+ _kClassroomDefaultRestrictionsAskKey
+ _kClassroomDefaultRestrictionsFilename
+ _kClassroomDefaultRestrictionsValueKey
+ _kClassroomPreferenceKeyDelimiter
+ _kClassroomRoleInstructor
+ _kClassroomRoleStudent
+ _objc_msgSend$MCXPrimitives
+ _objc_msgSend$addActiveClassroomRole:
+ _objc_msgSend$applyHeuristicsToFeature:boolType:
+ _objc_msgSend$applyIsForcedHeuristicsToFeature:isForced:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$classroomClassicAdHocModeEnabled
+ _objc_msgSend$classroomRoles
+ _objc_msgSend$crk_featureBoolTypeFromNumber:
+ _objc_msgSend$currentUserDidChange
+ _objc_msgSend$defaultAskValueForFeature:
+ _objc_msgSend$defaultValueForFeature:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$easyStudentSignInDisabled
+ _objc_msgSend$effectiveValueForSetting:configurationUUID:outAsk:
+ _objc_msgSend$generalObserverConstituentsRegistered
+ _objc_msgSend$heuristicsManager
+ _objc_msgSend$initWithClassKitFacade:rosterProviderGenerator:
+ _objc_msgSend$initWithDataStore:
+ _objc_msgSend$initWithGenerator:
+ _objc_msgSend$initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:
+ _objc_msgSend$initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:
+ _objc_msgSend$isClassicAdHocModeEnabledForUser:
+ _objc_msgSend$isEasyStudentSignInDisabledByServer
+ _objc_msgSend$isFeatureForced:
+ _objc_msgSend$isKeyUserModifiable:
+ _objc_msgSend$isRoleEnabled:
+ _objc_msgSend$isSignedInToStudentMAID
+ _objc_msgSend$keyForFeature:configurationUUID:ask:
+ _objc_msgSend$makeClassicAdHocSwitchReadingRosterProviderWithConfiguration:
+ _objc_msgSend$numberForKey:
+ _objc_msgSend$overrideFeaturesByFeature
+ _objc_msgSend$overrideIsForcedByFeature
+ _objc_msgSend$overrideIsPopulatedToYES
+ _objc_msgSend$overridingIsPopulatedToYES
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$previousValueOfAdHocModeEnabled
+ _objc_msgSend$processAdHocModeEnabled:
+ _objc_msgSend$registerGeneralObserverConstituents
+ _objc_msgSend$removeActiveClassroomRole:
+ _objc_msgSend$removeDuplicateEntriesFromStoredClassroomRoles
+ _objc_msgSend$restrictionDefaultValues
+ _objc_msgSend$setActiveClassroomRoles:
+ _objc_msgSend$setArray:forKey:
+ _objc_msgSend$setBoolValue:ask:forSetting:configurationUUID:
+ _objc_msgSend$setGeneralObserverConstituentsRegistered:
+ _objc_msgSend$setNumber:forKey:
+ _objc_msgSend$setOverridingIsPopulatedToYES:
+ _objc_msgSend$setPreviousValueOfAdHocModeEnabled:
+ _objc_msgSend$setRole:enabled:
+ _objc_msgSend$setSignedInToStudentMAID:
+ _objc_msgSend$startObservingCurrentUserProvider
+ _objc_msgSend$stopObservingCurrentUserProvider
+ _objc_msgSend$suspendableProvider
+ _objc_msgSend$syncServerConfigWithCompletion:
+ _objc_msgSend$unregisterForCurrentUserChangeNotification
+ _objc_msgSend$unregisterGeneralObserverConstituents
+ _overrideFeaturesByFeature.onceToken
+ _overrideFeaturesByFeature.overrideFeaturesByFeature
+ _overrideIsForcedByFeature.onceToken
+ _overrideIsForcedByFeature.overrideIsForcedByFeature
+ _restrictionDefaultValues.classroomRestrictionDefaultValues
+ _restrictionDefaultValues.onceToken
- +[CRKASMRosterProviderConfiguration currentPlatformRequiresPersonaAdoption]
- +[CRKASMRosterProviderConfiguration dataSeparationEnabled]
- +[CRKASMRosterProviderConfiguration makeBaseClassKitFacadeWithPersonaAdoption:]
- +[CRKASMRosterProviderConfiguration makeInstructorClassKitFacadeWithPersonaAdoption:]
- +[CRKASMRosterProviderConfiguration makeStudentClassKitFacade]
- -[CRKASMRosterProviderConfiguration initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:]
- -[CRKASMRosterProviderConfiguration initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:]
- -[CRKConcreteFeatureFlags isEasyMAIDPermissionCheckingEnabled]
- GCC_except_table9
- ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke.39
- ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_2.40
- ___block_literal_global.119
- ___block_literal_global.141
- ___block_literal_global.155
- ___block_literal_global.159
- ___block_literal_global.233
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.284
- ___block_literal_global.288
- ___block_literal_global.328
- ___block_literal_global.41
- ___block_literal_global.44
- ___block_literal_global.60
- ___block_literal_global.84
- ___block_literal_global.90
- _objc_msgSend$initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:
- _objc_msgSend$initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:
- _objc_msgSend$isEasyMAIDPermissionCheckingEnabled
CStrings:
+ "\x053"
+ "%@ask"
+ "@\"<CRKASMRosterProviding>\"8@?0"
+ "@\"<CRKMCXPrimitives>\""
+ "@\"CRKASMSuspendableRosterProvider\""
+ "@\"CRKFeatureDataStoreHeuristics_MCX\""
+ "@100@0:8@16@24@32@40@48q56q64d72B80@84d92"
+ "@84@0:8@16@24@32@40@48q56q64d72B80"
+ "B28@0:8@16B24"
+ "CRKASMClassicAdHocSwitchReadingRosterProvider"
+ "CRKASMClassicAdHocSwitchReadingRosterProviderObservationContext"
+ "CRKClassKitFacadeFactory"
+ "CRKClassroomSettingsPaneDidActivateNotificationName"
+ "CRKFeatureDataStoreDefaults_MCX"
+ "CRKFeatureDataStoreHeuristics_MCX"
+ "CRKFeatureDataStore_MCX"
+ "CRKForceClassicAdHocModeInsteadOfASMMode"
+ "CRKNotifyDaemonOfSettingsPaneActivationRequest"
+ "Classroom classic ad-hoc mode is NOT enabled in ASM. Resuming roster provider."
+ "Classroom classic ad-hoc mode is enabled in ASM. Suspending roster provider."
+ "Failed to notify daemon ot Settings pane activation: %{public}@"
+ "MCXPrimitives"
+ "T@\"<CRKFeatureDataStoreProtocol>\",W,N,V_dataStore"
+ "T@\"<CRKMCXPrimitives>\",R,N,V_MCXPrimitives"
+ "T@\"CRKASMSuspendableRosterProvider\",R,N,V_suspendableProvider"
+ "T@\"CRKFeatureDataStoreHeuristics_MCX\",&,N,V_heuristicsManager"
+ "T@\"NSNumber\",&,N,V_previousValueOfAdHocModeEnabled"
+ "T@\"NSString\",?,R,C"
+ "TB,N,GisSignedInToStudentMAID,V_signedInToStudentMAID"
+ "TB,N,V_generalObserverConstituentsRegistered"
+ "TB,N,V_overridingIsPopulatedToYES"
+ "User did activate Settings pane"
+ "_MCXPrimitives"
+ "_generalObserverConstituentsRegistered"
+ "_heuristicsManager"
+ "_overridingIsPopulatedToYES"
+ "_previousValueOfAdHocModeEnabled"
+ "_signedInToStudentMAID"
+ "_suspendableProvider"
+ "addActiveClassroomRole:"
+ "applyHeuristicsToFeature:boolType:"
+ "applyIsForcedHeuristicsToFeature:isForced:"
+ "arrayForKey:"
+ "ask"
+ "classroomClassicAdHocModeEnabled"
+ "currentUserDidChange"
+ "defaultAskValueForFeature:"
+ "defaultSettings_macOS"
+ "defaultValueForFeature:"
+ "dictionaryWithContentsOfFile:"
+ "easyStudentSignInDisabled"
+ "generalObserverConstituentsRegistered"
+ "heuristicsManager"
+ "initWithClassKitFacade:rosterProviderGenerator:"
+ "initWithDataStore:"
+ "initWithMCXPrimitives:"
+ "initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:"
+ "initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:classKitFacade:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:"
+ "isClassicAdHocModeEnabledForUser:"
+ "isKeyUserModifiable:"
+ "isRoleEnabled:"
+ "isSignedInToStudentMAID"
+ "keyForFeature:configurationUUID:ask:"
+ "makeClassicAdHocSwitchReadingRosterProviderWithConfiguration:"
+ "notifyDaemonOfSettingsPaneActivationOperationDidFail:"
+ "numberForKey:"
+ "overrideFeaturesByFeature"
+ "overrideIsForcedByFeature"
+ "overrideIsPopulatedToYES"
+ "overridingIsPopulatedToYES"
+ "pathForResource:ofType:"
+ "plist"
+ "previousValueOfAdHocModeEnabled"
+ "processAdHocModeEnabled:"
+ "registerGeneralObserverConstituents"
+ "removeActiveClassroomRole:"
+ "removeDuplicateEntriesFromStoredClassroomRoles"
+ "restrictionDefaultValues"
+ "setActiveClassroomRoles:"
+ "setArray:forKey:"
+ "setDataStore:"
+ "setGeneralObserverConstituentsRegistered:"
+ "setHeuristicsManager:"
+ "setNumber:forKey:"
+ "setOverridingIsPopulatedToYES:"
+ "setPreviousValueOfAdHocModeEnabled:"
+ "setRole:enabled:"
+ "setSignedInToStudentMAID:"
+ "signedInToStudentMAID"
+ "startObservingCurrentUserProvider"
+ "stopObservingCurrentUserProvider"
+ "suspendableProvider"
+ "syncServerConfigWithCompletion:"
+ "unregisterForCurrentUserChangeNotification"
+ "unregisterGeneralObserverConstituents"
+ "userDidActivateSettingsPane"
+ "v24@0:8@?<v@?B@\"NSError\">16"
- "\x043"
- "@76@0:8@16@24@32@40q48q56d64B72"
- "@92@0:8@16@24@32@40q48q56d64B72@76d84"
- "EasyMAIDPermissionChecking"
- "EasyMAIDPermissionChecking feature flag is disabled in the Classroom domain. Allowing Easy MAID Sign In."
- "TB,R,N,GisEasyMAIDPermissionCheckingEnabled"
- "easyMAIDPermissionCheckingEnabled"
- "initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:"
- "initWithUserCommonNamePrefix:trustedUserCommonNamePrefix:rosterRequirements:credentialStore:maxCourseUsersCount:maxCourseTrustedUsersCount:rosterMutationTimeout:userCachingEnabled:osTransactionPrimitives:transactionReleaseDelay:"
- "isEasyMAIDPermissionCheckingEnabled"
- "isPermissionCheckingEnabled"

```

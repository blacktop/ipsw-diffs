## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-28.122.2.0.0
-  __TEXT.__text: 0xf6d4
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x162c
+50.0.0.0.0
+  __TEXT.__text: 0x11c3c
+  __TEXT.__objc_methlist: 0x1a3c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x119d
+  __TEXT.__cstring: 0x1989
   __TEXT.__oslogstring: 0x5c3
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__unwind_info: 0x588
-  __TEXT.__objc_classname: 0x90b
-  __TEXT.__objc_methname: 0x2ce7
-  __TEXT.__objc_methtype: 0x85d
-  __TEXT.__objc_stubs: 0x1de0
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xc80
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0x3f50
-  __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x1f4
+  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__objc_const: 0x4740
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xe10
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0xa50
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA0A458C-407D-39C2-9E9F-0C33F796A67E
-  Functions: 530
-  Symbols:   2183
-  CStrings:  972
+  UUID: CF81643D-6FEF-33C0-8CB6-10574FFBE950
+  Functions: 606
+  Symbols:   2452
+  CStrings:  389
 
Symbols:
+ +[AECoreMenuBarItem supportsSecureCoding]
+ -[AEAssessmentIndividualConfiguration allowedMenuItems]
+ -[AEAssessmentIndividualConfiguration setAllowedMenuItems:]
+ -[AEAssessmentState _allowedCollaborationIDs]
+ -[AEAssessmentState _allowsAirPlay]
+ -[AEAssessmentState _allowsDonatingClipboardHistoryToSpotlight]
+ -[AEAssessmentState _allowsSharingServices]
+ -[AEAssessmentState _allowsSpotlight]
+ -[AEAssessmentState allowLockdownMode]
+ -[AEAssessmentState allowOnlyParticipantsToRun]
+ -[AEAssessmentState allowPrivateRelay]
+ -[AEAssessmentState allowedAppleMenuItems]
+ -[AEAssessmentState allowedBluetoothDeviceNames]
+ -[AEAssessmentState allowedBluetoothProfiles]
+ -[AEAssessmentState allowedDirectoriesAndFiles]
+ -[AEAssessmentState allowedMenuBarItems]
+ -[AEAssessmentState allowsAccessibilityAlternativeInputMethods]
+ -[AEAssessmentState allowsAccessibilityBackgroundSounds]
+ -[AEAssessmentState allowsAccessibilityHoverText]
+ -[AEAssessmentState allowsAccessibilityLiveSpeech]
+ -[AEAssessmentState allowsAccessibilitySpokenContent]
+ -[AEAssessmentState allowsAccessibilitySwitchControl]
+ -[AEAssessmentState allowsAccessibilityVoiceControl]
+ -[AEAssessmentState allowsAccessibilityVoiceOver]
+ -[AEAssessmentState allowsAccessibilityZoom]
+ -[AEAssessmentState allowsAutoFill]
+ -[AEAssessmentState allowsDock]
+ -[AEAssessmentState allowsMenuBar]
+ -[AEAssessmentState allowsStructuralInput]
+ -[AEAssessmentState allowsUserScriptExecution]
+ -[AEAssessmentState maxBluetoothDevicesAllowed]
+ -[AEAssessmentState requiresManagedDevice]
+ -[AEAssessmentState requiresSIP]
+ -[AEAssessmentState requiresSingleUser]
+ -[AEAssessmentState requiresUserAccountType]
+ -[AEAssessmentState setAllowLockdownMode:]
+ -[AEAssessmentState setAllowOnlyParticipantsToRun:]
+ -[AEAssessmentState setAllowPrivateRelay:]
+ -[AEAssessmentState setAllowedAppleMenuItems:]
+ -[AEAssessmentState setAllowedBluetoothDeviceNames:]
+ -[AEAssessmentState setAllowedBluetoothProfiles:]
+ -[AEAssessmentState setAllowedDirectoriesAndFiles:]
+ -[AEAssessmentState setAllowedMenuBarItems:]
+ -[AEAssessmentState setAllowsAccessibilityAlternativeInputMethods:]
+ -[AEAssessmentState setAllowsAccessibilityBackgroundSounds:]
+ -[AEAssessmentState setAllowsAccessibilityHoverText:]
+ -[AEAssessmentState setAllowsAccessibilityLiveSpeech:]
+ -[AEAssessmentState setAllowsAccessibilitySpokenContent:]
+ -[AEAssessmentState setAllowsAccessibilitySwitchControl:]
+ -[AEAssessmentState setAllowsAccessibilityVoiceControl:]
+ -[AEAssessmentState setAllowsAccessibilityVoiceOver:]
+ -[AEAssessmentState setAllowsAccessibilityZoom:]
+ -[AEAssessmentState setAllowsAutoFill:]
+ -[AEAssessmentState setAllowsDock:]
+ -[AEAssessmentState setAllowsMenuBar:]
+ -[AEAssessmentState setAllowsStructuralInput:]
+ -[AEAssessmentState setAllowsUserScriptExecution:]
+ -[AEAssessmentState setMaxBluetoothDevicesAllowed:]
+ -[AEAssessmentState setRequiresManagedDevice:]
+ -[AEAssessmentState setRequiresSIP:]
+ -[AEAssessmentState setRequiresSingleUser:]
+ -[AEAssessmentState setRequiresUserAccountType:]
+ -[AEAssessmentState set_allowedCollaborationIDs:]
+ -[AEAssessmentState set_allowsAirPlay:]
+ -[AEAssessmentState set_allowsDonatingClipboardHistoryToSpotlight:]
+ -[AEAssessmentState set_allowsSharingServices:]
+ -[AEAssessmentState set_allowsSpotlight:]
+ -[AEConcreteFeatureFlags isFullSystemExperienceAssessmentMode]
+ -[AECoreMenuBarItem .cxx_destruct]
+ -[AECoreMenuBarItem bundleIdentifier]
+ -[AECoreMenuBarItem copyWithZone:]
+ -[AECoreMenuBarItem description]
+ -[AECoreMenuBarItem encodeWithCoder:]
+ -[AECoreMenuBarItem hash]
+ -[AECoreMenuBarItem initWithCoder:]
+ -[AECoreMenuBarItem initWithSystemItemIdentifier:bundleIdentifier:]
+ -[AECoreMenuBarItem isEqual:]
+ -[AECoreMenuBarItem setBundleIdentifier:]
+ -[AECoreMenuBarItem setSystemItemIdentifier:]
+ -[AECoreMenuBarItem systemItemIdentifier]
+ -[AEPreferences allowWritingTools]
+ -[NSData(AEAdditions) ae_hexString]
+ _OBJC_CLASS_$_AECoreMenuBarItem
+ _OBJC_IVAR_$_AEAssessmentIndividualConfiguration._allowedMenuItems
+ _OBJC_IVAR_$_AEAssessmentState.__allowedCollaborationIDs
+ _OBJC_IVAR_$_AEAssessmentState.__allowsAirPlay
+ _OBJC_IVAR_$_AEAssessmentState.__allowsDonatingClipboardHistoryToSpotlight
+ _OBJC_IVAR_$_AEAssessmentState.__allowsSharingServices
+ _OBJC_IVAR_$_AEAssessmentState.__allowsSpotlight
+ _OBJC_IVAR_$_AEAssessmentState._allowLockdownMode
+ _OBJC_IVAR_$_AEAssessmentState._allowOnlyParticipantsToRun
+ _OBJC_IVAR_$_AEAssessmentState._allowPrivateRelay
+ _OBJC_IVAR_$_AEAssessmentState._allowedAppleMenuItems
+ _OBJC_IVAR_$_AEAssessmentState._allowedBluetoothDeviceNames
+ _OBJC_IVAR_$_AEAssessmentState._allowedBluetoothProfiles
+ _OBJC_IVAR_$_AEAssessmentState._allowedDirectoriesAndFiles
+ _OBJC_IVAR_$_AEAssessmentState._allowedMenuBarItems
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityAlternativeInputMethods
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityBackgroundSounds
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityHoverText
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityLiveSpeech
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilitySpokenContent
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilitySwitchControl
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityVoiceControl
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityVoiceOver
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityZoom
+ _OBJC_IVAR_$_AEAssessmentState._allowsAutoFill
+ _OBJC_IVAR_$_AEAssessmentState._allowsDock
+ _OBJC_IVAR_$_AEAssessmentState._allowsMenuBar
+ _OBJC_IVAR_$_AEAssessmentState._allowsStructuralInput
+ _OBJC_IVAR_$_AEAssessmentState._allowsUserScriptExecution
+ _OBJC_IVAR_$_AEAssessmentState._maxBluetoothDevicesAllowed
+ _OBJC_IVAR_$_AEAssessmentState._requiresManagedDevice
+ _OBJC_IVAR_$_AEAssessmentState._requiresSIP
+ _OBJC_IVAR_$_AEAssessmentState._requiresSingleUser
+ _OBJC_IVAR_$_AEAssessmentState._requiresUserAccountType
+ _OBJC_IVAR_$_AECoreMenuBarItem._bundleIdentifier
+ _OBJC_IVAR_$_AECoreMenuBarItem._systemItemIdentifier
+ _OBJC_METACLASS_$_AECoreMenuBarItem
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_AEAdditions
+ __OBJC_$_CATEGORY_NSData_$_AEAdditions
+ __OBJC_$_CLASS_METHODS_AECoreMenuBarItem
+ __OBJC_$_CLASS_PROP_LIST_AECoreMenuBarItem
+ __OBJC_$_INSTANCE_METHODS_AEConcreteFeatureFlags
+ __OBJC_$_INSTANCE_METHODS_AECoreMenuBarItem
+ __OBJC_$_INSTANCE_VARIABLES_AECoreMenuBarItem
+ __OBJC_$_PROP_LIST_AECoreMenuBarItem
+ __OBJC_$_PROP_LIST_AEFeatureFlags
+ __OBJC_$_PROP_LIST_NSData_$_AEAdditions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEFeatureFlags
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEFeatureFlags
+ __OBJC_CLASS_PROTOCOLS_$_AECoreMenuBarItem
+ __OBJC_CLASS_RO_$_AECoreMenuBarItem
+ __OBJC_METACLASS_RO_$_AECoreMenuBarItem
+ __os_feature_enabled_impl
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_allowedCollaborationIDs
+ _objc_msgSend$_allowsAirPlay
+ _objc_msgSend$_allowsDonatingClipboardHistoryToSpotlight
+ _objc_msgSend$_allowsSharingServices
+ _objc_msgSend$_allowsSpotlight
+ _objc_msgSend$allowLockdownMode
+ _objc_msgSend$allowOnlyParticipantsToRun
+ _objc_msgSend$allowPrivateRelay
+ _objc_msgSend$allowedAppleMenuItems
+ _objc_msgSend$allowedBluetoothDeviceNames
+ _objc_msgSend$allowedBluetoothProfiles
+ _objc_msgSend$allowedDirectoriesAndFiles
+ _objc_msgSend$allowedMenuBarItems
+ _objc_msgSend$allowedMenuItems
+ _objc_msgSend$allowsAccessibilityAlternativeInputMethods
+ _objc_msgSend$allowsAccessibilityBackgroundSounds
+ _objc_msgSend$allowsAccessibilityHoverText
+ _objc_msgSend$allowsAccessibilityLiveSpeech
+ _objc_msgSend$allowsAccessibilitySpokenContent
+ _objc_msgSend$allowsAccessibilitySwitchControl
+ _objc_msgSend$allowsAccessibilityVoiceControl
+ _objc_msgSend$allowsAccessibilityVoiceOver
+ _objc_msgSend$allowsAccessibilityZoom
+ _objc_msgSend$allowsAutoFill
+ _objc_msgSend$allowsDock
+ _objc_msgSend$allowsMenuBar
+ _objc_msgSend$allowsStructuralInput
+ _objc_msgSend$allowsUserScriptExecution
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$maxBluetoothDevicesAllowed
+ _objc_msgSend$requiresManagedDevice
+ _objc_msgSend$requiresSIP
+ _objc_msgSend$requiresSingleUser
+ _objc_msgSend$requiresUserAccountType
+ _objc_msgSend$setAllowLockdownMode:
+ _objc_msgSend$setAllowOnlyParticipantsToRun:
+ _objc_msgSend$setAllowPrivateRelay:
+ _objc_msgSend$setAllowedAppleMenuItems:
+ _objc_msgSend$setAllowedBluetoothDeviceNames:
+ _objc_msgSend$setAllowedBluetoothProfiles:
+ _objc_msgSend$setAllowedDirectoriesAndFiles:
+ _objc_msgSend$setAllowedMenuBarItems:
+ _objc_msgSend$setAllowedMenuItems:
+ _objc_msgSend$setAllowsAccessibilityAlternativeInputMethods:
+ _objc_msgSend$setAllowsAccessibilityBackgroundSounds:
+ _objc_msgSend$setAllowsAccessibilityHoverText:
+ _objc_msgSend$setAllowsAccessibilityLiveSpeech:
+ _objc_msgSend$setAllowsAccessibilitySpokenContent:
+ _objc_msgSend$setAllowsAccessibilitySwitchControl:
+ _objc_msgSend$setAllowsAccessibilityVoiceControl:
+ _objc_msgSend$setAllowsAccessibilityVoiceOver:
+ _objc_msgSend$setAllowsAccessibilityZoom:
+ _objc_msgSend$setAllowsAutoFill:
+ _objc_msgSend$setAllowsDock:
+ _objc_msgSend$setAllowsMenuBar:
+ _objc_msgSend$setAllowsStructuralInput:
+ _objc_msgSend$setAllowsUserScriptExecution:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setMaxBluetoothDevicesAllowed:
+ _objc_msgSend$setRequiresManagedDevice:
+ _objc_msgSend$setRequiresSIP:
+ _objc_msgSend$setRequiresSingleUser:
+ _objc_msgSend$setRequiresUserAccountType:
+ _objc_msgSend$setSystemItemIdentifier:
+ _objc_msgSend$set_allowedCollaborationIDs:
+ _objc_msgSend$set_allowsAirPlay:
+ _objc_msgSend$set_allowsDonatingClipboardHistoryToSpotlight:
+ _objc_msgSend$set_allowsSharingServices:
+ _objc_msgSend$set_allowsSpotlight:
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$systemItemIdentifier
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x7
- -[AEPreferences disableDictation]
- GCC_except_table10
- GCC_except_table9
- _OUTLINED_FUNCTION_8
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%02x"
+ "<%@: %p { allowsNetworkAccess = %@, required = %@, allowedMenuItems = %@, configurationInfo = %@ }>"
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityAlternativeInputMethods = %@, allowsAccessibilityBackgroundSounds = %@, allowsAccessibilityHoverText = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityLiveSpeech = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilitySpokenContent = %@, allowsAccessibilitySwitchControl = %@, allowsAccessibilityTypingFeedback = %@, allowsAccessibilityVoiceControl = %@, allowsAccessibilityVoiceOver = %@, allowsAccessibilityZoom = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, allowedAppleMenuItems = %@, allowedDirectoriesAndFiles = %@, allowsAutoFill = %@, allowsStructuralInput = %@, allowsDock = %@, allowsMenuBar = %@, allowedMenuBarItems = %@, allowsUserScriptExecution = %@, allowOnlyParticipantsToRun = %@, maxBluetoothDevicesAllowed = %@, allowedBluetoothDeviceNames = %@, allowedBluetoothProfiles = %@, allowLockdownMode = %@, allowPrivateRelay = %@, requiresManagedDevice = %@, requiresSIP = %@, requiresSingleUser = %@, requiresUserAccountType = %ld, _allowedCollaborationIDs = %@, _allowsAirPlay = %@, _allowsContentCapture = %@, _allowsDonatingClipboardHistoryToSpotlight = %@, _allowsNetworkAccess = %@, _allowsSharingServices = %@, _allowsSpotlight = %@}>"
+ "<AEMenuBarItem: bundle=%@>"
+ "<AEMenuBarItem: system=%@>"
+ "AllowWritingTools"
+ "AssessmentMode"
+ "FullSystemExperienceAssessmentMode"
+ "PhoneMultiAppAssessmentMode"
+ "System checks failed."
+ "_allowedCollaborationIDs"
+ "_allowsAirPlay"
+ "_allowsDonatingClipboardHistoryToSpotlight"
+ "_allowsSharingServices"
+ "_allowsSpotlight"
+ "allowLockdownMode"
+ "allowOnlyParticipantsToRun"
+ "allowPrivateRelay"
+ "allowedAppleMenuItems"
+ "allowedBluetoothDeviceNames"
+ "allowedBluetoothProfiles"
+ "allowedDirectoriesAndFiles"
+ "allowedMenuBarItems"
+ "allowedMenuItems"
+ "allowsAccessibilityAlternativeInputMethods"
+ "allowsAccessibilityBackgroundSounds"
+ "allowsAccessibilityHoverText"
+ "allowsAccessibilityLiveSpeech"
+ "allowsAccessibilitySpokenContent"
+ "allowsAccessibilitySwitchControl"
+ "allowsAccessibilityVoiceControl"
+ "allowsAccessibilityVoiceOver"
+ "allowsAccessibilityZoom"
+ "allowsAutoFill"
+ "allowsDock"
+ "allowsMenuBar"
+ "allowsStructuralInput"
+ "allowsUserScriptExecution"
+ "maxBluetoothDevicesAllowed"
+ "requiresManagedDevice"
+ "requiresSIP"
+ "requiresSingleUser"
+ "requiresUserAccountType"
+ "systemItemIdentifier"
- "#16@0:8"
- ".cxx_destruct"
- "2"
- "<%@: %p { allowsNetworkAccess = %@, required = %@, configurationInfo = %@ }>"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilityTypingFeedback = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, _allowsNetworkAccess = %@, _allowsContentCapture = %@}>"
- "@"
- "@\"<AEAccessibilityServerPrimitives>\""
- "@\"<AEAssessmentModeRestrictionEnforcer>\""
- "@\"<AEFileSystemPrimitives>\""
- "@\"<AEInvalidationRouterDelegate>\""
- "@\"<AEObservation>\""
- "@\"<AEObservation>\"32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?>24"
- "@\"<AEObservation>\"40@0:8@\"NSString\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?>32"
- "@\"<AEPerformancePrimitives>\""
- "@\"<AEPerformancePrimitivesInFlightInterval>\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"<AEPolicyDeactivation>\""
- "@\"<AEPolicyStore>\""
- "@\"<AEPreferencePrimitives>\""
- "@\"<AESystemNotificationPrimitives>\""
- "@\"<AEXPCConnectionOrigin>\""
- "@\"AEAssessmentIndividualConfiguration\""
- "@\"AEInvalidationRouter\""
- "@\"AEOSGestalt\""
- "@\"AEXPCProxy\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMapTable\""
- "@\"NSObject<AEAssessmentStateReading>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCConnection\"16@0:8"
- "@\"NSXPCInterface\""
- "@\"NSXPCListener\""
- "@\"NSXPCListenerEndpoint\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16r*24"
- "@32@0:8^@16@?24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@48@0:8@16@24@32@40"
- "@64@0:8@16@24@32@40@48@56"
- "@?"
- "@?16@0:8"
- "@?<v@?>16@0:8"
- "AEAccessibilityServerBackedAssessmentStateReader"
- "AEAccessibilityServerPrimitives"
- "AEActivationPool"
- "AEActivePolicySession"
- "AEActiveRestrictionUUIDFetching"
- "AEActiveRestrictionUUIDFetchingProxy"
- "AEActiveRestrictionUUIDFetchingXPCInterfaceFactory"
- "AEAdditions"
- "AEAnonymousXPCConnectionOrigin"
- "AEAssessmentAgentService"
- "AEAssessmentApplicationDescriptor"
- "AEAssessmentIndividualConfiguration"
- "AEAssessmentModeGestalt"
- "AEAssessmentModeRestrictionEnforcementSession"
- "AEAssessmentModeRestrictionEnforcer"
- "AEAssessmentModeRestrictionEnforcerProxy"
- "AEAssessmentState"
- "AEAssessmentStatePublishing"
- "AEAssessmentStatePublishingProxy"
- "AEAssessmentStatePublishingXPCInterfaceFactory"
- "AEAssessmentStateReading"
- "AEAssessmentStateSourceRegistering"
- "AEAssessmentStateSourceRegisteringProxy"
- "AEAssessmentStateSourceRegisteringXPCInterfaceFactory"
- "AEAssessmentUIConfiguration"
- "AEAssessmentUIService"
- "AEAssessmentUIServiceProxy"
- "AEAssessmentUIServiceXPCInterfaceFactory"
- "AECompositeAssessmentStateReader"
- "AEConcreteAccessibilityServerPrimitives"
- "AEConcreteDevicePrimitives"
- "AEConcreteFeatureFlags"
- "AEConcreteFileSystemPrimitives"
- "AEConcretePerformancePrimitives"
- "AEConcretePerformancePrimitivesInFlightInterval"
- "AEConcretePreferencePrimitives"
- "AEConcreteProcessInfoPrimitives"
- "AEConcreteSystemNotificationPrimitives"
- "AEDeactivationPool"
- "AEDevicePrimitives"
- "AEDevicePrimitivesProvider"
- "AEEmptyPerformancePrimitives"
- "AEEmptyPerformancePrimitivesInFlightInterval"
- "AEFeatureFlags"
- "AEFeatureFlagsProvider"
- "AEFileBackedAssessmentStateReader"
- "AEFileSystem"
- "AEFileSystemPrimitives"
- "AEInvalidatable"
- "AEInvalidationRouter"
- "AEInvalidationRouterDelegate"
- "AELifecycleEventHandling"
- "AELifecycleEventHandlingProxy"
- "AELifecycleEventHandlingXPCInterfaceFactory"
- "AELocalizedErrorDescriptions"
- "AEMachServiceXPCConnectionOrigin"
- "AEOSGestalt"
- "AEObservation"
- "AEOptionMirror"
- "AEPerformancePrimitives"
- "AEPerformancePrimitivesInFlightInterval"
- "AEPerformancePrimitivesProvider"
- "AEPersistentDeactivation"
- "AEPolicyBundle"
- "AEPolicySession"
- "AEPreference"
- "AEPreferencePrimitives"
- "AEPreferences"
- "AEProcessInfoPrimitives"
- "AEProcessInfoPrimitivesProvider"
- "AERecoveryPolicySession"
- "AEServiceXPCConnectionOrigin"
- "AESystemNotificationObservation"
- "AESystemNotificationPrimitives"
- "AEXPCConnection"
- "AEXPCConnectionOrigin"
- "AEXPCProxy"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"NSURL\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "DisableDication"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<AEObservation>\",R,N,V_notificationObservation"
- "T@\"<AEPreferencePrimitives>\",R,N,V_preferencePrimitives"
- "T@\"<AESystemNotificationPrimitives>\",R,N,V_systemNotificationPrimitives"
- "T@\"AEAssessmentIndividualConfiguration\",&,N,V_mainIndividualConfiguration"
- "T@\"AEPreference\",R,N"
- "T@\"NSData\",R,C,N"
- "T@\"NSDictionary\",C,N,V_configurationInfo"
- "T@\"NSDictionary\",C,N,V_configurationsByApplicationDescriptor"
- "T@\"NSMapTable\",R,N,V_cachedPreferencesByKey"
- "T@\"NSObject<AEAssessmentStateReading>\",R,N,V_assessmentStateReader"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_key"
- "T@\"NSString\",R,C,N,V_notificationName"
- "T@\"NSString\",R,C,N,V_teamIdentifier"
- "T@\"NSURL\",R,N"
- "T@,&,N"
- "T@,C,N,V_value"
- "T@,R,N,V_defaultValue"
- "T@?,C,N"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_notificationHandler"
- "T@?,R,N"
- "TB,N,GisActive,V_active"
- "TB,N,GisEnabled,V_enabled"
- "TB,N,GisRequired,V_required"
- "TB,N,V__allowsContentCapture"
- "TB,N,V__allowsNetworkAccess"
- "TB,N,V_allowsAccessibilityKeyboard"
- "TB,N,V_allowsAccessibilityLiveCaptions"
- "TB,N,V_allowsAccessibilityReader"
- "TB,N,V_allowsAccessibilitySpeech"
- "TB,N,V_allowsAccessibilityTypingFeedback"
- "TB,N,V_allowsActivityContinuation"
- "TB,N,V_allowsAutoCorrection"
- "TB,N,V_allowsContinuousPathKeyboard"
- "TB,N,V_allowsDictation"
- "TB,N,V_allowsEmojiKeyboard"
- "TB,N,V_allowsKeyboardMathSolving"
- "TB,N,V_allowsKeyboardShortcuts"
- "TB,N,V_allowsMathPaperSolving"
- "TB,N,V_allowsNetworkAccess"
- "TB,N,V_allowsPasswordAutoFill"
- "TB,N,V_allowsPredictiveKeyboard"
- "TB,N,V_allowsScreenshots"
- "TB,N,V_allowsSmartPunctuation"
- "TB,N,V_allowsSpellCheck"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisActive"
- "TB,R,N,GisOverridden,V_overridden"
- "TB,R,N,GisRestrictedForAAC"
- "TB,R,N,GshouldCaptureDisplays,V_captureDisplays"
- "TB,R,N,GshouldPresentDisplayShields,V_presentDisplayShields"
- "TB,R,N,V_requiresSignatureValidation"
- "TQ,R"
- "Td,R"
- "Tq,R,N"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_AECoreErrorHelper"
- "_OSGestalt"
- "__allowsContentCapture"
- "__allowsNetworkAccess"
- "_accessibilityServerPrimitives"
- "_accessibilityServerReader"
- "_activation"
- "_activations"
- "_active"
- "_allowsAccessibilityKeyboard"
- "_allowsAccessibilityLiveCaptions"
- "_allowsAccessibilityReader"
- "_allowsAccessibilitySpeech"
- "_allowsAccessibilityTypingFeedback"
- "_allowsActivityContinuation"
- "_allowsAutoCorrection"
- "_allowsContinuousPathKeyboard"
- "_allowsDictation"
- "_allowsEmojiKeyboard"
- "_allowsKeyboardMathSolving"
- "_allowsKeyboardShortcuts"
- "_allowsMathPaperSolving"
- "_allowsPasswordAutoFill"
- "_allowsPredictiveKeyboard"
- "_allowsScreenshots"
- "_allowsSmartPunctuation"
- "_allowsSpellCheck"
- "_assessmentFileURL"
- "_assessmentStateReader"
- "_bundleIdentifier"
- "_cachedPreferencesByKey"
- "_captureDisplays"
- "_configurationInfo"
- "_configurationsByApplicationDescriptor"
- "_connection"
- "_deactivation"
- "_defaultValue"
- "_delegate"
- "_deviceTypeInternal"
- "_domain"
- "_enabled"
- "_endpoint"
- "_enforcer"
- "_fileBackedReader"
- "_fileSystemPrimitives"
- "_forwardError"
- "_guidedAccessActiveStateChangeObservation"
- "_interface"
- "_interruptionHandler"
- "_invalidationHandler"
- "_invalidationRouter"
- "_isEnded"
- "_key"
- "_leftOptionsByRight"
- "_log"
- "_machServiceName"
- "_mainIndividualConfiguration"
- "_mode"
- "_name"
- "_notificationHandler"
- "_notificationName"
- "_notificationObservation"
- "_options"
- "_origin"
- "_overridden"
- "_performancePrimitives"
- "_persistentDeactivations"
- "_policyStore"
- "_preferencePrimitives"
- "_presentDisplayShields"
- "_processedInvalidation"
- "_proxy"
- "_queue"
- "_required"
- "_requiresSignatureValidation"
- "_rightOptionsByLeft"
- "_scratchpadIdentifier"
- "_serviceName"
- "_signpostID"
- "_stateChangeNotificationObservation"
- "_storedError"
- "_subsystem"
- "_systemNotificationPrimitives"
- "_teamIdentifier"
- "_value"
- "_xpcListener"
- "_xpcProxy"
- "activate"
- "activateSessionWithCompletion:"
- "activateWithConfiguration:completion:"
- "activateWithScratchpad:invalidationHandler:completion:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "ae_adding:"
- "ae_addingItems:"
- "ae_dataRepresentation"
- "ae_filter:"
- "ae_firstMatching:"
- "ae_forEach:"
- "ae_hasEntitlement:withValue:"
- "ae_isBeingTested"
- "ae_map:"
- "ae_poppingFirstItem:"
- "ae_removeFirstMatching:"
- "ae_removing:"
- "ae_split:includeBlock:"
- "ae_valueFromData:ofObjCType:"
- "ae_verboseDescription"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowRemotelyKillingAgent"
- "animateInWithCompletion:"
- "animateOutWithCompletion:"
- "appendFormat:"
- "arrayWithObjects:count:"
- "assessmentAgentContainerURL"
- "assessmentAgentPolicyStoreDirectoryURL"
- "assessmentAgentRecoveryMarkerStoreDirectoryURL"
- "assessmentModeFileURL"
- "assessmentStateReader"
- "autorelease"
- "beginIntervalWithCategory:name:"
- "beginObserving"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "cStringUsingEncoding:"
- "cachedPreferencesByKey"
- "class"
- "cleanUpPolicyStoreWithError:"
- "code"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAssessmentFile"
- "currentHandler"
- "d16@0:8"
- "daemonProxyWithQueue:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "deactivateWithCompletion:"
- "deactivationForScratchpad:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultPreferences"
- "defaultValue"
- "description"
- "deviceRecoveryOperations"
- "deviceType"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "disableContinuity"
- "disableDictation"
- "disableMultitaskingModes"
- "disableQuickNote"
- "disableSiri"
- "disableSystemHotKeys"
- "disableTrackpadLookup"
- "domain"
- "elevateWindows"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endInterval"
- "endPublications:"
- "enforceSingleAppMode"
- "enterSandbox"
- "enumerateKeysAndObjectsUsingBlock:"
- "environment"
- "errorWithDomain:code:userInfo:"
- "event"
- "exists"
- "expirationTime"
- "failOnDeactivation"
- "fetchCapturedErrorWithCompletion:"
- "fetchSetOfActiveRestrictionUUIDsWithClientType:completion:"
- "fileExistsAtURL:"
- "fileURLWithPath:isDirectory:"
- "fire"
- "forceScreenMirroring"
- "formattedCode:"
- "getValue:"
- "handleEventDidBeginWithCompletion:"
- "handleEventDidInvalidateWithError:completion:"
- "handleEventWantsBeginSingleAppModeWithCompletion:"
- "handleEventWantsEndSingleAppModeWithCompletion:"
- "handleEventWantsPresentBannerWithTitle:duration:completion:"
- "handleEventWantsStartWindowContentCaptureWithCompletion:"
- "handleEventWantsStopWindowContentCaptureWithCompletion:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasEntitlement:"
- "hasPersistentData"
- "hash"
- "identifier"
- "indexOfObjectPassingTest:"
- "init"
- "initWithAccessibilityServerPrimitives:queue:"
- "initWithBundleIdentifier:teamIdentifier:requiresSignatureValidation:"
- "initWithCoder:"
- "initWithDomain:"
- "initWithFileBackedReader:accessibilityServerReader:"
- "initWithKey:preferencesPrimitives:systemNotificationPrimitives:defaultValue:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithMachServiceName:queue:"
- "initWithMirroredOptions:"
- "initWithNotificationName:queue:notificationHandler:"
- "initWithPolicyStore:performancePrimitives:activations:queue:"
- "initWithPreferencePrimitives:systemNotificationPrimitives:queue:"
- "initWithPresentDisplayShields:captureDisplays:"
- "initWithQueue:"
- "initWithServiceName:"
- "initWithSystemNotificationPrimitives:fileSystemPrimitives:assessmentFileURL:queue:"
- "integerValue"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "invalidationRouter:didReceiveInvalidationError:"
- "isActive"
- "isBeingTested"
- "isEnabled"
- "isEqual:"
- "isFailable"
- "isInternalOS"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOverridden"
- "isProxy"
- "isRequired"
- "isRestrictedForAAC"
- "key"
- "keyPathsForValuesAffectingActive"
- "leftClearMask"
- "leftOptionsFromRight:"
- "length"
- "listener:shouldAcceptNewConnection:"
- "localizedDescription"
- "localizedRecoverySuggestion"
- "localizedStringForKey:value:table:"
- "makeAssessmentStateReaderWithQueue:"
- "makeConnection"
- "makeFeatureFlags"
- "makeInterface"
- "makePrimitives"
- "mutableCopy"
- "networkPolicyExemptExecutablePaths"
- "notificationHandler"
- "notificationName"
- "notificationObservation"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "objCType"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observationWithNotificationName:queue:notificationHandler:"
- "observeGuidedAccessActiveStateChangeOnQueue:withHandler:"
- "observeSystemNotificationWithName:onQueue:withHandler:"
- "observeValueForKeyPath:ofObject:change:context:"
- "overridden"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postSystemNotificationWithName:"
- "preferenceDidUpdate"
- "preferenceForKey:defaultArrayValue:"
- "preferenceForKey:defaultNumberValue:"
- "preferencePrimitives"
- "preferenceValue"
- "preferencesDidUpdate"
- "preferencesWithPreferencePrimitives:systemNotificationPrimitives:queue:"
- "presentShields"
- "processInfo"
- "propertyList:isValidForFormat:"
- "proxyWithEndpoint:queue:"
- "publishAssessmentState:withCompletion:"
- "q"
- "q16@0:8"
- "q24@0:8q16"
- "queue"
- "readOnlyScratchpadForIdentifier:"
- "recoverySession"
- "registerPublisherWithLifetimeEndpoint:completion:"
- "registerRestrictionEnforcer:machServiceName:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:forKeyPath:context:"
- "removeWithError:"
- "respondsToSelector:"
- "restrictContentCapture"
- "restrictFrontmostApp"
- "restrictMedia"
- "restrictNetworkAccess"
- "restrictedForAAC"
- "resume"
- "retain"
- "retainCount"
- "rightClearMask"
- "rightOptionsFromLeft:"
- "scrubPasteboard"
- "self"
- "server"
- "serviceProxyWithQueue:"
- "sessionWithPolicyStore:performancePrimitives:invalidationRouter:activations:persistentDeactivations:queue:"
- "setActive:"
- "setAllowsAccessibilityKeyboard:"
- "setAllowsAccessibilityLiveCaptions:"
- "setAllowsAccessibilityReader:"
- "setAllowsAccessibilitySpeech:"
- "setAllowsAccessibilityTypingFeedback:"
- "setAllowsActivityContinuation:"
- "setAllowsAutoCorrection:"
- "setAllowsContinuousPathKeyboard:"
- "setAllowsDictation:"
- "setAllowsEmojiKeyboard:"
- "setAllowsKeyboardMathSolving:"
- "setAllowsKeyboardShortcuts:"
- "setAllowsMathPaperSolving:"
- "setAllowsNetworkAccess:"
- "setAllowsPasswordAutoFill:"
- "setAllowsPredictiveKeyboard:"
- "setAllowsScreenshots:"
- "setAllowsSmartPunctuation:"
- "setAllowsSpellCheck:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfigurationInfo:"
- "setConfigurationsByApplicationDescriptor:"
- "setCustomHomeScreenLayout"
- "setDelegate:"
- "setEnabled:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMainIndividualConfiguration:"
- "setNotificationHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOfActiveRestrictionUUIDs:"
- "setPreferenceValue:"
- "setRemoteObjectInterface:"
- "setRequired:"
- "setRouterDelegate:"
- "setRouterMode:"
- "setValue:"
- "setWithObject:"
- "setWithObjects:"
- "set_allowsContentCapture:"
- "set_allowsNetworkAccess:"
- "shouldBeginRestrictingForAssessmentModeWithCompletion:"
- "shouldCaptureDisplays"
- "shouldEndRestrictingForAssessmentModeWithCompletion:"
- "shouldPresentDisplayShields"
- "showPromptsAndBanners"
- "stopAirPlayBeforehand"
- "stringByAppendingFormat:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemNotificationPrimitives"
- "systemUptime"
- "uninstallConfigurationProfile"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8q16"
- "v32@0:8@\"AEAssessmentState\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AEAssessmentUIConfiguration\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AEInvalidationRouter\"16@\"NSError\"24"
- "v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSObject\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32^v40"
- "validateProducedPersistentDeactivations:currentEvent:"
- "value"
- "valueForEntitlement:"
- "valueWithBytes:objCType:"
- "verboseDescriptionWithIndentation:"
- "writeOnlyScratchpadForIdentifier:"
- "zone"

```

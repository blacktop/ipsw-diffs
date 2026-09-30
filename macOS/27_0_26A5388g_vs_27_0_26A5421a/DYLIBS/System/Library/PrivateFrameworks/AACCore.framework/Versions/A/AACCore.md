## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/Versions/A/AACCore`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x139a8
-  __TEXT.__objc_methlist: 0x1a54
+56.1.1.0.0
+  __TEXT.__text: 0x140f0
+  __TEXT.__objc_methlist: 0x1aec
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1aa0
+  __TEXT.__cstring: 0x1c5b
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__unwind_info: 0x5a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc8
+  __DATA_CONST.__objc_selrefs: 0xd40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x1640
-  __AUTH_CONST.__objc_const: 0x46f8
+  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__objc_const: 0x4808
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x9f8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1130

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 641
-  Symbols:   1806
-  CStrings:  223
+  Functions: 655
+  Symbols:   1836
+  CStrings:  232
 
Symbols:
+ -[AEAssessmentApplicationDescriptor executablePath]
+ -[AEAssessmentApplicationDescriptor initWithExecutablePath:teamIdentifier:requiresSignatureValidation:]
+ -[AEAssessmentState _allowsAccessibilityIntelligence]
+ -[AEAssessmentState _allowsVisualIntelligence]
+ -[AEAssessmentState allowsForceQuitKeyboardShortcuts]
+ -[AEAssessmentState allowsLockdownMode]
+ -[AEAssessmentState allowsOnlyParticipantsToRun]
+ -[AEAssessmentState allowsPrivateRelay]
+ -[AEAssessmentState allowsVirtualMachine]
+ -[AEAssessmentState requiresReleaseOS]
+ -[AEAssessmentState setAllowsForceQuitKeyboardShortcuts:]
+ -[AEAssessmentState setAllowsLockdownMode:]
+ -[AEAssessmentState setAllowsOnlyParticipantsToRun:]
+ -[AEAssessmentState setAllowsPrivateRelay:]
+ -[AEAssessmentState setAllowsVirtualMachine:]
+ -[AEAssessmentState setRequiresReleaseOS:]
+ -[AEAssessmentState set_allowsAccessibilityIntelligence:]
+ -[AEAssessmentState set_allowsVisualIntelligence:]
+ -[AEConcreteFeatureFlags isAirPlayRestrictionsEnabled]
+ -[AEOSGestalt isPrereleaseOS]
+ -[AEPreferences useDeviceConfigurationProvider]
+ OBJC_IVAR_$_AEAssessmentApplicationDescriptor._executablePath
+ OBJC_IVAR_$_AEAssessmentState.__allowsAccessibilityIntelligence
+ OBJC_IVAR_$_AEAssessmentState.__allowsVisualIntelligence
+ OBJC_IVAR_$_AEAssessmentState._allowsForceQuitKeyboardShortcuts
+ OBJC_IVAR_$_AEAssessmentState._allowsLockdownMode
+ OBJC_IVAR_$_AEAssessmentState._allowsOnlyParticipantsToRun
+ OBJC_IVAR_$_AEAssessmentState._allowsPrivateRelay
+ OBJC_IVAR_$_AEAssessmentState._allowsVirtualMachine
+ OBJC_IVAR_$_AEAssessmentState._requiresReleaseOS
+ _MGCopyAnswer
+ _objc_msgSend$_allowsAccessibilityIntelligence
+ _objc_msgSend$_allowsVisualIntelligence
+ _objc_msgSend$allowsForceQuitKeyboardShortcuts
+ _objc_msgSend$allowsLockdownMode
+ _objc_msgSend$allowsOnlyParticipantsToRun
+ _objc_msgSend$allowsPrivateRelay
+ _objc_msgSend$allowsVirtualMachine
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$executablePath
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$requiresReleaseOS
+ _objc_msgSend$setAllowsForceQuitKeyboardShortcuts:
+ _objc_msgSend$setAllowsLockdownMode:
+ _objc_msgSend$setAllowsOnlyParticipantsToRun:
+ _objc_msgSend$setAllowsPrivateRelay:
+ _objc_msgSend$setAllowsVirtualMachine:
+ _objc_msgSend$setRequiresReleaseOS:
+ _objc_msgSend$set_allowsAccessibilityIntelligence:
+ _objc_msgSend$set_allowsVisualIntelligence:
- -[AEAssessmentState allowLockdownMode]
- -[AEAssessmentState allowOnlyParticipantsToRun]
- -[AEAssessmentState allowPrivateRelay]
- -[AEAssessmentState setAllowLockdownMode:]
- -[AEAssessmentState setAllowOnlyParticipantsToRun:]
- -[AEAssessmentState setAllowPrivateRelay:]
- -[NSData(AEAdditions) ae_hexString]
- OBJC_IVAR_$_AEAssessmentState._allowLockdownMode
- OBJC_IVAR_$_AEAssessmentState._allowOnlyParticipantsToRun
- OBJC_IVAR_$_AEAssessmentState._allowPrivateRelay
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_AEAdditions
- __OBJC_$_CATEGORY_NSData_$_AEAdditions
- __OBJC_$_PROP_LIST_NSData_$_AEAdditions
- _objc_msgSend$allowLockdownMode
- _objc_msgSend$allowOnlyParticipantsToRun
- _objc_msgSend$allowPrivateRelay
- _objc_msgSend$setAllowLockdownMode:
- _objc_msgSend$setAllowOnlyParticipantsToRun:
- _objc_msgSend$setAllowPrivateRelay:
- _objc_msgSend$stringWithCapacity:
CStrings:
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@, pid = %@, executablePath = %@ }>"
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityAlternativeInputMethods = %@, allowsAccessibilityBackgroundSounds = %@, allowsAccessibilityFullKeyboardAccess = %@, allowsAccessibilityHoverText = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityLiveSpeech = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilitySpokenContent = %@, allowsAccessibilitySwitchControl = %@, allowsAccessibilityTypingFeedback = %@, allowsAccessibilityVoiceControl = %@, allowsAccessibilityVoiceOver = %@, allowsAccessibilityZoom = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, allowedAppleMenuItems = %@, allowedDirectoriesAndFiles = %@, allowsAutoFill = %@, allowsStructuralInput = %@, allowsDock = %@, allowsMenuBar = %@, allowedMenuBarItems = %@, allowsUserScriptExecution = %@, allowsOnlyParticipantsToRun = %@, allowsForceQuitKeyboardShortcuts = %@, maxBluetoothDevicesAllowed = %@, allowedBluetoothDeviceNames = %@, allowedBluetoothProfiles = %@, allowsLockdownMode = %@, allowsPrivateRelay = %@, allowsVirtualMachine = %@, requiresManagedDevice = %@, requiresReleaseOS = %@, requiresSIP = %@, requiresSingleUser = %@, requiresUserAccountType = %ld, _allowedCollaborationIDs = %@, _allowsAccessibilityIntelligence = %@, _allowsAirPlay = %@, _allowsContentCapture = %@, _allowsDonatingClipboardHistoryToSpotlight = %@, _allowsNetworkAccess = %@, _allowsSharingServices = %@, _allowsSpotlight = %@, _allowsVisualIntelligence = %@}>"
+ "AirPlayRestrictions"
+ "ReleaseType"
+ "UseDeviceConfigurationProvider"
+ "_allowsAccessibilityIntelligence"
+ "_allowsVisualIntelligence"
+ "allowsForceQuitKeyboardShortcuts"
+ "allowsLockdownMode"
+ "allowsOnlyParticipantsToRun"
+ "allowsPrivateRelay"
+ "allowsVirtualMachine"
+ "executablePath"
+ "requiresReleaseOS"
- "%02x"
- "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@, pid = %@ }>"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityAlternativeInputMethods = %@, allowsAccessibilityBackgroundSounds = %@, allowsAccessibilityFullKeyboardAccess = %@, allowsAccessibilityHoverText = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityLiveSpeech = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilitySpokenContent = %@, allowsAccessibilitySwitchControl = %@, allowsAccessibilityTypingFeedback = %@, allowsAccessibilityVoiceControl = %@, allowsAccessibilityVoiceOver = %@, allowsAccessibilityZoom = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, allowedAppleMenuItems = %@, allowedDirectoriesAndFiles = %@, allowsAutoFill = %@, allowsStructuralInput = %@, allowsDock = %@, allowsMenuBar = %@, allowedMenuBarItems = %@, allowsUserScriptExecution = %@, allowOnlyParticipantsToRun = %@, maxBluetoothDevicesAllowed = %@, allowedBluetoothDeviceNames = %@, allowedBluetoothProfiles = %@, allowLockdownMode = %@, allowPrivateRelay = %@, requiresManagedDevice = %@, requiresSIP = %@, requiresSingleUser = %@, requiresUserAccountType = %ld, _allowedCollaborationIDs = %@, _allowsAirPlay = %@, _allowsContentCapture = %@, _allowsDonatingClipboardHistoryToSpotlight = %@, _allowsNetworkAccess = %@, _allowsSharingServices = %@, _allowsSpotlight = %@}>"
- "allowLockdownMode"
- "allowOnlyParticipantsToRun"
- "allowPrivateRelay"
```

## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x11f20
-  __TEXT.__objc_methlist: 0x1a7c
+56.0.0.0.0
+  __TEXT.__text: 0x1201c
+  __TEXT.__objc_methlist: 0x1a94
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1a29
+  __TEXT.__cstring: 0x1a7b
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__unwind_info: 0x598

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_selrefs: 0xcc0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1640
-  __AUTH_CONST.__objc_const: 0x47b0
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x47e0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x288
+  __DATA.__objc_ivar: 0x28c
   __DATA.__data: 0xa58
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__objc_data: 0x1180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 611
-  Symbols:   1806
-  CStrings:  223
+  Functions: 613
+  Symbols:   1811
+  CStrings:  224
 
Symbols:
+ -[AEAssessmentState allowsAccessibilityFullKeyboardAccess]
+ -[AEAssessmentState setAllowsAccessibilityFullKeyboardAccess:]
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilityFullKeyboardAccess
+ _objc_msgSend$allowsAccessibilityFullKeyboardAccess
+ _objc_msgSend$setAllowsAccessibilityFullKeyboardAccess:
CStrings:
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityAlternativeInputMethods = %@, allowsAccessibilityBackgroundSounds = %@, allowsAccessibilityFullKeyboardAccess = %@, allowsAccessibilityHoverText = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityLiveSpeech = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilitySpokenContent = %@, allowsAccessibilitySwitchControl = %@, allowsAccessibilityTypingFeedback = %@, allowsAccessibilityVoiceControl = %@, allowsAccessibilityVoiceOver = %@, allowsAccessibilityZoom = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, allowedAppleMenuItems = %@, allowedDirectoriesAndFiles = %@, allowsAutoFill = %@, allowsStructuralInput = %@, allowsDock = %@, allowsMenuBar = %@, allowedMenuBarItems = %@, allowsUserScriptExecution = %@, allowOnlyParticipantsToRun = %@, maxBluetoothDevicesAllowed = %@, allowedBluetoothDeviceNames = %@, allowedBluetoothProfiles = %@, allowLockdownMode = %@, allowPrivateRelay = %@, requiresManagedDevice = %@, requiresSIP = %@, requiresSingleUser = %@, requiresUserAccountType = %ld, _allowedCollaborationIDs = %@, _allowsAirPlay = %@, _allowsContentCapture = %@, _allowsDonatingClipboardHistoryToSpotlight = %@, _allowsNetworkAccess = %@, _allowsSharingServices = %@, _allowsSpotlight = %@}>"
+ "allowsAccessibilityFullKeyboardAccess"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilityAlternativeInputMethods = %@, allowsAccessibilityBackgroundSounds = %@, allowsAccessibilityHoverText = %@, allowsAccessibilityKeyboard = %@, allowsAccessibilityLiveCaptions = %@, allowsAccessibilityLiveSpeech = %@, allowsAccessibilityReader = %@, allowsAccessibilitySpeech = %@, allowsAccessibilitySpokenContent = %@, allowsAccessibilitySwitchControl = %@, allowsAccessibilityTypingFeedback = %@, allowsAccessibilityVoiceControl = %@, allowsAccessibilityVoiceOver = %@, allowsAccessibilityZoom = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, allowsEmojiKeyboard = %@, allowedAppleMenuItems = %@, allowedDirectoriesAndFiles = %@, allowsAutoFill = %@, allowsStructuralInput = %@, allowsDock = %@, allowsMenuBar = %@, allowedMenuBarItems = %@, allowsUserScriptExecution = %@, allowOnlyParticipantsToRun = %@, maxBluetoothDevicesAllowed = %@, allowedBluetoothDeviceNames = %@, allowedBluetoothProfiles = %@, allowLockdownMode = %@, allowPrivateRelay = %@, requiresManagedDevice = %@, requiresSIP = %@, requiresSingleUser = %@, requiresUserAccountType = %ld, _allowedCollaborationIDs = %@, _allowsAirPlay = %@, _allowsContentCapture = %@, _allowsDonatingClipboardHistoryToSpotlight = %@, _allowsNetworkAccess = %@, _allowsSharingServices = %@, _allowsSpotlight = %@}>"
```

## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`

```diff

-28.122.2.0.0
-  __TEXT.__text: 0x3458
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x4ec
-  __TEXT.__const: 0x370
-  __TEXT.__cstring: 0x303
-  __TEXT.__swift5_typeref: 0xce
+50.0.0.0.0
+  __TEXT.__text: 0x7850
+  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__const: 0x3ae
+  __TEXT.__cstring: 0x326
+  __TEXT.__swift5_typeref: 0x12b
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_reflstr: 0x22
   __TEXT.__swift5_fieldmd: 0x1c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x11a3
-  __TEXT.__objc_methtype: 0x1ee
-  __TEXT.__objc_stubs: 0xc80
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x210
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0x68
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__objc_const: 0xfb0
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x138
+  __DATA.__objc_ivar: 0xfc
+  __DATA.__data: 0x180
   __DATA.__bss: 0x490
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: A89250CF-22F2-3325-8A53-BA3CD50FF623
-  Functions: 150
-  Symbols:   514
-  CStrings:  240
+  UUID: 7F279F36-7BE7-3C50-8E27-9A95F53ADFCE
+  Functions: 250
+  Symbols:   807
+  CStrings:  31
 
Symbols:
+ -[AEAssessmentConfiguration _allowedCollaborationIDs]
+ -[AEAssessmentConfiguration _allowsAirPlay]
+ -[AEAssessmentConfiguration _allowsDonatingClipboardHistoryToSpotlight]
+ -[AEAssessmentConfiguration _allowsSharingServices]
+ -[AEAssessmentConfiguration _allowsSpotlight]
+ -[AEAssessmentConfiguration _setAllowedCollaborationIDs:]
+ -[AEAssessmentConfiguration _setAllowsAirPlay:]
+ -[AEAssessmentConfiguration _setAllowsDonatingClipboardHistoryToSpotlight:]
+ -[AEAssessmentConfiguration _setAllowsSharingServices:]
+ -[AEAssessmentConfiguration _setAllowsSpotlight:]
+ -[AEAssessmentConfiguration allowLockdownMode]
+ -[AEAssessmentConfiguration allowOnlyParticipantsToRun]
+ -[AEAssessmentConfiguration allowPrivateRelay]
+ -[AEAssessmentConfiguration allowedAppleMenuItems]
+ -[AEAssessmentConfiguration allowedBluetoothDeviceNames]
+ -[AEAssessmentConfiguration allowedBluetoothProfiles]
+ -[AEAssessmentConfiguration allowedDirectoriesAndFiles]
+ -[AEAssessmentConfiguration allowedMenuBarItems]
+ -[AEAssessmentConfiguration allowsAccessibilityAlternativeInputMethods]
+ -[AEAssessmentConfiguration allowsAccessibilityBackgroundSounds]
+ -[AEAssessmentConfiguration allowsAccessibilityHoverText]
+ -[AEAssessmentConfiguration allowsAccessibilityLiveSpeech]
+ -[AEAssessmentConfiguration allowsAccessibilitySpokenContent]
+ -[AEAssessmentConfiguration allowsAccessibilitySwitchControl]
+ -[AEAssessmentConfiguration allowsAccessibilityVoiceControl]
+ -[AEAssessmentConfiguration allowsAccessibilityVoiceOver]
+ -[AEAssessmentConfiguration allowsAccessibilityZoom]
+ -[AEAssessmentConfiguration allowsAutoFill]
+ -[AEAssessmentConfiguration allowsDock]
+ -[AEAssessmentConfiguration allowsMenuBar]
+ -[AEAssessmentConfiguration allowsStructuralInput]
+ -[AEAssessmentConfiguration allowsUserScriptExecution]
+ -[AEAssessmentConfiguration maxBluetoothDevicesAllowed]
+ -[AEAssessmentConfiguration requiresManagedDevice]
+ -[AEAssessmentConfiguration requiresSIP]
+ -[AEAssessmentConfiguration requiresSingleUser]
+ -[AEAssessmentConfiguration requiresUserAccountType]
+ -[AEAssessmentConfiguration setAllowLockdownMode:]
+ -[AEAssessmentConfiguration setAllowOnlyParticipantsToRun:]
+ -[AEAssessmentConfiguration setAllowPrivateRelay:]
+ -[AEAssessmentConfiguration setAllowedAppleMenuItems:]
+ -[AEAssessmentConfiguration setAllowedBluetoothDeviceNames:]
+ -[AEAssessmentConfiguration setAllowedBluetoothProfiles:]
+ -[AEAssessmentConfiguration setAllowedDirectoriesAndFiles:]
+ -[AEAssessmentConfiguration setAllowedMenuBarItems:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityAlternativeInputMethods:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityBackgroundSounds:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityHoverText:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityLiveSpeech:]
+ -[AEAssessmentConfiguration setAllowsAccessibilitySpokenContent:]
+ -[AEAssessmentConfiguration setAllowsAccessibilitySwitchControl:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityVoiceControl:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityVoiceOver:]
+ -[AEAssessmentConfiguration setAllowsAccessibilityZoom:]
+ -[AEAssessmentConfiguration setAllowsAutoFill:]
+ -[AEAssessmentConfiguration setAllowsDock:]
+ -[AEAssessmentConfiguration setAllowsMenuBar:]
+ -[AEAssessmentConfiguration setAllowsStructuralInput:]
+ -[AEAssessmentConfiguration setAllowsUserScriptExecution:]
+ -[AEAssessmentConfiguration setMaxBluetoothDevicesAllowed:]
+ -[AEAssessmentConfiguration setRequiresManagedDevice:]
+ -[AEAssessmentConfiguration setRequiresSIP:]
+ -[AEAssessmentConfiguration setRequiresSingleUser:]
+ -[AEAssessmentConfiguration setRequiresUserAccountType:]
+ -[AEAssessmentParticipantConfiguration _allowedMenuItems]
+ -[AEAssessmentParticipantConfiguration _originalLanguageIdentifiers]
+ -[AEAssessmentParticipantConfiguration allowedMenuItemLanguageIdentifiers]
+ -[AEAssessmentParticipantConfiguration allowedMenuItemsForLanguageIdentifier:]
+ -[AEAssessmentParticipantConfiguration setAllowedMenuItems:forLanguageIdentifier:]
+ -[AEAssessmentParticipantConfiguration set_allowedMenuItems:]
+ -[AEAssessmentParticipantConfiguration set_originalLanguageIdentifiers:]
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowedCollaborationIDs
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsAirPlay
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsDonatingClipboardHistoryToSpotlight
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsSharingServices
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsSpotlight
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowLockdownMode
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowOnlyParticipantsToRun
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowPrivateRelay
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowedAppleMenuItems
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowedBluetoothDeviceNames
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowedBluetoothProfiles
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowedDirectoriesAndFiles
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowedMenuBarItems
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityAlternativeInputMethods
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityBackgroundSounds
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityHoverText
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityLiveSpeech
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilitySpokenContent
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilitySwitchControl
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityVoiceControl
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityVoiceOver
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAccessibilityZoom
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsAutoFill
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsDock
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsMenuBar
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsStructuralInput
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsUserScriptExecution
+ _OBJC_IVAR_$_AEAssessmentConfiguration._maxBluetoothDevicesAllowed
+ _OBJC_IVAR_$_AEAssessmentConfiguration._requiresManagedDevice
+ _OBJC_IVAR_$_AEAssessmentConfiguration._requiresSIP
+ _OBJC_IVAR_$_AEAssessmentConfiguration._requiresSingleUser
+ _OBJC_IVAR_$_AEAssessmentConfiguration._requiresUserAccountType
+ _OBJC_IVAR_$_AEAssessmentParticipantConfiguration._allowedMenuItems
+ _OBJC_IVAR_$_AEAssessmentParticipantConfiguration._originalLanguageIdentifiers
+ ___chkstk_darwin
+ ___swift_destroy_boxed_opaque_existential_0
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_malloc_size
+ _bzero
+ _malloc_size
+ _memmove
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_allowedCollaborationIDs
+ _objc_msgSend$_allowsAirPlay
+ _objc_msgSend$_allowsDonatingClipboardHistoryToSpotlight
+ _objc_msgSend$_allowsSharingServices
+ _objc_msgSend$_allowsSpotlight
+ _objc_msgSend$_originalLanguageIdentifiers
+ _objc_msgSend$addObject:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allowLockdownMode
+ _objc_msgSend$allowOnlyParticipantsToRun
+ _objc_msgSend$allowPrivateRelay
+ _objc_msgSend$allowedAppleMenuItems
+ _objc_msgSend$allowedBluetoothDeviceNames
+ _objc_msgSend$allowedBluetoothProfiles
+ _objc_msgSend$allowedDirectoriesAndFiles
+ _objc_msgSend$allowedMenuBarItems
+ _objc_msgSend$allowedMenuItemLanguageIdentifiers
+ _objc_msgSend$allowedMenuItems
+ _objc_msgSend$allowedMenuItemsForLanguageIdentifier:
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
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$maxBluetoothDevicesAllowed
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$path
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$requiresManagedDevice
+ _objc_msgSend$requiresSIP
+ _objc_msgSend$requiresSingleUser
+ _objc_msgSend$set
+ _objc_msgSend$setAllowLockdownMode:
+ _objc_msgSend$setAllowOnlyParticipantsToRun:
+ _objc_msgSend$setAllowPrivateRelay:
+ _objc_msgSend$setAllowedAppleMenuItems:
+ _objc_msgSend$setAllowedBluetoothDeviceNames:
+ _objc_msgSend$setAllowedBluetoothProfiles:
+ _objc_msgSend$setAllowedDirectoriesAndFiles:
+ _objc_msgSend$setAllowedMenuBarItems:
+ _objc_msgSend$setAllowedMenuItems:
+ _objc_msgSend$setAllowedMenuItems:forLanguageIdentifier:
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
+ _objc_msgSend$setMaxBluetoothDevicesAllowed:
+ _objc_msgSend$setRequiresManagedDevice:
+ _objc_msgSend$setRequiresSIP:
+ _objc_msgSend$setRequiresSingleUser:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$set_allowedCollaborationIDs:
+ _objc_msgSend$set_allowsAirPlay:
+ _objc_msgSend$set_allowsDonatingClipboardHistoryToSpotlight:
+ _objc_msgSend$set_allowsSharingServices:
+ _objc_msgSend$set_allowsSpotlight:
+ _objc_msgSend$set_originalLanguageIdentifiers:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_retain_x9
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRetain
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x20
+ _symbolic SS3key______5valuet 10Foundation6LocaleV8LanguageV
+ _symbolic SS______t 10Foundation6LocaleV8LanguageV
+ _symbolic _____Sg 10Foundation6LocaleV8LanguageV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 10Foundation6LocaleV8LanguageV
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G s11_SetStorageC 10Foundation6LocaleV8LanguageV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation6LocaleV8LanguageV
- _OUTLINED_FUNCTION_1
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "<%@: %p { allowsNetworkAccess = %@, required = %@, allowedMenuItems = %@, configurationInfo = %@ }>"
- ".cxx_destruct"
- "<%@: %p { allowsNetworkAccess = %@, required = %@, configurationInfo = %@ }>"
- "@\"<AEAssessmentSessionDelegate>\""
- "@\"AEAssessmentParticipantConfiguration\""
- "@\"AECAssessmentSessionWrapper\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "AEAssessmentApplication"
- "AEAssessmentConfiguration"
- "AEAssessmentParticipantConfiguration"
- "AEAssessmentSession"
- "AECAssessmentSessionWrapperDelegate"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "NSCopying"
- "Q"
- "Q16@0:8"
- "T@\"<AEAssessmentSessionDelegate>\",W,N,V_delegate"
- "T@\"AEAssessmentConfiguration\",R,C,N"
- "T@\"AEAssessmentParticipantConfiguration\",R,N"
- "T@\"NSDictionary\",C,N,V_configurationInfo"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_teamIdentifier"
- "TB,N,GisRequired,V_required"
- "TB,N,V_allowsAccessibilityKeyboard"
- "TB,N,V_allowsAccessibilityLiveCaptions"
- "TB,N,V_allowsAccessibilityReader"
- "TB,N,V_allowsAccessibilitySpeech"
- "TB,N,V_allowsAccessibilityTypingFeedback"
- "TB,N,V_allowsActivityContinuation"
- "TB,N,V_allowsContinuousPathKeyboard"
- "TB,N,V_allowsDictation"
- "TB,N,V_allowsEmojiKeyboard"
- "TB,N,V_allowsKeyboardShortcuts"
- "TB,N,V_allowsNetworkAccess"
- "TB,N,V_allowsPasswordAutoFill"
- "TB,N,V_allowsPredictiveKeyboard"
- "TB,N,V_allowsScreenshots"
- "TB,N,V_allowsSpellCheck"
- "TB,N,V_requiresSignatureValidation"
- "TB,R"
- "TB,R,N,GisActive"
- "TQ,N,V_autocorrectMode"
- "_AEErrorHelper"
- "_allowsAccessibilityKeyboard"
- "_allowsAccessibilityLiveCaptions"
- "_allowsAccessibilityReader"
- "_allowsAccessibilitySpeech"
- "_allowsAccessibilityTypingFeedback"
- "_allowsActivityContinuation"
- "_allowsContentCapture"
- "_allowsContinuousPathKeyboard"
- "_allowsDictation"
- "_allowsEmojiKeyboard"
- "_allowsKeyboardMathSolving"
- "_allowsKeyboardShortcuts"
- "_allowsMathPaperSolving"
- "_allowsNetworkAccess"
- "_allowsPasswordAutoFill"
- "_allowsPredictiveKeyboard"
- "_allowsScreenshots"
- "_allowsSpellCheck"
- "_autocorrectMode"
- "_backingConfiguratonsByApplication"
- "_bundleIdentifier"
- "_configurationInfo"
- "_delegate"
- "_mainParticipantConfiguration"
- "_required"
- "_requiresSignatureValidation"
- "_sessionWrapper"
- "_setAllowsContentCapture:"
- "_setAllowsNetworkAccess:"
- "_teamIdentifier"
- "active"
- "allocWithZone:"
- "allowsAccessibilityKeyboard"
- "allowsAccessibilityLiveCaptions"
- "allowsAccessibilityReader"
- "allowsAccessibilitySpeech"
- "allowsAccessibilityTypingFeedback"
- "allowsActivityContinuation"
- "allowsAutoCorrection"
- "allowsContinuousPathKeyboard"
- "allowsDictation"
- "allowsEmojiKeyboard"
- "allowsKeyboardMathSolving"
- "allowsKeyboardShortcuts"
- "allowsMathPaperSolving"
- "allowsNetworkAccess"
- "allowsPasswordAutoFill"
- "allowsPredictiveKeyboard"
- "allowsScreenshots"
- "allowsSmartPunctuation"
- "allowsSpellCheck"
- "applicationDescriptor"
- "assessmentSession:failedToBeginWithError:"
- "assessmentSession:failedToUpdateToConfiguration:error:"
- "assessmentSession:wasInterruptedWithError:"
- "assessmentSessionDidBegin:"
- "assessmentSessionDidEnd:"
- "assessmentSessionDidUpdate:"
- "assessmentSessionWrapper:failedToBeginWithError:"
- "assessmentSessionWrapper:failedToUpdateToConfigurationWrapper:error:"
- "assessmentSessionWrapper:wasInterruptedWithError:"
- "assessmentSessionWrapperDidBegin:"
- "assessmentSessionWrapperDidEnd:"
- "assessmentSessionWrapperDidUpdate:"
- "autocorrectMode"
- "begin"
- "bundleForClass:"
- "bundleIdentifier"
- "code"
- "configuration"
- "configurationFromWrapper:"
- "configurationInfo"
- "configurationWrapper"
- "configurationsByApplication"
- "configurationsByApplicationDescriptor"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "delegate"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "end"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "hash"
- "individualConfiguration"
- "init"
- "initWithBundleIdentifier:"
- "initWithBundleIdentifier:teamIdentifier:"
- "initWithBundleIdentifier:teamIdentifier:requiresSignatureValidation:"
- "initWithConfiguration:"
- "initWithConfigurationWrapper:queue:"
- "instanceFromApplicationDescriptor:"
- "instanceFromIndividualConfiguration:"
- "isActive"
- "isEqual:"
- "isEqualToString:"
- "isMemberOfClass:"
- "isRequired"
- "mainIndividualConfiguration"
- "mainParticipantConfiguration"
- "mutableCopy"
- "new"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "removeApplication:"
- "required"
- "requiresSignatureValidation"
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
- "setAutocorrectMode:"
- "setConfiguration:forApplication:"
- "setConfigurationInfo:"
- "setConfigurationsByApplicationDescriptor:"
- "setDelegate:"
- "setMainIndividualConfiguration:"
- "setObject:forKeyedSubscript:"
- "setRequired:"
- "setRequiresSignatureValidation:"
- "stringWithFormat:"
- "supportsConfigurationUpdates"
- "supportsMultiAppConfiguration"
- "supportsMultipleParticipants"
- "teamIdentifier"
- "updateToConfiguration:"
- "updateToConfigurationWrapper:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AECAssessmentSessionWrapper\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"AECAssessmentSessionWrapper\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"AECAssessmentSessionWrapper\"16@\"AECAssessmentConfigurationWrapper\"24@\"NSError\"32"
- "v40@0:8@16@24@32"

```

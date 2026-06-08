## ClarityUIMessagesSettings

> `/System/Library/PreferenceBundles/ClarityUIMessagesSettings.bundle/ClarityUIMessagesSettings`

```diff

-1817.19.0.0.0
-  __TEXT.__text: 0x9c4
-  __TEXT.__auth_stubs: 0xb0
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x128
-  __TEXT.__objc_methname: 0x442
-  __TEXT.__cstring: 0x79
-  __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methtype: 0x3f
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x60
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0xe0
-  __DATA_CONST.__objc_classlist: 0x8
+1847.0.0.0.0
+  __TEXT.__text: 0x2e0c
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x5bc
+  __TEXT.__const: 0x28
+  __TEXT.__objc_methname: 0x1468
+  __TEXT.__cstring: 0x250
+  __TEXT.__objc_classname: 0x97
+  __TEXT.__objc_methtype: 0x363
+  __TEXT.__oslogstring: 0x33a
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x180
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x118
+  __DATA.__objc_const: 0x620
+  __DATA.__objc_selrefs: 0x5b8
+  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/Contacts.framework/Contacts
+  - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
+  - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
+  - /System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI
+  - /System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices
+  - /System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction
+  - /System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AdCore.framework/AdCore
+  - /System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief
+  - /System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI
+  - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
+  - /System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings
+  - /System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl
+  - /System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices
+  - /System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI
+  - /System/Library/PrivateFrameworks/TouchAccommodations.framework/TouchAccommodations
+  - /System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI
+  - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
+  - /System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices
+  - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
+  - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B9DB8CD-6659-36E1-9716-509682B158AD
-  Functions: 24
-  Symbols:   29
-  CStrings:  68
+  UUID: 170B716F-9848-3222-B8BA-B166A21697A2
+  Functions: 87
+  Symbols:   337
+  CStrings:  319
 
Symbols:
+ -[AXCLFCommunicationLimitController .cxx_destruct]
+ -[AXCLFCommunicationLimitController _addFavorite:]
+ -[AXCLFCommunicationLimitController _favoritesDidChange:]
+ -[AXCLFCommunicationLimitController _favoritesEntryPickerContactForContact:contactStore:]
+ -[AXCLFCommunicationLimitController _favoritesSpecifiers]
+ -[AXCLFCommunicationLimitController _isAllowedFavoritesEntry:]
+ -[AXCLFCommunicationLimitController _singleCommunicationLimitSpecifiersForSpecifier:]
+ -[AXCLFCommunicationLimitController _specifierForFavoritesEntry:]
+ -[AXCLFCommunicationLimitController _updateEditButton]
+ -[AXCLFCommunicationLimitController _updateForOutgoingCommunicationLimit]
+ -[AXCLFCommunicationLimitController actionBundleIdentifiersForFavoritesEntryPicker:]
+ -[AXCLFCommunicationLimitController actionTypesForFavoritesEntryPicker:]
+ -[AXCLFCommunicationLimitController actionTypes]
+ -[AXCLFCommunicationLimitController app]
+ -[AXCLFCommunicationLimitController bundleIdentifiers]
+ -[AXCLFCommunicationLimitController communicationLimitSpecifiers]
+ -[AXCLFCommunicationLimitController contactPicker:didSelectContact:]
+ -[AXCLFCommunicationLimitController contactPickerDidCancel:]
+ -[AXCLFCommunicationLimitController contactPickerPrompt]
+ -[AXCLFCommunicationLimitController favoritesController]
+ -[AXCLFCommunicationLimitController favoritesEntryPicker:didPickEntry:]
+ -[AXCLFCommunicationLimitController favoritesEntryPicker]
+ -[AXCLFCommunicationLimitController favoritesFooterText]
+ -[AXCLFCommunicationLimitController incomingHeaderText]
+ -[AXCLFCommunicationLimitController incomingSpecifiers]
+ -[AXCLFCommunicationLimitController outgoingHeaderText]
+ -[AXCLFCommunicationLimitController outgoingSpecifiers]
+ -[AXCLFCommunicationLimitController privacyAppBundleIdentifier]
+ -[AXCLFCommunicationLimitController setEditing:animated:]
+ -[AXCLFCommunicationLimitController setFavoritesController:]
+ -[AXCLFCommunicationLimitController setFavoritesEntryPicker:]
+ -[AXCLFCommunicationLimitController setIncomingSpecifiers:]
+ -[AXCLFCommunicationLimitController setOutgoingSpecifiers:]
+ -[AXCLFCommunicationLimitController setShouldAvoidReloadForNextFavoritesUpdate:]
+ -[AXCLFCommunicationLimitController settings]
+ -[AXCLFCommunicationLimitController shouldAvoidReloadForNextFavoritesUpdate]
+ -[AXCLFCommunicationLimitController tableView:canEditRowAtIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:canMoveRowAtIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:commitEditingStyle:forRowAtIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:didSelectRowAtIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:editingStyleForRowAtIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:moveRowAtIndexPath:toIndexPath:]
+ -[AXCLFCommunicationLimitController tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:]
+ -[AXCLFCommunicationLimitController tableViewStyle]
+ -[AXCLFCommunicationLimitController viewDidLoad]
+ -[CLCKController actionTypes]
+ -[CLCKController app]
+ -[CLCKController areConversationDetailsEnabled:]
+ -[CLCKController bundleIdentifiers]
+ -[CLCKController contactPickerPrompt]
+ -[CLCKController favoritesFooterText]
+ -[CLCKController incomingHeaderText]
+ -[CLCKController isEmojiKeyboardEnabled:]
+ -[CLCKController isPhotoKeyboardEnabled:]
+ -[CLCKController isSoftwareKeyboardEnabled:]
+ -[CLCKController isTapToSpeakEnabled:]
+ -[CLCKController isVideoRecordingEnabled:]
+ -[CLCKController outgoingHeaderText]
+ -[CLCKController privacyAppBundleIdentifier]
+ -[CLCKController setConversationDetailsEnabled:specifier:]
+ -[CLCKController setEditing:animated:]
+ -[CLCKController setEmojiKeyboardEnabled:specifier:]
+ -[CLCKController setPhotoKeyboardEnabled:specifier:]
+ -[CLCKController setSoftwareKeyboardEnabled:specifier:]
+ -[CLCKController setTapToSpeakEnabled:specifier:]
+ -[CLCKController setVideoRecordingEnabled:specifier:]
+ -[CLCKController settings]
+ -[CLCKController specifiers]
+ -[CLCKController viewDidLoad]
+ -[_SingleCommunicationLimitSpecifiers .cxx_destruct]
+ -[_SingleCommunicationLimitSpecifiers allContactsSpecifier]
+ -[_SingleCommunicationLimitSpecifiers allSpecifiers]
+ -[_SingleCommunicationLimitSpecifiers communicationLimitForSpecifier:]
+ -[_SingleCommunicationLimitSpecifiers everyoneSpecifier]
+ -[_SingleCommunicationLimitSpecifiers groupSpecifier]
+ -[_SingleCommunicationLimitSpecifiers initWithHeaderText:communicationLimit:maximumCommunicationLimit:app:direction:]
+ -[_SingleCommunicationLimitSpecifiers selectedContactsSpecifier]
+ -[_SingleCommunicationLimitSpecifiers setAllContactsSpecifier:]
+ -[_SingleCommunicationLimitSpecifiers setAllSpecifiers:]
+ -[_SingleCommunicationLimitSpecifiers setEveryoneSpecifier:]
+ -[_SingleCommunicationLimitSpecifiers setGroupSpecifier:]
+ -[_SingleCommunicationLimitSpecifiers setSelectedContactsSpecifier:]
+ -[_SingleCommunicationLimitSpecifiers specifierForCommunicationLimit:]
+ -[_SingleCommunicationLimitSpecifiers updateForCommunicationLimit:maximumCommunicationLimit:]
+ OBJC_IVAR_$_AXCLFCommunicationLimitController._favoritesController
+ OBJC_IVAR_$_AXCLFCommunicationLimitController._favoritesEntryPicker
+ OBJC_IVAR_$_AXCLFCommunicationLimitController._incomingSpecifiers
+ OBJC_IVAR_$_AXCLFCommunicationLimitController._outgoingSpecifiers
+ OBJC_IVAR_$_AXCLFCommunicationLimitController._shouldAvoidReloadForNextFavoritesUpdate
+ OBJC_IVAR_$__SingleCommunicationLimitSpecifiers._allContactsSpecifier
+ OBJC_IVAR_$__SingleCommunicationLimitSpecifiers._allSpecifiers
+ OBJC_IVAR_$__SingleCommunicationLimitSpecifiers._everyoneSpecifier
+ OBJC_IVAR_$__SingleCommunicationLimitSpecifiers._groupSpecifier
+ OBJC_IVAR_$__SingleCommunicationLimitSpecifiers._selectedContactsSpecifier
+ _AXFavoritesControllerSpecifierPropertyKey
+ _AXFavoritesEntrySpecifierPropertyKey
+ _AXUILocalizedStringForKey
+ _CLFCommunicationLimitContacts
+ _CLFCommunicationLimitEveryone
+ _CLFCommunicationLimitSelectedContacts
+ _CLFLogCommon
+ _CLFSortedCommunicationLimits
+ _NSRequestConcreteImplementation
+ _OBJC_CLASS_$_AXCLFBasePrivacyLinkController
+ _OBJC_CLASS_$_AXFavoritesEntryCell
+ _OBJC_CLASS_$_CLFLog
+ _OBJC_CLASS_$_CLFPhoneFaceTimeSettings
+ _OBJC_CLASS_$_CNContactPickerViewController
+ _OBJC_CLASS_$_CNContactStore
+ _OBJC_CLASS_$_CNUIFavoritesEntryPicker
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_PSSpecifier
+ _OBJC_CLASS_$_TPFavoritesController
+ _OBJC_CLASS_$__SingleCommunicationLimitSpecifiers
+ _OBJC_METACLASS_$_AXCLFBasePrivacyLinkController
+ _OBJC_METACLASS_$__SingleCommunicationLimitSpecifiers
+ _PSCellClassKey
+ _PSEnabledKey
+ _PSFooterTextGroupKey
+ _PSIsRadioGroupKey
+ _PSRadioGroupCheckedSpecifierKey
+ _TPFavoritesControllerFavoritesEntriesDidChangeNotification
+ __NSConcreteStackBlock
+ __OBJC_$_INSTANCE_METHODS_AXCLFCommunicationLimitController
+ __OBJC_$_INSTANCE_METHODS_CLCKController
+ __OBJC_$_INSTANCE_METHODS__SingleCommunicationLimitSpecifiers
+ __OBJC_$_INSTANCE_VARIABLES_AXCLFCommunicationLimitController
+ __OBJC_$_INSTANCE_VARIABLES__SingleCommunicationLimitSpecifiers
+ __OBJC_$_PROP_LIST_AXCLFCommunicationLimitController
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST__SingleCommunicationLimitSpecifiers
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNUIFavoritesEntryPickerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNContactPickerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNUIFavoritesEntryPickerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNContactPickerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNUIFavoritesEntryPickerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_CNContactPickerDelegate
+ __OBJC_$_PROTOCOL_REFS_CNUIFavoritesEntryPickerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AXCLFCommunicationLimitController
+ __OBJC_CLASS_RO_$_AXCLFCommunicationLimitController
+ __OBJC_CLASS_RO_$_CLCKController
+ __OBJC_CLASS_RO_$__SingleCommunicationLimitSpecifiers
+ __OBJC_LABEL_PROTOCOL_$_CNContactPickerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CNUIFavoritesEntryPickerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_AXCLFCommunicationLimitController
+ __OBJC_METACLASS_RO_$_CLCKController
+ __OBJC_METACLASS_RO_$__SingleCommunicationLimitSpecifiers
+ __OBJC_PROTOCOL_$_CNContactPickerDelegate
+ __OBJC_PROTOCOL_$_CNUIFavoritesEntryPickerDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ ___60-[AXCLFCommunicationLimitController contactPickerDidCancel:]_block_invoke
+ ___71-[AXCLFCommunicationLimitController favoritesEntryPicker:didPickEntry:]_block_invoke
+ ___93-[_SingleCommunicationLimitSpecifiers updateForCommunicationLimit:maximumCommunicationLimit:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ __os_log_fault_impl
+ __os_log_impl
+ _objc_alloc
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$_favoritesEntryPickerContactForContact:contactStore:
+ _objc_msgSend$_favoritesSpecifiers
+ _objc_msgSend$_isAllowedFavoritesEntry:
+ _objc_msgSend$_singleCommunicationLimitSpecifiersForSpecifier:
+ _objc_msgSend$_specifierForFavoritesEntry:
+ _objc_msgSend$_updateEditButton
+ _objc_msgSend$_updateForOutgoingCommunicationLimit
+ _objc_msgSend$actionTypes
+ _objc_msgSend$addEntry:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$allContactsSpecifier
+ _objc_msgSend$allSpecifiers
+ _objc_msgSend$app
+ _objc_msgSend$areKeysAvailable:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$availableKeyDescriptor
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$bundleIdentifiers
+ _objc_msgSend$canAddEntry
+ _objc_msgSend$commonLog
+ _objc_msgSend$communicationLimitForSpecifier:
+ _objc_msgSend$communicationLimitSpecifiers
+ _objc_msgSend$contactPickerPrompt
+ _objc_msgSend$contactStore
+ _objc_msgSend$containsObject:
+ _objc_msgSend$conversationDetailsEnabled
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$descriptorForRequiredKeys
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$editButtonItem
+ _objc_msgSend$emojiKeyboardEnabled
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$everyoneSpecifier
+ _objc_msgSend$favoritesController
+ _objc_msgSend$favoritesEntries
+ _objc_msgSend$favoritesEntryPicker
+ _objc_msgSend$favoritesFooterText
+ _objc_msgSend$fetchIfNeeded
+ _objc_msgSend$getGroupSpecifierForSpecifier:
+ _objc_msgSend$groupSpecifier
+ _objc_msgSend$groupSpecifierWithName:
+ _objc_msgSend$identifier
+ _objc_msgSend$incomingCommunicationLimit
+ _objc_msgSend$incomingHeaderText
+ _objc_msgSend$incomingSpecifiers
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$indexSetWithIndex:
+ _objc_msgSend$initWithContact:
+ _objc_msgSend$initWithContactStore:prefetchCount:
+ _objc_msgSend$initWithHeaderText:communicationLimit:maximumCommunicationLimit:app:direction:
+ _objc_msgSend$invalidateSelectionAnimated:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$loadSpecifiersFromPlistName:target:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$moveEntryAtIndex:toIndex:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$navigationItem
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$outgoingCommunicationLimit
+ _objc_msgSend$outgoingHeaderText
+ _objc_msgSend$outgoingSpecifiers
+ _objc_msgSend$photoKeyboardEnabled
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$preferenceSpecifierNamed:target:set:get:detail:cell:edit:
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$reloadSpecifiers
+ _objc_msgSend$removeEntriesAtIndexes:
+ _objc_msgSend$removeSpecifier:animated:
+ _objc_msgSend$requiresMoreRestrictiveOutgoingCommunicationLimit
+ _objc_msgSend$selectedContactsSpecifier
+ _objc_msgSend$setAllowsEditing:
+ _objc_msgSend$setAutocloses:
+ _objc_msgSend$setButtonAction:
+ _objc_msgSend$setConversationDetailsEnabled:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setEditing:animated:
+ _objc_msgSend$setEmojiKeyboardEnabled:
+ _objc_msgSend$setFavoritesController:
+ _objc_msgSend$setFavoritesEntryPicker:
+ _objc_msgSend$setHidesSearchableSources:
+ _objc_msgSend$setIncomingCommunicationLimit:
+ _objc_msgSend$setIncomingSpecifiers:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setOnlyRealContacts:
+ _objc_msgSend$setOutgoingCommunicationLimit:
+ _objc_msgSend$setOutgoingSpecifiers:
+ _objc_msgSend$setPhotoKeyboardEnabled:
+ _objc_msgSend$setPredicateForEnablingContact:
+ _objc_msgSend$setPrompt:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setRightBarButtonItem:
+ _objc_msgSend$setShouldAvoidReloadForNextFavoritesUpdate:
+ _objc_msgSend$setSoftwareKeyboardEnabled:
+ _objc_msgSend$setTapToSpeakEnabled:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setVideoRecordingEnabled:
+ _objc_msgSend$settings
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$shouldAvoidReloadForNextFavoritesUpdate
+ _objc_msgSend$softwareKeyboardEnabled
+ _objc_msgSend$specifierAtIndexPath:
+ _objc_msgSend$specifierForCommunicationLimit:
+ _objc_msgSend$specifiersWithPrivacyLinkSupport:
+ _objc_msgSend$tapToSpeakEnabled
+ _objc_msgSend$unifiedContactWithIdentifier:keysToFetch:error:
+ _objc_msgSend$updateForCommunicationLimit:maximumCommunicationLimit:
+ _objc_msgSend$videoRecordingEnabled
+ _objc_msgSend$viewController
+ _objc_opt_new
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
+ _os_log_type_enabled
- _objc_retainAutoreleasedReturnValue
- radr://5614542
CStrings:
+ "#16@0:8"
+ ".cxx_destruct"
+ "@\"CNUIFavoritesEntryPicker\""
+ "@\"CNUIUserActionListDataSource\"16@0:8"
+ "@\"NSArray\""
+ "@\"NSArray\"24@0:8@16"
+ "@\"NSString\"16@0:8"
+ "@\"PSSpecifier\""
+ "@\"TPFavoritesController\""
+ "@\"_SingleCommunicationLimitSpecifiers\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32Q40Q48"
+ "ADD_FAVORITE"
+ "AXCLFCommunicationLimitController"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@16@24"
+ "CNContactPickerDelegate"
+ "CNUIFavoritesEntryPickerDelegate"
+ "Could not retrieve a compatible contact using contact (%@) and contact store (%@) due to an error (%@)."
+ "FAVORITES_HEADER_CALLS"
+ "FAVORITES_HEADER_MESSAGES"
+ "MAKE_CALLS_TO_ANYONE"
+ "MAKE_CALLS_TO_CONTACTS"
+ "MAKE_CALLS_TO_FAVORITES"
+ "Missing source or destination favorites entry. Source specifier: %@, destination specifier: %@"
+ "NSObject"
+ "Not adding favorites entry as it exists already: %@"
+ "Not adding favorites entry as it is for an unrelated app: %@"
+ "Not adding favorites entry, as adding was not allowed: %@"
+ "RECEIVE_CALLS_FROM_ANYONE"
+ "RECEIVE_CALLS_FROM_CONTACTS"
+ "RECEIVE_CALLS_FROM_FAVORITES"
+ "RECEIVE_MESSAGES_FROM_ANYONE"
+ "RECEIVE_MESSAGES_FROM_CONTACTS"
+ "RECEIVE_MESSAGES_FROM_FAVORITES"
+ "Radio group checked specifier was unexpectedly out of sync with the selected specifier. Checked: %@, selected: %@"
+ "SEND_MESSAGES_TO_ANYONE"
+ "SEND_MESSAGES_TO_CONTACTS"
+ "SEND_MESSAGES_TO_FAVORITES"
+ "T#,R"
+ "T@\"CLFBaseCommunicationLimitSettings\",R,N"
+ "T@\"CNUIFavoritesEntryPicker\",&,N,V_favoritesEntryPicker"
+ "T@\"NSArray\",&,N,V_allSpecifiers"
+ "T@\"NSArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,C,N"
+ "T@\"PSSpecifier\",&,N,V_allContactsSpecifier"
+ "T@\"PSSpecifier\",&,N,V_everyoneSpecifier"
+ "T@\"PSSpecifier\",&,N,V_groupSpecifier"
+ "T@\"PSSpecifier\",&,N,V_selectedContactsSpecifier"
+ "T@\"TPFavoritesController\",&,N,V_favoritesController"
+ "T@\"_SingleCommunicationLimitSpecifiers\",&,N,V_incomingSpecifiers"
+ "T@\"_SingleCommunicationLimitSpecifiers\",&,N,V_outgoingSpecifiers"
+ "TB,N,V_shouldAvoidReloadForNextFavoritesUpdate"
+ "TQ,R"
+ "TQ,R,N"
+ "Unable to find Favorites entry in list: %@"
+ "Unable to find maximum communication limit \"%@\" in sorted list."
+ "Unable to find source or destination favorites in the list. Source index: %lu, destination index: %lu"
+ "Unexpectedly tried to delete a specifier with no Favorites entry associated: %@"
+ "Unhandled incoming communication limit specifier: %@"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_SingleCommunicationLimitSpecifiers"
+ "_addFavorite:"
+ "_allContactsSpecifier"
+ "_allSpecifiers"
+ "_everyoneSpecifier"
+ "_favoritesController"
+ "_favoritesDidChange:"
+ "_favoritesEntryPicker"
+ "_favoritesEntryPickerContactForContact:contactStore:"
+ "_favoritesSpecifiers"
+ "_groupSpecifier"
+ "_incomingSpecifiers"
+ "_isAllowedFavoritesEntry:"
+ "_outgoingSpecifiers"
+ "_selectedContactsSpecifier"
+ "_shouldAvoidReloadForNextFavoritesUpdate"
+ "_singleCommunicationLimitSpecifiersForSpecifier:"
+ "_specifierForFavoritesEntry:"
+ "_updateEditButton"
+ "_updateForOutgoingCommunicationLimit"
+ "actionBundleIdentifiersForFavoritesEntryPicker:"
+ "actionTypesForFavoritesEntryPicker:"
+ "actionsDataSource"
+ "addEntry:"
+ "addObject:"
+ "addObserver:selector:name:object:"
+ "allContactsSpecifier"
+ "allSpecifiers"
+ "areKeysAvailable:"
+ "array"
+ "arrayWithArray:"
+ "autorelease"
+ "availableKeyDescriptor"
+ "bundleIdentifier"
+ "canAddEntry"
+ "class"
+ "commonLog"
+ "communicationLimitForSpecifier:"
+ "conformsToProtocol:"
+ "contactPicker:didSelectContact:"
+ "contactPicker:didSelectContactProperties:"
+ "contactPicker:didSelectContactProperty:"
+ "contactPicker:didSelectContacts:"
+ "contactPickerDidCancel:"
+ "contactStore"
+ "containsObject:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "debugDescription"
+ "defaultCenter"
+ "description"
+ "descriptorForRequiredKeys"
+ "dismissViewControllerAnimated:completion:"
+ "editButtonItem"
+ "emailAddresses.@count > 0 OR phoneNumbers.@count > 0"
+ "enumerateObjectsUsingBlock:"
+ "everyoneSpecifier"
+ "favoritesController"
+ "favoritesEntries"
+ "favoritesEntryPicker"
+ "favoritesEntryPicker:didPickEntry:"
+ "favoritesEntryPicker:didPickEntry:dismissPicker:"
+ "favoritesEntryPicker:didUpdateWithMenu:"
+ "fetchIfNeeded"
+ "getGroupSpecifierForSpecifier:"
+ "groupSpecifier"
+ "groupSpecifierWithName:"
+ "hash"
+ "identifier"
+ "incomingCommunicationLimit"
+ "incomingSpecifiers"
+ "indexOfObject:"
+ "indexSetWithIndex:"
+ "init"
+ "initWithContact:"
+ "initWithContactStore:prefetchCount:"
+ "initWithHeaderText:communicationLimit:maximumCommunicationLimit:app:direction:"
+ "invalidateSelectionAnimated:"
+ "isEqual:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "moveEntryAtIndex:toIndex:"
+ "name"
+ "numberWithInt:"
+ "outgoingCommunicationLimit"
+ "outgoingSpecifiers"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predicateWithFormat:"
+ "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
+ "presentViewController:animated:completion:"
+ "presentedViewController"
+ "propertyForKey:"
+ "q16@0:8"
+ "q32@0:8@16@24"
+ "release"
+ "reloadSpecifiers"
+ "removeEntriesAtIndexes:"
+ "removeSpecifier:animated:"
+ "requiresMoreRestrictiveOutgoingCommunicationLimit"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "selectedContactsSpecifier"
+ "self"
+ "setAllContactsSpecifier:"
+ "setAllSpecifiers:"
+ "setAllowsEditing:"
+ "setAutocloses:"
+ "setButtonAction:"
+ "setDelegate:"
+ "setEveryoneSpecifier:"
+ "setFavoritesController:"
+ "setFavoritesEntryPicker:"
+ "setGroupSpecifier:"
+ "setHidesSearchableSources:"
+ "setIncomingCommunicationLimit:"
+ "setIncomingSpecifiers:"
+ "setMode:"
+ "setOnlyRealContacts:"
+ "setOutgoingCommunicationLimit:"
+ "setOutgoingSpecifiers:"
+ "setPredicateForEnablingContact:"
+ "setPrompt:"
+ "setProperty:forKey:"
+ "setRightBarButtonItem:"
+ "setSelectedContactsSpecifier:"
+ "setShouldAvoidReloadForNextFavoritesUpdate:"
+ "shouldAvoidReloadForNextFavoritesUpdate"
+ "specifierAtIndexPath:"
+ "specifierForCommunicationLimit:"
+ "specifiersWithPrivacyLinkSupport:"
+ "superclass"
+ "tableView:canEditRowAtIndexPath:"
+ "tableView:canMoveRowAtIndexPath:"
+ "tableView:commitEditingStyle:forRowAtIndexPath:"
+ "tableView:didSelectRowAtIndexPath:"
+ "tableView:editingStyleForRowAtIndexPath:"
+ "tableView:moveRowAtIndexPath:toIndexPath:"
+ "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
+ "tableViewStyle"
+ "unifiedContactWithIdentifier:keysToFetch:error:"
+ "updateForCommunicationLimit:maximumCommunicationLimit:"
+ "v20@0:8B16"
+ "v24@0:8@\"CNContactPickerViewController\"16"
+ "v24@0:8@16"
+ "v32@0:8@\"CNContactPickerViewController\"16@\"CNContact\"24"
+ "v32@0:8@\"CNContactPickerViewController\"16@\"CNContactProperty\"24"
+ "v32@0:8@\"CNContactPickerViewController\"16@\"NSArray\"24"
+ "v32@0:8@16@\"CNFavoritesEntry\"24"
+ "v32@0:8@16@\"NSArray\"24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v36@0:8@16@\"CNFavoritesEntry\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16q24@32"
+ "v8@?0"
+ "viewController"
+ "zone"

```

## AddressBookUI

> `/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI`

```diff

-2402.500.21.0.0
-  __TEXT.__text: 0x38e4
-  __TEXT.__auth_stubs: 0x1e0
+2407.100.2.0.0
+  __TEXT.__text: 0x3a54
   __TEXT.__objc_methlist: 0x854
   __TEXT.__cstring: 0x89e
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0xf6
-  __TEXT.__objc_methname: 0x1dbc
-  __TEXT.__objc_methtype: 0x4ae
-  __TEXT.__objc_stubs: 0x15a0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x7e0
   __AUTH_CONST.__objc_const: 0xc28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x208

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E09BF1D-5583-381C-A114-E3721A04DDAC
+  UUID: 4B7F99D2-1AEF-3DF9-A4DC-4D8EF3AE33D9
   Functions: 172
   Symbols:   726
-  CStrings:  501
+  CStrings:  132
 
Functions:
~ -[ABNewPersonViewController dealloc] : 152 -> 164
~ -[ABNewPersonViewController newPersonViewDelegate] : 16 -> 20
~ -[ABNewPersonViewController setNewPersonViewDelegate:] : 16 -> 20
~ -[ABNewPersonViewController addressBook] : 148 -> 152
~ -[ABNewPersonViewController setAddressBook:] : 92 -> 96
~ -[ABNewPersonViewController displayedPerson] : 16 -> 20
~ -[ABNewPersonViewController setDisplayedPerson:] : 84 -> 88
~ -[ABNewPersonViewController preferredContentSize] : 16 -> 20
~ -[ABNewPersonViewController contactViewController:didCompleteWithContact:] : 224 -> 228
~ -[ABNewPersonViewController loadContactViewController] : 992 -> 996
~ -[ABNewPersonViewController parentGroup] : 16 -> 20
~ -[ABNewPersonViewController setParentGroup:] : 16 -> 20
~ -[ABNewPersonViewController cnContactViewController] : 16 -> 20
~ -[ABNewPersonViewController parentSource] : 16 -> 20
~ -[ABNewPersonViewController setParentSource:] : 16 -> 20
~ -[ABNewPersonViewController mergeContact] : 16 -> 20
~ -[ABPeoplePickerNavigationController initWithAddressBook:] : 172 -> 176
~ -[ABPeoplePickerNavigationController dealloc] : 184 -> 212
~ -[ABPeoplePickerNavigationController setupViewControllers] : 356 -> 364
~ -[ABPeoplePickerNavigationController _isDelayingPresentation] : 156 -> 160
~ -[ABPeoplePickerNavigationController addressBook] : 16 -> 20
~ -[ABPeoplePickerNavigationController setAddressBook:] : 112 -> 116
~ -[ABPeoplePickerNavigationController contactPicker:didSelectContact:] : 192 -> 196
~ -[ABPeoplePickerNavigationController contactPicker:didSelectContactProperty:] : 272 -> 276
~ -[ABPeoplePickerNavigationController contactPickerDidCancel:] : 124 -> 128
~ -[ABPeoplePickerNavigationController peoplePickerDelegate] : 16 -> 20
~ -[ABPeoplePickerNavigationController setPeoplePickerDelegate:] : 16 -> 20
~ -[ABPeoplePickerNavigationController displayedProperties] : 16 -> 20
~ -[ABPeoplePickerNavigationController predicateForEnablingPerson] : 16 -> 20
~ -[ABPeoplePickerNavigationController predicateForSelectionOfPerson] : 16 -> 20
~ -[ABPeoplePickerNavigationController predicateForSelectionOfProperty] : 16 -> 20
~ -[ABPersonViewController dealloc] : 152 -> 168
~ -[ABPersonViewController addressBook] : 112 -> 116
~ -[ABPersonViewController setAddressBook:] : 92 -> 96
~ -[ABPersonViewController displayedPerson] : 16 -> 20
~ -[ABPersonViewController setDisplayedPerson:] : 152 -> 156
~ -[ABPersonViewController preferredContentSize] : 60 -> 64
~ -[ABPersonViewController reloadContactViewController] : 900 -> 904
~ -[ABPersonViewController personViewDelegate] : 16 -> 20
~ -[ABPersonViewController setPersonViewDelegate:] : 16 -> 20
~ -[ABPersonViewController displayedProperties] : 16 -> 20
~ -[ABPersonViewController allowsEditing] : 16 -> 20
~ -[ABPersonViewController setAllowsEditing:] : 16 -> 20
~ -[ABPersonViewController allowsActions] : 16 -> 20
~ -[ABPersonViewController setAllowsActions:] : 16 -> 20
~ -[ABPersonViewController shouldShowLinkedPeople] : 16 -> 20
~ -[ABPersonViewController setShouldShowLinkedPeople:] : 16 -> 20
~ -[ABPersonViewController style] : 16 -> 20
~ -[ABPersonViewController setStyle:] : 16 -> 20
~ -[ABPersonViewController highlightedProperty] : 16 -> 20
~ -[ABPersonViewController setHighlightedProperty:] : 16 -> 20
~ -[ABPersonViewController highlightedMultiValueIdentifier] : 16 -> 20
~ -[ABPersonViewController setHighlightedMultiValueIdentifier:] : 16 -> 20
~ -[ABPersonViewController highlightedImportant] : 16 -> 20
~ -[ABPersonViewController setHighlightedImportant:] : 16 -> 20
~ -[ABPersonViewController cnContactViewController] : 16 -> 20
~ -[ABUnknownPersonViewController initWithNibName:bundle:] : 128 -> 136
~ -[ABUnknownPersonViewController dealloc] : 168 -> 188
~ -[ABUnknownPersonViewController preferredContentSize] : 60 -> 64
~ -[ABUnknownPersonViewController addressBook] : 112 -> 116
~ -[ABUnknownPersonViewController setAddressBook:] : 92 -> 96
~ -[ABUnknownPersonViewController displayedPerson] : 16 -> 20
~ -[ABUnknownPersonViewController setDisplayedPerson:] : 84 -> 88
~ -[ABUnknownPersonViewController cnContactViewController] : 84 -> 88
~ -[ABUnknownPersonViewController loadContactViewController] : 536 -> 548
~ -[ABUnknownPersonViewController unknownPersonViewDelegate] : 16 -> 20
~ -[ABUnknownPersonViewController setUnknownPersonViewDelegate:] : 16 -> 20
~ -[ABUnknownPersonViewController alternateName] : 16 -> 20
~ -[ABUnknownPersonViewController message] : 16 -> 20
~ -[ABUnknownPersonViewController allowsActions] : 16 -> 20
~ -[ABUnknownPersonViewController setAllowsActions:] : 16 -> 20
~ -[ABUnknownPersonViewController allowsAddingToAddressBook] : 16 -> 20
~ -[ABUnknownPersonViewController setAllowsAddingToAddressBook:] : 16 -> 20
CStrings:
- "#16@0:8"
- "@"
- "@\"<ABNewPersonViewControllerDelegate>\""
- "@\"<ABPersonViewControllerDelegate>\""
- "@\"<ABUnknownPersonViewControllerDelegate>\""
- "@\"CNContact\""
- "@\"CNContactPickerViewController\""
- "@\"CNContactViewController\""
- "@\"NSArray\""
- "@\"NSPredicate\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"UIViewController\"32@0:8@\"NSArray\"16@\"NSCoder\"24"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^v16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16@24i32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^v32"
- "@44@0:8@16@24^v32i40"
- "ABNewPersonViewController"
- "ABPeoplePickerNavigationController"
- "ABPersonViewController"
- "ABUnknownPersonViewController"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"CNContactViewController\"16@\"CNContactProperty\"24"
- "B32@0:8@16@24"
- "B48@0:8@16@24@32@40"
- "CNContactPickerDelegate"
- "CNContactViewControllerDelegate"
- "CNContactViewControllerPrivateDelegate"
- "ISOCountryCode"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<ABNewPersonViewControllerDelegate>\",N"
- "T@\"<ABPeoplePickerNavigationControllerDelegate>\",N,V_peoplePickerDelegate"
- "T@\"<ABPersonViewControllerDelegate>\",N,V_personViewDelegate"
- "T@\"<ABUnknownPersonViewControllerDelegate>\",N,V_unknownPersonViewDelegate"
- "T@\"CNContact\",&,N,V_mergeContact"
- "T@\"CNContactStore\",R,N"
- "T@\"CNContactViewController\",&,N,V_cnContactViewController"
- "T@\"NSArray\",C,N,V_displayedProperties"
- "T@\"NSPredicate\",C,N,V_predicateForEnablingPerson"
- "T@\"NSPredicate\",C,N,V_predicateForSelectionOfPerson"
- "T@\"NSPredicate\",C,N,V_predicateForSelectionOfProperty"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_alternateName"
- "T@\"NSString\",C,N,V_message"
- "T@\"NSString\",R,C"
- "TB,N"
- "TB,N,V_allowsActions"
- "TB,N,V_allowsAddingToAddressBook"
- "TB,N,V_allowsEditing"
- "TB,N,V_highlightedImportant"
- "TB,N,V_shouldShowLinkedPeople"
- "TQ,R"
- "T^v,N"
- "T^v,N,V_addressBook"
- "T^v,N,V_displayedPerson"
- "T^v,N,V_parentGroup"
- "T^v,N,V_parentSource"
- "Ti,N,V_highlightedMultiValueIdentifier"
- "Ti,N,V_highlightedProperty"
- "Ti,N,V_style"
- "UIViewControllerRestoration"
- "Vv16@0:8"
- "^v"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "_addressBook"
- "_allowsActions"
- "_allowsAddingToAddressBook"
- "_allowsAutorotation"
- "_allowsEditing"
- "_alternateName"
- "_cnContactViewController"
- "_cn_filter:"
- "_cn_firstObjectPassingTest:"
- "_cn_map:"
- "_contactPicker"
- "_displayedPerson"
- "_displayedProperties"
- "_endDelayingPresentation"
- "_highlightedImportant"
- "_highlightedMultiValueIdentifier"
- "_highlightedProperty"
- "_ignoreViewWillBePresented"
- "_isDelayingPresentation"
- "_mergeContact"
- "_message"
- "_newPersonViewDelegate"
- "_parentGroup"
- "_parentSource"
- "_peoplePickerDelegate"
- "_personViewDelegate"
- "_predicateForEnablingPerson"
- "_predicateForSelectionOfPerson"
- "_predicateForSelectionOfProperty"
- "_screen"
- "_setBackgroundHidden:"
- "_setClipUnderlapWhileTransitioning:"
- "_setViewController:animated:"
- "_shouldPreventCancelButtonsFromShowing"
- "_shouldShowLinkedPeople"
- "_style"
- "_unknownPersonViewDelegate"
- "_viewWillBePresented"
- "ab_isDirectlyInPopover"
- "addChildViewController:"
- "addProperties:excludingProperties:fromContact:"
- "addSubview:"
- "addressBook"
- "allCardProperties"
- "allowsActions"
- "allowsAddingToAddressBook"
- "allowsEditing"
- "alternateName"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "blurRadius"
- "bounds"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "class"
- "cnContactViewController"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "contact"
- "contactFromPublicABPerson:keysToFetch:"
- "contactFromPublicABPerson:keysToFetch:mutable:"
- "contactPicker:didSelectContact:"
- "contactPicker:didSelectContactProperties:"
- "contactPicker:didSelectContactProperty:"
- "contactPicker:didSelectContacts:"
- "contactPickerDidCancel:"
- "contactPickerPresentedViewController:"
- "contactPropertyKeyFromPublicABPropertyID:"
- "contactStore"
- "contactStoreForPublicAddressBook:"
- "contactViewController:didChangeToEditMode:"
- "contactViewController:didCompleteWithContact:"
- "contactViewController:didDeleteContact:"
- "contactViewController:didExecuteBlockAndReportContactAction:"
- "contactViewController:shouldPerformDefaultActionForContact:property:labeledValue:"
- "contactViewController:shouldPerformDefaultActionForContactProperty:"
- "contactViewControllerDidExecuteAddToDowntimeWhitelistAction:"
- "contactViewControllerDidExecuteClearRecentsDataAction:"
- "contactViewControllerDidExecuteDeleteFromDowntimeWhitelistAction:"
- "contactViewControllerForUnknownContactDidBeginAddingToContacts:"
- "contactViewControllerForUnknownContactDidEndAddingToContacts:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "country"
- "countryCode"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeRestorableStateWithCoder:"
- "defaultCenter"
- "description"
- "descriptorForRequiredKeys"
- "didMoveToParentViewController:"
- "displayedPerson"
- "displayedProperties"
- "displayedPropertyKeys"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeRestorableStateWithCoder:"
- "firstObject"
- "groupsMatchingPredicate:error:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasPrefix:"
- "hash"
- "highlightPropertyWithKey:identifier:important:"
- "highlightedImportant"
- "highlightedMultiValueIdentifier"
- "highlightedProperty"
- "i"
- "i16@0:8"
- "iOSLegacyIdentifier"
- "identifier"
- "infoDictionary"
- "init"
- "initWithAddressBook:"
- "initWithFrame:"
- "initWithNibName:bundle:"
- "initWithNibName:bundle:addressBook:"
- "initWithNibName:bundle:addressBook:style:"
- "initWithNibName:bundle:style:"
- "initWithStyle:"
- "intValue"
- "integerValue"
- "isAccessGranted"
- "isBeingPresented"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMovingToParentViewController"
- "isProxy"
- "isViewLoaded"
- "isoCountryCode"
- "key"
- "labeledValue"
- "loadContactViewController"
- "loadView"
- "localizedStringForKey:value:table:"
- "logPresentation"
- "mainBundle"
- "mainScreen"
- "mergeContact"
- "message"
- "mutableCopy"
- "name"
- "nameProperties"
- "navigationItem"
- "newPersonViewController:didCompleteWithNewPerson:"
- "newPersonViewDelegate"
- "newlineCharacterSet"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "overwritePublicABPerson:"
- "parentGroup"
- "parentSource"
- "peoplePickerDelegate"
- "peoplePickerNavigationController:didSelectPerson:"
- "peoplePickerNavigationController:didSelectPerson:property:identifier:"
- "peoplePickerNavigationControllerDidCancel:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personViewController:shouldPerformDefaultActionForPerson:property:identifier:"
- "personViewDelegate"
- "postalAddressWithAddressBookDictionaryRepresentation:"
- "predicateForEnablingPerson"
- "predicateForSelectionOfPerson"
- "predicateForSelectionOfProperty"
- "predicateForiOSLegacyIdentifier:"
- "preferredContentSize"
- "publicABPersonFromContact:publicAddressBook:"
- "publicABPropertyIDFromContactPropertyKey:"
- "publicMultiValueIdentifierFromLabeledValue:"
- "release"
- "reloadContactViewController"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "save:"
- "savesNewContactOnSuspend"
- "scale"
- "self"
- "setAddressBook:"
- "setAllowsActions:"
- "setAllowsAddingToAddressBook:"
- "setAllowsCancel:"
- "setAllowsEditing:"
- "setAlternateName:"
- "setAutoresizingMask:"
- "setCnContactViewController:"
- "setContactStore:"
- "setCountry:"
- "setDelegate:"
- "setDisplayedPerson:"
- "setDisplayedProperties:"
- "setDisplayedPropertyKeys:"
- "setEditing:animated:"
- "setFrame:"
- "setHighlightedImportant:"
- "setHighlightedItemForProperty:withIdentifier:"
- "setHighlightedItemForProperty:withIdentifier:important:"
- "setHighlightedItemForProperty:withIdentifier:person:"
- "setHighlightedItemForProperty:withIdentifier:person:important:"
- "setHighlightedMultiValueIdentifier:"
- "setHighlightedProperty:"
- "setMergeContact:"
- "setMessage:"
- "setNavigationBarHidden:animated:"
- "setNewPersonViewDelegate:"
- "setParentGroup:"
- "setParentSource:"
- "setPeoplePickerDelegate:"
- "setPersonViewDelegate:"
- "setPredicateForEnablingContact:"
- "setPredicateForEnablingPerson:"
- "setPredicateForSelectionOfContact:"
- "setPredicateForSelectionOfPerson:"
- "setPredicateForSelectionOfProperty:"
- "setPreferredContentSize:"
- "setRestorationClass:"
- "setRestorationIdentifier:"
- "setSavesNewContactOnSuspend:"
- "setShouldShowLinkedContacts:"
- "setShouldShowLinkedPeople:"
- "setShowsCancelButton:"
- "setStyle:"
- "setTitle:"
- "setUnknownPersonViewDelegate:"
- "setView:"
- "setViewControllers:animated:"
- "settingsForPrivateStyle:"
- "setupViewControllers"
- "sharedCollector"
- "sharedDefaults"
- "sharedInstance"
- "shouldShowLinkedPeople"
- "showsCancelButton"
- "siriUILocalizedStringForKey:table:"
- "stringByTrimmingCharactersInSet:"
- "stringFromPostalAddress:style:"
- "style"
- "superclass"
- "supportedCountries"
- "unknownPersonViewController:didResolveToPerson:"
- "unknownPersonViewController:shouldPerformDefaultActionForPerson:property:identifier:"
- "unknownPersonViewDelegate"
- "updateNewPublicABPerson:inAddressBook:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CNContactPickerViewController\"16"
- "v24@0:8@\"CNContactViewController\"16"
- "v24@0:8@16"
- "v24@0:8B16B20"
- "v24@0:8^v16"
- "v24@0:8i16i20"
- "v28@0:8@\"CNContactViewController\"16B24"
- "v28@0:8@16B24"
- "v28@0:8i16i20B24"
- "v32@0:8@\"CNContactPickerViewController\"16@\"CNContact\"24"
- "v32@0:8@\"CNContactPickerViewController\"16@\"CNContactProperty\"24"
- "v32@0:8@\"CNContactPickerViewController\"16@\"NSArray\"24"
- "v32@0:8@\"CNContactViewController\"16@\"CNContact\"24"
- "v32@0:8@16@24"
- "v32@0:8i16i20^v24"
- "v36@0:8i16i20^v24B32"
- "valueForKey:"
- "view"
- "viewControllerForContact:"
- "viewControllerForNewContact:"
- "viewControllerForUnknownContact:"
- "viewControllerWithRestorationIdentifierPath:coder:"
- "viewControllers"
- "viewDidAppear:"
- "viewWillAppear:"
- "whitespaceAndNewlineCharacterSet"
- "willMoveToParentViewController:"
- "zone"
- "{CGSize=dd}16@0:8"

```

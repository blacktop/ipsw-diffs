## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-423.0.58.0.0
-  __TEXT.__text: 0x3ccfc
+425.0.98.0.0
+  __TEXT.__text: 0x3b420
   __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x39bc
+  __TEXT.__objc_methlist: 0x47e8
   __TEXT.__const: 0x116
-  __TEXT.__cstring: 0x3c21
-  __TEXT.__oslogstring: 0x1d65
+  __TEXT.__cstring: 0x3b11
   __TEXT.__gcc_except_tab: 0x4d8
+  __TEXT.__oslogstring: 0x1d29
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x68
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_capture: 0x4c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xf30
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0xee8
   __TEXT.__eh_frame: 0x168
-  __TEXT.__objc_classname: 0x8aa
-  __TEXT.__objc_methname: 0xc9d7
-  __TEXT.__objc_methtype: 0x26f5
-  __TEXT.__objc_stubs: 0x9100
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0xe20
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__objc_classname: 0x875
+  __TEXT.__objc_methname: 0xc569
+  __TEXT.__objc_methtype: 0x26dc
+  __TEXT.__objc_stubs: 0x8ce0
+  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__const: 0xdf0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29e0
+  __DATA_CONST.__objc_selrefs: 0x2f48
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x4400
-  __AUTH_CONST.__objc_const: 0x11ef0
+  __AUTH_CONST.__cfstring: 0x42a0
+  __AUTH_CONST.__objc_const: 0xf170
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x1058
+  __AUTH.__objc_data: 0x1008
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x3e0
-  __DATA.__data: 0xba0
-  __DATA.__bss: 0x260
+  __DATA.__objc_ivar: 0x3c8
+  __DATA.__data: 0xb40
+  __DATA.__bss: 0x258
   __DATA.__common: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1619
-  Symbols:   2013
-  CStrings:  3095
+  Functions: 1586
+  Symbols:   1968
+  CStrings:  3027
 
Symbols:
- _CNContactEmailAddressesKey
- _CNContactIdentifierKey
- _CNContactPhoneNumbersKey
- _OBJC_CLASS_$_CNContactPickerViewController
- _OBJC_CLASS_$_CNContactProperty
- _OBJC_CLASS_$_CNContactStore
- _OBJC_CLASS_$_CNUIContactPropertyRanker
- _OBJC_CLASS_$_DSShareLocationController
- _OBJC_CLASS_$_FMFHandle
- _OBJC_CLASS_$_FMFSession
- _OBJC_CLASS_$_NSCalendar
- _OBJC_CLASS_$_NSDate
- _OBJC_METACLASS_$_DSShareLocationController
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "%@\n\n%@"
+ "ERROR_APP_UNLAUNCHED"
+ "ERROR_DISABLED_IN_ICLOUD"
+ "ERROR_UNINSTALLED_IN_APPSTORE"
+ "allKeys"
+ "clearRemoteWidgetBlocklist"
+ "ds_presentableErrorsByLocalizedAppName"
+ "errorMessaging"
+ "findMyAccessoryManager:didFetchAccessoryInformationForDevice:ownershipType:communicationProtocol:accessoryTypeName:error:"
+ "findMyAccessoryManager:didFetchFindingCapabilitiesOnDevice:withFindingCapabilities:error:"
+ "localizedResourceNamesForPerson:"
+ "nullifyReplicatorAllowlist"
+ "textView:insertInputSuggestion:"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "v48@0:8@\"CLFindMyAccessoryManager\"16@\"NSUUID\"24@\"CLFindMyAccessoryFindingCapabilities\"32@\"NSError\"40"
+ "v64@0:8@\"CLFindMyAccessoryManager\"16@\"NSUUID\"24Q32Q40@\"NSString\"48@\"NSError\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "\x13\x11"
- "%@ %@"
- "%K != %@"
- "(emailAddresses.@count > 0) OR (phoneNumbers.@count > 0)"
- "(property == 'emailAddresses') OR (property == 'phoneNumbers')"
- "@\"CNContact\""
- "@\"CNContactPickerViewController\""
- "@\"FMFSession\""
- "CNContactPickerDelegate"
- "DSShareLocationController"
- "Error getting callerID."
- "Error offering location. Error - %@"
- "LOCATION_SHARING_FAILED"
- "LOCATION_SHARING_FAILED_TITLE"
- "SHARE_CONTACT"
- "SHARE_EOD"
- "SHARE_INDEFINITELY"
- "SHARE_LOCATION"
- "SHARE_LOCATION_CONTACT_FOOTER"
- "SHARE_LOCATION_DETAIL"
- "SHARE_LOCATION_TYPE_FOOTER"
- "SHARE_ONE_HOUR"
- "T@\"CNContact\",&,N,V_selectedContact"
- "T@\"CNContactPickerViewController\",&,N,V_contactsViewController"
- "T@\"FMFSession\",&,N,V_fmfSession"
- "T@\"NSArray\",&,N,V_locationSharingTypeNames"
- "Tq,N,V_selectedLocationSharingType"
- "_contactsViewController"
- "_fmfSession"
- "_locationSharingTypeNames"
- "_selectedContact"
- "_selectedLocationSharingType"
- "andPredicateWithSubpredicates:"
- "bestDefaultContactProperty"
- "bestPropertyComparator"
- "contactPicker:didSelectContact:"
- "contactPicker:didSelectContactProperties:"
- "contactPicker:didSelectContactProperty:"
- "contactPicker:didSelectContacts:"
- "contactPickerDidCancel:"
- "contactPropertyWithContact:propertyKey:identifier:"
- "contactsViewController"
- "currentCalendar"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "ds_meContactIdentifier"
- "emailAddresses"
- "endDateFromNowForOfferTimespan:"
- "findmy"
- "fmfHandleFromContactProperty:"
- "fmfHandlesFromContact:"
- "fmfSession"
- "handleWithId:"
- "iCloudAccountNameWithCompletion:"
- "initWithDelegate:"
- "key"
- "locationSharingTypeNames"
- "manageBoldButton"
- "nextDateAfterDate:matchingUnit:value:options:"
- "phoneNumbers"
- "pickContact"
- "presentSharingFailedAlert"
- "selectedContact"
- "selectedLocationSharingType"
- "sendFriendshipOfferToHandles:groupId:callerId:endDate:completion:"
- "setContactsViewController:"
- "setDisplayedPropertyKeys:"
- "setEnabled:"
- "setFmfSession:"
- "setLocationSharingTypeNames:"
- "setMultipleTouchEnabled:"
- "setPredicateForEnablingContact:"
- "setPredicateForSelectionOfContact:"
- "setPredicateForSelectionOfProperty:"
- "setSelectedContact:"
- "setSelectedLocationSharingType:"
- "shareLocation"
- "sortUsingComparator:"
- "unformattedInternationalStringValue"
- "v24@0:8@\"CNContactPickerViewController\"16"
- "v32@0:8@\"CNContactPickerViewController\"16@\"CNContact\"24"
- "v32@0:8@\"CNContactPickerViewController\"16@\"CNContactProperty\"24"
- "v32@0:8@\"CNContactPickerViewController\"16@\"NSArray\"24"
- "value"

```

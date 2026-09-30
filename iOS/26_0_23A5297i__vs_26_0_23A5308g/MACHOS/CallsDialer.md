## CallsDialer

> `/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/Frameworks/CallsDialer.framework/CallsDialer`

```diff

-3021.100.15.1.5
-  __TEXT.__text: 0x29e58
+3024.100.7.0.0
+  __TEXT.__text: 0x2a5d0
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x2b54
+  __TEXT.__objc_methlist: 0x2bc4
   __TEXT.__const: 0x984
-  __TEXT.__cstring: 0x13eb
+  __TEXT.__cstring: 0x13fb
   __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__oslogstring: 0x11fa
+  __TEXT.__oslogstring: 0x128a
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__swift5_typeref: 0x1ec
   __TEXT.__swift5_capture: 0x50

   __TEXT.__swift5_fieldmd: 0x16c
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0xae8
+  __TEXT.__unwind_info: 0xaf8
   __TEXT.__objc_classname: 0x43c
-  __TEXT.__objc_methname: 0x9744
-  __TEXT.__objc_methtype: 0x159d
-  __TEXT.__objc_stubs: 0x7a20
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0x6e8
+  __TEXT.__objc_methname: 0x995b
+  __TEXT.__objc_methtype: 0x15d3
+  __TEXT.__objc_stubs: 0x7c00
+  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27c8
+  __DATA_CONST.__objc_selrefs: 0x2850
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__const: 0x4b8
   __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__objc_const: 0x39f0
+  __AUTH_CONST.__objc_const: 0x3a20
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x400
-  __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x270
-  __DATA.__data: 0x880
+  __AUTH.__objc_data: 0x2b8
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x274
+  __DATA.__data: 0x860
   __DATA.__bss: 0x6d0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x5b0
-  __DATA_DIRTY.__data: 0x68
+  __DATA_DIRTY.__objc_data: 0x6f8
+  __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
+  - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E019A32C-CA7F-3589-A378-FB5065E7FF2A
-  Functions: 1123
-  Symbols:   2903
-  CStrings:  2332
+  UUID: 4038E264-F284-35E9-9281-CA303907FAAA
+  Functions: 1132
+  Symbols:   2931
+  CStrings:  2355
 
Symbols:
+ -[CNContactStore(PhoneKit) __contactsForHandles:keyDescriptors:alwaysUnifyLabeledValues:]
+ -[DialerController deviceHasMultipleSIM]
+ -[DialerController enableDualSimMenu]
+ -[PHHandsetDialerView constraintAddContactButtonForIPad]
+ -[PHHandsetDialerView constraintAddContactButtonForNonIPad]
+ -[PHHandsetDialerView constraintDualSimPicker]
+ -[PHHandsetDialerView enableDualSimMenu]
+ -[PHHandsetDialerView initWithFrame:appType:enableSmartDialer:enableSmartDialerExpandedSearch:enableDualSimMenu:]
+ -[PHHandsetDialerView setEnableDualSimMenu:]
+ OBJC_IVAR_$_PHHandsetDialerView._enableDualSimMenu
+ _OBJC_CLASS_$_FTDeviceSupport
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_CallsDialer
+ _objc_msgSend$__contactsForHandles:keyDescriptors:alwaysUnifyLabeledValues:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$constraintAddContactButtonForIPad
+ _objc_msgSend$constraintAddContactButtonForNonIPad
+ _objc_msgSend$constraintDualSimPicker
+ _objc_msgSend$deviceHasMultipleSIM
+ _objc_msgSend$deviceType
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$emailAddresses
+ _objc_msgSend$enableDualSimMenu
+ _objc_msgSend$initWithFrame:appType:enableSmartDialer:enableSmartDialerExpandedSearch:enableDualSimMenu:
+ _objc_msgSend$isGreenTea
+ _objc_msgSend$providerManager
+ _objc_msgSend$setEnableDualSimMenu:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$unifiedContactsMatchingPredicate:keysToFetch:error:
- _objc_msgSend$initWithFrame:appType:enableSmartDialer:enableSmartDialerExpandedSearch:
- _objc_msgSend$yOffsetForSmartDialerLCDView
CStrings:
+ "@68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48B56B60B64"
+ "Skipping phone number lookup on GreenTea iPad, returning nil for prefix hint."
+ "TB,N,V_enableDualSimMenu"
+ "TOTAL contacts fetched: regular = %lu accepted = %lu, combined = %lu"
+ "__contactsForHandles:keyDescriptors:alwaysUnifyLabeledValues:"
+ "_enableDualSimMenu"
+ "addEntriesFromDictionary:"
+ "apple.step.by.step.help"
+ "constraintAddContactButtonForIPad"
+ "constraintAddContactButtonForNonIPad"
+ "constraintDualSimPicker"
+ "deviceHasMultipleSIM"
+ "deviceType"
+ "dictionary"
+ "dictionaryWithDictionary:"
+ "emailAddresses"
+ "enableDualSimMenu"
+ "initWithFrame:appType:enableSmartDialer:enableSmartDialerExpandedSearch:enableDualSimMenu:"
+ "isGreenTea"
+ "providerManager"
+ "setEnableDualSimMenu:"
+ "setWithArray:"
+ "unifiedContactsMatchingPredicate:keysToFetch:error:"
- "iphone.badge.play"

```

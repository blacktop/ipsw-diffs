## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-593.0.1.0.0
-  __TEXT.__text: 0x2b334
+595.0.2.0.0
+  __TEXT.__text: 0x2aa84
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x1dec
-  __TEXT.__cstring: 0x13c7
+  __TEXT.__objc_methlist: 0x1dcc
+  __TEXT.__cstring: 0x1366
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0xd40
   __TEXT.__oslogstring: 0x2485
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x2a3
-  __TEXT.__objc_methname: 0x4aaa
+  __TEXT.__objc_methname: 0x4ae7
   __TEXT.__objc_methtype: 0xa50
-  __TEXT.__objc_stubs: 0x4140
+  __TEXT.__objc_stubs: 0x4120
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__const: 0xc80
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1400
+  __DATA_CONST.__objc_selrefs: 0x13f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__cfstring: 0x14a0
   __AUTH_CONST.__objc_const: 0x42c0
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x4e8
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C406D90-F87E-34B0-9600-CC41F22191A9
-  Functions: 805
-  Symbols:   3077
-  CStrings:  1533
+  UUID: E28A7E87-FB19-37FE-9C24-D72E0DDC5834
+  Functions: 803
+  Symbols:   3073
+  CStrings:  1524
 
Symbols:
+ +[DSUtilities phoneNumberCharacterSet]
+ +[DSUtilities phoneNumberCharacterSet].cold.1
+ -[DSXPCSharingPerson isEqual:].cold.1
+ -[NSString(DigitalSeparation) ds_isPhoneNumber]
+ -[NSString(DigitalSeparation) ds_prettyPrintedPotentialPhoneNumber]
+ GCC_except_table18
+ GCC_except_table26
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.77
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.77.cold.1
+ ___38+[DSUtilities phoneNumberCharacterSet]_block_invoke
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.321
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.321.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.323
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.326
+ ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.333
+ ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.400
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.336
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.336.cold.1
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.337
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.8
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.8.cold.1
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.9
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.17
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.328
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.328.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.329
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.330
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.16
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.16.cold.1
+ ___block_literal_global.325
+ ___block_literal_global.339
+ ___block_literal_global.343
+ ___block_literal_global.360
+ ___block_literal_global.369
+ ___block_literal_global.76
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$controlCharacterSet
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$ds_isPhoneNumber
+ _objc_msgSend$ds_prettyPrintedPotentialPhoneNumber
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$phoneNumberCharacterSet
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _phoneNumberCharacterSet.onceToken
+ _phoneNumberCharacterSet.phoneNumCharacterSet
- -[CNContact(DigitalSeparation) ds_emailAddresses]
- -[CNContact(DigitalSeparation) ds_isLikeContact:]
- -[CNContact(DigitalSeparation) ds_name]
- -[CNContact(DigitalSeparation) ds_phoneNumbers]
- -[DSXPCSharingPerson isLikeContact:]
- -[DSXPCSharingPerson isLikeContact:].cold.1
- -[NSString(DigitalSeparation) isPhoneNumber]
- GCC_except_table27
- _OBJC_CLASS_$_CNPhoneNumberHelper
- _OBJC_CLASS_$_NSProcessInfo
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.92
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.92.cold.1
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312.cold.1
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.314
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.317
- ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.324
- ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.391
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328.cold.1
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.329
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.22
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.24
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.24.cold.1
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.25
- ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.33
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319.cold.1
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.320
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.321
- ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.32
- ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.32.cold.1
- ___block_descriptor_32_e19_"NSDictionary"8?0l
- ___block_literal_global.12
- ___block_literal_global.317
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.351
- ___block_literal_global.91
- _objc_msgSend$ds_emailAddresses
- _objc_msgSend$ds_isLikeContact:
- _objc_msgSend$ds_name
- _objc_msgSend$ds_phoneNumbers
- _objc_msgSend$isLikeContact:
- _objc_msgSend$isPhoneNumber
- _objc_msgSend$isStringPhoneNumber:
- _objc_msgSend$processInfo
- _objc_msgSend$processName
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
CStrings:
+ "+()-"
+ "addCharactersInString:"
+ "componentsSeparatedByCharactersInSet:"
+ "controlCharacterSet"
+ "decimalDigitCharacterSet"
+ "ds_isPhoneNumber"
+ "ds_prettyPrintedPotentialPhoneNumber"
+ "formUnionWithCharacterSet:"
+ "phoneNumberCharacterSet"
+ "whitespaceAndNewlineCharacterSet"
- "com.apple.DigitalSeparation.SafetyCheckWhenBlockingExited"
- "ds_emailAddresses"
- "ds_isLikeContact:"
- "ds_name"
- "ds_phoneNumbers"
- "entrypoint"
- "fetchErrorCode"
- "isLikeContact:"
- "isPhoneNumber"
- "isStringPhoneNumber:"
- "processInfo"
- "processName"
- "stringByReplacingOccurrencesOfString:withString:"

```

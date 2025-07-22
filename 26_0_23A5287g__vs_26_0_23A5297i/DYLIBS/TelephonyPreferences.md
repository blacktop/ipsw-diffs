## TelephonyPreferences

> `/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`

```diff

-378.100.1.0.0
-  __TEXT.__text: 0x32d50
+380.100.4.0.0
+  __TEXT.__text: 0x32dd4
   __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_methlist: 0x3f48
   __TEXT.__const: 0x616
   __TEXT.__cstring: 0x2193
-  __TEXT.__oslogstring: 0x2410
+  __TEXT.__oslogstring: 0x243e
   __TEXT.__gcc_except_tab: 0x324
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__ustring: 0x9e

   __TEXT.__unwind_info: 0xfd0
   __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0xc74
-  __TEXT.__objc_methname: 0x9efd
+  __TEXT.__objc_methname: 0x9f13
   __TEXT.__objc_methtype: 0x1d8f
-  __TEXT.__objc_stubs: 0x61e0
-  __DATA_CONST.__got: 0x5f0
+  __TEXT.__objc_stubs: 0x6220
+  __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0xa20
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_selrefs: 0x2300
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x78

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/DefaultAppsSettings.framework/DefaultAppsSettings
+  - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3FD7E851-E335-3CD7-BC4C-2A909B387123
+  UUID: 3D494165-9B8A-3AFA-8E11-EDFC9DE7E503
   Functions: 1455
-  Symbols:   4769
-  CStrings:  2493
+  Symbols:   4772
+  CStrings:  2496
 
Symbols:
+ _OBJC_CLASS_$_FTDeviceSupport
+ _objc_msgSend$deviceType
+ _objc_msgSend$isGreenTea
Functions:
~ -[TPSPhonebookTelephonyController getPhoneNumberInfo] : 312 -> 444
CStrings:
+ "Skipping phone number lookup on GreenTea iPad"
+ "deviceType"
+ "isGreenTea"

```

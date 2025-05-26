## ContactsSettings

> `/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings`

```diff

-1232.1.0.0.0
-  __TEXT.__text: 0x58c8
+1238.0.0.0.0
+  __TEXT.__text: 0x5cac
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x502
+  __TEXT.__objc_methlist: 0x3cc
+  __TEXT.__cstring: 0x5e8
   __TEXT.__oslogstring: 0x1f0
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0xe5
-  __TEXT.__objc_methname: 0x16b1
-  __TEXT.__objc_methtype: 0x47e
-  __TEXT.__objc_stubs: 0x13c0
+  __TEXT.__unwind_info: 0x1f4
+  __TEXT.__objc_classname: 0x112
+  __TEXT.__objc_methname: 0x189d
+  __TEXT.__objc_methtype: 0x4d5
+  __TEXT.__objc_stubs: 0x14e0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb08
-  __DATA_CONST.__objc_selrefs: 0x5e8
-  __AUTH_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_const: 0xba0
+  __DATA_CONST.__objc_selrefs: 0x650
+  __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__data: 0x10
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_classrefs: 0xf0
+  __DATA.__objc_classrefs: 0x108
   __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x1e0
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x240
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 116
-  Symbols:   695
-  CStrings:  389
+  Functions: 124
+  Symbols:   727
+  CStrings:  417
 
Symbols:
+ -[ContactsSettingsPlugin onboardingControllerDidDismissSettings:]
+ -[ContactsSettingsPlugin onboardingController]
+ -[ContactsSettingsPlugin setOnboardingController:]
+ -[ContactsSettingsPlugin sharedNameAndPhotoAudience:]
+ -[ContactsSettingsPlugin sharedNameAndPhotoSharingFooterText]
+ -[ContactsSettingsPlugin showSharedNameAndPhotoSettings:]
+ _CNUIAllowMultiplePhoneNumbersSNaP
+ _CNUINarwhalEnabled
+ _OBJC_CLASS_$_CNEnvironment
+ _OBJC_CLASS_$_CNNicknameProvider
+ _OBJC_CLASS_$_CNSharedProfileOnboardingController
+ _OBJC_IVAR_$_ContactsSettingsPlugin._onboardingController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNSharedProfileOnboardingControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNSharedProfileOnboardingControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CNSharedProfileOnboardingControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CNSharedProfileOnboardingControllerDelegate
+ __OBJC_PROTOCOL_$_CNSharedProfileOnboardingControllerDelegate
+ _objc_msgSend$currentEnvironment
+ _objc_msgSend$initWithContactStore:
+ _objc_msgSend$isNicknameSharingEnabled
+ _objc_msgSend$nicknameProvider
+ _objc_msgSend$setOnboardingController:
+ _objc_msgSend$sharedNameAndPhotoSharingFooterText
+ _objc_msgSend$sharingAudience
+ _objc_msgSend$sharingAudienceDisplayString
+ _objc_msgSend$startOnboardingOrEditForMode:fromViewController:
CStrings:
+ "\x161%\x11"
+ "@\"CNSharedProfileOnboardingController\""
+ "CNSharedProfileOnboardingControllerDelegate"
+ "KTStaticId"
+ "NAME_AND_PHOTO_SHARING_ALWAYS_ASK_FOOTER"
+ "NAME_AND_PHOTO_SHARING_CONTACTS_ONLY_FOOTER"
+ "NAME_AND_PHOTO_SHARING_NOT_SHARING_FOOTER"
+ "Off"
+ "SharedNameAndPhoto"
+ "SharedNamePhotoSpacer"
+ "T@\"CNSharedProfileOnboardingController\",&,N,V_onboardingController"
+ "Transparency"
+ "_onboardingController"
+ "currentEnvironment"
+ "initWithContactStore:"
+ "isNicknameSharingEnabled"
+ "nicknameProvider"
+ "onboardingController"
+ "onboardingControllerDidDismissSettings:"
+ "onboardingControllerDidFinishSetup:"
+ "setOnboardingController:"
+ "sharedNameAndPhotoAudience:"
+ "sharedNameAndPhotoSharingFooterText"
+ "sharingAudience"
+ "sharingAudienceDisplayString"
+ "showSharedNameAndPhotoSettings:"
+ "snap_allow_multiple_phone_numbers"
+ "startOnboardingOrEditForMode:fromViewController:"
+ "v24@0:8@\"CNSharedProfileOnboardingController\"16"
- "\x161%"

```

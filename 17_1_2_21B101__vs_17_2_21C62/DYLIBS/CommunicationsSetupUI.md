## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1414.200.61.0.0
-  __TEXT.__text: 0x80d5c
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x6f74
-  __TEXT.__cstring: 0xa587
+1414.300.62.0.0
+  __TEXT.__text: 0x8063c
+  __TEXT.__auth_stubs: 0x11a0
+  __TEXT.__objc_methlist: 0x6fdc
+  __TEXT.__cstring: 0x9f27
   __TEXT.__const: 0x424
-  __TEXT.__gcc_except_tab: 0x31c8
-  __TEXT.__oslogstring: 0x52c7
-  __TEXT.__ustring: 0x140
+  __TEXT.__gcc_except_tab: 0x31f4
+  __TEXT.__oslogstring: 0x5336
+  __TEXT.__ustring: 0x40
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x28a
   __TEXT.__swift5_reflstr: 0x45

   __TEXT.__swift5_fieldmd: 0xd8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x25e4
+  __TEXT.__unwind_info: 0x25f8
   __TEXT.__objc_classname: 0xf6b
-  __TEXT.__objc_methname: 0x13562
+  __TEXT.__objc_methname: 0x13698
   __TEXT.__objc_methtype: 0x2b8b
-  __TEXT.__objc_stubs: 0xfb80
+  __TEXT.__objc_stubs: 0xfcc0
   __DATA_CONST.__got: 0x600
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc2d8
-  __DATA_CONST.__objc_selrefs: 0x4d60
+  __DATA_CONST.__objc_const: 0xc2f8
+  __DATA_CONST.__objc_selrefs: 0x4da8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0xa4e0
+  __AUTH_CONST.__cfstring: 0xa060
   __AUTH_CONST.__objc_const: 0x2010
   __AUTH_CONST.__const: 0xa48
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH.__objc_data: 0x1ce8
   __AUTH.__data: 0xc0
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x630
   __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0x530
+  __DATA.__objc_ivar: 0x534
   __DATA.__data: 0xd28
   __DATA.__bss: 0x6a8
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2777
-  Symbols:   9824
-  CStrings:  5600
+  Functions: 2784
+  Symbols:   9848
+  CStrings:  5583
 
Symbols:
+ +[CNFInternalSettingsUtilities killCallservicesd]
+ -[CNFRegController iMessageAccountMatchesiCloudAccount:]
+ -[CNFRegSettingsController configureSignOutForSpecifier:]
+ -[CNFRegSettingsController primaryAppleAccount]
+ -[CNFRegSettingsController refreshSharedNameAndPhotoSettingsAnimated:]
+ -[CNFRegSettingsController shouldShowSharedNameAndPhotoSpecifiers]
+ -[CNFRegSettingsController showSharedNameAndPhotoSettings:animated:]
+ -[CNFRegSettingsController signoutAccount:]
+ GCC_except_table103
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table170
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table193
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table95
+ GCC_except_table99
+ _OBJC_IVAR_$_CNFRegSettingsController._sharedNameAndPhotoSpecifiers
+ ___57-[CNFAccountRegistrar _accountRegistrationStatusChanged:]_block_invoke.171
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.688
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.692
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.693
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.712
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.714
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.716
+ ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.681
+ ___Block_byref_object_copy_.672
+ ___Block_byref_object_dispose_.673
+ ___block_literal_global.263
+ __unnamed_array_storage.336
+ _objc_msgSend$_debugFailureReason
+ _objc_msgSend$_isAppleIDUpdateNeeded
+ _objc_msgSend$aa_personID
+ _objc_msgSend$configureSignOutForSpecifier:
+ _objc_msgSend$iMessageAccountMatchesiCloudAccount:
+ _objc_msgSend$isAllowMultiplePhoneNumbersSNaPEnabled
+ _objc_msgSend$primaryAppleAccount
+ _objc_msgSend$refreshSharedNameAndPhotoSettingsAnimated:
+ _objc_msgSend$shouldShowSharedNameAndPhotoSpecifiers
+ _objc_msgSend$showSharedNameAndPhotoSettings:animated:
- -[CKSettingsMessagesController specifiers].cold.1
- GCC_except_table100
- GCC_except_table109
- GCC_except_table111
- GCC_except_table118
- GCC_except_table120
- GCC_except_table130
- GCC_except_table131
- GCC_except_table135
- GCC_except_table136
- GCC_except_table140
- GCC_except_table141
- GCC_except_table145
- GCC_except_table146
- GCC_except_table154
- GCC_except_table164
- GCC_except_table172
- GCC_except_table173
- GCC_except_table187
- GCC_except_table190
- GCC_except_table192
- GCC_except_table195
- GCC_except_table197
- GCC_except_table81
- GCC_except_table84
- GCC_except_table97
- _MarcoLogMadridLevel
- _MarcoShouldLogMadridLevel
- ___57-[CNFAccountRegistrar _accountRegistrationStatusChanged:]_block_invoke.151
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.677
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.681
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.682
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.701
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.703
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.705
- ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.670
- ___Block_byref_object_copy_.721
- ___Block_byref_object_dispose_.722
- ___block_literal_global.254
- __unnamed_array_storage.366
CStrings:
+ "\x0f\x04!"
+ "Check DSID of account, iCloud DSID: %@, iMessage account DSID : %@ for %@"
+ "MESSAGES_ACTIVATION_ERROR_TITLE_VERBOSE"
+ "MESSAGES_SIGN_OUT_GROUP_ID"
+ "MESSAGES_SIGN_OUT_ID"
+ "SHARED_NAME_AND_PHOTO_SETTINGS_GROUP"
+ "UPDATE_APPLEID_ERROR_ACTION"
+ "UPDATE_APPLEID_ERROR_MESSAGE"
+ "Using debug registration failure: %@"
+ "WAITING_FOR_ICLOUD_ERROR_ACTION"
+ "WAITING_FOR_ICLOUD_ERROR_MESSAGE"
+ "_sharedNameAndPhotoSpecifiers"
+ "aa_personID"
+ "configureSignOutForSpecifier:"
+ "iMessageAccountMatchesiCloudAccount:"
+ "isAllowMultiplePhoneNumbersSNaPEnabled"
+ "killCallservicesd"
+ "killall -9 callservicesd"
+ "prefs:root=APPLE_ACCOUNT&path=TRANSPARENCY"
+ "primaryAppleAccount"
+ "refreshSharedNameAndPhotoSettingsAnimated:"
+ "shouldShowSharedNameAndPhotoSpecifiers"
+ "showSharedNameAndPhotoSettings:animated:"
- "\x0f\x03!"
- "IMFoundation"

```

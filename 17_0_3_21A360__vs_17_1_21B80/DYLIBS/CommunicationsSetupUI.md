## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1414.100.1.2.1
-  __TEXT.__text: 0x801cc
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x6edc
-  __TEXT.__cstring: 0xa487
+1414.200.61.0.0
+  __TEXT.__text: 0x80d5c
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_methlist: 0x6f74
+  __TEXT.__cstring: 0xa587
   __TEXT.__const: 0x424
-  __TEXT.__gcc_except_tab: 0x317c
-  __TEXT.__oslogstring: 0x5254
+  __TEXT.__gcc_except_tab: 0x31c8
+  __TEXT.__oslogstring: 0x52c7
   __TEXT.__ustring: 0x140
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x28a

   __TEXT.__swift5_fieldmd: 0xd8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__unwind_info: 0x25e4
   __TEXT.__objc_classname: 0xf6b
-  __TEXT.__objc_methname: 0x13448
-  __TEXT.__objc_methtype: 0x2bbd
-  __TEXT.__objc_stubs: 0xfa80
+  __TEXT.__objc_methname: 0x13562
+  __TEXT.__objc_methtype: 0x2b8b
+  __TEXT.__objc_stubs: 0xfb80
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc2f8
-  __DATA_CONST.__objc_selrefs: 0x4cf8
+  __DATA_CONST.__objc_const: 0xc2d8
+  __DATA_CONST.__objc_selrefs: 0x4d60
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0xa420
+  __AUTH_CONST.__cfstring: 0xa4e0
   __AUTH_CONST.__objc_const: 0x2010
   __AUTH_CONST.__const: 0xa48
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_got: 0x8f0
   __AUTH.__objc_data: 0x1ce8
   __AUTH.__data: 0xc0
   __DATA.__objc_protorefs: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B8585CE6-B9F4-33C6-AB60-5EA68FBF5678
-  Functions: 2761
-  Symbols:   9781
-  CStrings:  6891
+  UUID: 98BB7072-D5EC-3528-A041-CC3205C5EF32
+  Functions: 2777
+  Symbols:   9824
+  CStrings:  6919
 
Symbols:
+ -[CKSettingsMessagesController _debugFailureReason]
+ -[CKSettingsMessagesController _failedAccounts]
+ -[CKSettingsMessagesController _isAppleIDUpdateNeeded]
+ -[CKSettingsMessagesController _isIDSDelayRegistrationEnabled]
+ -[CKSettingsMessagesController _isRegistrationInProgress]
+ -[CKSettingsMessagesController _nicknameSettingsDidChange:]
+ -[CKSettingsMessagesController _registrationFailures:areAllOfKind:]
+ -[CKSettingsMessagesController _registrationFailures:containsFailure:]
+ -[CKSettingsMessagesController _registrationFailures]
+ -[CKSettingsMessagesController shouldShowUpdateAppleID]
+ -[CKSettingsMessagesController showCKVSettings:]
+ -[CKSettingsMessagesController specifiers].cold.1
+ -[CNFRegController isAccountKeyCDPSyncingOrWaitingForUser]
+ -[IMAccount(CommunicationsSetupUI) isAccountKeyCDPSyncingOrWaitingForUser]
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table132
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table63
+ _CNFRegStringTableNameForServiceType
+ ___51-[CNFRegSettingsController handleCallStatusChanged]_block_invoke
+ ___57-[CNFAccountRegistrar _accountRegistrationStatusChanged:]_block_invoke.151
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.677
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.681
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.682
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.701
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.703
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.705
+ ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.670
+ ___Block_byref_object_copy_.721
+ ___Block_byref_object_dispose_.722
+ ___block_descriptor_41_e8_32s_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_literal_global.254
+ __unnamed_array_storage.366
+ _objc_msgSend$_failedAccounts
+ _objc_msgSend$_isIDSDelayRegistrationEnabled
+ _objc_msgSend$_isRegistrationInProgress
+ _objc_msgSend$_registrationFailures
+ _objc_msgSend$_registrationFailures:containsFailure:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isAccountKeyCDPSyncingOrWaitingForUser
+ _objc_msgSend$shouldShowUpdateAppleID
+ _objc_release_x2
- GCC_except_table108
- GCC_except_table117
- GCC_except_table125
- GCC_except_table165
- GCC_except_table166
- GCC_except_table167
- GCC_except_table170
- ___57-[CNFAccountRegistrar _accountRegistrationStatusChanged:]_block_invoke.150
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.674
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.678
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.679
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.698
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.700
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.702
- ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.667
- ___Block_byref_object_copy_.701
- ___Block_byref_object_dispose_.702
- ___block_literal_global.251
- __unnamed_array_storage.361
CStrings:
+ "Account (%@) failed with failure reason: %@ and alert info %@."
+ "B32@0:8@16q24"
+ "Failed accounts: %@ with registration failures: %@"
+ "IDS"
+ "IDSKTDelayRegistration"
+ "Invalid action URL %@."
+ "MADRID_UPDATE_APPLEID_BUTTON"
+ "Registration status: %@ failureReason: %@"
+ "UPDATE_APPLEID_DESCRIPTION"
+ "WAITING_FOR_ICLOUD_DESCRIPTION"
+ "_debugFailureReason"
+ "_failedAccounts"
+ "_isAppleIDUpdateNeeded"
+ "_isIDSDelayRegistrationEnabled"
+ "_isRegistrationInProgress"
+ "_nicknameSettingsDidChange:"
+ "_registrationFailures"
+ "_registrationFailures:areAllOfKind:"
+ "_registrationFailures:containsFailure:"
+ "integerForKey:"
+ "isAccountKeyCDPSyncingOrWaitingForUser"
+ "shouldShowUpdateAppleID"
+ "showCKVSettings:"
+ "userRegistrationKTFailure"
- "Account (%@) failed with alert info %@."
- "Registration status: %@"
- "generatePosterAnimationControllerWithWindowScene:imageHandler:"
- "v32@0:8@\"UIWindowScene\"16@?<v@?@\"UIViewController\"@\"NSError\">24"

```

## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-493.2.1.1.0
-  __TEXT.__text: 0xb58b8
+494.4.9.0.0
+  __TEXT.__text: 0xb5510
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x6f4c
+  __TEXT.__objc_methlist: 0x6f64
   __TEXT.__const: 0x1144
   __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__cstring: 0x47a7
-  __TEXT.__oslogstring: 0x910a
+  __TEXT.__cstring: 0x4717
+  __TEXT.__oslogstring: 0x90b3
   __TEXT.__dlopen_cstrs: 0x387
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x16be

   __TEXT.__unwind_info: 0x2d7c
   __TEXT.__eh_frame: 0x53c
   __TEXT.__objc_classname: 0x1aa2
-  __TEXT.__objc_methname: 0x1621d
+  __TEXT.__objc_methname: 0x1622d
   __TEXT.__objc_methtype: 0x42ef
-  __TEXT.__objc_stubs: 0x10800
+  __TEXT.__objc_stubs: 0x107e0
   __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0x23f8
   __DATA_CONST.__objc_classlist: 0x548

   __DATA_CONST.__objc_selrefs: 0x50b8
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__objc_const: 0x3a60
-  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__cfstring: 0x3ce0
   __AUTH_CONST.__const: 0x1a68
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4311
-  Symbols:   12538
-  CStrings:  5539
+  Functions: 4309
+  Symbols:   12533
+  CStrings:  5532
 
Symbols:
+ -[AAUIAccountRecoveryViewController _continueShowingAddCustodian]
+ -[AAUIAccountRecoveryViewController _showAddCustodian].cold.1
+ -[AAUIMyCustodianActionHandler _continueDoingDestructiveAction:specifier:account:]
+ -[AAUIMyCustodianActionHandler doDestructiveAction:specifier:].cold.1
+ -[AAUIRecoveryFactorController _continueAddingRecoveryContact]
+ GCC_except_table19
+ GCC_except_table54
+ GCC_except_table65
+ GCC_except_table71
+ ___62-[AAUIRecoveryFactorController _continueAddingRecoveryContact]_block_invoke
+ ___62-[AAUISignInViewController _attemptAuthenticationWithContext:]_block_invoke.204
+ ___63+[AAUISignInViewController phoneNumberSupportedWithCompletion:]_block_invoke.28
+ ___82-[AAUIMyCustodianActionHandler _continueDoingDestructiveAction:specifier:account:]_block_invoke
+ ___82-[AAUIMyCustodianActionHandler _continueDoingDestructiveAction:specifier:account:]_block_invoke.cold.1
+ ___block_literal_global.170
+ _objc_msgSend$_continueAddingRecoveryContact
+ _objc_msgSend$_continueDoingDestructiveAction:specifier:account:
+ _objc_msgSend$_continueShowingAddCustodian
- +[AAUIFeatureFlags isProxAdvertisementOverridden]
- +[AAUIFeatureFlags isProxAdvertisementOverridden].cold.1
- -[AAUISignInViewController _shouldDisableProximityAppleIDAdvertisement]
- -[AAUISignInViewController _shouldDisableProximityAppleIDAdvertisement].cold.1
- -[AAUISignInViewController _shouldDisableProximityAppleIDAdvertisement].cold.2
- GCC_except_table23
- GCC_except_table66
- GCC_except_table72
- ___58-[AAUIRecoveryFactorController startAddingRecoveryContact]_block_invoke
- ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke
- ___62-[AAUIMyCustodianActionHandler doDestructiveAction:specifier:]_block_invoke.cold.1
- ___62-[AAUISignInViewController _attemptAuthenticationWithContext:]_block_invoke.221
- ___63+[AAUISignInViewController phoneNumberSupportedWithCompletion:]_block_invoke.31
- ___block_literal_global.182
- ___block_literal_global.187
- _objc_msgSend$_shouldDisableProximityAppleIDAdvertisement
- _objc_msgSend$akURLBag
- _objc_msgSend$configurationAtKey:
- _objc_msgSend$isProxAdvertisementOverridden
CStrings:
+ "_continueAddingRecoveryContact"
+ "_continueDoingDestructiveAction:specifier:account:"
+ "_continueShowingAddCustodian"
+ "appleAccount found nil, returning without adding RC"
- "AppleIDSetup/ProxAdvertisementOverride=%d"
- "ProxAdvertisementOverride"
- "Proximity Authentication is disabled."
- "Proximity Authentication override feature flag is enabled."
- "SIGN_IN_ACTION_DONT_HAVE_AN_APPLE_ID"
- "_shouldDisableProximityAppleIDAdvertisement"
- "aidProxAdvertisementDisabled"
- "configurationAtKey:"
- "dont-have-apple-id-button"
- "forgot-password-button"
- "isProxAdvertisementOverridden"

```

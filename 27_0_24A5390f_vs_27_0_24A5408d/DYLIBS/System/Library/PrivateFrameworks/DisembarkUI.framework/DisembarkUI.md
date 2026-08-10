## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0x1f3b8
-  __TEXT.__objc_methlist: 0x2920
+285.0.0.0.0
+  __TEXT.__text: 0x20790
+  __TEXT.__objc_methlist: 0x2a38
   __TEXT.__const: 0x194
-  __TEXT.__cstring: 0x1d54
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__oslogstring: 0xda5
+  __TEXT.__cstring: 0x1df4
+  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__oslogstring: 0x109b
   __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__swift5_typeref: 0x1c0
   __TEXT.__swift5_capture: 0xf0

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__unwind_info: 0x850
   __TEXT.__eh_frame: 0x180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__const: 0x1070
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a78
+  __DATA_CONST.__objc_selrefs: 0x1b10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x4c8
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x4ff8
+  __AUTH_CONST.__cfstring: 0x1640
+  __AUTH_CONST.__objc_const: 0x50a8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0xf98
   __AUTH.__data: 0x140
-  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0xaf0
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/swift/libswiftARKit.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 950
-  Symbols:   2565
-  CStrings:  359
+  Functions: 988
+  Symbols:   2632
+  CStrings:  378
 
Symbols:
+ -[DKAccountProvider _validateWalrusForSignOutWithCompletion:]
+ -[DKAccountProvider authenticateForSignOutWithPresentingViewController:completion:]
+ -[DKAccountProvider authenticatedWipeToken]
+ -[DKAccountProvider didValidateWalrusSignOut]
+ -[DKAccountProvider setAuthenticatedWipeToken:]
+ -[DKAccountProvider setDidValidateWalrusSignOut:]
+ -[DKConfiguration .cxx_destruct]
+ -[DKConfiguration preEraseStep]
+ -[DKConfiguration setPreEraseStep:]
+ -[DKEraseFlow _authenticateSignOutIfNeededWithCompletion:]
+ -[DKEraseFlow _erase]
+ -[DKEraseFlow _presentPreEraseStep]
+ -[DKEraseFlow _presentUnknownFailureAlertThenEndFlowForCancellationWithReason:]
+ -[DKEraseFlow _runPreEraseStep]
+ -[DKEraseFlow _signOutIfNeededWithCompletion:]
+ -[DKFindMyProvider _authenticateDisableWithPresentingViewController:keepAlertVisible:completion:]
+ -[DKFindMyProvider _disableInContextWithWipeToken:completion:]
+ -[DKFindMyProvider _handleAuthenticateDisableResultWithCancel:wipeToken:completion:]
+ -[DKFindMyProvider authenticateFindMyDisableWithPresentingViewController:completion:]
+ -[DKFindMyProvider commitFindMyDisableWithWipeToken:completion:]
+ -[DKFindMyProvider disableFindMyDeviceWithWipeToken:presentingViewController:completion:]
+ GCC_except_table33
+ GCC_except_table39
+ GCC_except_table49
+ GCC_except_table59
+ GCC_except_table93
+ _OBJC_IVAR_$_DKAccountProvider._authenticatedWipeToken
+ _OBJC_IVAR_$_DKAccountProvider._didValidateWalrusSignOut
+ _OBJC_IVAR_$_DKConfiguration._preEraseStep
+ ___21-[DKEraseFlow _erase]_block_invoke
+ ___31-[DKEraseFlow _runPreEraseStep]_block_invoke
+ ___35-[DKEraseFlow _presentPreEraseStep]_block_invoke
+ ___35-[DKEraseFlow _presentPreEraseStep]_block_invoke_2
+ ___46-[DKEraseFlow _signOutIfNeededWithCompletion:]_block_invoke
+ ___46-[DKEraseFlow _signOutIfNeededWithCompletion:]_block_invoke_2
+ ___58-[DKEraseFlow _authenticateSignOutIfNeededWithCompletion:]_block_invoke
+ ___58-[DKEraseFlow _authenticateSignOutIfNeededWithCompletion:]_block_invoke_2
+ ___61-[DKAccountProvider _validateWalrusForSignOutWithCompletion:]_block_invoke
+ ___62-[DKFindMyProvider _disableInContextWithWipeToken:completion:]_block_invoke
+ ___79-[DKEraseFlow _presentUnknownFailureAlertThenEndFlowForCancellationWithReason:]_block_invoke
+ ___83-[DKAccountProvider authenticateForSignOutWithPresentingViewController:completion:]_block_invoke
+ ___83-[DKAccountProvider authenticateForSignOutWithPresentingViewController:completion:]_block_invoke_2
+ ___85-[DKFindMyProvider authenticateFindMyDisableWithPresentingViewController:completion:]_block_invoke
+ ___97-[DKFindMyProvider _authenticateDisableWithPresentingViewController:keepAlertVisible:completion:]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e21_v20?0B8"NSString"12lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e21_v20?0B8"NSString"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e21_v20?0B8"NSString"12ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftAppleArchive_$_DisembarkUI
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_DisembarkUI
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_DisembarkUI
+ _objc_msgSend$_authenticateDisableWithPresentingViewController:keepAlertVisible:completion:
+ _objc_msgSend$_authenticateSignOutIfNeededWithCompletion:
+ _objc_msgSend$_disableInContextWithWipeToken:completion:
+ _objc_msgSend$_erase
+ _objc_msgSend$_handleAuthenticateDisableResultWithCancel:wipeToken:completion:
+ _objc_msgSend$_presentPreEraseStep
+ _objc_msgSend$_presentUnknownFailureAlertThenEndFlowForCancellationWithReason:
+ _objc_msgSend$_runPreEraseStep
+ _objc_msgSend$_signOutIfNeededWithCompletion:
+ _objc_msgSend$_validateWalrusForSignOutWithCompletion:
+ _objc_msgSend$authenticateFindMyDisableWithPresentingViewController:completion:
+ _objc_msgSend$authenticateForSignOutWithPresentingViewController:completion:
+ _objc_msgSend$authenticatedWipeToken
+ _objc_msgSend$commitFindMyDisableWithWipeToken:completion:
+ _objc_msgSend$didValidateWalrusSignOut
+ _objc_msgSend$disableFindMyDeviceWithWipeToken:presentingViewController:completion:
+ _objc_msgSend$preEraseStep
+ _objc_msgSend$setAuthenticatedWipeToken:
+ _objc_msgSend$setDidValidateWalrusSignOut:
- -[DKEraseFlow _signOutAndEraseDevice]
- GCC_except_table31
- GCC_except_table47
- GCC_except_table57
- ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke
- ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke_2
- ___88-[DKAccountProvider signOutFlowController:performWalrusValidationForAccount:completion:]_block_invoke
- _objc_msgSend$_signOutAndEraseDevice
CStrings:
+ "-[DKEraseFlow _authenticateSignOutIfNeededWithCompletion:]"
+ "-[DKEraseFlow _signOutIfNeededWithCompletion:]"
+ "-[DKFindMyProvider commitFindMyDisableWithWipeToken:completion:]"
+ "Authenticating Find My disable..."
+ "Authenticating sign out of primary Apple account..."
+ "Committing Find My disable with wipe token..."
+ "Failed to authenticate sign out of primary Apple account: %@"
+ "Find My disable authenticated; returning wipe token to caller for commit."
+ "Find My disable authentication canceled; aborting."
+ "Find My disable authentication did not return a wipe token; treating as failure."
+ "Find My not enabled; nothing to commit."
+ "Find My not enabled; skipping disable authentication."
+ "No pre-erase step configured; advancing to erase."
+ "Pre-Erase Step"
+ "Pre-erase step completed; proceeding to erase"
+ "Pre-erase step did not complete; ending flow without erasing"
+ "Running pre-erase step before erase..."
+ "Sign-out authentication did not succeed; ending flow without erasing"
+ "a"
+ "wipeToken"
- "-[DKEraseFlow _signOutAndEraseDevice]"
```

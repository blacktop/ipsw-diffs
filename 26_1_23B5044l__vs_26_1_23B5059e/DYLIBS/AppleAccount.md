## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1037.0.0.0.0
-  __TEXT.__text: 0xe90d8
+1037.125.3.0.0
+  __TEXT.__text: 0xe9510
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xad34
-  __TEXT.__cstring: 0xedfc
+  __TEXT.__objc_methlist: 0xad8c
+  __TEXT.__cstring: 0xee3c
   __TEXT.__const: 0x2380
   __TEXT.__gcc_except_tab: 0x249c
-  __TEXT.__oslogstring: 0xfc1d
+  __TEXT.__oslogstring: 0xfcbd
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_typeref: 0x2ed

   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2ef0
+  __TEXT.__unwind_info: 0x2f08
   __TEXT.__eh_frame: 0x3e8
-  __TEXT.__objc_classname: 0x1fac
-  __TEXT.__objc_methname: 0x1577f
-  __TEXT.__objc_methtype: 0x2fe6
-  __TEXT.__objc_stubs: 0xc0c0
-  __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0x3a68
+  __TEXT.__objc_classname: 0x1fae
+  __TEXT.__objc_methname: 0x15892
+  __TEXT.__objc_methtype: 0x2ff8
+  __TEXT.__objc_stubs: 0xc140
+  __DATA_CONST.__got: 0xd88
+  __DATA_CONST.__const: 0x3a78
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4da8
+  __DATA_CONST.__objc_selrefs: 0x4de8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x7160
-  __AUTH_CONST.__cfstring: 0xcc60
-  __AUTH_CONST.__objc_const: 0x23760
+  __AUTH_CONST.__cfstring: 0xcca0
+  __AUTH_CONST.__objc_const: 0x237b0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0xb88
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0xb9c
-  __DATA.__data: 0x1a50
+  __DATA.__objc_ivar: 0xba4
+  __DATA.__data: 0x1a48
   __DATA.__bss: 0x1080
   __DATA.__common: 0x91
   __DATA_DIRTY.__objc_data: 0x4600

   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4CCB2E90-1A2B-3737-893F-E8461F31E5A1
-  Functions: 4886
-  Symbols:   16151
-  CStrings:  8883
+  UUID: C82DDFBB-2092-3E99-A417-5CAA7754D7B3
+  Functions: 4895
+  Symbols:   16180
+  CStrings:  8902
 
Symbols:
+ -[AADataclassManager setUserDefaults:]
+ -[AADataclassManager userDefaultsDisabledDataclasses]
+ -[AADataclassManager userDefaultsDisabledDataclasses].cold.1
+ -[AADataclassManager userDefaults]
+ -[AASignInFlowController dataclassManager]
+ -[AASignInFlowController initWithAccountStore:dataclassManager:]
+ -[ACAccount(AppleAccount_Internal) aa_isSubscribedToTrustedContactContainers]
+ -[ACAccount(AppleAccount_Internal) aa_setSubscribedToTrustedContactContainers:]
+ GCC_except_table61
+ _AAUserDefaultsDisabledDataclassesKey
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_AADataclassManager._userDefaults
+ _OBJC_IVAR_$_AASignInFlowController._dataclassManager
+ ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.151
+ ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.144
+ ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.144.cold.1
+ ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.141
+ ___75-[AADataclassManager filterDataclassesForPossibleAutoEnablementForAccount:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e21_B24?0"NSString"8Q16ls32l8s40l8
+ ___block_literal_global.122
+ ___block_literal_global.132
+ _kAAAccountSubscribedToTrustedContactContainersKey
+ _objc_msgSend$dataclassManager
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$userDefaults
+ _objc_msgSend$userDefaultsDisabledDataclasses
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.150
- ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.137
- ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.137.cold.1
- ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.140
- ___block_descriptor_40_e8_32s_e21_B24?0"NSString"8Q16ls32l8
- ___block_literal_global.116
- ___block_literal_global.125
CStrings:
+ "@\"NSUserDefaults\""
+ "Checking if any dataclasses should be disabled from user defaults."
+ "DisabledDataclasses"
+ "Find My dataclass is disabled in user defaults."
+ "T@\"NSUserDefaults\",&,N,V_userDefaults"
+ "User defaults disabled dataclasses: %@"
+ "_userDefaults"
+ "aa_isSubscribedToTrustedContactContainers"
+ "aa_setSubscribedToTrustedContactContainers:"
+ "dataclassManager"
+ "initWithAccountStore:dataclassManager:"
+ "initWithSuiteName:"
+ "r"
+ "setUserDefaults:"
+ "subscribedToTrustedContactContainers"
+ "userDefaults"
+ "userDefaultsDisabledDataclasses"

```

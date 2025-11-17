## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-553.250.1.0.0
-  __TEXT.__text: 0x24f004
-  __TEXT.__auth_stubs: 0x3bc0
+553.250.3.0.0
+  __TEXT.__text: 0x252f00
+  __TEXT.__auth_stubs: 0x3be0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x244
-  __TEXT.__objc_methlist: 0xb484
-  __TEXT.__cstring: 0xa579
-  __TEXT.__const: 0xbed4
-  __TEXT.__gcc_except_tab: 0x169c
-  __TEXT.__oslogstring: 0xe5ec
+  __TEXT.__objc_methlist: 0xb52c
+  __TEXT.__cstring: 0xa6b9
+  __TEXT.__const: 0xbeee
+  __TEXT.__gcc_except_tab: 0x16cc
+  __TEXT.__oslogstring: 0xe81c
   __TEXT.__dlopen_cstrs: 0x526
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x4ba8
-  __TEXT.__swift5_typeref: 0xd64a
-  __TEXT.__swift5_reflstr: 0x2616
-  __TEXT.__swift5_fieldmd: 0x247c
+  __TEXT.__constg_swiftt: 0x4bf8
+  __TEXT.__swift5_typeref: 0xd68a
+  __TEXT.__swift5_reflstr: 0x2646
+  __TEXT.__swift5_fieldmd: 0x2494
   __TEXT.__swift5_types: 0x454
-  __TEXT.__swift5_capture: 0x2a24
+  __TEXT.__swift5_capture: 0x2b4c
   __TEXT.__swift5_assocty: 0xc50
   __TEXT.__swift5_proto: 0x5c4
   __TEXT.__swift_as_entry: 0x108

   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5650
+  __TEXT.__unwind_info: 0x56a0
   __TEXT.__eh_frame: 0x1518
-  __TEXT.__objc_classname: 0x2210
-  __TEXT.__objc_methname: 0x1b7a9
-  __TEXT.__objc_methtype: 0x508e
-  __TEXT.__objc_stubs: 0x13ba0
-  __DATA_CONST.__got: 0x1c68
-  __DATA_CONST.__const: 0x3248
-  __DATA_CONST.__objc_classlist: 0x7f0
+  __TEXT.__objc_classname: 0x2247
+  __TEXT.__objc_methname: 0x1b912
+  __TEXT.__objc_methtype: 0x5110
+  __TEXT.__objc_stubs: 0x13c40
+  __DATA_CONST.__got: 0x1c70
+  __DATA_CONST.__const: 0x3288
+  __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x370
+  __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6858
-  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x68b0
+  __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x1e00
-  __AUTH_CONST.__const: 0x9dc8
-  __AUTH_CONST.__cfstring: 0x4b60
-  __AUTH_CONST.__objc_const: 0x3d388
+  __AUTH_CONST.__auth_got: 0x1e10
+  __AUTH_CONST.__const: 0xa0c0
+  __AUTH_CONST.__cfstring: 0x4ce0
+  __AUTH_CONST.__objc_const: 0x3d7b0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x6c10
+  __AUTH.__objc_data: 0x6cc0
   __AUTH.__data: 0x29b0
-  __DATA.__objc_ivar: 0xbe8
-  __DATA.__data: 0x5590
+  __DATA.__objc_ivar: 0xbec
+  __DATA.__data: 0x5640
   __DATA.__bss: 0xbfe0
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2D30A93-66DA-3917-AFD9-B2ADFAA3AE47
-  Functions: 11617
-  Symbols:   17530
-  CStrings:  8123
+  UUID: 4CB05FD6-509F-3435-AB74-4956FC1DA0B1
+  Functions: 11675
+  Symbols:   17598
+  CStrings:  8177
 
Symbols:
+ +[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]
+ +[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:].cold.1
+ +[AAUIPaymentVerificationHook _contextTypeFromProcessName:]
+ -[AAUIConnectToFamilyFlowContext .cxx_destruct]
+ -[AAUIConnectToFamilyFlowContext assetID]
+ -[AAUIConnectToFamilyFlowContext setAssetID:]
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:]
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:].cold.1
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:].cold.2
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:].cold.3
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:].cold.4
+ GCC_except_table17
+ _AAUISignOutErrorDomain
+ _OBJC_CLASS_$_AAUIConnectToFamilyFlowContext
+ _OBJC_CLASS_$_AKAuthenticatableResource
+ _OBJC_IVAR_$_AAUIConnectToFamilyFlowContext._assetID
+ _OBJC_METACLASS_$_AAUIConnectToFamilyFlowContext
+ __OBJC_$_CLASS_METHODS_AAUIPaymentVerificationHook
+ __OBJC_$_INSTANCE_METHODS_AAUIConnectToFamilyFlowContext
+ __OBJC_$_INSTANCE_VARIABLES_AAUIConnectToFamilyFlowContext
+ __OBJC_$_PROP_LIST_AAUIConnectToFamilyFlowContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPWalrusStatusProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CDPWalrusStatusProvider
+ __OBJC_$_PROTOCOL_REFS_CDPWalrusStatusProvider
+ __OBJC_CLASS_RO_$_AAUIConnectToFamilyFlowContext
+ __OBJC_LABEL_PROTOCOL_$_CDPWalrusStatusProvider
+ __OBJC_METACLASS_RO_$_AAUIConnectToFamilyFlowContext
+ __OBJC_PROTOCOL_$_CDPWalrusStatusProvider
+ ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.78
+ ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.79
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.66
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.74
+ ___59+[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]_block_invoke
+ ___59+[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]_block_invoke_2
+ ___59+[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]_block_invoke_2.cold.1
+ ___59+[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]_block_invoke_2.cold.2
+ ___59+[AAUIFeatureFlags isPrivacyRepromptEnabledWithCompletion:]_block_invoke_2.cold.3
+ ___85-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:]_block_invoke
+ ___85-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithContext:completion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ _block_copy_helper.107
+ _block_copy_helper.42
+ _block_descriptor.109
+ _block_descriptor.44
+ _block_destroy_helper.108
+ _block_destroy_helper.43
+ _flat unique So23CDPWalrusStatusProvider_p
+ _kAAAnalyticsEventPrivacyRepromptClicked
+ _kAAAnalyticsEventPrivacyRepromptShown
+ _objc_msgSend$_contextTypeFromProcessName:
+ _objc_msgSend$assetID
+ _objc_msgSend$authenticatableResource
+ _objc_msgSend$configurationValueForKey:fromCache:completion:
+ _objc_msgSend$setAuthenticatableResource:
+ _symbolic SuIegd_
+ _symbolic SuIegr_
+ _symbolic SuIegy_
+ _symbolic ______pSg So23CDPWalrusStatusProviderP
- +[AAUIFeatureFlags isPrivacyRepromptEnabled]
- +[AAUIFeatureFlags isPrivacyRepromptEnabled].cold.1
- +[AAUIFeatureFlags isPrivacyRepromptEnabled].cold.2
- -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]
- -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:].cold.1
- ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.53
- ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.54
- ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.41
- ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.48
- ___77-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]_block_invoke
- ___77-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]_block_invoke.cold.1
- _block_copy_helper.41
- _block_descriptor.43
- _block_destroy_helper.42
CStrings:
+ "@\"CDPCombinedWalrusStatus\"24@0:8^@16"
+ "AAUIConnectToFamilyFlowContext"
+ "Apple Account & Privacy"
+ "Buddy"
+ "CDPWalrusStatusProvider"
+ "ConnectToFamilyFlowPresenter - customShieldAssetID property not available yet (waiting for rdar://162647923)"
+ "ConnectToFamilyFlowPresenter - present with context (assetID: %@)."
+ "ConnectToFamilyFlowPresenter - setting customShieldAssetID to: %{public}@"
+ "Error fetching consent reprompt config: %@, falling back to OS feature flag"
+ "Failed to query CDP Walrus status: %s"
+ "Missing altDSID or flow ID for telemetry"
+ "Preferences"
+ "Privacy reprompt clicked event sent with ADP state: %lu"
+ "Privacy reprompt disabled by server kill switch"
+ "Privacy reprompt shown event sent with ADP state: %lu"
+ "Q24@0:8^@16"
+ "Setup"
+ "T@\"NSString\",C,N,V_assetID"
+ "_assetID"
+ "_contextTypeFromProcessName:"
+ "advancedDataProtectionState"
+ "assetID"
+ "authenticatableResource"
+ "buddy"
+ "com.apple.appleaccount.privacyRepromptClicked"
+ "com.apple.appleaccount.privacyRepromptShown"
+ "combinedWalrusStatus:"
+ "combinedWalrusStatusWithCompletion:"
+ "configurationValueForKey:fromCache:completion:"
+ "customShieldAssetID"
+ "disableConsentReprompt"
+ "flowType"
+ "initWithAccount:walrusStatusProvider:"
+ "isPrivacyRepromptEnabledWithCompletion called with nil completion block"
+ "isPrivacyRepromptEnabledWithCompletion:"
+ "presentConnectToFamilyFlowWithContext:completion:"
+ "pvk"
+ "repairWalrusStatusWithCompletion:"
+ "setAssetID:"
+ "setAuthenticatableResource:"
+ "setCustomShieldAssetID:"
+ "settings"
+ "v24@0:8@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">16"
+ "v24@0:8@?<v@?Q@\"NSError\">16"
+ "v24@?0@8@\"NSError\"16"
+ "walrusStatusProvider"
- "About Apple Account & Privacy"
- "AppleAccountUI/PrivacyReprompt is enabled on internal builds."
- "ConnectToFamilyFlowPresenter - present."
- "isPrivacyRepromptEnabled"
- "presentConnectToFamilyFlowWithCompletion:"

```

## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.1.1.0.0
-  __TEXT.__text: 0x6f828
+345.10.20.0.0
+  __TEXT.__text: 0x6faa0
   __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x30e4
+  __TEXT.__objc_methlist: 0x30fc
   __TEXT.__const: 0x438
-  __TEXT.__cstring: 0x1a3f4
-  __TEXT.__oslogstring: 0x5ad
+  __TEXT.__cstring: 0x1a524
+  __TEXT.__oslogstring: 0x5bd
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xcb

   __TEXT.__unwind_info: 0x16f8
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x2bc
-  __TEXT.__objc_methname: 0xcaaf
+  __TEXT.__objc_methname: 0xcb4d
   __TEXT.__objc_methtype: 0x114c
-  __TEXT.__objc_stubs: 0x7be0
+  __TEXT.__objc_stubs: 0x7c80
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x177c
+  __DATA_CONST.__const: 0x17a4
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2af8
+  __DATA_CONST.__objc_selrefs: 0x2b18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0xb18
-  __AUTH_CONST.__cfstring: 0x5320
-  __AUTH_CONST.__objc_const: 0x7210
+  __AUTH_CONST.__cfstring: 0x5360
+  __AUTH_CONST.__objc_const: 0x7250
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x3e8
+  __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x2f8
-  __DATA.__objc_ivar: 0xa2c
+  __DATA.__objc_ivar: 0xa34
   __DATA.__data: 0xa40
   __DATA.__common: 0x40
   __DATA.__bss: 0x740

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97EE7FED-9167-3AD8-88D3-CDD70B06F1AE
-  Functions: 2845
-  Symbols:   8342
-  CStrings:  6073
+  UUID: 710B0D51-5F8D-3D7A-B752-41CAAB4A69F2
+  Functions: 2848
+  Symbols:   8356
+  CStrings:  6090
 
Symbols:
+ -[HDSSetupService activateWithCompletion:].cold.1
+ -[HDSSetupSession _runDataAndPrivacy]
+ -[HDSSetupSession _runDataAndPrivacy].cold.1
+ -[HDSSetupSession _runDataAndPrivacy].cold.2
+ -[HDSSetupSession _runDataAndPrivacy].cold.3
+ -[HDSSetupSession _runDataAndPrivacy].cold.4
+ -[HDSSetupSession dataAndPrivacyAgreed]
+ -[HDSSetupSession promptForDataAndPrivacyHandler]
+ -[HDSSetupSession setPromptForDataAndPrivacyHandler:]
+ GCC_except_table11
+ GCC_except_table310
+ GCC_except_table369
+ GCC_except_table420
+ _OBJC_IVAR_$_HDSSetupSession._dataPrivacyAgreed
+ _OBJC_IVAR_$_HDSSetupSession._dataPrivacyState
+ _OBJC_IVAR_$_HDSSetupSession._promptForDataAndPrivacyHandler
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1665
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1665.cold.1
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.662
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.662.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.684
+ ___39-[HDSSetupSession dataAndPrivacyAgreed]_block_invoke
+ ___39-[HDSSetupSession dataAndPrivacyAgreed]_block_invoke.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_21
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_21.cold.1
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1812
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1813
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1813.cold.1
+ ___block_descriptor_40_e8_32s_e31_v24?0"NSString"8"NSString"16ls32l8
+ ___block_literal_global.1667
+ ___block_literal_global.3574
+ ___block_literal_global.3578
+ ___block_literal_global.3582
+ ___block_literal_global.3585
+ ___block_literal_global.3588
+ ___block_literal_global.3596
+ ___block_literal_global.3600
+ ___block_literal_global.3614
+ ___block_literal_global.3618
+ ___block_literal_global.3632
+ ___block_literal_global.3635
+ ___block_literal_global.3638
+ ___block_literal_global.3642
+ ___block_literal_global.3646
+ ___block_literal_global.3664
+ ___block_literal_global.3676
+ ___block_literal_global.3680
+ ___block_literal_global.3683
+ ___block_literal_global.3686
+ ___block_literal_global.3690
+ ___block_literal_global.3695
+ ___block_literal_global.3699
+ ___block_literal_global.3704
+ ___block_literal_global.3708
+ ___block_literal_global.3711
+ ___block_literal_global.3714
+ ___block_literal_global.3718
+ ___block_literal_global.3721
+ ___block_literal_global.3725
+ ___block_literal_global.3728
+ ___block_literal_global.3731
+ ___block_literal_global.3735
+ ___block_literal_global.3739
+ ___block_literal_global.3840
+ ___block_literal_global.602
+ ___block_literal_global.667
+ _objc_msgSend$_runDataAndPrivacy
+ _objc_msgSend$dataAndPrivacyAgreed
+ _objc_msgSend$isCompactVoiceTriggerAvailableForLanguageCode:forPhraseDeviceType:
+ _objc_msgSend$setPromptForDataAndPrivacyHandler:
+ _objc_msgSend$setPromptToShareSettingsHandler:
+ _objc_msgSend$stringForKey:
- -[HDSSetupSession _runPreflightJSCheck].cold.1
- -[HDSSetupSession _runPreflightJSCheck].cold.2
- -[HDSSetupSession _runPreflightJSCheck].cold.3
- -[HDSSetupSession promptToShareSettingsV2Handler]
- -[HDSSetupSession setPromptToShareSettingsV2Handler:]
- GCC_except_table12
- GCC_except_table309
- GCC_except_table368
- GCC_except_table419
- _OBJC_IVAR_$_HDSSetupSession._promptToShareSettingsV2Handler
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1667
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1667.cold.1
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.661
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.661.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.683
- ___39-[HDSSetupSession _runPreflightJSCheck]_block_invoke
- ___39-[HDSSetupSession _runPreflightJSCheck]_block_invoke_2
- ___39-[HDSSetupSession _runPreflightJSCheck]_block_invoke_2.cold.1
- ___42-[HDSSetupService activateWithCompletion:]_block_invoke.cold.1
- ___42-[HDSSetupService activateWithCompletion:]_block_invoke_3
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1814
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1815
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1815.cold.1
- ___block_literal_global.1669
- ___block_literal_global.3572
- ___block_literal_global.3576
- ___block_literal_global.3580
- ___block_literal_global.3583
- ___block_literal_global.3586
- ___block_literal_global.3594
- ___block_literal_global.3598
- ___block_literal_global.3612
- ___block_literal_global.3616
- ___block_literal_global.3630
- ___block_literal_global.3633
- ___block_literal_global.3636
- ___block_literal_global.3640
- ___block_literal_global.3644
- ___block_literal_global.3662
- ___block_literal_global.3674
- ___block_literal_global.3678
- ___block_literal_global.3681
- ___block_literal_global.3684
- ___block_literal_global.3688
- ___block_literal_global.3693
- ___block_literal_global.3697
- ___block_literal_global.3702
- ___block_literal_global.3706
- ___block_literal_global.3709
- ___block_literal_global.3712
- ___block_literal_global.3716
- ___block_literal_global.3719
- ___block_literal_global.3723
- ___block_literal_global.3726
- ___block_literal_global.3729
- ___block_literal_global.3733
- ___block_literal_global.3737
- ___block_literal_global.3838
- ___block_literal_global.601
- ___block_literal_global.666
- _objc_msgSend$setPromptToShareSettingsV2Handler:
CStrings:
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_21"
+ "-[HDSSetupService activateWithCompletion:]"
+ "-[HDSSetupSession _runDataAndPrivacy]"
+ "-[HDSSetupSession dataAndPrivacyAgreed]_block_invoke"
+ "CLISetupInteractor: promptForDataAndPrivacyHandler\n"
+ "CLISetupInteractor: promptToShareSettingsHandler\n"
+ "CmdHomeDeviceSetupNoUI promptForDataAndPrivacyHandler\n"
+ "CmdHomeDeviceSetupNoUI promptToShareSettingsHandler\n"
+ "DataAndPrivacy"
+ "DataAndPrivacy prompting user\n"
+ "DataAndPrivacy skipping check with no prompt handler\n"
+ "DataAndPrivacy user agreed\n"
+ "DataAndPrivacy user hasn't agreed yet\n"
+ "DataAndPrivacyPrompt"
+ "T@?,C,N,V_promptForDataAndPrivacyHandler"
+ "User agree to Data and Privacy\n"
+ "_dataPrivacyAgreed"
+ "_dataPrivacyState"
+ "_promptForDataAndPrivacyHandler"
+ "_runDataAndPrivacy"
+ "carry"
+ "dataAndPrivacyAgreed"
+ "isCompactVoiceTriggerAvailableForLanguageCode:forPhraseDeviceType:"
+ "oseligibility_eu"
+ "promptForDataAndPrivacyHandler"
+ "setPromptForDataAndPrivacyHandler:"
+ "stringForKey:"
+ "sysdrop_carry"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
- "-[HDSSetupService activateWithCompletion:]_block_invoke"
- "-[HDSSetupSession _runPreflightJSCheck]_block_invoke_2"
- "CLISetupInteractor: promptToShareSettingsV2Handler\n"
- "CmdHomeDeviceSetupNoUI promptToShareSettingsV2Handler\n"
- "T@?,C,N,V_promptToShareSettingsV2Handler"
- "_promptToShareSettingsV2Handler"
- "_runPreflightJSCheck called with request %@\n"
- "_runPreflightJSCheck in progress\n"
- "_runPreflightJSCheck succeeded\n"
- "oseligability_eu"
- "promptToShareSettingsV2Handler"
- "setPromptToShareSettingsV2Handler:"
- "sysdrop_external"
- "walkabout"

```

## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-277.50.15.0.0
-  __TEXT.__text: 0x65b14
+277.60.4.0.0
+  __TEXT.__text: 0x66870
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x2d84
-  __TEXT.__const: 0x3a2
-  __TEXT.__cstring: 0x18624
+  __TEXT.__objc_methlist: 0x2dcc
+  __TEXT.__const: 0x422
+  __TEXT.__cstring: 0x18874
   __TEXT.__oslogstring: 0x57d
   __TEXT.__gcc_except_tab: 0x154
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x1530
+  __TEXT.__unwind_info: 0x1558
   __TEXT.__eh_frame: 0x490
   __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methname: 0xbb36
+  __TEXT.__objc_methname: 0xbc07
   __TEXT.__objc_methtype: 0x111e
-  __TEXT.__objc_stubs: 0x7340
+  __TEXT.__objc_stubs: 0x7380
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x14c8
+  __DATA_CONST.__const: 0x14d0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2800
+  __DATA_CONST.__objc_selrefs: 0x2828
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0x848
-  __AUTH_CONST.__cfstring: 0x4d80
-  __AUTH_CONST.__objc_const: 0x6a40
+  __AUTH_CONST.__const: 0xa28
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0x6ab8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x94c
-  __DATA.__data: 0xac0
+  __DATA.__objc_ivar: 0x958
+  __DATA.__data: 0xa40
   __DATA.__common: 0x40
-  __DATA.__bss: 0x690
+  __DATA.__bss: 0x700
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1D00AE9F-EBE2-314A-87EB-ED31AD40DC76
-  Functions: 2580
-  Symbols:   7646
-  CStrings:  5650
+  UUID: 22BCA470-5263-3A1B-9EC7-C1DB4A942A8F
+  Functions: 2624
+  Symbols:   7765
+  CStrings:  5680
 
Symbols:
+ +[HDSDefaults forceHH2Upsell]
+ -[HDSSetupSession _runHH2Upsell]
+ -[HDSSetupSession _runHH2Upsell].cold.1
+ -[HDSSetupSession _runPreAuthResponse:error:].cold.10
+ -[HDSSetupSession promptForHH2UpsellHandler]
+ -[HDSSetupSession setPromptForHH2UpsellHandler:]
+ GCC_except_table279
+ GCC_except_table337
+ _OBJC_IVAR_$_HDSSetupSession._hh2UpsellState
+ _OBJC_IVAR_$_HDSSetupSession._promptForHH2UpsellHandler
+ _OBJC_IVAR_$_HDSSetupSession._upsellHH2
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.1
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.2
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.3
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1562
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1562.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.656
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3.cold.2
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16.cold.1
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1709
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1710
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1710.cold.1
+ ___block_literal_global.1564
+ ___block_literal_global.3293
+ ___block_literal_global.3297
+ ___block_literal_global.3300
+ ___block_literal_global.3303
+ ___block_literal_global.3311
+ ___block_literal_global.3315
+ ___block_literal_global.3346
+ ___block_literal_global.3349
+ ___block_literal_global.3352
+ ___block_literal_global.3356
+ ___block_literal_global.3360
+ ___block_literal_global.3389
+ ___block_literal_global.3393
+ ___block_literal_global.3396
+ ___block_literal_global.3399
+ ___block_literal_global.3403
+ ___block_literal_global.3408
+ ___block_literal_global.3412
+ ___block_literal_global.3417
+ ___block_literal_global.3421
+ ___block_literal_global.3424
+ ___block_literal_global.3427
+ ___block_literal_global.3431
+ ___block_literal_global.3434
+ ___block_literal_global.3438
+ ___block_literal_global.3441
+ ___block_literal_global.3444
+ ___block_literal_global.3448
+ ___block_literal_global.3452
+ ___block_literal_global.3553
+ ___block_literal_global.892
+ ___block_literal_global.896
+ ___block_literal_global.903
+ ___block_literal_global.909
+ ___block_literal_global.912
+ ___block_literal_global.916
+ ___initValAVAudioSessionCategoryAmbient_block_invoke
+ ___initValAVAudioSessionCategoryAmbient_block_invoke.cold.1
+ ___initValAVAudioSessionInterruptionNotification_block_invoke
+ ___initValAVAudioSessionInterruptionNotification_block_invoke.cold.1
+ ___initValAVAudioSessionModeDefault_block_invoke
+ ___initValAVAudioSessionModeDefault_block_invoke.cold.1
+ ___initValHMAccessoryCategoryTypeAppleTV_block_invoke
+ ___initValHMAccessoryCategoryTypeAppleTV_block_invoke.cold.1
+ ___initValHMAccessoryCategoryTypeHomePod_block_invoke
+ ___initValHMAccessoryCategoryTypeHomePod_block_invoke.cold.1
+ ___initValTRActivationOperationErrorKey_block_invoke
+ ___initValTRActivationOperationErrorKey_block_invoke.cold.1
+ ___initValTRActivationOperationIsActivatedKey_block_invoke
+ ___initValTRActivationOperationIsActivatedKey_block_invoke.cold.1
+ ___initValTRAuthenticationOperationErrorKey_block_invoke
+ ___initValTRAuthenticationOperationErrorKey_block_invoke.cold.1
+ ___initValTRAuthenticationOperationUnauthenticatedServicesKey_block_invoke
+ ___initValTRAuthenticationOperationUnauthenticatedServicesKey_block_invoke.cold.1
+ ___initValTROperationErrorDomain_block_invoke
+ ___initValTROperationErrorDomain_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationNeedsNetworkKey_block_invoke
+ ___initValTRSetupConfigurationOperationNeedsNetworkKey_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationUnauthenticatedServicesKey_block_invoke
+ ___initValTRSetupConfigurationOperationUnauthenticatedServicesKey_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationUseAIDAKey_block_invoke
+ ___initValTRSetupConfigurationOperationUseAIDAKey_block_invoke.cold.1
+ ___initValkAccountDataclassHome_block_invoke
+ ___initValkAccountDataclassHome_block_invoke.cold.1
+ _kDefaultsKey_ForceHH2
+ _objc_msgSend$_runHH2Upsell
+ _objc_msgSend$forceHH2Upsell
+ _objc_msgSend$setPromptForHH2UpsellHandler:
+ _softLinkOnceAVAudioSessionCategoryAmbient
+ _softLinkOnceAVAudioSessionInterruptionNotification
+ _softLinkOnceAVAudioSessionModeDefault
+ _softLinkOnceHMAccessoryCategoryTypeAppleTV
+ _softLinkOnceHMAccessoryCategoryTypeHomePod
+ _softLinkOnceTRActivationOperationErrorKey
+ _softLinkOnceTRActivationOperationIsActivatedKey
+ _softLinkOnceTRAuthenticationOperationErrorKey
+ _softLinkOnceTRAuthenticationOperationUnauthenticatedServicesKey
+ _softLinkOnceTROperationErrorDomain
+ _softLinkOnceTRSetupConfigurationOperationNeedsNetworkKey
+ _softLinkOnceTRSetupConfigurationOperationUnauthenticatedServicesKey
+ _softLinkOnceTRSetupConfigurationOperationUseAIDAKey
+ _softLinkOncekAccountDataclassHome
- GCC_except_table274
- GCC_except_table332
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1547
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1547.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke.cold.2
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.cold.2
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1694
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1695
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1695.cold.1
- ___block_literal_global.1549
- ___block_literal_global.3270
- ___block_literal_global.3274
- ___block_literal_global.3278
- ___block_literal_global.3286
- ___block_literal_global.3290
- ___block_literal_global.3304
- ___block_literal_global.3308
- ___block_literal_global.3321
- ___block_literal_global.3325
- ___block_literal_global.3350
- ___block_literal_global.3362
- ___block_literal_global.3366
- ___block_literal_global.3372
- ___block_literal_global.3381
- ___block_literal_global.3386
- ___block_literal_global.3401
- ___block_literal_global.3405
- ___block_literal_global.3506
- ___block_literal_global.891
- ___block_literal_global.895
- ___block_literal_global.902
- ___block_literal_global.911
- _objc_msgSend$sysDropEnabled
CStrings:
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16"
+ "-[HDSSetupSession _runHH2Upsell]"
+ "-[HDSSetupSession _runHH2Upsell]_block_invoke"
+ "-[HDSSetupSession _runHH2Upsell]_block_invoke_2"
+ "-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3"
+ "CLISetupInteractor: promptForHH2UpsellHandler\n"
+ "HH2 Upsell Start\n"
+ "HH2Upsell"
+ "HomePod needsHH2: %s | %#m\n"
+ "T@?,C,N,V_promptForHH2UpsellHandler"
+ "You cannot setup a 19.0 HomePod while in HH1\n"
+ "_hh2UpsellState"
+ "_promptForHH2UpsellHandler"
+ "_runHH2Upsell"
+ "_runHH2Upsell: fetchSetupModeWithCompletion returned error: %{error}\n"
+ "_runHH2Upsell: mode %lu | upsell %s\n"
+ "_runHH2Upsell: prompting upsell, Account is in HH1\n"
+ "_runHH2Upsell: skipping\n"
+ "_upsellHH2"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "forceHH2"
+ "forceHH2Upsell"
+ "hds_n_h2"
+ "promptForHH2UpsellHandler"
+ "setPromptForHH2UpsellHandler:"
+ "sysdrop_carry"
- "sysdrop_external"

```

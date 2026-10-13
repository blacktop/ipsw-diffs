## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-405.10.34.1.1
-  __TEXT.__text: 0x71258
-  __TEXT.__objc_methlist: 0x3494
-  __TEXT.__const: 0x488
-  __TEXT.__cstring: 0x1aac4
-  __TEXT.__oslogstring: 0x81d
+405.10.36.0.0
+  __TEXT.__text: 0x71cdc
+  __TEXT.__objc_methlist: 0x3514
+  __TEXT.__const: 0x478
+  __TEXT.__cstring: 0x1ad64
+  __TEXT.__oslogstring: 0x82d
   __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xd3

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x25a8
+  __TEXT.__unwind_info: 0x25d0
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19d8
+  __DATA_CONST.__const: 0x19e8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e10
+  __DATA_CONST.__objc_selrefs: 0x2e70
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x420
   __AUTH_CONST.__const: 0xc58
-  __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0x78a8
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x79b0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x850
   __AUTH.__objc_data: 0x778
   __AUTH.__data: 0x328
-  __DATA.__objc_ivar: 0xa4c
+  __DATA.__objc_ivar: 0xa64
   __DATA.__data: 0xb78
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3080
-  Symbols:   3348
-  CStrings:  3127
+  Functions: 3098
+  Symbols:   3367
+  CStrings:  3149
 
Symbols:
+ +[HDSDefaults forceTopCapBigAsset]
+ +[HDSDefaults forceTopCapNight]
+ +[HDSHPCommon productSupportsLightShow]
+ -[HDSSetupService lightShowOptedIn]
+ -[HDSSetupSession _runLightShowUserInput]
+ -[HDSSetupSession lightShowOptedIn:]
+ -[HDSSetupSession promptForLightShowOptInHandler]
+ -[HDSSetupSession setPromptForLightShowOptInHandler:]
+ GCC_except_table314
+ GCC_except_table377
+ GCC_except_table382
+ GCC_except_table432
+ _OBJC_IVAR_$_CLISetupInteractor._lightShowOptedIn
+ _OBJC_IVAR_$_HDSSetupService._lightShowOptedIn
+ _OBJC_IVAR_$_HDSSetupSession._isLightShowCapable
+ _OBJC_IVAR_$_HDSSetupSession._lightShowSelection
+ _OBJC_IVAR_$_HDSSetupSession._lightShowUserInputState
+ _OBJC_IVAR_$_HDSSetupSession._promptForLightShowOptInHandler
+ _OUTLINED_FUNCTION_80
+ ___36-[HDSSetupSession lightShowOptedIn:]_block_invoke
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_22
+ _kDefaultsKey_ForceTopCapBigAsset
+ _kDefaultsKey_ForceTopCapNight
- GCC_except_table311
- GCC_except_table374
- GCC_except_table379
- GCC_except_table429
CStrings:
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_22"
+ "-[HDSSetupSession _runLightShowUserInput]"
+ "-[HDSSetupSession lightShowOptedIn:]_block_invoke"
+ "AudioAccessory11,1"
+ "CLISetupInteractor: promptForLightShowHandler\n"
+ "CmdHomeDeviceSetupNoUI promptForLightShowHandler %s\n"
+ "HomePod Light Show capable: %s | %#m\n"
+ "Light Show capable: %s\n"
+ "Light Show user selection = %s\n"
+ "LightShow"
+ "LightShow Complete, user choice: %s\n"
+ "LightShowUserInput"
+ "LightShowUserInput asking user to opt in\n"
+ "LightShowUserInput skipping with no prompt handler\n"
+ "LightShowUserInput start\n"
+ "forceTopCapBigAsset"
+ "forceTopCapNight"
+ "lightShow"
+ "lightShowState"
+ "ls_ca"
+ "ls_oi"
+ "setSetupUserInputConfig Light Show opted in set to cli arg %s\n"
```

## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-  __TEXT.__text: 0x73114
-  __TEXT.__objc_methlist: 0x3474
+  __TEXT.__text: 0x726a4
+  __TEXT.__objc_methlist: 0x342c
   __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x1ad54
-  __TEXT.__oslogstring: 0x82d
+  __TEXT.__cstring: 0x1aa54
+  __TEXT.__oslogstring: 0x81d
   __TEXT.__gcc_except_tab: 0x294
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xcb

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x1870
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1980
+  __DATA_CONST.__const: 0x1978
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dc8
+  __DATA_CONST.__objc_selrefs: 0x2d98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
   __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0xc38
-  __AUTH_CONST.__cfstring: 0x5640
-  __AUTH_CONST.__objc_const: 0x78c0
+  __AUTH_CONST.__cfstring: 0x5580
+  __AUTH_CONST.__objc_const: 0x77d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x840
   __AUTH.__objc_data: 0x728
-  __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0xa64
+  __AUTH.__data: 0x328
+  __DATA.__objc_ivar: 0xa48
   __DATA.__data: 0xb70
   __DATA.__common: 0x40
   __DATA.__bss: 0x7d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3092
-  Symbols:   9033
-  CStrings:  3853
+  Functions: 3075
+  Symbols:   8980
+  CStrings:  3825
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table310
+ GCC_except_table369
+ GCC_except_table421
- +[HDSDefaults forceSiriV2]
- -[HDSSetupSession _runSiriV2UserInput]
- -[HDSSetupSession _shouldShowPersonalRequestsForSiriV2]
- -[HDSSetupSession promptForSiriV2OptInHandler]
- -[HDSSetupSession setPromptForSiriV2OptInHandler:]
- -[HDSSetupSession siriV2OptedIn:]
- GCC_except_table313
- GCC_except_table373
- GCC_except_table425
- _OBJC_IVAR_$_CLISetupInteractor._siriV2OptedIn
- _OBJC_IVAR_$_HDSSetupSession._companionSiriV2Capable
- _OBJC_IVAR_$_HDSSetupSession._companionSiriV2Enabled
- _OBJC_IVAR_$_HDSSetupSession._isSiriV2Capable
- _OBJC_IVAR_$_HDSSetupSession._promptForSiriV2OptInHandler
- _OBJC_IVAR_$_HDSSetupSession._siriV2Selection
- _OBJC_IVAR_$_HDSSetupSession._siriV2UserInputState
- _OUTLINED_FUNCTION_80
- _OUTLINED_FUNCTION_81
- ___33-[HDSSetupSession siriV2OptedIn:]_block_invoke
- ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_22
- _initAFIsLinwoodCapableIgnoringUserSetting
- _initAFIsLinwoodEnabledAndAvailable
- _kDefaultsKey_ForceSiriV2
- _objc_msgSend$_runSiriV2UserInput
- _objc_msgSend$_shouldShowPersonalRequestsForSiriV2
- _objc_msgSend$forceSiriV2
- _objc_msgSend$setPromptForSiriV2OptInHandler:
- _objc_msgSend$siriV2OptedIn:
- _softLinkAFIsLinwoodCapableIgnoringUserSetting
- _softLinkAFIsLinwoodEnabledAndAvailable
CStrings:
- "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_22"
- "-[HDSSetupSession _runSiriV2UserInput]"
- "-[HDSSetupSession _shouldShowPersonalRequestsForSiriV2]"
- "AFIsLinwoodCapableIgnoringUserSetting"
- "AFIsLinwoodEnabledAndAvailable"
- "CLISetupInteractor: promptForSiriV2Handler\n"
- "CmdHomeDeviceSetupNoUI promptForSiriV2Handler %s\n"
- "Companion SiriV2 capable: %s, enabled: %s\n"
- "HomePod SiriV2 capable: %s | %#m\n"
- "PersonalRequests SiriV2 gating: companionCapable=%s companionEnabled=%s homePodCapable=%s siriV2Selection=%d result=%s\n"
- "SiriV2"
- "SiriV2 Complete, user choice: %s\n"
- "SiriV2UserInput"
- "SiriV2UserInput asking user to opt in\n"
- "SiriV2UserInput skipping with no prompt handler\n"
- "SiriV2UserInput start\n"
- "forceSiriV2"
- "setSetupUserInputConfig SiriV2 opted in set to cli arg %s\n"
- "siriV2"
- "siriv2"
- "sv2_ca"
- "sv2_oi"

```

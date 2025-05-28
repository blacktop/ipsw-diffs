## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-255.100.5.0.0
-  __TEXT.__text: 0x94514
+255.120.2.0.0
+  __TEXT.__text: 0x94ae8
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x2234
-  __TEXT.__cstring: 0x512a
-  __TEXT.__oslogstring: 0xb8ab
+  __TEXT.__cstring: 0x517d
+  __TEXT.__oslogstring: 0xb932
   __TEXT.__gcc_except_tab: 0xa9c
   __TEXT.__const: 0x60
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__unwind_info: 0x8d4
   __TEXT.__eh_frame: 0x23c
   __TEXT.__objc_classname: 0x499
-  __TEXT.__objc_methname: 0x90a0
+  __TEXT.__objc_methname: 0x90bc
   __TEXT.__objc_methtype: 0x2197
   __TEXT.__objc_stubs: 0x6e60
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x4438
+  __DATA_CONST.__const: 0x4460
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1074
-  Symbols:   5564
-  CStrings:  2423
+  Functions: 1077
+  Symbols:   5571
+  CStrings:  2427
 
Symbols:
+ -[SUSUISoftwareUpdateController(BetaUpdates) setBetaProgramFromUI:forSpecifier:withCompletion:]
+ -[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]
+ GCC_except_table21
+ GCC_except_table27
+ ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.354
+ ___71-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]_block_invoke
+ ___71-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]_block_invoke.724
+ ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.317
+ ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke.318
+ ___78-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$enrollInBetaUpdatesForProgram:completion:
+ _objc_msgSend$setBetaProgramFromUI:forSpecifier:withCompletion:
- -[SUSUISoftwareUpdateController(BetaUpdates) setBetaProgramFromUI:forSpecifier:]
- -[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]
- GCC_except_table18
- GCC_except_table24
- ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke
- ___60-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke.724
- ___68-[SUSUISoftwareUpdateBetaUpdatesController presentAuthKitController]_block_invoke.352
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- _objc_msgSend$enrollInBetaUpdatesForProgram:
- _objc_msgSend$setBetaProgramFromUI:forSpecifier:
CStrings:
+ "%s: Failed to enroll device in seeding"
+ "%s: Finished to enroll device in seeding"
+ "%s: No programs to enroll in, aborting"
+ "%s: enrollInBetaUpdates feature is not enabled"
+ "-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]"
+ "-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:completion:]_block_invoke"
+ "enrollInBetaUpdatesForProgram:completion:"
+ "setBetaProgramFromUI completion finished"
+ "setBetaProgramFromUI:forSpecifier:withCompletion:"
- "-[SUSUISoftwareUpdateManager enrollInBetaUpdatesForProgram:]_block_invoke"
- "Failed to enroll device in seeding."
- "No programs to enroll in, aborting."
- "enrollInBetaUpdatesForProgram:"
- "setBetaProgramFromUI:forSpecifier:"

```

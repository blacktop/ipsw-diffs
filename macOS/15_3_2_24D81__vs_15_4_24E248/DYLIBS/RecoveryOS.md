## RecoveryOS

> `/System/Library/PrivateFrameworks/RecoveryOS.framework/Versions/A/RecoveryOS`

```diff

-738.0.0.0.0
-  __TEXT.__text: 0x4fc4
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x2d0
+743.0.0.0.0
+  __TEXT.__text: 0x54cc
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x4ec
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__cstring: 0x5c6
+  __TEXT.__gcc_except_tab: 0x350
+  __TEXT.__cstring: 0x697
   __TEXT.__oslogstring: 0x24e
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methname: 0xd3d
-  __TEXT.__objc_methtype: 0x3de
-  __TEXT.__objc_stubs: 0x860
+  __TEXT.__objc_methname: 0xdf6
+  __TEXT.__objc_methtype: 0x41b
+  __TEXT.__objc_stubs: 0x8a0
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x20
+  __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x310
+  __DATA_CONST.__objc_selrefs: 0x3c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x290
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__const: 0x2b0
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x9f0
+  __AUTH_CONST.__objc_const: 0x690
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x160

   - /usr/lib/libRosetta.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17898DBA-068B-3B69-A0E7-37B4FFD37A49
-  Functions: 128
-  Symbols:   422
-  CStrings:  271
+  UUID: 1E2FF893-AC0A-357B-892E-64C2E7B14938
+  Functions: 137
+  Symbols:   442
+  CStrings:  288
 
Symbols:
+ +[ROSAgent sharedManager].cold.1
+ +[ROSEnvironment softwareUpdateEnvironment]
+ +[ROSLockoutController LogObject].cold.1
+ -[ROSAgent setUserAuthenticatedInRecovery:error:]
+ -[ROSAgent userAuthenticatedInRecovery]
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table43
+ ROS_LOG.cold.2
+ __33-[ROSAgent runAquaSpecificTasks:]_block_invoke.71
+ __34-[ROSAgent launchLanguageChooser:]_block_invoke.102
+ __96-[ROSAgent launchExecutableAtPath:withArguments:waitUntilExit:synchronouslyWait:withCompletion:]_block_invoke.75
+ ___39-[ROSAgent userAuthenticatedInRecovery]_block_invoke
+ ___39-[ROSAgent userAuthenticatedInRecovery]_block_invoke_2
+ ___49-[ROSAgent setUserAuthenticatedInRecovery:error:]_block_invoke
+ ___49-[ROSAgent setUserAuthenticatedInRecovery:error:]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ __block_literal_global.105
+ __block_literal_global.67
+ _access
+ _asprintf
+ _objc_msgSend$setUserAuthenticatedInRecovery:completion:
+ _objc_msgSend$userAuthenticatedInRecoveryWithCompletion:
+ _os_parse_boot_arg_from_buffer_string
+ _sysctlbyname_get_data_np
- GCC_except_table29
- _OUTLINED_FUNCTION_3
- __33-[ROSAgent runAquaSpecificTasks:]_block_invoke.66
- __34-[ROSAgent launchLanguageChooser:]_block_invoke.97
- __96-[ROSAgent launchExecutableAtPath:withArguments:waitUntilExit:synchronouslyWait:withCompletion:]_block_invoke.70
- __block_literal_global.62
CStrings:
+ "-post-upgrade"
+ "/System/Volumes/Preboot/%s/%s"
+ "B28@0:8B16^@20"
+ "Failed to invoke userAuthenticatedInRecovery with error:%s"
+ "TB,R,N"
+ "com.apple.RecoveryOS"
+ "kern.apfsprebootuuid"
+ "kern.bootargs"
+ "kern.bootuuid"
+ "setUserAuthenticatedInRecovery:completion:"
+ "setUserAuthenticatedInRecovery:error:"
+ "softwareUpdateEnvironment"
+ "userAuthenticatedInRecovery"
+ "userAuthenticatedInRecoveryWithCompletion:"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "var/db/.com.apple.templatemigration"

```

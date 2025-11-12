## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.250.1.0.0
-  __TEXT.__text: 0x86998
+416.250.2.0.0
+  __TEXT.__text: 0x86da8
   __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x510c
+  __TEXT.__objc_methlist: 0x511c
   __TEXT.__const: 0x7d0
-  __TEXT.__oslogstring: 0x1230e
-  __TEXT.__cstring: 0xd295
+  __TEXT.__oslogstring: 0x123ee
+  __TEXT.__cstring: 0xd2b5
   __TEXT.__gcc_except_tab: 0xa00
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x37f

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__unwind_info: 0x1b50
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xe732
+  __TEXT.__objc_methname: 0xe779
   __TEXT.__objc_methtype: 0x260b
-  __TEXT.__objc_stubs: 0xba60
+  __TEXT.__objc_stubs: 0xbac0
   __DATA_CONST.__got: 0xfe8
-  __DATA_CONST.__const: 0x2138
+  __DATA_CONST.__const: 0x2140
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_selrefs: 0x3538
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__auth_got: 0x8e8
   __AUTH_CONST.__const: 0xab0
   __AUTH_CONST.__cfstring: 0x8680
-  __AUTH_CONST.__objc_const: 0xf870
+  __AUTH_CONST.__objc_const: 0xf890
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x1020
-  __AUTH.__data: 0x50
+  __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x1200
+  __DATA.__data: 0x1210
   __DATA.__bss: 0x470
   __DATA_DIRTY.__objc_data: 0xa60
   __DATA_DIRTY.__data: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D209BB62-8363-3721-B74E-4EA3AAF438FE
-  Functions: 2866
-  Symbols:   9336
-  CStrings:  6104
+  UUID: 2D7AA5E0-04C7-32F9-9688-986E02513199
+  Functions: 2869
+  Symbols:   9346
+  CStrings:  6111
 
Symbols:
+ -[CDPDStateMachine _shouldEnableSecureBackupWithCompletion:]
+ GCC_except_table107
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.157
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.158
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.160
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.106
+ ___60-[CDPDStateMachine _shouldEnableSecureBackupWithCompletion:]_block_invoke
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.104
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.104.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.169
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.169.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.170
+ ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.143
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.165
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.165.cold.1
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.165.cold.2
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.166
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.127
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.128
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.144.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.146
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_literal_global.137
+ _objc_msgSend$_shouldEnableSecureBackupWithCompletion:
+ _objc_msgSend$isSingleICSC
+ _objc_msgSend$setIsSingleICSC:
- GCC_except_table104
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.154
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.155
- ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.158
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.104
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.cold.1
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.166
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.167
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.167.cold.1
- ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.141
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.163
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.163.cold.1
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.163.cold.2
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.164
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.125
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.126
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.142
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.142.cold.1
- ___block_literal_global.135
CStrings:
+ "Attempting to enable secure backup..."
+ "Ledger: No probation applied to singleICSC users"
+ "We determined healthy record for Password Change context type, skipping secure backup enable"
+ "_shouldEnableSecureBackupWithCompletion:"
+ "isSingleICSC"
+ "isSingleICSCUser"
+ "setIsSingleICSC:"
+ "shouldPerformRepair indicates repair needed, no viable escrow record found"
- "Always attempting to enable secure backup..."

```

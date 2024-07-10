## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0x7e1f0
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x3d18
+378.1.0.0.0
+  __TEXT.__text: 0x7d888
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_methlist: 0x3cf0
   __TEXT.__const: 0x4ae
-  __TEXT.__oslogstring: 0x1061a
-  __TEXT.__cstring: 0x56da
+  __TEXT.__oslogstring: 0x104ca
+  __TEXT.__cstring: 0x565a
   __TEXT.__gcc_except_tab: 0x768
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x12c
   __TEXT.__swift5_typeref: 0x26e
+  __TEXT.__constg_swiftt: 0x12c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x63
   __TEXT.__swift5_fieldmd: 0x64

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x100
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__unwind_info: 0x17f0
   __TEXT.__eh_frame: 0x710
   __TEXT.__objc_classname: 0xb80
-  __TEXT.__objc_methname: 0xce49
+  __TEXT.__objc_methname: 0xcdd2
   __TEXT.__objc_methtype: 0x23d4
-  __TEXT.__objc_stubs: 0xa7e0
+  __TEXT.__objc_stubs: 0xa760
   __DATA_CONST.__got: 0xe70
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f28
+  __DATA_CONST.__objc_selrefs: 0x2f08
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__auth_ptr: 0x170
-  __AUTH_CONST.__const: 0x20c0
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_ptr: 0x168
+  __AUTH_CONST.__const: 0x2030
   __AUTH_CONST.__cfstring: 0x3d80
-  __AUTH_CONST.__objc_const: 0xfae0
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_const: 0xfac0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x888
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x37c
+  __DATA.__objc_ivar: 0x378
   __DATA.__data: 0xff8
   __DATA.__bss: 0x510
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2556
-  Symbols:   5988
-  CStrings:  680
+  Functions: 2539
+  Symbols:   5960
+  CStrings:  677
 
Symbols:
+ __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.185
+ __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.186
+ __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.187
+ __156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.190
+ __38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.133
+ __42-[CDPDSecureChannelController joinCircle:]_block_invoke.19
+ __42-[CDPDSecureChannelController joinCircle:]_block_invoke.19.cold.1
+ __42-[CDPDSecureChannelController joinCircle:]_block_invoke.19.cold.2
+ __42-[CDPDSecureChannelController joinCircle:]_block_invoke.cold.1
+ __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.120
+ __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.121
+ __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.127
+ __56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.80
+ __56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.cold.1
+ __56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.cold.2
+ __58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.77
+ __65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.128
+ __65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.129
+ __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.104
+ __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.108
+ __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.91
+ __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.91.cold.1
+ __66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.72
+ __66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.73
+ __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.202
+ __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.203
+ __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.203.cold.1
+ __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.204
+ __72-[CDPDLocalSecretController localSecretChangedTo:secretType:completion:]_block_invoke.25
+ __72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.170
+ __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.196
+ __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.196.cold.1
+ __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.200
+ __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.171
+ __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.171.cold.1
+ __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.175
+ __85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.90
- -[CDPDLocalSecretController localSecretChangedTo:secretType:completion:].cold.1
- -[CDPDSecureChannelController _joinCircle:]
- -[CDPDSecureChannelController _joinCircle:].cold.1
- -[CDPDSecureChannelController _startListeningWithProxy:].cold.1
- -[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]
- -[CDPDSecureChannelController enforceQOS:]
- OBJC_IVAR_$_CDPDSecureChannelController._secureChannelProcessingQueue
- __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.174
- __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.175
- __119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.176
- __156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.179
- __38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.122
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.22
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.22.cold.1
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.22.cold.2
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.25
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.25.cold.1
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.26
- __43-[CDPDSecureChannelController _joinCircle:]_block_invoke.cold.1
- __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.108
- __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.110
- __55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.116
- __58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.65
- __65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.117
- __65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.118
- __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.79
- __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.79.cold.1
- __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.80
- __65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.96
- __66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.60
- __66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.61
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.90
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.93
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.93.cold.1
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.94
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.cold.1
- __71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.cold.2
- __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.191
- __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.192
- __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.192.cold.1
- __71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.193
- __72-[CDPDLocalSecretController localSecretChangedTo:secretType:completion:]_block_invoke.27
- __72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.159
- __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.185
- __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.185.cold.1
- __74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.189
- __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.160
- __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.160.cold.1
- __82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.164
- __85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.78
- ___42-[CDPDSecureChannelController enforceQOS:]_block_invoke
- ___43-[CDPDSecureChannelController _joinCircle:]_block_invoke
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e24_v32?0"NSData"8^16^24l
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_64_e8_32s40bs_e5_v8?0l
- _cdp_dispatch_sync_with_qos
- _objc_msgSend$_joinCircle:
- _objc_msgSend$_startListeningWithProxyWithEnforcedQoS:
- _objc_msgSend$enforceQOS:
- _objc_msgSend$numberWithUnsignedInt:
- _qos_class_self
CStrings:
- "-[CDPDLocalSecretController localSecretChangedTo:secretType:completion:]"
- "I"
- "com.apple.cdpd.secureChannelProcessingQueue"

```

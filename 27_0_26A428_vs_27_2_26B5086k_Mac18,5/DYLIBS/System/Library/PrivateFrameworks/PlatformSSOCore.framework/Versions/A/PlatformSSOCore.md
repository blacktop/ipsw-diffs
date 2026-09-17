## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore`

```diff

-643.1.1.0.0
-  __TEXT.__text: 0xfa4e8
-  __TEXT.__objc_methlist: 0x71d0
-  __TEXT.__const: 0x33d8
-  __TEXT.__cstring: 0xf5f7
-  __TEXT.__oslogstring: 0x6293
-  __TEXT.__gcc_except_tab: 0x114c
+643.40.23.0.0
+  __TEXT.__text: 0xfd044
+  __TEXT.__objc_methlist: 0x7240
+  __TEXT.__const: 0x3530
+  __TEXT.__cstring: 0xf7b7
+  __TEXT.__oslogstring: 0x669c
+  __TEXT.__gcc_except_tab: 0x1164
   __TEXT.__dlopen_cstrs: 0x363
-  __TEXT.__swift5_typeref: 0x66e
-  __TEXT.__constg_swiftt: 0xbb8
-  __TEXT.__swift5_reflstr: 0x92a
-  __TEXT.__swift5_fieldmd: 0x9a4
-  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_typeref: 0x694
+  __TEXT.__constg_swiftt: 0xbfc
+  __TEXT.__swift5_reflstr: 0x98a
+  __TEXT.__swift5_fieldmd: 0x9f0
+  __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift_as_cont: 0x118
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x4780
-  __TEXT.__eh_frame: 0x2088
+  __TEXT.__swift5_mpenum: 0x48
+  __TEXT.__unwind_info: 0x47d0
+  __TEXT.__eh_frame: 0x20d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f90
+  __DATA_CONST.__const: 0x1fa8
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3720
+  __DATA_CONST.__objc_selrefs: 0x3768
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xb60
-  __AUTH_CONST.__const: 0x2df8
-  __AUTH_CONST.__cfstring: 0x8b80
-  __AUTH_CONST.__objc_const: 0x17928
-  __AUTH_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__got: 0xb78
+  __AUTH_CONST.__const: 0x2e88
+  __AUTH_CONST.__cfstring: 0x8be0
+  __AUTH_CONST.__objc_const: 0x17978
+  __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1078
+  __AUTH_CONST.__auth_got: 0x1088
   __AUTH.__objc_data: 0x3438
-  __AUTH.__data: 0x928
-  __DATA.__objc_ivar: 0x704
-  __DATA.__data: 0x14e8
+  __AUTH.__data: 0x948
+  __DATA.__objc_ivar: 0x708
+  __DATA.__data: 0x1538
   __DATA.__common: 0x89
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5699
-  Symbols:   8785
-  CStrings:  2646
+  Functions: 5728
+  Symbols:   8821
+  CStrings:  2671
 
Symbols:
+ +[POBaseSystemSupport backoffStateForUser:domains:counters:]
+ +[POBaseSystemSupport dataVolumeDevicePath]
+ +[POCoreConfigurationUtil accountDisplayNameForDeviceConfiguration:loginConfiguration:]
+ +[POCoreConfigurationUtil alwaysUseLoginUIOverride]
+ +[POCoreConfigurationUtil shouldUsePlatformSSOLoginUIForDeviceConfiguration:]
+ -[PODeviceConfiguration alwaysUseLoginUI]
+ -[PODeviceConfiguration requiresPlatformSSOLoginUI]
+ -[PODeviceConfiguration setAlwaysUseLoginUI:]
+ -[PODeviceConfiguration supportsOpenID]
+ -[POKeyBag loadKeybagForUserId:]
+ GCC_except_table11
+ OBJC_IVAR_$_PODeviceConfiguration._alwaysUseLoginUI
+ __32-[POKeyBag loadKeybagForUserId:]_block_invoke
+ ___32-[POKeyBag loadKeybagForUserId:]_block_invoke
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _get_enum_tag_for_layout_string 15PlatformSSOCore10POHintTypeO7ContextO
+ _objc_msgSend$accountDisplayNameForDeviceConfiguration:loginConfiguration:
+ _objc_msgSend$alwaysUseLoginUI
+ _objc_msgSend$alwaysUseLoginUIOverride
+ _objc_msgSend$backoffStateForUser:domains:counters:
+ _objc_msgSend$biometricIsRequired
+ _objc_msgSend$dataVolumeDevicePath
+ _objc_msgSend$loadKeybagForUserId:
+ _objc_msgSend$requiresPlatformSSOLoginUI
+ _objc_msgSend$supportsOpenID
+ _symbolic Si5count_t
+ _symbolic _____ 15PlatformSSOCore37PODefaultBaseSystemAuthenticationFlowC16EmptyResultCause33_E0BB9AAF438611B3E2B311B84B5155B5LLO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ dataVolumeDevicePath.cachedDevicePath
- +[POBaseSystemSupport isUserInBackoff:timeRemaining:]
- ___swift_memcpy16_8
- _objc_msgSend$isUserInBackoff:timeRemaining:
CStrings:
+ " submission failed"
+ "%s IdP display name from the login configuration, the profile sets no AccountDisplayName on %@"
+ "%s Platform SSO login UI: %{public}@, alwaysUseLoginUI:%{public}@ openID:%{public}@ biometricRequired:%{public}@ loginType:%{public}@ on %@"
+ "%s Platform SSO login UI: always, set by local override on %@"
+ "%s no IdP display name in the device or login configuration on %@"
+ "+[POBaseSystemSupport backoffStateForUser:domains:counters:]"
+ "+[POCoreConfigurationUtil accountDisplayNameForDeviceConfiguration:loginConfiguration:]"
+ "+[POCoreConfigurationUtil shouldUsePlatformSSOLoginUIForDeviceConfiguration:]"
+ "-[PODeviceConfiguration supportsOpenID]"
+ "AlwaysUseLoginUI"
+ "Authentication flow: OpenID not configured or missing required values"
+ "Invalid user identifier, cannot read backoff state"
+ "No authenticator result to route"
+ "Unable to get APFS record for %{public}@: %d (%{public}s)"
+ "Unable to resolve data volume for group %{public}@"
+ "User is %{public}s, %u of %u failed attempts, %us remaining (console %u attempts %us, other %u attempts %us)"
+ "User is not enrolled in xART policy, no backoff state"
+ "credentialSubmitted: account has exhausted its unlock attempts"
+ "credentialSubmitted: account is in backoff, %{public}us remaining"
+ "getLoginHints: backoff state unavailable, no lockout hint shown"
+ "in backoff"
+ "no credential was submitted"
+ "not in backoff"
+ "not required"
+ "out of attempts"
+ "required"
+ "resolveResult(%{public}s): nothing to route, %{public}s"
+ "the flow was cancelled"
+ "xART policy is missing, cannot determine backoff state"
+ "xART policy is not enforced, no backoff applies"
- "+[POBaseSystemSupport isUserInBackoff:timeRemaining:]"
- "Unable to get APFS record: %08x"
- "User has to many failed attempts"
- "User is in backoff"
- "User is not in backoff"
```

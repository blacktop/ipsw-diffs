## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/Versions/A/AppSSO`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0x2d224
+417.100.37.0.0
+  __TEXT.__text: 0x2e064
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x1668
+  __TEXT.__objc_methlist: 0x19dc
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x1bd8
-  __TEXT.__cstring: 0x2e25
+  __TEXT.__gcc_except_tab: 0x1dd0
+  __TEXT.__cstring: 0x2e61
   __TEXT.__dlopen_cstrs: 0x6be
-  __TEXT.__oslogstring: 0x4544
-  __TEXT.__unwind_info: 0xd18
-  __TEXT.__objc_classname: 0x3bb
-  __TEXT.__objc_methname: 0x4a51
+  __TEXT.__oslogstring: 0x4615
+  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__objc_classname: 0x3be
+  __TEXT.__objc_methname: 0x4b35
   __TEXT.__objc_methtype: 0xa0a
-  __TEXT.__objc_stubs: 0x3900
+  __TEXT.__objc_stubs: 0x39e0
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a8
+  __DATA_CONST.__objc_selrefs: 0x1180
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0xe20
-  __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x44c8
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x3fa0
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x670
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x640

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A5CE733-69FF-3037-9948-A063BA2D8595
-  Functions: 983
-  Symbols:   2441
-  CStrings:  1632
+  UUID: E72F1B3C-8EA8-3F84-93A4-C484C642C268
+  Functions: 1022
+  Symbols:   2490
+  CStrings:  1654
 
Symbols:
+ +[SOConfigurationHost defaultManager].cold.2
+ +[SOConfigurationManager defaultManager].cold.2
+ +[SODebugHints sharedInstance].cold.1
+ +[SOExtensionManager sharedInstance].cold.1
+ +[SOHostExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[SOHostExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[SORemoteExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[SORemoteExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[SORequestQueue requestQueueWithIdentifier:].cold.1
+ -[SOAuthorization cancelLock]
+ -[SOAuthorization cancelled]
+ -[SOAuthorization setCancelLock:]
+ -[SOAuthorization setCancelled:]
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:].cold.4
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:].cold.5
+ -[SOConfigurationHost platformSSOProfile]
+ -[SOConfigurationHost platformSSOProfile].cold.1
+ -[SOConfigurationHost platformSSOProfile].cold.2
+ -[SOConfigurationHost platformSSOProfile].cold.3
+ -[SOConfigurationHost verifyCacheFileAccess]
+ -[SOConfigurationHost verifyCacheFileAccess].cold.1
+ -[SOConfigurationHost verifyCacheFileAccess].cold.2
+ -[SODebugHints debugHintsWithCompletion:].cold.1
+ -[SORemoteExtensionViewController viewServiceDidTerminateWithError:].cold.1
+ GCC_except_table107
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table26
+ GCC_except_table35
+ GCC_except_table54
+ OBJC_IVAR_$_SOAuthorization._cancelLock
+ OBJC_IVAR_$_SOAuthorization._cancelled
+ SO_LOG_AppSSOClientImpl.cold.1
+ SO_LOG_SOAuthorization.cold.1
+ SO_LOG_SOAuthorizationRequest.cold.1
+ SO_LOG_SOConfigurationHost.cold.1
+ SO_LOG_SOConfigurationManager.cold.1
+ SO_LOG_SOExtension.cold.1
+ SO_LOG_SOExtensionFinder.cold.1
+ SO_LOG_SOExtensionManager.cold.1
+ SO_LOG_SOExtensionServiceConnection.cold.1
+ SO_LOG_SOExtensionViewService.cold.1
+ SO_LOG_SOHostExtensionContext.cold.1
+ SO_LOG_SOPreferences.cold.1
+ SO_LOG_SORemoteExtensionContext.cold.1
+ SO_LOG_SORequestQueue.cold.1
+ __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.33
+ __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.37
+ __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.46
+ __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke_2.47
+ __60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.78
+ __60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.78.cold.1
+ ___block_descriptor_56_e8_32s40s48s_e56_v32?0"NSString"8"NSXPCListenerEndpoint"16"NSError"24l
+ ___block_descriptor_64_e8_32s40s48s56s_e33_v24?0"SOExtension"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56s_e53_v24?0"SORemoteExtensionViewController"8"NSError"16l
+ __block_literal_global.239
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$cancelLock
+ _objc_msgSend$cancelled
+ _objc_msgSend$code
+ _objc_msgSend$intValue
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$setCancelled:
- GCC_except_table101
- GCC_except_table112
- GCC_except_table113
- GCC_except_table28
- GCC_except_table37
- GCC_except_table53
- _OUTLINED_FUNCTION_13
- __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.31
- __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.36
- __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.47
- __52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke_2.48
- __60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.77
- __60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.77.cold.1
- ___block_descriptor_48_e8_32s40s_e56_v32?0"NSString"8"NSXPCListenerEndpoint"16"NSError"24l
- ___block_descriptor_56_e8_32s40s48s_e33_v24?0"SOExtension"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e53_v24?0"SORemoteExtensionViewController"8"NSError"16l
- __block_literal_global.236
CStrings:
+ "-[SOConfigurationHost platformSSOProfile]"
+ "Cache file group mismatch."
+ "Cache file permission mismatch."
+ "NSUnderlyingError"
+ "No Platform SSO profiles found"
+ "Request was cancelled: identifier = %{public}@"
+ "T@\"NSObject\",&,N,V_cancelLock"
+ "TB,N,V_cancelled"
+ "_cancelLock"
+ "_cancelled"
+ "attributesOfItemAtPath:error:"
+ "cancelLock"
+ "cancelled"
+ "code"
+ "failed to change file attributes of path: %{public}@, error: %{public}@"
+ "intValue"
+ "platformSSOProfile"
+ "removeItemAtURL:error:"
+ "setCancelLock:"
+ "setCancelled:"
+ "verifyCacheFileAccess"

```

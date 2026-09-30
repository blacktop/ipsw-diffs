## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-643.40.23.0.0
-  __TEXT.__text: 0x5a3d8
-  __TEXT.__objc_methlist: 0x35bc
+643.40.27.0.0
+  __TEXT.__text: 0x5aeac
+  __TEXT.__objc_methlist: 0x36bc
   __TEXT.__const: 0x322
-  __TEXT.__cstring: 0x82e6
-  __TEXT.__oslogstring: 0x2961
-  __TEXT.__gcc_except_tab: 0x1454
+  __TEXT.__cstring: 0x8376
+  __TEXT.__oslogstring: 0x2a41
+  __TEXT.__gcc_except_tab: 0x1464
   __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_capture: 0x14c

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0x58
-  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__unwind_info: 0x1e60
   __TEXT.__eh_frame: 0x628
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf78
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0xfa0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_selrefs: 0x2460
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x458
   __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x8670
+  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__objc_const: 0x8828
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x760
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x394
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x3a4
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2154
-  Symbols:   3638
-  CStrings:  1053
+  Functions: 2179
+  Symbols:   3671
+  CStrings:  1058
 
Symbols:
+ +[POSoftwareUpdateCredentialPolicy credentialsWanted]
+ +[POSoftwareUpdateCredentialPolicy harvestPassword:forUserId:]
+ -[POAgentAuthenticationProcess keychainAccess]
+ -[POAgentAuthenticationProcess setKeychainAccess:]
+ -[POAgentProcess configurationManagerForUserName:]
+ -[POAgentProcess keychainAccess]
+ -[POAgentProcess setKeychainAccess:]
+ -[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]
+ -[POAgentProcess updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]
+ -[POAuthPluginProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]
+ -[POConfigurationManager keychainAccess]
+ -[POConfigurationManager setKeychainAccess:]
+ -[PODirectoryServices .cxx_destruct]
+ -[PODirectoryServices init]
+ -[PODirectoryServices keychainAccess]
+ -[PODirectoryServices setKeychainAccess:]
+ -[PORegistrationManager setUserAuthPluginProcess:]
+ -[PORegistrationManager storeCredentialContext:]
+ -[PORegistrationManager updatePasswordHint]
+ -[POServiceConnection updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]
+ GCC_except_table101
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table180
+ GCC_except_table31
+ GCC_except_table57
+ GCC_except_table74
+ _OBJC_CLASS_$_POKeychainAccess
+ _OBJC_CLASS_$_POSoftwareUpdateCredentialPolicy
+ _OBJC_IVAR_$_POAgentAuthenticationProcess._keychainAccess
+ _OBJC_IVAR_$_POAgentProcess._keychainAccess
+ _OBJC_IVAR_$_POConfigurationManager._keychainAccess
+ _OBJC_IVAR_$_PODirectoryServices._keychainAccess
+ _OBJC_METACLASS_$_POSoftwareUpdateCredentialPolicy
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_CLASS_METHODS_POSoftwareUpdateCredentialPolicy
+ __OBJC_$_CLASS_PROP_LIST_POSoftwareUpdateCredentialPolicy
+ __OBJC_$_INSTANCE_VARIABLES_PODirectoryServices
+ __OBJC_CLASS_RO_$_POSoftwareUpdateCredentialPolicy
+ __OBJC_METACLASS_RO_$_POSoftwareUpdateCredentialPolicy
+ ___104-[POServiceConnection updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]_block_invoke
+ ___48-[PORegistrationManager storeCredentialContext:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ _objc_msgSend$configurationManagerForUserName:
+ _objc_msgSend$updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:
+ _objc_msgSend$updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:
+ _objc_msgSend$updatePasswordHint
- -[PORegistrationManager storeCredentialAndUpdatePasswordHint]
- GCC_except_table100
- GCC_except_table110
- GCC_except_table115
- GCC_except_table123
- GCC_except_table129
- GCC_except_table178
- GCC_except_table30
- GCC_except_table45
- GCC_except_table73
- GCC_except_table86
- _OBJC_CLASS_$_NSURLRequest
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$setClass:forSelector:argumentIndex:ofReply:
- _objc_msgSend$storeCredentialAndUpdatePasswordHint
CStrings:
+ "\v"
+ "-[POAuthPluginProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]"
+ "Falling back to password-authorized local account password change"
+ "No usable old credential was supplied; using the stashed credential"
+ "Password update fallback result: %{public}@"
+ "The new credential context cannot be externalized"
+ "\xf0\xd1"
- "\n"
- "\xf0\xc1"
```

## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.120.4.0.0
-  __TEXT.__text: 0x5bbf0
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x331c
-  __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x7e96
-  __TEXT.__oslogstring: 0x2271
-  __TEXT.__gcc_except_tab: 0x152c
+635.0.0.0.0
+  __TEXT.__text: 0x59b34
+  __TEXT.__objc_methlist: 0x348c
+  __TEXT.__const: 0x312
+  __TEXT.__cstring: 0x8246
+  __TEXT.__oslogstring: 0x2411
+  __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__dlopen_cstrs: 0x110
-  __TEXT.__swift5_typeref: 0xc2
-  __TEXT.__swift5_capture: 0x118
+  __TEXT.__swift5_typeref: 0xd9
+  __TEXT.__swift5_capture: 0x14c
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1448
-  __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x3e5
-  __TEXT.__objc_methname: 0x9dd4
-  __TEXT.__objc_methtype: 0x1558
-  __TEXT.__objc_stubs: 0x7180
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0xeb0
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__swift_as_cont: 0x58
+  __TEXT.__unwind_info: 0x1548
+  __TEXT.__eh_frame: 0x628
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf38
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2200
+  __DATA_CONST.__objc_selrefs: 0x2330
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH_CONST.__const: 0xc08
-  __AUTH_CONST.__cfstring: 0x3800
-  __AUTH_CONST.__objc_const: 0x83a0
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__got: 0x418
+  __AUTH_CONST.__const: 0xc80
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x8590
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x740
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x368
-  __DATA.__data: 0x620
+  __DATA.__objc_ivar: 0x388
+  __DATA.__data: 0x600
   __DATA.__bss: 0x340
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EC51886C-00AE-377F-94E6-74B9C3CB4FEE
-  Functions: 2064
-  Symbols:   7332
-  CStrings:  3145
+  UUID: 1363933E-095E-3063-AD26-7D6CA2A03726
+  Functions: 2108
+  Symbols:   7536
+  CStrings:  1496
 
Symbols:
+ +[POConfigurationUtil platformSSOEnabledForUsername:options:]
+ -[POAgentAuthenticationProcess requestUserAuthenticationAndChangePassword]
+ -[POAgentAuthenticationProcess requestUserAuthenticationAndChangePassword].cold.1
+ -[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]
+ -[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:].cold.1
+ -[POAgentProcess updateLocalAccountPasswordWithTokenForUser:passwordContext:completion:]
+ -[POAgentProcess updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]
+ -[POAuthPluginProcess updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]
+ -[PODaemonConnection registerExternalAuthenticationForUsername:completion:]
+ -[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]
+ -[POProfile accessKeyReaderIssuerCertificatePersistentRef]
+ -[POProfile accessKeyTerminalIdentityPersistentRef]
+ -[POProfile allowQRCodeAsOfflinePassword]
+ -[POProfile allowWebLoginPasswordSync]
+ -[POProfile initWithProfile:].cold.1
+ -[POProfile setAllowQRCodeAsOfflinePassword:]
+ -[POProfile setAllowWebLoginPasswordSync:]
+ -[POProfile webLoginURLAllowList]
+ -[PORegistrationContext biometricIsRequired]
+ -[PORegistrationContext isNewOpenIDUser]
+ -[PORegistrationContext registrationUIWindow]
+ -[PORegistrationContext setBiometricIsRequired:]
+ -[PORegistrationContext setNewOpenIDUser:]
+ -[PORegistrationManager createOrRepairUserConfigurationWithError:].cold.2
+ -[PORegistrationManager createOrRepairUserConfigurationWithError:].cold.3
+ -[PORegistrationManager handleBindingForNewAccounts]
+ -[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]
+ -[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:].cold.1
+ -[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]
+ -[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:].cold.1
+ -[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:forOpenID:]
+ -[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:callbackResponse:loginContext:completion:]
+ -[POServiceConnection completeTemporaryUserAccountLogin:passwordContext:completion:]
+ -[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:callbackResponse:completion:]
+ -[POServiceConnection performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]
+ -[POServiceConnection retrieveOpenIDAuthorizationRequestForLoginUserName:completion:]
+ -[POServiceConnection updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]
+ -[POServiceConnection verifyOpenIDUser:loginUserName:callbackResponse:passwordContext:completion:]
+ -[POUserRegistrationStatus isChangepasswordButtonEnabled]
+ -[POUserRegistrationStatus setChangePasswordButtonEnabled:]
+ GCC_except_table107
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table173
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table71
+ GCC_except_table87
+ GCC_except_table97
+ _OBJC_CLASS_$_NSURLRequest
+ _OBJC_IVAR_$_POProfile._accessKeyReaderIssuerCertificatePersistentRef
+ _OBJC_IVAR_$_POProfile._accessKeyTerminalIdentityPersistentRef
+ _OBJC_IVAR_$_POProfile._allowQRCodeAsOfflinePassword
+ _OBJC_IVAR_$_POProfile._allowWebLoginPasswordSync
+ _OBJC_IVAR_$_POProfile._webLoginURLAllowList
+ _OBJC_IVAR_$_PORegistrationContext._biometricIsRequired
+ _OBJC_IVAR_$_PORegistrationContext._newOpenIDUser
+ _OBJC_IVAR_$_POUserRegistrationStatus._changePasswordButtonEnabled
+ _POAuthenticationMethodOpenID
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.425
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.425.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.431
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.431.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.435
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.435.cold.1
+ ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.526
+ ___110-[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:callbackResponse:completion:]_block_invoke
+ ___110-[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:callbackResponse:completion:]_block_invoke.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.209
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.209.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.215
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.215.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.221
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.221.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.227
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.227.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.233
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.233.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.239
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.239.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.102
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.102.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.105
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.105.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.106
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.112
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.112.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.115
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.115.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.118
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.118.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.119
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.119.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.122
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.122.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.125
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.125.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.128
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.128.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.129
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.129.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.133
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.133.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.137
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.99
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.99.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.cold.1
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke_2
+ ___122-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke_2.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.141
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.141.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.147
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.147.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.153
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.153.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.159
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.159.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.162
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.cold.1
+ ___126-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke_2
+ ___127-[POServiceConnection performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke
+ ___127-[POServiceConnection performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.cold.1
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.114
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.114.cold.1
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.120
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.120.cold.1
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.126
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.126.cold.1
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.133
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke.cold.1
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke_2
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke_3
+ ___130-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]_block_invoke_4
+ ___147-[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:callbackResponse:loginContext:completion:]_block_invoke
+ ___147-[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:callbackResponse:loginContext:completion:]_block_invoke.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.109
+ ___29-[POProfile initWithProfile:]_block_invoke.109.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.112
+ ___29-[POProfile initWithProfile:]_block_invoke.112.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.99
+ ___29-[POProfile initWithProfile:]_block_invoke.99.cold.1
+ ___40-[POServiceConnection _connectToService]_block_invoke.87
+ ___40-[POServiceConnection _connectToService]_block_invoke.87.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.101
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.101.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.105
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.105.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.109
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.109.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.113
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.113.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.118
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.118.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.122
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.122.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.126
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.126.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.130
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.130.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.134
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.134.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.138
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.138.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.142
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.142.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.146
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.146.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.81
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.81.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.85
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.85.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.89
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.89.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.93
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.93.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.97
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.97.cold.1
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.209
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.209.cold.1
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.215
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.215.cold.1
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.221
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.151
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.151.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.155
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.155.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.159
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.159.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.161
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.161.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.165
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.165.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.169
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.169.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.173
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.173.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.178
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.178.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.182
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.182.cold.1
+ ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.99
+ ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.99.cold.1
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.90
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.90.cold.1
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.90.cold.2
+ ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.90.cold.3
+ ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.112
+ ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.112.cold.1
+ ___52-[POAgentAuthenticationProcess _performStartupSteps]_block_invoke.89
+ ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.108
+ ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.108.cold.1
+ ___52-[PORegistrationManager finishRegistrationWithRetry]_block_invoke.106
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.223
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.223.cold.1
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.229
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.229.cold.1
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.235
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.492
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.492.cold.1
+ ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.130
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.390
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.390.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.398
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.398.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.402
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.402.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.348
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.348.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.351
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.351.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.352
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.352.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.429
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.429.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.433
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.433.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.436
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.436.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.442
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.442.cold.1
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.249
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.249.cold.1
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.255
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.255.cold.1
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.267
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.267.cold.1
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.267.cold.2
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.268
+ ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.268.cold.1
+ ___59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.446
+ ___59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.446.cold.1
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.472
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.472.cold.1
+ ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.138
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.237
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.237.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.243
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.243.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.274
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.274.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.280
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.280.cold.1
+ ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.145
+ ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.76
+ ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.76.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.286
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.286.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.290
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.290.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.294
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.296
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.296.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.300
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.300.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.304
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.304.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.308
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.308.cold.1
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.418
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.418.cold.1
+ ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.66
+ ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.66.cold.1
+ ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.141
+ ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.141.cold.1
+ ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.144
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.297
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.297.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.298
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.298.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.304
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.304.cold.1
+ ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.37
+ ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.37.cold.1
+ ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.47
+ ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.47.cold.1
+ ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.322
+ ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.326
+ ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.326.cold.1
+ ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.330
+ ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.165
+ ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.165.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.363
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.363.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.366
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.366.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.373
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.373.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.379
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.379.cold.1
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.329
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.138.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.142
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.163
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.163.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.176
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.188
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.191
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.192
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.192.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.196
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.196.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.202
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.334
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.334.cold.1
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.340
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.340.cold.1
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.346
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.346.cold.1
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.365
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.365.cold.1
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.371
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.371.cold.1
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.377
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.453
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.453.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.456
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.456.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.457
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.457.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.460
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.460.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.463
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.463.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.467
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.467.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.470
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.470.cold.1
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.458
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.458.cold.1
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.464
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.464.cold.1
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.112
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.112.cold.1
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.118
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.118.cold.1
+ ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.125
+ ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.342
+ ___72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.153
+ ___72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.153.cold.1
+ ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.336
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.177
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.177.cold.1
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.183
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.383
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.383.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.389
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.389.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.393
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.393.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.399
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.399.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.405
+ ___74-[PORegistrationManager requestUserAuthenticationSyncPassword:completion:]_block_invoke
+ ___75-[POAgentAuthenticationProcess doUnlockWithEmptyCredentialContext:atLogin:]_block_invoke_2.cold.1
+ ___75-[PODaemonConnection registerExternalAuthenticationForUsername:completion:]_block_invoke
+ ___75-[PODaemonConnection registerExternalAuthenticationForUsername:completion:]_block_invoke.cold.1
+ ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.73
+ ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.73.cold.1
+ ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke_2.cold.2
+ ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke_2.cold.3
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.498
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.498.cold.1
+ ___80-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:forOpenID:]_block_invoke
+ ___80-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:forOpenID:]_block_invoke.200
+ ___80-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:forOpenID:]_block_invoke.200.cold.1
+ ___80-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:forOpenID:]_block_invoke.cold.1
+ ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.174
+ ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.174.cold.1
+ ___84-[POServiceConnection completeTemporaryUserAccountLogin:passwordContext:completion:]_block_invoke
+ ___84-[POServiceConnection completeTemporaryUserAccountLogin:passwordContext:completion:]_block_invoke.cold.1
+ ___85-[POServiceConnection retrieveOpenIDAuthorizationRequestForLoginUserName:completion:]_block_invoke
+ ___85-[POServiceConnection retrieveOpenIDAuthorizationRequestForLoginUserName:completion:]_block_invoke.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.102
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.102.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.106
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.94
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.94.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.98
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.98.cold.1
+ ___97-[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]_block_invoke
+ ___97-[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]_block_invoke.cold.1
+ ___97-[POServiceConnection updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]_block_invoke
+ ___97-[POServiceConnection updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]_block_invoke.cold.1
+ ___98-[POServiceConnection verifyOpenIDUser:loginUserName:callbackResponse:passwordContext:completion:]_block_invoke
+ ___98-[POServiceConnection verifyOpenIDUser:loginUserName:callbackResponse:passwordContext:completion:]_block_invoke.cold.1
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s104bs_e47_v32?0Q8"POAuthenticationContext"16"NSData"24ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e22_v24?0Q8"LAContext"16l
+ ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e22_v24?0Q8"LAContext"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e22_v24?0Q8"LAContext"16ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.122
+ ___block_literal_global.124
+ ___block_literal_global.131
+ ___block_literal_global.135
+ ___block_literal_global.157
+ ___block_literal_global.167
+ ___block_literal_global.181
+ ___block_literal_global.190
+ ___block_literal_global.207
+ ___block_literal_global.227
+ ___block_literal_global.237
+ ___block_literal_global.272
+ ___block_literal_global.278
+ ___block_literal_global.292
+ ___block_literal_global.296
+ ___block_literal_global.360
+ ___block_literal_global.411
+ ___block_literal_global.497
+ ___block_literal_global.677
+ ___block_literal_global.857
+ ___block_literal_global.861
+ ___block_literal_global.88
+ ___block_literal_global.95
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.117
+ ___swift_closure_destructor.122
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.51
+ ___swift_closure_destructor.51Tm
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.55Tm
+ ___swift_closure_destructor.59
+ ___swift_closure_destructor.63
+ ___swift_closure_destructor.67
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.81
+ ___swift_closure_destructor.85
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.96
+ ___swift_closure_destructorTm
+ __os_feature_enabled_impl
+ __os_log_default
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_PlatformSSO
+ _block_copy_helper.100
+ _block_copy_helper.103
+ _block_copy_helper.106
+ _block_copy_helper.109
+ _block_copy_helper.113
+ _block_copy_helper.12
+ _block_copy_helper.24
+ _block_copy_helper.27
+ _block_copy_helper.42
+ _block_copy_helper.45
+ _block_copy_helper.6
+ _block_copy_helper.9
+ _block_descriptor.102
+ _block_descriptor.105
+ _block_descriptor.108
+ _block_descriptor.11
+ _block_descriptor.111
+ _block_descriptor.115
+ _block_descriptor.14
+ _block_descriptor.26
+ _block_descriptor.29
+ _block_descriptor.44
+ _block_descriptor.47
+ _block_descriptor.8
+ _block_destroy_helper.10
+ _block_destroy_helper.101
+ _block_destroy_helper.104
+ _block_destroy_helper.107
+ _block_destroy_helper.110
+ _block_destroy_helper.114
+ _block_destroy_helper.13
+ _block_destroy_helper.25
+ _block_destroy_helper.28
+ _block_destroy_helper.43
+ _block_destroy_helper.46
+ _block_destroy_helper.7
+ _kSecurityAgentUid
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$allowQRCodeAsOfflinePassword
+ _objc_msgSend$allowWebLoginPasswordSync
+ _objc_msgSend$authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:callbackResponse:loginContext:completion:
+ _objc_msgSend$authorizationURL
+ _objc_msgSend$authorizationURLKeypath
+ _objc_msgSend$biometricIsRequired
+ _objc_msgSend$completeTemporaryUserAccountLogin:passwordContext:completion:
+ _objc_msgSend$createContextForUserCredential
+ _objc_msgSend$createUserAccount:passwordContext:smartCardContext:tokenId:callbackResponse:completion:
+ _objc_msgSend$fallbackFederationType
+ _objc_msgSend$handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:
+ _objc_msgSend$handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isNewOpenIDUser
+ _objc_msgSend$performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:
+ _objc_msgSend$performOpenIDLoginUsingContext:completion:
+ _objc_msgSend$platformSSOEnabledForUsername:options:
+ _objc_msgSend$registerExternalAuthenticationForUsername:completion:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$requestUserAuthenticationAndChangePassword
+ _objc_msgSend$retrieveOpenIDAuthorizationRequestForLoginUserName:completion:
+ _objc_msgSend$setAllowQRCodeAsOfflinePassword:
+ _objc_msgSend$setAllowWebLoginPasswordSync:
+ _objc_msgSend$setBiometricIsRequired:
+ _objc_msgSend$setCallbackResponse:
+ _objc_msgSend$setChangePasswordButtonEnabled:
+ _objc_msgSend$setClass:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setNewOpenIDUser:
+ _objc_msgSend$setWebLoginURLAllowList:
+ _objc_msgSend$updateLocalAccountPasswordWithTokenForUser:passwordContext:completion:
+ _objc_msgSend$updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:
+ _objc_msgSend$updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:
+ _objc_msgSend$userDecryptionKeyHash
+ _objc_msgSend$userUnlockData
+ _objc_msgSend$userUnlockHash
+ _objc_msgSend$verifyOpenIDUser:loginUserName:callbackResponse:passwordContext:completion:
+ _objc_msgSend$webLoginURLAllowList
+ _objc_msgSend$window
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x21
+ _symbolic Sccy______So9LAContextCSgt_____G So13POLoginResultV s5NeverO
- -[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]
- -[PORegistrationManager handleBindingForNewPasswordAccounts]
- -[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]
- -[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:].cold.1
- -[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]
- -[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:].cold.1
- -[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]
- -[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:loginContext:completion:]
- -[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:completion:]
- GCC_except_table102
- GCC_except_table109
- GCC_except_table113
- GCC_except_table117
- GCC_except_table118
- GCC_except_table123
- GCC_except_table126
- GCC_except_table170
- GCC_except_table19
- GCC_except_table283
- GCC_except_table292
- GCC_except_table70
- GCC_except_table85
- GCC_except_table95
- _OBJC_CLASS_$_OS_dispatch_queue
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.412
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.412.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.418
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.418.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.422
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.422.cold.1
- ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.513
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.132
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.132.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.138
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.138.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.144
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.144.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.150
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke_2
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.202
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.202.cold.1
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.208
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.208.cold.1
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.214
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.214.cold.1
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.220
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.220.cold.1
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.226
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.226.cold.1
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.232
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.232.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.111
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.111.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.117
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.117.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.124
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke_2
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke_3
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke_4
- ___130-[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke
- ___130-[POServiceConnection authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.cold.1
- ___29-[POProfile initWithProfile:]_block_invoke.106
- ___29-[POProfile initWithProfile:]_block_invoke.106.cold.1
- ___29-[POProfile initWithProfile:]_block_invoke.93
- ___29-[POProfile initWithProfile:]_block_invoke.93.cold.1
- ___29-[POProfile initWithProfile:]_block_invoke.97
- ___29-[POProfile initWithProfile:]_block_invoke.97.cold.1
- ___40-[POServiceConnection _connectToService]_block_invoke.83
- ___40-[POServiceConnection _connectToService]_block_invoke.83.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.102
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.102.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.106
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.106.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.110
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.110.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.114
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.114.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.119
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.119.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.123
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.123.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.127
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.127.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.131
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.131.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.135
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.135.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.139
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.139.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.143
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.143.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.147
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.147.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.82
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.82.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.86
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.86.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.90
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.90.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.94
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.94.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.98
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.98.cold.1
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.191
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.191.cold.1
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.197
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.197.cold.1
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.203
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.152
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.152.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.156
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.156.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.160
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.160.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.162
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.162.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.166
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.166.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.170
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.170.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.175
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.175.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.179
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.179.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.183
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.183.cold.1
- ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.100
- ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.100.cold.1
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.87
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.87.cold.1
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.87.cold.2
- ___51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.87.cold.3
- ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.113
- ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.113.cold.1
- ___52-[POAgentAuthenticationProcess _performStartupSteps]_block_invoke.86
- ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.109
- ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.109.cold.1
- ___52-[PORegistrationManager finishRegistrationWithRetry]_block_invoke.103
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.205
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.205.cold.1
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.211
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.211.cold.1
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.217
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.479
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.479.cold.1
- ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.131
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.378
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.378.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.390
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.390.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.340
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.340.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.418
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.418.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.421
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.421.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424.cold.1
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.242
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.242.cold.1
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.248
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.248.cold.1
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.254
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.254.cold.1
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.260
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.260.cold.1
- ___59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.260.cold.2
- ___59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.433
- ___59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.433.cold.1
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.459
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.459.cold.1
- ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.139
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.238
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.238.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.244
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.244.cold.1
- ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.146
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.73
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.73.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.273
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.273.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.279
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.279.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.283
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.283.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.287
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.289
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.289.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.293
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.293.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.297
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.297.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.301
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.301.cold.1
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.406
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.406.cold.1
- ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.63
- ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.63.cold.1
- ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.102
- ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.99
- ___65-[POAgentProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.99.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.286
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.286.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292.cold.1
- ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.38
- ___66-[PORegistrationManager createOrRepairUserConfigurationWithError:]_block_invoke.38.cold.1
- ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.315
- ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.319
- ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.319.cold.1
- ___67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.323
- ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.166
- ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.166.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.355
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.355.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361.cold.1
- ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.317
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.126
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.126.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.159
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.159.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.172
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.181
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.184
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.185
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.185.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.189
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.189.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.195
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.327
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.327.cold.1
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.333
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.333.cold.1
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.339
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.339.cold.1
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.345
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.345.cold.1
- ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.364
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.445
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.445.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.448
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.448.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458.cold.1
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.445
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.445.cold.1
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.451
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.451.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.108
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.108.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.114
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.114.cold.1
- ___70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.121
- ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.330
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.182
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.182.cold.1
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.cold.1
- ___72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.111
- ___72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.111.cold.1
- ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.165
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.165.cold.1
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.171
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.370
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.370.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.376
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.376.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.380
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.380.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.386
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.386.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.392
- ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.70
- ___79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.70.cold.1
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.485
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.485.cold.1
- ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.175
- ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.175.cold.1
- ___89-[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]_block_invoke
- ___89-[PODaemonConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]_block_invoke.cold.1
- ___93-[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:completion:]_block_invoke
- ___93-[POServiceConnection createUserAccount:passwordContext:smartCardContext:tokenId:completion:]_block_invoke.cold.1
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.91
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.91.cold.1
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.95
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.95.cold.1
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.99
- ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.99.cold.1
- ___block_descriptor_32_e8_v16?0Q8l
- ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
- ___block_descriptor_51_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_59_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.155
- ___block_literal_global.158
- ___block_literal_global.175
- ___block_literal_global.183
- ___block_literal_global.208
- ___block_literal_global.219
- ___block_literal_global.228
- ___block_literal_global.247
- ___block_literal_global.251
- ___block_literal_global.273
- ___block_literal_global.279
- ___block_literal_global.315
- ___block_literal_global.398
- ___block_literal_global.479
- ___block_literal_global.666
- ___block_literal_global.844
- ___block_literal_global.848
- ___block_literal_global.89
- ___block_literal_global.96
- ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
- __swiftEmptyArrayStorage
- _block_copy_helper.107
- _block_copy_helper.14
- _block_copy_helper.17
- _block_copy_helper.2
- _block_copy_helper.20
- _block_copy_helper.23
- _block_copy_helper.33
- _block_copy_helper.5
- _block_copy_helper.8
- _block_copy_helper.88
- _block_copy_helper.91
- _block_copy_helper.94
- _block_descriptor.10
- _block_descriptor.109
- _block_descriptor.16
- _block_descriptor.19
- _block_descriptor.22
- _block_descriptor.25
- _block_descriptor.35
- _block_descriptor.4
- _block_descriptor.7
- _block_descriptor.90
- _block_descriptor.93
- _block_descriptor.96
- _block_destroy_helper.108
- _block_destroy_helper.15
- _block_destroy_helper.18
- _block_destroy_helper.21
- _block_destroy_helper.24
- _block_destroy_helper.3
- _block_destroy_helper.34
- _block_destroy_helper.6
- _block_destroy_helper.89
- _block_destroy_helper.9
- _block_destroy_helper.92
- _block_destroy_helper.95
- _objc_msgSend$_startDeviceRegistration
- _objc_msgSend$authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:loginContext:completion:
- _objc_msgSend$createUserAccount:passwordContext:smartCardContext:tokenId:completion:
- _objc_msgSend$handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:
- _objc_msgSend$handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:
- _objc_msgSend$updateLoginStateForIdentifier:state:loginDate:loginType:completion:
- _objectdestroy.39Tm
- _objectdestroy.43Tm
- _objectdestroyTm
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_getWitnessTable
- _swift_retain
- _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
CStrings:
+ "(#Y"
+ "-[POAgentAuthenticationProcess requestUserAuthenticationAndChangePassword]"
+ "-[POAgentProcess performOpenIDLogin:loginUserName:callbackResponse:passwordContext:updateLocalAccountPassword:completion:]"
+ "-[POAuthPluginProcess updateLocalAccountPasswordWithTokenForUser:passwordContextData:completion:]"
+ "-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]"
+ "-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:newOpenIDUser:notified:profile:]"
+ "AccessKeyReaderIssuerCertificatePersistentRef"
+ "AccessKeyTerminalIdentityPersistentRef"
+ "AllowOpenIDForTouchIDFallback"
+ "AllowQRCodeAsOfflinePassword"
+ "AllowWebLoginPasswordSync"
+ "Biometric not available during user registration for 2FA policy: %{public}@"
+ "Biometric not available during user registration: %{public}@"
+ "ChangePassword"
+ "Creating context for user credential"
+ "Decrypting OpenID Tokens"
+ "Decrypting Tokens"
+ "Failed to complete user registration because biometric authentication (Touch ID or Apple Watch) is not available."
+ "Failed to insert token for user."
+ "Not a password or openid user"
+ "OpenID authentication requires shared device keys and protocol version 2.0."
+ "PlatformSSO"
+ "PlatformSSO_OpenIDAuth"
+ "Prompting user for OpenID authentication"
+ "RequireTouchID"
+ "RequireTouchIDOrWatch"
+ "SEP key biometric policy = %{public}@"
+ "The authorizationURL is missing."
+ "The authorizationURLKeypath is missing."
+ "WebLoginURLAllowList"
+ "WebLoginURLAllowList entry is not a string; discarding"
+ "changePasswordButtonEnabled"
+ "no credential for user for password change"
+ "openid"
+ "platformSSOLoginUI"
+ "v24@?0Q8@\"LAContext\"16"
- "#16@0:8"
- "(#V"
- "-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]"
- "-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]"
- ".cxx_destruct"
- "@\"<POAgentAuthenticationProcessKerberosDelegate>\""
- "@\"<POExtensionDelegate>\""
- "@\"<POJWKSStorageProvider>\""
- "@\"<POUIRegistrationUIProvider>\""
- "@\"<SOHostExtensionContextProtocol>\""
- "@\"LAContext\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSData\"24@0:8@\"NSString\"16"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDistributedNotificationCenter\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNotificationCenter\""
- "@\"NSNumber\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"POAgentAuthenticationProcess\""
- "@\"POAuthPluginProcess\""
- "@\"POAuthenticationProcess\""
- "@\"POConfigurationManager\""
- "@\"POConfigurationVersion\""
- "@\"PODaemonConnection\""
- "@\"PODeviceConfiguration\""
- "@\"PODirectoryServices\""
- "@\"POExtension\""
- "@\"POKerberosHelper\""
- "@\"POKeyBag\""
- "@\"POKeyWrap\""
- "@\"POKeychainHelper\""
- "@\"POLoginConfiguration\""
- "@\"POProfile\""
- "@\"PORegistrationContext\""
- "@\"PORegistrationManager\""
- "@\"POServiceConnection\""
- "@\"POServiceLoginManagerConnection\""
- "@\"POTokenHelper\""
- "@\"POUIServiceConnection\""
- "@\"POUserConfiguration\""
- "@\"POUserGroupManager\""
- "@\"SOConfigurationHost\""
- "@\"SOExtension\""
- "@\"SOExtensionManager\""
- "@\"SOFullProfile\""
- "@\"SORemoteExtensionViewController\""
- "@\"UNUserNotificationCenter\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSData\"16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@24@0:8I16B20"
- "@24@0:8^@16"
- "@24@0:8q16"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8d16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32^@40"
- "Failed to create key during user registration because touchID or watch is not available."
- "I"
- "I16@0:8"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "POAlgorithmUtil"
- "POConstantUtil"
- "PODSUser"
- "PODaemonProtocol"
- "PODeviceRegistrationStatus"
- "POExtensionDelegate"
- "POJWKSStorageProvider"
- "POJWTBody"
- "POKerberosEntry"
- "POKeychainJWKSStorageProvider"
- "POMutableJWTBody"
- "POMutableUser"
- "POPlatformSSOListener"
- "POPlatformSSOLoginManagerListener"
- "POPlatformSSOUIManagerListener"
- "PORegistrationContext"
- "POServiceCoreProtocol"
- "POServiceLoginManagerProtocol"
- "POServiceProtocol"
- "POUIAgentProcess"
- "POUIServiceProtocol"
- "POUser"
- "POUserIdentifierProvider"
- "POUserRegistrationStatus"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q36@0:8@16@24B32"
- "Q44@0:8@16@24@32B40"
- "Q60@0:8B16@20^@28^@36^@44^@52"
- "SOExtensionDelegate"
- "T#,R"
- "T@\"<POAgentAuthenticationProcessKerberosDelegate>\",W,V_kerberosDelegate"
- "T@\"<POExtensionDelegate>\",W,V_delegate"
- "T@\"<POJWKSStorageProvider>\",&,V_jwksStorageProvider"
- "T@\"<POUIRegistrationUIProvider>\",&,V_registrationUI"
- "T@\"<SOHostExtensionContextProtocol>\",&,V_hostExtensionContext"
- "T@\"LAContext\",&,V_credentialContext"
- "T@\"NSArray\",C,N,V_nonPlatformSSOAccounts"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_URLPrefix"
- "T@\"NSArray\",R,N,V_administratorGroups"
- "T@\"NSArray\",R,N,V_createUserAuthenticationMethods"
- "T@\"NSArray\",R,N,V_otherGroups"
- "T@\"NSData\",&,N,V_messageBuffer"
- "T@\"NSData\",&,N,V_sessionKey"
- "T@\"NSData\",&,V_smartCardHash"
- "T@\"NSData\",C,D"
- "T@\"NSData\",R,N,V_accessKeyReaderGroupIdentifier"
- "T@\"NSData\",R,N,V_accessKeyReaderTerminalCapabilityIdentifier"
- "T@\"NSDate\",&,V_lastAuthenticationAttempt"
- "T@\"NSDate\",R"
- "T@\"NSDictionary\",C,N"
- "T@\"NSDictionary\",C,N,V_extensionData"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,C,N,V_extensionData"
- "T@\"NSDictionary\",R,N,V_authorizationGroups"
- "T@\"NSDictionary\",R,N,V_tokenToUserMapping"
- "T@\"NSDistributedNotificationCenter\",&,V_distributedNotificationCenter"
- "T@\"NSMutableArray\",&,V_keyProxies"
- "T@\"NSMutableDictionary\",&,V__analytics"
- "T@\"NSNotificationCenter\",&,V_notificationCenter"
- "T@\"NSNumber\",&,N,V_encryptionAlgorithm"
- "T@\"NSNumber\",&,N,V_loginFrequency"
- "T@\"NSNumber\",&,N,V_signingAlgorithm"
- "T@\"NSNumber\",&,N,V_userSigningAlgorithm"
- "T@\"NSNumber\",&,V_pendingEncryptionAlgorithm"
- "T@\"NSNumber\",&,V_pendingSigningAlgorithm"
- "T@\"NSNumber\",&,V_pendingUserSEPSigningAlgorithm"
- "T@\"NSNumber\",R,N,V_sdkVersionString"
- "T@\"NSObject\",&,V_authenticationObserver"
- "T@\"NSObject\",&,V_authenticationTimerLock"
- "T@\"NSObject\",&,V_platformSSOActiveLock"
- "T@\"NSObject\",&,V_screenUnlockLock"
- "T@\"NSObject\",&,V_shieldLoweredLock"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_configurationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_loginQueue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_accountName"
- "T@\"NSString\",&,N,V_clientName"
- "T@\"NSString\",&,N,V_loginUserName"
- "T@\"NSString\",&,N,V_realm"
- "T@\"NSString\",&,N,V_registeredBundleIdentifier"
- "T@\"NSString\",&,N,V_registeredExtensionName"
- "T@\"NSString\",&,N,V_requestIdentifier"
- "T@\"NSString\",&,N,V_serviceName"
- "T@\"NSString\",&,V_containerAppBundleIdentifier"
- "T@\"NSString\",&,V_extensionIdentifier"
- "T@\"NSString\",&,V_generatedUUID"
- "T@\"NSString\",&,V_homeDirectory"
- "T@\"NSString\",&,V_loginUserName"
- "T@\"NSString\",&,V_registrationToken"
- "T@\"NSString\",&,V_shell"
- "T@\"NSString\",&,V_smartCardTokenId"
- "T@\"NSString\",&,V_ticketKeyPath"
- "T@\"NSString\",&,V_userName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,D"
- "T@\"NSString\",R,N,V_accessKeyReaderIssuerCertificateUUID"
- "T@\"NSString\",R,N,V_accessKeyTerminalIdentityUUID"
- "T@\"NSString\",R,N,V_accountDisplayName"
- "T@\"NSString\",R,N,V_extensionBundleIdentifier"
- "T@\"NSString\",R,N,V_registrationToken"
- "T@\"NSString\",R,V_userIdentifier"
- "T@\"NSTimer\",&,V_authenticationTimer"
- "T@\"NSURL\",&,N,V_filePath"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"POAgentAuthenticationProcess\",&,V_agentProcess"
- "T@\"POAgentAuthenticationProcess\",&,V_process"
- "T@\"POAgentAuthenticationProcess\",W,V_process"
- "T@\"POAuthPluginProcess\",&,V_systemAuthPluginProcess"
- "T@\"POAuthPluginProcess\",R,N,V_systemAuthPluginProcess"
- "T@\"POAuthPluginProcess\",R,N,V_userAuthPluginProcess"
- "T@\"POAuthenticationProcess\",&,V_authenticationProcess"
- "T@\"POConfigurationManager\",&,N,V_configurationManager"
- "T@\"POConfigurationManager\",&,V_configurationManager"
- "T@\"POConfigurationVersion\",&,V_deviceConfigurationVersion"
- "T@\"POConfigurationVersion\",&,V_loginConfigurationVersion"
- "T@\"POConfigurationVersion\",&,V_userConfigurationVersion"
- "T@\"PODirectoryServices\",&,V_directoryServices"
- "T@\"POExtension\",&,V_ssoExtension"
- "T@\"POKerberosHelper\",&,V_kerberosHelper"
- "T@\"POKeyBag\",&,V_keyBag"
- "T@\"POKeyWrap\",&,V_keyWrap"
- "T@\"POKeychainHelper\",&,V_keychainHelper"
- "T@\"POLoginConfiguration\",R,C,N"
- "T@\"POProfile\",&,V_profile"
- "T@\"PORegistrationContext\",&,V_registrationContext"
- "T@\"PORegistrationManager\",&,V_registrationManager"
- "T@\"POTokenHelper\",&,V_tokenHelper"
- "T@\"POUserGroupManager\",&,V_userGroupManager"
- "T@\"POUserLoginConfiguration\",R,C,N"
- "T@\"SOConfigurationHost\",&,N,V_configurationHost"
- "T@\"SOConfigurationHost\",&,V_configurationHost"
- "T@\"SOExtensionManager\",&,V_extensionManager"
- "T@\"SOFullProfile\",C,N,V_profile"
- "T@\"UNUserNotificationCenter\",&,V_userNotificationCenter"
- "T@?,C,N,V___screenUnlockHandler"
- "T@?,C,N,V___shieldLoweredHandler"
- "T@?,C,V_authenticationCompletion"
- "T@?,C,V_invalidationHandler"
- "TB,GisBuddyFlow,V_buddyFlow"
- "TB,GisNewPasswordUser,V_newPasswordUser"
- "TB,GisNewSecureEnclaveUser,V_newSecureEnclaveUser"
- "TB,GisNewSmartCardUser,V_newSmartCardUser"
- "TB,GisRepair,V_repair"
- "TB,GisRetry,V_retry"
- "TB,GisRunningInBuddy,V_runningInBuddy"
- "TB,N,GisActionButtonEnabled,V_actionButtonEnabled"
- "TB,N,GisAuthenticateButtonEnabled,V_authenticateButtonEnabled"
- "TB,N,GisPlatformSSOEnabled,V_platformSSOEnabled"
- "TB,N,V_isSystem"
- "TB,R"
- "TB,R,GisDeviceRegistered"
- "TB,R,GisUserRegistered"
- "TB,R,V_allowAccessKeyExpressMode"
- "TB,V_allowDeviceIdentifiersInAttestation"
- "TB,V_authorizationEnabled"
- "TB,V_authorizationProvided"
- "TB,V_createFirstUserDuringSetupEnabled"
- "TB,V_createUsersEnabled"
- "TB,V_credentialTransferCompleted"
- "TB,V_dataVaultInitialized"
- "TB,V_deviceKeysShouldChange"
- "TB,V_enableNetworkChanges"
- "TB,V_enableRegistrationDuringSetup"
- "TB,V_forLogin"
- "TB,V_migratingDeviceKeys"
- "TB,V_newUserBindingComplete"
- "TB,V_platformSSOAccount"
- "TB,V_platformSSOActive"
- "TB,V_registrationFailed"
- "TB,V_resetKeys"
- "TB,V_screenUnlocked"
- "TB,V_shieldLowered"
- "TB,V_shouldRunConfigurationChangeWhenUnlocked"
- "TB,V_synchronizeProfilePicture"
- "TB,V_temporarySessionQuickLogin"
- "TB,V_useSharedDeviceKeys"
- "TB,V_userIsPlatformSSOUser"
- "TB,V_userNotified"
- "TB,V_userSEPKeyInvalid"
- "TGTReceivedForRealm:upn:cache:"
- "TGTRequestDidBegin"
- "TGTRequestDidComplete"
- "TI,V_gid"
- "TI,V_uid"
- "TQ,N,V_fileVaultPolicy"
- "TQ,N,V_loginPolicy"
- "TQ,N,V_unlockPolicy"
- "TQ,R"
- "T^{__SecCertificate=},R,N,V_deviceAttestationCertificate"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_pendingEncryptionKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_pendingSigningKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_pendingUserSEPKey"
- "Ti,N,V_encryptionKeyType"
- "Ti,R,N"
- "Ti,R,V_authenticationMethod"
- "Ti,V_authMethod"
- "Ti,V_failureCount"
- "Tq,N,V_actionButtonAction"
- "Tq,N,V_authenticationMethod"
- "Tq,N,V_deviceRegistrationStatus"
- "Tq,N,V_offlineGracePeriod"
- "Tq,N,V_requireAuthGracePeriod"
- "Tq,N,V_userRegistrationStatus"
- "Tq,N,V_userTokenStatus"
- "Tq,R"
- "Tq,R,V_newUserAuthorizationMode"
- "Tq,R,V_userAuthorizationMode"
- "Tq,V_options"
- "Tq,V_protocolVersion"
- "Tq,V_state"
- "UNUserNotificationCenterDelegate"
- "URLByAppendingPathComponent:"
- "URLPrefix"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__SecCertificate=}"
- "^{__SecCertificate=}16@0:8"
- "^{__SecIdentity=}24@0:8q16"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@0:8q16"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8q16^@24"
- "^{gss_cred_id_t_desc_struct=}24@0:8@16"
- "_URLPrefix"
- "___screenUnlockHandler"
- "___shieldLoweredHandler"
- "__analytics"
- "__removeDeviceConfigurationWithIdentifier:"
- "__removeLoginConfigurationForIdentifier:"
- "__screenUnlockHandler"
- "__shieldLoweredHandler"
- "_accessKeyReaderGroupIdentifier"
- "_accessKeyReaderIssuerCertificateUUID"
- "_accessKeyReaderTerminalCapabilityIdentifier"
- "_accessKeyTerminalIdentityUUID"
- "_accountDisplayName"
- "_accountName"
- "_actionButtonAction"
- "_actionButtonEnabled"
- "_administratorGroups"
- "_agentProcess"
- "_allowAccessKeyExpressMode"
- "_allowDeviceIdentifiersInAttestation"
- "_analytics"
- "_authMethod"
- "_authenticateButtonEnabled"
- "_authenticationCompletion"
- "_authenticationMethod"
- "_authenticationObserver"
- "_authenticationProcess"
- "_authenticationTimer"
- "_authenticationTimerLock"
- "_authorizationEnabled"
- "_authorizationGroups"
- "_authorizationProvided"
- "_buddyFlow"
- "_clientName"
- "_configurationHost"
- "_configurationManager"
- "_configurationQueue"
- "_connectToService"
- "_containerAppBundleIdentifier"
- "_createFirstUserDuringSetupEnabled"
- "_createUserAuthenticationMethods"
- "_createUsersEnabled"
- "_credential"
- "_credentialContext"
- "_credentialTransferCompleted"
- "_currentDeviceConfiguration"
- "_currentLoginConfiguration"
- "_currentUserConfiguration"
- "_dataVaultInitialized"
- "_defaultCacheFile"
- "_defaultConfigurationPath"
- "_delegate"
- "_deleteAllCachedAttestations"
- "_deleteCachedAttestationForExtensionIdentifier:key:"
- "_deviceAttestationCertificate"
- "_deviceConfigurationForIdentifier:"
- "_deviceConfigurationVersion"
- "_deviceKeysShouldChange"
- "_deviceRegistrationStatus"
- "_directoryServices"
- "_disableAccessKeyDefaults"
- "_disablePlatformSSORuleForLogin:"
- "_disablePlatformSSORuleForScreensaver:"
- "_disableTemporarySessionDefaults"
- "_distributedNotificationCenter"
- "_doLoginWithPasswordContext:tokenId:"
- "_doRefreshWithPasswordContext:tokenId:"
- "_doUnlockForTokenWithCredentialContext:atLogin:"
- "_enableAccessKeyDefaults"
- "_enableNetworkChanges"
- "_enablePlatformSSORuleForLogin:"
- "_enablePlatformSSORuleForScreensaver:"
- "_enableRegistrationDuringSetup"
- "_enableTemporarySessionDefaults"
- "_encryptionAlgorithm"
- "_encryptionKeyType"
- "_extension"
- "_extensionBundleIdentifier"
- "_extensionData"
- "_extensionIdentifier"
- "_extensionManager"
- "_extensionViewController"
- "_failureCount"
- "_filePath"
- "_fileVaultPolicy"
- "_forLogin"
- "_generatedUUID"
- "_gid"
- "_handleConfigurationChanged:startup:"
- "_handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:"
- "_homeDirectory"
- "_hostExtensionContext"
- "_initCachePath:ifNeededWithError:"
- "_initDataVaultIfNeededWithError:"
- "_invalidationHandler"
- "_isSystem"
- "_jwksStorageProvider"
- "_kerberosDelegate"
- "_kerberosHelper"
- "_keyBag"
- "_keyForKeyType:error:"
- "_keyProxies"
- "_keyWrap"
- "_keychainHelper"
- "_lastAuthenticationAttempt"
- "_loginConfigurationVersion"
- "_loginContext"
- "_loginFrequency"
- "_loginPolicy"
- "_loginQueue"
- "_loginUserName"
- "_messageBuffer"
- "_migratingDeviceKeys"
- "_newPasswordUser"
- "_newSecureEnclaveUser"
- "_newSmartCardUser"
- "_newUserAuthorizationMode"
- "_newUserBindingComplete"
- "_nextAvailableUserId:"
- "_nonPlatformSSOAccounts"
- "_notificationCenter"
- "_offlineGracePeriod"
- "_options"
- "_otherGroups"
- "_pendingEncryptionAlgorithm"
- "_pendingEncryptionKey"
- "_pendingSigningAlgorithm"
- "_pendingSigningKey"
- "_pendingUserSEPKey"
- "_pendingUserSEPSigningAlgorithm"
- "_performStartupSteps"
- "_platformSSOAccount"
- "_platformSSOActive"
- "_platformSSOActiveLock"
- "_platformSSOEnabled"
- "_process"
- "_profile"
- "_protocolVersion"
- "_realm"
- "_registeredBundleIdentifier"
- "_registeredExtensionName"
- "_registrationContext"
- "_registrationFailed"
- "_registrationManager"
- "_registrationToken"
- "_registrationUI"
- "_removeDeviceConfigurationForIdentifier:error:"
- "_removeLoginConfigurationForIdentifier:error:"
- "_removeUserConfigurationForIdentifier:error:"
- "_repair"
- "_requestIdentifier"
- "_requireAuthGracePeriod"
- "_resetKeys"
- "_retry"
- "_runningInBuddy"
- "_saveCredentialForUserName:passwordContext:completion:"
- "_saveDeviceConfiguration:identifier:error:"
- "_saveLoginConfiguration:identifier:error:"
- "_saveUserConfigurationData:forIdentifier:error:"
- "_saveUserLoginStateList:error:"
- "_screenUnlockLock"
- "_screenUnlocked"
- "_sdkVersionString"
- "_serviceConnection"
- "_serviceName"
- "_sessionKey"
- "_setQueue:"
- "_setTargetUserIdentifier:"
- "_setTokens:identifier:extensionIdentifier:returningError:"
- "_setupContext"
- "_shell"
- "_shieldLowered"
- "_shieldLoweredLock"
- "_shouldRunConfigurationChangeWhenUnlocked"
- "_signingAlgorithm"
- "_smartCardHash"
- "_smartCardTokenId"
- "_ssoExtension"
- "_startDeviceRegistration"
- "_startDeviceRegistrationWithCompletionHandler:"
- "_startUserRegistration"
- "_startUserRegistrationWithCompletionHandler:"
- "_state"
- "_synchronizeProfilePicture"
- "_systemAuthPluginProcess"
- "_temporarySessionQuickLogin"
- "_ticketKeyPath"
- "_tokenHelper"
- "_tokenToUserMapping"
- "_tokensForExtensionIdentifier:identifier:"
- "_uid"
- "_unload"
- "_unlockPolicy"
- "_updateGroupForRight:newGroup:"
- "_updateRegistrationState:failed:"
- "_useSharedDeviceKeys"
- "_userAuthPluginProcess"
- "_userAuthorizationMode"
- "_userConfigurationVersion"
- "_userGroupManager"
- "_userIdentifier"
- "_userIsPlatformSSOUser"
- "_userName"
- "_userNotificationCenter"
- "_userNotified"
- "_userRegistrationStatus"
- "_userSEPKeyInvalid"
- "_userSigningAlgorithm"
- "_userTokenStatus"
- "_verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:"
- "_xpcConnection"
- "absoluteString"
- "accessKeyReaderGroupIdentifier"
- "accessKeyReaderIssuerCertificateUUID"
- "accessKeyReaderTerminalCapabilityIdentifier"
- "accessKeyTerminalIdentityUUID"
- "accountDisplayName"
- "acquireCredentialForUUID:"
- "actionIdentifier"
- "actionWithIdentifier:title:options:"
- "addCustomClaims:"
- "addEntriesFromDictionary:"
- "addEvent:"
- "addEvent:forKeyType:"
- "addLocalUser:toLocalGroup:completion:"
- "addNotificationRequest:withCompletionHandler:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addPlatformSSOToSearchPolicyWithCompletion:"
- "addTimer:forMode:"
- "addTokens:metaData:toKeychainForService:username:"
- "addTokens:metaData:toKeychainForService:username:system:"
- "administratorGroups"
- "agentProcess"
- "allData"
- "allKeys"
- "allowAccessKeyExpressMode"
- "allowDeviceIdentifiersInAttestation"
- "alternateDSID"
- "analyticsForLoginConfiguration:"
- "analyticsForLoginManager:"
- "analyticsForLoginType:result:"
- "analyticsForRegistrationType:options:result:"
- "appSSOEnabled"
- "array"
- "arrayWithObjects:count:"
- "attestKey:clientData:completion:"
- "attestKey:pending:clientDataHash:completion:"
- "attestPendingKey:clientData:completion:"
- "auditSessionIdentifier"
- "auditToken"
- "authMethod"
- "authMethodWithString:"
- "authenticateTemporaryUserAccount:forLogin:passwordContext:smartCardContext:tokenId:loginContext:completion:"
- "authenticationCompletion"
- "authenticationMethodWithCompletion:"
- "authenticationMethods"
- "authenticationObserver"
- "authenticationProcess"
- "authenticationTimer"
- "authenticationTimerLock"
- "authorization:didCompleteWithCredential:error:"
- "authorizationDidFailWithOtherVersionError:"
- "authorizationEnabled"
- "authorizationGroups"
- "authorizationProvided"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "beginDeviceRegistrationUsingOptions:extensionData:completion:"
- "beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:"
- "bestEncryptionAlgorithm:or:"
- "bestSigningAlgorithm:or:"
- "bindTokenForUsername:hash:wrapHash:tokenId:pinContext:completion:"
- "boolValue"
- "buddyFlow"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleIdentifierForXPCConnection:"
- "bundlePath"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bundleWithIdentifier:"
- "bytes"
- "cacheName"
- "calculateExpirationForTokens:"
- "canEvaluatePolicy:error:"
- "canPerformRegistration"
- "canPerformRegistrationCompletion:"
- "categoryIdentifier"
- "categoryWithIdentifier:actions:intentIdentifiers:options:"
- "certificateForData:"
- "changePasswordForUser:passwordContext:secureToken:secureTokenPasswordContext:completion:"
- "changePasswordUsingBootstrapTokenForUser:passwordContext:completion:"
- "changeTempSessionAccountWithCompletion:"
- "checkForValidKerberosTGT:"
- "checkIfBiometricConstraintsForSigning:"
- "checkIfGroupNamesNeedUpdate"
- "checkIfGroupNamesNeedUpdateForRegistrationManager:"
- "checkIfPlatformSSOIsActive"
- "checkIfProfilePictureNeedsUpdate"
- "checkVersion"
- "class"
- "cleanupUserConfigAfterMigrationToShared"
- "clientName"
- "clientNameKeyName"
- "close"
- "closeDialogs"
- "code"
- "compare:"
- "completeLegacyUserRegistration"
- "completeRotationKeyForKeyType:"
- "completeRotationKeyForKeyType:completion:"
- "componentsSeparatedByString:"
- "configurationChanged:"
- "configurationDidChangeAndRemovedExtension:removed:"
- "configurationDidChangeAndRemovedExtension:removed:completion:"
- "configurationHost"
- "configurationManager"
- "configurationQueue"
- "configurationRemovedForExtension:"
- "conformsToProtocol:"
- "connectionInvalidated"
- "containerAppBundleIdentifier"
- "containingBundleRecord"
- "containsObject:"
- "content"
- "continueDeviceRegistration:"
- "continueUserRegistration:"
- "copy"
- "copyIdentityForKeyType:"
- "copyKeyForKeyType:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAppSSOCachePath"
- "createAppSSOCachePathWithCompletion:"
- "createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:"
- "createContextForUserCredential"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createFirstUserDuringSetupEnabled"
- "createIdentityFromEndpoint:error:"
- "createKeyFromEndpoint:error:"
- "createOrRepairDeviceConfigurationWithError:"
- "createOrRepairUserConfigurationWithError:"
- "createOrUpdateAdminGroups:authorizationGroups:previousAuthorizationGroups:otherGroups:completion:"
- "createOrUpdateUser:completion:"
- "createOrUpdateUser:withError:"
- "createPasswordChangedNotificationWithAccountName:extensionIdentifier:"
- "createPlatformSSOAdminGroupWithCompletion:"
- "createRegistrationNotificationWithAccountName:"
- "createRegistrationUpdateNotificationWithAccountName:"
- "createSEPEncryptionKeyForAlgorithm:shared:"
- "createSEPSigningKeyForAlgorithm:shared:"
- "createSignInNotificationWithAccountName:extensionIdentifier:"
- "createTemporaryUser:passwordContext:completion:"
- "createUnlockKeyWithPublicKey:userName:returningCertificate:hash:encryptedData:"
- "createUser:passwordContext:name:loginUserName:idpIdentifier:isAdmin:groupMembership:completion:"
- "createUserAccount:passwordContext:smartCardContext:tokenId:completion:"
- "createUserAuthenticationMethods"
- "createUserConfigurationForBuddyUser"
- "createUserLoginTypes"
- "createUserSEPSigningKeyForAlgorithm:"
- "createUserSEPSigningKeyForAlgorithm:userPresence:currentSet:"
- "createUsersEnabled"
- "credentialContext"
- "credentialTransferCompleted"
- "currentDeviceConfiguration"
- "currentLoginConfiguration"
- "currentRefreshToken"
- "currentRunLoop"
- "currentTempSessionAccountWithCompletion:"
- "currentUser"
- "currentUserConfiguration"
- "data"
- "dataForCertificate:"
- "dataRepresentation"
- "dataUsingEncoding:"
- "dataVaultInitialized"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decimalValue"
- "decodeObjectOfClass:forKey:"
- "decryptPendingSSOTokens:UsingPrivateKey:sharedData:"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "description"
- "destroyCredentialForUUID:"
- "deviceAttestationCertificate"
- "deviceConfiguration"
- "deviceConfigurationForIdentifier:completion:"
- "deviceConfigurationVersion"
- "deviceEncryptionAlgorithmToUse:deviceConfiguration:"
- "deviceEncryptionIdentity"
- "deviceEncryptionKey"
- "deviceEncryptionKeyWithContext:"
- "deviceKeysShouldChange"
- "deviceRegistered"
- "deviceRegistrationsNeedsRepair"
- "deviceRegistrationsNeedsRepairWithCompletion:"
- "deviceSigningAlgorithmToUse:deviceConfiguration:"
- "deviceSigningIdentity"
- "deviceSigningKey"
- "deviceSigningKeyWithContext:"
- "deviceStatus"
- "deviceStatusWithCompletion:"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "directoryServices"
- "disablePlatformSSORulesAndDefaults:"
- "displayNamesForGroups:extensionData:completion:"
- "distributedNotificationCenter"
- "doUnlockForPasswordWithCredentialContext:atLogin:"
- "doUnlockForSmartCardWithCredentialContext:tokenId:atLogin:"
- "doUnlockForTokenLoginWithCredentialContext:atLogin:"
- "doUnlockForTokenUnlockWithCredentialContext:atLogin:"
- "doUnlockWithEmptyCredentialContext:atLogin:"
- "doubleValue"
- "enableNetworkChanges"
- "enablePlatformSSORulesAndDefaults:"
- "enablePlatformSSORulesAndDefaultsIfNeeded:"
- "enableRegistrationDuringSetup"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptPendingSSOTokens:usingPublicKey:sharedData:encryptedTokens:"
- "encryptionAlgorithm"
- "encryptionKeyType"
- "encryptionKeyTypeKeyName"
- "endpoint"
- "errorWithCode:description:"
- "errorWithCode:underlyingError:description:"
- "errorWithDomain:code:userInfo:"
- "evaluateAccessControl:operation:options:error:"
- "evaluateWithObject:"
- "exchangeKerberosTGTForEntry:"
- "exchangeRequired"
- "exchangeTGTForStatus:"
- "exitDeviceRegistration:"
- "exitRegistration:"
- "exitUserRegistration:"
- "extensionBundleIdentifier"
- "extensionData"
- "extensionIdentifier"
- "extensionManager"
- "externalizedContext"
- "failDeviceRegistrationBeforeAuthorization"
- "failDeviceRegistrationPostRegistrationWithUserInteractionAllowed:"
- "failUserRegistrationBeforeAuthorization"
- "failedToConnect"
- "failureCount"
- "federationMexURL"
- "federationMexURLKeypath"
- "federationPredicate"
- "federationRequestURN"
- "federationType"
- "federationUserPreauthenticationURL"
- "fileExistsAtPath:isDirectory:"
- "filePath"
- "fileSystemRepresentation"
- "fileVaultPolicy"
- "findExistingSmartCardBinding"
- "findTokenIdForSmartCardAMUser:tokenHash:"
- "findTokenIdForSmartCardBoundUser:tokenHash:"
- "findUser:withError:"
- "findUserWithName:completion:"
- "finishRegistrationWithRetry"
- "finishRegistrationWithStatus:"
- "finishRegistrationWithStatus:message:"
- "forLogin"
- "forceKerberosTGTExchange"
- "getAllUsersWithCompletion:"
- "getAllUsersWithError:"
- "getLoginTypeForUser:completion:"
- "gid"
- "handleAgentStartup"
- "handleAuthRights"
- "handleAuthorizationForNewUsers"
- "handleBindingForNewPasswordAccounts"
- "handleChecksAfterSuccessfulLoginWithPasswordContext:"
- "handleConfigurationChanged:"
- "handleConfigurationChanged:startup:"
- "handleDeviceAndUserRegistrationForRepair:"
- "handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:"
- "handleDeviceRegistrationNotification"
- "handleEncryptionKeyRotation"
- "handleKerberosMappingForTokens:extensionIdentifier:userConfiguration:"
- "handleKerberosMappingForTokens:loginConfiguration:userConfiguration:"
- "handleKeyRequestSync"
- "handleKeyRequestWithCompletion:"
- "handleKeyUpdatesWithPasswordContext:"
- "handleNetworkChange"
- "handlePendingSSOTokensWithSharedData:"
- "handlePreviousRefreshTokens"
- "handleRegistrationViewControllerWithCompletion:"
- "handleRemovingRegistrationForExtension:alreadyDeleted:"
- "handleRemovingSSOTokens"
- "handleScreenLock"
- "handleScreenUnlock"
- "handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:afterBuddy:"
- "handleTokenBindingWithPasswordContext:"
- "handleUnfinishedTGTExchanges"
- "handleUserAuthorizationForRegistration"
- "handleUserAuthorizationNeededForAccountDisplayName:bundleIdentifier:"
- "handleUserAuthorizationUsing:userName:tokens:configurationManager:"
- "handleUserCredentialNeededAtLogin:smartCard:accountDisplayName:bundleIdentifier:returningContext:"
- "handleUserNeedsReauthenticationAfterDelay:"
- "handleUserRegistrationForUser:repair:"
- "handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:"
- "handleUserRegistrationNotification"
- "hasAllRequiredValues"
- "hasAnyMDMProfileForExtension:"
- "hash"
- "homeDirectory"
- "hostExtensionContext"
- "hpkeAuthPublicKey"
- "hpkePsk"
- "hpkePsk_id"
- "i16@0:8"
- "i32@0:8@16@24"
- "iconForApplicationIdentifier:"
- "identifier"
- "identityForKeyType:"
- "importKerberosEntry:error:"
- "importSuccessful"
- "includePreviousRefreshTokenInLoginRequest"
- "increaseVersionWithMessage:"
- "init"
- "initForAgentWithDelegate:configurationHost:"
- "initForBaseSystem:"
- "initForLogin:authenticationProcess:"
- "initWithAgentAuthenticationProcess:userNotificationCenter:configurationHost:"
- "initWithAuthenticationProcess:"
- "initWithBase64EncodedString:options:"
- "initWithBundleIdentifier:"
- "initWithCoder:"
- "initWithConfigurationHost:"
- "initWithConfigurationType:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDictionary:"
- "initWithExtensionBundleIdentifier:delegate:"
- "initWithExtensionBundleIdentifier:extensionManager:delegate:"
- "initWithExternalizedContext:"
- "initWithExternalizedContext:userSession:"
- "initWithFilePath:"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "initWithIdentifierProvider:"
- "initWithIdentity:"
- "initWithJWTData:"
- "initWithKey:"
- "initWithLoginUserName:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithProfile:"
- "initWithSystem:"
- "initWithUUIDString:"
- "initWithUid:"
- "initWithUid:forLogin:"
- "initWithUserName:"
- "initWithUserName:directoryServices:sharedOnly:"
- "initWithUserName:identifierProvider:sharedOnly:"
- "initWithXPCConnection:"
- "initWithXPCConnection:authenticationProcess:"
- "initWithXPCConnection:identifierProvider:jwksStroageProvider:"
- "insertTokenForUser:"
- "intValue"
- "integerValue"
- "interfaceWithInternalProtocol:"
- "internalErrorWithMessage:"
- "invalidCredentialPredicate"
- "invalidate"
- "invalidateAllKeyProxies"
- "invalidationHandler"
- "isActionButtonEnabled"
- "isAssociatedDomainValidated"
- "isAuthenticateButtonEnabled"
- "isBuddyFlow"
- "isCallerCurrentSSOExtension"
- "isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:"
- "isCredentialSet:"
- "isCurrentSSOExtension:"
- "isDeviceRegisteredWithCompletion:"
- "isEncryptionAlgorithm:validForKey:"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNewPasswordUser"
- "isNewSecureEnclaveUser"
- "isNewSmartCardUser"
- "isNewUser"
- "isPlatformSSOEnabled"
- "isPlatformSSOUserName:"
- "isProxy"
- "isRepair"
- "isRetry"
- "isRunningInBuddy"
- "isSystem"
- "isTemporaryAccountUserName:"
- "isURL:validForProfile:"
- "isUserKeybagUnlocked"
- "isUserNotification"
- "isUserRegisteredWithCompletion:"
- "isValidJSONObject:"
- "jwksCache"
- "jwksCacheForExtensionIdentifier:"
- "jwksStorageProvider"
- "kerberosDelegate"
- "kerberosHelper"
- "kerberosStatus"
- "kerberosTicketMappings"
- "keyBag"
- "keyProxies"
- "keyProxyEndpointForKeyType:"
- "keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:"
- "keyWillRotateForKeyType:newKey:extensionData:completion:"
- "keyWrap"
- "keychainHelper"
- "lastAuthenticationAttempt"
- "lastEncryptionKeyChange"
- "lastLoginDate"
- "length"
- "listener:shouldAcceptNewConnection:"
- "loadExtensionWithBundleIdentifier:"
- "loadSSOExtensionWithExtensionBundleIdentifier:"
- "loadUsers_lockedWithError:"
- "localizedName"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "loginConfigurationForIdentifier:completion:"
- "loginConfigurationVersion"
- "loginConfigurationWithCompletion:"
- "loginFrequency"
- "loginPolicy"
- "loginQueue"
- "loginRequestHpkePsk"
- "loginRequestHpkePsk_id"
- "loginType"
- "loginUserNameWithCompletion:"
- "lowercaseString"
- "maskName:"
- "mergedConfigurationWithUserLoginConfiguration:"
- "messageBuffer"
- "messageBufferKeyName"
- "migrateConfiguration:completion:"
- "migratingDeviceKeys"
- "mutableBytes"
- "mutableCopy"
- "newPasswordUser"
- "newSecureEnclaveUser"
- "newSmartCardUser"
- "newUserAuthorizationMode"
- "newUserBindingComplete"
- "nonPlatformSSOAccounts"
- "nonceEndpointURL"
- "notification"
- "notificationCenter"
- "notifyDeviceRegistrationDidChange"
- "notifyKerberosDelegateTGTDidBegin"
- "notifyKerberosDelegateTGTDidComplete"
- "notifyUserRegistrationDidChange"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "offlineGracePeriod"
- "operatingSystemVersionString"
- "options"
- "otherGroups"
- "passwordDataFromContext:error:"
- "passwordDidChangeForUsername:passwordContext:completion:"
- "path"
- "pendingEncryptionAlgorithm"
- "pendingEncryptionKey"
- "pendingSigningAlgorithm"
- "pendingSigningKey"
- "pendingUserSEPKey"
- "pendingUserSEPSigningAlgorithm"
- "performKeyRequestUsingContext:completion:"
- "performLoginForCurrentUserWithPasswordContext:"
- "performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:"
- "performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:"
- "performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:"
- "performPasswordLogin:passwordContext:updateLocalAccountPassword:"
- "performPasswordLogin:passwordContext:updateLocalAccountPassword:completion:"
- "performPasswordLoginUsingContext:completion:"
- "performSEPKeyLoginUsingContext:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSmartCardLoginUsingContext:completion:"
- "performTokenRefreshUsingContext:completion:"
- "platformSSO"
- "platformSSOAccount"
- "platformSSOActive"
- "platformSSOActiveLock"
- "platformSSODevModeEnabled"
- "platformSSOEnabledForUsername:"
- "platformSSOProfile"
- "postAuthenticationNotification:"
- "postNotificationName:object:userInfo:"
- "postNotificationName:object:userInfo:deliverImmediately:"
- "predicateWithFormat:"
- "presentAuthorizationViewControllerInWindow:hints:completion:"
- "presentAuthorizationViewControllerWithHints:requestIdentifier:completion:"
- "presentRegistrationViewControllerWithCompletion:"
- "process"
- "processInfo"
- "profile"
- "profilePictureForUserUsingExtensionData:completion:"
- "promptUserForRegistration"
- "protocolVersion"
- "protocolVersionCompletion:"
- "pssoRegistrationToken"
- "q16@0:8"
- "realm"
- "realmKeyName"
- "refreshEndpointURL"
- "refreshTokenFromTokens:"
- "registerDefaults:"
- "registrationCompleted"
- "registrationContext"
- "registrationDidCancelWithCompletion:"
- "registrationDidCompleteWithCompletion:"
- "registrationFailed"
- "registrationManager"
- "registrationNeedsToShowUI"
- "registrationState"
- "registrationTokenWithCompletion:"
- "registrationUI"
- "release"
- "reloadSSOExtensionIfNeeded"
- "removeAllDeliveredNotifications"
- "removeAllPendingNotificationRequests"
- "removeBindingForNonPasswordAuth"
- "removeDelegateForRequestIdentifier:"
- "removeDeliveredNotificationsWithIdentifiers:"
- "removeDeviceConfiguration"
- "removeDeviceConfigurationForIdentifier:completion:"
- "removeItemAtURL:error:"
- "removeLocalUser:fromLocalGroup:completion:"
- "removeLoginConfiguration"
- "removeLoginConfigurationForIdentifier:completion:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removePendingNotificationRequestsWithIdentifiers:"
- "removePlatformSSOAdminGroupWithCompletion:"
- "removePlatformSSOFromSearchPolicyWithCompletion:"
- "removePlatformSSOUser:completion:"
- "removeTokensFromKeychainWithService:username:system:"
- "removeUserConfigurationForIdentifier:completion:"
- "removeUserConfigurationForUserName:"
- "removeUserDeviceConfiguration"
- "removeUserLoginConfiguration"
- "removeUserWithName:completion:"
- "removeUserWithName:withError:"
- "repair"
- "request"
- "requestAndBindSmartCardForUser"
- "requestAuthorizationViewControllerWithCompletion:"
- "requestDidCompleteWithError:"
- "requestIdentifier"
- "requestReauthenticationWithCompletion:"
- "requestReauthenticationWithRequestIdentifier:completion:"
- "requestSmartCardForBinding:window:tokenId:tokenHash:wrapTokenHash:pinContext:"
- "requestUserAuthenticationSyncPassword:completion:"
- "requestUserAuthenticationWithUserInfo:forceLogin:"
- "requestUserAuthenticationWithWindow:completion:"
- "requestUserPasswordChangePreference"
- "requestWithIdentifier:content:trigger:destinations:"
- "requireAuthGracePeriod"
- "reset"
- "resetDeviceKeysWithCompletion:"
- "resetKeys"
- "resetRegistrationWithCompletion:"
- "resetStoredConfiguration"
- "resetStoredConfigurationWithCompletion:"
- "resetTemporaryAccountWithName:completion:"
- "resetUserSecureEnclaveKeyWithCompletion:"
- "respondsToSelector:"
- "restorePlatformSSORulesAndDefaultsIfNeeded"
- "resume"
- "retain"
- "retainContextForUserName:context:completion:"
- "retainCount"
- "retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:"
- "retrieveIdentityForTokenId:context:forSigning:hash:identity:"
- "retrievePendingSSOTokenForIdentifier:completion:"
- "retrievePendingSSOTokensForUserName:"
- "retrieveProfilePicture"
- "retrieveStashedDecryptionContextForIdentifier:completion:"
- "retrieveStashedSSOTokenForIdentifier:completion:"
- "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
- "retry"
- "rotateKeyForKeyType:"
- "rotateKeyForKeyType:completion:"
- "runningInBuddy"
- "saveAppSSOConfiguration:"
- "saveAppSSOConfiguration:completion:"
- "saveCachedContextsToDiskWithCompletion:"
- "saveCertificate:keyType:"
- "saveConfigurationData:completion:"
- "saveCredentialForUserName:passwordContext:"
- "saveCredentialForUserName:passwordContext:completion:"
- "saveCurrentUserConfiguration"
- "saveDelegate:forRequestIdentifier:"
- "saveDeviceConfiguration:"
- "saveDeviceConfiguration:identifier:completion:"
- "saveLoginConfiguration:"
- "saveLoginConfiguration:error:"
- "saveLoginConfiguration:identifier:completion:"
- "savePendingSSOTokens:forUserName:"
- "savePendingSSOTokens:identifier:completion:"
- "savePlatformSSOUniqueIdentifier:forUser:completion:"
- "saveSSOTokens:toKeychainUsingContext:tokenId:"
- "saveStashedDecryptionContext:identifier:completion:"
- "saveStashedSSOTokens:forUserName:"
- "saveStashedSSOTokens:identifier:completion:"
- "saveUserConfiguration:forIdentifier:completion:"
- "saveUserConfiguration:forUserName:"
- "saveUserConfigurationData:forIdentifier:completion:"
- "saveUserLoginConfiguration:error:"
- "saveUsers_locked:withError:"
- "screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:"
- "screenDidUnlockWithCredentialContext:smartCardContext:biometricContext:tokenId:atLogin:tokenUnlock:completion:"
- "screenUnlockLock"
- "screenUnlocked"
- "sdkVersionString"
- "secIdentityProxyEndpointForKeyType:completion:"
- "secKeyProxyEndpointForKeyType:completion:"
- "self"
- "sendPasswordChangedNotification"
- "sepKey"
- "sepKeyCertificate"
- "sepKeyWithContext:"
- "serviceName"
- "serviceNameKeyName"
- "sessionKey"
- "sessionKeyKeyName"
- "setAccessTokenReaderGroupIdentifier:"
- "setAccessTokenReaderTerminalCapabilityIdentifier:"
- "setAccountDisplayName:"
- "setAccountName:"
- "setActionButtonAction:"
- "setActionButtonEnabled:"
- "setAdministratorGroups:"
- "setAgentProcess:"
- "setAllowAccessTokenExpressMode:"
- "setAllowDeviceIdentifiersInAttestation:"
- "setAltSecurityIdentity:"
- "setAttributes:ofItemAtPath:error:"
- "setAuthGracePeriodStart:"
- "setAuthMethod:"
- "setAuthenticateButtonEnabled:"
- "setAuthenticationCompletion:"
- "setAuthenticationMethod:"
- "setAuthenticationObserver:"
- "setAuthenticationProcess:"
- "setAuthenticationTimer:"
- "setAuthenticationTimerLock:"
- "setAuthorizationEnabled:"
- "setAuthorizationGroups:"
- "setAuthorizationProvided:"
- "setBody:"
- "setBuddyFlow:"
- "setCacheName:"
- "setCategoryIdentifier:"
- "setCertificateData:keyType:completion:"
- "setClientName:"
- "setConfigurationHost:"
- "setConfigurationManager:"
- "setConfigurationQueue:"
- "setContainerAppBundleIdentifier:"
- "setCreateFirstUserDuringSetupEnabled:"
- "setCreateUserLoginTypes:"
- "setCreateUsersEnabled:"
- "setCredential:type:"
- "setCredentialContext:"
- "setCredentialTransferCompleted:"
- "setData:"
- "setDataVaultInitialized:"
- "setDelegate:"
- "setDeviceConfigurationVersion:"
- "setDeviceEncryptionCertificate:"
- "setDeviceEncryptionKey:"
- "setDeviceKeysShouldChange:"
- "setDeviceRegistrationStatus:"
- "setDeviceSigningCertificate:"
- "setDeviceSigningKey:"
- "setDirectoryServices:"
- "setDistributedNotificationCenter:"
- "setEmbeddedAssertionCertificate:"
- "setEmbeddedAssertionSigningKey:"
- "setEnableNetworkChanges:"
- "setEnableRegistrationDuringSetup:"
- "setEncryptionAlgorithm:"
- "setEncryptionKeyType:"
- "setExchangeRequired:"
- "setExpirationDate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtensionData:"
- "setExtensionIdentifier:"
- "setExtensionManager:"
- "setFailedToConnect:"
- "setFailureCount:"
- "setFilePath:"
- "setFileVaultPolicy:"
- "setForLogin:"
- "setFormatOptions:"
- "setGeneratedUUID:"
- "setGid:"
- "setGroups:forLocalUser:completion:"
- "setGroups:forPlatformSSOUser:completion:"
- "setHomeDirectory:"
- "setHostExtensionContext:"
- "setIcon:"
- "setImportSuccessful:"
- "setInteractionNotAllowed:"
- "setInterruptionHandler:"
- "setInterruptionLevel:"
- "setInvalidationHandler:"
- "setIsSystem:"
- "setJwksCache:forExtensionIdentifier:"
- "setJwksStorageProvider:"
- "setKerberosDelegate:"
- "setKerberosHelper:"
- "setKerberosStatus:"
- "setKeyBag:"
- "setKeyProxies:"
- "setKeyWrap:"
- "setKeychainHelper:"
- "setLastAuthenticationAttempt:"
- "setLastEncryptionKeyChange:"
- "setLastLoginDate:"
- "setLocalizedFallbackTitle:"
- "setLocalizedReason:"
- "setLockHandler:"
- "setLoginConfiguration:completion:"
- "setLoginConfigurationVersion:"
- "setLoginFrequency:"
- "setLoginPolicy:"
- "setLoginQueue:"
- "setLoginType:"
- "setLoginUserName:"
- "setLoginUserName:completion:"
- "setMessageBuffer:"
- "setMigratingDeviceKeys:"
- "setNewPasswordUser:"
- "setNewSecureEnclaveUser:"
- "setNewSmartCardUser:"
- "setNewUserAuthorizationMode:"
- "setNewUserBindingComplete:"
- "setNonPlatformSSOAccounts:"
- "setNotificationCategories:"
- "setNotificationCenter:"
- "setObject:forKeyedSubscript:"
- "setOfflineGracePeriod:"
- "setOptionAuthenticationTitle:"
- "setOptionCallerAuditToken:"
- "setOptionCallerIconPath:"
- "setOptionCallerName:"
- "setOptionFallbackVisible:"
- "setOptions:"
- "setOtherGroups:"
- "setPassword:"
- "setPendingEncryptionAlgorithm:"
- "setPendingEncryptionKey:"
- "setPendingSigningAlgorithm:"
- "setPendingSigningKey:"
- "setPendingUserSEPKey:"
- "setPendingUserSEPSigningAlgorithm:"
- "setPlatformSSOAccount:"
- "setPlatformSSOActive:"
- "setPlatformSSOActiveLock:"
- "setPlatformSSOEnabled:"
- "setProcess:"
- "setProfile:"
- "setProtocolVersion:"
- "setRealm:"
- "setRefreshToken:"
- "setRegisteredBundleIdentifier:"
- "setRegisteredExtensionName:"
- "setRegistrationCompleted:"
- "setRegistrationContext:"
- "setRegistrationFailed:"
- "setRegistrationManager:"
- "setRegistrationToken:"
- "setRegistrationToken:completion:"
- "setRegistrationUI:"
- "setRemoteObjectInterface:"
- "setRepair:"
- "setRequestIdentifier:"
- "setRequireAuthGracePeriod:"
- "setResetKeys:"
- "setRetry:"
- "setRunningInBuddy:"
- "setScreenUnlockLock:"
- "setScreenUnlocked:"
- "setSdkVersionString:"
- "setSepKey:"
- "setServiceName:"
- "setSessionKey:"
- "setSharedDeviceKeys:"
- "setSharedOnly:"
- "setShell:"
- "setShieldLowered:"
- "setShieldLoweredLock:"
- "setShouldBackgroundDefaultAction:"
- "setShouldPreventNotificationDismissalAfterDefaultAction:"
- "setShouldRunConfigurationChangeWhenUnlocked:"
- "setSigningAlgorithm:"
- "setSmartCardHash:"
- "setSmartCardTokenId:"
- "setSsoExtension:"
- "setSsoTokens:"
- "setSsoTokens:completion:"
- "setState:"
- "setSynchronizeProfilePicture:"
- "setSystemAuthPluginProcess:"
- "setTemporarySessionQuickLogin:"
- "setTicketKeyPath:"
- "setTitle:"
- "setTokenHelper:"
- "setTokenToUserMapping:"
- "setTokens:extensionIdentifier:returningError:"
- "setTokens:user:extensionIdentifier:returningError:"
- "setTolerance:"
- "setUid:"
- "setUniqueIdentifier:"
- "setUniqueIdpIdentifier:"
- "setUnlockPolicy:"
- "setUpn:"
- "setUseSharedDeviceKeys:"
- "setUserAuthorizationMode:"
- "setUserConfigurationVersion:"
- "setUserDecryptionCertificate:"
- "setUserDecryptionContext:"
- "setUserDecryptionKeyHash:"
- "setUserGroupManager:"
- "setUserInfo:"
- "setUserIsPlatformSSOUser:"
- "setUserLoginConfiguration:"
- "setUserLoginConfiguration:completion:"
- "setUserName:"
- "setUserNotificationCenter:"
- "setUserNotified:"
- "setUserRegistrationStatus:"
- "setUserSEPKeyInvalid:"
- "setUserSepSigningAlgorithm:"
- "setUserSigningAlgorithm:"
- "setUserTokenStatus:"
- "setUserUnlockCertificate:"
- "setUserUnlockData:"
- "setUserUnlockHash:"
- "setValue:forKey:"
- "setWaitForConnectivity:"
- "setWantsNotificationResponsesDelivered"
- "setWithArray:"
- "setXpcConnection:"
- "set__screenUnlockHandler:"
- "set__shieldLoweredHandler:"
- "set_analytics:"
- "set_credential:"
- "set_loginContext:"
- "set_setupContext:"
- "setupDeviceRegistrationOptions"
- "setupNonUISessionWithCompletion:"
- "setupNotificationCategories"
- "setupTimerForAuthentication"
- "setupUserRegistrationOptions"
- "sharedDeviceKeys"
- "sharedInstance"
- "sharedManager"
- "sharedOnly"
- "shell"
- "shieldLowered"
- "shieldLoweredLock"
- "shortNameForUserName:"
- "shouldRunConfigurationChangeWhenUnlocked"
- "showAlertMessage:messageText:completion:"
- "showAlertWithError:completion:"
- "showRegistrationStatus:"
- "showRegistrationUI"
- "signingAlgorithm"
- "sleepForTimeInterval:"
- "smartCardHash"
- "smartCardTokenId"
- "ssoExtension"
- "ssoMethodToUse:profile:"
- "ssoTokens"
- "ssoTokensWithCompletion:"
- "standardUserDefaults"
- "startAction:forUserName:completion:"
- "startDeviceAction:"
- "startDeviceAction:completion:"
- "startObservingKeyBagLockStatusChanges"
- "startUserAction:forUserName:"
- "state"
- "statusForUser:completion:"
- "statusForUserName:"
- "storeCredentialAndUpdatePasswordHint"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringForDeviceAction:"
- "stringForKey:"
- "stringForKeyType:"
- "stringForLoginResult:"
- "stringForLoginType:"
- "stringForRegistrationStatus:"
- "stringForTokenStatus:"
- "stringForUserAction:"
- "stringFromDate:"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "supportedDeviceEncryptionAlgorithms"
- "supportedDeviceEncryptionAlgorithmsCompletion:"
- "supportedDeviceSigningAlgorithms"
- "supportedDeviceSigningAlgorithmsCompletion:"
- "supportedGrantTypes"
- "supportedGrantTypesCompletion:"
- "supportedUserSecureEnclaveKeySigningAlgorithms"
- "supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:"
- "supportsCreateTemporaryUsers"
- "supportsSecureCoding"
- "supportsTokenUnlock"
- "swift"
- "synchronizeProfilePicture"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemAuthPluginProcess"
- "temporarySessionQuickLogin"
- "ticketKeyPath"
- "timeIntervalSinceNow"
- "tokenEndpointURL"
- "tokenExpiration"
- "tokenHelper"
- "tokenIsAccessKey:"
- "tokenReceived"
- "tokenToUserMapping"
- "tokensForExtensionIdentifier:"
- "tokensForExtensionIdentifier:user:"
- "translatePolicy:"
- "triggerVPNForRealm:"
- "triggerWithTimeInterval:repeats:"
- "unbindTokenForAllUsersWithCompletion:"
- "unbindTokenForUsername:hash:completion:"
- "uniqueIdentifierForUserName:"
- "uniqueIdpIdentifier"
- "unload"
- "unlockPolicy"
- "unwrapBlob:"
- "updateGroupNames:completion:"
- "updateLocalAccountPassword:passwordContext:completion:"
- "updateLocalAccountPassword:passwordContextData:completion:"
- "updateLoginStateForIdentifier:state:loginDate:loginType:completion:"
- "updateLoginStateForUserName:state:loginDate:loginType:"
- "updateProfilePicture:forUsername:completion:"
- "updateRegistrationState:failed:"
- "updateRegistrationState:failed:completion:"
- "updateRegistrationStateFailed:"
- "updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:"
- "updateTriggerFile"
- "updateWithProfile:"
- "upn"
- "useSharedDeviceKeys"
- "useVolume:completion:"
- "userAuthPluginProcess"
- "userAuthorizationMode"
- "userAuthorizationModeWithString:"
- "userConfigurationForIdentifier:completion:"
- "userConfigurationForUserName:"
- "userConfigurationVersion"
- "userDeviceConfiguration"
- "userGroupManager"
- "userIdentifier"
- "userInfo"
- "userIsPlatformSSOUser"
- "userLoginConfigurationWithCompletion:"
- "userLoginStateForIdentifier:completion:"
- "userName"
- "userNeedsReauthenticationWithCompletion:"
- "userNotificationCenter"
- "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
- "userNotificationCenter:openSettingsForNotification:"
- "userNotificationCenter:willPresentNotification:withCompletionHandler:"
- "userNotified"
- "userRegistered"
- "userRegistrationsNeedsRepair"
- "userRegistrationsNeedsRepairWithCompletion:"
- "userSEPKeyBiometricPolicy"
- "userSEPKeyInvalid"
- "userSigningAlgorithm"
- "userSigningAlgorithmToUse:userConfiguration:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"PODeviceRegistrationStatus\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"POLoginConfiguration\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"POUserLoginConfiguration\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q>16"
- "v24@0:8@?<v@?i@\"NSError\">16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?B@\"NSError\">20"
- "v28@0:8q16B24"
- "v32@0:8@\"NSData\"16@\"NSString\"24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"POUserConfiguration\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"POUserLoginState\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"POUserRegistrationStatus\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"POLoginConfiguration\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"POUserLoginConfiguration\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v32@0:8^{__SecCertificate=}16q24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSNumber\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSData\"16q24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?Q@\"NSData\"@\"NSString\"@\"NSArray\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?Q@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"SOAuthorizationCredential\"24@\"NSError\"32"
- "v40@0:8@\"POUserConfiguration\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8B16B20B24B28@32"
- "v40@0:8q16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v44@0:8@\"NSString\"16@\"NSData\"24B32@?<v@?Q@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16@24B32B36B40"
- "v44@0:8q16B24@\"NSData\"28@?<v@?@\"NSArray\"@\"NSError\">36"
- "v44@0:8q16B24@28@?36"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16B24B28B32B36@40"
- "v48@0:8B16B20@24@32^@40"
- "v48@0:8q16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32@?40"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32B40@?<v@?Q@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16i24q28@36@?44"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSDate\"32@\"NSNumber\"40@?<v@?B@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32@40B48B52"
- "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48B52@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32@40B48B52@?56"
- "v64@0:8Q16@24@32@40@48@56"
- "v68@0:8@16B24@28@36@44@52@?60"
- "v76@0:8@16@24@32@40@48B56@60@?68"
- "validatedProfileForPlatformSSO"
- "valueForEntitlement:"
- "valueForKeyPath:"
- "verifyAgentEntitlement"
- "verifyKey:"
- "verifyLoginUserEntitlement"
- "verifyPasswordChangeEntitlement"
- "verifyPasswordLogin:passwordContext:completion:"
- "verifyPasswordUser:passwordContext:completion:"
- "verifyUserAccount:passwordContext:smartCardContext:tokenId:completion:"
- "waitForConnectivity"
- "waitForKeyBagFirstUnlockOnStartupWithCompletion:"
- "waitForKeyBagUnlockWithCompletion:"
- "waitForScreenUnlockithCompletion:"
- "waitForShieldLoweredWithCompletion:"
- "waitForTokenAvailable:"
- "windowDidClose"
- "wrapBlob:"
- "writeData:toPath:saveError:"
- "writeToURL:options:error:"
- "xpcConnection"
- "xpcQueue"
- "zone"

```

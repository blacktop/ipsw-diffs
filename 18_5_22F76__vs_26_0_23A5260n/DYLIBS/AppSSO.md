## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-417.120.4.0.0
-  __TEXT.__text: 0x27cb4
+483.0.6.0.1
+  __TEXT.__text: 0x29038
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x19dc
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x1b8c
-  __TEXT.__cstring: 0x2d95
+  __TEXT.__objc_methlist: 0x1a94
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x1bcc
+  __TEXT.__cstring: 0x2f83
   __TEXT.__dlopen_cstrs: 0x5e4
-  __TEXT.__oslogstring: 0x40f1
-  __TEXT.__unwind_info: 0xce8
+  __TEXT.__oslogstring: 0x4283
+  __TEXT.__unwind_info: 0xd18
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x47f3
-  __TEXT.__objc_methtype: 0x9e3
-  __TEXT.__objc_stubs: 0x3760
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xb98
+  __TEXT.__objc_methname: 0x49e7
+  __TEXT.__objc_methtype: 0xa91
+  __TEXT.__objc_stubs: 0x3800
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xcb0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1100
+  __DATA_CONST.__objc_selrefs: 0x1150
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__objc_const: 0x3f78
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x40a8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x160
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x670
-  __DATA.__bss: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA.__bss: 0x1f8
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47785F0C-AD7B-3EF5-8B67-C16FFB6AA16F
-  Functions: 938
-  Symbols:   3414
-  CStrings:  1603
+  UUID: BE53F2B6-2414-3A97-B6B9-A528FCB62D98
+  Functions: 971
+  Symbols:   3476
+  CStrings:  1645
 
Symbols:
+ +[SOAuthorization canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]
+ +[SOAuthorization canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:].cold.1
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.1
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.2
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.3
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.4
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.5
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.6
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.7
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.8
+ -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]
+ -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:].cold.1
+ -[SOExtension displayNamesForGroups:extensionData:completion:]
+ -[SOExtension presentRegistrationViewControllerWithCompletion:]
+ -[SOExtension profilePictureForUserUsingExtensionData:completion:]
+ -[SOExtension sessionID]
+ -[SOHostExtensionContext presentRegistrationViewControllerWithCompletion:]
+ -[SORemoteExtensionContext displayNamesForGroups:extensionData:completion:]
+ -[SORemoteExtensionContext groupsCompletion]
+ -[SORemoteExtensionContext pictureCompletion]
+ -[SORemoteExtensionContext profilePictureForUserUsingExtensionData:completion:]
+ -[SORemoteExtensionContext setGroupsCompletion:]
+ -[SORemoteExtensionContext setPictureCompletion:]
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table21
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table73
+ GCC_except_table77
+ _OBJC_IVAR_$_SORemoteExtensionContext._groupsCompletion
+ _OBJC_IVAR_$_SORemoteExtensionContext._pictureCompletion
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.115
+ ___119+[SOAuthorization canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke
+ ___119+[SOAuthorization canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_2
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.119
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.119.cold.1
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.118
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.118.cold.1
+ ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.120
+ ___51-[SOExtension _finishAuthorization:withCompletion:]_block_invoke.33
+ ___51-[SOExtension _finishAuthorization:withCompletion:]_block_invoke.cold.1
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.117
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.117.cold.1
+ ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.34
+ ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.38
+ ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.43
+ ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke_2.44
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.116
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.116.cold.1
+ ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.122
+ ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.122.cold.1
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.47
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.47.cold.1
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.66
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.66.cold.1
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.67
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.67.cold.1
+ ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.71
+ ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.124
+ ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.124.cold.1
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.127
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.127.cold.1
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.cold.1
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.cold.2
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.129
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.129.cold.1
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.cold.1
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.cold.2
+ ___72-[SOExtension _connectContextToSessionWithRequestIdentifier:completion:]_block_invoke.49
+ ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.125
+ ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.125.cold.1
+ ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.113
+ ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.126
+ ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.126.cold.1
+ ___93-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
+ ___94-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32r_e37_v24?0"SOConfiguration"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40bs_e16_v16?0"NSData"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e22_v16?0"NSDictionary"8ls40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.121
+ ___block_literal_global.193
+ ___block_literal_global.215
+ ___block_literal_global.58
+ ___getSOClientClass_block_invoke
+ ___getSOClientClass_block_invoke.cold.1
+ _getSOClientClass.softClass
+ _kCFPreferencesAnyUser
+ _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
+ _objc_msgSend$canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:
+ _objc_msgSend$configurationWithCompletion:
+ _objc_msgSend$displayNamesForGroups:extensionData:completion:
+ _objc_msgSend$presentRegistrationViewControllerWithCompletion:
+ _objc_msgSend$profilePictureForUserUsingExtensionData:completion:
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:]
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.1
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.2
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.3
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.4
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.5
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.6
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:].cold.7
- -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:completion:]
- -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:completion:].cold.1
- GCC_except_table109
- GCC_except_table110
- GCC_except_table24
- GCC_except_table38
- GCC_except_table39
- GCC_except_table47
- GCC_except_table51
- GCC_except_table56
- GCC_except_table58
- GCC_except_table70
- GCC_except_table74
- ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.103
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.107
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.107.cold.1
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.106
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.106.cold.1
- ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.108
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.105
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.105.cold.1
- ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.32
- ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.37
- ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke.42
- ___52-[SOAuthorization beginAuthorizationWithParameters:]_block_invoke_2.43
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.104
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.104.cold.1
- ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.110
- ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.110.cold.1
- ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.64
- ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.64.cold.1
- ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.65
- ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.65.cold.1
- ___60-[SOAuthorization _finishAuthorizationWithCredential:error:]_block_invoke.69
- ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.112
- ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.112.cold.1
- ___72-[SOExtension _connectContextToSessionWithRequestIdentifier:completion:]_block_invoke.37
- ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.113
- ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.113.cold.1
- ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.101
- ___78-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:completion:]_block_invoke
- ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.114
- ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.114.cold.1
- ___block_literal_global.115
- ___block_literal_global.177
- ___block_literal_global.214
- ___block_literal_global.55
- _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:completion:
CStrings:
+ "-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]"
+ "-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]"
+ "-[SOExtension displayNamesForGroups:extensionData:completion:]"
+ "-[SOExtension profilePictureForUserUsingExtensionData:completion:]"
+ "-[SORemoteExtensionContext displayNamesForGroups:extensionData:completion:]"
+ "-[SORemoteExtensionContext profilePictureForUserUsingExtensionData:completion:]"
+ "Calling displayNamesForGroups on extension"
+ "Calling profilePictureForUser on extension"
+ "Finished displayNamesForGroups"
+ "Finished profilePictureForUser"
+ "Loading SSO extension"
+ "No extension session ID => not calling finishAuthorizationWithCompletion on extension"
+ "No extension session ID."
+ "Presenting registration view controller not allowed."
+ "SOClient"
+ "T@\"NSUUID\",R,N"
+ "T@?,C,V_groupsCompletion"
+ "T@?,C,V_pictureCompletion"
+ "_groupsCompletion"
+ "_isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:"
+ "_pictureCompletion"
+ "canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:"
+ "configurationWithCompletion:"
+ "displayNamesForGroups:extensionData:completion:"
+ "extension PSSO API displayNamesForGroups is not implemented in extension"
+ "extension PSSO API profilePictureForUser is not implemented in extension"
+ "groupsCompletion"
+ "isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:"
+ "pictureCompletion"
+ "platform sso"
+ "presentRegistrationViewControllerWithCompletion:"
+ "profilePictureForUserUsingExtensionData:completion:"
+ "sessionID"
+ "setGroupsCompletion:"
+ "setPictureCompletion:"
+ "v16@?0@\"NSData\"8"
+ "v16@?0@\"NSDictionary\"8"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@?0@\"SOConfiguration\"8@\"NSError\"16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\">24"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
+ "v52@0:8@16q24@32B40@?44"
- "-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:completion:]"
- "-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:completion:]"
- "_isConfigurationActiveForExtensionIdentifier:completion:"
- "isConfigurationActiveForExtensionIdentifier:completion:"

```

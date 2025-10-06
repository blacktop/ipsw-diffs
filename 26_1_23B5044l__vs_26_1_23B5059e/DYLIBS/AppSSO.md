## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-483.40.9.0.0
-  __TEXT.__text: 0x29740
-  __TEXT.__auth_stubs: 0x690
+483.40.13.0.0
+  __TEXT.__text: 0x298bc
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x1a94
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x1be8
-  __TEXT.__cstring: 0x30f4
+  __TEXT.__cstring: 0x313b
   __TEXT.__dlopen_cstrs: 0x638
-  __TEXT.__oslogstring: 0x4291
+  __TEXT.__oslogstring: 0x42f6
   __TEXT.__unwind_info: 0xd20
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x4b6c
+  __TEXT.__objc_methname: 0x4b9a
   __TEXT.__objc_methtype: 0xa91
-  __TEXT.__objc_stubs: 0x3a20
-  __DATA_CONST.__got: 0x220
+  __TEXT.__objc_stubs: 0x3a40
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11d8
+  __DATA_CONST.__objc_selrefs: 0x11e0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__cfstring: 0x11e0
   __AUTH_CONST.__objc_const: 0x40a8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x670
-  __DATA.__bss: 0x218
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 390A0C7B-3E06-37A8-BD0F-D6213295E02A
-  Functions: 977
-  Symbols:   3511
-  CStrings:  1695
+  UUID: 11783B30-2AE8-347C-B833-C215B6725B14
+  Functions: 978
+  Symbols:   3518
+  CStrings:  1702
 
Symbols:
+ -[SOExtension checkAssociatedDomainsWithCache:].cold.5
+ -[SOExtension checkAssociatedDomainsWithCompletion:].cold.7
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.122
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.126
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.126.cold.1
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.125
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.125.cold.1
+ ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.127
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.124
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.124.cold.1
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.123
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.123.cold.1
+ ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.129
+ ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.129.cold.1
+ ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.131
+ ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.131.cold.1
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.134
+ ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.134.cold.1
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.136
+ ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.136.cold.1
+ ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.132
+ ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.132.cold.1
+ ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.120
+ ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.133
+ ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.133.cold.1
+ _objc_msgSend$postNotificationName:object:userInfo:options:
+ _objc_retain_x27
- ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.115
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.119
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.119.cold.1
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.118
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.118.cold.1
- ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.120
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.117
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.117.cold.1
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.116
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.116.cold.1
- ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.122
- ___58-[SOExtension supportedDeviceSigningAlgorithmsCompletion:]_block_invoke.122.cold.1
- ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.124
- ___61-[SOExtension supportedDeviceEncryptionAlgorithmsCompletion:]_block_invoke.124.cold.1
- ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.127
- ___62-[SOExtension displayNamesForGroups:extensionData:completion:]_block_invoke.127.cold.1
- ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.129
- ___66-[SOExtension profilePictureForUserUsingExtensionData:completion:]_block_invoke.129.cold.1
- ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.125
- ___72-[SOExtension supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:]_block_invoke.125.cold.1
- ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.113
- ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.126
- ___81-[SOExtension keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:]_block_invoke.126.cold.1
Functions:
~ -[SOExtension checkAssociatedDomainsWithCache:] : 1764 -> 1816
~ -[SOExtension checkAssociatedDomainsWithCompletion:] : 1272 -> 1496
~ -[SOExtension checkAssociatedDomainsWithCompletion:].cold.6 : 180 -> 104
+ -[SOExtension checkAssociatedDomainsWithCompletion:].cold.7
CStrings:
+ "Associated domain: Notify swcd"
+ "Associated domain: failed to get extension bundle at path: %{public}@"
+ "CP_SharedWebCredentialsDidChangeNotification"
+ "Failed to find bundle URL"
+ "postNotificationName:object:userInfo:options:"

```

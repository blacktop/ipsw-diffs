## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.40.9.0.0
-  __TEXT.__text: 0x59300
+483.40.13.0.0
+  __TEXT.__text: 0x594c8
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x32d4
-  __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x80b6
-  __TEXT.__oslogstring: 0x22e1
+  __TEXT.__objc_methlist: 0x32e4
+  __TEXT.__const: 0x28a
+  __TEXT.__cstring: 0x8106
+  __TEXT.__oslogstring: 0x2301
   __TEXT.__gcc_except_tab: 0x1528
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2

   __TEXT.__unwind_info: 0x1530
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9d79
+  __TEXT.__objc_methname: 0x9d9d
   __TEXT.__objc_methtype: 0x151a
   __TEXT.__objc_stubs: 0x6f60
   __DATA_CONST.__got: 0x430

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2218
+  __DATA_CONST.__objc_selrefs: 0x2220
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__cfstring: 0x3880
   __AUTH_CONST.__objc_const: 0x81d0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0x9b0
   __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x620
   __DATA.__bss: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A72899CC-E3B8-31BD-8DFE-839D24C25073
-  Functions: 2051
-  Symbols:   7248
-  CStrings:  3150
+  UUID: 0A1F4D6F-151E-369B-A18F-F5BF102FCEFD
+  Functions: 2054
+  Symbols:   7254
+  CStrings:  3156
 
Symbols:
+ -[PORegistrationManager createUserConfigurationForBuddyUser]
+ GCC_except_table102
+ GCC_except_table111
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.132
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.132.cold.1
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.138
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.138.cold.1
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.144
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.144.cold.1
+ ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.150
+ ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.111
+ ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.111.cold.1
+ ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.117
+ ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.117.cold.1
+ ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.124
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.191
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.191.cold.1
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.197
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.197.cold.1
+ ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.203
+ ___52-[PORegistrationManager finishRegistrationWithRetry]_block_invoke.103
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.205
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.205.cold.1
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.211
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.211.cold.1
+ ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.217
+ ___60-[PORegistrationManager createUserConfigurationForBuddyUser]_block_invoke
+ ___60-[PORegistrationManager createUserConfigurationForBuddyUser]_block_invoke.cold.1
+ ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.73
+ ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.73.cold.1
+ ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.63
+ ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.63.cold.1
+ ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.182
+ ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.182.cold.1
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.165
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.165.cold.1
+ ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.171
+ ___block_literal_global.155
+ ___block_literal_global.219
+ ___block_literal_global.479
- GCC_except_table100
- GCC_except_table109
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.124
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.124.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.130
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.130.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.136
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.136.cold.1
- ___112-[PORegistrationManager handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.142
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.103
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.103.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.109
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.109.cold.1
- ___116-[PORegistrationManager handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.116
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.183
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.183.cold.1
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.189
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.189.cold.1
- ___47-[PORegistrationManager retrieveProfilePicture]_block_invoke.195
- ___52-[PORegistrationManager finishRegistrationWithRetry]_block_invoke.95
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.197
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.197.cold.1
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.203
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.203.cold.1
- ___53-[PORegistrationManager requestDidCompleteWithError:]_block_invoke.209
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.65
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke.65.cold.1
- ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.55
- ___64-[PORegistrationManager cleanupUserConfigAfterMigrationToShared]_block_invoke.55.cold.1
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.174
- ___70-[PORegistrationManager saveSSOTokens:toKeychainUsingContext:tokenId:]_block_invoke.174.cold.1
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.157
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.157.cold.1
- ___72-[PORegistrationManager handleRegistrationViewControllerWithCompletion:]_block_invoke.163
- ___block_literal_global.118
- ___block_literal_global.147
- ___block_literal_global.211
- ___block_literal_global.470
CStrings:
+ "Creating setup user configuration"
+ "Failed to save setup user configuration during user registration."
+ "_mbsetupuser"
+ "createUserConfigurationForBuddyUser"

```

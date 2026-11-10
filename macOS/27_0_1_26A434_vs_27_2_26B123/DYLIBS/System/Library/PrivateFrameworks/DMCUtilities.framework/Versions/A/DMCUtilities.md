## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x30558
-  __TEXT.__objc_methlist: 0x2b7c
+113.40.20.0.0
+  __TEXT.__text: 0x30c08
+  __TEXT.__objc_methlist: 0x2c44
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x490
-  __TEXT.__cstring: 0x304c
-  __TEXT.__oslogstring: 0x4b74
+  __TEXT.__cstring: 0x30dc
+  __TEXT.__oslogstring: 0x4b9b
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xc88
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f8
+  __DATA_CONST.__objc_selrefs: 0x2270
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x1720
-  __AUTH_CONST.__cfstring: 0x3b40
-  __AUTH_CONST.__objc_const: 0x4330
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__got: 0x658
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x3bc0
+  __AUTH_CONST.__objc_const: 0x44e0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0xd98
+  __AUTH.__objc_data: 0xe88
   __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x2e8
-  __DATA.__bss: 0x5c0
+  __DATA.__bss: 0x5e0
   __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1310
-  Symbols:   3337
-  CStrings:  890
+  Functions: 1329
+  Symbols:   3393
+  CStrings:  894
 
Symbols:
+ +[DMCAccountUtilities hasUserAccountsOfTypes:]
+ +[DMCAppNetworkAccessCheck _stateForBundleID:]
+ +[DMCAppNetworkAccessCheck allCapabilities]
+ +[DMCAppNetworkAccessCheck appBundleIdentifierForCapability:]
+ +[DMCAppNetworkAccessCheck displayNameForBundleIdentifier:]
+ +[DMCAppNetworkAccessCheck stateForCapability:]
+ +[DMCDeviceEligibility isEligibleForNoninteractiveEnhancedLogCollection]
+ +[DMCDeviceEligibility userAccountTypeIdentifiersForNoninteractiveEnhancedLogCollection]
+ +[DMCLockdownUtilities isDevicePasscodeSet]
+ +[DMCRatchet isAuthorizedForOperation:policy:completion:]
+ -[ACAccountStore(DeviceManagementClient) _dmc_accountsWithType:error:criteria:]
+ -[ACAccountStore(DeviceManagementClient) _dmc_logConflictingAccounts:matchedOn:value:]
+ -[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]
+ -[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithUsername:error:]
+ AppleMediaServicesBundle.onceToken
+ AppleMediaServicesBundle.retval
+ DMCEnsureAppleMediaServicesLoaded
+ MDMMigrationConfigFetchRetryInfoFilePath
+ MDMMigrationConfigFetchRetryInfoFilePath.once
+ MDMMigrationConfigFetchRetryInfoFilePath.str
+ _ACAccountTypeIdentifierCalDAV
+ _ACAccountTypeIdentifierCardDAV
+ _ACAccountTypeIdentifierExchange
+ _ACAccountTypeIdentifierGmail
+ _ACAccountTypeIdentifierHotmail
+ _ACAccountTypeIdentifierIMAP
+ _ACAccountTypeIdentifierIMAPMail
+ _ACAccountTypeIdentifierIMAPNotes
+ _ACAccountTypeIdentifierPOP
+ _ACAccountTypeIdentifierYahoo
+ _DMCEnsureAppleMediaServicesLoaded
+ _MDMMigrationConfigFetchRetryInfoFilePath
+ _OBJC_CLASS_$_DMCAppNetworkAccessCheck
+ _OBJC_CLASS_$_DMCDeviceEligibility
+ _OBJC_CLASS_$_DMCLockdownUtilities
+ _OBJC_METACLASS_$_DMCAppNetworkAccessCheck
+ _OBJC_METACLASS_$_DMCDeviceEligibility
+ _OBJC_METACLASS_$_DMCLockdownUtilities
+ __OBJC_$_CLASS_METHODS_DMCAccountUtilities
+ __OBJC_$_CLASS_METHODS_DMCAppNetworkAccessCheck
+ __OBJC_$_CLASS_METHODS_DMCDeviceEligibility
+ __OBJC_$_CLASS_METHODS_DMCLockdownUtilities
+ __OBJC_CLASS_RO_$_DMCAppNetworkAccessCheck
+ __OBJC_CLASS_RO_$_DMCDeviceEligibility
+ __OBJC_CLASS_RO_$_DMCLockdownUtilities
+ __OBJC_METACLASS_RO_$_DMCAppNetworkAccessCheck
+ __OBJC_METACLASS_RO_$_DMCDeviceEligibility
+ __OBJC_METACLASS_RO_$_DMCLockdownUtilities
+ ___83-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]_block_invoke
+ ___83-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]_block_invoke_2
+ ___84-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithUsername:error:]_block_invoke
+ ___AppleMediaServicesBundle_block_invoke
+ ___AppleMediaServicesBundle_block_invoke_2
+ ___MDMMigrationConfigFetchRetryInfoFilePath_block_invoke
+ _objc_msgSend$_dmc_accountsWithType:error:criteria:
+ _objc_msgSend$_dmc_logConflictingAccounts:matchedOn:value:
+ _objc_msgSend$_stateForBundleID:
+ _objc_msgSend$ams_isLocalAccount
+ _objc_msgSend$appBundleIdentifierForCapability:
+ _objc_msgSend$dmc_conflictingAccountsWithAltDSID:error:
+ _objc_msgSend$dmc_conflictingAccountsWithUsername:error:
+ _objc_msgSend$owningBundleID
- +[DMCRatchet isAuthorizedForOperation:completion:]
- GCC_except_table35
- __89-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithUsername:error:]_block_invoke
- ___88-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithAltDSID:error:]_block_invoke
- ___88-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithAltDSID:error:]_block_invoke_2
- ___89-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithUsername:error:]_block_invoke
CStrings:
+ "/System/Library/PrivateFrameworks/AppleMediaServices.framework"
+ "Conflicting account with %{public}@ (%{public}@) exists (%lu total). Identifier: %@, type: %{public}@, owning bundle ID: %{public}@, primary: %d"
+ "Failed to fetch accounts to determine user-data presence: %{public}@"
+ "MDMMigrationConfigFetchRetryInfo.plist"
+ "com.apple.AppStore"
+ "com.apple.mobilesafari"
- "Conflicting account with altDSID (%{public}@) exists. Identifier: %@, type: %{public}@"
- "Conflicting account with username (%{public}@) exists. Identifier: %@, type: %{public}@"
```

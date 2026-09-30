## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x2f0a0
-  __TEXT.__objc_methlist: 0x2b7c
+113.40.17.0.0
+  __TEXT.__text: 0x2f48c
+  __TEXT.__objc_methlist: 0x2bcc
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x490
-  __TEXT.__cstring: 0x304c
-  __TEXT.__oslogstring: 0x4b74
+  __TEXT.__cstring: 0x30b2
+  __TEXT.__oslogstring: 0x4bb9
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1040
+  __TEXT.__unwind_info: 0x1058
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f8
+  __DATA_CONST.__objc_selrefs: 0x2220
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x1720
-  __AUTH_CONST.__cfstring: 0x3b40
-  __AUTH_CONST.__objc_const: 0x4330
+  __DATA_CONST.__got: 0x658
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0x4450
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH.__objc_data: 0xd98
+  __AUTH.__objc_data: 0xe38
   __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x2e8
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1310
-  Symbols:   3337
-  CStrings:  890
+  Functions: 1320
+  Symbols:   3373
+  CStrings:  893
 
Symbols:
+ +[DMCAccountUtilities hasUserAccountsOfTypes:]
+ +[DMCDeviceEligibility isEligibleForNoninteractiveEnhancedLogCollection]
+ +[DMCDeviceEligibility userAccountTypeIdentifiersForNoninteractiveEnhancedLogCollection]
+ +[DMCLockdownUtilities isDevicePasscodeSet]
+ AppleMediaServicesBundle.onceToken
+ AppleMediaServicesBundle.retval
+ DMCEnsureAppleMediaServicesLoaded
+ GCC_except_table34
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
+ _OBJC_CLASS_$_DMCDeviceEligibility
+ _OBJC_CLASS_$_DMCLockdownUtilities
+ _OBJC_METACLASS_$_DMCDeviceEligibility
+ _OBJC_METACLASS_$_DMCLockdownUtilities
+ __OBJC_$_CLASS_METHODS_DMCAccountUtilities
+ __OBJC_$_CLASS_METHODS_DMCDeviceEligibility
+ __OBJC_$_CLASS_METHODS_DMCLockdownUtilities
+ __OBJC_CLASS_RO_$_DMCDeviceEligibility
+ __OBJC_CLASS_RO_$_DMCLockdownUtilities
+ __OBJC_METACLASS_RO_$_DMCDeviceEligibility
+ __OBJC_METACLASS_RO_$_DMCLockdownUtilities
+ ___AppleMediaServicesBundle_block_invoke
+ ___AppleMediaServicesBundle_block_invoke_2
+ ___MDMMigrationConfigFetchRetryInfoFilePath_block_invoke
+ _objc_msgSend$ams_isLocalAccount
- GCC_except_table35
- __89-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithUsername:error:]_block_invoke
CStrings:
+ "/System/Library/PrivateFrameworks/AppleMediaServices.framework"
+ "Failed to fetch accounts to determine user-data presence: %{public}@"
+ "MDMMigrationConfigFetchRetryInfo.plist"
```

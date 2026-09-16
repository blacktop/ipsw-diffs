## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-113.2.5.0.0
-  __TEXT.__text: 0x34f10
-  __TEXT.__objc_methlist: 0x2fbc
+113.40.17.0.0
+  __TEXT.__text: 0x352e0
+  __TEXT.__objc_methlist: 0x3004
   __TEXT.__const: 0x1a8
   __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__cstring: 0x3b06
-  __TEXT.__oslogstring: 0x5a2f
+  __TEXT.__cstring: 0x3b2d
+  __TEXT.__oslogstring: 0x5a74
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0x12e8
+  __TEXT.__unwind_info: 0x1300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26b0
+  __DATA_CONST.__objc_selrefs: 0x26d0
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x6b8
-  __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__cfstring: 0x4440
-  __AUTH_CONST.__objc_const: 0x4520
+  __DATA_CONST.__got: 0x710
+  __AUTH_CONST.__const: 0xd00
+  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__objc_const: 0x4640
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH.__objc_data: 0xf00
+  __AUTH.__objc_data: 0xfa0
   __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x300
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1433
-  Symbols:   3630
-  CStrings:  1042
+  Functions: 1441
+  Symbols:   3662
+  CStrings:  1044
 
Symbols:
+ +[DMCAccountUtilities hasUserAccountsOfTypes:]
+ +[DMCDeviceEligibility isEligibleForNoninteractiveEnhancedLogCollection]
+ +[DMCDeviceEligibility userAccountTypeIdentifiersForNoninteractiveEnhancedLogCollection]
+ +[DMCLockdownUtilities isDevicePasscodeSet]
+ GCC_except_table32
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
+ _AppleMediaServicesBundle
+ _DMCEnsureAppleMediaServicesLoaded
+ _MDMMigrationConfigFetchRetryInfoFilePath
+ _MDMMigrationConfigFetchRetryInfoFilePath.once
+ _MDMMigrationConfigFetchRetryInfoFilePath.str
+ _OBJC_CLASS_$_DMCDeviceEligibility
+ _OBJC_CLASS_$_DMCLockdownUtilities
+ _OBJC_METACLASS_$_DMCDeviceEligibility
+ _OBJC_METACLASS_$_DMCLockdownUtilities
+ __OBJC_$_CLASS_METHODS_DMCDeviceEligibility
+ __OBJC_$_CLASS_METHODS_DMCLockdownUtilities
+ __OBJC_CLASS_RO_$_DMCDeviceEligibility
+ __OBJC_CLASS_RO_$_DMCLockdownUtilities
+ __OBJC_METACLASS_RO_$_DMCDeviceEligibility
+ __OBJC_METACLASS_RO_$_DMCLockdownUtilities
+ ___MDMMigrationConfigFetchRetryInfoFilePath_block_invoke
+ ___block_descriptor_65_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ _objc_msgSend$ams_isLocalAccount
+ _objc_msgSend$hasUserAccountsOfTypes:
+ _objc_msgSend$initWithAuthenticationResults:presentingViewController:options:
+ _objc_msgSend$isDevicePasscodeSet
+ _objc_msgSend$userAccountTypeIdentifiersForNoninteractiveEnhancedLogCollection
- GCC_except_table33
- ___89-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithUsername:error:]_block_invoke_2
- ___block_descriptor_81_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- _objc_msgSend$initWithAccount:presentingViewController:options:
- _objc_msgSend$setAltDSID:
CStrings:
+ "Failed to fetch accounts to determine user-data presence: %{public}@"
+ "MDMMigrationConfigFetchRetryInfo.plist"
```

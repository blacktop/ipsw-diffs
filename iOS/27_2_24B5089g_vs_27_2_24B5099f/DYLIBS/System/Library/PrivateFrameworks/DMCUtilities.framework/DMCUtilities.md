## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-113.40.17.0.0
-  __TEXT.__text: 0x352e0
-  __TEXT.__objc_methlist: 0x3004
-  __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__cstring: 0x3b2d
-  __TEXT.__oslogstring: 0x5a74
+113.40.20.0.0
+  __TEXT.__text: 0x35f88
+  __TEXT.__objc_methlist: 0x309c
+  __TEXT.__const: 0x1b8
+  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__cstring: 0x3b61
+  __TEXT.__oslogstring: 0x5bf5
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0x1300
+  __TEXT.__unwind_info: 0x1350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26d0
+  __DATA_CONST.__objc_selrefs: 0x2790
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x710
+  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0xd00
-  __AUTH_CONST.__cfstring: 0x4460
-  __AUTH_CONST.__objc_const: 0x4640
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__cfstring: 0x44a0
+  __AUTH_CONST.__objc_const: 0x46d0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0xfa0
   __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x300
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA.__data: 0x2f9
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1441
-  Symbols:   2841
-  CStrings:  1044
+  Functions: 1460
+  Symbols:   2863
+  CStrings:  1052
 
Symbols:
+ +[DMCAppNetworkAccessCheck _stateForBundleID:]
+ +[DMCAppNetworkAccessCheck _stateForPolicy:]
+ +[DMCAppNetworkAccessCheck allCapabilities]
+ +[DMCAppNetworkAccessCheck appBundleIdentifierForCapability:]
+ +[DMCAppNetworkAccessCheck displayNameForBundleIdentifier:]
+ +[DMCAppNetworkAccessCheck stateForCapability:]
+ +[DMCRatchet _armRatchetForOperation:completion:]
+ +[DMCRatchet _requireBiometricsForOperation:completion:]
+ +[DMCRatchet _responseForPolicy:result:error:]
+ +[DMCRatchet isAuthorizedForOperation:policy:completion:]
+ -[ACAccountStore(DeviceManagementClient) _dmc_accountsWithType:error:criteria:]
+ -[ACAccountStore(DeviceManagementClient) _dmc_logConflictingAccounts:matchedOn:value:]
+ -[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]
+ -[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithUsername:error:]
+ _OBJC_CLASS_$_DMCAppNetworkAccessCheck
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_METACLASS_$_DMCAppNetworkAccessCheck
+ __OBJC_$_CLASS_METHODS_DMCAppNetworkAccessCheck
+ __OBJC_CLASS_RO_$_DMCAppNetworkAccessCheck
+ __OBJC_METACLASS_RO_$_DMCAppNetworkAccessCheck
+ ___49+[DMCRatchet _armRatchetForOperation:completion:]_block_invoke
+ ___56+[DMCRatchet _requireBiometricsForOperation:completion:]_block_invoke
+ ___83-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]_block_invoke
+ ___83-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithAltDSID:error:]_block_invoke_2
+ ___84-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsWithUsername:error:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
+ ___getLAContextClass_block_invoke
+ _getLAContextClass
+ _getLAContextClass.softClass
- +[DMCRatchet _responseFromRatchetResult:error:]
- +[DMCRatchet isAuthorizedForOperation:completion:]
- GCC_except_table32
- ___50+[DMCRatchet isAuthorizedForOperation:completion:]_block_invoke
- ___88-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithAltDSID:error:]_block_invoke
- ___88-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithAltDSID:error:]_block_invoke_2
- ___89-[ACAccountStore(DeviceManagementClient) dmc_conflictingAccountsExistWithUsername:error:]_block_invoke
CStrings:
+ "App network access policy for %{public}@. Cellular: %ld, Wi-Fi: %ld, satellite: %ld, managed: %d, restricted: %d"
+ "Conflicting account with %{public}@ (%{public}@) exists (%lu total). Identifier: %@, type: %{public}@, owning bundle ID: %{public}@, primary: %d"
+ "DMCRatchet is authorized because LAContext is unavailable"
+ "Failed to load record for app: %{public}@ with error: %{public}@."
+ "LAContext"
+ "No app network access policy exists for %{public}@ yet."
+ "No app network access policy returned for %{public}@."
+ "Unable to read app network access policy for %{public}@: %{public}@"
+ "com.apple.AppStore"
+ "com.apple.mobilesafari"
- "Conflicting account with altDSID (%{public}@) exists. Identifier: %@, type: %{public}@"
- "Conflicting account with username (%{public}@) exists. Identifier: %@, type: %{public}@"
```

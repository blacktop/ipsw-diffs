## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-113.40.17.0.0
-  __TEXT.__text: 0x2c690
-  __TEXT.__objc_methlist: 0x1d74
-  __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x47ab
-  __TEXT.__cstring: 0x27e8
-  __TEXT.__gcc_except_tab: 0x8e4
+113.40.20.0.0
+  __TEXT.__text: 0x2cd64
+  __TEXT.__objc_methlist: 0x1da4
+  __TEXT.__const: 0x108
+  __TEXT.__oslogstring: 0x48d6
+  __TEXT.__cstring: 0x28d5
+  __TEXT.__gcc_except_tab: 0x904
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0xc30
+  __TEXT.__unwind_info: 0xc50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1498
+  __DATA_CONST.__const: 0x14a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d80
+  __DATA_CONST.__objc_selrefs: 0x1db8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x578
+  __DATA_CONST.__objc_arraydata: 0x588
   __DATA_CONST.__got: 0x4e0
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x1a80
   __AUTH_CONST.__objc_const: 0x2060
-  __AUTH_CONST.__objc_intobj: 0xb70
+  __AUTH_CONST.__objc_intobj: 0xb88
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x1a8
-  __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__data: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 870
-  Symbols:   1519
-  CStrings:  624
+  Functions: 878
+  Symbols:   1530
+  CStrings:  634
 
Symbols:
+ -[DMCEnrollmentFlowController _ensureAppNetworkAccessWithEnrollmentMethod:essoDetails:]
+ -[DMCEnrollmentFlowController(Utilities) _duplicateAccountErrorForConflictingAccounts:]
+ -[DMCEnrollmentFlowController(Utilities) _requiresAppNetworkAccessConsent]
+ -[DMCEnrollmentFlowController(Utilities) _signOutFromAppBundleIDs]
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table114
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table146
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table179
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table226
+ GCC_except_table233
+ GCC_except_table24
+ GCC_except_table265
+ GCC_except_table52
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table78
+ GCC_except_table83
+ GCC_except_table87
+ _DMCIsGreenTea
+ ___66-[DMCEnrollmentFlowController(Utilities) _signOutFromAppBundleIDs]_block_invoke
+ ___87-[DMCEnrollmentFlowController _ensureAppNetworkAccessWithEnrollmentMethod:essoDetails:]_block_invoke
+ ___87-[DMCEnrollmentFlowController _ensureAppNetworkAccessWithEnrollmentMethod:essoDetails:]_block_invoke_2
+ __signOutFromAppBundleIDs.bundleIDs
+ __signOutFromAppBundleIDs.onceToken
- GCC_except_table100
- GCC_except_table104
- GCC_except_table111
- GCC_except_table116
- GCC_except_table121
- GCC_except_table130
- GCC_except_table137
- GCC_except_table147
- GCC_except_table154
- GCC_except_table155
- GCC_except_table160
- GCC_except_table162
- GCC_except_table176
- GCC_except_table20
- GCC_except_table203
- GCC_except_table213
- GCC_except_table220
- GCC_except_table227
- GCC_except_table262
- GCC_except_table63
- GCC_except_table69
- GCC_except_table77
- GCC_except_table8
- GCC_except_table84
CStrings:
+ "-[DMCEnrollmentFlowController _ensureAppNetworkAccessWithEnrollmentMethod:essoDetails:]_block_invoke_2"
+ "App network access check complete. Continuing: %d"
+ "Checking app network access for capabilities: 0x%lx"
+ "DMC_DUPLICATE_ACCOUNT_EXISTS_IN_APP_%@_%@"
+ "EnsureAppNetworkAccess"
+ "Not checking app network access. This device does not gate app network access behind user consent."
+ "Not checking app network access. This enrollment does not depend on any app reaching the network."
+ "com.apple.MobileAddressBook"
+ "com.apple.mobilecal"
+ "com.apple.mobilemail"
```

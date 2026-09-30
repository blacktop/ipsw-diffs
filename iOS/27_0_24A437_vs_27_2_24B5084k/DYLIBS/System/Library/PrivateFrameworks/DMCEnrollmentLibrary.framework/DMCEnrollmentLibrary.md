## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-113.2.5.0.0
-  __TEXT.__text: 0x2b7f0
-  __TEXT.__objc_methlist: 0x1d1c
+113.40.17.0.0
+  __TEXT.__text: 0x2c690
+  __TEXT.__objc_methlist: 0x1d74
   __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x46a2
-  __TEXT.__cstring: 0x278f
-  __TEXT.__gcc_except_tab: 0x880
-  __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__oslogstring: 0x47ab
+  __TEXT.__cstring: 0x27e8
+  __TEXT.__gcc_except_tab: 0x8e4
+  __TEXT.__dlopen_cstrs: 0x104
+  __TEXT.__unwind_info: 0xc30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x13a8
+  __DATA_CONST.__const: 0x1498
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d38
+  __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x558
+  __DATA_CONST.__objc_arraydata: 0x578
   __DATA_CONST.__got: 0x4e0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x2030
-  __AUTH_CONST.__objc_intobj: 0xb28
-  __AUTH_CONST.__objc_arrayobj: 0x4e0
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x2060
+  __AUTH_CONST.__objc_intobj: 0xb70
+  __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 854
-  Symbols:   2349
-  CStrings:  617
+  Functions: 870
+  Symbols:   2384
+  CStrings:  624
 
Symbols:
+ +[DMCEnrollmentFlowController(Utilities) _createSignInErrorFromError:]
+ -[DMCEnrollmentFlowController _checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:]
+ -[DMCEnrollmentFlowController _checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:]
+ -[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]
+ -[DMCEnrollmentFlowController requiredAppID]
+ -[DMCEnrollmentFlowController setRequiredAppID:]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_displayManagementDetailsSteps]
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table176
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table262
+ _AppleAccountLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._requiredAppID
+ ___100-[DMCEnrollmentFlowController _checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:]_block_invoke
+ ___100-[DMCEnrollmentFlowController _checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:]_block_invoke_2
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_2
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_3
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_4
+ ___94-[DMCEnrollmentFlowController _checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:]_block_invoke
+ ___94-[DMCEnrollmentFlowController _checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:]_block_invoke_2
+ ___AppleAccountLibraryCore_block_invoke
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e23_v24?0B8B12"NSError"16lw40l8s32l8
+ ___block_descriptor_74_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ _audit_stringAppleAccount
+ _objc_msgSend$_ADxE_ESSO_displayManagementDetailsSteps
+ _objc_msgSend$_checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:
+ _objc_msgSend$_checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:
+ _objc_msgSend$_createSignInErrorFromError:
+ _objc_msgSend$_presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:
+ _objc_msgSend$aa_isTermsOfServiceUpdateRequired
+ _objc_msgSend$requestRemovalOfExistingApplicationForReason:iTunesStoreID:allowSkip:completionHandler:
+ _objc_msgSend$requiredAppID
+ _objc_msgSend$setRequiredAppID:
- GCC_except_table149
- GCC_except_table151
- GCC_except_table165
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table202
- GCC_except_table212
- GCC_except_table216
- GCC_except_table219
- GCC_except_table251
- GCC_except_table47
- _objc_msgSend$_appNameWithBundleID:
- _objc_msgSend$_createEnterpriseApplicationExistsErrorWithAppName:
CStrings:
+ "CheckExistingESSOApplication"
+ "CheckExistingRequiredApplication"
+ "DMC_MAA_TERMS_NOT_ACCEPTED"
+ "Failed to fetch bundle IDs while checking for an existing Enrollment SSO app: %{public}@"
+ "Failed to fetch bundle IDs while checking for an existing required app, skipping removal prompt: %{public}@"
+ "Required app matches ESSO app, skipping required-app removal prompt"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
```

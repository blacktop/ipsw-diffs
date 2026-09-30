## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/Versions/A/DMCEnrollmentLibrary`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x29e68
-  __TEXT.__objc_methlist: 0x1adc
+113.40.17.0.0
+  __TEXT.__text: 0x2a6d0
+  __TEXT.__objc_methlist: 0x1b34
   __TEXT.__const: 0xf8
   __TEXT.__oslogstring: 0x3f11
-  __TEXT.__cstring: 0x24af
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0xb38
+  __TEXT.__cstring: 0x255d
+  __TEXT.__gcc_except_tab: 0x7d0
+  __TEXT.__dlopen_cstrs: 0xa2
+  __TEXT.__unwind_info: 0xb78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ae0
+  __DATA_CONST.__objc_selrefs: 0x1b28
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x548
+  __DATA_CONST.__objc_arraydata: 0x568
   __DATA_CONST.__got: 0x478
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x1860
-  __AUTH_CONST.__objc_const: 0x1c20
-  __AUTH_CONST.__objc_intobj: 0xb28
-  __AUTH_CONST.__objc_arrayobj: 0x4e0
+  __AUTH_CONST.__const: 0x1180
+  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__objc_const: 0x1c50
+  __AUTH_CONST.__objc_intobj: 0xb70
+  __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x168
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x2d0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 816
-  Symbols:   2147
-  CStrings:  561
+  Functions: 830
+  Symbols:   2179
+  CStrings:  566
 
Symbols:
+ +[DMCEnrollmentFlowController(Utilities) _createSignInErrorFromError:]
+ -[DMCEnrollmentFlowController _checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:]
+ -[DMCEnrollmentFlowController _checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:]
+ -[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]
+ -[DMCEnrollmentFlowController requiredAppID]
+ -[DMCEnrollmentFlowController setRequiredAppID:]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_displayManagementDetailsSteps]
+ AppleAccountLibraryCore.frameworkLibrary
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table200
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table292
+ GCC_except_table49
+ OBJC_IVAR_$_DMCEnrollmentFlowController._requiredAppID
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_2
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_3
+ ___107-[DMCEnrollmentFlowController _presentAndHandleRemovalForITunesStoreID:installedBundleID:reason:allowSkip:]_block_invoke_4
+ ___AppleAccountLibraryCore_block_invoke
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40w_e23_v24?0B8B12"NSError"16l
+ ___block_descriptor_74_e8_32s40s48s56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56w
+ ___destroy_helper_block_e8_32s40s48s56w
+ _audit_stringAppleAccount
+ _objc_msgSend$_ADxE_ESSO_displayManagementDetailsSteps
+ _objc_msgSend$_checkExistingESSOApplicationWithITunesStoreID:debuggingAppIDs:
+ _objc_msgSend$_checkExistingRequiredApplicationWithITunesStoreID:essoITunesStoreID:
+ _objc_msgSend$_createSignInErrorFromError:
+ _objc_msgSend$aa_isTermsOfServiceUpdateRequired
+ _objc_msgSend$requestRemovalOfExistingApplicationForReason:iTunesStoreID:allowSkip:completionHandler:
+ _objc_msgSend$requiredAppID
+ _objc_msgSend$setRequiredAppID:
- GCC_except_table191
- GCC_except_table225
- GCC_except_table228
- GCC_except_table231
- GCC_except_table235
- GCC_except_table242
- GCC_except_table245
- GCC_except_table249
- GCC_except_table252
- GCC_except_table283
- GCC_except_table48
CStrings:
+ "/System/Library/PrivateFrameworks/AppleAccount.framework/Contents/MacOS/AppleAccount"
+ "CheckExistingESSOApplication"
+ "CheckExistingRequiredApplication"
+ "DMC_MAA_TERMS_NOT_ACCEPTED"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
```

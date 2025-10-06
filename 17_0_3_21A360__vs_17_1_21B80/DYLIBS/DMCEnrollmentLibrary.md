## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-3.26.0.0.0
-  __TEXT.__text: 0x13728
+3.26.2.3.0
+  __TEXT.__text: 0x13c38
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0xcdc
+  __TEXT.__objc_methlist: 0xcf4
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x14c3
-  __TEXT.__gcc_except_tab: 0x354
-  __TEXT.__oslogstring: 0x1c1b
+  __TEXT.__cstring: 0x14c6
+  __TEXT.__gcc_except_tab: 0x368
+  __TEXT.__oslogstring: 0x1d69
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x480e
-  __TEXT.__objc_methtype: 0x4a8
-  __TEXT.__objc_stubs: 0x3740
-  __DATA_CONST.__got: 0x170
+  __TEXT.__objc_methname: 0x48a0
+  __TEXT.__objc_methtype: 0x4b6
+  __TEXT.__objc_stubs: 0x37a0
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xb88
-  __DATA_CONST.__objc_selrefs: 0xeb0
+  __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_arraydata: 0x4c8
   __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x48

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63AFF104-29EB-3A85-A590-000D20B83E0C
-  Functions: 366
-  Symbols:   1554
-  CStrings:  1039
+  UUID: 3F596782-686A-313A-8B38-A290879906A4
+  Functions: 369
+  Symbols:   1565
+  CStrings:  1047
 
Symbols:
+ +[DMCEnrollmentFlowController _createEnterpriseApplicationExistsErrorWithAppName:]
+ -[DMCEnrollmentFlowController _appNameWithBundleID:]
+ -[DMCEnrollmentFlowController _verifyAccountsInformationWithAltDSID:personaID:]
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table139
+ GCC_except_table159
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ ___79-[DMCEnrollmentFlowController _verifyAccountsInformationWithAltDSID:personaID:]_block_invoke
+ ___block_descriptor_40_e19_"NSDictionary"8?0l
+ ___block_descriptor_56_e8_32s40s48w_e23_v24?0B8B12"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ _kMDMAnalyticsIsESSO
+ _objc_msgSend$_appNameWithBundleID:
+ _objc_msgSend$_createEnterpriseApplicationExistsErrorWithAppName:
+ _objc_msgSend$_verifyAccountsInformationWithAltDSID:personaID:
+ _objc_msgSend$dmc_iTunesAccountForRemoteManagingAccountWithAltDSID:
+ _objc_msgSend$localizedName
+ _objc_msgSend$personaIdentifier
- +[DMCEnrollmentFlowController _createEnterpriseApplicationExistsError]
- GCC_except_table102
- GCC_except_table107
- GCC_except_table110
- GCC_except_table116
- GCC_except_table136
- GCC_except_table156
- GCC_except_table85
- GCC_except_table88
- GCC_except_table91
- GCC_except_table94
- GCC_except_table97
- ___block_descriptor_39_e19_"NSDictionary"8?0l
- ___block_descriptor_40_e8_32w_e23_v24?0B8B12"NSError"16lw32l8
- ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_msgSend$_createEnterpriseApplicationExistsError
- _objc_msgSend$_serverForAppleMAID
- _objc_msgSend$isAppleWellKnownEnabled
CStrings:
+ "B32@0:8@16@24"
+ "DMC_ENTERPRISE_APPLICATION_EXISTS_%@"
+ "Failed to load record for app: %{public}@ with error: %{public}@."
+ "The persona ID (%{public}@) of the iCloud account (%{public}@) is different from the persona ID (%{public}@) used in this enrollment."
+ "The persona ID (%{public}@) of the iTunes account (%{public}@) is different from the persona ID (%{public}@) used in this enrollment."
+ "_appNameWithBundleID:"
+ "_createEnterpriseApplicationExistsErrorWithAppName:"
+ "_verifyAccountsInformationWithAltDSID:personaID:"
+ "dmc_iTunesAccountForRemoteManagingAccountWithAltDSID:"
+ "localizedName"
+ "personaIdentifier"
- "DMC_ENTERPRISE_APPLICATION_EXISTS"
- "_createEnterpriseApplicationExistsError"
- "isAppleWellKnownEnabled"

```

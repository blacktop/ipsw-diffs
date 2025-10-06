## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-3.26.2.3.0
-  __TEXT.__text: 0x13c38
+3.26.3.6.0
+  __TEXT.__text: 0x13c30
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0xcf4
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x14c6
+  __TEXT.__cstring: 0x14aa
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__oslogstring: 0x1d69
+  __TEXT.__oslogstring: 0x1de9
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__unwind_info: 0x434
   __TEXT.__objc_classname: 0xb9
   __TEXT.__objc_methname: 0x48a0
   __TEXT.__objc_methtype: 0x4b6

   __DATA_CONST.__objc_const: 0xb88
   __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__cfstring: 0xd80
+  __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__auth_got: 0x280

   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0xcc
   __DATA.__bss: 0x68
-  __DATA_DIRTY.__const: 0x60
+  __DATA_DIRTY.__const: 0x80
   __DATA_DIRTY.__objc_const: 0x1b0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F596782-686A-313A-8B38-A290879906A4
+  UUID: F2E1B223-D8BB-37FF-B817-1AC8EC0CFDA3
   Functions: 369
   Symbols:   1565
-  CStrings:  1047
+  CStrings:  1049
 
Symbols:
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.188
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.204
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.205
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.206
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.207
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.209
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.208
+ ___block_literal_global.362
+ ___block_literal_global.400
+ ___block_literal_global.446
+ __unnamed_array_storage.364
+ __unnamed_array_storage.386
+ __unnamed_array_storage.397
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.191
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.207
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.208
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.209
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.210
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.212
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.211
- ___block_literal_global.365
- ___block_literal_global.403
- ___block_literal_global.449
- __unnamed_array_storage.367
- __unnamed_array_storage.389
- __unnamed_array_storage.400
CStrings:
+ "No MDM profile found!"
+ "Unenrolling with altDSID..."
+ "Unenrolling with persona identifier..."
+ "Unenrolling with profile identifier..."
- "DEVICE_MISSING_APPLEACCOUNT"

```

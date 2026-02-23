## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.475.13.1.0
-  __TEXT.__text: 0x1966b8
+525.475.16.0.0
+  __TEXT.__text: 0x196d5c
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xef5c
+  __TEXT.__objc_methlist: 0xefbc
   __TEXT.__const: 0x6a48
-  __TEXT.__cstring: 0x1076f
+  __TEXT.__cstring: 0x1076e
   __TEXT.__gcc_except_tab: 0xa798
-  __TEXT.__oslogstring: 0x13afa
+  __TEXT.__oslogstring: 0x13cce
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4528
+  __TEXT.__unwind_info: 0x4538
   __TEXT.__objc_classname: 0x1e34
-  __TEXT.__objc_methname: 0x25057
-  __TEXT.__objc_methtype: 0x492d
-  __TEXT.__objc_stubs: 0x10b20
-  __DATA_CONST.__got: 0xac8
+  __TEXT.__objc_methname: 0x2510d
+  __TEXT.__objc_methtype: 0x496b
+  __TEXT.__objc_stubs: 0x10b80
+  __DATA_CONST.__got: 0xad0
   __DATA_CONST.__const: 0xa6a8
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78a8
+  __DATA_CONST.__objc_selrefs: 0x78c0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0x11560
-  __AUTH_CONST.__objc_const: 0x28238
+  __AUTH_CONST.__cfstring: 0x11540
+  __AUTH_CONST.__objc_const: 0x28280
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0x1154
+  __DATA.__objc_ivar: 0x1158
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64914DAB-690D-35BE-8D8A-A2DE53551ADB
-  Functions: 5766
-  Symbols:   21821
-  CStrings:  12801
+  UUID: 64B36112-2C9B-3EEF-96EC-4D987145BC64
+  Functions: 5770
+  Symbols:   21829
+  CStrings:  12813
 
Symbols:
+ -[AKAccountManager passkeyDeletionAttemptDateForAccount:]
+ -[AKAccountManager setPasskeyDeletionAttemptDate:forAccount:]
+ -[AKAccountManager setPasskeyRegistrationAttemptDate:forAccount:]
+ -[AKAppleIDPasskeySetupContext forceEnrollmentIgnoringServerState]
+ -[AKAppleIDPasskeySetupContext setForceEnrollmentIgnoringServerState:]
+ -[AKOSEligibilityManager _fetchRegulatoryRegionsForDomain:]
+ -[AKOSEligibilityManager _regulatoryCountryRegionsFromOSEligibility]
+ -[AKOSEligibilityManager _stringFromXPCArray:]
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table116
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table165
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table209
+ GCC_except_table218
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table257
+ GCC_except_table277
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table302
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table351
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table376
+ _AKAppleIDPasskeyDeletionAttemptDate
+ _AKURLBagKeyPasskeyCleanupDisabled
+ _OBJC_IVAR_$_AKAppleIDPasskeySetupContext._forceEnrollmentIgnoringServerState
+ __AKAppleIDPasskeyForceEnrollmentIgnoringServerStateKey
+ ___65-[AKAccountManager updatePasskeyCredentialsWithAltDSID:username:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_literal_global.251
+ ___block_literal_global.276
+ _kAKAnalyticsPdpState
+ _objc_msgSend$_fetchRegulatoryRegionsForDomain:
+ _objc_msgSend$_regulatoryCountryRegionsFromOSEligibility
+ _objc_msgSend$_stringFromXPCArray:
+ _objc_msgSend$updatePasskeyCredentialWithUserHandle:newName:completion:
- -[AKAccountManager passkeysDeletionAttemptDateForAccount:]
- -[AKAccountManager setPasskeyRegistrationAttemptDateForAccount:forAccount:]
- -[AKAccountManager setPasskeysDeletionAttemptDate:forAccount:]
- -[AKOSEligibilityManager _stringFromXPCArray:logPrefix:]
- -[AKURLBag isPasskeyCleanupDisabled]
- GCC_except_table110
- GCC_except_table112
- GCC_except_table120
- GCC_except_table123
- GCC_except_table146
- GCC_except_table161
- GCC_except_table168
- GCC_except_table171
- GCC_except_table173
- GCC_except_table181
- GCC_except_table184
- GCC_except_table195
- GCC_except_table204
- GCC_except_table205
- GCC_except_table211
- GCC_except_table213
- GCC_except_table221
- GCC_except_table222
- GCC_except_table252
- GCC_except_table254
- GCC_except_table261
- GCC_except_table281
- GCC_except_table282
- GCC_except_table300
- GCC_except_table303
- GCC_except_table306
- GCC_except_table322
- GCC_except_table323
- GCC_except_table324
- GCC_except_table325
- GCC_except_table355
- GCC_except_table361
- GCC_except_table362
- GCC_except_table59
- _AKAppleIDPasskeysDeletionAttemptDate
- __AKURLBagKeyPasskeyCleanupDisabled
- ___block_literal_global.249
- ___block_literal_global.274
- _kAKAnalyticsPdpEligibility
- _objc_msgSend$_stringFromXPCArray:logPrefix:
CStrings:
+ "@\"NSDate\"24@0:8@\"ACAccount\"16"
+ "@\"NSNumber\"24@0:8@\"ACAccount\"16"
+ "Failed to update passkey credential after username change: %{private}@"
+ "No primary AuthKit account, cannot determine user age range"
+ "No regulatory country regions found in XPC array"
+ "Regulatory country regions: %@"
+ "Successfully updated passkey credential after username change for altDSID: %{mask.hash}@"
+ "TB,N,V_forceEnrollmentIgnoringServerState"
+ "Updating passkey credentials for altDSID: %{mask.hash}@ with username: %@"
+ "User age range is unknown, cannot determine appropriate domain"
+ "User is adult, using adult age verification domain"
+ "User is child, using guardian age verification domain"
+ "User is teen, using teen attached to family domain"
+ "_fetchRegulatoryRegionsForDomain:"
+ "_forceEnrollmentIgnoringServerState"
+ "_regulatoryCountryRegionsFromOSEligibility"
+ "_stringFromXPCArray:"
+ "forceEnrollmentIgnoringServerState"
+ "passkeyDeletionAttemptDate"
+ "passkeyDeletionAttemptDateForAccount:"
+ "setForceEnrollmentIgnoringServerState:"
+ "setPasskeyDeletionAttemptDate:forAccount:"
+ "setPasskeyRegistrationAttemptDate:forAccount:"
- "%@-%@"
- "%@: %@"
- "No strings found in XPC array for %@"
- "Passkey credential update skipped: feature not enabled or platform not supported"
- "Regulatory country regions"
- "_stringFromXPCArray:logPrefix:"
- "isPasskeyCleanupDisabled"
- "passkeysDeletionAttemptDate"
- "passkeysDeletionAttemptDateForAccount:"
- "pdpEligible"
- "setPasskeyRegistrationAttemptDateForAccount:forAccount:"
- "setPasskeysDeletionAttemptDate:forAccount:"

```

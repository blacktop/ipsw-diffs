## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x1182cc
-  __TEXT.__objc_methlist: 0x7f34
-  __TEXT.__const: 0x127f4
-  __TEXT.__cstring: 0xb118
+625.1.29.11.25
+  __TEXT.__text: 0x117af8
+  __TEXT.__objc_methlist: 0x7f1c
+  __TEXT.__const: 0x12784
+  __TEXT.__cstring: 0xb128
   __TEXT.__ustring: 0x65ac
   __TEXT.__oslogstring: 0x3378
-  __TEXT.__gcc_except_tab: 0x118c
+  __TEXT.__gcc_except_tab: 0x1158
   __TEXT.__dlopen_cstrs: 0x25e
-  __TEXT.__swift5_typeref: 0x2b0e
+  __TEXT.__swift5_typeref: 0x2ab0
   __TEXT.__constg_swiftt: 0x1eb4
   __TEXT.__swift5_reflstr: 0x199a
   __TEXT.__swift5_fieldmd: 0x2b18

   __TEXT.__swift5_assocty: 0x730
   __TEXT.__swift5_proto: 0x8ec
   __TEXT.__swift5_types: 0x2f4
-  __TEXT.__swift_as_entry: 0x1dc
-  __TEXT.__swift_as_ret: 0x1ec
-  __TEXT.__swift_as_cont: 0x3c8
+  __TEXT.__swift_as_entry: 0x1d4
+  __TEXT.__swift_as_ret: 0x1f4
+  __TEXT.__swift_as_cont: 0x3d0
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_capture: 0xc14
+  __TEXT.__swift5_capture: 0xb54
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__unwind_info: 0x51e0
-  __TEXT.__eh_frame: 0x5608
+  __TEXT.__unwind_info: 0x51a0
+  __TEXT.__eh_frame: 0x5560
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b80
+  __DATA_CONST.__objc_selrefs: 0x4b90
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __DATA_CONST.__got: 0xeb8
-  __AUTH_CONST.__const: 0x9e00
+  __DATA_CONST.__got: 0xea8
+  __AUTH_CONST.__const: 0x9cc0
   __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0xf8a8
+  __AUTH_CONST.__objc_const: 0xf8b8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1388
+  __AUTH_CONST.__auth_got: 0x1358
   __AUTH.__objc_data: 0x30b0
   __AUTH.__data: 0x13c0
   __DATA.__objc_ivar: 0x790
-  __DATA.__data: 0x3350
+  __DATA.__data: 0x3368
   __DATA.__bss: 0x10c20
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x9c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7470
-  Symbols:   8333
+  Functions: 7456
+  Symbols:   8330
   CStrings:  1348
 
Symbols:
+ -[ASAuthorizationProviderExtensionLoginConfiguration includePlatformSSOAuthorizationScopes]
+ -[ASAuthorizationProviderExtensionLoginConfiguration setIncludePlatformSSOAuthorizationScopes:]
+ GCC_except_table56
+ _credentialRequiresDismissalFromViewService
+ _objc_msgSend$continueRunningActivityWithSavedAccountStore:completionHandler:
+ _objc_msgSend$includePlatformSSOAuthorizationScopes
+ _objc_msgSend$isAutomaticPasswordChangeAllowlistEnabled
+ _objc_msgSend$isAutomaticPasswordChangeCustomDebugWebsitesListEnabled
+ _objc_msgSend$preWarmWarningsWithCompletionHandler:
+ _objc_msgSend$reportAnalyticsIfNecessary
+ _objc_msgSend$setIncludePlatformSSOAuthorizationScopes:
- -[ASAuthorizationServiceViewController _credentialRequiresDismissalFromViewService:]
- GCC_except_table57
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_3
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_4
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_5
- _objc_msgSend$_credentialRequiresDismissalFromViewService:
- _objc_msgSend$acknowledgeCompletedAutomaticPasswordChangeSessionsWithCompletionHandler:
- _objc_msgSend$donateSecurityRecommendationsToBiomeWithPasswordWarningManager:completionHandler:
- _objc_msgSend$notifyUserAboutAutomaticSecurityUpgradesIfNecessaryWithPasswordWarningManager:completionHandler:
- _objc_msgSend$performMetadataChecksForDomainsInSavedAccountStore:quirksManager:completionHandler:
- _symbolic Sny_____G 10Foundation4DateV
- _symbolic So24WBSAutoFillQuirksManagerC
- _symbolic So25WBSPasswordWarningManagerC
- _symbolic _____5lower_AA5uppert 10Foundation4DateV
CStrings:
+ "Allow “%@” to temporarily access verification codes?"
+ "“%@” will be able to use one-time verification codes in %@ while it signs in to your accounts."
+ "“%@” will be able to use one-time verification codes while it signs in to your accounts."
- "Allow “%@” to temporarily access verification codes you receive?"
- "This will make one-time verification codes available to “%@” for up to %@."
- "This will make one-time verification codes received in %@ available to “%@” for up to %@."
```

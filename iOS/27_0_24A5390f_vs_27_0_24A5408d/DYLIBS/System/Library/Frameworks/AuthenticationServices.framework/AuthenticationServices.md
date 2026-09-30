## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-625.1.24.10.1
-  __TEXT.__text: 0x14376c
-  __TEXT.__objc_methlist: 0x8074
+625.1.29.10.3
+  __TEXT.__text: 0x1431a8
+  __TEXT.__objc_methlist: 0x8064
   __TEXT.__cstring: 0xb558
-  __TEXT.__const: 0x13f64
-  __TEXT.__gcc_except_tab: 0x1204
-  __TEXT.__oslogstring: 0x34db
+  __TEXT.__const: 0x13ef4
+  __TEXT.__gcc_except_tab: 0x11d4
+  __TEXT.__oslogstring: 0x356b
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d36
-  __TEXT.__swift5_typeref: 0x328e
+  __TEXT.__swift5_typeref: 0x324e
   __TEXT.__constg_swiftt: 0x22b4
   __TEXT.__swift5_reflstr: 0x1d5c
   __TEXT.__swift5_fieldmd: 0x2f10

   __TEXT.__swift5_proto: 0x9bc
   __TEXT.__swift5_types: 0x354
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_capture: 0xea8
-  __TEXT.__swift_as_entry: 0x250
-  __TEXT.__swift_as_ret: 0x2cc
-  __TEXT.__swift_as_cont: 0x500
+  __TEXT.__swift5_capture: 0xde8
+  __TEXT.__swift_as_entry: 0x248
+  __TEXT.__swift_as_ret: 0x2d4
+  __TEXT.__swift_as_cont: 0x508
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__unwind_info: 0x5d40
-  __TEXT.__eh_frame: 0x6eac
+  __TEXT.__unwind_info: 0x5d00
+  __TEXT.__eh_frame: 0x6e04
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ca0
+  __DATA_CONST.__objc_selrefs: 0x4cb8
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x10a0
-  __AUTH_CONST.__const: 0x9bd8
+  __DATA_CONST.__got: 0x1090
+  __AUTH_CONST.__const: 0x9a98
   __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x10130
+  __AUTH_CONST.__objc_const: 0x10150
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x16b8
+  __AUTH_CONST.__auth_got: 0x1680
   __AUTH.__objc_data: 0x3a28
   __AUTH.__data: 0x18c0
-  __DATA.__objc_ivar: 0x6fc
-  __DATA.__data: 0x38e0
+  __DATA.__objc_ivar: 0x700
+  __DATA.__data: 0x38a0
   __DATA.__bss: 0x12530
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x510

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8193
-  Symbols:   8449
-  CStrings:  1350
+  Functions: 8182
+  Symbols:   8450
+  CStrings:  1352
 
Symbols:
+ -[_ASPasswordManagerIconController resumeFetching]
+ -[_ASPasswordManagerIconController suspendFetching]
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table67
+ _OBJC_IVAR_$__ASPasswordManagerIconController._fetchingSuspended
+ ___50-[_ASPasswordManagerIconController resumeFetching]_block_invoke
+ ___51-[_ASPasswordManagerIconController suspendFetching]_block_invoke
+ _objc_msgSend$continueRunningActivityWithSavedAccountStore:completionHandler:
+ _objc_msgSend$isAutomaticPasswordChangeAllowlistEnabled
+ _objc_msgSend$isAutomaticPasswordChangeCustomDebugWebsitesListEnabled
+ _objc_msgSend$preWarmWarningsWithCompletionHandler:
+ _objc_msgSend$reportAnalyticsIfNecessary
- GCC_except_table54
- GCC_except_table62
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_4
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_5
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_6
- _objc_msgSend$acknowledgeCompletedAutomaticPasswordChangeSessionsWithCompletionHandler:
- _objc_msgSend$donateSecurityRecommendationsToBiomeWithPasswordWarningManager:completionHandler:
- _objc_msgSend$notifyUserAboutAutomaticSecurityUpgradesIfNecessaryWithPasswordWarningManager:completionHandler:
- _objc_msgSend$performMetadataChecksForDomainsInSavedAccountStore:quirksManager:completionHandler:
- _symbolic Sny_____G 10Foundation4DateV
- _symbolic So25WBSPasswordWarningManagerC
- _symbolic _____5lower_AA5uppert 10Foundation4DateV
CStrings:
+ "Allow “%@” to temporarily access verification codes?"
+ "Skipping touch icon fetch while suspended; domain=%{sensitive, mask.hash}@"
+ "Suspending icon fetching; cancelling %d in-flight request(s)"
+ "“%@” will be able to use one-time verification codes in apps like %@ while it signs in to your accounts."
+ "“%@” will be able to use one-time verification codes while it signs in to your accounts."
+ "\xf01"
- "Allow “%@” to temporarily access verification codes you receive?"
- "This will make one-time verification codes available to “%@” for up to %@."
- "This will make one-time verification codes received in apps like %@ available to “%@” for up to %@."
- "\xf0!"
```

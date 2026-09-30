## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-9.4.28.2.1
-  __TEXT.__text: 0x10be8
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x5d4
+9.5.4.0.0
+  __TEXT.__text: 0x1100c
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x9c5
+  __TEXT.__cstring: 0x9d5
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__oslogstring: 0x28ed
+  __TEXT.__oslogstring: 0x2a51
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xbe

   __TEXT.__unwind_info: 0x388
   __TEXT.__eh_frame: 0x420
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x1eda
+  __TEXT.__objc_methname: 0x1f3c
   __TEXT.__objc_methtype: 0x315
-  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__objc_stubs: 0x2040
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x920
+  __DATA_CONST.__objc_selrefs: 0x930
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x3d8
-  __AUTH_CONST.__const: 0x208
+  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x7e0
   __AUTH_CONST.__objc_const: 0x568
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 129DA0A3-5997-3646-BC70-399D2BE23374
-  Functions: 222
-  Symbols:   185
-  CStrings:  641
+  UUID: 1DE5276C-EBBB-3199-9787-888A0807D37B
+  Functions: 224
+  Symbols:   186
+  CStrings:  647
 
Symbols:
+ __os_feature_enabled_impl
CStrings:
+ "%{public}@: [%{public}@] Beta local account storefront was updated from Production local account. betaLocalAccount = %{public}@ | productionLocalAccount = %{public}@"
+ "%{public}@: [%{public}@] Beta local account's storefront doesn't need to be updated. betaLocalAccount = %{public}@"
+ "%{public}@: [%{public}@] No Beta local account found to update storefront."
+ "BetaLocalAccount"
+ "_updateBetaLocalAccountStorefrontIfNeededFromProductionLocalAccount:store:"
+ "ams_isLocalBetaAccount"

```

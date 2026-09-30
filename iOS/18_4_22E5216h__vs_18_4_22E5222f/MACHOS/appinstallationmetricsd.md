## appinstallationmetricsd

> `/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd`

```diff

-2.4.5.0.0
-  __TEXT.__text: 0x2ae6c
-  __TEXT.__auth_stubs: 0x1520
+2.4.6.0.0
+  __TEXT.__text: 0x2b0e4
+  __TEXT.__auth_stubs: 0x1530
   __TEXT.__objc_methlist: 0x2f8
-  __TEXT.__const: 0x1940
+  __TEXT.__const: 0x1910
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xd37
+  __TEXT.__cstring: 0xd44
   __TEXT.__constg_swiftt: 0x8c8
-  __TEXT.__swift5_typeref: 0x8cf
+  __TEXT.__swift5_typeref: 0x8c7
   __TEXT.__swift5_reflstr: 0x461
   __TEXT.__swift5_fieldmd: 0x6c8
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__objc_methname: 0x8c1
-  __TEXT.__oslogstring: 0xae5
+  __TEXT.__oslogstring: 0xbf4
   __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0x9c
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0x1b4
-  __TEXT.__swift_as_entry: 0xb4
-  __TEXT.__swift_as_ret: 0xd8
+  __TEXT.__swift_as_entry: 0xa8
+  __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x1b0
+  __TEXT.__swift5_capture: 0x1e0
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0xb68
-  __TEXT.__eh_frame: 0x1f18
-  __DATA_CONST.__auth_got: 0xa90
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__auth_ptr: 0x408
-  __DATA_CONST.__const: 0x15d0
+  __TEXT.__unwind_info: 0xb20
+  __TEXT.__eh_frame: 0x1d80
+  __DATA_CONST.__auth_got: 0xa98
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__auth_ptr: 0x410
+  __DATA_CONST.__const: 0x1678
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xd98
   __DATA.__objc_selrefs: 0x338
   __DATA.__objc_data: 0x360
-  __DATA.__data: 0x1180
+  __DATA.__data: 0x1170
   __DATA.__bss: 0x2340
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 795
-  Symbols:   576
-  CStrings:  311
+  Functions: 784
+  Symbols:   577
+  CStrings:  315
 
Symbols:
+ _$sSD11descriptionSSvg
+ _AnalyticsSendEventLazy
- _$s22AppInstallationMetrics0B5EventV17billingStorefrontSSSgvg
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Posting CA event for %{public}s: %s"
+ "[%@] Event with bundleID: %s has a polus storefront: %s"
+ "[%@] Event with bundleID: %s is missing a polus storefront. Falling back to header sourced storefront: %s"
+ "[%@] Failed to find storefront for bundleID: %s"
+ "com.apple.appinstallationmetrics.polusStorefrontMissing"
+ "polusStorefrontMissing"
- "billingStorefront"
- "piu-config/billingStorefrontName"
- "v28@?0@\"NSString\"8B16@\"NSError\"20"

```

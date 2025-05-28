## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-1.5.10.2.6
-  __TEXT.__text: 0x49bf64
-  __TEXT.__auth_stubs: 0x4d80
-  __TEXT.__objc_stubs: 0x19e0
+1.5.16.0.0
+  __TEXT.__text: 0x4aff88
+  __TEXT.__auth_stubs: 0x4de0
+  __TEXT.__objc_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x1584
-  __TEXT.__const: 0x36598
+  __TEXT.__const: 0x36638
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x41ea
-  __TEXT.__cstring: 0x14a64
-  __TEXT.__objc_methname: 0x5cb8
-  __TEXT.__constg_swiftt: 0x5434
-  __TEXT.__swift5_types: 0x794
-  __TEXT.__swift5_proto: 0x12cc
+  __TEXT.__swift5_typeref: 0x41c0
+  __TEXT.__cstring: 0x14f74
+  __TEXT.__objc_methname: 0x5cf2
+  __TEXT.__constg_swiftt: 0x545c
+  __TEXT.__swift5_types: 0x798
+  __TEXT.__swift5_proto: 0x12d4
   __TEXT.__swift5_protos: 0x68
-  __TEXT.__objc_classname: 0x420
-  __TEXT.__objc_methtype: 0x14ab
-  __TEXT.__gcc_except_tab: 0x438
+  __TEXT.__objc_classname: 0x41f
+  __TEXT.__objc_methtype: 0x14bb
+  __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__oslogstring: 0x308
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__unwind_info: 0xf0cc
-  __TEXT.__eh_frame: 0x28a90
-  __DATA_CONST.__auth_got: 0x26d0
-  __DATA_CONST.__got: 0x1090
-  __DATA_CONST.__auth_ptr: 0x418
-  __DATA_CONST.__const: 0x25350
+  __TEXT.__unwind_info: 0xf360
+  __TEXT.__eh_frame: 0x29e20
+  __DATA_CONST.__auth_got: 0x2700
+  __DATA_CONST.__got: 0x1098
+  __DATA_CONST.__auth_ptr: 0x420
+  __DATA_CONST.__const: 0x254a0
   __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_classrefs: 0x418
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6bd8
-  __DATA.__objc_selrefs: 0x1850
+  __DATA.__objc_const: 0x6bb0
+  __DATA.__objc_selrefs: 0x1860
   __DATA.__objc_ivar: 0xcc
-  __DATA.__objc_data: 0x1eb0
-  __DATA.__data: 0x10838
-  __DATA.__common: 0xb68
-  __DATA.__bss: 0x255f0
+  __DATA.__objc_data: 0x1f00
+  __DATA.__data: 0x108a8
+  __DATA.__common: 0xb70
+  __DATA.__bss: 0x256f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16750
-  Symbols:   2240
-  CStrings:  3181
+  Functions: 16885
+  Symbols:   2248
+  CStrings:  3204
 
Symbols:
+ _$s14MarketplaceKit24LicenseResolutionContextV6logKey3urlACSS_10Foundation3URLVtcfC
+ _$s14MarketplaceKit24LicenseResolutionContextVMa
+ _$s14MarketplaceKit24LicenseResolutionRequestV3runyyYaKF
+ _$s14MarketplaceKit24LicenseResolutionRequestV3runyyYaKFTu
+ _$s14MarketplaceKit24LicenseResolutionRequestV7contextAcA0cD7ContextV_tcfC
+ _$s14MarketplaceKit24LicenseResolutionRequestVMa
+ _$ss4Int8VMn
+ _objc_autorelease
CStrings:
+ "2`"
+ "App License Expired"
+ "B32@0:8@?16^@24"
+ "Failed to renew expiring licenses: %{public}@"
+ "ManagedAppDistribution.AppLicenseExpired.Message"
+ "ManagedAppDistribution.AppLicenseExpired.NoRecovery.Message"
+ "ManagedAppDistribution.AppLicenseExpired.Title"
+ "ManagedAppDistribution.Common.Cancel"
+ "ManagedAppDistribution.Common.Resolve"
+ "ManagedAppDistribution.MarketplaceLicenseExpired.Title"
+ "Marketplace License Expired"
+ "The license for “@@appName@@” has expired and can't be opened. Contact the developer for additional details."
+ "The license for “@@appName@@” has expired. To open the app, you must first resolve the issue."
+ "[%@] Acknowledged developer interaction required alert"
+ "[%@] Asked to resolve license issue"
+ "[%@] Ignored request to resolve license issue"
+ "[%@] Not showing license resolution sheet as prompting not allowed"
+ "[%@] Not showing license resolution sheet as this was a request for multiple apps"
+ "[%@] Re-attempting license renewal after showing resolution sheet for ineligible license"
+ "[%@] Re-attempting license renewal after showing resolution sheet for invalid response"
+ "[%@] Re-attempting license renewal after showing resolution sheet for invalid status code"
+ "[%@] Renewing licenses for apps: %{public}s"
+ "apps"
+ "licenseResolutionURL"
+ "performTransaction:error:"
+ "resolutionURL"
+ "setPercentComplete:"
+ "setPreparationPromise:withError:"
- "2@`"
- "[%@] Failed to renew licenses: %{public}s"
- "[%@] Renewing licenses with ids: %{public}s"
- "licenseIDs"
- "performTransaction:"

```

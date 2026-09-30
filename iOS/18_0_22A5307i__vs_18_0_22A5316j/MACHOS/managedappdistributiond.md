## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-2.0.32.0.0
-  __TEXT.__text: 0x4dece4
-  __TEXT.__auth_stubs: 0x5460
+2.0.37.0.0
+  __TEXT.__text: 0x4ec15c
+  __TEXT.__auth_stubs: 0x54c0
   __TEXT.__objc_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x15f4
-  __TEXT.__const: 0x370c8
-  __TEXT.__cstring: 0xae85
+  __TEXT.__objc_methlist: 0x15cc
+  __TEXT.__const: 0x37148
+  __TEXT.__cstring: 0xb1f5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x5d3e
-  __TEXT.__oslogstring: 0xb36e
-  __TEXT.__objc_classname: 0x41f
-  __TEXT.__objc_methtype: 0x1519
+  __TEXT.__objc_methname: 0x5d6c
+  __TEXT.__oslogstring: 0xb69e
+  __TEXT.__objc_classname: 0x403
+  __TEXT.__objc_methtype: 0x14fa
   __TEXT.__gcc_except_tab: 0x498
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__constg_swiftt: 0x561c
-  __TEXT.__swift5_typeref: 0x445e
-  __TEXT.__swift5_proto: 0x1310
-  __TEXT.__swift5_types: 0x7c8
+  __TEXT.__constg_swiftt: 0x5644
+  __TEXT.__swift5_typeref: 0x4482
+  __TEXT.__swift5_proto: 0x1318
+  __TEXT.__swift5_types: 0x7cc
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__info_plist: 0x766
-  __TEXT.__unwind_info: 0xebb0
-  __TEXT.__eh_frame: 0x2c1e0
-  __DATA_CONST.__auth_got: 0x2a40
-  __DATA_CONST.__got: 0x16b8
-  __DATA_CONST.__auth_ptr: 0x1938
-  __DATA_CONST.__const: 0x28440
+  __TEXT.__unwind_info: 0xed30
+  __TEXT.__eh_frame: 0x2c910
+  __DATA_CONST.__auth_got: 0x2a70
+  __DATA_CONST.__got: 0x16c0
+  __DATA_CONST.__auth_ptr: 0x1958
+  __DATA_CONST.__const: 0x28498
   __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6f50
-  __DATA.__objc_selrefs: 0x1888
+  __DATA.__objc_const: 0x6eb8
+  __DATA.__objc_selrefs: 0x1890
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x2040
-  __DATA.__data: 0xc790
-  __DATA.__bss: 0x255f0
-  __DATA.__common: 0xb90
+  __DATA.__data: 0xc800
+  __DATA.__bss: 0x256f0
+  __DATA.__common: 0xba0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14175
-  Symbols:   2444
-  CStrings:  3291
+  Functions: 14239
+  Symbols:   2451
+  CStrings:  3320
 
Symbols:
+ _$s14MarketplaceKit15AutomaticUpdateV11appShareURL10Foundation0G0VSgvg
+ _$s14MarketplaceKit17AppInstallRequestV11appShareURL10Foundation0H0VSgvg
+ _$s14MarketplaceKit17AppInstallRequestV3adp4type10oAuthToken019installVerificationI09accountID11appShareURLAC10Foundation0P0V_07ManagedC12Distribution0cdE4TypeOSSSgAPSSALSgtcfC
+ _$s14MarketplaceKit24LicenseResolutionContextV6logKey3urlACSS_10Foundation3URLVtcfC
+ _$s14MarketplaceKit24LicenseResolutionContextVMa
+ _$s14MarketplaceKit24LicenseResolutionRequestV3runyyYaKF
+ _$s14MarketplaceKit24LicenseResolutionRequestV3runyyYaKFTu
+ _$s14MarketplaceKit24LicenseResolutionRequestV7contextAcA0cD7ContextV_tcfC
+ _$s14MarketplaceKit24LicenseResolutionRequestVMa
- _$s14MarketplaceKit17AppInstallRequestV3adp4type10oAuthToken019installVerificationI09accountIDAC10Foundation3URLV_07ManagedC12Distribution0cdE4TypeOSSSgAOSStcfC
- _objc_release_x11
CStrings:
+ "App License Expired"
+ "DoForceDeltaUpdateFailure"
+ "Forced failure of delta-package downloads is enabled."
+ "ManagedAppDistribution.AppLicenseExpired.Message"
+ "ManagedAppDistribution.AppLicenseExpired.NoRecovery.Message"
+ "ManagedAppDistribution.AppLicenseExpired.Title"
+ "ManagedAppDistribution.Common.Cancel"
+ "ManagedAppDistribution.Common.Resolve"
+ "ManagedAppDistribution.MarketplaceLicenseExpired.Title"
+ "ManagedAppDistributionDaemon/CommonAlerts.swift"
+ "Marketplace License Expired"
+ "Received event: %!s(MISSING)"
+ "The license for “@@appName@@” has expired and can't be opened. Contact the developer for additional details."
+ "The license for “@@appName@@” has expired. To open the app, you must first resolve the issue."
+ "Unable to get license info"
+ "[%!@(MISSING)] Acknowledged developer interaction required alert"
+ "[%!@(MISSING)] Allowing promotion"
+ "[%!@(MISSING)] Asked to resolve license issue"
+ "[%!@(MISSING)] Created coordinator: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Forcing failure of delta update (expect further error messages prior to expected retry with full update)…"
+ "[%!@(MISSING)] Found existing coordinator: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Ignored request to resolve license issue"
+ "[%!@(MISSING)] Not showing license resolution sheet as prompting not allowed"
+ "[%!@(MISSING)] Not showing license resolution sheet as this was a request for multiple apps"
+ "[%!@(MISSING)] Re-attempting license renewal after showing resolution sheet for ineligible license"
+ "[%!@(MISSING)] Re-attempting license renewal after showing resolution sheet for invalid response"
+ "[%!@(MISSING)] Re-attempting license renewal after showing resolution sheet for invalid status code"
+ "[%!@(MISSING)] Renewing licenses for apps: %!{(MISSING)public}s"
+ "appShareURL"
+ "app_share_url"
+ "apps"
+ "licenseResolutionURL"
+ "resolutionURL"
+ "setPercentComplete:"
+ "setPreparationPromise:withError:"
+ "setShareURL:"
- "AppLicenseDeliveryUtilities"
- "[%!@(MISSING)] Coordinator: %!{(MISSING)public}@"
- "[%!@(MISSING)] Renewing licenses with ids: %!{(MISSING)public}s"
- "[%!@(MISSING)][%!{(MISSING)public}s] Unhandled to create / find coordinator"
- "licenseIDs"
- "licenseInfoForData:"
- "{LicenseInfo_=IiQQQQ}24@0:8@16"

```

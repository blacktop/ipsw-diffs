## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-3.0.50.0.0
-  __TEXT.__text: 0x617734
-  __TEXT.__auth_stubs: 0x5ea0
+3.0.52.0.0
+  __TEXT.__text: 0x61e7a0
+  __TEXT.__auth_stubs: 0x5f10
   __TEXT.__objc_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0x2164
-  __TEXT.__const: 0x3c544
+  __TEXT.__objc_methlist: 0x2184
+  __TEXT.__const: 0x3c594
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x6114
-  __TEXT.__cstring: 0xc555
-  __TEXT.__oslogstring: 0xeaee
+  __TEXT.__objc_methname: 0x61c9
+  __TEXT.__cstring: 0xc545
+  __TEXT.__oslogstring: 0xedce
   __TEXT.__objc_classname: 0x3e9
   __TEXT.__objc_methtype: 0x150c
   __TEXT.__gcc_except_tab: 0x508
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__constg_swiftt: 0x6540
-  __TEXT.__swift5_typeref: 0x54b8
+  __TEXT.__swift5_typeref: 0x54e8
   __TEXT.__swift5_proto: 0x16f8
   __TEXT.__swift5_types: 0x920
-  __TEXT.__swift_as_entry: 0x9c8
-  __TEXT.__swift_as_ret: 0x1234
+  __TEXT.__swift_as_entry: 0x9d8
+  __TEXT.__swift_as_ret: 0x1250
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__unwind_info: 0x11090
-  __TEXT.__eh_frame: 0x337b4
-  __DATA_CONST.__auth_got: 0x2f60
-  __DATA_CONST.__got: 0x1c68
-  __DATA_CONST.__auth_ptr: 0x16f0
-  __DATA_CONST.__const: 0x2d5d0
+  __TEXT.__unwind_info: 0x10cf8
+  __TEXT.__eh_frame: 0x33c64
+  __DATA_CONST.__auth_got: 0x2f98
+  __DATA_CONST.__got: 0x1c90
+  __DATA_CONST.__auth_ptr: 0x16f8
+  __DATA_CONST.__const: 0x2d648
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5eb8
-  __DATA.__objc_selrefs: 0x1c00
+  __DATA.__objc_const: 0x5ec0
+  __DATA.__objc_selrefs: 0x1c40
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1f30
-  __DATA.__data: 0xcbd0
+  __DATA.__data: 0xcc10
   __DATA.__bss: 0x2c650
   __DATA.__common: 0xca8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8150F1C2-0E9C-330A-BC8F-3BC109B2922B
-  Functions: 14758
-  Symbols:   2826
-  CStrings:  3771
+  UUID: 91789580-B128-32E5-BFE6-2C3DB676FC4A
+  Functions: 14795
+  Symbols:   2838
+  CStrings:  3788
 
Symbols:
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO05isWebC0Sbvg
+ _$s14MarketplaceKit19InstallSheetContextV6sourceAC6SourceOvg
+ _$s14MarketplaceKit25SKSalesReportTokenRequestV16bundleIDOverrideSSSgvg
+ _$s14MarketplaceKit25SKSalesReportTokenRequestV9tokenTypeSSvg
+ _$s14MarketplaceKit25SKSalesReportTokenRequestVMa
+ _$s14MarketplaceKit25SKSalesReportTokenRequestVSEAAMc
+ _$s14MarketplaceKit25SKSalesReportTokenRequestVSeAAMc
+ _$s14MarketplaceKit26SKSalesReportTokenResponseV5tokenACSS_tcfC
+ _$s14MarketplaceKit26SKSalesReportTokenResponseVMn
+ _$s8StoreKit18SKExternalPurchaseO5token4type14clientOverrideS2S_So20SKPaymentQueueClientCtYaKFZ
+ _$s8StoreKit18SKExternalPurchaseO5token4type14clientOverrideS2S_So20SKPaymentQueueClientCtYaKFZTu
+ _OBJC_CLASS_$_SKPaymentQueueClient
CStrings:
+ "App Store app cannot request sales reporting token"
+ "Failed to fetch reporting token from Store Kit: %s"
+ "Fetch token"
+ "Fetching reporting token from store kit with bundleID:%{public}s itemID:%{public}@ versionID: %@ environment:%ld tokenType:%s"
+ "Sales reporting token request %{public}s called for 3rd party marketplace app with bundleID:%{public}s itemID:%{public}@"
+ "Sales reporting token request %{public}s called for Xcode built app with bundleID:%{public}s"
+ "Sales reporting token request called by internal build using bundleID override:%s"
+ "Sales reporting token request called using bundleID:%s"
+ "Successfully fetched reporting token from Store Kit:%s"
+ "Unknown type of app"
+ "distributorIsFirstPartyApple"
+ "environmentType"
+ "lockedADP"
+ "setBundleIdentifier:"
+ "setEnvironmentType:"
+ "setStoreExternalVersion:"
+ "setStoreItemIdentifier:"
+ "storeExternalVersion"
+ "tokenForTokenType:reply:"
- "adp"
- "network.cellular.button.update"

```

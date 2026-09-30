## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-3.2.11.0.0
-  __TEXT.__text: 0x6a9398
-  __TEXT.__auth_stubs: 0x6640
+3.2.14.2.10
+  __TEXT.__text: 0x6b042c
+  __TEXT.__auth_stubs: 0x6670
   __TEXT.__objc_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0x2354
-  __TEXT.__const: 0x400e0
+  __TEXT.__const: 0x40270
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x67d9
-  __TEXT.__cstring: 0xfbc5
-  __TEXT.__oslogstring: 0x11cd2
+  __TEXT.__objc_methname: 0x680b
+  __TEXT.__cstring: 0x10325
+  __TEXT.__oslogstring: 0x11d82
   __TEXT.__objc_classname: 0x410
   __TEXT.__objc_methtype: 0x1540
   __TEXT.__gcc_except_tab: 0x518
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__constg_swiftt: 0x6800
+  __TEXT.__constg_swiftt: 0x6818
   __TEXT.__swift5_typeref: 0x5a36
   __TEXT.__swift5_proto: 0x1724
   __TEXT.__swift5_types: 0x948
-  __TEXT.__swift_as_entry: 0xac4
-  __TEXT.__swift_as_ret: 0x15c4
+  __TEXT.__swift_as_entry: 0xad8
+  __TEXT.__swift_as_ret: 0x1624
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__unwind_info: 0x11808
-  __TEXT.__eh_frame: 0x3864c
-  __DATA_CONST.__auth_got: 0x3330
-  __DATA_CONST.__got: 0x1ed0
+  __TEXT.__unwind_info: 0x12198
+  __TEXT.__eh_frame: 0x38c54
+  __DATA_CONST.__auth_got: 0x3348
+  __DATA_CONST.__got: 0x1f00
   __DATA_CONST.__auth_ptr: 0x1868
-  __DATA_CONST.__const: 0x2e150
+  __DATA_CONST.__const: 0x2e218
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6448
-  __DATA.__objc_selrefs: 0x1da8
+  __DATA.__objc_const: 0x6488
+  __DATA.__objc_selrefs: 0x1db8
   __DATA.__objc_ivar: 0xcc
-  __DATA.__objc_data: 0x20a8
-  __DATA.__data: 0xd558
+  __DATA.__objc_data: 0x20b0
+  __DATA.__data: 0xd5a0
   __DATA.__bss: 0x2cbd0
   __DATA.__common: 0xd98
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0312EC58-95FF-32A3-95B5-44A9BC3905C6
-  Functions: 15589
-  Symbols:   3056
-  CStrings:  4210
+  UUID: CE46B9D9-E5D7-3155-A8A0-5952A2552D37
+  Functions: 15658
+  Symbols:   3065
+  CStrings:  4230
 
Symbols:
+ _$s13OSEligibility0A7ContextO22marketplaceInstallFlowyACSScACmFWC
+ _$s14MarketplaceKit17FetchDataResponseV0E0O011usesUpdatedA11InstallFlowyAESbcAEmFWC
+ _$s14MarketplaceKit17FetchDataResponseV0E0O13catalogRegionyAESSSgcAEmFWC
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO011DistributorE0V4name2id7appName7iconURL09isCurrentG8AppStore07currentgK0AGSS_S2S10Foundation0M0VSgSbSSSgtcfC
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO03WebcE0V6domain13developerName0I2ID03appJ08isUpdate7iconURL0M26CurrentDistributorAppStore07currentrJ0AGSS_S3SSb10Foundation0P0VSgSbSSSgtcfC
+ _$s14MarketplaceKit22FetchPublicDataRequestV0F0O13catalogRegionyA2EmFWC
+ _$s14MarketplaceKit23FetchPrivateDataRequestV0F0O011usesUpdatedA11InstallFlowyA2EmFWC
+ _$sScTss5NeverORs_rlE5valuexvg
+ _$sScTss5NeverORs_rlE5valuexvgTu
CStrings:
+ "Joining existing localization load task already in progress."
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.FromMarketplaceToMarketplace.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.FromMarketplaceToWeb.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.FromWebToMarketplace.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.UnapprovedDeveloper.Alternate.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.UnapprovedDeveloper.Alternate.Body.IPad"
+ "No localized distributor names found for: %{public}@"
+ "Not eligible for alternative distribution"
+ "Unhandled distributor transition: "
+ "[%@] Inline installation is not available in this region"
+ "currentDistributor"
+ "currentMarketplace"
+ "hasParallelPlaceholder"
+ "installingMarketplace"
+ "loaderTask"
+ "setAllowDistributorChange:"
+ "“@@appName@@” was previously installed and updated from “@@currentMarketplace@@”. You can replace this app with a version from “@@installingMarketplace@@”. Your app data and settings will remain unchanged."
+ "“@@appName@@” was previously installed and updated from “@@domain@@”. You can replace this app with a version from “@@marketplaceName@@”. Your app data and settings will remain unchanged."
+ "“@@appName@@” was previously installed and updated from “@@marketplaceName@@”.\n\nTo replace this app with a version from “@@domain@@,” change your installation settings on this iPad to allow apps from “@@developerName@@” to be installed from the web. Your app data and app settings will remain unchanged."
+ "“@@appName@@” was previously installed and updated from “@@marketplaceName@@”.\n\nTo replace this app with a version from “@@domain@@,” change your installation settings on this iPhone to allow apps from “@@developerName@@” to be installed from the web. Your app data and app settings will remain unchanged."
+ "“@@appName@@” was previously installed and updated from “@@marketplaceName@@”. You can replace this app with a version from “@@domain@@”. Your app data and settings will remain unchanged."
- "No localized distributor names found for %{public}s"

```

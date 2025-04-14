## HomeUI

> `/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI`

```diff

-1026.6.20.0.0
-  __TEXT.__text: 0x663154
-  __TEXT.__auth_stubs: 0x6cc0
-  __TEXT.__objc_methlist: 0x4e31c
-  __TEXT.__const: 0xd420
+1026.6.26.0.0
+  __TEXT.__text: 0x66394c
+  __TEXT.__auth_stubs: 0x6cd0
+  __TEXT.__objc_methlist: 0x4e36c
+  __TEXT.__const: 0xd440
   __TEXT.__dlopen_cstrs: 0x302
-  __TEXT.__cstring: 0x45c90
+  __TEXT.__cstring: 0x45d8f
   __TEXT.__swift5_typeref: 0xaffa
   __TEXT.__swift5_fieldmd: 0x4574
   __TEXT.__constg_swiftt: 0x8338

   __TEXT.__swift5_proto: 0x724
   __TEXT.__swift5_types: 0x51c
   __TEXT.__swift5_capture: 0x2478
-  __TEXT.__oslogstring: 0x2065b
+  __TEXT.__oslogstring: 0x20b95
   __TEXT.__swift_as_entry: 0x21c
   __TEXT.__swift_as_ret: 0x244
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x9938
+  __TEXT.__gcc_except_tab: 0x9a58
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x16800
+  __TEXT.__unwind_info: 0x16840
   __TEXT.__eh_frame: 0x9a04
-  __TEXT.__objc_classname: 0xc9fe
-  __TEXT.__objc_methname: 0xac007
+  __TEXT.__objc_classname: 0xca15
+  __TEXT.__objc_methname: 0xac0e6
   __TEXT.__objc_methtype: 0x15a8d
-  __TEXT.__objc_stubs: 0x6b060
-  __DATA_CONST.__got: 0x5f98
+  __TEXT.__objc_stubs: 0x6b160
+  __DATA_CONST.__got: 0x5fa0
   __DATA_CONST.__const: 0xefb0
   __DATA_CONST.__objc_classlist: 0x2780
-  __DATA_CONST.__objc_catlist: 0x1f8
+  __DATA_CONST.__objc_catlist: 0x200
   __DATA_CONST.__objc_protolist: 0x1208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21368
+  __DATA_CONST.__objc_selrefs: 0x213a8
   __DATA_CONST.__objc_protorefs: 0x678
   __DATA_CONST.__objc_superrefs: 0x1ea8
   __DATA_CONST.__objc_arraydata: 0x9b8
-  __AUTH_CONST.__auth_got: 0x3670
-  __AUTH_CONST.__auth_ptr: 0x1ad0
-  __AUTH_CONST.__const: 0x110f8
-  __AUTH_CONST.__cfstring: 0x22220
-  __AUTH_CONST.__objc_const: 0x8b420
+  __AUTH_CONST.__auth_got: 0x3678
+  __AUTH_CONST.__auth_ptr: 0x1aa0
+  __AUTH_CONST.__const: 0x11158
+  __AUTH_CONST.__cfstring: 0x222c0
+  __AUTH_CONST.__objc_const: 0x8b498
   __AUTH_CONST.__objc_intobj: 0x1bc0
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x5c8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 36875
-  Symbols:   30818
-  CStrings:  38084
+  Functions: 36883
+  Symbols:   30828
+  CStrings:  38104
 
Symbols:
+ _HFForceHomeHubMigrationBannerVisible
+ _OBJC_CLASS_$_HFMatterAccessoryLikeItemProvider
CStrings:
+ "%s: bulletinBoardNotificationByEndpoint: %@ for accessory: %@"
+ "(HMHome:hf_homeHubMigrationBannerDescription:) homeUUID = %{public}@ | Resident contains both ATV and HP | atvs.count = %ld | atvsHH1EOL.count = %ld | hps.count = %ld | hpsHH1EOL.count = %ld | enabledResidents.count = %ld | allResidentsCount = %ld | isOwner = %{BOOL}d"
+ "(HMHome:hf_homeHubMigrationBannerDescription:) homeUUID = %{public}@ | allResidentsAreATVsWithHH1EOL = YES | atvs.count = %ld | atvsHH1EOL.count = %ld | enabledResidents.count = %ld | allResidentsCount = %ld | isOwner = %{BOOL}d"
+ "(HMHome:hf_homeHubMigrationBannerDescription:) homeUUID = %{public}@ | allResidentsAreHPsWithHH1EOL = YES | hps.count = %ld | hpsHH1EOL.count = %ld | enabledResidents.count = %ld | allResidentsCount = %ld | isOwner = %{BOOL}d"
+ "(HMHome:hf_homeHubMigrationBannerDescription:) homeUUID = %{public}@ | allResidentsAreiPads = YES | enabledResidents.count = %ld | enabledIPads.count = %ld | isOwner = %{BOOL}d"
+ "(HUDashboardViewController:didSelectHomeHubMigrationBanner) userTappedLearnMore %{BOOL}d"
+ "(HUHomeHubMigrationBannerItem:shouldHideForHomes:withUserDefaults:softwareUpdateCounter) Forcing home hub migration banner to be visible."
+ "<HMHome+HomeHubMigrationBanner-hf_isHomeHubMigrationBannerVisible:> Showing HH2 migration banner: %{BOOL}d | canUpdateToHH2: %{BOOL}d | isOwner:%{BOOL}d | migrationAvailable:%{BOOL}d | userAlreadyOptedIn:%{BOOL}d | shouldPostHH2UgradeRequired: %{BOOL}d"
+ "<HUSoftwareUpdateStandaloneViewController-bannerView:footerViewTapped:> Completed handling migration banner tapping with result %@"
+ "<HUSoftwareUpdateStandaloneViewController-bannerView:footerViewTapped:> userTappedLearnMore from software update banner %{BOOL}d | hpSWUpdateInProgress = %{BOOL}d"
+ "ControlCenterSharedStateManager init"
+ "HULearnMoreTitle"
+ "HUResidentSWUpdateRequired_AllResidentsAreATVsWithHH1EOL_Description"
+ "HUResidentSWUpdateRequired_AllResidentsAreHomePodsWithHH1EOL_Description"
+ "HUResidentSWUpdateRequired_HasHH1EOL_Description"
+ "HUResidentSWUpdateRequired_NonOwner_Description"
+ "HUSoftwareUpdateHomeKitUpdateRequiredDescription_accessoriesOnly"
+ "HomeHubMigrationBanner"
+ "_hh1EOLAccessories:"
+ "hf_allResidentAccessories"
+ "hf_homeHubMigrationBannerDescription"
+ "hf_homeHubMigrationBannerTitle"
+ "hf_isHomeHubMigrationBannerVisible"
+ "hf_shouldDisplayHH2UpdateLearnMore"
+ "hf_shouldPostHH2UgradeRequired"
+ "itemProviderInHome:inRoom:"
+ "majorVersion"
- "%@ HH2 migration banner. Owner:%@ migrationAvailable:%@ userAlreadyOptedIn:%@"
- "%s: bulletinBoardNotificationByEndpoint: %@"
- "HUSafetyAndSecuritySoftwareUpdateImproveReliabilityAndPerformance"
- "Hiding HH2 migration banner. Owner:%@ migrationAvailable:%@ userAlreadyOptedIn:%@"
- "Should show HH2 migration banner?:NO Owner:%{BOOL}d migrationAvailable:%{BOOL}d userAlreadyOptedIn:%{BOOL}d. Skipping user defaults and software update checks."
- "Showing HH2 migration banner. Owner:%@ migrationAvailable:%@ userAlreadyOptedIn:%@"
- "hf_shouldPostHomeUgradeRequired"

```

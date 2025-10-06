## SensorKitUI

> `/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`

```diff

-707.0.47.0.0
-  __TEXT.__text: 0xba64
+756.0.25.0.0
+  __TEXT.__text: 0xc10c
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0xe94
-  __TEXT.__cstring: 0x1832
-  __TEXT.__oslogstring: 0x87b
+  __TEXT.__objc_methlist: 0xefc
+  __TEXT.__cstring: 0x19f0
+  __TEXT.__oslogstring: 0x8d8
   __TEXT.__const: 0x2c
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__ustring: 0x5a2
-  __TEXT.__unwind_info: 0x344
+  __TEXT.__unwind_info: 0x350
   __TEXT.__objc_classname: 0x2ac
-  __TEXT.__objc_methname: 0x4b6f
+  __TEXT.__objc_methname: 0x4d69
   __TEXT.__objc_methtype: 0x11f6
-  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_stubs: 0x3440
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2690
-  __DATA_CONST.__objc_selrefs: 0xe38
+  __DATA_CONST.__objc_const: 0x2760
+  __DATA_CONST.__objc_selrefs: 0xe90
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x1cc0
   __AUTH_CONST.__auth_got: 0x1e0
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17270265-7ABF-39D7-89F3-31602BAEDC8D
-  Functions: 315
-  Symbols:   1453
-  CStrings:  1392
+  UUID: 9AF72791-3968-3154-B71F-68E2FC77333F
+  Functions: 326
+  Symbols:   1488
+  CStrings:  1438
 
Symbols:
+ +[NSURL sk_PreferencesMotionAndFitness]
+ -[SRAuthorizationCategoryDetailCell numberOfWhatIsSharedLabels]
+ -[SRAuthorizationCategoryDetailCell setNumberOfWhatIsSharedLabels:]
+ -[SRAuthorizationCategoryDetailCell setWhatIsSharedLabels:]
+ -[SRAuthorizationCategoryDetailCell whatIsSharedLabels]
+ -[SRAuthorizationCategoryDetailCell whatIsSharedTitleLabel]
+ -[SRAuthorizationGroup localizedWhatIsShared]
+ -[SRResearchDataPerCategoryViewController datastoreBackend]
+ -[SRResearchDataPerCategoryViewController navigateToAuthorization]
+ -[SRResearchDataPerCategoryViewController setDatastoreBackend:]
+ _OBJC_IVAR_$_SRAuthorizationCategoryDetailCell._numberOfWhatIsSharedLabels
+ _OBJC_IVAR_$_SRAuthorizationCategoryDetailCell._whatIsSharedLabels
+ _OBJC_IVAR_$_SRResearchDataPerCategoryViewController._datastoreBackend
+ __OBJC_$_PROP_LIST_SRRemoteAuthorizationPromptViewController.104
+ ___113+[SRAuthorizationCategoryDetailCell categoryDetailCellForAuthGroup:bundle:titleFont:bodyFont:textColor:OBKStyle:]_block_invoke_4
+ ___53-[SRResearchDataPerCategoryViewController exportData]_block_invoke.56
+ ___54-[SRResearchDataPerCategoryViewController viewDidLoad]_block_invoke.14
+ ___block_literal_global.61
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$datastoreBackend
+ _objc_msgSend$localizedWhatIsShared
+ _objc_msgSend$navigateToAuthorization
+ _objc_msgSend$openSensitiveURL:withOptions:error:
+ _objc_msgSend$setDatastoreBackend:
+ _objc_msgSend$setNumberOfWhatIsSharedLabels:
+ _objc_msgSend$setWhatIsSharedLabels:
+ _objc_msgSend$whatIsSharedLabels
+ _objc_msgSend$whatIsSharedTitleLabel
+ _objc_opt_self
+ _objc_release_x19
- __OBJC_$_PROP_LIST_SRRemoteAuthorizationPromptViewController.103
- ___53-[SRResearchDataPerCategoryViewController exportData]_block_invoke.53
- ___54-[SRResearchDataPerCategoryViewController viewDidLoad]_block_invoke_3
- ___block_literal_global.60
- _objc_release_x22
- _objc_release_x24
CStrings:
+ "Collected data is stored in Motion & Fitness. You can manage this data in Motion & Fitness privacy settings."
+ "Error opening %{public}@ because %{public}@"
+ "Failed to find sensor description for %{public}@"
+ "Once data has been shared to authorized studies it cannot be retrieved or deleted."
+ "SRWhatIsShared"
+ "Show Motion & Fitness Privacy"
+ "T@\"NSArray\",&,N,V_whatIsSharedLabels"
+ "T@\"NSString\",?,R,C"
+ "T@\"UILabel\",R,N,V_whatIsSharedTitleLabel"
+ "Tq,N,V_datastoreBackend"
+ "Tq,N,V_numberOfWhatIsSharedLabels"
+ "URLWithString:"
+ "What is shared:"
+ "_datastoreBackend"
+ "_numberOfWhatIsSharedLabels"
+ "_whatIsSharedLabels"
+ "_whatIsSharedTitleLabel"
+ "datastoreBackend"
+ "deleteAllFooterLongTermDatastore"
+ "downloadAllFooterFaceMetrics"
+ "exportAllFooterLongTerm"
+ "followUpActionLabelTitle"
+ "localizedWhatIsShared"
+ "navigateToAuthorization"
+ "numberOfWhatIsSharedLabels"
+ "openSensitiveURL:withOptions:error:"
+ "prefs:root=Privacy&path=MOTION"
+ "setDatastoreBackend:"
+ "setNumberOfWhatIsSharedLabels:"
+ "setWhatIsSharedLabels:"
+ "showMotionFitnessTitleLabel"
+ "whatIsSharedLabels"
+ "whatIsSharedTitleLabel"

```

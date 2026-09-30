## SiriUIBridge

> `/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge`

```diff

-3400.23.1.0.0
-  __TEXT.__text: 0x14c24
-  __TEXT.__auth_stubs: 0xd60
+3400.26.1.0.0
+  __TEXT.__text: 0x14ce0
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x7a4
   __TEXT.__const: 0x302
   __TEXT.__cstring: 0xbeb

   __TEXT.__objc_methname: 0x13aa
   __TEXT.__objc_methtype: 0x7e3
   __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__auth_ptr: 0x180
   __AUTH_CONST.__const: 0x18b0
   __AUTH_CONST.__cfstring: 0x160

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 879
-  Symbols:   496
-  CStrings:  124
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 881
+  Symbols:   505
+  CStrings:  8
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x01\xc0\xe1j\xb8\xf4 >\x01\xc0\xe1j\xd8\xf4 >\x01\xc0\xe1j\xf8\xf4 >\x01\xc0\xe1j\x18\xf5 >\x01\xc0\xe1j8\xf5 >\x01\xc0\xe1jX\xf5 >\x01\xc0\xe1jx\xf5 >\x01\xc0\xe1j\x98\xf5 >\x01\xc0\xe1j\xb8\xf5 >\x01\xc0\xe1j\xd8\xf5 >\x01\xc0\xe1j\xf8\xf5 >\x01\xc0\xe1j\x18\xf6 >\x01\xc0\xe1j8\xf6 >\x01\xc0\xe1jX\xf6 >\x01\xc0\xe1jx\xf6 >\x01\xc0\xe1j\x98\xf6 >\x01\xc0\xe1j\xb8\xf6 >\x01\xc0\xe1j\xd8\xf6 >\x01\xc0\xe1j\xf8\xf6 >\x01\xc0\xe1j\x18\xf7 >\x01\xc0\xe1j8\xf7 >\x01\xc0\xe1jX\xf7 >\x01\xc0\xe1jx\xf7 >\x01\xc0\xe1j\x98\xf7 >\x01\xc0\xe1j\xb8\xf7 >\x01\xc0\xe1j\xd8\xf7 >\x01\xc0\xe1j\xf8\xf7 >\x01\xc0\xe1j\x18\xf8 >\x01\xc0\xe1j8\xf8 >\x01\xc0\xe1jX\xf8 >\x01\xc0\xe1jx\xf8 >\x01\xc0\xe1j\x98\xf8 >\x01\xc0\xe1j\xb8\xf8 >\x01\xc0\xe1j\xd8\xf8 >\x01\xc0\xe1j\xf8\xf8 >\x01\xc0\xe1j\x18\xf9 >\x01\xc0\xe1j8\xf9 >\x01\xc0\xe1jX\xf9 >\x01\xc0\xe1jx\xf9 >\x01\xc0\xe1j\x98\xf9 >\x01\xc0\xe1j\xb8\xf9 >\x01\xc0\xe1j\xd8\xf9 >\x01\xc0\xe1j\xf8\xf9 >\x01\xc0\xe1j\x18\xfa >\x01\xc0\xe1j8\xfa >\x01\xc0\xe1jX\xfa >\x01\xc0\xe1jx\xfa >\x01\xc0\xe1j\x98\xfa >\x01\xc0\xe1j\xb8\xfa >\x01\xc0\xe1j\xd8\xfa >\x01\xc0\xe1j\xf8\xfa >\x01\xc0\xe1j\x18\xfb >\x01\xc0\xe1j8\xfb >\x01\xc0\xe1jX\xfb >\x01\xc0\xe1jx\xfb >\x01\xc0\xe1j\x98\xfb >\x01\xc0\xe1j\xb8\xfb >\x01\xc0\xe1j\xd8\xfb >\x01\xc0\xe1j\xf8\xfb >\x01\xc0\xe1j\x18\xfc >\x01\xc0\xe1j8\xfc >\x01\xc0\xe1jX\xfc >\x01\xc0\xe1jx\xfc >\x01\xc0\xe1j\x98\xfc >\x01\xc0\xe1j\xb8\xfc >\x01\xc0\xe1j\xd8\xfc >\x01\xc0\xe1j\xf8\xfc >\x01\xc0\xe1j\x18\xfd >\x01\xc0\xe1j8\xfd >\x01\xc0\xe1jX\xfd >\x01\xc0\xe1jx\xfd >\x01\xc0\xe1j\x98\xfd >\x01\xc0\xe1j\xb8\xfd >\x01\xc0\xe1j\xd8\xfd >\x01\xc0\xe1j\xf8\xfd >\x01\xc0\xe1j\x18\xfe >\x01\xc0\xe1j8\xfe >\x01\xc0\xe1jX\xfe >\x01\xc0\xe1jx\xfe >\x01\xc0\xe1j\x98\xfe >\x01\xc0\xe1j\xb8\xfe >\x01\xc0\xe1j\xd8\xfe >\x01\xc0\xe1j\xf8\xfe >\x01\xc0\xe1j\x18\xff >\x01\xc0\xe1j8\xff >\x01\xc0\xe1jX\xff >\x01\xc0\xe1jx\xff >\x01\xc0\xe1j\x98\xff >\x01\xc0\xe1j\xb8\xff >\x01\xc0\xe1j\xd8\xff >\x01\xc0\xe1j\xf8\xff >\x01\xc0\xe1j\x18"
+ "!>\x01\xc0\xe1j8"
+ "!>\x01\xc0\xe1jX"
+ "!>\x01\xc0\xe1jx"
+ "!>\x01\xc0\xe1j\x98"
+ "!>\x01\xc0\xe1j\xb8"
+ "!>\x01\xc0\xe1j\xd8"
+ "!>\x01\xc0\xe1j\xf8"
- "_$s10Foundation16AttributedStringV18HealthExperienceUIE13mapOutUIFontsACyF"
- "_$s12CoreGraphics7CGFloatV18HealthExperienceUIE16viewCornerRadiusACvgZ"
- "_$s12CoreGraphics7CGFloatV18HealthExperienceUIE18buttonCornerRadiusACvgZ"
- "_$s14HealthPlatform14PluginFeedItemV0A12ExperienceUIE011makeSidebardE015displayCategory17actionHandlerType0lM8UserData13sourceProfile7sectionACSo09HKDisplayK0C_xm10Foundation0P0VSgAA06SourceR0OAD0I7SectionOtKAD019ConfigurationActionM0RzlFZ"
- "_$s14HealthPlatform14PluginFeedItemV0A12ExperienceUIE011makeSidebardE026configurationProviderClass9viewModel15automationTitle17actionHandlerType0qR8UserData16uniqueIdentifier13sourceProfile7sectionACxm_04ViewN0QzSgSSq_m10Foundation0U0VSgSSAA06SourceY0OAD0I7SectionOtKAD0c13ConfigurationK0RzAD019ConfigurationActionR0R_r0_lFZ"
- "_$s14HealthPlatform14PluginFeedItemV0A12ExperienceUIE011makeSidebardE09viewModel16uniqueIdentifier13sourceProfile7sectionAcD0i13ConfigurationK0V_SSAA06SourceO0OAD0I7SectionOtKFZ"
- "_$s16HealthExperience21AnalyticsTransformingP0aB2UIE15analyticsString3forSSAD12PresentationO_tFZ"
- "_$s18HealthExperienceUI018DataTypeTileHeaderD6SourcePAAE06headerE0AA0fgE0Ovg"
- "_$s18HealthExperienceUI018DataTypeTileHeaderD6SourcePAAE11dateUpdated10Foundation4DateVSgvg"
- "_$s18HealthExperienceUI023DataTypeDetailFavoritesD6SourceC06objectE020managedObjectContext20pinnedContentManager11healthStore14sourceProfiles11headerTitle21layoutBackgroundColor22contentInsetsReferenceACSo08HKObjectE0C_So09NSManagedkL0C0A8Platform06PinnedN8Managing_pSo08HKHealthQ0CSayAP0H7ProfileOGSSSo7UIColorCSgSo09UIContentZ9ReferenceVtcfc"
- "_$s18HealthExperienceUI023DataTypeDetailFavoritesD6SourceCMa"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC05imageH0So07UIImageH0Cvg"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC07messagegH0AA0defgH0Cvg"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC0H5ModelV5image15attributedTitle4body10actionText12hasSeparator15backgroundColor20automationIdentifierAESo7UIImageC_So18NSAttributedStringCSSSgSSSbSo7UIColorCSStcfC"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC0H5ModelV5image5title4body10actionText12hasSeparator15backgroundColor20automationIdentifierAESo7UIImageC_S2SSgSSSbSo7UIColorCSStcfC"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC0H5ModelVMa"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageC11updateViewsyyAC0H5ModelVFTj"
- "_$s18HealthExperienceUI025MessageWithActionTileViewE5ImageCMu"
- "_$s18HealthExperienceUI10HeightItemV6height14valueFormatterACSo10HKQuantityCSg_AA019ConfirmDetailsValueH0_ptcfC"
- "_$s18HealthExperienceUI10HeightItemVMa"
- "_$s18HealthExperienceUI14SidebarSectionOMa"
- "_$s18HealthExperienceUI15MultilineButtonCMa"
- "_$s18HealthExperienceUI15MultiselectItemV5title8subtitle29accessibilityIdentifierPrefix5state10identifierACSS_S2SSgSbSStcfC"
- "_$s18HealthExperienceUI15MultiselectItemVMa"
- "_$s18HealthExperienceUI17PDFVerticalSpacerVMa"
- "_$s18HealthExperienceUI17PDFVerticalSpacerVyAC12CoreGraphics7CGFloatVcfC"
- "_$s18HealthExperienceUI20InteractivePickerRowV15hidePlaceholder5label15showClearButton05clearL7OnRight10onInteract21placeholderVisibility24baseAutomationIdentifier05inputE4View0rX0ACyxq_G05SwiftC07BindingVySbG_SSS2byycSgAA0hS4RuleOSSxycq_yctcfC"
- "_$s18HealthExperienceUI20InteractivePickerRowVMa"
- "_$s18HealthExperienceUI21CellSelectionHandlingP012shouldSelectD0_2inSbSo6UIViewC_So0J10ControllerCtFTj"
- "_$s18HealthExperienceUI21CellSelectionHandlingP029selectionShouldFollowFocusForD0_2inSbSgSo6UIViewC_So0M10ControllerCtFTj"
- "_$s18HealthExperienceUI21CellSelectionHandlingP09didSelectD0_2inySo6UIViewC_So0J10ControllerCtFTj"
- "_$s18HealthExperienceUI21CellSelectionHandlingP19deselectionBehavior2inAA0d11DeselectionH0OSo16UIViewControllerC_tFTj"
- "_$s18HealthExperienceUI21CellSelectionHandlingP19deselectionBehaviorAA0d11DeselectionH0OvgTj"
- "_$s18HealthExperienceUI21CellSelectionHandlingPA2A016SectionedAdaptorD0RzrlE09didSelectD0_2inySo6UIViewC_So0L10ControllerCtF"
- "_$s18HealthExperienceUI21CellSelectionHandlingPAAE029selectionShouldFollowFocusForD0_2inSbSgSo6UIViewC_So0M10ControllerCtF"
- "_$s18HealthExperienceUI21CellSelectionHandlingPAAE19deselectionBehavior2inAA0d11DeselectionH0OSo16UIViewControllerC_tF"
- "_$s18HealthExperienceUI21CellSelectionHandlingPAAE36deselectOnRegularHorizontalSizeClass3forAA0D19DeselectionBehaviorOSo16UIViewControllerC_tF"
- "_$s18HealthExperienceUI21TextTableViewItemCellCMa"
- "_$s18HealthExperienceUI22DataTypeTileHeaderViewC06updateD6SourceyyAA0fgdJ0_pSgFTj"
- "_$s18HealthExperienceUI22DataTypeTileHeaderViewC10dataSourceAA0fgdJ0_pSgvgTj"
- "_$s18HealthExperienceUI22DataTypeTileHeaderViewCMa"
- "_$s18HealthExperienceUI22NotificationGeneratingPAAE06createD24EnabledDefaultsPublisher4with3for7Combine03AnyI0VySbs5NeverOGSo13HKHealthStoreC_AA013SharedProfileD4TypeOtFZ"
- "_$s18HealthExperienceUI22NotificationGeneratingPAAE06createD8UserInfo3for4with4uuidSDys11AnyHashableVypGSo20HKNotificationDomainV_10Foundation3URLVSgAM4UUIDVSgtFZ"
- "_$s18HealthExperienceUI22NotificationGeneratingPAAE17notificationSoundSo014UNNotificationG0CvgZ"
- "_$s18HealthExperienceUI23CellDeselectionBehaviorOMa"
- "_$s18HealthExperienceUI25DismissibleCellHeaderViewV0G5ModelC9titleText15systemImageName06detailJ015foregroundColor17detailsVisibilityAESS_SSSgAA0ef6DetailJ0OSg0aB00P14RepresentationOSgAA0ef7DetailsR0Vtcfc"
- "_$s18HealthExperienceUI25DismissibleCellHeaderViewV0G5ModelCMa"
- "_$s18HealthExperienceUI25PlaceholderVisibilityRuleOMa"
- "_$s18HealthExperienceUI25SidebarConfigurationModelV5title19imageRepresentation05colorI016indentationLevelACSS_0aB005ImageI0OAH05ColorI0OSgSitcfC"
- "_$s18HealthExperienceUI25SidebarConfigurationModelVMa"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV011GetMoreFromA9ComponentV02hkE019additionalPredicateAESo08HKObjectE0CSg_So11NSPredicateCSgtcfC"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV011GetMoreFromA9ComponentV04makeD6Source7contextAA08SnapshotdM0_pSgAC7ContextV_tF"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV011GetMoreFromA9ComponentVMa"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV04makeD6Source7contextAA017CompoundSectioneddI0CAC7ContextV_tF"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV15childComponentsACSayAA0deF9Component_pG_tcfC"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV19ComponentIdentifierO9promotionSSvgZ"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV22VerticalGroupComponentV10identifier15childComponentsAESS_SayAA0defJ0_pGtcfC"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV7ContextV06healthB5Store0A8Platform0abJ0_pvg"
- "_$s18HealthExperienceUI27DataTypeDetailConfigurationV7ContextV06healthB5Store0iJ04mode20pinnedContentManager05chartH023restorationUserActivityAE0A8Platform0abJ0_p_So08HKHealthJ0CAA0deF4ModeOAL06PinnedM8Managing_pSgAA05ChartH0CSgSo06NSUserR0CSgtcfC"
- "_$s18HealthExperienceUI28SidebarConfigurationProviderC011makeContentE02id9viewModel0J7Context9cellState013actionHandlerH05UIKit09UIContentE0_pSS_AA0deK0VAA012ProvidedViewL0CAA014ObservableCellN0CAA0e14FeedItemActionH0VSgtKFTj"
- "_$s18HealthExperienceUI28SidebarConfigurationProviderC014makeBackgroundE09cellState5UIKit012UIBackgroundE0VSgAA014ObservableCellJ0C_tFTj"
- "_$s18HealthExperienceUI28SidebarConfigurationProviderC15makeAccessoriesSay5UIKit15UICellAccessoryVGyFTj"
- "_$s18HealthExperienceUI28SidebarConfigurationProviderCACycfc"
- "_$s18HealthExperienceUI28SidebarConfigurationProviderCMa"
- "_$s18HealthExperienceUI30DataSourceWithSectionItemLimitC6source04itemI0ACyxGx_Sitcfc"
- "_$s18HealthExperienceUI30DataSourceWithSectionItemLimitCMa"
- "_$s18HealthExperienceUI31CameraScannerOverlayContentViewC04makee17ActionIntroHeaderH05imageSo07UIImageH0CSo0N0CSg_tFZ"
- "_$s18HealthExperienceUI31CameraScannerOverlayContentViewC04makee21ActionCheckmarkHeaderH0So07UIImageH0CyFZ"
- "_$s18HealthExperienceUI31CameraScannerOverlayContentViewCMa"
- "_$s18HealthExperienceUI33ContentConfigurationTableViewCellCMa"
- "_$s18HealthExperienceUI34FetchedResultsWithLayoutDataSourceCMa"
- "_$s18HealthExperienceUI34FetchedResultsWithLayoutDataSourceC_6layoutACyxGSo09NSFetchedE10ControllerCyxG_So012NSCollectionG7SectionCtcfc"
- "_$s18HealthExperienceUI35DataTypeDetailConfigurationProviderP13configuration3forAA0defG0VSo08HKObjectE0C_tKFTj"
- "_$s18HealthExperienceUI35FeatureOnboardingTileViewControllerC011headerImageG0So07UIImageG0CvgTj"
- "_$s18HealthExperienceUI35FeatureOnboardingTileViewControllerC11headerTitleSo7UILabelCvgTj"
- "_$s18HealthExperienceUI35FeatureOnboardingTileViewControllerC7contextAA08FeedItemgH7Context_pSgvgTj"
- "_$s18HealthExperienceUI36CollectionHeaderWithIconReusableViewCMa"
- "_$s18HealthExperienceUI36DataTypeDetailChildComponentMutatingPAAE06insertH0_2at9directionSbAA0defH0_p_SSAA0deF13ConfigurationV17MutationDirectionOtF"
- "_$s18HealthExperienceUI36DataTypeDetailChildComponentMutatingPAAE07replaceH0_4withSbSS_AA0defH0_pSgtF"
- "_$s18HealthExperienceUI38AllHighlightsForDataTypeViewControllerC02hkH011healthStore0lbM008hideShowD6Button10provenanceACSo08HKObjectH0C_So08HKHealthM0C0A8Platform0abM0_pSbSSSgtcfc"
- "_$s18HealthExperienceUI38AllHighlightsForDataTypeViewControllerCMa"
- "_$s18HealthExperienceUI42ContentConfigurationCollectionViewListCellCMa"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC10headerIconSo7UIImageCSgvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC11headerTitleSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC13bulletOneIconSo7UIImageCvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC13bulletTwoIconSo7UIImageCvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC14bulletOneTitleSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC14bulletTwoTitleSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC15bulletThreeIconSo7UIImageCvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC16bulletThreeTitleSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC20bulletOneDescriptionSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC20bulletTwoDescriptionSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerC22bulletThreeDescriptionSSvgZ"
- "_$s18HealthExperienceUI42SummarySharingOnboardingInfoViewControllerCMa"
- "_$s18HealthExperienceUI47DataTypeDetailRoomEntryAnalyticsEventSubmittingPAAE04sendghiJ006objectE019chartOverlayVersion11healthStoreySo08HKObjectE0C_So07HKChartoP0aSo08HKHealthR0CtF"
- "_$s18HealthExperienceUI47DataTypeDetailRoomEntryAnalyticsEventSubmittingPAAE04sendghiJ010identifier19chartOverlayVersion11healthStoreySS_So07HKChartoP0aSo08HKHealthR0CtF"
- "_$s18HealthExperienceUI52StandardWithChartDataTypeDetailConfigurationProviderV13configuration3forAA0ghiJ0VSo08HKObjectH0C_tF"
- "_$s18HealthExperienceUI52StandardWithChartDataTypeDetailConfigurationProviderVACycfC"
- "_$s18HealthExperienceUI52StandardWithChartDataTypeDetailConfigurationProviderVMa"
- "_$s18HealthExperienceUI57StandardWithSampleListDataTypeDetailConfigurationProviderV13configuration3forAA0hijK0VSo08HKObjectI0C_tF"
- "_$s18HealthExperienceUI57StandardWithSampleListDataTypeDetailConfigurationProviderVACycfC"
- "_$s18HealthExperienceUI57StandardWithSampleListDataTypeDetailConfigurationProviderVMa"
- "_$s18HealthExperienceUI7PDFGridC7columns10rowSpacing06columnG0_ACSi_12CoreGraphics7CGFloatVAISayAA13PDFRenderable_pGyXEtcfc"
- "_$s18HealthExperienceUI7PDFGridCMa"
- "_$s18HealthExperienceUI8HostViewC06parentE10ControllerSo06UIViewG0CSgvgTj"
- "_$s18HealthExperienceUI8HostViewC06parentE10ControllerSo06UIViewG0CSgvsTj"
- "_$s18HealthExperienceUI8HostViewC14hostedViewableAA0G0_pSgvgTj"
- "_$s18HealthExperienceUI8HostViewC14hostedViewableAA0G0_pSgvsTj"
- "_$s18HealthExperienceUI8HostViewCMa"
- "_$s7Combine12AnyPublisherV18HealthExperienceUI0D8Platform17NotifiableContentRzrlE26executeNotificationRequestyyF"
- "_$sSS18HealthExperienceUIE29sidebarCategoryFeedItemPrefixSSvgZ"
- "_$sSo11UITableViewC18HealthExperienceUIE12registerCellyyxmAC08ReusableB0RzlF"
- "_$sSo17HKDisplayCategoryC18HealthExperienceUIE25sidebarFeedItemIdentifierSSvg"
- "_$sSo18NSAttributedStringC18HealthExperienceUIE24copyWithUnbreakableWordsSo019NSMutableAttributedB0CyF"
- "_$sSo19HKFeatureIdentifiera18HealthExperienceUIE11descriptionSSvg"
- "_$sSo6UIFontC18HealthExperienceUIE10createFont4with6weight6traits7rounded26maximumContentSizeCategory19respectsDynamicTypeABSo0A9TextStylea_So0A6WeightaSgSo0A24DescriptorSymbolicTraitsVSbSo09UIContentmN0aSgSbtFZ"
- "_$sSo6UIViewC18HealthExperienceUIE12roundCorners6radius5curve06maskedF0y12CoreGraphics7CGFloatV_So18CALayerCornerCurveaSo12CACornerMaskVtF"
- "_$sSo6UIViewC18HealthExperienceUIE17resetCornerRadiusyyF"
- "_$sSo6UIViewC18HealthExperienceUIE22isTouchOnAccessoryView_09accessoryI025minimumTappableDimensionsSbSo7UITouchC_ABSgSo6CGSizeVtF"
- "ctionHandlingPAAE19deselectionBehaviorAA0d11DeselectionH0Ovg"
- "iderACyxGSo09NSFetchedE10ControllerCyxG_So012NSCollectiongK0CAA014CollectionViewG7ContextVKctcfc"
- "lthExperienceUI025MessageWithActionTileViewE5ImageCMa"
- "ntext07featureG00A8Platform06PluginhI0VSgAG16GeneratorContextV_0A12KitAdditions0fG0OtF"
- "onTileViewE5ImageC9ConstantsO10imageWidth12CoreGraphics7CGFloatVvgZ"

```

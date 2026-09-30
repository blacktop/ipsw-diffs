## AppStoreComponents

> `/System/iOSSupport/System/Library/PrivateFrameworks/AppStoreComponents.framework/Versions/A/AppStoreComponents`

```diff

-7.2.15.0.0
-  __TEXT.__text: 0x6d0a4
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x5d40
-  __TEXT.__const: 0x11c4
+7.4.13.0.0
+  __TEXT.__text: 0x6cfb0
+  __TEXT.__auth_stubs: 0x1560
+  __TEXT.__objc_methlist: 0x635c
+  __TEXT.__const: 0x11f4
   __TEXT.__gcc_except_tab: 0x7c8
-  __TEXT.__cstring: 0x3372
+  __TEXT.__cstring: 0x33a2
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__oslogstring: 0x2d26
+  __TEXT.__oslogstring: 0x2d95
   __TEXT.__constg_swiftt: 0x634
   __TEXT.__swift5_typeref: 0x3b8
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x9f0
+  __TEXT.__swift5_reflstr: 0x9e0
   __TEXT.__swift5_fieldmd: 0x928
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_proto: 0xe8
   __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x1d0
-  __TEXT.__unwind_info: 0x1e50
+  __TEXT.__unwind_info: 0x1ea8
   __TEXT.__objc_classname: 0xcd9
-  __TEXT.__objc_methname: 0xd14a
-  __TEXT.__objc_methtype: 0x1e0b
-  __TEXT.__objc_stubs: 0x9700
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x1630
+  __TEXT.__objc_methname: 0xd248
+  __TEXT.__objc_methtype: 0x1e17
+  __TEXT.__objc_stubs: 0x9780
+  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__const: 0x1628
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cc0
+  __DATA_CONST.__objc_selrefs: 0x2d70
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0xad0
+  __AUTH_CONST.__auth_got: 0xac0
   __AUTH_CONST.__const: 0x1988
   __AUTH_CONST.__cfstring: 0x4180
-  __AUTH_CONST.__objc_const: 0xc5c0
+  __AUTH_CONST.__objc_const: 0xbb10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x22e0

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B2D9BC99-B39A-36F8-895D-F2A91ED4EB79
-  Functions: 2861
-  Symbols:   6026
-  CStrings:  3996
+  UUID: 6B86AECA-D85B-33E8-9259-F732CC919102
+  Functions: 2925
+  Symbols:   6095
+  CStrings:  4005
 
Symbols:
+ +[ASCAppLaunchTrampoline log].cold.1
+ +[ASCAppOfferStateCenter log].cold.1
+ +[ASCAppOfferStateCenter sharedCenter].cold.1
+ +[ASCAppearMetricsPresenter log].cold.1
+ +[ASCArtworkFetcher sharedFetcher].cold.1
+ +[ASCDefaultLockupTheme sharedTheme].cold.1
+ +[ASCDefaults daemonDefaults].cold.1
+ +[ASCHasher executionSeed].cold.1
+ +[ASCLockupFetcher sharedFetcher].cold.1
+ +[ASCLockupPresenter log].cold.1
+ +[ASCLockupViewGroup log].cold.1
+ +[ASCMetrics sharedMetrics].cold.1
+ +[ASCMetricsActivity defaultFields].cold.1
+ +[ASCOfferButton progressStateImageFittingSize:forTheme:startPercent:endPercent:useFullImageSize:].cold.1
+ +[ASCOfferButton smallTitleFontForText:compatibleWithTraitCollection:].cold.1
+ +[ASCOfferButton subtitleFontFittingSize:forTheme:compatibleWithTraitCollection:].cold.1
+ +[ASCOfferButton textBackgroundImageFittingSize:forTheme:].cold.1
+ +[ASCOfferTheme adTheme].cold.1
+ +[ASCOfferTheme blueTheme].cold.1
+ +[ASCOfferTheme essoTheme].cold.1
+ +[ASCOfferTheme grayTheme].cold.1
+ +[ASCOfferTheme viewInAppStoreTheme].cold.1
+ +[ASCOfferTheme whiteOnGrayTheme].cold.1
+ +[ASCOfferTheme whiteTheme].cold.1
+ +[ASCOverlaySettings sharedSettings].cold.1
+ +[ASCPresenterContext sharedContext].cold.1
+ +[ASCRebootstrapNotifier sharedNotifier].cold.1
+ +[ASCSemanticColor artworkBorder].cold.1
+ +[ASCSemanticColor artworkPlaceholder].cold.1
+ +[ASCSemanticColor artworkSymbolTint].cold.1
+ +[ASCServicesConnection log].cold.1
+ +[ASCServicesConnection sharedConnection].cold.1
+ +[ASCTaskCoordinator log].cold.1
+ +[ASCUtilities shared].cold.1
+ +[ASCWatchApps sharedWatchApps].cold.1
+ +[ASCWorkspace log].cold.1
+ +[ASCWorkspace sharedWorkspace].cold.1
+ +[NSBundle(AppStoreComponents) asc_frameworkBundle].cold.1
+ +[NSBundle(AppStoreComponents) asc_realMainBundle].cold.1
+ +[UIColor(AppStoreComponents) _asc_highlightBlendColor].cold.1
+ -[ASCLockupContentView headingLabel].cold.1
+ -[ASCLockupContentView offerStatusLabel].cold.1
+ -[ASCLockupContentView setLockupSize:].cold.1
+ -[ASCLockupView layoutContentView].cold.1
+ -[ASCOfferButton updateLabelStyleProperties].cold.1
+ -[ASCOfferButton updateLabelStyleProperties].cold.2
+ -[ASCOfferButton updateLabelStyleProperties].cold.3
+ -[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:usingUserActivityWithPayloadURL:configuration:pendingResult:]
+ ASCAppOfferStateDelegateGetInterface.cold.1
+ ASCAppOfferStateServiceGetInterface.cold.1
+ ASCLockupFetcherServiceGetInterface.cold.1
+ ASCMetricsServiceGetInterface.cold.1
+ ASCOfferGetCodableClasses.cold.1
+ ASCServiceBrokerGetInterface.cold.1
+ ASCUtilityServiceGetInterface.cold.1
+ _NSUserActivityTypeBrowsingWeb
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSUserActivity
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __145-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:usingUserActivityWithPayloadURL:configuration:pendingResult:]_block_invoke.cold.1
+ __94-[ASCLockupViewGroup(Fetching) _lockupDictionaryForRequest:includingKeys:withCompletionBlock:]_block_invoke_2.cold.1
+ ___145-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:usingUserActivityWithPayloadURL:configuration:pendingResult:]_block_invoke
+ ___block_descriptor_49_e8_32s_e54_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^{CGContext=}40ls32l8
+ __block_literal_global.48
+ __block_literal_global.56
+ _objc_msgSend$initWithActivityType:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$openUserActivity:usingApplicationRecord:configuration:completionHandler:
+ _objc_msgSend$setWebpageURL:
- ___block_descriptor_48_e8_32s_e54_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^{CGContext=}40ls32l8
- __block_literal_global.46
- __block_literal_global.50
- __block_literal_global.54
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AppStoreComponents
- _swift_bridgeObjectRelease_n
CStrings:
+ "@\"NSObject\""
+ "Found valid universal link with no matching app, source %{public}@, target %{public}@"
+ "Open application with URL user activity failed, reason %{public}@"
+ "Open application with URL user activity succeeded."
+ "T@\"NSObject\",R,N,V_object"
+ "com.apple.GameOverlay"
+ "initWithActivityType:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "openApplicationWithBundleIdentifier:usingUserActivityWithPayloadURL:configuration:pendingResult:"
+ "openUserActivity:usingApplicationRecord:configuration:completionHandler:"
+ "pause_resume_offer_button_label_2024E"
+ "setWebpageURL:"
- "Found valid universal link with mismatching bundle ID, source %{public}@, target %{public}@"
- "T@\"<NSObject>\",R,N,V_object"
- "com.apple.GameOverlayUI"

```

## SoftwareUpdateSettingsExtension

> `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsExtension.appex/Contents/MacOS/SoftwareUpdateSettingsExtension`

```diff

-2078.80.2.0.2
-  __TEXT.__text: 0x71aa0
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_methlist: 0x430
-  __TEXT.__cstring: 0x65cf
-  __TEXT.__swift5_typeref: 0xb5ae
-  __TEXT.__swift5_capture: 0x8d4
-  __TEXT.__const: 0x44b4
-  __TEXT.__objc_methname: 0x2201
-  __TEXT.__constg_swiftt: 0x1c58
-  __TEXT.__swift5_reflstr: 0xf1f
-  __TEXT.__swift5_fieldmd: 0xc6c
+2078.101.1.0.0
+  __TEXT.__text: 0x96e48
+  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__objc_methlist: 0x93c
+  __TEXT.__cstring: 0x6ccf
+  __TEXT.__swift5_typeref: 0xcf8a
+  __TEXT.__const: 0x5a34
+  __TEXT.__constg_swiftt: 0x2904
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_assocty: 0x4d0
-  __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0x104
+  __TEXT.__swift5_reflstr: 0x135f
+  __TEXT.__swift5_fieldmd: 0x11f0
+  __TEXT.__swift5_assocty: 0x748
+  __TEXT.__swift5_capture: 0x980
+  __TEXT.__swift5_proto: 0x250
+  __TEXT.__swift5_types: 0x178
+  __TEXT.__objc_methname: 0x225c
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methtype: 0x101c
+  __TEXT.__objc_methtype: 0x1042
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_ret: 0x64
   __TEXT.__oslogstring: 0x85
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1810
-  __TEXT.__eh_frame: 0x1240
-  __DATA_CONST.__auth_got: 0xd58
-  __DATA_CONST.__got: 0x690
-  __DATA_CONST.__auth_ptr: 0xd48
-  __DATA_CONST.__const: 0x2ca8
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__unwind_info: 0x2120
+  __TEXT.__eh_frame: 0x1b18
+  __DATA_CONST.__auth_got: 0xec8
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__auth_ptr: 0x1198
+  __DATA_CONST.__const: 0x31b8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x2878
-  __DATA.__objc_selrefs: 0x720
-  __DATA.__objc_data: 0x10f0
-  __DATA.__data: 0x3430
-  __DATA.__bss: 0x3970
-  __DATA.__common: 0x50
+  __DATA.__objc_const: 0x1f58
+  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_data: 0x8f8
+  __DATA.__data: 0x5050
+  __DATA.__bss: 0x51f0
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/PackageUIKit.framework/Versions/A/PackageUIKit
   - /System/Library/PrivateFrameworks/Seeding.framework/Versions/A/Seeding
   - /System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings
+  - /System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FE304156-A6B6-38A7-AC61-5D05377F208D
-  Functions: 2430
-  Symbols:   181
-  CStrings:  990
+  UUID: 33E0AA1A-5ECA-3E50-960C-EF8319716738
+  Functions: 3165
+  Symbols:   195
+  CStrings:  1029
 
Symbols:
+ _NSFileSystemFreeSize
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_SUSharedPrefs
+ _SUOSUUserActionDetailsKeyBytesRequired
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_allocBox
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRetain_n
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCastClass
+ _swift_initEnumMetadataMultiPayload
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_makeBoxUnique
+ _swift_projectBox
+ _swift_release_n
+ _swift_retain_n
+ _swift_setDeallocating
- _OBJC_CLASS_$_SUOSUProductStub
- _OBJC_CLASS_$__TtC31SoftwareUpdateSettingsExtension15SUOSUClientStub
- _OBJC_CLASS_$__TtC31SoftwareUpdateSettingsExtension31SUOSUPreferencePaneV2Controller
- _OBJC_METACLASS_$__TtC31SoftwareUpdateSettingsExtension15SUOSUClientStub
- _OBJC_METACLASS_$__TtC31SoftwareUpdateSettingsExtension31SUOSUPreferencePaneV2Controller
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _swift_getAssociatedTypeWitness
CStrings:
+ "\nEnforcedWithin24Hours: "
+ "\nInstallableTonight="
+ "\nPaddedPastDueDate: "
+ " [More Info…](https://support.apple.com/HT201541)"
+ " [Retry…](https://support.apple.com/HT206996)"
+ " nestedSheets: ["
+ "$__lazy_storage_$_isAppleInternal"
+ "$__lazy_storage_$_preferencesController"
+ ", schedulingForLater="
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Alerts/InstallErrorAlertModifier.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/AutomaticUpdates/AdvancedOptionsView.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/AutomaticUpdates/PreferencesController.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/BetaUpdates/BetaUpdatesManager.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/CatalogConfiguration/CatalogConfigurationBannerView.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Common/Controls/InstallNowButton.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Common/Controls/InstallTonightButton.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/ContentView.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Scanning/ScanErrorView.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/SettingsController.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/SettingsState.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Sheets/SheetCoordinator.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/URLScheme/URLScheme.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/URLScheme/URLSchemeCoordinator.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/UpdatesAvailable/UpToDateView.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettingsExtension/SoftwareUpdateSettingsExtension.swift"
+ "A Security Response is scheduled"
+ "Advanced Options Sheet"
+ "AlsoAvailableHeader"
+ "Beta Updates Sheet"
+ "Bytes required is missing from details."
+ "CancelUpdatesButton"
+ "Cancelling scheduled products: "
+ "Check for Update"
+ "CheckForUpdatesButton"
+ "Clicked retry after scan error."
+ "Clicked to check for updates."
+ "Clicked to install available updates: ["
+ "DISABLE_APPLE_INTELLIGENCE_ALLOW"
+ "DISABLE_APPLE_INTELLIGENCE_DENY"
+ "DISABLE_APPLE_INTELLIGENCE_MANAGE_STORAGE"
+ "DISABLE_APPLE_INTELLIGENCE_PROMPT_TITLE"
+ "DISABLE_APPLE_INTELLIGENCE_PROMPT_WITH_SPACE_REQUIRED"
+ "Dismissing sheet: "
+ "Displayed Updates Changed:\n    Scheduled Updates=["
+ "DownloadFailureDescription"
+ "Each arg is the name of an update."
+ "Error calling cacheDeletePurgeableSpace: "
+ "Failed to retrieve .systemFreeSize attribute."
+ "Failed to retrieve an active window... stopping the request."
+ "Failed to retrieve the active window... attempting to fall back to the first application window."
+ "Failed to retrieve the first application window too..."
+ "First two args is the name of an update, the last arg is the number of additional updates."
+ "HeaderDescription"
+ "INSUFFICIENT_DISK_SPACE_SINGLE_MESSAGE"
+ "Initial scan complete, displaying results..."
+ "Install complete for products: "
+ "Install failed for products: "
+ "InstallTonightText"
+ "InstalledVersion"
+ "License Agreement Sheet"
+ "More Storage Required"
+ "MoreInfoView.InstallTonightButton"
+ "No active sheets - returning the main app window."
+ "No change in displayed products."
+ "Once downloaded, this update will take about 20 minutes to install."
+ "Presenting sheet: "
+ "PrimaryUpdateSection"
+ "Receive Minor updates: "
+ "Received Critical updates: "
+ "Received Major update: "
+ "Received Scheduled Updates: "
+ "Received Scheduling Updates: "
+ "Received a DDM status change: "
+ "Received a catalog change: "
+ "Received a request for the current active window. Number of sheets: "
+ "Registered product: "
+ "Removing existing product: "
+ "Returned window: "
+ "Scan completed with error: "
+ "Scheduled Updates"
+ "ScheduledUpdatesTable"
+ "SchedulingProgress"
+ "SecondaryUpdatesSection"
+ "SelectedDescription"
+ "SelectedFooterText"
+ "SettingsViewControllerProtocol"
+ "Space available: "
+ "Space available: error calculating available free space: "
+ "Start installing products: "
+ "Start scanning..."
+ "These updates will be automatically installed in under 1 day."
+ "This update will be automatically installed in under 1 day."
+ "This update will take about 20 minutes to install."
+ "Unable to download"
+ "Update Scheduled"
+ "Update Summary Sheet"
+ "Update catalog returned with success="
+ "UpdateFooterText"
+ "Updates Available Sheet"
+ "Updates Scheduled Sheet"
+ "Updates are available for your Mac"
+ "Updates are scheduled for your Mac"
+ "UpdatesScheduledSection"
+ "Use of this software is subject to the original license agreement that accompanied the software being updated. [Learn more…](https://www.apple.com/legal/sla/)"
+ "]\n    Primary Update=["
+ "];\n    Secondary Updates: ["
+ "_$observationRegistrar"
+ "_TtC31SoftwareUpdateSettingsExtension12InstallState"
+ "_TtC31SoftwareUpdateSettingsExtension13SettingsState"
+ "_TtC31SoftwareUpdateSettingsExtension15SettingsContext"
+ "_TtC31SoftwareUpdateSettingsExtension15SheetDescriptor"
+ "_TtC31SoftwareUpdateSettingsExtension16SheetCoordinator"
+ "_TtC31SoftwareUpdateSettingsExtension17ProductCollection"
+ "_TtC31SoftwareUpdateSettingsExtension18BetaUpdatesManager"
+ "_TtC31SoftwareUpdateSettingsExtension18SettingsController"
+ "_TtC31SoftwareUpdateSettingsExtension21PreferencesController"
+ "_TtC31SoftwareUpdateSettingsExtension21UpdateFooterViewModel"
+ "_TtC31SoftwareUpdateSettingsExtension7Product"
+ "_TtCC31SoftwareUpdateSettingsExtension16SheetCoordinator13SettingsSheet"
+ "_TtCV31SoftwareUpdateSettingsExtension16UpdateHeaderView9ViewModel"
+ "__isPresented"
+ "_allProducts"
+ "_coordinator"
+ "_currentWindowRequest"
+ "_ddmState"
+ "_displayInstallErrorAlert"
+ "_id"
+ "_initialLoadComplete"
+ "_installState"
+ "_isDisplayedTopmost"
+ "_isDownloadedAndPrepared"
+ "_isInstalledSuccessfully"
+ "_isInstalling"
+ "_isScanning"
+ "_isScheduled"
+ "_isScheduling"
+ "_isSchedulingForLater"
+ "_isSelectedToUpdate"
+ "_nestedSheets"
+ "_primaryUpdate"
+ "_products"
+ "_progress"
+ "_rootSheet"
+ "_scheduledUpdates"
+ "_secondaryUpdates"
+ "_sheetCoordinator"
+ "_sheets"
+ "_showCatalogSelector"
+ "_totalBytesAvailableOnDisk"
+ "_totalSpaceRequired"
+ "_wrappedProduct"
+ "_wrappedProducts"
+ "_wrappedSheet"
+ "attributesOfFileSystemForPath:error:"
+ "cacheDeletePurgeableSpaceWithCompletionHandler:"
+ "calculateFreeSpace()"
+ "client(_:installDidFinishWithError:forUpdates:mdmInitiated:installEvent:)"
+ "criticalProductsReceived"
+ "defaultManager"
+ "dismissSheet(_:)"
+ "displayState"
+ "fetchActiveWindow(completionHandler:)"
+ "fetchPurgeableSpace()"
+ "fetchingMajorOSFromURLScheme"
+ "init(clientInitWithDelegate:catalogManager:betaUpdatesManager:state:)"
+ "installComplete(products:)"
+ "installFailed(products:error:)"
+ "installStarted(products:progress:schedulingForLater:)"
+ "isAppleInternal"
+ "isInstallSchedulingForLater"
+ "lastSeenPrimaryUpdate"
+ "latestQualifyingMajorProduct"
+ "longLongValue"
+ "mainWindow"
+ "majorProductsReceived"
+ "minorProductsReceived"
+ "presentSheet(_:)"
+ "productVersionExtra"
+ "receivedCatalogChange(catalog:)"
+ "receivedCriticalProducts(products:)"
+ "receivedDDMState(ddmState:)"
+ "receivedMajorProduct(product:)"
+ "receivedMinorProducts(products:)"
+ "receivedProductsSchedulingForTonight(products:)"
+ "receivedScheduledProducts(products:installTonightArmed:)"
+ "registerProduct(product:)"
+ "scanCompleted(scanError:)"
+ "scheduledProductsCancelled()"
+ "showLowSpaceText"
+ "state"
+ "stringFromByteCount:countStyle:"
+ "unsignedLongLongValue"
+ "updateCatalog(server:)"
+ "updateDisplayedProducts(scheduled:primary:secondary:)"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "viewController"
+ "withActiveWindow(_:)"
+ "wrappedSheet"
+ "x-apple.systempreferences:com.apple.settings.Storage"
- ". The latest available Rapid Security Response will also be applied."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Advanced/SUOSUAdvancedOptionsView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/Advanced/SUOSUPreferencesController.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/BetaUpdates/SUOSUBetaUpdatesManager.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/CatalogConfiguration/SUOSUCatalogConfigurationView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/ContentView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/SUOSUInstallingView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/SUOSUPreferencePaneV2Controller.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/URLScheme/URLScheme.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/URLScheme/URLSchemeCoordinator.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/UpdatesAvailable/SUOSUMoreInfoView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/UpdatesAvailable/SUOSUPrimaryUpdateBannerView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettings/UpdatesAvailable/SUOSUUpdatesAvailableView.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SoftwareUpdate_binaries/SoftwareUpdateSettingsExtension/SoftwareUpdateSettingsExtension.swift"
- "A Security Response is scheduled "
- "Clicked to install available updates"
- "Clicked to install checked updates: "
- "Clicked to install major update "
- "Clicked to install update "
- "Clicked upgrade now for DDM update: "
- "Clicked upgrade now for critical update: "
- "Clicked upgrade now for major update: "
- "CriticalUpdateTextView.Text"
- "Don't show revoked splat: "
- "Error getting details URL attributed string"
- "Failed to cancel updates queued for later"
- "Fatal error"
- "Found existing: "
- "IconAndTextView.UpdateIcon"
- "IconAndTextView.UpdateTitleText"
- "IconAndTextView.UpdateVersionText"
- "IconAndTextView.UpdateVersionText.MajorUpdate"
- "IconAndTextView.UpgradeNowButton"
- "InstallingView.MajorOSIcon"
- "MoreInfoView.CancelUpdatesButton"
- "MoreInfoView.SplatComboDescription"
- "No implementation"
- "No managed DDM update, not showing declaration"
- "Once downloaded, this update will take about 20 minutes to install. [More Info…](https://support.apple.com/HT201541)"
- "Organization Help URL:"
- "Other Available Updates"
- "PrimaryUpdateBannerView.ManagedDetailsURL"
- "PrimaryUpdateBannerView.MoreInfoText"
- "Scheduled Updates "
- "Skipping DDM update since it's being shown in the primary banner: "
- "SoftwareUpdateSettingsExtension.SUOSUClientStub"
- "SoftwareUpdateSettingsExtension/SUOSUClientStub.swift"
- "Successfully cancelled updates queued for later"
- "T@\"NSDate\",N,R"
- "T@\"NSImage\",N,R"
- "T@\"NSString\",N,R"
- "T@?,N,C"
- "TB,N"
- "TB,N,R"
- "TQ,N"
- "The argument is a URL"
- "These updates will be automatically installed in under 1 day"
- "This update will be automatically installed in under 1 day"
- "This update will take about 20 minutes to install. [More Info…](https://support.apple.com/HT201541)"
- "UpToDateView.CurrentOSText.NoBuildVersion"
- "UpToDateView.LastCheckedText"
- "UpdatesAvailableInstallLaterView.MoreInfoText.ApplyState"
- "UpdatesAvailableInstallLaterView.MoreInfoText.RestartState"
- "UpdatesAvailableInstallLaterView.MoreInfoText.UpdateState"
- "UpdatesAvailableView.AlsoAvailableHeaderText"
- "UpdatesAvailableView.OtherUpdatesHeaderText"
- "UpdatesAvailableWithoutBannerView.ActionButton"
- "UpdatesAvailableWithoutBannerView.BulletedUpdateText"
- "UpdatesAvailableWithoutBannerView.HeaderText"
- "UpdatesAvailableWithoutBannerView.InstallTonightButton"
- "UpdatesAvailableWithoutBannerView.QueuingProgressIndicator"
- "Use of this software is subject to the [original license agreement](https://www.apple.com/legal/sla/) that accompanied the software being updated."
- "Your Mac will try to update later tonight and will automatically restart. [More Info…](https://support.apple.com/HT201541)"
- "Your Mac will try to update later tonight. [More Info…](https://support.apple.com/HT201541)"
- "_TtC31SoftwareUpdateSettingsExtension15SUOSUClientStub"
- "_TtC31SoftwareUpdateSettingsExtension20SUOSUTableUpdateItem"
- "_TtC31SoftwareUpdateSettingsExtension21SUOSUClientStubConfig"
- "_TtC31SoftwareUpdateSettingsExtension23SUOSUBetaUpdatesManager"
- "_TtC31SoftwareUpdateSettingsExtension26SUOSUPreferencesController"
- "_TtC31SoftwareUpdateSettingsExtension31SUOSUPreferencePaneV2Controller"
- "_availableCriticalUpdates"
- "_availableMSUUpdates"
- "_availableMajorUpdates"
- "_availableUpdates"
- "_availableUpdatesTableRowItems"
- "_ddmManagedUpdate"
- "_displayAdvancedOptionsSheet"
- "_enrollmentSheetPresented"
- "_fetchingMajorOSFromURLScheme"
- "_installFinished"
- "_installProgressSchedulingForLater"
- "_installProgressValue"
- "_installingUpdates"
- "_latestQualifyingMajorUpdate"
- "_licenseAgreementRequest"
- "_queuingForLater"
- "_scanning"
- "_selectedForInstall"
- "_semiSplatAvailableUpdate"
- "_updatesSelectedToInstall"
- "client(_:installDidFinishWithError:forUpdates:mdmInitiated:)"
- "config"
- "criticalUpdates"
- "ddmDetailsURLAttributedString(urlString:)"
- "declarationFromKeys"
- "delegate"
- "id"
- "isAutoCheckForUpdatesEnabled"
- "isAutoDownloadUpdatesEnabled"
- "isAutoInstallAppUpdatesEnabled"
- "isAutoInstallMacUpdatesEnabled"
- "isAutoInstallSecurityUpdatesEnabled"
- "majorUpdate"
- "minorUpdates"
- "prefPaneDisplayName"
- "setClientType:"
- "splatRevoked"
- "splitOutTitle"
- "systemGreenColor"
- "toMajorProduct"
- "toProduct"
- "updateSize"
- "updateTitle"
- "updateVersion"
- "updatesAvailableBulletedString()"
- "v24@0:8Q16"

```

## CarouselPreferenceServices

> `/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices`

```diff

-1112.0.187.0.0
-  __TEXT.__text: 0x182b0
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x18e4
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x144b
-  __TEXT.__oslogstring: 0x7ce
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__unwind_info: 0x828
-  __TEXT.__objc_classname: 0x7dd
-  __TEXT.__objc_methname: 0x3ce6
-  __TEXT.__objc_methtype: 0xe0e
-  __TEXT.__objc_stubs: 0x2d00
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__objc_classlist: 0x160
+1112.1.27.0.0
+  __TEXT.__text: 0x1fb28
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x1fa8
+  __TEXT.__const: 0x2c4
+  __TEXT.__cstring: 0x1f0d
+  __TEXT.__oslogstring: 0xc7e
+  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__swift5_typeref: 0x14
+  __TEXT.__constg_swiftt: 0x6c
+  __TEXT.__swift5_reflstr: 0xc
+  __TEXT.__swift5_fieldmd: 0x38
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xae8
+  __TEXT.__objc_classname: 0xa62
+  __TEXT.__objc_methname: 0x4f88
+  __TEXT.__objc_methtype: 0x11d9
+  __TEXT.__objc_stubs: 0x3de0
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__const: 0xf20
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7790
-  __DATA_CONST.__objc_selrefs: 0xd58
+  __DATA_CONST.__objc_const: 0x9ae0
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__objc_const: 0x1140
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__cfstring: 0x2500
+  __AUTH_CONST.__const: 0x508
+  __AUTH_CONST.__objc_const: 0x1728
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_classrefs: 0x280
-  __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x840
-  __DATA.__bss: 0xc8
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH.__objc_data: 0x1310
+  __AUTH.__data: 0x98
+  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_superrefs: 0x190
+  __DATA.__objc_ivar: 0x2e8
+  __DATA.__data: 0xb08
+  __DATA.__bss: 0x310
+  __DATA.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WatchKit.framework/WatchKit
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 724
-  Symbols:   2836
-  CStrings:  1174
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 996
+  Symbols:   3864
+  CStrings:  1595
 
Symbols:
+ +[CSLPRFAppSwitcherDefaultApplications defaultApplicationList]
+ +[CSLPRFAppSwitcherEditing logAppSwitcherEditingAction:fromSource:]
+ +[CSLPRFAppViewChoiceCell preferredCellHeight]
+ +[CSLPRFAppViewImageCache getImageForLauncherMode:]
+ +[CSLPRFAppViewImageCache getImageForLauncherMode:].cold.1
+ +[CSLPRFAppViewImageCache storeImage:forLauncherMode:]
+ +[CSLPRFDeviceUtilities activeWatch]
+ +[CSLPRFDeviceUtilities bridgeController]
+ +[CSLPRFDeviceUtilities bridgeController].cold.1
+ +[CSLPRFDeviceUtilities isTinker:]
+ +[CSLPRFDeviceUtilities screenImageNameWithPrefix:]
+ +[CSLPRFDeviceUtilities seriesForProductType:]
+ +[CSLPRFPairing shared]
+ +[CSLPRFReturnToAppSettingsModel returnToAppSettingsToDictionary:]
+ +[CSLPRFWatchChoice watchChoice:]
+ +[CSLPRFWatchChoice watchChoices]
+ -[CSLAppSwitcherFavoritesSetting .cxx_destruct]
+ -[CSLAppSwitcherFavoritesSetting _withLock:]
+ -[CSLAppSwitcherFavoritesSetting delegate]
+ -[CSLAppSwitcherFavoritesSetting favorites]
+ -[CSLAppSwitcherFavoritesSetting init]
+ -[CSLAppSwitcherFavoritesSetting maximumFavorites]
+ -[CSLAppSwitcherFavoritesSetting setDelegate:]
+ -[CSLAppSwitcherFavoritesSetting setFavorites:]
+ -[CSLAppSwitcherFavoritesSetting setMaximumFavorites:]
+ -[CSLAppSwitcherFavoritesSetting twoWaySyncSettingDidUpdate:]
+ -[CSLAppSwitcherModeSetting .cxx_destruct]
+ -[CSLAppSwitcherModeSetting _withLock:]
+ -[CSLAppSwitcherModeSetting delegate]
+ -[CSLAppSwitcherModeSetting init]
+ -[CSLAppSwitcherModeSetting mode]
+ -[CSLAppSwitcherModeSetting setDelegate:]
+ -[CSLAppSwitcherModeSetting setMode:]
+ -[CSLAppSwitcherModeSetting twoWaySyncSettingDidUpdate:]
+ -[CSLPRFAppViewChoiceButton init]
+ -[CSLPRFAppViewChoiceButton intrinsicContentSize]
+ -[CSLPRFAppViewChoiceCell .cxx_destruct]
+ -[CSLPRFAppViewChoiceCell bundleID]
+ -[CSLPRFAppViewChoiceCell bundle]
+ -[CSLPRFAppViewChoiceCell initWithStyle:reuseIdentifier:]
+ -[CSLPRFAppViewChoiceCell launcherViewModeSettingChanged]
+ -[CSLPRFAppViewChoiceCell layoutSubviews]
+ -[CSLPRFAppViewChoiceCell localize:]
+ -[CSLPRFAppViewChoiceCell retrieveImageForLauncherViewMode:size:completion:]
+ -[CSLPRFAppViewChoiceCell sizeThatFits:]
+ -[CSLPRFAppViewChoiceCell systemLayoutSizeFittingSize:]
+ -[CSLPRFAppViewChoiceCell watchChooser:madeChoice:]
+ -[CSLPRFAppViewChoiceView .cxx_destruct]
+ -[CSLPRFAppViewChoiceView _updateSelectedChoice:]
+ -[CSLPRFAppViewChoiceView _withLock:]
+ -[CSLPRFAppViewChoiceView currentWatchChoice]
+ -[CSLPRFAppViewChoiceView delegate]
+ -[CSLPRFAppViewChoiceView horizontalOffset]
+ -[CSLPRFAppViewChoiceView initWithDelegate:horizontalOffset:choices:]
+ -[CSLPRFAppViewChoiceView setDelegate:]
+ -[CSLPRFAppViewChoiceView setHorizontalOffset:]
+ -[CSLPRFAppViewChoiceView setWatchChoice:]
+ -[CSLPRFAppViewChoiceView sizeThatFits:]
+ -[CSLPRFAppViewChoiceView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:]
+ -[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:]
+ -[CSLPRFConcurrentObserverStore .cxx_destruct]
+ -[CSLPRFConcurrentObserverStore _withLock:]
+ -[CSLPRFConcurrentObserverStore addObserver:]
+ -[CSLPRFConcurrentObserverStore count]
+ -[CSLPRFConcurrentObserverStore enumerateObserversWithBlock:]
+ -[CSLPRFConcurrentObserverStore initWithServiceName:]
+ -[CSLPRFConcurrentObserverStore init]
+ -[CSLPRFConcurrentObserverStore observersLock]
+ -[CSLPRFConcurrentObserverStore observers]
+ -[CSLPRFConcurrentObserverStore performSelectorOnMainThreadWithRespondingObservers:object:waitUntilDone:]
+ -[CSLPRFConcurrentObserverStore removeObserver:]
+ -[CSLPRFConcurrentObserverStore setObservers:]
+ -[CSLPRFConcurrentObserverStore setObserversLock:]
+ -[CSLPRFLauncherViewModeSetting .cxx_destruct]
+ -[CSLPRFLauncherViewModeSetting delegate]
+ -[CSLPRFLauncherViewModeSetting init]
+ -[CSLPRFLauncherViewModeSetting launcherViewModeReason]
+ -[CSLPRFLauncherViewModeSetting launcherViewMode]
+ -[CSLPRFLauncherViewModeSetting launcherViewMode].cold.1
+ -[CSLPRFLauncherViewModeSetting launcherViewMode].cold.2
+ -[CSLPRFLauncherViewModeSetting setDelegate:]
+ -[CSLPRFLauncherViewModeSetting setLauncherViewMode:reason:]
+ -[CSLPRFLauncherViewModeSetting twoWaySyncSettingDidUpdate:]
+ -[CSLPRFPairing _didPair:]
+ -[CSLPRFPairing init]
+ -[CSLPRFPairing isTinker]
+ -[CSLPRFReturnToAppSettings alwaysReturnToAppInSession]
+ -[CSLPRFReturnToAppSettings description]
+ -[CSLPRFReturnToAppSettings hasCustomReturnToAppTimeout]
+ -[CSLPRFReturnToAppSettings hash]
+ -[CSLPRFReturnToAppSettings initWithDictionary:]
+ -[CSLPRFReturnToAppSettings init]
+ -[CSLPRFReturnToAppSettings isEqual:]
+ -[CSLPRFReturnToAppSettings returnToAppTimeout]
+ -[CSLPRFReturnToAppSettings sessionCapable]
+ -[CSLPRFReturnToAppSettings setAlwaysReturnToAppInSession:]
+ -[CSLPRFReturnToAppSettings setReturnToAppTimeout:]
+ -[CSLPRFReturnToAppSettings setSessionCapable:]
+ -[CSLPRFReturnToAppSettings toDictionary]
+ -[CSLPRFReturnToAppSettingsModel .cxx_destruct]
+ -[CSLPRFReturnToAppSettingsModel _withLock:]
+ -[CSLPRFReturnToAppSettingsModel addObserver:]
+ -[CSLPRFReturnToAppSettingsModel init]
+ -[CSLPRFReturnToAppSettingsModel reloadAppSettings]
+ -[CSLPRFReturnToAppSettingsModel removeObserver:]
+ -[CSLPRFReturnToAppSettingsModel saveAppSettings]
+ -[CSLPRFReturnToAppSettingsModel setSettings:forBundleID:]
+ -[CSLPRFReturnToAppSettingsModel settingsForBundleID:]
+ -[CSLPRFWatchChoice .cxx_destruct]
+ -[CSLPRFWatchChoice choice]
+ -[CSLPRFWatchChoice imageProvider]
+ -[CSLPRFWatchChoice initWithChoice:]
+ -[CSLPRFWatchChoice label]
+ -[CSLPRFWatchChoice screenImageName]
+ -[CSLPRFWatchChoice screenImage]
+ -[CSLPRFWatchChoice setImageProvider:]
+ -[CSLPRFWatchChoice setScreenImage:]
+ -[CSLPRFWatchChoice swapForRightToLeft]
+ -[CSLPRFWatchChoiceView .cxx_destruct]
+ -[CSLPRFWatchChoiceView _addWatchScreenImageIfNecessary:]
+ -[CSLPRFWatchChoiceView _createWatchViewForChoice:]
+ -[CSLPRFWatchChoiceView _updateWatchViewPreferredWidth]
+ -[CSLPRFWatchChoiceView choice]
+ -[CSLPRFWatchChoiceView horizontalOffset]
+ -[CSLPRFWatchChoiceView initWithChoice:delegate:horizontalOffset:selectionHandler:]
+ -[CSLPRFWatchChoiceView selectedByTap:]
+ -[CSLPRFWatchChoiceView setHorizontalOffset:]
+ -[CSLPRFWatchChoiceView setSelected:]
+ -[CSLPRFWatchChoiceView sizeThatFits:]
+ -[CSLPRFWatchChoiceView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:]
+ GCC_except_table11
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table7
+ _AnalyticsSendEvent
+ _BPSGetActiveSetupCompletedDevice
+ _CFPreferencesGetAppBooleanValue
+ _CSLAlertServiceIsApplePay
+ _CSLAlertServiceIsNanoSharing
+ _CSLAlertServiceIsSharingAuth
+ _CSLAlertServiceOverControlCenter
+ _CSLAppSwitcherEditingActionToNSString
+ _CSLAppSwitcherEditingSourceToNSString
+ _CSLAppSwitcherModeDefault
+ _CSLAppSwitcherModeToNSString
+ _CSLAppSwitcherModeValid
+ _CSLPRFBannerLookScreenDwellTimeout
+ _CSLPRFBulletinAlertAfterSleepGestureLingerTimeout
+ _CSLPRFCachedAppViewImageURL
+ _CSLPRFCachedAppViewImageURL.cold.1
+ _CSLPRFClip
+ _CSLPRFDisableViewOnWakePreferenceKey
+ _CSLPRFDistance
+ _CSLPRFEqual
+ _CSLPRFFEqual
+ _CSLPRFFFloatTolerance
+ _CSLPRFFGreater
+ _CSLPRFFLess
+ _CSLPRFFloatTolerance
+ _CSLPRFGreater
+ _CSLPRFGreaterEqual
+ _CSLPRFIdleScreenOffExtendedTimeout
+ _CSLPRFInterpolatedFloat
+ _CSLPRFInterpolatedPoint
+ _CSLPRFLess
+ _CSLPRFLessEqual
+ _CSLPRFNear
+ _CSLPRFOnWakeTimeoutPreferenceKey
+ _CSLPRFPercent
+ _CSLPRFSaturate
+ _CSLPRFViewOnWakeFirstUpdateTimeout
+ _CSLPRFViewOnWakePreferencesDomain
+ _CSLPRFViewOnWakeUpdateDefaultTimeout
+ _CSLPRFViewOnWakeUpdateDefaultTimeoutObsolete
+ _CSLPRFWakeToQuickLookTimeOut
+ _CSLPRFWakeToViewMissedBundleAlertTimeOut
+ _CSLPairingIsTinker
+ _CSLSAllowReturnToAppUntilCrownPress
+ _CSLSAllowReturnToAppUntilCrownPress.__canControlReturnToAppUntilCrownPress
+ _CSLSAllowReturnToAppUntilCrownPress.log
+ _CSLSAllowReturnToAppUntilCrownPress.onceToken
+ _MGCopyAnswer
+ _NRDevicePropertyIsAltAccount
+ _NRDevicePropertyLocalPairingDataStorePath
+ _NRDevicePropertyProductType
+ _NRPairedDeviceRegistryDeviceDidPairNotification
+ _NSStringFromCGSize
+ _OBJC_CLASS_$_BPSBridgeAppContext
+ _OBJC_CLASS_$_BPSIllustratedWatchView
+ _OBJC_CLASS_$_CSLAppSwitcherFavoritesSetting
+ _OBJC_CLASS_$_CSLAppSwitcherModeSetting
+ _OBJC_CLASS_$_CSLPRFAppSwitcherDefaultApplications
+ _OBJC_CLASS_$_CSLPRFAppSwitcherEditing
+ _OBJC_CLASS_$_CSLPRFAppViewChoiceButton
+ _OBJC_CLASS_$_CSLPRFAppViewChoiceCell
+ _OBJC_CLASS_$_CSLPRFAppViewChoiceView
+ _OBJC_CLASS_$_CSLPRFAppViewImageCache
+ _OBJC_CLASS_$_CSLPRFAppViewImageProvider
+ _OBJC_CLASS_$_CSLPRFConcurrentObserverStore
+ _OBJC_CLASS_$_CSLPRFDeviceUtilities
+ _OBJC_CLASS_$_CSLPRFLauncherViewModeSetting
+ _OBJC_CLASS_$_CSLPRFPairing
+ _OBJC_CLASS_$_CSLPRFReturnToAppSettings
+ _OBJC_CLASS_$_CSLPRFReturnToAppSettingsModel
+ _OBJC_CLASS_$_CSLPRFWatchChoice
+ _OBJC_CLASS_$_CSLPRFWatchChoiceView
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_PBBridgeWatchAttributeController
+ _OBJC_CLASS_$_UIActivityIndicatorView
+ _OBJC_CLASS_$_UIButton
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_CLASS_$_UITapGestureRecognizer
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_CSLAppSwitcherFavoritesSetting._delegate
+ _OBJC_IVAR_$_CSLAppSwitcherFavoritesSetting._favoritesSetting
+ _OBJC_IVAR_$_CSLAppSwitcherFavoritesSetting._lock
+ _OBJC_IVAR_$_CSLAppSwitcherFavoritesSetting._maximumFavoritesSetting
+ _OBJC_IVAR_$_CSLAppSwitcherModeSetting._delegate
+ _OBJC_IVAR_$_CSLAppSwitcherModeSetting._lock
+ _OBJC_IVAR_$_CSLAppSwitcherModeSetting._mode
+ _OBJC_IVAR_$_CSLAppSwitcherModeSetting._setting
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceCell._appViewChoiceView
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceCell._appViewSetting
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceView._choice
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceView._delegate
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceView._horizontalOffset
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceView._lock
+ _OBJC_IVAR_$_CSLPRFAppViewChoiceView._watchViews
+ _OBJC_IVAR_$_CSLPRFConcurrentObserverStore._observers
+ _OBJC_IVAR_$_CSLPRFConcurrentObserverStore._observersLock
+ _OBJC_IVAR_$_CSLPRFLauncherViewModeSetting._delegate
+ _OBJC_IVAR_$_CSLPRFLauncherViewModeSetting._modeSetting
+ _OBJC_IVAR_$_CSLPRFLauncherViewModeSetting._reasonSetting
+ _OBJC_IVAR_$_CSLPRFPairing._isTinker
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettings._alwaysReturnToAppInSession
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettings._hasCustomReturnToAppTimeout
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettings._returnToAppTimeout
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettings._sessionCapable
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettingsModel._lock
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettingsModel._npsDomainAccessor
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettingsModel._npsManager
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettingsModel._observers
+ _OBJC_IVAR_$_CSLPRFReturnToAppSettingsModel._returnToAppSettingsByBundleID
+ _OBJC_IVAR_$_CSLPRFWatchChoice._choice
+ _OBJC_IVAR_$_CSLPRFWatchChoice._imageProvider
+ _OBJC_IVAR_$_CSLPRFWatchChoice._label
+ _OBJC_IVAR_$_CSLPRFWatchChoice._screenImage
+ _OBJC_IVAR_$_CSLPRFWatchChoice._screenImageName
+ _OBJC_IVAR_$_CSLPRFWatchChoice._swapForRightToLeft
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._button
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._choice
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._delegate
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._horizontalOffset
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._selectionHandler
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._tapRecognizer
+ _OBJC_IVAR_$_CSLPRFWatchChoiceView._watchView
+ _OBJC_METACLASS_$_CSLAppSwitcherFavoritesSetting
+ _OBJC_METACLASS_$_CSLAppSwitcherModeSetting
+ _OBJC_METACLASS_$_CSLPRFAppSwitcherDefaultApplications
+ _OBJC_METACLASS_$_CSLPRFAppSwitcherEditing
+ _OBJC_METACLASS_$_CSLPRFAppViewChoiceButton
+ _OBJC_METACLASS_$_CSLPRFAppViewChoiceCell
+ _OBJC_METACLASS_$_CSLPRFAppViewChoiceView
+ _OBJC_METACLASS_$_CSLPRFAppViewImageCache
+ _OBJC_METACLASS_$_CSLPRFAppViewImageProvider
+ _OBJC_METACLASS_$_CSLPRFConcurrentObserverStore
+ _OBJC_METACLASS_$_CSLPRFDeviceUtilities
+ _OBJC_METACLASS_$_CSLPRFLauncherViewModeSetting
+ _OBJC_METACLASS_$_CSLPRFPairing
+ _OBJC_METACLASS_$_CSLPRFReturnToAppSettings
+ _OBJC_METACLASS_$_CSLPRFReturnToAppSettingsModel
+ _OBJC_METACLASS_$_CSLPRFWatchChoice
+ _OBJC_METACLASS_$_CSLPRFWatchChoiceView
+ _OBJC_METACLASS_$_UIButton
+ _OBJC_METACLASS_$_UIStackView
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _UIImagePNGRepresentation
+ _UILayoutFittingCompressedSize
+ __CSLDeviceIsVictory.isVictory
+ __CSLDeviceIsVictory.onceToken
+ __CSLPairingIsTinker
+ __DATA__TtC26CarouselPreferenceServicesP33_87AE82AF7B7E08FFE21504AC8CC7CB4019ResourceBundleClass
+ __METACLASS_DATA__TtC26CarouselPreferenceServicesP33_87AE82AF7B7E08FFE21504AC8CC7CB4019ResourceBundleClass
+ __OBJC_$_CLASS_METHODS_CSLPRFAppSwitcherDefaultApplications
+ __OBJC_$_CLASS_METHODS_CSLPRFAppSwitcherEditing
+ __OBJC_$_CLASS_METHODS_CSLPRFAppViewChoiceCell
+ __OBJC_$_CLASS_METHODS_CSLPRFAppViewImageCache
+ __OBJC_$_CLASS_METHODS_CSLPRFDeviceUtilities
+ __OBJC_$_CLASS_METHODS_CSLPRFPairing
+ __OBJC_$_CLASS_METHODS_CSLPRFReturnToAppSettingsModel
+ __OBJC_$_CLASS_METHODS_CSLPRFWatchChoice
+ __OBJC_$_CLASS_PROP_LIST_CSLPRFPairing
+ __OBJC_$_INSTANCE_METHODS_CSLAppSwitcherFavoritesSetting
+ __OBJC_$_INSTANCE_METHODS_CSLAppSwitcherModeSetting
+ __OBJC_$_INSTANCE_METHODS_CSLPRFAppViewChoiceButton
+ __OBJC_$_INSTANCE_METHODS_CSLPRFAppViewChoiceCell
+ __OBJC_$_INSTANCE_METHODS_CSLPRFAppViewChoiceView
+ __OBJC_$_INSTANCE_METHODS_CSLPRFAppViewImageProvider
+ __OBJC_$_INSTANCE_METHODS_CSLPRFConcurrentObserverStore
+ __OBJC_$_INSTANCE_METHODS_CSLPRFLauncherViewModeSetting
+ __OBJC_$_INSTANCE_METHODS_CSLPRFPairing
+ __OBJC_$_INSTANCE_METHODS_CSLPRFReturnToAppSettings
+ __OBJC_$_INSTANCE_METHODS_CSLPRFReturnToAppSettingsModel
+ __OBJC_$_INSTANCE_METHODS_CSLPRFWatchChoice
+ __OBJC_$_INSTANCE_METHODS_CSLPRFWatchChoiceView
+ __OBJC_$_INSTANCE_VARIABLES_CSLAppSwitcherFavoritesSetting
+ __OBJC_$_INSTANCE_VARIABLES_CSLAppSwitcherModeSetting
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFAppViewChoiceCell
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFAppViewChoiceView
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFConcurrentObserverStore
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFLauncherViewModeSetting
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFPairing
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFReturnToAppSettings
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFReturnToAppSettingsModel
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFWatchChoice
+ __OBJC_$_INSTANCE_VARIABLES_CSLPRFWatchChoiceView
+ __OBJC_$_PROP_LIST_CSLAppSwitcherFavoritesProviding
+ __OBJC_$_PROP_LIST_CSLAppSwitcherFavoritesSetting
+ __OBJC_$_PROP_LIST_CSLAppSwitcherModeProviding
+ __OBJC_$_PROP_LIST_CSLAppSwitcherModeSetting
+ __OBJC_$_PROP_LIST_CSLPRFAppViewChoiceCell
+ __OBJC_$_PROP_LIST_CSLPRFAppViewChoiceView
+ __OBJC_$_PROP_LIST_CSLPRFAppViewImageProvider
+ __OBJC_$_PROP_LIST_CSLPRFConcurrentObserverStore
+ __OBJC_$_PROP_LIST_CSLPRFLauncherViewModeSetting
+ __OBJC_$_PROP_LIST_CSLPRFLocalizer
+ __OBJC_$_PROP_LIST_CSLPRFPairing
+ __OBJC_$_PROP_LIST_CSLPRFReturnToAppSettings
+ __OBJC_$_PROP_LIST_CSLPRFWatchChoice
+ __OBJC_$_PROP_LIST_CSLPRFWatchChoiceView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLAppSwitcherFavoritesProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLAppSwitcherModeProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLPRFLauncherViewModeSettingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLPRFLocalizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLPRFWatchChoiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLPRFWatchChoiceImageProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLPRFWatchChoiceProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLAppSwitcherFavoritesProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLAppSwitcherModeProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLPRFLauncherViewModeSettingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLPRFLocalizer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLPRFWatchChoiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLPRFWatchChoiceImageProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLPRFWatchChoiceProviding
+ __OBJC_$_PROTOCOL_REFS_CSLAppSwitcherFavoritesProviding
+ __OBJC_$_PROTOCOL_REFS_CSLAppSwitcherModeProviding
+ __OBJC_$_PROTOCOL_REFS_CSLPRFLauncherViewModeSettingDelegate
+ __OBJC_$_PROTOCOL_REFS_CSLPRFLocalizer
+ __OBJC_$_PROTOCOL_REFS_CSLPRFWatchChoiceDelegate
+ __OBJC_$_PROTOCOL_REFS_CSLPRFWatchChoiceImageProviding
+ __OBJC_$_PROTOCOL_REFS_CSLPRFWatchChoiceProviding
+ __OBJC_CLASS_PROTOCOLS_$_CSLAppSwitcherFavoritesSetting
+ __OBJC_CLASS_PROTOCOLS_$_CSLAppSwitcherModeSetting
+ __OBJC_CLASS_PROTOCOLS_$_CSLPRFAppViewChoiceCell
+ __OBJC_CLASS_PROTOCOLS_$_CSLPRFAppViewChoiceView
+ __OBJC_CLASS_PROTOCOLS_$_CSLPRFAppViewImageProvider
+ __OBJC_CLASS_PROTOCOLS_$_CSLPRFLauncherViewModeSetting
+ __OBJC_CLASS_RO_$_CSLAppSwitcherFavoritesSetting
+ __OBJC_CLASS_RO_$_CSLAppSwitcherModeSetting
+ __OBJC_CLASS_RO_$_CSLPRFAppSwitcherDefaultApplications
+ __OBJC_CLASS_RO_$_CSLPRFAppSwitcherEditing
+ __OBJC_CLASS_RO_$_CSLPRFAppViewChoiceButton
+ __OBJC_CLASS_RO_$_CSLPRFAppViewChoiceCell
+ __OBJC_CLASS_RO_$_CSLPRFAppViewChoiceView
+ __OBJC_CLASS_RO_$_CSLPRFAppViewImageCache
+ __OBJC_CLASS_RO_$_CSLPRFAppViewImageProvider
+ __OBJC_CLASS_RO_$_CSLPRFConcurrentObserverStore
+ __OBJC_CLASS_RO_$_CSLPRFDeviceUtilities
+ __OBJC_CLASS_RO_$_CSLPRFLauncherViewModeSetting
+ __OBJC_CLASS_RO_$_CSLPRFPairing
+ __OBJC_CLASS_RO_$_CSLPRFReturnToAppSettings
+ __OBJC_CLASS_RO_$_CSLPRFReturnToAppSettingsModel
+ __OBJC_CLASS_RO_$_CSLPRFWatchChoice
+ __OBJC_CLASS_RO_$_CSLPRFWatchChoiceView
+ __OBJC_LABEL_PROTOCOL_$_CSLAppSwitcherFavoritesProviding
+ __OBJC_LABEL_PROTOCOL_$_CSLAppSwitcherModeProviding
+ __OBJC_LABEL_PROTOCOL_$_CSLPRFLauncherViewModeSettingDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSLPRFLocalizer
+ __OBJC_LABEL_PROTOCOL_$_CSLPRFWatchChoiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSLPRFWatchChoiceImageProviding
+ __OBJC_LABEL_PROTOCOL_$_CSLPRFWatchChoiceProviding
+ __OBJC_METACLASS_RO_$_CSLAppSwitcherFavoritesSetting
+ __OBJC_METACLASS_RO_$_CSLAppSwitcherModeSetting
+ __OBJC_METACLASS_RO_$_CSLPRFAppSwitcherDefaultApplications
+ __OBJC_METACLASS_RO_$_CSLPRFAppSwitcherEditing
+ __OBJC_METACLASS_RO_$_CSLPRFAppViewChoiceButton
+ __OBJC_METACLASS_RO_$_CSLPRFAppViewChoiceCell
+ __OBJC_METACLASS_RO_$_CSLPRFAppViewChoiceView
+ __OBJC_METACLASS_RO_$_CSLPRFAppViewImageCache
+ __OBJC_METACLASS_RO_$_CSLPRFAppViewImageProvider
+ __OBJC_METACLASS_RO_$_CSLPRFConcurrentObserverStore
+ __OBJC_METACLASS_RO_$_CSLPRFDeviceUtilities
+ __OBJC_METACLASS_RO_$_CSLPRFLauncherViewModeSetting
+ __OBJC_METACLASS_RO_$_CSLPRFPairing
+ __OBJC_METACLASS_RO_$_CSLPRFReturnToAppSettings
+ __OBJC_METACLASS_RO_$_CSLPRFReturnToAppSettingsModel
+ __OBJC_METACLASS_RO_$_CSLPRFWatchChoice
+ __OBJC_METACLASS_RO_$_CSLPRFWatchChoiceView
+ __OBJC_PROTOCOL_$_CSLAppSwitcherFavoritesProviding
+ __OBJC_PROTOCOL_$_CSLAppSwitcherModeProviding
+ __OBJC_PROTOCOL_$_CSLPRFLauncherViewModeSettingDelegate
+ __OBJC_PROTOCOL_$_CSLPRFLocalizer
+ __OBJC_PROTOCOL_$_CSLPRFWatchChoiceDelegate
+ __OBJC_PROTOCOL_$_CSLPRFWatchChoiceImageProviding
+ __OBJC_PROTOCOL_$_CSLPRFWatchChoiceProviding
+ ___105-[CSLPRFConcurrentObserverStore performSelectorOnMainThreadWithRespondingObservers:object:waitUntilDone:]_block_invoke
+ ___23+[CSLPRFPairing shared]_block_invoke
+ ___33-[CSLAppSwitcherModeSetting init]_block_invoke
+ ___33-[CSLAppSwitcherModeSetting mode]_block_invoke
+ ___37-[CSLPRFReturnToAppSettings isEqual:]_block_invoke
+ ___37-[CSLPRFReturnToAppSettings isEqual:]_block_invoke_2
+ ___37-[CSLPRFReturnToAppSettings isEqual:]_block_invoke_3
+ ___37-[CSLPRFReturnToAppSettings isEqual:]_block_invoke_4
+ ___38-[CSLPRFConcurrentObserverStore count]_block_invoke
+ ___42-[CSLPRFAppViewChoiceView setWatchChoice:]_block_invoke
+ ___43-[CSLAppSwitcherFavoritesSetting favorites]_block_invoke
+ ___45-[CSLPRFAppViewChoiceView currentWatchChoice]_block_invoke
+ ___45-[CSLPRFConcurrentObserverStore addObserver:]_block_invoke
+ ___48-[CSLPRFConcurrentObserverStore removeObserver:]_block_invoke
+ ___49-[CSLPRFAppViewChoiceView _updateSelectedChoice:]_block_invoke
+ ___49-[CSLPRFReturnToAppSettingsModel saveAppSettings]_block_invoke
+ ___50-[CSLAppSwitcherFavoritesSetting maximumFavorites]_block_invoke
+ ___51-[CSLPRFReturnToAppSettingsModel reloadAppSettings]_block_invoke
+ ___51-[CSLPRFReturnToAppSettingsModel reloadAppSettings]_block_invoke_2
+ ___54-[CSLPRFReturnToAppSettingsModel settingsForBundleID:]_block_invoke
+ ___57-[CSLPRFAppViewChoiceCell initWithStyle:reuseIdentifier:]_block_invoke
+ ___57-[CSLPRFWatchChoiceView _addWatchScreenImageIfNecessary:]_block_invoke
+ ___58-[CSLPRFReturnToAppSettingsModel setSettings:forBundleID:]_block_invoke
+ ___58-[CSLPRFReturnToAppSettingsModel setSettings:forBundleID:]_block_invoke_2
+ ___61-[CSLPRFConcurrentObserverStore enumerateObserversWithBlock:]_block_invoke
+ ___66+[CSLPRFReturnToAppSettingsModel returnToAppSettingsToDictionary:]_block_invoke
+ ___69-[CSLPRFAppViewChoiceView initWithDelegate:horizontalOffset:choices:]_block_invoke
+ ___69-[CSLPRFAppViewChoiceView initWithDelegate:horizontalOffset:choices:]_block_invoke_2
+ ___76-[CSLPRFAppViewChoiceCell retrieveImageForLauncherViewMode:size:completion:]_block_invoke
+ ___79-[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:]_block_invoke
+ ___79-[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:]_block_invoke.1
+ ___79-[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:]_block_invoke.cold.1
+ ___CSLSAllowReturnToAppUntilCrownPress_block_invoke
+ ____CSLDeviceIsVictory_block_invoke
+ ___block_descriptor_32_e8_16?08l
+ ___block_descriptor_40_e38_v32?0"CSLPRFWatchChoiceView"8Q16^B24l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e34_v32?0"CSLPRFWatchChoice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e52_v32?0"NSString"8"CSLPRFReturnToAppSettings"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e5_d8?0ls32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0q8lw32l8
+ ___block_descriptor_48_e8_32bs_e29_v24?0"UIImage"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e45_v16?0"<CSLPRFReturnToAppSettingsObserver>"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"UIImage"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"UIImage"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48w_e34_v32?0"CSLPRFWatchChoice"8Q16^B24ls32l8w48l8s40l8
+ ___block_literal_global.10
+ ___block_literal_global.13
+ ___block_literal_global.16
+ ___block_literal_global.19
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.28
+ ___block_literal_global.31
+ ___block_literal_global.34
+ ___block_literal_global.37
+ ___block_literal_global.40
+ ___block_literal_global.43
+ ___cslprf_app_switcher_log_block_invoke
+ ___cslprf_backlight_log_block_invoke
+ ___cslprf_diagnostics_log_block_invoke
+ ___cslprf_dock_log_block_invoke
+ ___cslprf_fluidui_log_block_invoke
+ ___cslprf_icon_field_log_block_invoke
+ ___cslprf_icon_log_block_invoke
+ ___cslprf_sessions_log_block_invoke
+ ___cslprf_startup_log_block_invoke
+ ___cslprf_sting_log_block_invoke
+ ___cslprf_systemstate_log_block_invoke
+ ___cslprf_ui_log_block_invoke
+ ___swift_allocate_value_buffer
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFileProvider_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CarouselPreferenceServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_CarouselPreferenceServices
+ _associated conformance 26CarouselPreferenceServices9DepthUnitOSHAASQ
+ _cslprf_app_switcher_log
+ _cslprf_app_switcher_log.__logger
+ _cslprf_app_switcher_log.onceToken
+ _cslprf_backlight_log
+ _cslprf_backlight_log.__logger
+ _cslprf_backlight_log.onceToken
+ _cslprf_diagnostics_log
+ _cslprf_diagnostics_log.__logger
+ _cslprf_diagnostics_log.onceToken
+ _cslprf_dock_log
+ _cslprf_dock_log.__logger
+ _cslprf_dock_log.onceToken
+ _cslprf_fluidui_log
+ _cslprf_fluidui_log.__logger
+ _cslprf_fluidui_log.onceToken
+ _cslprf_icon_field_log
+ _cslprf_icon_field_log.__logger
+ _cslprf_icon_field_log.onceToken
+ _cslprf_icon_log
+ _cslprf_icon_log.__logger
+ _cslprf_icon_log.onceToken
+ _cslprf_sessions_log
+ _cslprf_sessions_log.__logger
+ _cslprf_sessions_log.onceToken
+ _cslprf_startup_log
+ _cslprf_startup_log.__logger
+ _cslprf_startup_log.onceToken
+ _cslprf_sting_log
+ _cslprf_sting_log.__logger
+ _cslprf_sting_log.onceToken
+ _cslprf_systemstate_log
+ _cslprf_systemstate_log.__logger
+ _cslprf_systemstate_log.onceToken
+ _cslprf_ui_log
+ _cslprf_ui_log.__logger
+ _cslprf_ui_log.onceToken
+ _kActivityAppBundleIdentifier
+ _kAppStoreBundleIdentifier
+ _kAudiobooksBundleIdentifier
+ _kAuthSharingAlertIdentifier
+ _kCSLAppSwitcherEditingActionKey
+ _kCSLAppSwitcherEditingEvent
+ _kCSLAppSwitcherEditingSourceKey
+ _kCSLAppSwitcherModeKey
+ _kCSLAppSwitcherModeLegacyKey
+ _kCSLDataMigrationMonitiorIdentifier
+ _kCSLLauncherBundleIdentifier
+ _kCSLPreboardBundleIdentifier
+ _kCSLReBoardBundleIdentifier
+ _kCalculatorBundleIdentifier
+ _kCalendarBundleIdentifier
+ _kCameraBundleIdentifier
+ _kCarouselBundleIdentifier
+ _kCarouselSceneIdentifier
+ _kClockBundleIdentifier
+ _kClockFaceBundleIdentifier
+ _kClockSceneIdentifier
+ _kCompassBundleIdentifier
+ _kContactsBundleIdentifier
+ _kCoreSpeechDaemonBundleIdentifier
+ _kDepthBundleIdentifier
+ _kDeskClockAlertIdentifier
+ _kEmergencyAlertIdentifier
+ _kFindMyDevicesBundleIdentifier
+ _kFindMyItemsBundleIdentifier
+ _kFindMyPeopleBundleIdentifier
+ _kHeartAppBundleIdentifier
+ _kHeartRhythmBundleIdentifier
+ _kHomeBundleIdentifier
+ _kHomeScreenSceneIdentifier
+ _kMailBundleIdentifier
+ _kMandrakeBundleIdentifier
+ _kMapsAppBundleIdentifier
+ _kMedicationsBundleIdentifier
+ _kMemojiEditorBundleIdentifier
+ _kMenstrualCyclesBundleIdentifier
+ _kMessagesAppBundleIdentifier
+ _kMindBundleIdentifier
+ _kMusicBundleIdentifier
+ _kNanoAlarmAlertIdentifier
+ _kNanoAlarmBundleIdentifier
+ _kNanoBuddyIdentifier
+ _kNanoCompassAlertIdentifier
+ _kNanoDemoBundleIdentifier
+ _kNanoDiagnosticsBundleIdentifier
+ _kNanoPhoneAlertIdentifier
+ _kNanoPhoneBundleIdentifier
+ _kNanoPhoneNonCellularAlertIdentifier
+ _kNanoPhotosBundleIdentifier
+ _kNanoSharingAlertIdentifier
+ _kNanoStopwatchBundleIdentifier
+ _kNanoTimerAlertIdentifier
+ _kNanoTimerBundleIdentifier
+ _kNewsBundleIdentifier
+ _kNoiseBundleIdentifier
+ _kNowPlayingAppBundleIdentifer
+ _kOxygenSaturationBundleIdentifier
+ _kPassbookAlertIdentifier
+ _kPassbookBundleIdentifier
+ _kPassbookExpressAlertIdentifier
+ _kPodcastsBundleIdentifier
+ _kQuickBoardViewServiceBundleIdentifier
+ _kRaiseToSpeakAlertIdentifier
+ _kRemindersBundleIdentifier
+ _kRemoteBundleIdentifier
+ _kSchoolTimeAlertBundleIdentifier
+ _kSessionTrackerAppBundleIdentifier
+ _kSettingsBundleIdentifier
+ _kShortcutsBundleIdentifier
+ _kSleepBundleIdentifier
+ _kStocksBundleIdentifier
+ _kTapToRadar
+ _kTinCanBundleIdentifier
+ _kTipsBundleIdentifier
+ _kVictoryBundleIdentifier
+ _kVoiceMemosIdentifier
+ _kWeatherBundleIdentifier
+ _kWorldClockBundleIdentifier
+ _objc_msgSend$_addWatchScreenImageIfNecessary:
+ _objc_msgSend$_createWatchViewForChoice:
+ _objc_msgSend$_setHyphenationFactor:
+ _objc_msgSend$_updateSelectedChoice:
+ _objc_msgSend$_updateWatchViewPreferredWidth
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$activeDeviceSelectorBlock
+ _objc_msgSend$activePairedDeviceSelectorBlock
+ _objc_msgSend$addArrangedSubview:
+ _objc_msgSend$addConstraint:
+ _objc_msgSend$addGestureRecognizer:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$alwaysReturnToAppInSession
+ _objc_msgSend$appSwitcherFavoritesDidUpdate:
+ _objc_msgSend$appSwitcherModeDidUpdate:
+ _objc_msgSend$appendDouble:
+ _objc_msgSend$appendDouble:counterpart:
+ _objc_msgSend$appendFloat:withName:
+ _objc_msgSend$blackColor
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$bounds
+ _objc_msgSend$bridgeController
+ _objc_msgSend$bundle
+ _objc_msgSend$choice
+ _objc_msgSend$compact
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:
+ _objc_msgSend$contentView
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$defaultApplicationList
+ _objc_msgSend$defaultValue
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumerateObserversWithBlock:
+ _objc_msgSend$favorites
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$floatValue
+ _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
+ _objc_msgSend$getAppViewListImage:completion:
+ _objc_msgSend$getDevicesMatching:
+ _objc_msgSend$getImageForLauncherMode:
+ _objc_msgSend$hasCustomReturnToAppTimeout
+ _objc_msgSend$image
+ _objc_msgSend$imageProvider
+ _objc_msgSend$imageWithData:scale:
+ _objc_msgSend$inWatchSetupFlow
+ _objc_msgSend$initWithActivityIndicatorStyle:
+ _objc_msgSend$initWithChoice:
+ _objc_msgSend$initWithChoice:delegate:horizontalOffset:selectionHandler:
+ _objc_msgSend$initWithDelegate:horizontalOffset:choices:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithTarget:action:
+ _objc_msgSend$intValue
+ _objc_msgSend$isTinker
+ _objc_msgSend$isTinkerPairing
+ _objc_msgSend$label
+ _objc_msgSend$launcherViewMode
+ _objc_msgSend$launcherViewModeSettingChanged
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$localize:
+ _objc_msgSend$migrate:withMapping:
+ _objc_msgSend$mode
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$performSelectorOnMainThread:withObject:waitUntilDone:
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$reloadAppSettings
+ _objc_msgSend$removeFromSuperview
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$replacePointerAtIndex:withPointer:
+ _objc_msgSend$retrieveImageForLauncherViewMode:size:completion:
+ _objc_msgSend$returnToAppSettingsToDictionary:
+ _objc_msgSend$returnToAppTimeout
+ _objc_msgSend$screenImage
+ _objc_msgSend$screenImageName
+ _objc_msgSend$screenImageNameWithPrefix:
+ _objc_msgSend$seriesForProductType:
+ _objc_msgSend$sessionCapable
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setAxis:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setContentCompressionResistancePriority:forAxis:
+ _objc_msgSend$setContentHuggingPriority:forAxis:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setDistribution:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setHorizontalOffset:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setImage:forState:
+ _objc_msgSend$setImageProvider:
+ _objc_msgSend$setLauncherViewMode:reason:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setNumberOfLines:
+ _objc_msgSend$setPreferredCGSizeValue:
+ _objc_msgSend$setScreenImage:
+ _objc_msgSend$setScreenImageName:
+ _objc_msgSend$setScreenImageSearchBundleIdentifier:
+ _objc_msgSend$setSelected:
+ _objc_msgSend$setText:
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$setUserInteractionEnabled:
+ _objc_msgSend$setWatchChoice:
+ _objc_msgSend$settingsChanged:forBundleID:
+ _objc_msgSend$shared
+ _objc_msgSend$sharedDeviceController
+ _objc_msgSend$size
+ _objc_msgSend$sizeFromDevice:
+ _objc_msgSend$startAnimating
+ _objc_msgSend$stopAnimating
+ _objc_msgSend$storeImage:forLauncherMode:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$systemGrayColor
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$systemLayoutSizeFittingSize:
+ _objc_msgSend$systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:
+ _objc_msgSend$systemOrangeColor
+ _objc_msgSend$toDictionary
+ _objc_msgSend$topAnchor
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$valueForProperty:
+ _objc_msgSend$valueWithCGSize:
+ _objc_msgSend$watchChoice:
+ _objc_msgSend$watchChoices
+ _objc_msgSend$watchChooser:madeChoice:
+ _objc_msgSend$watchScreenImageView
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_msgSend$writeToURL:atomically:
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _shared.Shared
+ _shared.onceToken
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_getObjCClassFromMetadata
+ _swift_getWitnessTable
+ _swift_once
+ _swift_slowAlloc
+ _symbolic _____ 26CarouselPreferenceServices19ResourceBundleClass33_87AE82AF7B7E08FFE21504AC8CC7CB40LLC
+ _symbolic _____ 26CarouselPreferenceServices9DepthUnitO
- ___55-[CSLPRFStingConfiguration twoWaySyncSettingDidUpdate:]_block_invoke.cold.1
- ___63-[CSLPRFStingConfiguration depthAutoLaunchAppSettingDidUpdate:]_block_invoke.cold.1
CStrings:
+ "\x03\x11"
+ "\x12"
+ "$"
+ "%@ UIApp provided device %@"
+ "%@ doesn't provide to activeWatch"
+ "%@-Default"
+ "%@-S3_Default"
+ "%@-S4_Default"
+ "%{public}@ initialValue %{private}@"
+ "%{public}@ updated to %{private}@"
+ "%{public}s setting stingSettings to %{private}@"
+ ","
+ "-[CSLPRFStingConfiguration setConfigurationForBundleID:actionType:identifier:source:]_block_invoke"
+ "27120128-3A0E-492A-8BBC-C57A70E362CA"
+ ">>>> %@ %@ retrieved %@"
+ ">>>> %@ adding retrieved image %@ to view %@"
+ ">>>> %@ retrieved image is %@, not adding to view %@"
+ ">>>> %d selected"
+ ">>>> CSLPRFDeviceAppviewImageCachePath: Error creating cache directory %@ path %@"
+ ">>>> CSLPRFPerDeviceAppViewImageCachePath: cachePath %@, device %@"
+ ">>>> adding provided %@ to view %@"
+ ">>>> calling getAppViewListImage %@"
+ ">>>> could not get app view list image %@"
+ ">>>> could not read from %@"
+ ">>>> got image %@, calling %@"
+ ">>>> no bridgeController"
+ ">>>> no path for app view image"
+ ">>>> read data from %@"
+ ">>>> selecting %@"
+ ">>>> setting choice to %d was %d"
+ ">>>> unselecting %@"
+ ">>>> watchChoiceProvider %@ madeChoice %d"
+ "@\"<CSLAppSwitcherFavoritesSettingDelegate>\""
+ "@\"<CSLAppSwitcherFavoritesSettingDelegate>\"16@0:8"
+ "@\"<CSLAppSwitcherModeSettingDelegate>\""
+ "@\"<CSLAppSwitcherModeSettingDelegate>\"16@0:8"
+ "@\"<CSLPRFLauncherViewModeSettingDelegate>\""
+ "@\"<CSLPRFWatchChoiceDelegate>\""
+ "@\"<CSLPRFWatchChoiceImageProviding>\""
+ "@\"BPSIllustratedWatchView\""
+ "@\"CSLPRFAppViewChoiceButton\""
+ "@\"CSLPRFAppViewChoiceView\""
+ "@\"CSLPRFConcurrentObserverStore\""
+ "@\"CSLPRFLauncherViewModeSetting\""
+ "@\"NSMutableArray\""
+ "@\"NSPointerArray\""
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"UITapGestureRecognizer\""
+ "@16@?0@8"
+ "@40@0:8@16d24@32"
+ "@48@0:8@16@24d32@?40"
+ "APP_VIEW_CHOICE_GRID_VIEW"
+ "APP_VIEW_CHOICE_LIST_VIEW"
+ "AllowReturnToAppUntilCrownPress"
+ "AlwaysReturnToAppInSession"
+ "AppSwitcherMode"
+ "AppViewGrid.png"
+ "AppViewList.png"
+ "Bridge"
+ "CSLAppSwitcherFavoritesProviding"
+ "CSLAppSwitcherFavoritesSetting"
+ "CSLAppSwitcherModeChangedNotification"
+ "CSLAppSwitcherModeProviding"
+ "CSLAppSwitcherModeSetting"
+ "CSLDockSettingsChangedNotification"
+ "CSLLauncherSettingsChangedNotification"
+ "CSLPRFAppSwitcherDefaultApplications"
+ "CSLPRFAppSwitcherEditing"
+ "CSLPRFAppViewChoiceButton"
+ "CSLPRFAppViewChoiceCell"
+ "CSLPRFAppViewChoiceView"
+ "CSLPRFAppViewImageCache"
+ "CSLPRFAppViewImageProvider"
+ "CSLPRFConcurrentObserverStore"
+ "CSLPRFDeviceUtilities"
+ "CSLPRFLauncherViewModeSetting"
+ "CSLPRFLauncherViewModeSettingDelegate"
+ "CSLPRFLocalizer"
+ "CSLPRFPairing"
+ "CSLPRFReturnToAppSettings"
+ "CSLPRFReturnToAppSettingsModel"
+ "CSLPRFWatchChoice"
+ "CSLPRFWatchChoiceDelegate"
+ "CSLPRFWatchChoiceImageProviding"
+ "CSLPRFWatchChoiceProviding"
+ "CSLPRFWatchChoiceView"
+ "CarouselAppViewChoice"
+ "FavoriteApplications"
+ "LauncherViewMode"
+ "LauncherViewModeReason"
+ "MRUBasedDockLayout"
+ "MaximumFavoriteApplications"
+ "OnWakeTimeoutSeconds"
+ "Pairing didPair isTinker? %d"
+ "Pairing init isTinker? %d"
+ "ReturnToAppSettings"
+ "ReturnToAppTimeout"
+ "Screen-Carousel"
+ "Screen-Carousel-Default-484h"
+ "Screen-Carousel-Default-502h"
+ "Screen-Carousel-S3_Default-484h"
+ "Screen-Carousel-S4_Default-394h"
+ "Screen-Carousel-S4_Default-448h"
+ "Screen-Carousel-S4_Default-484h"
+ "Screen-Carousel-S4_Default-compact"
+ "Screen-Carousel-S4_Default-regular"
+ "Screen-CarouselList"
+ "SessionCapable"
+ "T@\"<CSLAppSwitcherFavoritesSettingDelegate>\",W,N"
+ "T@\"<CSLAppSwitcherFavoritesSettingDelegate>\",W,N,V_delegate"
+ "T@\"<CSLAppSwitcherModeSettingDelegate>\",W,N"
+ "T@\"<CSLAppSwitcherModeSettingDelegate>\",W,N,V_delegate"
+ "T@\"<CSLPRFLauncherViewModeSettingDelegate>\",W,N,V_delegate"
+ "T@\"<CSLPRFWatchChoiceDelegate>\",W,N,V_delegate"
+ "T@\"<CSLPRFWatchChoiceImageProviding>\",&,N,V_imageProvider"
+ "T@\"CSLPRFPairing\",R"
+ "T@\"NSArray\",&,N"
+ "T@\"NSPointerArray\",&,N,V_observers"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_label"
+ "T@\"NSString\",R,N,V_screenImageName"
+ "T@\"UIImage\",&,N,V_screenImage"
+ "TB,N,V_alwaysReturnToAppInSession"
+ "TB,N,V_sessionCapable"
+ "TB,R,N,V_hasCustomReturnToAppTimeout"
+ "TB,R,N,V_swapForRightToLeft"
+ "Td,N"
+ "Td,N,V_horizontalOffset"
+ "Tq,N,V_mode"
+ "Tq,R,N,V_choice"
+ "T{os_unfair_lock_s=I},N,V_observersLock"
+ "_TtC26CarouselPreferenceServicesP33_87AE82AF7B7E08FFE21504AC8CC7CB4019ResourceBundleClass"
+ "__canControlReturnToAppUntilCrownPress = %{BOOL}u, allowReturnToAppUntilCrownPress = %{BOOL}u"
+ "_addWatchScreenImageIfNecessary:"
+ "_alwaysReturnToAppInSession"
+ "_appViewChoiceView"
+ "_appViewSetting"
+ "_button"
+ "_choice"
+ "_createWatchViewForChoice:"
+ "_didPair:"
+ "_favoritesSetting"
+ "_hasCustomReturnToAppTimeout"
+ "_hasCustomReturnToAppTimeout = %{BOOL}u"
+ "_horizontalOffset"
+ "_imageProvider"
+ "_isTinker"
+ "_label"
+ "_maximumFavoritesSetting"
+ "_mode"
+ "_modeSetting"
+ "_npsDomainAccessor"
+ "_npsManager"
+ "_observers"
+ "_observersLock"
+ "_reasonSetting"
+ "_returnToAppSettingsByBundleID"
+ "_returnToAppTimeout"
+ "_screenImage"
+ "_screenImageName"
+ "_selectionHandler"
+ "_sessionCapable"
+ "_setHyphenationFactor:"
+ "_setting"
+ "_swapForRightToLeft"
+ "_tapRecognizer"
+ "_updateSelectedChoice:"
+ "_updateWatchViewPreferredWidth"
+ "_watchView"
+ "_watchViews"
+ "activateConstraints:"
+ "activeDeviceSelectorBlock"
+ "activePairedDeviceSelectorBlock"
+ "add"
+ "addArrangedSubview:"
+ "addConstraint:"
+ "addGestureRecognizer:"
+ "addPointer:"
+ "addSubview:"
+ "addTarget:action:forControlEvents:"
+ "alwaysReturnToAppInSession"
+ "appSwitcherFavoritesDidUpdate:"
+ "appSwitcherModeDidUpdate:"
+ "app_switcher"
+ "appendDouble:"
+ "appendDouble:counterpart:"
+ "appendFloat:withName:"
+ "backlight"
+ "blackColor"
+ "bottomAnchor"
+ "bounds"
+ "bridgeController"
+ "bundle"
+ "checkmark.circle.fill"
+ "choice"
+ "circle"
+ "com.apple.Carousel.launcher"
+ "com.apple.DataMigrationMonitor"
+ "com.apple.Depth"
+ "com.apple.DeskClock.alert"
+ "com.apple.Mandrake"
+ "com.apple.Mind"
+ "com.apple.NanoAlarm.alert"
+ "com.apple.NanoCompass.NanoCompassAlertUI"
+ "com.apple.NanoCompass.watchkitapp"
+ "com.apple.NanoContacts"
+ "com.apple.NanoDemo"
+ "com.apple.NanoDiagnostics"
+ "com.apple.NanoMedications"
+ "com.apple.NanoOxygenSaturation.watchkitapp"
+ "com.apple.NanoTapToRadar"
+ "com.apple.NanoTimer.alert"
+ "com.apple.NanoTips"
+ "com.apple.PreBoard"
+ "com.apple.QuickboardViewService"
+ "com.apple.RaiseToSpeakAlert"
+ "com.apple.ReBoard"
+ "com.apple.SchoolTime"
+ "com.apple.carousel"
+ "com.apple.carousel.clock"
+ "com.apple.carousel.dock.edited"
+ "com.apple.clockface"
+ "com.apple.corespeechd"
+ "com.apple.findmy.finddevices"
+ "com.apple.findmy.finditems"
+ "com.apple.nano"
+ "com.apple.nanobuddy"
+ "com.apple.nanopassbook.alert"
+ "com.apple.nanopassbook.transactioncompletealert"
+ "com.apple.nanophone.cellularDeviceAlert"
+ "com.apple.nanophone.emergencyAlert"
+ "com.apple.nanophone.nonCellularDeviceAlert"
+ "com.apple.nanosharing.alert"
+ "com.apple.sharing.auth"
+ "com.apple.shortcuts.watch"
+ "com.apple.watch.homescreen"
+ "com.apple.watchmemojieditor"
+ "com.nike.nikeplus-gps.watchkitapp"
+ "compact"
+ "companionSettings"
+ "configurationWithPointSize:weight:"
+ "constraintEqualToAnchor:"
+ "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
+ "contentView"
+ "currentWatchChoice"
+ "d"
+ "d16@0:8"
+ "d8@?0"
+ "dataWithContentsOfURL:"
+ "defaultApplicationList"
+ "diagnostics"
+ "dictionaryWithCapacity:"
+ "dock"
+ "enumerateObjectsUsingBlock:"
+ "enumerateObserversWithBlock:"
+ "favorites"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "floatValue"
+ "fluidui"
+ "fuKL2rMywRgQF1wowOA/cg"
+ "getAllDevicesWithArchivedAltAccountDevicesMatching:"
+ "getAppViewListImage:completion:"
+ "getDevicesMatching:"
+ "getImageForLauncherMode:"
+ "gizmoSettings"
+ "gizmoSwitcher"
+ "hasCustomReturnToAppTimeout"
+ "horizontalOffset"
+ "icon"
+ "icon_field"
+ "illustrated_assets"
+ "image"
+ "imageProvider"
+ "imageWithData:scale:"
+ "inWatchSetupFlow"
+ "initWithActivityIndicatorStyle:"
+ "initWithChoice:"
+ "initWithChoice:delegate:horizontalOffset:selectionHandler:"
+ "initWithDelegate:horizontalOffset:choices:"
+ "initWithDictionary:"
+ "initWithServiceName:"
+ "initWithTarget:action:"
+ "intValue"
+ "intrinsicContentSize"
+ "isTinker"
+ "isTinker:"
+ "isTinkerPairing"
+ "label"
+ "launcherViewMode"
+ "launcherViewMode is %d"
+ "launcherViewModeReason"
+ "launcherViewModeSettingChanged"
+ "layoutIfNeeded"
+ "layoutSubviews"
+ "leadingAnchor"
+ "localize:"
+ "logAppSwitcherEditingAction:fromSource:"
+ "maximumFavorites"
+ "mode"
+ "mru"
+ "numberWithDouble:"
+ "observers"
+ "observersLock"
+ "performSelectorOnMainThread:withObject:waitUntilDone:"
+ "performSelectorOnMainThreadWithRespondingObservers:object:waitUntilDone:"
+ "pointerAtIndex:"
+ "preferredCellHeight"
+ "rangeOfString:"
+ "reloadAppSettings"
+ "removabilityDidChangeForApplications:onDeviceWithPairingID:"
+ "remove"
+ "removeFromSuperview"
+ "removeObserver:name:object:"
+ "reorder"
+ "replacePointerAtIndex:withPointer:"
+ "retrieveImageForLauncherViewMode:size:completion:"
+ "returnToAppSettingsToDictionary:"
+ "returnToAppTimeout"
+ "saveAppSettings"
+ "screenImage"
+ "screenImageName"
+ "screenImageNameWithPrefix:"
+ "selectedByTap:"
+ "seriesForProductType:"
+ "sessionCapable"
+ "sessions"
+ "setAlignment:"
+ "setAlwaysReturnToAppInSession:"
+ "setAxis:"
+ "setBackgroundColor:"
+ "setContentCompressionResistancePriority:forAxis:"
+ "setContentHuggingPriority:forAxis:"
+ "setCustomSpacing:afterView:"
+ "setDistribution:"
+ "setFavorites:"
+ "setHidden:"
+ "setHorizontalOffset:"
+ "setImage:"
+ "setImage:forState:"
+ "setImageProvider:"
+ "setLauncherViewMode:reason:"
+ "setMaximumFavorites:"
+ "setMode:"
+ "setNeedsLayout"
+ "setNumberOfLines:"
+ "setObservers:"
+ "setObserversLock:"
+ "setPreferredCGSizeValue:"
+ "setReturnToAppTimeout:"
+ "setScreenImage:"
+ "setScreenImageName:"
+ "setScreenImageSearchBundleIdentifier:"
+ "setSelected:"
+ "setSessionCapable:"
+ "setSettings:forBundleID:"
+ "setText:"
+ "setTintColor:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setUserInteractionEnabled:"
+ "setWatchChoice:"
+ "setting %@ to %d"
+ "setting %@ to %d was %d"
+ "setting launcherViewMode to %d"
+ "setting returnToAppTimeout to %d"
+ "settingsChanged:forBundleID:"
+ "settingsForBundleID:"
+ "shared"
+ "sharedDeviceController"
+ "size"
+ "sizeFromDevice:"
+ "sizeThatFits:"
+ "startAnimating"
+ "startup"
+ "sting"
+ "stopAnimating"
+ "storeImage:forLauncherMode:"
+ "stringByAppendingPathComponent:"
+ "substringWithRange:"
+ "swapForRightToLeft"
+ "systemGrayColor"
+ "systemImageNamed:withConfiguration:"
+ "systemLayoutSizeFittingSize:"
+ "systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:"
+ "systemOrangeColor"
+ "systemstate"
+ "toDictionary"
+ "topAnchor"
+ "trailingAnchor"
+ "ui"
+ "v16@?0@\"<CSLPRFReturnToAppSettingsObserver>\"8"
+ "v16@?0q8"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8@\"<CSLAppSwitcherFavoritesSettingDelegate>\"16"
+ "v24@0:8@\"<CSLAppSwitcherModeSettingDelegate>\"16"
+ "v24@0:8d16"
+ "v24@?0@\"UIImage\"8@\"NSError\"16"
+ "v32@0:8@\"<CSLPRFWatchChoiceProviding>\"16q24"
+ "v32@0:8Q16Q24"
+ "v32@0:8q16Q24"
+ "v32@?0@\"CSLPRFWatchChoice\"8Q16^B24"
+ "v32@?0@\"CSLPRFWatchChoiceView\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"CSLPRFReturnToAppSettings\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v36@0:8:16@24B32"
+ "v48@0:8q16{CGSize=dd}24@?40"
+ "v48@0:8q16{CGSize=dd}24@?<v@?@\"UIImage\">40"
+ "value for %@ (%d) is out of range, substituting %d"
+ "valueForProperty:"
+ "valueWithCGSize:"
+ "viewOnWakeDisabled"
+ "watchChoice:"
+ "watchChoices"
+ "watchChooser:madeChoice:"
+ "watchScreenImageView"
+ "weakObjectsPointerArray"
+ "writeToURL:atomically:"
+ "{CGSize=dd}16@0:8"
+ "{CGSize=dd}32@0:8{CGSize=dd}16"
+ "{CGSize=dd}40@0:8{CGSize=dd}16f32f36"
+ "{os_unfair_lock_s=I}16@0:8"
- "@\"BBSectionInfo\"16@0:8"
- "T@\"BBSectionInfo\",R,N"
- "T@\"BBSectionInfo\",R,N,V_bbSectionInfo"

```

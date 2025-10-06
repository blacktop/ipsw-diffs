## PencilPairingUI

> `/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`

```diff

-136.4.4.0.0
-  __TEXT.__text: 0x1af98
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x263c
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0xb0f
-  __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__unwind_info: 0x980
-  __TEXT.__objc_classname: 0x7b7
-  __TEXT.__objc_methname: 0x7d40
-  __TEXT.__objc_methtype: 0x1ef4
-  __TEXT.__objc_stubs: 0x6180
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x630
-  __DATA_CONST.__objc_classlist: 0x158
+136.15.0.0.0
+  __TEXT.__text: 0x1fcf0
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x2bac
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0xe75
+  __TEXT.__oslogstring: 0x4f3
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__unwind_info: 0xad4
+  __TEXT.__objc_classname: 0x854
+  __TEXT.__objc_methname: 0x8447
+  __TEXT.__objc_methtype: 0x1a93
+  __TEXT.__objc_stubs: 0x6e60
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8fb0
-  __DATA_CONST.__objc_selrefs: 0x1c28
-  __DATA_CONST.__objc_classrefs: 0x320
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__objc_const: 0x1118
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x38c
+  __DATA_CONST.__objc_const: 0x8f80
+  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_classrefs: 0x368
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_arraydata: 0x100
+  __AUTH_CONST.__objc_const: 0x13e8
+  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__auth_got: 0x360
+  __AUTH.__objc_data: 0xf50
+  __DATA.__objc_ivar: 0x3d8
   __DATA.__data: 0xaf0
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/PencilKit.framework/PencilKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE0FC2D4-9107-308D-A741-CB2DED30802D
-  Functions: 898
-  Symbols:   3683
-  CStrings:  2023
+  UUID: E8E66C3D-0DE4-378F-B2DF-97EC45499080
+  Functions: 1026
+  Symbols:   4183
+  CStrings:  2203
 
Symbols:
+ +[BundleControllerHelper sharedInstance]
+ +[PNPPreDeclare squeezeInteraction:setMiniPaletteVisible:hoverLocation:inView:]
+ +[PNPSqueezeController _controllerWithType:buttonType:deviceType:delegate:]
+ +[PNPSqueezeThresholdController defaultThreshold]
+ +[PNPSqueezeThresholdController sharedController]
+ +[PNPSqueezeThresholdSliderCell opaqueTouchSenderDescriptor]
+ +[PencilSettings pencilUserDefaults]
+ +[PencilSettings sharedPencilSettings]
+ -[BundleControllerHelper .cxx_destruct]
+ -[BundleControllerHelper doubleTapRequiresHover]
+ -[BundleControllerHelper loadSpecifiersFromPlistName:stringsName:bundle:specifier:target:]
+ -[BundleControllerHelper opaqueTouchSenderDescriptor]
+ -[BundleControllerHelper setDoubleTapRequiresHover:]
+ -[BundleControllerHelper setOpaqueTouchProperty:value:]
+ -[PNPAnimatedHardwareView .cxx_destruct]
+ -[PNPAnimatedHardwareView configureForCurrentHardwareAndDevice]
+ -[PNPAnimatedHardwareView deviceType]
+ -[PNPAnimatedHardwareView hardwareType]
+ -[PNPAnimatedHardwareView layerForHardwareType:deviceType:]
+ -[PNPAnimatedHardwareView layoutSubviews]
+ -[PNPAnimatedHardwareView pencilLayer]
+ -[PNPAnimatedHardwareView preferredHeightForWidth:]
+ -[PNPAnimatedHardwareView setDeviceType:]
+ -[PNPAnimatedHardwareView setHardwareType:]
+ -[PNPAnimatedHardwareView setHardwareType:deviceType:]
+ -[PNPAnimatedHardwareView setPencilLayer:]
+ -[PNPDeviceState deviceType]
+ -[PNPDeviceState displayName]
+ -[PNPDeviceState setDeviceType:]
+ -[PNPDeviceState setDisplayName:]
+ -[PNPFeatureListController addDoubleTapBulletForPro]
+ -[PNPFeatureListController addDoubleTapBullet]
+ -[PNPFeatureListController addHoverBullet]
+ -[PNPFeatureListController addQuickNoteBullet]
+ -[PNPFeatureListController addScreenshotsBulletForPro]
+ -[PNPFeatureListController addScreenshotsBullet]
+ -[PNPFeatureListController addScribbleBulletIfNecessary]
+ -[PNPFeatureListController addSqueezeBullet]
+ -[PNPFeatureListController bulletCount]
+ -[PNPFeatureListController configureFor532]
+ -[PNPFeatureListController setBulletCount:]
+ -[PNPPairingViewController dismissViewControllerAnimated:completion:]
+ -[PNPPairingViewController pairingStartedWithDimming:deviceType:]
+ -[PNPPencilView prepareMovieForSpinningPencil:]
+ -[PNPSqueezeController .cxx_destruct]
+ -[PNPSqueezeController canvasView]
+ -[PNPSqueezeController dealloc]
+ -[PNPSqueezeController loadSqueezeAnimationLayer]
+ -[PNPSqueezeController loadSqueezeAnimationPackage]
+ -[PNPSqueezeController paletteHoverLocation]
+ -[PNPSqueezeController pencilLayerHiddenByInteraction]
+ -[PNPSqueezeController pencilLayer]
+ -[PNPSqueezeController setCanvasView:]
+ -[PNPSqueezeController setPaletteHoverLocation:]
+ -[PNPSqueezeController setPencilLayer:]
+ -[PNPSqueezeController setPencilLayerHiddenByInteraction:]
+ -[PNPSqueezeController setToolPicker:]
+ -[PNPSqueezeController toolPickerSelectedToolDidChange:]
+ -[PNPSqueezeController toolPickerVisibilityDidChange:]
+ -[PNPSqueezeController toolPicker]
+ -[PNPSqueezeController viewDidAppear:]
+ -[PNPSqueezeController viewDidLoad]
+ -[PNPSqueezeController viewWillAppear:]
+ -[PNPSqueezeController viewWillDisappear:]
+ -[PNPSqueezeThresholdController autoCalibrationInProgress]
+ -[PNPSqueezeThresholdController disableAutoCalibrationIfNecessary]
+ -[PNPSqueezeThresholdController disableSqueezeOnboardingMode]
+ -[PNPSqueezeThresholdController initializeToDefaultThreshold]
+ -[PNPSqueezeThresholdController opaqueTouchSenderDescriptor]
+ -[PNPSqueezeThresholdController resetAutoCalibration]
+ -[PNPSqueezeThresholdController setAutoCalibrationInProgress:]
+ -[PNPSqueezeThresholdController setSqueezeOnboardingModeEnabled:]
+ -[PNPSqueezeThresholdController setSqueezeThreshold:]
+ -[PNPSqueezeThresholdController squeezeOnboardingModeEnabled]
+ -[PNPSqueezeThresholdController squeezeThreshold]
+ -[PNPSqueezeThresholdController startAutoCalibrationIfNecessary]
+ -[PNPSqueezeThresholdController synchronizeSqueezeThresholdToBackboard]
+ -[PNPSqueezeThresholdSliderCell isExtendedRange]
+ -[PNPSqueezeThresholdSliderCell pencilSqueezeThreshold]
+ -[PNPSqueezeThresholdSliderCell refreshCellContentsWithSpecifier:]
+ -[PNPSqueezeThresholdSliderCell setPencilSqueezeThreshold:]
+ -[PNPSqueezeThresholdSliderCell squeezeThresholdToThreshold:]
+ -[PNPSqueezeThresholdSliderCell thresholdToSqueezeThreshold:]
+ -[PNPWelcomeController isRTL]
+ -[PNPWhatsNewController addDoubleTapBulletForPro]
+ -[PNPWhatsNewController addDoubleTapBullet]
+ -[PNPWhatsNewController addHoverBullet]
+ -[PNPWhatsNewController addQuickNoteBullet]
+ -[PNPWhatsNewController addScreenshotsBulletForPro]
+ -[PNPWhatsNewController addScreenshotsBullet]
+ -[PNPWhatsNewController addScribbleBulletIfNecessary]
+ -[PNPWhatsNewController addSmarterNotesBullet]
+ -[PNPWhatsNewController addSqueezeBullet]
+ -[PNPWhatsNewController bulletCount]
+ -[PNPWhatsNewController configureFor532]
+ -[PNPWhatsNewController setBulletCount:]
+ -[PNPWizardViewController createOnboardingControllerWithPencilUUID:]
+ -[PNPWizardViewController deviceStateDidChange]
+ -[PNPWizardViewController didCreateFindMyCoordinator]
+ -[PNPWizardViewController exit]
+ -[PNPWizardViewController prewarmFMUIControllerIfNecessary]
+ -[PNPWizardViewController prewarmFMUIController]
+ -[PNPWizardViewController prewarmFMUIController].cold.1
+ -[PNPWizardViewController setDidCreateFindMyCoordinator:]
+ -[PNPWizardViewController showFindMyController].cold.1
+ -[PencilSettings _postPencilSettingsDidChangeRemoteNotification]
+ -[PencilSettings init]
+ -[PencilSettings loadSettings]
+ -[PencilSettings observeValueForKeyPath:ofObject:change:context:]
+ -[PencilSettings preferredSqueezeAction]
+ -[PencilSettings preferredTapAction]
+ -[PencilSettings setPreferredSqueezeAction:]
+ -[PencilSettings setPreferredTapAction:]
+ -[PencilSettings syncSettingsToBackboard]
+ -[_PNPPencilMovieView assetName]
+ -[_PNPPencilMovieView initWithDeviceType:]
+ GCC_except_table13
+ GCC_except_table4
+ GCC_except_table8
+ GCC_except_table9
+ OBJC_IVAR_$_PSSpecifier.getter
+ OBJC_IVAR_$_PSSpecifier.setter
+ _BKSHIDServicesGetPersistentServiceProperties
+ _BKSHIDServicesSetPersistentServiceProperties
+ _CFRelease
+ _FindMyUICoreLibrary
+ _FindMyUICoreLibraryCore.frameworkLibrary
+ _IOHIDEventSystemClientCopyServices
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientSetMatching
+ _IOHIDServiceClientCopyProperty
+ _OBJC_CLASS_$_BKSHIDEventSenderDescriptor
+ _OBJC_CLASS_$_BundleControllerHelper
+ _OBJC_CLASS_$_CAPackage
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_PKInkingTool
+ _OBJC_CLASS_$_PKPencilSqueezeInteraction
+ _OBJC_CLASS_$_PKToolPicker
+ _OBJC_CLASS_$_PNPAnimatedHardwareView
+ _OBJC_CLASS_$_PNPPreDeclare
+ _OBJC_CLASS_$_PNPSqueezeController
+ _OBJC_CLASS_$_PNPSqueezeThresholdController
+ _OBJC_CLASS_$_PNPSqueezeThresholdSliderCell
+ _OBJC_CLASS_$_PSSliderTableCell
+ _OBJC_CLASS_$_PencilSettings
+ _OBJC_IVAR_$_BundleControllerHelper._bundleControllers
+ _OBJC_IVAR_$_PNPAnimatedHardwareView._deviceType
+ _OBJC_IVAR_$_PNPAnimatedHardwareView._hardwareType
+ _OBJC_IVAR_$_PNPAnimatedHardwareView._pencilLayer
+ _OBJC_IVAR_$_PNPDeviceState._deviceType
+ _OBJC_IVAR_$_PNPDeviceState._displayName
+ _OBJC_IVAR_$_PNPFeatureListController._bulletCount
+ _OBJC_IVAR_$_PNPSqueezeController._canvasView
+ _OBJC_IVAR_$_PNPSqueezeController._paletteHoverLocation
+ _OBJC_IVAR_$_PNPSqueezeController._pencilLayer
+ _OBJC_IVAR_$_PNPSqueezeController._pencilLayerHiddenByInteraction
+ _OBJC_IVAR_$_PNPSqueezeController._toolPicker
+ _OBJC_IVAR_$_PNPSqueezeThresholdSliderCell._isExtendedRange
+ _OBJC_IVAR_$_PNPSqueezeThresholdSliderCell._numTicks
+ _OBJC_IVAR_$_PNPSqueezeThresholdSliderCell._tickValues
+ _OBJC_IVAR_$_PNPWhatsNewController._bulletCount
+ _OBJC_IVAR_$_PNPWizardViewController._didCreateFindMyCoordinator
+ _OBJC_IVAR_$_PencilSettings._preferredSqueezeAction
+ _OBJC_IVAR_$_PencilSettings._preferredTapAction
+ _OBJC_IVAR_$__PNPPencilMovieView._deviceType
+ _OBJC_METACLASS_$_BundleControllerHelper
+ _OBJC_METACLASS_$_PNPAnimatedHardwareView
+ _OBJC_METACLASS_$_PNPPreDeclare
+ _OBJC_METACLASS_$_PNPSqueezeController
+ _OBJC_METACLASS_$_PNPSqueezeThresholdController
+ _OBJC_METACLASS_$_PNPSqueezeThresholdSliderCell
+ _OBJC_METACLASS_$_PSSliderTableCell
+ _OBJC_METACLASS_$_PencilSettings
+ _PKInkTypePen
+ _PNPSliderIsExtendedRange
+ _PSControlMaximumKey
+ _PSControlMinimumKey
+ _PSDefaultValueKey
+ _PSSliderIsSegmented
+ _PSSliderSegmentCount
+ _PSSliderShowValueKey
+ _SpecifiersFromPlist
+ _UIPencilPreferredSqueezeActionKey
+ _UIPencilPreferredTapActionKey
+ __AXSPencilExtendedSqueezeRangeEnabled
+ __OBJC_$_CLASS_METHODS_BundleControllerHelper
+ __OBJC_$_CLASS_METHODS_PNPPreDeclare
+ __OBJC_$_CLASS_METHODS_PNPSqueezeController
+ __OBJC_$_CLASS_METHODS_PNPSqueezeThresholdController
+ __OBJC_$_CLASS_METHODS_PNPSqueezeThresholdSliderCell
+ __OBJC_$_CLASS_METHODS_PencilSettings
+ __OBJC_$_CLASS_PROP_LIST_PNPSqueezeThresholdController
+ __OBJC_$_INSTANCE_METHODS_BundleControllerHelper
+ __OBJC_$_INSTANCE_METHODS_PNPAnimatedHardwareView
+ __OBJC_$_INSTANCE_METHODS_PNPSqueezeController
+ __OBJC_$_INSTANCE_METHODS_PNPSqueezeThresholdController
+ __OBJC_$_INSTANCE_METHODS_PNPSqueezeThresholdSliderCell
+ __OBJC_$_INSTANCE_METHODS_PencilSettings
+ __OBJC_$_INSTANCE_VARIABLES_BundleControllerHelper
+ __OBJC_$_INSTANCE_VARIABLES_PNPAnimatedHardwareView
+ __OBJC_$_INSTANCE_VARIABLES_PNPFeatureListController
+ __OBJC_$_INSTANCE_VARIABLES_PNPSqueezeController
+ __OBJC_$_INSTANCE_VARIABLES_PNPSqueezeThresholdSliderCell
+ __OBJC_$_INSTANCE_VARIABLES_PNPWhatsNewController
+ __OBJC_$_INSTANCE_VARIABLES_PencilSettings
+ __OBJC_$_PROP_LIST_BundleControllerHelper
+ __OBJC_$_PROP_LIST_PNPAnimatedHardwareView
+ __OBJC_$_PROP_LIST_PNPFeatureListController
+ __OBJC_$_PROP_LIST_PNPSqueezeController
+ __OBJC_$_PROP_LIST_PNPSqueezeThresholdController
+ __OBJC_$_PROP_LIST_PNPSqueezeThresholdSliderCell
+ __OBJC_$_PROP_LIST_PNPWhatsNewController
+ __OBJC_$_PROP_LIST_PencilSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FMUIAccessoryOnboardingCoordinatorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PKToolPickerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FMUIAccessoryOnboardingCoordinatorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PKToolPickerObserver
+ __OBJC_$_PROTOCOL_REFS_FMUIAccessoryOnboardingCoordinatorDelegate
+ __OBJC_$_PROTOCOL_REFS_PKToolPickerObserver
+ __OBJC_CLASS_PROTOCOLS_$_PNPSqueezeController
+ __OBJC_CLASS_RO_$_BundleControllerHelper
+ __OBJC_CLASS_RO_$_PNPAnimatedHardwareView
+ __OBJC_CLASS_RO_$_PNPPreDeclare
+ __OBJC_CLASS_RO_$_PNPSqueezeController
+ __OBJC_CLASS_RO_$_PNPSqueezeThresholdController
+ __OBJC_CLASS_RO_$_PNPSqueezeThresholdSliderCell
+ __OBJC_CLASS_RO_$_PencilSettings
+ __OBJC_LABEL_PROTOCOL_$_FMUIAccessoryOnboardingCoordinatorDelegate
+ __OBJC_LABEL_PROTOCOL_$_PKToolPickerObserver
+ __OBJC_METACLASS_RO_$_BundleControllerHelper
+ __OBJC_METACLASS_RO_$_PNPAnimatedHardwareView
+ __OBJC_METACLASS_RO_$_PNPPreDeclare
+ __OBJC_METACLASS_RO_$_PNPSqueezeController
+ __OBJC_METACLASS_RO_$_PNPSqueezeThresholdController
+ __OBJC_METACLASS_RO_$_PNPSqueezeThresholdSliderCell
+ __OBJC_METACLASS_RO_$_PencilSettings
+ __OBJC_PROTOCOL_$_FMUIAccessoryOnboardingCoordinatorDelegate
+ __OBJC_PROTOCOL_$_PKToolPickerObserver
+ __PNPSignpostLog
+ __PNPSignpostLog.___PNPSignpostLog
+ __PNPSignpostLog.onceToken
+ ___31-[PNPWizardViewController exit]_block_invoke
+ ___36+[PencilSettings pencilUserDefaults]_block_invoke
+ ___38+[PencilSettings sharedPencilSettings]_block_invoke
+ ___40+[BundleControllerHelper sharedInstance]_block_invoke
+ ___49+[PNPSqueezeThresholdController sharedController]_block_invoke
+ ___53-[BundleControllerHelper opaqueTouchSenderDescriptor]_block_invoke
+ ___54-[PNPSqueezeController toolPickerVisibilityDidChange:]_block_invoke
+ ___60+[PNPSqueezeThresholdSliderCell opaqueTouchSenderDescriptor]_block_invoke
+ ___60-[PNPSqueezeThresholdController opaqueTouchSenderDescriptor]_block_invoke
+ ___FindMyUICoreLibraryCore_block_invoke
+ ____PNPSignpostLog_block_invoke
+ ___block_descriptor_32_e44_v16?0"BKSMutableHIDEventSenderDescriptor"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSNumber"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.11
+ ___block_literal_global.14
+ ___block_literal_global.2
+ ___block_literal_global.22
+ ___block_literal_global.68
+ ___getFMUIAccessoryOnboardingCoordinatorClass_block_invoke
+ ___getFMUIAccessoryOnboardingCoordinatorClass_block_invoke.cold.1
+ ___getFMUIDiscoveredAccessoryClass_block_invoke
+ ___getFMUIDiscoveredAccessoryClass_block_invoke.cold.1
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ __os_log_impl
+ __sl_dlopen
+ __unnamed_array_storage.31
+ __unnamed_array_storage.38
+ __unnamed_array_storage.43
+ __unnamed_array_storage.50
+ _abort_report_np
+ _audit_stringFindMyUICore
+ _free
+ _getFMUIAccessoryOnboardingCoordinatorClass.softClass
+ _getFMUIDiscoveredAccessoryClass.softClass
+ _getOpaqueTouchValue
+ _kCAPackageTypeArchive
+ _kCFAllocatorDefault
+ _kExtendedRangeTickValues
+ _kNormalTickValues
+ _objc_getClass
+ _objc_msgSend$_existingInteractionForWindowScene:
+ _objc_msgSend$_paletteView
+ _objc_msgSend$_postPencilSettingsDidChangeRemoteNotification
+ _objc_msgSend$_preferredSqueezeAction
+ _objc_msgSend$_setMiniPaletteVisible:hoverLocation:inView:
+ _objc_msgSend$addDoubleTapBullet
+ _objc_msgSend$addDoubleTapBulletForPro
+ _objc_msgSend$addHoverBullet
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addQuickNoteBullet
+ _objc_msgSend$addScreenshotsBullet
+ _objc_msgSend$addScreenshotsBulletForPro
+ _objc_msgSend$addScribbleBulletIfNecessary
+ _objc_msgSend$addSmarterNotesBullet
+ _objc_msgSend$addSqueezeBullet
+ _objc_msgSend$assetName
+ _objc_msgSend$autoCalibrationInProgress
+ _objc_msgSend$boolValue
+ _objc_msgSend$build:
+ _objc_msgSend$bulletCount
+ _objc_msgSend$bundlePath
+ _objc_msgSend$configureFor532
+ _objc_msgSend$configureForCurrentHardwareAndDevice
+ _objc_msgSend$createOnboardingControllerWithPencilUUID:
+ _objc_msgSend$defaultThreshold
+ _objc_msgSend$deviceStateDidChange
+ _objc_msgSend$didCreateFindMyCoordinator
+ _objc_msgSend$displayName
+ _objc_msgSend$exit
+ _objc_msgSend$findMyCoordinator
+ _objc_msgSend$hardwareType
+ _objc_msgSend$imageNamed:inBundle:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithDeviceType:
+ _objc_msgSend$initWithIdentifier:productType:productImage:
+ _objc_msgSend$initWithInkType:color:
+ _objc_msgSend$initWithPresenter:accessory:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initializeToDefaultThreshold
+ _objc_msgSend$isRTL
+ _objc_msgSend$isVisible
+ _objc_msgSend$layerForHardwareType:deviceType:
+ _objc_msgSend$loadSettings
+ _objc_msgSend$loadSqueezeAnimationLayer
+ _objc_msgSend$loadSqueezeAnimationPackage
+ _objc_msgSend$opaqueTouchSenderDescriptor
+ _objc_msgSend$packageWithContentsOfURL:type:options:error:
+ _objc_msgSend$pairingStartedWithDimming:
+ _objc_msgSend$pencilLayer
+ _objc_msgSend$pencilLayerHiddenByInteraction
+ _objc_msgSend$pencilUserDefaults
+ _objc_msgSend$postNotificationName:object:userInfo:deliverImmediately:
+ _objc_msgSend$preferredTapAction
+ _objc_msgSend$prepareMovieForSpinningPencil:
+ _objc_msgSend$prewarmFMUIController
+ _objc_msgSend$prewarmFMUIControllerIfNecessary
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$recordSetPencilPerferredAction:
+ _objc_msgSend$removeFromSuperlayer
+ _objc_msgSend$rootLayer
+ _objc_msgSend$selectedTool
+ _objc_msgSend$setAffineTransform:
+ _objc_msgSend$setAnchorPoint:
+ _objc_msgSend$setAnimationDuration:
+ _objc_msgSend$setAutoCalibrationInProgress:
+ _objc_msgSend$setAutoHideEnabled:
+ _objc_msgSend$setAutoresizingMask:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setBulletCount:
+ _objc_msgSend$setCanvasView:
+ _objc_msgSend$setCompletionBlock:
+ _objc_msgSend$setDidCreateFindMyCoordinator:
+ _objc_msgSend$setDrawingPolicy:
+ _objc_msgSend$setGeometryFlipped:
+ _objc_msgSend$setHardwareType:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setOpaqueTouchProperty:value:
+ _objc_msgSend$setPencilLayer:
+ _objc_msgSend$setPencilLayerHiddenByInteraction:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setPrimaryPage:primaryUsage:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setSelectedTool:
+ _objc_msgSend$setSqueezeOnboardingModeEnabled:
+ _objc_msgSend$setSqueezeThreshold:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setTool:
+ _objc_msgSend$setToolPicker:
+ _objc_msgSend$setVisible:forFirstResponder:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$sharedController
+ _objc_msgSend$sharedPencilSettings
+ _objc_msgSend$shouldShowFMOnboardingFlow
+ _objc_msgSend$showFindMyController
+ _objc_msgSend$squeezeInteraction:setMiniPaletteVisible:hoverLocation:inView:
+ _objc_msgSend$squeezeOnboardingModeEnabled
+ _objc_msgSend$squeezeThreshold
+ _objc_msgSend$squeezeThresholdToThreshold:
+ _objc_msgSend$start
+ _objc_msgSend$syncSettingsToBackboard
+ _objc_msgSend$synchronize
+ _objc_msgSend$synchronizeSqueezeThresholdToBackboard
+ _objc_msgSend$thresholdToSqueezeThreshold:
+ _objc_msgSend$toolPicker
+ _objc_msgSend$windowScene
+ _objc_retain_x24
+ _objc_retain_x25
+ _os_log_create
+ _os_log_type_enabled
+ _pencilUserDefaults.__pencilUserDefaults
+ _pencilUserDefaults.onceToken
+ _sharedController.onceToken
+ _sharedController.sController
+ _sharedInstance.sHelper
+ _sharedPencilSettings.__sharedPencilSettings
+ _sharedPencilSettings.onceToken
- +[PNPFindMyController _controllerWithType:buttonType:deviceType:delegate:]
- -[PNPFindMyController .cxx_destruct]
- -[PNPFindMyController mapView]
- -[PNPFindMyController setMapView:]
- -[PNPFindMyController viewDidLoad]
- -[PNPPencilView prepareMovieForSpinningPencil]
- _NSLog
- _OBJC_CLASS_$_MKMapView
- _OBJC_CLASS_$_PNPFindMyController
- _OBJC_IVAR_$_PNPFindMyController._mapView
- _OBJC_METACLASS_$_PNPFindMyController
- __OBJC_$_CLASS_METHODS_PNPFindMyController
- __OBJC_$_INSTANCE_METHODS_PNPFindMyController
- __OBJC_$_INSTANCE_VARIABLES_PNPFindMyController
- __OBJC_$_PROP_LIST_PNPFindMyController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MKMapViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MKMapViewDelegate
- __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
- __OBJC_$_PROTOCOL_REFS_MKMapViewDelegate
- __OBJC_CLASS_PROTOCOLS_$_PNPFindMyController
- __OBJC_CLASS_RO_$_PNPFindMyController
- __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
- __OBJC_LABEL_PROTOCOL_$_MKMapViewDelegate
- __OBJC_METACLASS_RO_$_PNPFindMyController
- __OBJC_PROTOCOL_$_CLLocationManagerDelegate
- __OBJC_PROTOCOL_$_MKMapViewDelegate
- ___block_literal_global.18
- ___block_literal_global.58
- __unnamed_array_storage.20
- __unnamed_array_storage.25
- _objc_msgSend$UUID
- _objc_msgSend$prepareMovieForSpinningPencil
- _objc_msgSend$setMapView:
CStrings:
+ "%s"
+ "-B332"
+ "-B532"
+ "@\"CALayer\""
+ "@\"PKToolPicker\""
+ "@32@0:8Q16q24"
+ "@56@0:8@16@24@32@40@48"
+ "APPLE_PENCIL_NAME_PRO"
+ "Auto-calibration not done, setting default value: %g"
+ "BundleControllerHelper"
+ "Current squeeze threshold %@"
+ "Did load wizard view controller"
+ "Disabling squeeze onboarding mode"
+ "DoubleTapGestureDisabled"
+ "Error getting animation package: %@"
+ "Error getting squeeze animation package: %@"
+ "FMUIAccessoryOnboardingCoordinator"
+ "FMUIAccessoryOnboardingCoordinatorDelegate"
+ "FMUICoordinator result for should show find my controller: %d"
+ "FMUIDiscoveredAccessory"
+ "GesturesOnlyWhileHoveringEnabled"
+ "PKToolPickerObserver"
+ "PNPAnimatedHardwareView"
+ "PNPParingVCDidAppearNotification"
+ "PNPParingVCDidDisappearNotification"
+ "PNPPreDeclare"
+ "PNPSqueezeController"
+ "PNPSqueezeThresholdController"
+ "PNPSqueezeThresholdSliderCell"
+ "PNPWizardViewController prepareForPresentation. Device type: %ld, shouldShowWhatsNew: %d"
+ "PencilFindMyPin"
+ "PencilPairingSqueeze-B532"
+ "Prewarm Error: nil pencilUUID needed create AccessoryOnboardingCoordinator"
+ "Prewarming find my controller for pencilID: %@"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "SQUEEZE_DESCRIPTION"
+ "SQUEEZE_TITLE"
+ "Setting index for PNPWelcomeController: %ld"
+ "Setting new auto-calibrated value: %@"
+ "Setting opaque touch property: %@: %@"
+ "Setting squeeze threshold: %@"
+ "Setting squeze threshold: %@ (index: %@)"
+ "ShowFindMyController Error: nil pencilUUID for FMUIDiscoveredAccessory needed create FMUIAccessoryOnboardingCoordinator"
+ "Squeeze"
+ "SqueezeAutoCalibrationEnabled"
+ "SqueezeGestureDisabled"
+ "SqueezeOnboardingModeEnabled"
+ "SqueezeThreshold"
+ "Synchronizing squeeze threshold to default value: %g"
+ "Synchronizing squeeze threshold: %@"
+ "Syncing settings to backboard"
+ "T@\"CALayer\",&,N,V_pencilLayer"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSString\",C,N,V_displayName"
+ "T@\"PKCanvasView\",&,N,V_canvasView"
+ "T@\"PKToolPicker\",&,N,V_toolPicker"
+ "TB,N,V_didCreateFindMyCoordinator"
+ "TB,N,V_pencilLayerHiddenByInteraction"
+ "TB,R,N,V_isExtendedRange"
+ "TQ,N,V_hardwareType"
+ "Tq,N,V_bulletCount"
+ "Tq,N,V_preferredSqueezeAction"
+ "Tq,N,V_preferredTapAction"
+ "T{CGPoint=dd},N,V_paletteHoverLocation"
+ "Unable to find class %s"
+ "WELCOME_DETAIL_TEXT_PRO"
+ "WELCOME_SCREENSHOT_DESCRIPTION_PRO"
+ "WELCOME_SCREENSHOT_DESCRIPTION_RTOL_PRO"
+ "WELCOME_SQUEEZE_DESCRIPTION"
+ "WELCOME_SQUEEZE_TITLE"
+ "WELCOME_SWITCH_TOOLS_DESCRIPTION_PRO"
+ "WELCOME_TITLE_PRO"
+ "Warning: failed to load preferences plist '%@.plist' for bundle %@"
+ "_bulletCount"
+ "_bundleControllers"
+ "_didCreateFindMyCoordinator"
+ "_displayName"
+ "_existingInteractionForWindowScene:"
+ "_hardwareType"
+ "_isExtendedRange"
+ "_numTicks"
+ "_paletteHoverLocation"
+ "_paletteView"
+ "_pencilLayer"
+ "_pencilLayerHiddenByInteraction"
+ "_postPencilSettingsDidChangeRemoteNotification"
+ "_preferredSqueezeAction"
+ "_preferredTapAction"
+ "_setMiniPaletteVisible:hoverLocation:inView:"
+ "_tickValues"
+ "_toolPicker"
+ "addDoubleTapBullet"
+ "addDoubleTapBulletForPro"
+ "addHoverBullet"
+ "addObserver:"
+ "addQuickNoteBullet"
+ "addScreenshotsBullet"
+ "addScreenshotsBulletForPro"
+ "addScribbleBulletIfNecessary"
+ "addSmarterNotesBullet"
+ "addSqueezeBullet"
+ "apple_pencil-B532"
+ "assetName"
+ "autoCalibrationInProgress"
+ "boolValue"
+ "build:"
+ "bulletCount"
+ "bundlePath"
+ "caar"
+ "com.apple.UIKit"
+ "com.apple.pencilpairingui"
+ "com.apple.sharingd"
+ "configureFor532"
+ "configureForCurrentHardwareAndDevice"
+ "createOnboardingControllerWithPencilUUID:"
+ "defaultThreshold"
+ "deviceStateDidChange"
+ "didCreateFindMyCoordinator"
+ "disableAutoCalibrationIfNecessary"
+ "disableSqueezeOnboardingMode"
+ "displayName"
+ "doubleTapRequiresHover"
+ "exit"
+ "extendedRange"
+ "hardwareType"
+ "hasEverShownEduUI"
+ "hasSeenScribbleEducationPanelsKey"
+ "imageNamed:inBundle:"
+ "initWithContentsOfFile:"
+ "initWithDeviceType:"
+ "initWithIdentifier:productType:productImage:"
+ "initWithInkType:color:"
+ "initWithPresenter:accessory:"
+ "initWithSuiteName:"
+ "initializeToDefaultThreshold"
+ "isExtendedRange"
+ "isRTL"
+ "isVisible"
+ "lastSeenWhatsNewVersionKey"
+ "layerForHardwareType:deviceType:"
+ "loadSettings"
+ "loadSpecifiersFromPlistName:stringsName:bundle:specifier:target:"
+ "loadSqueezeAnimationLayer"
+ "loadSqueezeAnimationPackage"
+ "opaqueTouchSenderDescriptor"
+ "packageWithContentsOfURL:type:options:error:"
+ "pairingStartedWithDimming:deviceType:"
+ "paletteHoverLocation"
+ "pencilInteraction:didReceiveSqueeze:"
+ "pencilInteraction:didReceiveTap:"
+ "pencilLayer"
+ "pencilLayerHiddenByInteraction"
+ "pencilSqueezeThreshold"
+ "pencilUserDefaults"
+ "postNotificationName:object:userInfo:deliverImmediately:"
+ "preferredHeightForWidth:"
+ "preferredSqueezeAction"
+ "preferredTapAction"
+ "prepareMovieForSpinningPencil:"
+ "prewarmFMUIController"
+ "prewarmFMUIControllerIfNecessary"
+ "propertyForKey:"
+ "r^d"
+ "refreshCellContentsWithSpecifier:"
+ "removeFromSuperlayer"
+ "resetAutoCalibration"
+ "rootLayer"
+ "selectedTool"
+ "setAffineTransform:"
+ "setAnchorPoint:"
+ "setAnimationDuration:"
+ "setAutoCalibrationInProgress:"
+ "setAutoCalibrationInProgress: %d (readback: %d)"
+ "setAutoHideEnabled:"
+ "setAutoresizingMask:"
+ "setBool:forKey:"
+ "setBulletCount:"
+ "setCanvasView:"
+ "setCompletionBlock:"
+ "setDidCreateFindMyCoordinator:"
+ "setDisplayName:"
+ "setDoubleTapRequiresHover:"
+ "setDrawingPolicy:"
+ "setGeometryFlipped:"
+ "setHardwareType:"
+ "setHardwareType:deviceType:"
+ "setInteger:forKey:"
+ "setOpacity:"
+ "setOpaqueTouchProperty:value:"
+ "setPaletteHoverLocation:"
+ "setPencilLayer:"
+ "setPencilLayerHiddenByInteraction:"
+ "setPencilSqueezeThreshold:"
+ "setPosition:"
+ "setPreferredSqueezeAction:"
+ "setPreferredTapAction:"
+ "setPrimaryPage:primaryUsage:"
+ "setProperty:forKey:"
+ "setSelectedTool:"
+ "setSqueezeOnboardingModeEnabled:"
+ "setSqueezeOnboardingModeEnabled: %d (readback: %d)"
+ "setSqueezeThreshold:"
+ "setTarget:"
+ "setTool:"
+ "setToolPicker:"
+ "setVisible:forFirstResponder:"
+ "setWithObject:"
+ "sharedController"
+ "sharedPencilSettings"
+ "shouldShowFMOnboardingFlow"
+ "showFindMyController pencilUUID: %@"
+ "signposts"
+ "softlink:r:path:/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore"
+ "squeezeInteraction:setMiniPaletteVisible:hoverLocation:inView:"
+ "squeezeOnboardingModeEnabled"
+ "squeezeThreshold"
+ "squeezeThresholdToThreshold:"
+ "start"
+ "startAutoCalibrationIfNecessary"
+ "syncSettingsToBackboard"
+ "synchronize"
+ "synchronizeSqueezeThresholdToBackboard"
+ "thresholdToSqueezeThreshold:"
+ "toolPicker"
+ "toolPickerFramesObscuredDidChange:"
+ "toolPickerIsRulerActiveDidChange:"
+ "toolPickerSelectedToolDidChange:"
+ "toolPickerVisibilityDidChange:"
+ "v16@?0@\"BKSMutableHIDEventSenderDescriptor\"8"
+ "v24@0:8@\"PKToolPicker\"16"
+ "v28@0:8@\"FMUIAccessoryOnboardingCoordinator\"16B24"
+ "v32@0:8@\"UIPencilInteraction\"16@\"UIPencilInteractionSqueeze\"24"
+ "v32@0:8@\"UIPencilInteraction\"16@\"UIPencilInteractionTap\"24"
+ "v32@0:8Q16q24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v52@0:8@16B24{CGPoint=dd}28@44"
+ "welcomeSqueezePane-B532"
+ "welcome_double_tap"
+ "welcome_scribble"
+ "welcome_squeeze"
+ "welcome_swipe"
+ "windowScene"
- "@\"MKAnnotationView\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"MKClusterAnnotation\"32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "@\"MKMapView\""
- "@\"MKOverlayRenderer\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKOverlayView\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "Annotate"
- "B24@0:8@\"CLLocationManager\"16"
- "CLLocationManagerDelegate"
- "FIND_MY_DESCRIPTION"
- "FIND_MY_TITLE"
- "MKMapViewDelegate"
- "PNPFindMyController"
- "Pencil"
- "PencilPairing-HUMMINGBIRD"
- "ScreenCapture"
- "Scribble"
- "Still pencil uuid, using a random UUID"
- "T@\"MKMapView\",&,N,V_mapView"
- "UUID"
- "_mapView"
- "locationManager:didChangeAuthorizationStatus:"
- "locationManager:didDetermineState:forRegion:"
- "locationManager:didEnterRegion:"
- "locationManager:didExitRegion:"
- "locationManager:didFailRangingBeaconsForConstraint:error:"
- "locationManager:didFailWithError:"
- "locationManager:didFinishDeferredUpdatesWithError:"
- "locationManager:didRangeBeacons:inRegion:"
- "locationManager:didRangeBeacons:satisfyingConstraint:"
- "locationManager:didStartMonitoringForRegion:"
- "locationManager:didUpdateHeading:"
- "locationManager:didUpdateLocations:"
- "locationManager:didUpdateToLocation:fromLocation:"
- "locationManager:didVisit:"
- "locationManager:monitoringDidFailForRegion:withError:"
- "locationManager:rangingBeaconsDidFailForRegion:withError:"
- "locationManagerDidChangeAuthorization:"
- "locationManagerDidPauseLocationUpdates:"
- "locationManagerDidResumeLocationUpdates:"
- "locationManagerShouldDisplayHeadingCalibration:"
- "mapView"
- "mapView:annotationView:calloutAccessoryControlTapped:"
- "mapView:annotationView:didChangeDragState:fromOldState:"
- "mapView:clusterAnnotationForMemberAnnotations:"
- "mapView:didAddAnnotationViews:"
- "mapView:didAddOverlayRenderers:"
- "mapView:didAddOverlayViews:"
- "mapView:didChangeUserTrackingMode:animated:"
- "mapView:didDeselectAnnotation:"
- "mapView:didDeselectAnnotationView:"
- "mapView:didFailToLocateUserWithError:"
- "mapView:didSelectAnnotation:"
- "mapView:didSelectAnnotationView:"
- "mapView:didUpdateUserLocation:"
- "mapView:regionDidChangeAnimated:"
- "mapView:regionWillChangeAnimated:"
- "mapView:rendererForOverlay:"
- "mapView:viewForAnnotation:"
- "mapView:viewForOverlay:"
- "mapViewDidChangeVisibleRegion:"
- "mapViewDidFailLoadingMap:withError:"
- "mapViewDidFinishLoadingMap:"
- "mapViewDidFinishRenderingMap:fullyRendered:"
- "mapViewDidStopLocatingUser:"
- "mapViewWillStartLoadingMap:"
- "mapViewWillStartLocatingUser:"
- "mapViewWillStartRenderingMap:"
- "pencilUUID: %@"
- "prepareMovieForSpinningPencil"
- "setMapView:"
- "v24@0:8@\"CLLocationManager\"16"
- "v24@0:8@\"MKMapView\"16"
- "v28@0:8@\"CLLocationManager\"16i24"
- "v28@0:8@\"MKMapView\"16B24"
- "v28@0:8@16i24"
- "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
- "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
- "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
- "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
- "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
- "v32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "v32@0:8@\"MKMapView\"16@\"MKAnnotationView\"24"
- "v32@0:8@\"MKMapView\"16@\"MKUserLocation\"24"
- "v32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "v32@0:8@\"MKMapView\"16@\"NSError\"24"
- "v36@0:8@\"MKMapView\"16q24B32"
- "v36@0:8@16q24B32"
- "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
- "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
- "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
- "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
- "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
- "v40@0:8@\"MKMapView\"16@\"MKAnnotationView\"24@\"UIControl\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"MKMapView\"16@\"MKAnnotationView\"24Q32Q40"
- "v48@0:8@16@24Q32Q40"

```

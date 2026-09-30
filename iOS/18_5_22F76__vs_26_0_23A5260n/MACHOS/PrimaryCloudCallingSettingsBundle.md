## PrimaryCloudCallingSettingsBundle

> `/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle`

```diff

-2975.600.42.2.1
-  __TEXT.__text: 0x53b8
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x12e0
-  __TEXT.__objc_methlist: 0x6e4
-  __TEXT.__const: 0x538
-  __TEXT.__cstring: 0x44e
-  __TEXT.__objc_methname: 0x166c
-  __TEXT.__oslogstring: 0x732
-  __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methtype: 0x287
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__cfstring: 0x4c0
-  __DATA_CONST.__objc_classlist: 0x30
+3011.100.2.2.10
+  __TEXT.__text: 0x4598
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x1320
+  __TEXT.__objc_methlist: 0x54c
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x50f
+  __TEXT.__objc_methname: 0x14b9
+  __TEXT.__oslogstring: 0x82a
+  __TEXT.__objc_classname: 0x10a
+  __TEXT.__objc_methtype: 0x281
+  __TEXT.__unwind_info: 0x198
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__cfstring: 0x580
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x7a8
-  __DATA.__objc_selrefs: 0x788
-  __DATA.__objc_ivar: 0x28
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x218
-  __DATA.__bss: 0x198
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x788
+  __DATA.__objc_selrefs: 0x6c0
+  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0x38
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/CallsDialer.framework/CallsDialer
+  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 175A8CE6-38D8-3640-84BC-83971A692EC6
-  Functions: 175
-  Symbols:   136
-  CStrings:  439
+  UUID: 00585A8C-531B-3A02-ABF8-E9278AE1B478
+  Functions: 118
+  Symbols:   143
+  CStrings:  434
 
Symbols:
+ _AKDeviceListChangedNotification
+ _ConduitUserDefaultsSuiteName
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_TUAvailableDevicesHelper
+ __Unwind_Resume
+ ___objc_personality_v0
+ _kIncomingCallBannerEnabledKey
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_retain_x1
- _MGGetProductType
- _OBJC_CLASS_$_CADisplay
- _OBJC_CLASS_$_UIDevice
- _OBJC_METACLASS_$_PHUIConfiguration
- _PHUIInCallControlAlignmentIs
CStrings:
+ "Adding new deviceID %@ to the enabled devices list."
+ "AppleTV"
+ "B"
+ "Could not find defaults for suite %@ with key %@"
+ "NEARBY_INCOMING_CALL_NOTIFICATIONS_FOOTER"
+ "NEARBY_INCOMING_CALL_NOTIFICATIONS_HEADER"
+ "Received device list changed event. Reloading specifiers"
+ "Removing deviceID %@ from the enabled devices list %@."
+ "T@\"NSArray\",&,N,V_callNotificationsEligibleDeviceList"
+ "TB,N,V_devicesEligibleForCallNotifications"
+ "[WARN] Not showing the primary cloud-calling settings because: ((supportsThumperCalling:%@ || supportsRelayCalling:%@) && supportsPrimaryCalling:%@ && supportsDisplayingFaceTimeVideoCalls:%@) || otherDevicesAvailable:%@"
+ "_callNotificationsEligibleDeviceList"
+ "_devicesEligibleForCallNotifications"
+ "aa_altDSID"
+ "ams_activeiCloudAccount"
+ "ams_sharedAccountStore"
+ "arrayForKey:"
+ "callNotificationsEligibleDeviceList"
+ "cloudDeviceSpecifiers"
+ "com.apple.NeighborhoodActivityConduitService"
+ "containsObject:"
+ "deviceID %@ already exists in the enabled devices list %@."
+ "deviceListChanged:"
+ "devicesEligibleForCallNotifications"
+ "getAvailableCallNotificationDevices"
+ "getAvailableDevicesForAccountID:operatingSystem:model:minimumMajorVersion:completion:"
+ "getIncomingCallBannerEnabled:"
+ "getRemoteDevicesAvailableForCallNotifications"
+ "incomingCallBannerEnabledDevices"
+ "incomingCallDeviceSpecifiers"
+ "initWithParentListController:"
+ "initWithSuiteName:"
+ "model"
+ "removeObject:"
+ "serialNumber"
+ "setCallNotificationsEligibleDeviceList:"
+ "setDevicesEligibleForCallNotifications:"
+ "setIncomingCallBannerEnabled:specifier:"
+ "setObject:forKey:"
+ "tvOS"
+ "v16@?0@\"NSArray\"8"
- "Determined screen size to be %ld for screenHeight: %d"
- "PHUIConfiguration"
- "[WARN] Not showing the primary cloud-calling settings because: (supportsThumperCalling:%@ || supportsRelayCalling:%@) && supportsPrimaryCalling:%@ && supportsDisplayingFaceTimeVideoCalls:%@"
- "ambientAudioRoutesButtonSize"
- "ambientAudioRoutesInset"
- "ambientAudioRoutesSymbolInset"
- "ambientHorizontalPadding"
- "ambientHorizontalSizeClass"
- "ambientInCallControlSize"
- "ambientInCallControlSpacing"
- "ambientVerticalPadding"
- "ambientVerticalSizeClass"
- "canAutoRotateInCallUIForFaceTime"
- "canAutoRotateInCallUIForFaceTimeAudio"
- "canRotateInCallUIOverlayForFaceTime"
- "contentViewSizeForFaceTime"
- "currentDevice"
- "d16@0:8"
- "deviceSpecifiers"
- "distanceBetweenEndButtonAndKeyPadLastRow"
- "handsetDialerSize"
- "handsetDialerSpacing"
- "inCallBottomBarAssetSize"
- "inCallBottomBarLowerOffset"
- "inCallBottomBarMaxTitleSize"
- "inCallBottomBarSpacing"
- "inCallControlAlignment"
- "inCallControlButtonSizeRatio"
- "inCallControlButtonVerticalSpacingRatio"
- "inCallControlSize"
- "inCallControlSpacing"
- "inCallFaceTimeOverlayUISize"
- "inCallSlideToAnswerSize"
- "inComingCallAndInCallControlsBottomPaddingRatio"
- "inComingCallSupplementalButtonAndMainButtonSpacingRatio"
- "mainDisplay"
- "pipPartialHomeOffset"
- "pipRadius"
- "pipStatusBarPadding"
- "pipWallInset"
- "pipWidth"
- "screenSize"
- "shouldUseExplicitLayoutDimensions"
- "shouldUseFullScreenPeoplePicker"
- "shouldUseSOSTightSpacing"
- "tableViewCellVerticalSpacing"
- "userInterfaceIdiom"
- "voicemailLayoutSpacing"
- "yOffsetForDialerLCDView"
- "yOffsetForDialerLCDViewForDxDevices"
- "yOffsetForParticipantsView"
- "yParticipantsViewAdjustmentForKeypad"

```

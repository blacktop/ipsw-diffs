## NotificationsSettings

> `/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-310.2.2.0.0
-  __TEXT.__text: 0x5b15c
-  __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_stubs: 0x6300
-  __TEXT.__objc_methlist: 0x258c
+310.2.4.0.0
+  __TEXT.__text: 0x5bc90
+  __TEXT.__auth_stubs: 0x1ec0
+  __TEXT.__objc_stubs: 0x63e0
+  __TEXT.__objc_methlist: 0x25c4
   __TEXT.__const: 0x1aa4
   __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__objc_methname: 0x84df
-  __TEXT.__cstring: 0x3dcb
+  __TEXT.__objc_methname: 0x860f
+  __TEXT.__cstring: 0x3edb
   __TEXT.__objc_classname: 0x875
   __TEXT.__objc_methtype: 0x1095
   __TEXT.__oslogstring: 0xea2

   __TEXT.__swift_as_cont: 0x118
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1b28
-  __TEXT.__eh_frame: 0x1548
-  __DATA_CONST.__const: 0x1e78
-  __DATA_CONST.__cfstring: 0x3300
+  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__eh_frame: 0x1570
+  __DATA_CONST.__const: 0x1e60
+  __DATA_CONST.__cfstring: 0x3380
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x108
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0xf58
-  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__auth_got: 0xf70
+  __DATA_CONST.__got: 0x9d0
   __DATA_CONST.__auth_ptr: 0x428
-  __DATA.__objc_const: 0x5ee0
-  __DATA.__objc_selrefs: 0x1f80
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_const: 0x5f40
+  __DATA.__objc_selrefs: 0x1fc8
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__objc_data: 0x1020
-  __DATA.__data: 0x12a8
+  __DATA.__data: 0x12c0
   __DATA.__common: 0x510
   - /System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1862
-  Symbols:   560
-  CStrings:  2011
+  Functions: 1870
+  Symbols:   568
+  CStrings:  2029
 
Symbols:
+ _NCBundleIdentifiersExcludedFromSiri
+ _NCDevicePrefixedImageForKeyWithDefaultSystemClock
+ _NCIsExcludedFromSiriForBundleIdentifier
+ _OBJC_CLASS_$_UITraitDisplayScale
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ _UIGraphicsEndImageContext
+ _UIRectCenteredXInRectScale
+ _UIRoundToScale
+ _kNCSiriAppExclusionChangedBundleIdentifiersKey
+ _kNCSiriAppExclusionChangedNotification
+ _kTCCServiceSiriAccess
- _MGIsDeviceOfType
- _NCDeviceImageWithDefaultSystemClock
- _NCLoadFromCoverSheetKit
- _NCLockScreenTimeAttributedStringWithFont
CStrings:
+ "@\"NSSet\""
+ "AppExclusions"
+ "EXCLUDED_FROM_SIRI_BUNDLE_IDENTIFIERS_KEY"
+ "EXCLUDED_FROM_SIRI_KEY"
+ "IntelligenceFlow"
+ "NCSiriAppExclusionChangedBundleIdentifiers"
+ "NCSiriAppExclusionChangedNotification"
+ "RESTRICT_ACCESS_ID"
+ "SPOKEN_NOTIFICATIONS_APP_EXCLUDED_FROM_SIRI_EDIT_LINK"
+ "SPOKEN_NOTIFICATIONS_APP_EXCLUDED_FROM_SIRI_FOOTER"
+ "SiriSettings"
+ "_builtExcludedFromSiriBundleIdentifiers"
+ "_didPushExcludedAppsSettings"
+ "_excludedFromSiri"
+ "_excludedFromSiriBundleIdentifiers"
+ "_updateForTraitChange"
+ "ipad-legacy"
+ "ipad-legacy-banners"
+ "ipad-legacy-count"
+ "ipad-legacy-history"
+ "ipad-legacy-list"
+ "ipad-legacy-lockscreen"
+ "ipad-legacy-stack"
+ "iphone-D20"
+ "iphone-D5x"
+ "iphone-D6x"
+ "iphone-D7x"
+ "iphone-V68"
+ "iphone-V68-banners"
+ "iphone-V68-count"
+ "iphone-V68-history"
+ "iphone-V68-lockscreen"
+ "iphone-V68-stack"
+ "iphone-V6x"
+ "isEqualToSet:"
+ "postNotificationName:object:userInfo:"
+ "registerForTraitChanges:withTarget:action:"
+ "set"
+ "setWithArray:"
+ "settingsNavigationProxy_pushPaneWithContentIdentifier:bundleName:"
+ "siriAppExclusionChanged:"
+ "tappedExcludedAppsSettings:"
+ "userInfo"
- "%@-dark"
- "%@-legacy"
- "-legacy"
- "D20"
- "D5x"
- "D6x"
- "D7x"
- "V68"
- "V6x"
- "com.apple.CoverSheetKit"
- "ipad-banners-dark"
- "ipad-banners-legacy"
- "ipad-banners-legacy-dark"
- "ipad-count-legacy"
- "ipad-history-dark"
- "ipad-history-legacy"
- "ipad-history-legacy-dark"
- "ipad-list-legacy"
- "ipad-lockscreen-dark"
- "ipad-lockscreen-legacy"
- "ipad-lockscreen-legacy-dark"
- "ipad-stack-legacy"
- "iphone"
- "traitCollectionDidChange:"
- "updateForUserInterfaceStyleChange"
```

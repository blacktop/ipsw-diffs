## PreferencesMigrator

> `/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator`

```diff

-1308.4.4.0.0
-  __TEXT.__text: 0x1cd0
-  __TEXT.__auth_stubs: 0x310
+1341.0.0.0.0
+  __TEXT.__text: 0x1d28
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_stubs: 0x700
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x350
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__cstring: 0x375
   __TEXT.__oslogstring: 0x40a
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methname: 0x66c
   __TEXT.__objc_methtype: 0x58
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x198
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
-  - /System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI
   - /System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI
   - /System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F49CA32B-6448-3AC4-B62B-9C674DB1A7AB
-  Functions: 29
-  Symbols:   77
-  CStrings:  150
+  UUID: 9187D4A5-A030-3AEC-8DF1-24C882C1C08A
+  Functions: 32
+  Symbols:   80
+  CStrings:  152
 
Symbols:
+ _dispatch_once
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _os_log_create
- _PSUILogForCategory
CStrings:
+ "Base"
+ "com.apple.Settings.DataMigrator"

```

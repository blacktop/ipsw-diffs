## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1765.14.0.0.0
-  __TEXT.__text: 0x162908
-  __TEXT.__auth_stubs: 0x4280
-  __TEXT.__objc_stubs: 0x22820
-  __TEXT.__objc_methlist: 0x11c94
+1773.2.0.0.0
+  __TEXT.__text: 0x163798
+  __TEXT.__auth_stubs: 0x42f0
+  __TEXT.__objc_stubs: 0x22840
+  __TEXT.__objc_methlist: 0x11d44
   __TEXT.__const: 0x1a30
   __TEXT.__gcc_except_tab: 0x3284
-  __TEXT.__objc_methname: 0x30cbc
-  __TEXT.__cstring: 0x1762c
-  __TEXT.__oslogstring: 0x379d
-  __TEXT.__objc_classname: 0x3f32
+  __TEXT.__objc_methname: 0x30def
+  __TEXT.__cstring: 0x1775c
+  __TEXT.__oslogstring: 0x37bd
+  __TEXT.__objc_classname: 0x3f67
   __TEXT.__objc_methtype: 0x5dd5
   __TEXT.__dlopen_cstrs: 0x236
   __TEXT.__ustring: 0x2e

   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x14c
-  __TEXT.__unwind_info: 0x5110
+  __TEXT.__unwind_info: 0x5150
   __TEXT.__eh_frame: 0x170
-  __DATA_CONST.__auth_got: 0x2150
-  __DATA_CONST.__got: 0x2170
+  __DATA_CONST.__auth_got: 0x2188
+  __DATA_CONST.__got: 0x2180
   __DATA_CONST.__auth_ptr: 0x4b0
-  __DATA_CONST.__const: 0x4b68
-  __DATA_CONST.__cfstring: 0x1a480
-  __DATA_CONST.__objc_classlist: 0xd78
+  __DATA_CONST.__const: 0x4ba8
+  __DATA_CONST.__cfstring: 0x1a6e0
+  __DATA_CONST.__objc_classlist: 0xd80
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa58
+  __DATA_CONST.__objc_superrefs: 0xa60
   __DATA_CONST.__objc_intobj: 0x1a58
   __DATA_CONST.__objc_arraydata: 0x12b0
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x1c0
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0xa78
-  __DATA.__objc_const: 0x1ee78
-  __DATA.__objc_selrefs: 0xb588
-  __DATA.__objc_ivar: 0xd60
-  __DATA.__objc_data: 0x8cb0
+  __DATA.__objc_const: 0x1efc0
+  __DATA.__objc_selrefs: 0xb5c8
+  __DATA.__objc_ivar: 0xd70
+  __DATA.__objc_data: 0x8d00
   __DATA.__data: 0x2bb2
   __DATA.__bss: 0x18ed
   __DATA.__common: 0x50

   - /System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings
   - /System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7691
-  Symbols:   18329
-  CStrings:  12590
+  Functions: 7712
+  Symbols:   18374
+  CStrings:  12622
 
Symbols:
+ -[AXAudioController alwaysShowVolumeControlEnabled:]
+ -[AXAudioController mixToUplink:]
+ -[AXAudioController setAlwaysShowVolumeControlEnabled:specifier:]
+ -[AXMixToUplinkController .cxx_destruct]
+ -[AXMixToUplinkController _appSupportsUplink:]
+ -[AXMixToUplinkController _generateAppSpecifiers]
+ -[AXMixToUplinkController _setAppSupportsUplink:specifier:]
+ -[AXMixToUplinkController mixToUplink:]
+ -[AXMixToUplinkController setMixToUplink:specifier:]
+ -[AXMixToUplinkController specifiers]
+ -[AXMixToUplinkController viewDidLoad]
+ -[AXSiriSettingsController event:params:reply:]
+ -[AXSiriSettingsController localAuthContext]
+ -[AXSiriSettingsController setLocalAuthContext:]
+ -[UIViewController(AXMedinaPreboardSecureIntent) accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:]
+ GCC_except_table42
+ OBJC_IVAR_$_AXMixToUplinkController._appSpecifiers
+ OBJC_IVAR_$_AXMixToUplinkController._deniedApps
+ OBJC_IVAR_$_AXMixToUplinkController._supportedApps
+ OBJC_IVAR_$_AXSiriSettingsController._localAuthContext
+ _OBJC_CLASS_$_AXMixToUplinkController
+ _OBJC_METACLASS_$_AXMixToUplinkController
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ _TCCAccessCopyBundleIdentifiersForService
+ _TCCAccessSetForBundleId
+ __AXSAllowsMixToUplink
+ __AXSAlwaysShowVolumeControlEnabled
+ __AXSAlwaysShowVolumeControlSetEnabled
+ __AXSSetAllowsMixToUplink
+ __OBJC_$_INSTANCE_METHODS_AXMixToUplinkController
+ __OBJC_$_INSTANCE_METHODS_UIViewController(AXTripleClickConflictAvoidance|AXMedinaPreboardSecureIntent|ClarityUI)
+ __OBJC_$_INSTANCE_VARIABLES_AXMixToUplinkController
+ __OBJC_$_PROP_LIST_AXSiriSettingsController
+ __OBJC_CLASS_PROTOCOLS_$_AXSiriSettingsController
+ __OBJC_CLASS_RO_$_AXMixToUplinkController
+ __OBJC_METACLASS_RO_$_AXMixToUplinkController
+ ___141-[UIViewController(AXMedinaPreboardSecureIntent) accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:]_block_invoke
+ ___141-[UIViewController(AXMedinaPreboardSecureIntent) accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:]_block_invoke_2
+ ___141-[UIViewController(AXMedinaPreboardSecureIntent) accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:]_block_invoke_3
+ ___141-[UIViewController(AXMedinaPreboardSecureIntent) accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:]_block_invoke_4
+ ___38-[AXMixToUplinkController viewDidLoad]_block_invoke
+ __block_literal_global.466
+ __block_literal_global.468
+ __block_literal_global.499
+ __block_literal_global.846
+ __block_literal_global.873
+ _kAXSAllowsMixToUplinkDidChangeNotification
+ _kTCCServiceMicrophoneInjection
+ _objc_msgSend$bundleContainerURL
- GCC_except_table41
- __OBJC_$_INSTANCE_METHODS_UIViewController(AXTripleClickConflictAvoidance|ClarityUI)
- __block_literal_global.483
- __block_literal_global.836
- __block_literal_global.863
CStrings:
+ "\v\x12"
+ "ALLOWED_APPS"
+ "ALWAYS_SHOW_VOLUME_CONTROL"
+ "ALWAYS_SHOW_VOLUME_CONTROL_FOOTER"
+ "AXCameraControl"
+ "AXMedinaPreboardSecureIntent"
+ "AXMixToUplinkController"
+ "AXPAAlwaysShowVolumeControlSpecID"
+ "CAMERA_CONTROL"
+ "CAMERA_CONTROL_SWITCH"
+ "LIGHT_PRESS"
+ "LIGHT_PRESS_FORCE"
+ "MIX_TO_UPLINK"
+ "MIX_TO_UPLINK_FOOTER"
+ "MIX_TO_UPLINK_SUB_TITLE"
+ "MIX_TO_UPLINK_TITLE"
+ "MixToUplink"
+ "MotionCuesOff"
+ "MotionCuesOn"
+ "MotionCuesOnInCar"
+ "SECURE_INTENT_CUSTOM_SOUND_CANCEL"
+ "SECURE_INTENT_CUSTOM_SOUND_REBOOT"
+ "SWIPE"
+ "Setting TCC microphone for %!@(MISSING)=%!@(MISSING) result=%!@(MISSING)"
+ "_appSupportsUplink:"
+ "_deniedApps"
+ "_setAppSupportsUplink:specifier:"
+ "_supportedApps"
+ "accessibilityPresentMedinaPreboardAlertWithTitle:message:completionBlock:cancellationBlock:"
+ "alwaysShowVolumeControlEnabled:"
+ "bundleContainerURL"
+ "intelligence"
+ "mixToUplink:"
+ "setAlwaysShowVolumeControlEnabled:specifier:"
+ "setMixToUplink:specifier:"
+ "url"
- "\v\x11"
- "MotionCuesLearnMoreItemAppearsInVehicleDescription"
- "MotionCuesLearnMoreItemAppearsInVehicleTitle"
- "car.fill"

```

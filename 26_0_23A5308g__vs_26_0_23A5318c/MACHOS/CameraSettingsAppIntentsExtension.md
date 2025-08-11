## CameraSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension`

```diff

-4096.0.0.0.2
-  __TEXT.__text: 0xa204
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0x9d4
-  __TEXT.__cstring: 0x39d1
+4097.6.5.0.0
+  __TEXT.__text: 0xa698
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__const: 0x9e4
+  __TEXT.__cstring: 0x3ae1
   __TEXT.__constg_swiftt: 0x104
   __TEXT.__swift5_typeref: 0x3a0
   __TEXT.__swift5_fieldmd: 0x2c8
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__objc_methname: 0x523
+  __TEXT.__objc_methname: 0x5ad
   __TEXT.__swift5_reflstr: 0x487
   __TEXT.__swift5_assocty: 0x118
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__oslogstring: 0x1d2
   __TEXT.__unwind_info: 0x2e8
   __TEXT.__eh_frame: 0x220
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x4d0
   __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__data: 0x300
   __DATA.__bss: 0x1010
   __DATA.__common: 0x38
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2A2D6CF8-C4CB-36C9-B17E-D614BA307C94
+  UUID: 57454D96-13D0-3249-B1A5-3A9F0CAB431E
   Functions: 197
-  Symbols:   104
-  CStrings:  285
+  Symbols:   122
+  CStrings:  316
 
Symbols:
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSBundle
+ __CFPreferencesCopyAppValueWithContainer
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_error_impl
+ __os_log_impl
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x8
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x8
+ _os_log_create
+ _os_log_type_enabled
Functions:
~ sub_10000970c -> sub_1000097bc : 76 -> 1248
CStrings:
+ "Camera"
+ "CameraButtonSensitivity"
+ "Could not find CameraOverlayAngel bundle record: %{public}@"
+ "Disabling camera adjustments by default due to disabled gestures"
+ "Disabling camera adjustments by default due to lack of usage history"
+ "Enabling camera adjustments by default due to behavior defaults written"
+ "Enabling camera adjustments by default due to explicitly enabled gestures"
+ "Enabling camera adjustments by default due to last-used control data: %@"
+ "Inspecting defaults for Camera Control usage history"
+ "bundleIdentifier"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "com.apple.Accessibility"
+ "com.apple.CameraOverlayAngel"
+ "dataContainerURL"
+ "isEqualToString:"
+ "mainBundle"
+ "objectForKey:"
+ "path"
+ "systemOverlay.halfPressGestureEnabled"
+ "systemOverlay.hidesClientControls"
+ "systemOverlay.lastUsedControl"
+ "systemOverlay.menuToggleMaxIntervalMilliseconds"
+ "systemOverlay.swipeToPresentEnabled"

```

## CameraOverlayServices

> `/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`

```diff

-4097.62.6.0.3
-  __TEXT.__text: 0xa420
-  __TEXT.__auth_stubs: 0x3c0
+4097.80.9.0.0
+  __TEXT.__text: 0xb19c
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x101c
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x6b9
-  __TEXT.__oslogstring: 0x2b7
+  __TEXT.__cstring: 0x804
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__oslogstring: 0x589
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_classname: 0x257
-  __TEXT.__objc_methname: 0x2042
+  __TEXT.__objc_methname: 0x213e
   __TEXT.__objc_methtype: 0x550
-  __TEXT.__objc_stubs: 0x1740
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x260
+  __TEXT.__objc_stubs: 0x1860
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x828
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xc80
+  __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C97DF075-DD7A-3DB3-AE08-A81E0C57B336
-  Functions: 302
-  Symbols:   1137
-  CStrings:  704
+  UUID: 3AB7A732-0C3E-321E-8A00-0146EB70EB52
+  Functions: 315
+  Symbols:   1179
+  CStrings:  745
 
Symbols:
+ _CAMApplyCameraControlSettingsData
+ _CAMApplyCameraControlSettingsData.cold.1
+ _CAMApplyCameraControlSettingsData.cold.2
+ _CAMCameraAdjustmentsEnabled
+ _CAMCameraControlSettingsData
+ _CAMCameraControlSettingsData.cold.1
+ _CAMDeleteCameraAdjustmentsDefault
+ _CAMLastUsedOverlayControlData
+ _CAMLastUsedOverlayControlData.cold.1
+ _CAMUserPreferenceCameraAdjustmentsEnabled
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyAppValue
+ _CFPreferencesSetAppValue
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSUserDefaults
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __CAMCameraAdjustmentsEnabledFromDictionary
+ __CAMCameraControlSettingsDictionary
+ __CFPreferencesCopyAppValueWithContainer
+ __CFPreferencesSetAppValueWithContainer
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$dataContainerURL
+ _objc_msgSend$dictionary
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$path
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
CStrings:
+ "CAMUserPreferenceCameraAdjustmentsEnabled"
+ "CameraButtonSensitivity"
+ "Could not find CameraOverlayAngel bundle record for setting last used control: %{public}@"
+ "Could not find CameraOverlayAngel bundle record: %{public}@"
+ "Disabling camera adjustments by default due to disabled gestures"
+ "Disabling camera adjustments by default due to lack of usage history"
+ "Disabling camera adjustments by default due to nil data"
+ "Enabling camera adjustments by default due to behavior defaults written"
+ "Enabling camera adjustments by default due to explicitly enabled gestures"
+ "Enabling camera adjustments by default due to last-used control data: %@"
+ "Failed to archive camera control settings: %{public}@"
+ "Failed to unarchive camera control settings: %{public}@"
+ "Inspecting defaults for Camera Control usage history"
+ "Settings"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "com.apple.Accessibility"
+ "com.apple.CameraOverlayAngel"
+ "com.apple.camera"
+ "dataContainerURL"
+ "dictionary"
+ "objectForKey:"
+ "path"
+ "setObject:forKeyedSubscript:"
+ "standardUserDefaults"
+ "systemOverlay.halfPressGestureEnabled"
+ "systemOverlay.hidesClientControls"
+ "systemOverlay.lastUsedControl"
+ "systemOverlay.menuToggleMaxIntervalMilliseconds"
+ "systemOverlay.swipeToPresentEnabled"
+ "unarchivedObjectOfClasses:fromData:error:"

```

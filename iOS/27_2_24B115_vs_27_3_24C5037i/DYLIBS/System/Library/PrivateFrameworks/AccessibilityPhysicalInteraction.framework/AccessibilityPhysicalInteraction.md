## AccessibilityPhysicalInteraction

> `/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x1d768
-  __TEXT.__objc_methlist: 0x210c
-  __TEXT.__const: 0x6ed
+3245.8.14.0.0
+  __TEXT.__text: 0x1e2fc
+  __TEXT.__objc_methlist: 0x2154
+  __TEXT.__const: 0x72d
   __TEXT.__dlopen_cstrs: 0xb6
   __TEXT.__constg_swiftt: 0x8c
-  __TEXT.__swift5_typeref: 0xc0
+  __TEXT.__swift5_typeref: 0xca
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__cstring: 0x9bd
+  __TEXT.__cstring: 0x9c6
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_cont: 0x70
-  __TEXT.__oslogstring: 0x730
-  __TEXT.__swift5_capture: 0xa8
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__unwind_info: 0xd10
-  __TEXT.__eh_frame: 0x5d0
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_cont: 0x7c
+  __TEXT.__oslogstring: 0x903
+  __TEXT.__swift5_capture: 0xc8
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__gcc_except_tab: 0x1e8
+  __TEXT.__unwind_info: 0xd68
+  __TEXT.__eh_frame: 0x6e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18b8
+  __DATA_CONST.__objc_selrefs: 0x1930
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x588
-  __AUTH_CONST.__const: 0x660
+  __DATA_CONST.__got: 0x5b0
+  __AUTH_CONST.__const: 0x6b0
   __AUTH_CONST.__cfstring: 0x7e0
-  __AUTH_CONST.__objc_const: 0x28d0
+  __AUTH_CONST.__objc_const: 0x2900
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x1e0
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__data: 0x338
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 977
-  Symbols:   1638
-  CStrings:  147
+  Functions: 997
+  Symbols:   1656
+  CStrings:  156
 
Symbols:
+ -[AXPISystemActionHelper _backEscapeTargetInApplication:]
+ -[AXPISystemActionHelper _performScrollAction:onDisplay:]
+ -[AXPISystemActionHelper performActionButtonItemRecognitionAction]
+ -[AXPISystemActionHelper performBack]
+ -[AXPISystemActionHelper scrollDownOnDisplay:]
+ -[AXPISystemActionHelper scrollUpOnDisplay:]
+ -[AXPISystemActionHelper usesSilentModeForMute]
+ GCC_except_table246
+ GCC_except_table268
+ GCC_except_table330
+ GCC_except_table392
+ GCC_except_table721
+ GCC_except_table748
+ _AXDeviceIsRingerSwitchAvailable
+ _AXUIDisplayConfigurationForDisplayID
+ _AXUIScreenForDisplayIDWithFallback
+ _CGRectIsEmpty
+ _OBJC_CLASS_$_AXVoiceOverServer
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_AXPISystemActionHelper._fingerControllerDisplayID
+ __AXSApplicationAccessibilityEnabled
+ __AXSSetAccessibilityEnabled
+ ___57-[AXPISystemActionHelper _performScrollAction:onDisplay:]_block_invoke
+ _kAXBackButtonTrait
+ _swift_release_x21
+ _symbolic SbIeAgHr_
- -[AXPISystemActionHelper _performScrollAction:]
- GCC_except_table245
- GCC_except_table267
- GCC_except_table327
- GCC_except_table386
- GCC_except_table715
- GCC_except_table742
- ___47-[AXPISystemActionHelper _performScrollAction:]_block_invoke
CStrings:
+ "Action Button Image Recognition command failed to reach VoiceOver — VoiceOver may not be running."
+ "Back: enabling application accessibility"
+ "Back: nothing to go back from in %{public}@"
+ "Back: performed escape on %{public}@"
+ "Back: pressed back button in %{public}@: %d"
+ "Mute action: setting Silent Mode to %{public}d"
+ "Scrolling %{public}s on display %u (requested %u), orientation %d, screen rect {%.0f, %.0f, %.0f, %.0f}"
+ "Skipping scroll: empty screen rect for display %u"
+ "down"
+ "up"
- "3"
```

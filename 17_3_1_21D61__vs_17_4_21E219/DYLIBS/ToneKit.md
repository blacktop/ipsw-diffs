## ToneKit

> `/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit`

```diff

-603.0.0.0.0
-  __TEXT.__text: 0x22e70
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x2a40
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__cstring: 0x15db
-  __TEXT.__oslogstring: 0x856
+605.0.0.0.0
+  __TEXT.__text: 0x23794
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x2a48
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__cstring: 0x162e
+  __TEXT.__oslogstring: 0xa1f
   __TEXT.__ustring: 0x9c
-  __TEXT.__unwind_info: 0xa90
-  __TEXT.__objc_classname: 0x6d0
-  __TEXT.__objc_methname: 0xa76e
+  __TEXT.__dlopen_cstrs: 0xb7
+  __TEXT.__unwind_info: 0xaac
+  __TEXT.__objc_classname: 0x6d4
+  __TEXT.__objc_methname: 0xa862
   __TEXT.__objc_methtype: 0x19fa
-  __TEXT.__objc_stubs: 0x7b40
+  __TEXT.__objc_stubs: 0x7c00
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x50e0
-  __DATA_CONST.__objc_selrefs: 0x22c8
+  __DATA_CONST.__objc_const: 0x5120
+  __DATA_CONST.__objc_selrefs: 0x2300
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0xf0
   __AUTH_CONST.__objc_const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x1020
+  __AUTH_CONST.__cfstring: 0x1040
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x348
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x300
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x404
+  __AUTH_CONST.__auth_got: 0x360
+  __AUTH.__objc_data: 0xa00
+  __DATA.__objc_ivar: 0x40c
   __DATA.__data: 0x780
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1003
-  Symbols:   3887
-  CStrings:  2012
+  Functions: 1013
+  Symbols:   3927
+  CStrings:  2034
 
Symbols:
+ -[TKTonePickerViewController _isAllowedToPresentMediaPicker]
+ -[TKTonePickerViewController _isAllowedToPresentMediaPicker].cold.1
+ -[TKTonePickerViewController _isAllowedToPresentMediaPicker].cold.2
+ GCC_except_table59
+ GCC_except_table73
+ _CoreServicesLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_TKTonePickerViewController._isAllowedToPresentMediaPicker
+ _OBJC_IVAR_$_TKTonePickerViewController._isAllowedToPresentMediaPickerFlagLoaded
+ _OUTLINED_FUNCTION_6
+ _PrivacyDisclosureCoreLibraryCore.frameworkLibrary
+ ___CoreServicesLibraryCore_block_invoke
+ ___PrivacyDisclosureCoreLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___getLSApplicationRecordClass_block_invoke
+ ___getLSApplicationRecordClass_block_invoke.cold.1
+ ___getPDCPreflightManagerClass_block_invoke
+ ___getPDCPreflightManagerClass_block_invoke.cold.1
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringCoreServices
+ _audit_stringPrivacyDisclosureCore
+ _getLSApplicationRecordClass.softClass
+ _getPDCPreflightManagerClass.softClass
+ _objc_getClass
+ _objc_msgSend$_isAllowedToPresentMediaPicker
+ _objc_msgSend$applicationState
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithTargetQueue:
+ _objc_msgSend$isBeingPresented
+ _objc_msgSend$isValid
+ _objc_msgSend$requiresPreflightForApplicationRecord:
- GCC_except_table72
- _objc_msgSend$showsMedia
CStrings:
+ "\x04\"\x16\x11!"
+ "%s"
+ "%{public}@: Failed to retrieve record %{public}@ for Music application with error: %{public}@."
+ "%{public}@: Music application %{public}@ does not require preflight for privacy disclosure according to %{public}@."
+ "%{public}@: Music application %{public}@ requires preflight for privacy disclosure according to %{public}@."
+ "%{public}@: Showing media is not allowed. Will prevent selection of songs."
+ "%{public}@: State for Music application %{public}@ is invalid."
+ "LSApplicationRecord"
+ "PDCPreflightManager"
+ "T@\"NSString\",?,R,C"
+ "Unable to find class %s"
+ "_isAllowedToPresentMediaPicker"
+ "_isAllowedToPresentMediaPickerFlagLoaded"
+ "applicationState"
+ "com.apple.Music"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithTargetQueue:"
+ "isBeingPresented"
+ "isValid"
+ "requiresPreflightForApplicationRecord:"
+ "softlink:r:path:/System/Library/Frameworks/CoreServices.framework/CoreServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore"
+ "\xf01"
- "\x04(\x11!"

```

## ScreenTimeUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI`

```diff

-537.3.3.0.0
-  __TEXT.__text: 0x1bdfc
+537.4.20.1.0
+  __TEXT.__text: 0x1c288
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x1450
+  __TEXT.__objc_methlist: 0x17dc
   __TEXT.__const: 0x126
-  __TEXT.__cstring: 0xd6c
+  __TEXT.__cstring: 0xd7c
   __TEXT.__gcc_except_tab: 0x46c
   __TEXT.__oslogstring: 0x24e1
   __TEXT.__ustring: 0x4

   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x798
-  __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x5b51
-  __TEXT.__objc_methtype: 0x8dc
-  __TEXT.__objc_stubs: 0x4a00
+  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__objc_classname: 0x1ea
+  __TEXT.__objc_methname: 0x5bca
+  __TEXT.__objc_methtype: 0x91d
+  __TEXT.__objc_stubs: 0x4a40
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15e0
+  __DATA_CONST.__objc_selrefs: 0x1760
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x1040
-  __AUTH_CONST.__objc_const: 0x2d80
+  __AUTH_CONST.__objc_const: 0x2758
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x164

   - /System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
-  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 55950C4C-5D34-32D1-861A-B0DEAECEB376
-  Functions: 671
-  Symbols:   1989
-  CStrings:  1530
+  UUID: ECAB2A0B-0F42-3ACC-A313-85B517731AE8
+  Functions: 685
+  Symbols:   1995
+  CStrings:  1536
 
Symbols:
+ +[STBlockingUILog log].cold.1
+ +[STIconCache sharedCache].cold.1
+ +[STRemotePasscodeController _xpcConnection].cold.1
+ -[STBlockingViewController _approveOneMoreMinuteWithPreemptiveHide]
+ -[STBlockingViewController _ignoreLimitWithPreemptiveHideForAdditionalTime:]
+ -[STBlockingViewController updateAppearanceUsingBlockedContactHandles:contactNameByHandle:forBundleIdentifier:isApplicationCurrentlyLimited:contactStore:].cold.1
+ -[STBlockingViewController updateAppearanceUsingPolicy:forBundleIdentifier:].cold.3
+ -[STBlockingViewController updateAppearanceUsingPolicy:forCategoryIdentifier:].cold.2
+ -[STBlockingViewController updateAppearanceUsingPolicy:forWebpageURL:].cold.3
+ -[STLockoutViewController setView:].cold.1
+ -[STPasscodeField initWithFrame:length:].cold.1
+ -[STPasscodeField setLength:].cold.1
+ -[STPasscodeField setLength:].cold.2
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __43-[STBlockingViewController _oneMoreMinute:]_block_invoke.cold.1
+ __58-[STBlockingViewController _ignoreLimitForAdditionalTime:]_block_invoke.cold.1
+ __67-[STBlockingViewController _approveOneMoreMinuteWithPreemptiveHide]_block_invoke_3.cold.1
+ __76-[STBlockingViewController _ignoreLimitWithPreemptiveHideForAdditionalTime:]_block_invoke_3.cold.1
+ ___67-[STBlockingViewController _approveOneMoreMinuteWithPreemptiveHide]_block_invoke
+ ___67-[STBlockingViewController _approveOneMoreMinuteWithPreemptiveHide]_block_invoke_2
+ ___67-[STBlockingViewController _approveOneMoreMinuteWithPreemptiveHide]_block_invoke_3
+ ___76-[STBlockingViewController _ignoreLimitWithPreemptiveHideForAdditionalTime:]_block_invoke
+ ___76-[STBlockingViewController _ignoreLimitWithPreemptiveHideForAdditionalTime:]_block_invoke_2
+ ___76-[STBlockingViewController _ignoreLimitWithPreemptiveHideForAdditionalTime:]_block_invoke_3
+ ___block_descriptor_40_e17_v16?0"NSError"8l
+ __block_literal_global.176
+ _objc_msgSend$_approveOneMoreMinuteWithPreemptiveHide
+ _objc_msgSend$_ignoreLimitWithPreemptiveHideForAdditionalTime:
- __43-[STBlockingViewController _oneMoreMinute:]_block_invoke_3.cold.1
- __58-[STBlockingViewController _ignoreLimitForAdditionalTime:]_block_invoke_3.cold.1
- ___43-[STBlockingViewController _oneMoreMinute:]_block_invoke_2
- ___43-[STBlockingViewController _oneMoreMinute:]_block_invoke_3
- ___58-[STBlockingViewController _ignoreLimitForAdditionalTime:]_block_invoke_2
- ___58-[STBlockingViewController _ignoreLimitForAdditionalTime:]_block_invoke_3
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ScreenTimeUI
- __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftIntents_$_ScreenTimeUI
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "T@\"UIConversationContext\",?,&,N"
+ "_approveOneMoreMinuteWithPreemptiveHide"
+ "_ignoreLimitWithPreemptiveHideForAdditionalTime:"
+ "fast_debounce"
+ "v24@0:8@\"UIConversationContext\"16"

```

## GameControllerUI

> `/System/Library/PrivateFrameworks/GameControllerUI.framework/GameControllerUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x6638
-  __TEXT.__objc_methlist: 0x7fc
-  __TEXT.__const: 0x186
-  __TEXT.__cstring: 0x196
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__oslogstring: 0x218
+14.0.21.0.0
+  __TEXT.__text: 0x770c
+  __TEXT.__objc_methlist: 0x964
+  __TEXT.__const: 0x196
+  __TEXT.__cstring: 0x1c8
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__oslogstring: 0x418
   __TEXT.__swift5_typeref: 0x148
   __TEXT.__swift5_reflstr: 0x3c
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__unwind_info: 0x378
   __TEXT.__eh_frame: 0xd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e0
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x170
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x23a0
+  __AUTH_CONST.__const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0x2970
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x520
-  __DATA.__bss: 0x1b0
+  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x6a0
+  __DATA.__bss: 0x1d0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/GameController.framework/GameController
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 207
-  Symbols:   762
-  CStrings:  34
+  Functions: 247
+  Symbols:   879
+  CStrings:  54
 
Symbols:
+ +[GCGameIntentGamePolicyAction supportsSecureCoding]
+ +[GCGameIntentOpenPlatformGameLibraryAction homeScreenService]
+ -[GCGameIntentGamePolicyAction copyWithZone:]
+ -[GCGameIntentGamePolicyAction encodeWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithOptions:]
+ -[GCGameIntentGamePolicyAction init]
+ -[GCGameIntentGamePolicyAction performAction]
+ -[GCGameIntentLaunchAppleGamesAction(GamePolicy) performAction]
+ -[GCGameIntentLaunchApplicationAction(UI) performAction]
+ -[GCGameIntentOpenPlatformGameLibraryAction tryPresentAppLibraryPod:]
+ -[GCGameIntentOpenPlatformGameLibraryAction(UI) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) tryMergeWithOther:]
+ -[_GCUserNotificationConfiguration(UI) _ui_configureNotificationDictionary:]
+ GCC_except_table0
+ GCC_except_table10
+ GCC_except_table6
+ GCC_except_table9
+ _OBJC_CLASS_$_GCGameIntentGamePolicyAction
+ _OBJC_CLASS_$_GCGameIntentLaunchAppleGamesAction
+ _OBJC_CLASS_$_GCGameIntentLaunchApplicationAction
+ _OBJC_CLASS_$_GCGameIntentOpenPlatformGameLibraryAction
+ _OBJC_CLASS_$_GCGameIntentShowAppleGameOverlayAction
+ _OBJC_CLASS_$_GPUserExperienceProxy
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_SBSHomeScreenService
+ _OBJC_CLASS_$__GCUserNotificationConfiguration
+ _OBJC_IVAR_$_GCGameIntentGamePolicyAction._options
+ _OBJC_METACLASS_$_GCGameIntentGamePolicyAction
+ _SBSSuspendFrontmostApplication
+ __OBJC_$_CATEGORY_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_GCGameIntentLaunchApplicationAction_$_UI
+ __OBJC_$_CATEGORY_GCGameIntentOpenPlatformGameLibraryAction_$_UI
+ __OBJC_$_CATEGORY_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentLaunchApplicationAction_$_UI
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentOpenPlatformGameLibraryAction_$_UI
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__GCUserNotificationConfiguration_$_UI
+ __OBJC_$_CATEGORY__GCUserNotificationConfiguration_$_UI
+ __OBJC_$_CLASS_METHODS_GCGameIntentGamePolicyAction
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentGamePolicyAction
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentGamePolicyAction
+ __OBJC_$_INSTANCE_VARIABLES_GCGameIntentGamePolicyAction
+ __OBJC_$_PROP_LIST_GCGameIntentGamePolicyAction
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCGameIntentAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_GCGameIntentAction
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentGamePolicyAction
+ __OBJC_CLASS_RO_$_GCGameIntentGamePolicyAction
+ __OBJC_LABEL_PROTOCOL_$_GCGameIntentAction
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_GCGameIntentGamePolicyAction
+ __OBJC_PROTOCOL_$_GCGameIntentAction
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___45-[GCGameIntentGamePolicyAction performAction]_block_invoke
+ ___45-[GCGameIntentGamePolicyAction performAction]_block_invoke_2
+ ___62-[GCGameIntentOpenPlatformGameLibraryAction(UI) performAction]_block_invoke
+ ___62-[GCGameIntentOpenPlatformGameLibraryAction(UI) performAction]_block_invoke_2
+ ___66+[GCGameIntentOpenPlatformGameLibraryAction(UI) homeScreenService]_block_invoke
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke_2
+ ___73-[GCGameIntentOpenPlatformGameLibraryAction(UI) tryPresentAppLibraryPod:]_block_invoke
+ ____gc_log_game_intent_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e19_v16?0"GCPromise"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e19_v16?0"GCPromise"8ls32l8
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __gc_log_game_intent
+ __gc_log_game_intent.Log
+ __gc_log_game_intent.onceToken
+ __os_activity_create
+ __os_activity_current
+ __os_log_error_impl
+ _homeScreenService.Service
+ _homeScreenService.onceToken
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$code
+ _objc_msgSend$date
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$dismissAppLibraryWithCompletion:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$failWithError:
+ _objc_msgSend$futureWithBlock:
+ _objc_msgSend$futureWithResult:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$isConditional
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$launchGameOverlayWithOptions:reply:
+ _objc_msgSend$launchGamesApp
+ _objc_msgSend$openApplicationWithBundleID:
+ _objc_msgSend$presentAppLibraryCategoryPodForCategoryIdentifier:completion:
+ _objc_msgSend$proxy
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$timeIntervalSinceDate:
+ _os_activity_scope_enter
+ _os_activity_scope_leave
CStrings:
+ "%lu"
+ "Dismiss app library fails: %@"
+ "Dismiss app library success."
+ "Dismiss app library: already dismissed"
+ "GameIntent"
+ "Launch Application"
+ "Launch Game Overlay: Handled by game policy (%zu)"
+ "Launch Game Overlay: Not handled (timeout)."
+ "Launch Game Overlay: Not handled."
+ "Launch Games Application"
+ "Open Game Layer"
+ "Present app library fails: %@"
+ "Present app library success."
+ "Present app library: Not on the home screen! Dismissing frontmost application..."
+ "Present app library: already presented"
+ "Show Game Overlay"
+ "Toggle Platform Game Library"
+ "options"
+ "v16@?0@\"NSError\"8"
+ "v16@?0Q8"
```

## GameControllerUI

> `/System/Library/PrivateFrameworks/GameControllerUI.framework/Versions/A/GameControllerUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x101fc
-  __TEXT.__objc_methlist: 0xbc4
-  __TEXT.__const: 0x4b6
-  __TEXT.__cstring: 0x656
-  __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__oslogstring: 0x357
+14.0.21.0.0
+  __TEXT.__text: 0x10d94
+  __TEXT.__objc_methlist: 0xcbc
+  __TEXT.__const: 0x4c6
+  __TEXT.__cstring: 0x666
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__oslogstring: 0x434
   __TEXT.__swift5_typeref: 0x228
   __TEXT.__swift5_capture: 0x54
   __TEXT.__constg_swiftt: 0x2c4

   __TEXT.__swift5_fieldmd: 0x1a8
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x518
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xa78
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x370
-  __AUTH_CONST.__const: 0x6c8
-  __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x2eb0
+  __DATA_CONST.__got: 0x3a0
+  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_const: 0x3458
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH.__objc_data: 0x4d8
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH.__objc_data: 0x528
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x640
-  __DATA.__bss: 0x28
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x700
+  __DATA.__bss: 0x38
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GamePolicy.framework/Versions/A/GamePolicy
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 372
-  Symbols:   1394
-  CStrings:  127
+  Functions: 397
+  Symbols:   1469
+  CStrings:  138
 
Symbols:
+ +[GCGameIntentGamePolicyAction supportsSecureCoding]
+ -[GCGameIntentGamePolicyAction copyWithZone:]
+ -[GCGameIntentGamePolicyAction encodeWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithOptions:]
+ -[GCGameIntentGamePolicyAction init]
+ -[GCGameIntentGamePolicyAction performAction]
+ -[GCGameIntentLaunchAppleGamesAction(GamePolicy) performAction]
+ -[GCGameIntentLaunchApplicationAction(NS) performAction]
+ -[GCGameIntentOpenPlatformGameLibraryAction(NS) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) tryMergeWithOther:]
+ GCC_except_table0
+ GCC_except_table11
+ GCC_except_table12
+ GCC_except_table6
+ OBJC_IVAR_$_GCGameIntentGamePolicyAction._options
+ _OBJC_CLASS_$_GCGameIntentGamePolicyAction
+ _OBJC_CLASS_$_GCGameIntentLaunchAppleGamesAction
+ _OBJC_CLASS_$_GCGameIntentLaunchApplicationAction
+ _OBJC_CLASS_$_GCGameIntentOpenPlatformGameLibraryAction
+ _OBJC_CLASS_$_GCGameIntentShowAppleGameOverlayAction
+ _OBJC_CLASS_$_GPUserExperienceProxy
+ _OBJC_CLASS_$_NSDate
+ _OBJC_METACLASS_$_GCGameIntentGamePolicyAction
+ __45-[GCGameIntentGamePolicyAction performAction]_block_invoke_2
+ __56-[GCGameIntentLaunchApplicationAction(NS) performAction]_block_invoke
+ __67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke_2
+ __OBJC_$_CATEGORY_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_GCGameIntentLaunchApplicationAction_$_NS
+ __OBJC_$_CATEGORY_GCGameIntentOpenPlatformGameLibraryAction_$_NS
+ __OBJC_$_CATEGORY_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentLaunchApplicationAction_$_NS
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentOpenPlatformGameLibraryAction_$_NS
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
+ __OBJC_$_CLASS_METHODS_GCGameIntentGamePolicyAction
+ __OBJC_$_CLASS_PROP_LIST_GCGameIntentGamePolicyAction
+ __OBJC_$_INSTANCE_METHODS_GCGameIntentGamePolicyAction
+ __OBJC_$_INSTANCE_VARIABLES_GCGameIntentGamePolicyAction
+ __OBJC_$_PROP_LIST_GCGameIntentGamePolicyAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCGameIntentAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCGameIntentAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_GCGameIntentAction
+ __OBJC_CLASS_PROTOCOLS_$_GCGameIntentGamePolicyAction
+ __OBJC_CLASS_RO_$_GCGameIntentGamePolicyAction
+ __OBJC_LABEL_PROTOCOL_$_GCGameIntentAction
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_GCGameIntentGamePolicyAction
+ __OBJC_PROTOCOL_$_GCGameIntentAction
+ __OBJC_PROTOCOL_$_NSCopying
+ ___45-[GCGameIntentGamePolicyAction performAction]_block_invoke
+ ___45-[GCGameIntentGamePolicyAction performAction]_block_invoke_2
+ ___56-[GCGameIntentLaunchApplicationAction(NS) performAction]_block_invoke
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke_2
+ ____gc_log_game_intent_block_invoke
+ ___block_descriptor_48_e8_32s40s_e8_v16?0Q8l
+ ___block_descriptor_48_e8_32s_e19_v16?0"GCPromise"8l
+ __gc_log_game_intent
+ __os_activity_create
+ __os_activity_current
+ __os_log_error_impl
+ _gc_log_game_intent
+ _gc_log_game_intent.Log
+ _gc_log_game_intent.onceToken
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$date
+ _objc_msgSend$futureWithBlock:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$isConditional
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$launchGameOverlayWithOptions:reply:
+ _objc_msgSend$launchGamesApp
+ _objc_msgSend$proxy
+ _objc_msgSend$timeIntervalSinceDate:
+ _os_activity_scope_enter
+ _os_activity_scope_leave
- -[GCGameIntentManager(NS) _ui_launchApplicationWithBundleIdentifier:]
- -[GCGameIntentManager(NS) ui_togglePlatformGamesLibrary]
- _OBJC_CLASS_$_GCGameIntentManager
- __OBJC_$_CATEGORY_GCGameIntentManager_$_NS
- __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentManager_$_NS
- ___69-[GCGameIntentManager(NS) _ui_launchApplicationWithBundleIdentifier:]_block_invoke
CStrings:
+ "GameIntent"
+ "Launch Application"
+ "Launch Game Overlay: Handled by game policy (%zu)"
+ "Launch Game Overlay: Not handled (timeout)."
+ "Launch Game Overlay: Not handled."
+ "Launch Games Application"
+ "Open Game Layer"
+ "Open Spotlight"
+ "Show Game Overlay"
+ "options"
+ "v16@?0Q8"
```

## GameControllerUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/GameControllerUI.framework/Versions/A/GameControllerUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
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
-  __TEXT.__text: 0xc650
-  __TEXT.__objc_methlist: 0xc34
-  __TEXT.__const: 0x444
-  __TEXT.__cstring: 0x573
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__oslogstring: 0x342
+14.0.21.0.0
+  __TEXT.__text: 0xcfa8
+  __TEXT.__objc_methlist: 0xd54
+  __TEXT.__const: 0x454
+  __TEXT.__cstring: 0x58f
+  __TEXT.__gcc_except_tab: 0x1a4
+  __TEXT.__oslogstring: 0x3fd
   __TEXT.__swift5_typeref: 0x18e
   __TEXT.__swift5_reflstr: 0xc6
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_fieldmd: 0x90
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x4c8
   __TEXT.__eh_frame: 0xd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x490
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0xa20
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x340
-  __AUTH_CONST.__const: 0x270
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x34b0
+  __DATA_CONST.__got: 0x370
+  __AUTH_CONST.__const: 0x290
+  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__objc_const: 0x39c0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x490
-  __AUTH.__objc_data: 0x368
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH.__objc_data: 0x3b8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x5d0
-  __DATA.__bss: 0x1c0
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x750
+  __DATA.__bss: 0x1d0
   __DATA_DIRTY.__objc_data: 0x2a8
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GamePolicy.framework/Versions/A/GamePolicy
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper
   - /System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 327
-  Symbols:   1281
-  CStrings:  93
+  Functions: 349
+  Symbols:   1362
+  CStrings:  102
 
Symbols:
+ +[GCGameIntentGamePolicyAction supportsSecureCoding]
+ -[GCGameIntentGamePolicyAction copyWithZone:]
+ -[GCGameIntentGamePolicyAction encodeWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithCoder:]
+ -[GCGameIntentGamePolicyAction initWithOptions:]
+ -[GCGameIntentGamePolicyAction init]
+ -[GCGameIntentGamePolicyAction performAction]
+ -[GCGameIntentLaunchAppleGamesAction(GamePolicy) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]
+ -[GCGameIntentShowAppleGameOverlayAction(GamePolicy) tryMergeWithOther:]
+ GCC_except_table10
+ GCC_except_table6
+ GCC_except_table9
+ OBJC_IVAR_$_GCGameIntentGamePolicyAction._options
+ _OBJC_CLASS_$_GCGameIntentGamePolicyAction
+ _OBJC_CLASS_$_GCGameIntentLaunchAppleGamesAction
+ _OBJC_CLASS_$_GCGameIntentShowAppleGameOverlayAction
+ _OBJC_CLASS_$_GPUserExperienceProxy
+ _OBJC_CLASS_$_NSDate
+ _OBJC_METACLASS_$_GCGameIntentGamePolicyAction
+ __45-[GCGameIntentGamePolicyAction performAction]_block_invoke_2
+ __67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke_2
+ __OBJC_$_CATEGORY_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentLaunchAppleGamesAction_$_GamePolicy
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_GCGameIntentShowAppleGameOverlayAction_$_GamePolicy
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
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke
+ ___67-[GCGameIntentShowAppleGameOverlayAction(GamePolicy) performAction]_block_invoke_2
+ ____gc_log_game_intent_block_invoke
+ ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e19_v16?0"GCPromise"8ls32l8
+ __gc_log_game_intent
+ __os_activity_create
+ __os_activity_current
+ __os_log_error_impl
+ _gc_log_game_intent
+ _gc_log_game_intent.Log
+ _gc_log_game_intent.onceToken
+ _objc_msgSend$date
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$encodeInteger:forKey:
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
CStrings:
+ "GameIntent"
+ "Launch Game Overlay: Handled by game policy (%zu)"
+ "Launch Game Overlay: Not handled (timeout)."
+ "Launch Game Overlay: Not handled."
+ "Launch Games Application"
+ "Open Game Layer"
+ "Show Game Overlay"
+ "options"
+ "v16@?0Q8"
```

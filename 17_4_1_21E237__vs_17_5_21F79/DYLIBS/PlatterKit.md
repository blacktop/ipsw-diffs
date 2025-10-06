## PlatterKit

> `/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit`

```diff

-311.109.0.0.0
-  __TEXT.__text: 0x23c00
+311.111.100.0.0
+  __TEXT.__text: 0x23ca0
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x2b30
+  __TEXT.__objc_methlist: 0x2b40
   __TEXT.__const: 0x1c8
   __TEXT.__gcc_except_tab: 0x2e8
   __TEXT.__cstring: 0xbd4
   __TEXT.__oslogstring: 0x512
   __TEXT.__objc_const_ax: 0x34c
   __TEXT.__unwind_info: 0xc74
-  __TEXT.__objc_classname: 0x85d
-  __TEXT.__objc_methname: 0xac55
+  __TEXT.__objc_classname: 0x85e
+  __TEXT.__objc_methname: 0xac73
   __TEXT.__objc_methtype: 0x2327
-  __TEXT.__objc_stubs: 0x7740
+  __TEXT.__objc_stubs: 0x7760
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x810
   __DATA_CONST.__objc_classlist: 0x120

   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xb590
-  __DATA_CONST.__objc_selrefs: 0x2358
+  __DATA_CONST.__objc_selrefs: 0x2368
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_classrefs: 0x330
   __DATA_CONST.__objc_superrefs: 0xf0

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 181D3014-107A-3A93-8B74-758B29D9F993
-  Functions: 1080
-  Symbols:   4392
-  CStrings:  2073
+  UUID: BD49A780-28F7-3D16-BF55-AA9DF40D11A8
+  Functions: 1081
+  Symbols:   4395
+  CStrings:  2075
 
Symbols:
+ -[PLPlatterActionButtonsView actionButtonCount]
+ -[PLSwipeInteraction _actuateFeedbackForDefaultActionLockedIfNecessary]
+ -[PLSwipeInteraction _actuateFeedbackForDefaultActionUnlockedIfNecessary]
+ -[PLSwipeInteraction _panLocation]
+ -[PLSwipeInteraction defaultActionFeedbackGenerator]
+ -[PLSwipeInteraction didPlayHaptic]
+ -[PLSwipeInteraction setDefaultActionFeedbackGenerator:]
+ -[PLSwipeInteraction setDidPlayHaptic:]
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table45
+ _OBJC_IVAR_$_PLSwipeInteraction._defaultActionFeedbackGenerator
+ _OBJC_IVAR_$_PLSwipeInteraction._didPlayHaptic
+ _objc_msgSend$_panLocation
+ _objc_msgSend$actionButtonCount
+ _objc_msgSend$initWithStyle:view:
+ _objc_msgSend$transitionToState:ended:atLocation:
- -[PLPlatterActionButtonsView _actuateFeedbackForDefaultActionLockedIfNecessary]
- -[PLPlatterActionButtonsView _actuateFeedbackForDefaultActionUnlockedIfNecessary]
- -[PLPlatterActionButtonsView _configureDefaultActionFeedbackIfNecessary]
- -[PLPlatterActionButtonsView defaultActionFeedbackGenerator]
- -[PLPlatterActionButtonsView didPlayHaptic]
- -[PLPlatterActionButtonsView setDefaultActionFeedbackGenerator:]
- -[PLPlatterActionButtonsView setDidPlayHaptic:]
- GCC_except_table28
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table42
- _OBJC_IVAR_$_PLPlatterActionButtonsView._defaultActionFeedbackGenerator
- _OBJC_IVAR_$_PLPlatterActionButtonsView._didPlayHaptic
- _objc_msgSend$_configureDefaultActionFeedbackIfNecessary
- _objc_msgSend$defaultActionFeedbackGenerator
- _objc_msgSend$initWithStyle:
CStrings:
+ "\x01\x15!1"
+ "\x116"
+ "_panLocation"
+ "actionButtonCount"
+ "initWithStyle:view:"
+ "transitionToState:ended:atLocation:"
- "\x01\x15!"
- "\x117"
- "_configureDefaultActionFeedbackIfNecessary"
- "initWithStyle:"

```

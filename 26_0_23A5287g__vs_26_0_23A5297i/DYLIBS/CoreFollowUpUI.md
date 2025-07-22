## CoreFollowUpUI

> `/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI`

```diff

-278.0.0.0.0
-  __TEXT.__text: 0xa42c
+280.0.0.0.0
+  __TEXT.__text: 0xa4b8
   __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_methlist: 0x9d4
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__cstring: 0x623
   __TEXT.__oslogstring: 0x953
   __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x2072
-  __TEXT.__objc_methtype: 0x4fb
-  __TEXT.__objc_stubs: 0x2060
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__objc_methname: 0x2094
+  __TEXT.__objc_methtype: 0x50f
+  __TEXT.__objc_stubs: 0x2080
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_selrefs: 0x9e8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x2b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2C45759-CBC7-383B-A351-E586AD562429
+  UUID: E4F95F92-0334-379E-A005-7C8DC3336967
   Functions: 234
-  Symbols:   1239
-  CStrings:  632
+  Symbols:   1241
+  CStrings:  634
 
Symbols:
+ -[FLPreferencesController startPresentingForHandler:withRemoteController:customPresentationStyle:]
+ -[FLPreferencesFollowUpItemListViewController startPresentingForHandler:withRemoteController:customPresentationStyle:]
+ _FLUserInfoPropertyHasCustomModalPresentationStyle
+ ___block_descriptor_48_e8_32s40w_e26_v16?0"UIViewController"8lw40l8s32l8
+ _objc_msgSend$boolValue
+ _objc_msgSend$startPresentingForHandler:withRemoteController:customPresentationStyle:
- -[FLPreferencesController startPresentingForHandler:withRemoteController:]
- -[FLPreferencesFollowUpItemListViewController startPresentingForHandler:withRemoteController:]
- ___block_descriptor_40_e8_32w_e26_v16?0"UIViewController"8lw32l8
- _objc_msgSend$startPresentingForHandler:withRemoteController:
Functions:
~ -[FLPreferencesController startPresentingForHandler:withRemoteController:] -> -[FLPreferencesController startPresentingForHandler:withRemoteController:customPresentationStyle:] : 232 -> 240
~ -[FLSpecifierTapHandler _handleActionForItem:fromSpecifier:eventSource:withCompletionHandler:] : 716 -> 736
~ ___94-[FLSpecifierTapHandler _handleActionForItem:fromSpecifier:eventSource:withCompletionHandler:]_block_invoke : 132 -> 244
CStrings:
+ "boolValue"
+ "startPresentingForHandler:withRemoteController:customPresentationStyle:"
+ "v36@0:8@\"FLSpecifierTapHandler\"16@\"UIViewController\"24B32"
+ "v36@0:8@16@24B32"
- "startPresentingForHandler:withRemoteController:"
- "v32@0:8@\"FLSpecifierTapHandler\"16@\"UIViewController\"24"

```

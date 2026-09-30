## Podcasts

> `/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts`

```diff

-2963.10.30.1.0
-  __TEXT.__text: 0xcd1c
+2994.2.0.0.0
+  __TEXT.__text: 0xcd60
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x1c68
-  __TEXT.__cstring: 0x2ed6
+  __TEXT.__objc_methlist: 0x1dfc
+  __TEXT.__cstring: 0x2e8a
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x210
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x650
-  __TEXT.__objc_classname: 0x15fa
-  __TEXT.__objc_methname: 0x1505
-  __TEXT.__objc_methtype: 0x120
-  __TEXT.__objc_stubs: 0x1340
+  __TEXT.__objc_classname: 0x1616
+  __TEXT.__objc_methname: 0x17d9
+  __TEXT.__objc_methtype: 0x29c
+  __TEXT.__objc_stubs: 0x1360
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x168
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3a40
-  __AUTH_CONST.__objc_const: 0x5308
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x54b0
   __AUTH.__objc_data: 0x3c0
-  __DATA.__data: 0x8
+  __DATA.__data: 0xc8
   __DATA.__common: 0x2
   __DATA.__bss: 0x11
   __DATA_DIRTY.__objc_data: 0x2a30

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F275F3C3-D423-3D2E-B769-AB6AF56E81D8
+  UUID: 2C0B3AF2-39C3-3B58-AA35-8EE70F8EB82D
   Functions: 518
-  Symbols:   2091
-  CStrings:  1334
+  Symbols:   2106
+  CStrings:  1388
 
Symbols:
+ _OBJC_CLASS_$_UIFocusSystem
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_REFS_UIFocusEnvironment
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_UIFocusEnvironment
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_UIFocusEnvironment
+ __OBJC_PROTOCOL_REFERENCE_$_UIFocusEnvironment
+ ___block_literal_global.298
+ ___block_literal_global.304
+ ___block_literal_global.379
+ ___block_literal_global.385
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$focusSystemForEnvironment:
+ _objc_msgSend$focusedItem
- _OBJC_CLASS_$_UIScreen
- ___block_literal_global.295
- ___block_literal_global.301
- ___block_literal_global.376
- ___block_literal_global.382
- _objc_msgSend$focusedView
- _objc_msgSend$mainScreen
Functions:
~ ___46+[AXPodcastGlue accessibilityInitializeBundle]_block_invoke_3 : 1412 -> 1372
~ _accessibilityElementIsUIKitFocused : 108 -> 132
~ +[ShowMetadataViewAccessibility _accessibilityPerformValidations:] : 152 -> 180
~ -[ShowMetadataViewAccessibility accessibilityLabel] : 616 -> 672
CStrings:
+ "@\"<UIFocusEnvironment>\"16@0:8"
+ "@\"<UIFocusItemContainer>\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSString\"16@0:8"
+ "@\"NSString\"24@0:8@\"UIFocusUpdateContext\"16"
+ "@\"UIView\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@\"UIFocusUpdateContext\"16"
+ "NSObject"
+ "T#,R"
+ "T@\"<UIFocusEnvironment>\",R,W,N"
+ "T@\"<UIFocusItemContainer>\",R,N"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",R,C"
+ "T@\"UIView\",?,R,W,N"
+ "TQ,R"
+ "UIFocusEnvironment"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "didUpdateFocusInContext:withAnimationCoordinator:"
+ "focusGroupIdentifier"
+ "focusItemContainer"
+ "focusSystemForEnvironment:"
+ "focusedItem"
+ "hash"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "parentFocusEnvironment"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "preferredFocusEnvironments"
+ "preferredFocusedView"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setNeedsFocusUpdate"
+ "shouldUpdateFocusInContext:"
+ "soundIdentifierForFocusUpdateInContext:"
+ "superclass"
+ "updateFocusIfNeeded"
+ "v32@0:8@\"UIFocusUpdateContext\"16@\"UIFocusAnimationCoordinator\"24"
+ "v32@0:8@16@24"
+ "zone"
- "focusedView"
- "mainScreen"

```

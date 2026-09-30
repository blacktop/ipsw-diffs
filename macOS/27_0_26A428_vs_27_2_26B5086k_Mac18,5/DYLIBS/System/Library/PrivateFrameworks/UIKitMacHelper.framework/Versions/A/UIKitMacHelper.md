## UIKitMacHelper

> `/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper`

```diff

-9127.0.84.1.406
-  __TEXT.__text: 0xb48c4
-  __TEXT.__objc_methlist: 0xe5e0
+9127.1.6.1.402
+  __TEXT.__text: 0xb4be8
+  __TEXT.__objc_methlist: 0xe5e8
   __TEXT.__const: 0x7e8
   __TEXT.__dlopen_cstrs: 0x6a6
-  __TEXT.__cstring: 0xd4d1
+  __TEXT.__cstring: 0xd56a
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x5ada
-  __TEXT.__gcc_except_tab: 0x16dc
+  __TEXT.__oslogstring: 0x5ab2
+  __TEXT.__gcc_except_tab: 0x1724
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x3ba8
+  __TEXT.__unwind_info: 0x3bc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x158
   __DATA_CONST.__got: 0xc40
-  __AUTH_CONST.__const: 0x2ea0
-  __AUTH_CONST.__cfstring: 0x8ac0
-  __AUTH_CONST.__objc_const: 0x17770
+  __AUTH_CONST.__const: 0x2e80
+  __AUTH_CONST.__cfstring: 0x8b20
+  __AUTH_CONST.__objc_const: 0x17778
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0xba4
+  __DATA.__objc_ivar: 0xb9c
   __DATA.__data: 0x20e8
   __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_ivar: 0x4b0
+  __DATA_DIRTY.__objc_ivar: 0x4b8
   __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x8e8
+  __DATA_DIRTY.__bss: 0x8f8
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4645
+  Functions: 4646
   Symbols:   11740
-  CStrings:  1955
+  CStrings:  1960
 
Symbols:
+ -[UINSDragTrackingGestureRecognizer acceptsFirstTouch:event:]
+ -[UINSMouseEventTranslator cancelDirectTouchesWithEvent:]
+ -[UINSTouchGestureRecognizer lastTouchEvent]
+ -[UINSTouchGestureRecognizer reset]
+ GCC_except_table104
+ GCC_except_table32
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table87
+ _UINSSceneRoleIsMenuBarHostedPresentation
+ __OBJC_$_PROP_LIST_UINSTouchGestureRecognizer
+ ___UINSSceneRoleIsMenuBarHostedPresentation_block_invoke
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSEvent"8l
+ ___get_UIWindowFirstResponderUserInfoKeySymbolLoc_block_invoke
+ _objc_msgSend$cancelDirectTouchesWithEvent:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$lastTouchEvent
- -[UINSEventTranslator directTouchesWithEvent:]
- -[UINSWindowStateController _isPodcasts]
- -[UINSWindowStateController sceneIDWeHidInsteadOfClosing]
- -[UINSWindowStateController setSceneIDWeHidInsteadOfClosing:]
- GCC_except_table28
- GCC_except_table65
- GCC_except_table76
- GCC_except_table89
- OBJC_IVAR_$_UINSTouchGestureRecognizer._outstandingEvents
- OBJC_IVAR_$_UINSWindowStateController._sceneIDWeHidInsteadOfClosing
- ___40-[UINSWindowStateController _isPodcasts]_block_invoke
- ___47-[UINSWindow _wantsFullScreenCleanupOnOrderOut]_block_invoke
- ___block_descriptor_40_e8_32s_e17_v16?0"NSEvent"8l
- _objc_msgSend$_isPodcasts
- _objc_msgSend$_unhideWindowForScene:
- _objc_msgSend$sceneIDWeHidInsteadOfClosing
- _objc_msgSend$setSceneIDWeHidInsteadOfClosing:
CStrings:
+ "+"
+ "BOOL UINSSceneRoleIsMenuBarHostedPresentation(UIScene *__strong _Nonnull)"
+ "NSString *get_UIWindowFirstResponderUserInfoKey(void)"
+ "_UIWindowFirstResponderUserInfoKey"
+ "bannerFloating"
+ "integratedCompactLeading"
+ "integratedCompactTrailing"
+ "integratedExpanded"
+ "integratedMinimal"
- "%s: We have a previous hidden window!"
- "-[UINSWindowStateController _closeOrHideWindowWithScene:]"
- "Hiding last window, without termination"
- "com.apple.podcasts"
```

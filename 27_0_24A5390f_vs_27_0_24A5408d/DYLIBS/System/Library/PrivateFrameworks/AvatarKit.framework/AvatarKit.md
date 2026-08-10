## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-366.0.0.0.0
-  __TEXT.__text: 0x77a28
-  __TEXT.__objc_methlist: 0x54bc
+367.0.0.0.0
+  __TEXT.__text: 0x77bb0
+  __TEXT.__objc_methlist: 0x54b4
   __TEXT.__const: 0xa4c
-  __TEXT.__cstring: 0x1df4b
+  __TEXT.__cstring: 0x1df64
   __TEXT.__oslogstring: 0x2ec0
   __TEXT.__ustring: 0x66
-  __TEXT.__gcc_except_tab: 0xddc
-  __TEXT.__unwind_info: 0x1bd0
+  __TEXT.__gcc_except_tab: 0xde4
+  __TEXT.__unwind_info: 0x1be0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27f0
+  __DATA_CONST.__const: 0x2818
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d70
+  __DATA_CONST.__objc_selrefs: 0x3d78
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x625a8
   __DATA_CONST.__got: 0x9e8
   __AUTH_CONST.__const: 0xa40
   __AUTH_CONST.__cfstring: 0x249a0
-  __AUTH_CONST.__objc_const: 0xdd38
+  __AUTH_CONST.__objc_const: 0xdd58
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x7bd8

   __AUTH_CONST.__objc_dictobj: 0x4ede0
   __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x1888
-  __DATA.__objc_ivar: 0xa50
+  __DATA.__objc_ivar: 0xa54
   __DATA.__data: 0x788
   __DATA.__bss: 0xab8
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2530
-  Symbols:   6290
-  CStrings:  5159
+  Symbols:   6294
+  CStrings:  5160
 
Symbols:
+ -[AVTView _windowDidRotateNotification:]
+ _OBJC_IVAR_$_AVTView._windowDidRotateObserver
+ _UIWindowDidRotateNotification
+ ___26-[AVTView didMoveToWindow]_block_invoke
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ _objc_msgSend$_windowDidRotateNotification:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$repeatCount
- -[AVTView _UIOrientationDidChangeNotification:]
- -[AVTView setupOrientation]
- _UIApplicationDidChangeStatusBarOrientationNotification
- _objc_msgSend$setupOrientation
Functions:
~ ___73-[AVTAvatarPoseAnimation _initWithSceneKitScene:usdaMetadata:identifier:]_block_invoke : 360 -> 364
~ __AVTAvatarPoseImportSceneKitAnimation : 2084 -> 2168
~ -[AVTView dealloc] : 148 -> 172
~ -[AVTView didMoveToWindow] : 76 -> 360
~ -[AVTView setupOrientation] -> ___26-[AVTView didMoveToWindow]_block_invoke : 116 -> 92
~ -[AVTView updateInterfaceOrientation] -> -[AVTView _windowDidRotateNotification:] : 156 -> 4
~ -[AVTView _UIOrientationDidChangeNotification:] -> -[AVTView updateInterfaceOrientation] : 4 -> 156
~ -[AVTView .cxx_destruct] : 336 -> 356
CStrings:
+ "v16@?0@\"NSNotification\"8"
```

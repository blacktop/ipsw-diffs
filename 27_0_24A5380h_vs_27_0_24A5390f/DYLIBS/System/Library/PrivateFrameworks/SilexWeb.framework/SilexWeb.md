## SilexWeb

> `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-5923.0.0.0.0
-  __TEXT.__text: 0x189cc
-  __TEXT.__objc_methlist: 0x358c
+5926.0.0.0.0
+  __TEXT.__text: 0x18e04
+  __TEXT.__objc_methlist: 0x35cc
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1e2d
+  __TEXT.__cstring: 0x1e30
   __TEXT.__gcc_except_tab: 0x164
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x890
+  __TEXT.__unwind_info: 0x898
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x16c0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x278
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x9e10
+  __AUTH_CONST.__objc_const: 0x9e40
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x480
+  __DATA.__objc_ivar: 0x484
   __DATA.__data: 0x1748
   __DATA_DIRTY.__objc_data: 0x1950
   __DATA_DIRTY.__bss: 0x78

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 933
-  Symbols:   3117
+  Functions: 938
+  Symbols:   3133
   CStrings:  275
 
Symbols:
+ -[SWContainerViewController currentScreen]
+ -[SWContainerViewController handleScreenDidDisconnect:]
+ -[SWContainerViewController invalidateKeyboardFrameIfScreenChanged]
+ -[SWContainerViewController keyboardScreen]
+ -[SWContainerViewController setKeyboardScreen:]
+ _OBJC_CLASS_$_UIScreen
+ _OBJC_IVAR_$_SWContainerViewController._keyboardScreen
+ _UIScreenDidDisconnectNotification
+ _objc_msgSend$currentScreen
+ _objc_msgSend$invalidateKeyboardFrameIfScreenChanged
+ _objc_msgSend$keyboardScreen
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$screen
+ _objc_msgSend$setKeyboardScreen:
+ _objc_msgSend$window
+ _objc_msgSend$windowScene
```

## SystemApertureUI

> `/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-99.0.0.0.0
-  __TEXT.__text: 0x15174
-  __TEXT.__objc_methlist: 0x244c
+101.0.0.0.0
+  __TEXT.__text: 0x152b4
+  __TEXT.__objc_methlist: 0x249c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xcad
-  __TEXT.__oslogstring: 0xaa4
+  __TEXT.__cstring: 0xc7d
+  __TEXT.__oslogstring: 0xa75
   __TEXT.__gcc_except_tab: 0xad0
   __TEXT.__unwind_info: 0x908
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b8
+  __DATA_CONST.__objc_selrefs: 0x10d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xa80
-  __AUTH_CONST.__objc_const: 0x6648
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x66c0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0xf00
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x28

   - /System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 603
-  Symbols:   1680
-  CStrings:  142
+  Functions: 607
+  Symbols:   1691
+  CStrings:  138
 
Symbols:
+ -[SAUIElementViewController _refreshMatchMoveAnimation]
+ -[SAUIElementViewController prefersContentViewMatchMove]
+ -[SAUIElementViewController setPrefersContentViewMatchMove:]
+ -[SAUILayoutSpecifyingElementViewController prefersContentViewMatchMove]
+ -[SAUILayoutSpecifyingElementViewController setPrefersContentViewMatchMove:]
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table32
+ GCC_except_table6
+ _OBJC_IVAR_$_SAUIElementViewController._prefersContentViewMatchMove
+ _OBJC_IVAR_$_SAUILayoutSpecifyingElementViewController._prefersContentViewMatchMove
+ __OBJC_$_PROP_LIST_SAUIContentTransitioning
+ _objc_msgSend$_refreshMatchMoveAnimation
+ _objc_msgSend$animationForKey:
+ _objc_msgSend$removeAnimationForKey:
- GCC_except_table102
- GCC_except_table105
- GCC_except_table30
- _objc_msgSend$valueForKey:
CStrings:
+ "\xd1!"
- "View will transition with settings: %{public}@"
- "__animator"
- "__mainContext"
- "_fluidBehaviorSettings"
- "\xc1!"
```

## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4636.102.1.0.0
-  __TEXT.__text: 0xa2c10
-  __TEXT.__objc_methlist: 0xe8b4
+4636.110.0.0.0
+  __TEXT.__text: 0xa2ef8
+  __TEXT.__objc_methlist: 0xe8cc
   __TEXT.__const: 0xac8
   __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__cstring: 0xabf9
+  __TEXT.__cstring: 0xabfa
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x4802
-  __TEXT.__unwind_info: 0x32d8
+  __TEXT.__unwind_info: 0x32e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7cc8
+  __DATA_CONST.__objc_selrefs: 0x7ce8
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__got: 0x10c8
   __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0xa240
-  __AUTH_CONST.__objc_const: 0x2daa0
+  __AUTH_CONST.__objc_const: 0x2dac0
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x168

   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50f0
-  __DATA.__objc_ivar: 0xd3c
+  __DATA.__objc_ivar: 0xd40
   __DATA.__data: 0x3810
   __DATA.__bss: 0x3e8
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4807
-  Symbols:   12400
+  Functions: 4809
+  Symbols:   12405
   CStrings:  1822
 
Symbols:
+ -[SBUIPasscodeLockViewWithKeyboard _correctContainerBottomConstraintIfNeeded]
+ -[SBUIPasscodeLockViewWithKeyboard initWithLightStyle:pinKeyboardToBottom:]
+ _OBJC_IVAR_$_SBUIPasscodeLockViewWithKeyboard._pinKeyboardToBottom
+ _objc_msgSend$_correctContainerBottomConstraintIfNeeded
+ _objc_msgSend$firstAttribute
+ _objc_msgSend$initWithLightStyle:pinKeyboardToBottom:
+ _objc_msgSend$secondAttribute
- GCC_except_table13
- GCC_except_table17
Functions:
~ +[SBUIPasscodeLockViewFactory _passcodeLockViewForStyle:withLightStyle:dimmed:] : 220 -> 280
~ -[SBUIPasscodeLockViewWithKeyboard initWithLightStyle:] : 1224 -> 8
+ -[SBUIPasscodeLockViewWithKeyboard initWithLightStyle:pinKeyboardToBottom:]
~ -[SBUIPasscodeLockViewWithKeyboard layoutSubviews] : 100 -> 136
+ -[SBUIPasscodeLockViewWithKeyboard _correctContainerBottomConstraintIfNeeded]
```

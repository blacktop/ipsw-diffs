## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-7303.0.102.0.0
+7439.1.106.0.0
   __TEXT.__text: 0x160e4
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0xb98
+  __TEXT.__objc_methlist: 0xba0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xca8
+  __TEXT.__cstring: 0xcbc
   __TEXT.__gcc_except_tab: 0x558
-  __TEXT.__oslogstring: 0x1285
+  __TEXT.__oslogstring: 0x1280
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x52c
+  __TEXT.__unwind_info: 0x534
   __TEXT.__objc_classname: 0x293
-  __TEXT.__objc_methname: 0x32bb
-  __TEXT.__objc_methtype: 0xb21
-  __TEXT.__objc_stubs: 0x2bc0
+  __TEXT.__objc_methname: 0x32df
+  __TEXT.__objc_methtype: 0xb32
+  __TEXT.__objc_stubs: 0x2be0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d40
-  __DATA_CONST.__objc_selrefs: 0xc68
+  __DATA_CONST.__objc_const: 0x1d20
+  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x558

   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x308
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x150
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 328
-  Symbols:   1518
-  CStrings:  905
+  Functions: 329
+  Symbols:   1520
+  CStrings:  907
 
Symbols:
+ -[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table46
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table94
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_2
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_3
+ ___65-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke_4
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.521
+ ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.526
+ ___block_literal_global.304
+ ___block_literal_global.489
+ ___block_literal_global.705
+ _objc_msgSend$updateKeyboardStatus:fromHandler:fromFocus:
- GCC_except_table110
- GCC_except_table115
- GCC_except_table145
- GCC_except_table149
- GCC_except_table151
- GCC_except_table45
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table70
- GCC_except_table93
- _OBJC_IVAR_$__UIKeyboardArbiter._newlyConnectedActiveHandle
- ___55-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]_block_invoke
- ___55-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]_block_invoke_2
- ___55-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]_block_invoke_3
- ___55-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]_block_invoke_4
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.519
- ___72-[_UIKeyboardArbiterClientHandle takeProcessAssertionOnRemoteWithQueue:]_block_invoke.524
- ___block_literal_global.303
- ___block_literal_global.487
- ___block_literal_global.703
CStrings:
+ "\x0311#\x11\x11\x13\x11!"
+ "-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]"
+ "-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:fromFocus:]_block_invoke"
+ "2bqR\x11"
+ "T@\"NSString\",?,R,C"
+ "[%@] Skip keyboard down change info from %@, due to the keyboard is on screen for handle %@"
+ "updateKeyboardStatus:fromHandler:fromFocus:"
+ "v36@0:8@16@24B32"
- "\x03A1#\x11\x11\x13\x11!"
- "-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]"
- "-[_UIKeyboardArbiter updateKeyboardStatus:fromHandler:]_block_invoke"
- "3bqR\x11"
- "[%@] Skip keyboard down change info from %@, due to newly connected keyboard on screen handle %@"
- "_newlyConnectedActiveHandle"

```

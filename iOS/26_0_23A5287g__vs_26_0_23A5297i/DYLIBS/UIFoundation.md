## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-1009.0.0.0.0
-  __TEXT.__text: 0x1053d8
+1011.0.0.0.0
+  __TEXT.__text: 0x105634
   __TEXT.__auth_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xbab4
+  __TEXT.__objc_methlist: 0xbabc
   __TEXT.__const: 0x73c
-  __TEXT.__cstring: 0xff0d
-  __TEXT.__gcc_except_tab: 0x3414
+  __TEXT.__cstring: 0xff26
+  __TEXT.__gcc_except_tab: 0x33f8
   __TEXT.__ustring: 0x2b4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x3d28
+  __TEXT.__unwind_info: 0x3d30
   __TEXT.__objc_classname: 0x1294
   __TEXT.__objc_methname: 0x1fef2
   __TEXT.__objc_methtype: 0x8734
   __TEXT.__objc_stubs: 0x14b60
   __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x9010
+  __DATA_CONST.__const: 0x9060
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x12f0
   __AUTH_CONST.__const: 0x1268
-  __AUTH_CONST.__cfstring: 0xc8e0
+  __AUTH_CONST.__cfstring: 0xc8c0
   __AUTH_CONST.__objc_const: 0x12818
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B56C2A5-CFD0-349A-B0A2-39D9E94FE1B1
-  Functions: 5252
-  Symbols:   17904
-  CStrings:  10606
+  UUID: D8729138-6EB4-39EC-BD1B-00D194CCE20A
+  Functions: 5255
+  Symbols:   17912
+  CStrings:  10605
 
Symbols:
+ -[NSTextLayoutFragment resolvedBaseWritingDirection]
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table152
+ GCC_except_table42
+ GCC_except_table59
+ ___31-[NSTextLayoutFragment _layout]_block_invoke_7
+ ___44-[NSTextRange initWithLocation:endLocation:]_block_invoke_2
+ ___block_descriptor_107_e8_32r40r48r56r64r72r80w_e31_v24?0"NSTextLineFragment"8Q16lr32l8r40l8r48l8r56l8r64l8w80l8r72l8
+ ___block_descriptor_48_e8_32o40o_e18_"NSString"16?08ls32l8s40l8
+ ___block_descriptor_80_e8_32o40o48r56r64r72r_e51_v24?0"NSTextLayoutFragment"8"NSParagraphStyle"16lr48l8s32l8s40l8r56l8r64l8r72l8
+ ___block_literal_global.159
+ ___block_literal_global.77
- GCC_except_table142
- GCC_except_table143
- GCC_except_table57
- GCC_except_table92
- ___block_descriptor_99_e8_32r40r48r56w_e31_v24?0"NSTextLineFragment"8Q16lr32l8r40l8w56l8r48l8
- ___block_literal_global.161
Functions:
~ ___NSStringDrawingEngine : 4296 -> 4428
~ ___31-[NSTextLayoutFragment _layout]_block_invoke_5 : 344 -> 152
~ -[NSTextLayoutFragment _layout] : 5596 -> 5584
~ ___31-[NSTextLayoutFragment _layout]_block_invoke_6 : 132 -> 376
~ ___31-[NSTextLayoutFragment _layout]_block_invoke : 1008 -> 324
~ -[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges] : 1416 -> 1440
+ -[NSTextLayoutFragment resolvedBaseWritingDirection]
~ ___31-[NSTextLayoutFragment _layout]_block_invoke_2 : 656 -> 1008
~ ___31-[NSTextLayoutFragment _layout]_block_invoke_3 : 188 -> 656
~ ___31-[NSTextLayoutFragment _layout]_block_invoke_4 : 152 -> 188
+ ___31-[NSTextLayoutFragment _layout]_block_invoke_7
~ -[NSTextLayoutManager _invalidateLayoutForTextRange:hard:] : 2452 -> 2496
~ -[NSTextLayoutManager enumerateTemporaryAttributesFromLocation:reverse:usingBlock:] : 480 -> 504
~ -[NSTextRange initWithLocation:endLocation:] : 488 -> 460
+ ___44-[NSTextRange initWithLocation:endLocation:]_block_invoke_2
CStrings:
+ "Invalid initilizer arguments: location-%@ endLocation=%@"
+ "v24@?0@\"NSTextLayoutFragment\"8@\"NSParagraphStyle\"16"
- "attempt to create %@ from nil location"
- "attempt to create backwards %@ from %@ to %@"

```

## BaseBoard

> `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`

```diff

-731.0.0.0.0
-  __TEXT.__text: 0xa2564
+732.0.0.0.0
+  __TEXT.__text: 0xa2958
   __TEXT.__auth_stubs: 0x2100
-  __TEXT.__objc_methlist: 0x6e5c
+  __TEXT.__objc_methlist: 0x6e64
   __TEXT.__const: 0x308
   __TEXT.__dlopen_cstrs: 0xe8
-  __TEXT.__gcc_except_tab: 0x118a0
-  __TEXT.__cstring: 0x8d09
+  __TEXT.__gcc_except_tab: 0x11918
+  __TEXT.__cstring: 0x8ea9
   __TEXT.__oslogstring: 0x3053
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x5028
+  __TEXT.__unwind_info: 0x5030
   __TEXT.__objc_classname: 0xffd
-  __TEXT.__objc_methname: 0xb618
+  __TEXT.__objc_methname: 0xb667
   __TEXT.__objc_methtype: 0x22a5
   __TEXT.__objc_stubs: 0x72c0
   __DATA_CONST.__got: 0x848

   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_selrefs: 0x3188
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1090
   __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x8bc0
-  __AUTH_CONST.__objc_const: 0xd140
+  __AUTH_CONST.__cfstring: 0x8ca0
+  __AUTH_CONST.__objc_const: 0xd170
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x810
+  __DATA.__objc_ivar: 0x814
   __DATA.__data: 0x1108
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x40

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7974D33C-78DF-38F8-BD30-D3956F03BD5A
-  Functions: 2981
-  Symbols:   10779
-  CStrings:  5533
+  UUID: D8AC4E07-5127-3C6D-8E0C-506F2EA5819B
+  Functions: 2982
+  Symbols:   10782
+  CStrings:  5550
 
Symbols:
+ +[BSObjCMethod methodWithSelector:typeEncoding:outParsingError:]
+ +[BSObjCProtocol _gatherMethodMetadataForRequired:onProtocol:toMethods:andErrors:]
+ -[BSObjCProtocol _initWithName:protocol:parsingErrors:inherited:methods:properties:virtual:]
+ -[BSObjCProtocol parsingErrors]
+ GCC_except_table128
+ GCC_except_table134
+ GCC_except_table141
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table183
+ _OBJC_IVAR_$_BSObjCProtocol._parsingErrors
+ ___block_literal_global.580
+ ___block_literal_global.692
+ ___block_literal_global.818
+ ___block_literal_global.823
- +[BSObjCMethod methodWithSelector:typeEncoding:]
- +[BSObjCProtocol _gatherMethodMetadataForProtocol:required:]
- -[BSObjCProtocol _initWithName:protocol:inherited:methods:properties:virtual:]
- GCC_except_table109
- GCC_except_table133
- GCC_except_table136
- GCC_except_table148
- GCC_except_table165
- GCC_except_table167
- GCC_except_table170
- GCC_except_table182
- ___block_literal_global.565
- ___block_literal_global.670
- ___block_literal_global.796
- ___block_literal_global.801
CStrings:
+ "T@\"NSArray\",R,C,N,V_parsingErrors"
+ "[method selector] == [newMethod selector]"
+ "_parsingErrors"
+ "dropping distinguishable method due to selector collision : method=%@ existing=%@"
+ "exception creating NSMethodSignature for @selector(%@): %@"
+ "exception while building method %@ with encoding '%s': %@"
+ "ignoring @selector(%@) because it contains a union"
+ "ignoring @selector(%@) because the argument count does not match the encoding"
+ "ignoring @selector(%@) because the first two arguments are not 'self' and '_cmd'"
+ "methodWithSelector:typeEncoding:outParsingError:"
+ "parsingErrors"
+ "signature"
- "[newMethod selector] == [newMethod selector]"
- "methodWithSelector:typeEncoding:"

```

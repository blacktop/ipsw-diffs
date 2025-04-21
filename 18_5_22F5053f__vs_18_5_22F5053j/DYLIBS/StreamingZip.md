## StreamingZip

> `/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`

```diff

-226.0.0.0.0
-  __TEXT.__text: 0x21854
+226.120.1.0.0
+  __TEXT.__text: 0x21be4
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0xe4c
+  __TEXT.__objc_methlist: 0xe64
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__cstring: 0x3a75
-  __TEXT.__oslogstring: 0x5aba
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__cstring: 0x3acf
+  __TEXT.__oslogstring: 0x5af4
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x2f20
-  __TEXT.__objc_methtype: 0xd25
-  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methname: 0x2f76
+  __TEXT.__objc_methtype: 0xd46
+  __TEXT.__objc_stubs: 0x2320
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__const: 0xc28
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xa78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1d60
-  __AUTH_CONST.__objc_const: 0x19b0
-  __DATA.__objc_ivar: 0x160
+  __AUTH_CONST.__cfstring: 0x1da0
+  __AUTH_CONST.__objc_const: 0x19d0
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 355
-  Symbols:   1626
-  CStrings:  1505
+  Functions: 358
+  Symbols:   1637
+  CStrings:  1514
 
Symbols:
+ -[SZExtractor _setUpWithPath:options:error:]
+ -[SZExtractor initWithOptions:error:]
+ -[SZExtractor initWithPath:options:error:]
+ GCC_except_table355
+ _OBJC_IVAR_$_StreamingUnzipper._passthroughEnabled
+ _SZExtractorOptionsNoPassthrough
+ _SZThrowForSetupError
+ __OBJC_$_PROP_LIST_SZExtractor.460
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.184
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.191
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.197
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.200
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.225
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.226
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.230
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2.193
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.122
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.137
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.142
+ ___Block_byref_object_copy_.461
+ ___Block_byref_object_dispose_.462
+ ___block_descriptor_32_e5_v8?0l.956
+ ___block_literal_global.937
+ _objc_msgSend$_setUpWithPath:options:error:
+ _objc_msgSend$initWithOptions:error:
+ _objc_msgSend$initWithPath:options:error:
+ _objc_msgSend$userInfo
- -[SZExtractor _setUpWithPath:options:]
- GCC_except_table352
- __OBJC_$_PROP_LIST_SZExtractor.454
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.182
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.189
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.195
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.196
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.223
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.224
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.228
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2.191
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.119
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.135
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.140
- ___Block_byref_object_copy_.457
- ___Block_byref_object_dispose_.458
- ___block_descriptor_32_e5_v8?0l.951
- ___block_literal_global.930
- _objc_msgSend$_setUpWithPath:options:
CStrings:
+ "@32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "Byte stream does not represent a valid streamable archive"
+ "SZExtractorOptionsNoPassthrough"
+ "_passthroughEnabled"
+ "_setUpWithPath:options:error:"
+ "initWithOptions:error:"
+ "initWithPath:options:error:"
+ "userInfo"
- "_setUpWithPath:options:"

```

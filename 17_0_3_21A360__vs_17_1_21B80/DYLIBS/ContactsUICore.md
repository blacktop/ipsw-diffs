## ContactsUICore

> `/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore`

```diff

-3496.2.0.0.0
-  __TEXT.__text: 0x5c4f4
+3501.0.0.0.0
+  __TEXT.__text: 0x5c634
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x5a88
+  __TEXT.__objc_methlist: 0x5ab8
   __TEXT.__const: 0x210
-  __TEXT.__oslogstring: 0x278b
+  __TEXT.__oslogstring: 0x27d0
   __TEXT.__cstring: 0x3338
   __TEXT.__gcc_except_tab: 0x594
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__unwind_info: 0x1af8
-  __TEXT.__objc_classname: 0x196d
-  __TEXT.__objc_methname: 0x10fe5
-  __TEXT.__objc_methtype: 0x2c0f
-  __TEXT.__objc_stubs: 0xc160
+  __TEXT.__unwind_info: 0x1afc
+  __TEXT.__objc_classname: 0x196f
+  __TEXT.__objc_methname: 0x11063
+  __TEXT.__objc_methtype: 0x2c40
+  __TEXT.__objc_stubs: 0xc1a0
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x2570
+  __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xac68
-  __DATA_CONST.__objc_selrefs: 0x3868
+  __DATA_CONST.__objc_const: 0xad18
+  __DATA_CONST.__objc_selrefs: 0x3878
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__const: 0x18a0
   __AUTH_CONST.__cfstring: 0x2400

   __AUTH.__objc_data: 0x1860
   __AUTH.__data: 0x90
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x7e0
+  __DATA.__objc_classrefs: 0x7e8
   __DATA.__objc_superrefs: 0x350
-  __DATA.__objc_ivar: 0x538
+  __DATA.__objc_ivar: 0x540
   __DATA.__data: 0x1640
   __DATA.__bss: 0x3f0
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B40B04CD-2024-33D6-A59C-DB9720C28281
-  Functions: 2720
-  Symbols:   9985
-  CStrings:  3960
+  UUID: 63D92C29-07E2-31BD-AC3D-009964B6CBEF
+  Functions: 2726
+  Symbols:   10003
+  CStrings:  3967
 
Symbols:
+ +[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:refetchContact:]
+ -[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:bitmapFormat:reply:]
+ -[CNUIPRLikenessLookup setSkipContactLookup:]
+ -[CNUIPRLikenessLookup skipContactLookup]
+ -[CNUIPRLikenessResolver setSkipContactLookup:]
+ -[CNUIPRLikenessResolver skipContactLookup]
+ _OBJC_CLASS_$_CNImageUtilsBitmapFormat
+ _OBJC_IVAR_$_CNUIPRLikenessLookup._skipContactLookup
+ _OBJC_IVAR_$_CNUIPRLikenessResolver._skipContactLookup
+ __OBJC_$_PROP_LIST_CNUIPRLikenessResolver.153
+ ___76+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:refetchContact:]_block_invoke
+ ___76+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:refetchContact:]_block_invoke.46
+ ___76+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:refetchContact:]_block_invoke.46.cold.1
+ ___76+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:refetchContact:]_block_invoke.cold.1
+ ___91-[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:bitmapFormat:reply:]_block_invoke
+ ___91-[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:bitmapFormat:reply:]_block_invoke_2
+ ___block_descriptor_57_e8_32s40s_e9_16?0^8ls32l8s40l8
+ ___block_literal_global.186
+ _objc_msgSend$contactFuture:contactStore:scheduler:refetchContact:
+ _objc_msgSend$getBackgroundColorOnImageData:bitmapFormat:withReply:
+ _objc_msgSend$setSkipContactLookup:
+ _objc_msgSend$skipContactLookup
- +[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:]
- -[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:reply:]
- __OBJC_$_PROP_LIST_CNUIPRLikenessResolver.145
- ___61+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:]_block_invoke
- ___61+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:]_block_invoke.46
- ___61+[CNUIPRLikenessLookup contactFuture:contactStore:scheduler:]_block_invoke.46.cold.1
- ___78-[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:reply:]_block_invoke
- ___78-[CNUIImageRemoteBackgroundColorAnalyzer getBackgroundColorOnImageData:reply:]_block_invoke_2
- ___block_literal_global.177
- _objc_msgSend$contactFuture:contactStore:scheduler:
- _objc_msgSend$getBackgroundColorOnImageData:withReply:
CStrings:
+ "$"
+ "@44@0:8@16@24@32B40"
+ "TB,N,V_skipContactLookup"
+ "[LikenessResolver] Contact lookup disabled, skipping contact refetch"
+ "_skipContactLookup"
+ "contactFuture:contactStore:scheduler:refetchContact:"
+ "getBackgroundColorOnImageData:bitmapFormat:reply:"
+ "getBackgroundColorOnImageData:bitmapFormat:withReply:"
+ "setSkipContactLookup:"
+ "skipContactLookup"
+ "v40@0:8@\"NSData\"16@\"CNImageUtilsBitmapFormat\"24@?<v@?@\"NSArray\">32"
- "contactFuture:contactStore:scheduler:"
- "getBackgroundColorOnImageData:reply:"
- "getBackgroundColorOnImageData:withReply:"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSArray\">24"

```

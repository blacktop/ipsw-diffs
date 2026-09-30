## ACCNowPlayingFeature

> `/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCNowPlayingFeature.xpc/ACCNowPlayingFeature`

```diff

   __TEXT.__text: 0x12a28
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x1000
+  __TEXT.__objc_methlist: 0x1010
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__objc_methname: 0x2b3f
+  __TEXT.__objc_methname: 0x2b5b
   __TEXT.__oslogstring: 0x2ba2
-  __TEXT.__cstring: 0x120b
+  __TEXT.__cstring: 0x1213
   __TEXT.__objc_classname: 0x1b0
   __TEXT.__objc_methtype: 0x5f6
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x440
   __DATA_CONST.__const: 0x980
-  __DATA_CONST.__cfstring: 0xc60
+  __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x268
   __DATA.__objc_const: 0x22a0
-  __DATA.__objc_selrefs: 0xab0
+  __DATA.__objc_selrefs: 0xab8
   __DATA.__objc_ivar: 0x13c
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x2c8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 434
-  Symbols:   3549
-  CStrings:  1003
+  Functions: 435
+  Symbols:   3554
+  CStrings:  1006
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[ACCNowPlayingFeature setMockXPCListenerEndpoint:]
+ GCC_except_table76
+ GCC_except_table81
- GCC_except_table75
- GCC_except_table80
Functions:
+ -[ACCNowPlayingFeature setMockXPCListenerEndpoint:]
~ -[ACCNowPlayingFeature _nowPlayingArtworkDidChange] : 656 -> 636
~ -[ACCStatInfoAccumulator init] : 96 -> 104
CStrings:
+ "Unnamed"
+ "setMockXPCListenerEndpoint:"

```

## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`

```diff

-3605.4.1.0.0
-  __TEXT.__text: 0x2ad0c
-  __TEXT.__objc_methlist: 0x3448
+3610.1.1.0.0
+  __TEXT.__text: 0x2afa4
+  __TEXT.__objc_methlist: 0x3460
   __TEXT.__const: 0x68982
-  __TEXT.__cstring: 0x885b
-  __TEXT.__oslogstring: 0xd80
+  __TEXT.__cstring: 0x886a
+  __TEXT.__oslogstring: 0xdbd
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0x14

   __TEXT.__swift5_typeref: 0x1c
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__unwind_info: 0xe90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e8
+  __DATA_CONST.__objc_selrefs: 0x2500
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__got: 0x508
   __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x1720
-  __AUTH_CONST.__objc_const: 0x9650
+  __AUTH_CONST.__objc_const: 0x9690
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x648
   __AUTH.__objc_data: 0xec8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x74c
+  __DATA.__objc_ivar: 0x754
   __DATA.__data: 0x770
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1152
-  Symbols:   2549
+  Functions: 1155
+  Symbols:   2553
   CStrings:  377
 
Symbols:
+ -[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:fragConstants:]
+ -[SUICEdgeLightMaskMetalLayer setCustomCornerRadii:]
+ -[SUICEdgeLightMaskMetalLayer setCustomCornerRadiiWithTopLeft:topRight:bottomLeft:bottomRight:width:]
+ GCC_except_table33
+ _OBJC_IVAR_$_SUICEdgeLightMaskMetalLayer._customCornerRadii
+ _OBJC_IVAR_$_SUICEdgeLightMaskMetalLayer._renderPipelinePerCorner
+ _OBJC_IVAR_$_SUICEdgeLightMaskMetalLayer._usePerCornerRadiiPipeline
- -[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:]
- GCC_except_table31
- _OBJC_IVAR_$_SUICEdgeLightMaskMetalLayer._customCornerRadius
Functions:
~ -[SUICEdgeLightMaskMetalLayer _loadMetalPipelines] : 540 -> 696
- -[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:]
~ -[SUICEdgeLightMaskMetalLayer _updateForUIIdiom] : 804 -> 840
~ -[SUICEdgeLightMaskMetalLayer _calculateCornerRadiusRatio] : 320 -> 344
~ -[SUICEdgeLightMaskMetalLayer _updateCustomCornerRadius] : 44 -> 72
~ -[SUICEdgeLightMaskMetalLayer _drawFrame:] : 1324 -> 1356
+ -[SUICEdgeLightMaskMetalLayer setCustomCornerRadii:]
+ -[SUICEdgeLightMaskMetalLayer setCustomCornerRadiiWithTopLeft:topRight:bottomLeft:bottomRight:width:]
+ -[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:fragConstants:]
~ -[SUICEdgeLightMaskMetalLayer .cxx_destruct] : 312 -> 332
+ -[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:fragConstants:].cold.1
~ -[SUICEdgeLightMaskMetalLayer _loadMetalPipelines].cold.2 : 96 -> 84
CStrings:
+ "%s Failed to specialize fragment %@ with constants, error %@"
+ "-[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:fragConstants:]"
- "\r\xf0\xf0\xf0\xf0\xc1"
- "-[SUICEdgeLightMaskMetalLayer _createRenderPipelineFromLibrary:archive:vert:frag:]"
```

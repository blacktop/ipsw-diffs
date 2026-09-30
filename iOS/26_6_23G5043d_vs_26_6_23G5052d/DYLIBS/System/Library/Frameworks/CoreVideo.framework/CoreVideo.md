## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-  __TEXT.__text: 0x51760
+  __TEXT.__text: 0x51948
   __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__cstring: 0x855c
+  __TEXT.__cstring: 0x86bc
   __TEXT.__objc_databytes: 0x493
   __TEXT.__const: 0x3878
   __TEXT.__oslogstring: 0x29b

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 2606
   Symbols:   5081
-  CStrings:  1309
+  CStrings:  1311
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__dof_CVPixelBu : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_dataobj : content changed
~ __AUTH.__objc_databytes : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _CVPixelBufferCreateWithIOSurface : 632 -> 640
~ _checkIOOrEXSurfaceAndCreatePixelBufferBacking : 2776 -> 3256
CStrings:
+ "checkIOOrEXSurfaceAndCreatePixelBufferBacking returning err %d because planeHeight[planeIndex %u] %u is not equal to %u required by image height %u and verticalSubsampling %u"
+ "checkIOOrEXSurfaceAndCreatePixelBufferBacking returning err %d because planeWidth[planeIndex %u] %u is not equal to %u required by image width %u and horizontalSubsampling %u"

```

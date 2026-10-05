## CoreIMS

> `/System/Library/PrivateFrameworks/CoreIMS.framework/CoreIMS`

```diff

-124.0.4.0.0
-  __TEXT.__text: 0x4f960
-  __TEXT.__objc_methlist: 0x47f4
-  __TEXT.__const: 0x4ea0
-  __TEXT.__gcc_except_tab: 0x50a8
+124.40.1.0.0
+  __TEXT.__text: 0x4faa0
+  __TEXT.__objc_methlist: 0x480c
+  __TEXT.__const: 0x4ec0
+  __TEXT.__gcc_except_tab: 0x50c8
   __TEXT.__cstring: 0x5dda
-  __TEXT.__oslogstring: 0x41c4
+  __TEXT.__oslogstring: 0x41f9
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x15b0
+  __TEXT.__unwind_info: 0x15b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x2258
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x410

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1627
-  Symbols:   3076
+  Functions: 1628
+  Symbols:   3078
   CStrings:  992
 
Symbols:
+ +[IMSRuntimeMaskRenderer minimumControlPointsForInterpolation:]
+ __OBJC_$_CLASS_METHODS_IMSRuntimeMaskRenderer
CStrings:
+ "[Mask] Mask Data is invalid, return full mask: interpolation %ld requires >= %lu control points (left %lu, right %lu)"
- "[Mask] Mask Data is invalid, return full mask: left %d, right %d"
```

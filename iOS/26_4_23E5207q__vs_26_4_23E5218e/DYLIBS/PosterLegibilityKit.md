## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-304.4.11.0.0
-  __TEXT.__text: 0x1b674
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x1ba4
-  __TEXT.__const: 0x330
+304.4.13.0.0
+  __TEXT.__text: 0x1b9ec
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x1bec
+  __TEXT.__const: 0x328
   __TEXT.__cstring: 0xf52
-  __TEXT.__oslogstring: 0xe6d
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__oslogstring: 0xf60
+  __TEXT.__gcc_except_tab: 0x6e0
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__objc_classname: 0x4fb
-  __TEXT.__objc_methname: 0x4831
-  __TEXT.__objc_methtype: 0xd0f
-  __TEXT.__objc_stubs: 0x38a0
-  __DATA_CONST.__got: 0x378
+  __TEXT.__objc_methname: 0x496b
+  __TEXT.__objc_methtype: 0xd74
+  __TEXT.__objc_stubs: 0x38e0
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11b0
+  __DATA_CONST.__objc_selrefs: 0x11e8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x4ed8
+  __AUTH_CONST.__objc_const: 0x4f78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x540
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x7d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23617C17-11F8-3B54-A665-9A6FD9B05F10
-  Functions: 674
-  Symbols:   2800
-  CStrings:  1362
+  UUID: E908041A-3F3D-3F7F-9B45-68F0F335055A
+  Functions: 680
+  Symbols:   2821
+  CStrings:  1381
 
Symbols:
+ -[PLKLegibilityImageRenderer setUsesContentAlignmentRectInsets:]
+ -[PLKLegibilityImageRenderer usesContentAlignmentRectInsets]
+ -[PLKLegibilityView alignmentMode]
+ -[PLKLegibilityView setAlignmentMode:]
+ -[PLKLegibilityView setShadowAlignmentInsets:]
+ -[PLKLegibilityView shadowAlignmentInsets]
+ _NSStringFromUIEdgeInsets
+ _OBJC_IVAR_$_PLKLegibilityImageRenderer._usesContentAlignmentRectInsets
+ _OBJC_IVAR_$_PLKLegibilityView._alignmentMode
+ _OBJC_IVAR_$_PLKLegibilityView._shadowAlignmentInsets
+ _UIEdgeInsetsZero
+ __OBJC_$_INSTANCE_VARIABLES_PLKLegibilityImageRenderer
+ __OBJC_$_PROP_LIST_PLKLegibilityImageRenderer
+ ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.111
+ ___block_literal_global.98
+ _objc_msgSend$alignmentRectInsets
+ _objc_msgSend$flatMap:
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$setNeedsLayout
- ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.112
- ___block_literal_global.99
- _objc_msgSend$flatMap:continuationScheduler:
- _objc_msgSend$globalAsyncScheduler
CStrings:
+ "PLK alignment-aware shadow rendering: alignmentInsets=%@"
+ "PLK view alignment offset: insets=%@, offset=(%.2f, %.2f)"
+ "TB,N,V_usesContentAlignmentRectInsets"
+ "TQ,N,V_alignmentMode"
+ "T{UIEdgeInsets=dddd},N,V_shadowAlignmentInsets"
+ "[SBH_LEGIBILITY] PLK alignment-aware contentRect: imageSize=%@, alignmentInsets=%@, alignmentSize=%@, bounds=%@, contentRect=%@"
+ "_alignmentMode"
+ "_shadowAlignmentInsets"
+ "_usesContentAlignmentRectInsets"
+ "alignmentMode"
+ "alignmentRectInsets"
+ "flatMap:"
+ "setAlignmentMode:"
+ "setNeedsLayout"
+ "setShadowAlignmentInsets:"
+ "setUsesContentAlignmentRectInsets:"
+ "shadowAlignmentInsets"
+ "usesContentAlignmentRectInsets"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
+ "{UIEdgeInsets=dddd}16@0:8"
- "flatMap:continuationScheduler:"
- "globalAsyncScheduler"

```

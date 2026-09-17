## HIToolbox

> `/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox`

```diff

-1272.0.0.0.0
-  __TEXT.__text: 0x28c07c
-  __TEXT.__objc_methlist: 0x3d74
-  __TEXT.__gcc_except_tab: 0x5804
-  __TEXT.__const: 0xab20
-  __TEXT.__cstring: 0x2da87
+1273.3.0.0.0
+  __TEXT.__text: 0x28d4c0
+  __TEXT.__objc_methlist: 0x3dfc
+  __TEXT.__gcc_except_tab: 0x5848
+  __TEXT.__const: 0xab30
+  __TEXT.__cstring: 0x2dae4
   __TEXT.__ustring: 0x9e
   __TEXT.__oslogstring: 0xc69
-  __TEXT.__unwind_info: 0xcb48
+  __TEXT.__unwind_info: 0xcb90
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x7a10
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2110
+  __DATA_CONST.__objc_selrefs: 0x2148
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__got: 0xce0
   __AUTH_CONST.__const: 0x15198
-  __AUTH_CONST.__cfstring: 0x1bc60
-  __AUTH_CONST.__objc_const: 0x4a18
+  __AUTH_CONST.__cfstring: 0x1bd60
+  __AUTH_CONST.__objc_const: 0x4b48
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3118
-  __AUTH.__objc_data: 0xa50
+  __AUTH_CONST.__auth_got: 0x3138
+  __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x328
-  __DATA.__objc_ivar: 0x4b0
+  __DATA.__objc_ivar: 0x4bc
   __DATA.__data: 0xbd8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x288

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 14285
-  Symbols:   18034
-  CStrings:  5633
+  Functions: 14298
+  Symbols:   18066
+  CStrings:  5641
 
Symbols:
+ -[CDImageData originalFrame]
+ -[CDImageData resetScaledSourceDragComponentsWithCursorOffset:]
+ -[CDImageData scaleSourceDragComponentsWithCursorOffset:options:]
+ -[CDImageData setOriginalFrame:]
+ -[CoreDragDraggingLayer contentRect:]
+ -[CoreDragDraggingLayer iconBounds]
+ -[_CDBadgeLayer init]
+ -[_CDOperationLayer dealloc]
+ -[_CDOperationLayer drawInContext:]
+ -[_CDOperationLayer init]
+ -[_CDOperationLayer operation]
+ -[_CDOperationLayer setOperation:]
+ OBJC_IVAR_$_CDImageData._originalFrame
+ OBJC_IVAR_$_CDImageData._scalingOptions
+ OBJC_IVAR_$__CDOperationLayer._operation
+ OBJC_IVAR_$__CDOperationLayer._pdfDocument
+ _BackingScaleFactor
+ _CGContextDrawPDFPage
+ _CGPDFDocumentCreateWithURL
+ _CGPDFDocumentGetPage
+ _CGPDFDocumentRelease
+ _CGPDFPageGetBoxRect
+ _OBJC_CLASS_$__CDOperationLayer
+ _OBJC_METACLASS_$__CDOperationLayer
+ __OBJC_$_INSTANCE_METHODS__CDOperationLayer
+ __OBJC_$_INSTANCE_VARIABLES__CDOperationLayer
+ __OBJC_$_PROP_LIST__CDOperationLayer
+ __OBJC_CLASS_RO_$__CDOperationLayer
+ __OBJC_METACLASS_RO_$__CDOperationLayer
+ __Z20SetupForFlockingPileP14OpaqueCoreDragP7CALayer7CGPoint
+ __ZL12MasterOffsetP14OpaqueCoreDragP21CoreDragDraggingLayerb
+ ___CoreDragUpdateContents
+ ___block_descriptor_40_e8_32o_e39_B32?0"CoreDragComponentLayer"8Q16^B24l
+ _objc_msgSend$iconBounds
+ _objc_msgSend$layerContentsForContentsScale:
+ _objc_msgSend$recommendedLayerContentsScale:
+ _objc_msgSend$resetScaledSourceDragComponentsWithCursorOffset:
+ _objc_msgSend$scaleSourceDragComponentsWithCursorOffset:options:
+ _objc_msgSend$setContentsScale:
+ _objc_msgSend$setOperation:
+ _objc_msgSend$setOriginalFrame:
- -[CDImageData resetScaledSourceDragComponentsWithCursorOffest:isTouch:]
- -[CDImageData scaleSourceDragComponentsToMeetHISpecWithCursorOffest:isTouch:]
- OBJC_IVAR_$_CDImageData._originalSize
- _CATransform3DMakeScale
- __Z25SetupForFlockingDirtyPileP14OpaqueCoreDragP7CALayer7CGPoint
- ___block_descriptor_40_e8_32o_e15_B32?08Q16^B24l
- _objc_msgSend$_ensureMinimumIconComponentTouchTargetSizeAndUpdateLabelPosition
- _objc_msgSend$resetScaledSourceDragComponentsWithCursorOffest:isTouch:
- _objc_msgSend$scaleSourceDragComponentsToMeetHISpecWithCursorOffest:isTouch:
CStrings:
+ "B32@?0@\"CoreDragComponentLayer\"8Q16^B24"
+ "CDDebugTouchDragging"
+ "alias"
+ "copy"
+ "leader"
+ "notallowed"
+ "operation"
+ "pdf"
+ "poof"
- "B32@?0@8Q16^B24"
```

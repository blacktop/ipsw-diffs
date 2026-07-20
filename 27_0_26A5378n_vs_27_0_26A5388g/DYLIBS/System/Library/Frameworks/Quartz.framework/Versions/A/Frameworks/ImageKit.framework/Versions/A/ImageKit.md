## ImageKit

> `/System/Library/Frameworks/Quartz.framework/Versions/A/Frameworks/ImageKit.framework/Versions/A/ImageKit`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1242.0.0.0.0
-  __TEXT.__text: 0x16f8d0
-  __TEXT.__objc_methlist: 0x1fbc4
-  __TEXT.__cstring: 0x17492
+1243.0.0.0.0
+  __TEXT.__text: 0x16fbac
+  __TEXT.__objc_methlist: 0x1fbd4
+  __TEXT.__cstring: 0x174ba
   __TEXT.__gcc_except_tab: 0xdec
   __TEXT.__const: 0x1b68
   __TEXT.__ustring: 0x9c

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x108b0
+  __DATA_CONST.__objc_selrefs: 0x108e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x958
   __DATA_CONST.__objc_arraydata: 0x5f8
   __DATA_CONST.__got: 0x1bc0
   __AUTH_CONST.__const: 0x2460
-  __AUTH_CONST.__cfstring: 0x16540
-  __AUTH_CONST.__objc_const: 0x304b8
+  __AUTH_CONST.__cfstring: 0x16560
+  __AUTH_CONST.__objc_const: 0x304c0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_doubleobj: 0x60

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10825
-  Symbols:   24722
-  CStrings:  3162
+  Functions: 10826
+  Symbols:   24728
+  CStrings:  3163
 
Symbols:
+ -[IKImageView2 _handleDoubleTapToZoom:]
+ GCC_except_table61
+ _objc_msgSend$_setMagnification:centeredAroundPoint:animate:
+ _objc_msgSend$locationInView:
+ _objc_msgSend$setAllowedTouchTypes:
+ _objc_msgSend$setButtonMask:
+ _objc_msgSend$setDelaysPrimaryMouseButtonEvents:
- GCC_except_table59
Functions:
~ -[IKImageView2 commonInit] : 820 -> 928
~ -[IKImageContentView setZoomFactor:centeredAtImagePoint:animate:stickyFit:] : 1420 -> 1448
~ -[IKScannerDeviceViewHandler setModeAndAdjust:] : 444 -> 452
~ ___75-[IKImageContentView setZoomFactor:centeredAtImagePoint:animate:stickyFit:]_block_invoke_2 : 216 -> 232
~ __75-[IKImageContentView setZoomFactor:centeredAtImagePoint:animate:stickyFit:]_block_invoke.151 : 256 -> 272
~ -[IKImageContentView _flipImageDirectionWithAnimation:] : 560 -> 568
~ ___55-[IKImageContentView _flipImageDirectionWithAnimation:]_block_invoke : 172 -> 188
~ -[IKImageContentView _setRotationAngleWithAnimation:duration:] : 908 -> 916
~ ___62-[IKImageContentView _setRotationAngleWithAnimation:duration:]_block_invoke : 272 -> 288
~ -[IKPictureTaker beginPictureTakerPopoverForView:withDelegate:relativeRect:source:didEndSelector:contextInfo:] : 212 -> 220
~ ___47-[IKScannerDeviceViewHandler setModeAndAdjust:]_block_invoke : 100 -> 92
~ __47-[IKScannerDeviceViewHandler setModeAndAdjust:]_block_invoke.209 : 100 -> 92
~ -[IKScanResultsTextCellView updateIcon] : 116 -> 132
~ ___39-[IKScanResultsTextCellView updateIcon]_block_invoke : 180 -> 176
~ -[IKScanUIControllerAdvanced setSelectionRect:] : 804 -> 808
~ ___47-[IKScanUIControllerAdvanced setSelectionRect:]_block_invoke : 40 -> 20
+ -[IKImageView2 _handleDoubleTapToZoom:]
CStrings:
+ "IKImageView2.doubleTapGestureRecognizer"
```

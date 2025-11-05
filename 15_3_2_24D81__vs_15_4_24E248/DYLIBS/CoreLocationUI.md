## CoreLocationUI

> `/System/iOSSupport/System/Library/Frameworks/CoreLocationUI.framework/Versions/A/CoreLocationUI`

```diff

-2956.0.6.0.0
-  __TEXT.__text: 0x5a50
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x454
-  __TEXT.__const: 0x98
+2960.0.57.0.0
+  __TEXT.__text: 0x5d40
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0x5d0
+  __TEXT.__const: 0x44
   __TEXT.__gcc_except_tab: 0x140
   __TEXT.__cstring: 0x2e5
   __TEXT.__oslogstring: 0x422
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x178
   __TEXT.__objc_classname: 0x72
   __TEXT.__objc_methname: 0x10ce
   __TEXT.__objc_methtype: 0x3ec
   __TEXT.__objc_stubs: 0xe20
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x4f8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0xd40
+  __AUTH_CONST.__objc_const: 0xaa0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97B55757-5BA6-3162-86EC-6843128444B4
-  Functions: 105
+  UUID: 36F14E67-FB87-3128-B869-1C30B88BB8B0
+  Functions: 104
   Symbols:   410
   CStrings:  335
 
Functions:
~ -[CLLocationButton init] : 232 -> 228
~ -[CLLocationButton initWithFrame:] : 264 -> 260
~ -[CLLocationButton initWithCoder:] : 628 -> 640
~ -[CLLocationButton _setupSlotView] : 2212 -> 2320
~ ___34-[CLLocationButton _setupSlotView]_block_invoke : 764 -> 808
~ __34-[CLLocationButton _setupSlotView]_block_invoke.37 : 168 -> 176
~ -[CLLocationButton _sendActionsForEvents:withEvent:] : 208 -> 224
~ -[CLLocationButton _computeLocationButtonTag] : 1304 -> 1368
~ -[CLLocationButton _yieldSlotViewContentForLayerContextID:slotStyle:withYieldBlock:] : 1056 -> 1124
~ ___84-[CLLocationButton _yieldSlotViewContentForLayerContextID:slotStyle:withYieldBlock:]_block_invoke : 268 -> 284
~ ___84-[CLLocationButton _yieldSlotViewContentForLayerContextID:slotStyle:withYieldBlock:]_block_invoke_2 : 440 -> 472
~ -[CLLocationButton intrinsicContentSize] : 160 -> 152
~ -[CLLocationButtonTag initWithLabel:iconType:backgroundColor:tintColor:cornerRadius:frame:fontSize:] : 500 -> 492
~ -[CLLocationButtonTag copyWithZone:] : 496 -> 516
~ -[CLLocationButtonTag initWithCoder:] : 648 -> 644
~ -[CLLocationButtonTag isEqual:] : 108 -> 104
~ -[CLLocationButtonTag isValid] : 144 -> 140
~ -[CLLocationButtonTag contrastValidForBgColorAndFgTextWithCumulativeOpacity:] : 1328 -> 1436
~ +[CLLocationButtonTag secureNameForLabel:] : 184 -> 220
- sub_263a01c24
~ -[CLLocationButtonTag setRenderedSuccessfully:] : 56 -> 48
~ -[CLLocationButtonDrawing initWithStyle:tag:remote:] : 316 -> 304
~ +[CLLocationButtonDrawing _drawingWithStyle:tag:remote:] : 196 -> 188
~ -[CLLocationButtonDrawing drawingSize] : 288 -> 280
~ -[CLLocationButtonDrawing drawInContext:atPoint:] : 1220 -> 1252
~ -[CLLocationButtonDrawing _computeImageMetrics] : 3528 -> 3636
~ -[CLLocationButtonDrawing imageWithStyle:tag:forRemote:] : 136 -> 132
~ _calculateLuminanceForColor : 420 -> 600

```

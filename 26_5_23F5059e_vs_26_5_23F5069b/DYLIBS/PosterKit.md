## PosterKit

> `/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit`

```diff

-304.5.3.0.0
-  __TEXT.__text: 0x157da8
-  __TEXT.__auth_stubs: 0x2690
+304.5.4.102.0
+  __TEXT.__text: 0x158364
+  __TEXT.__auth_stubs: 0x26a0
   __TEXT.__objc_methlist: 0x18844
-  __TEXT.__const: 0x28c4
+  __TEXT.__const: 0x28e4
   __TEXT.__cstring: 0x9c6f
-  __TEXT.__oslogstring: 0x62a9
+  __TEXT.__oslogstring: 0x65c9
   __TEXT.__gcc_except_tab: 0x2848
   __TEXT.__ustring: 0x1c
   __TEXT.__constg_swiftt: 0xa38

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_mpenum: 0x118
-  __TEXT.__unwind_info: 0x5ef0
+  __TEXT.__unwind_info: 0x5ef8
   __TEXT.__eh_frame: 0xa30
   __TEXT.__objc_classname: 0x3e98
-  __TEXT.__objc_methname: 0x3fb4f
+  __TEXT.__objc_methname: 0x3fb5f
   __TEXT.__objc_methtype: 0xc04d
-  __TEXT.__objc_stubs: 0x21ce0
+  __TEXT.__objc_stubs: 0x21d00
   __DATA_CONST.__got: 0x19b8
   __DATA_CONST.__const: 0x3558
   __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba08
+  __DATA_CONST.__objc_selrefs: 0xba10
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x838
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x1358
+  __AUTH_CONST.__auth_got: 0x1360
   __AUTH_CONST.__const: 0x23c0
   __AUTH_CONST.__cfstring: 0x9ca0
   __AUTH_CONST.__objc_const: 0x4f0d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F9B6F1C0-D20B-3259-A0ED-DC1D05F3630D
+  UUID: F8CBBB0F-8511-3F7B-90AA-5B53211EED25
   Functions: 8961
-  Symbols:   29104
-  CStrings:  13418
+  Symbols:   29106
+  CStrings:  13428
 
Symbols:
+ _UIFloorToScale
+ _objc_msgSend$screen
Functions:
~ -[PREditor setComplicationRowAtBottom:] : 544 -> 688
~ -[PRComplicationContainerViewController setWidgetsUseBottomLayout:] : 212 -> 380
~ -[PRComplicationContainerViewController updateForComplicationGalleryHeight:completion:] : 460 -> 632
~ -[PRComplicationContainerViewController updateComplicationLayoutIfCovered:] : 308 -> 492
~ -[PREditingSceneViewController _updateComplicationLayout] : 624 -> 776
~ -[PREditingSceneViewController setComplicationsUseBottomLayout:animated:] : 196 -> 372
~ -[PREditingSceneViewController _updateComplicationLayoutIfPermitted] : 176 -> 392
~ -[PREditingSceneViewController _dismissAnyPresentedComplicationGalleryAnimated:withCompletion:] : 436 -> 564
~ -[PREditingSceneViewController presentationControllerDidDismiss:] : 424 -> 552
CStrings:
+ "[Widget Row] PREditor setComplicationRowAtBottom: %{bool}u -> %{bool}u"
+ "[Widget Row] _dismissAnyPresentedComplicationGallery: anyPresented=%{bool}u isDismissing=%{bool}u animated=%{bool}u"
+ "[Widget Row] _updateComplicationLayoutIfPermitted: galleryPresented=%{bool}u dragInProgress=%{bool}u"
+ "[Widget Row] container setWidgetsUseBottomLayout: %{bool}u frame=%@"
+ "[Widget Row] presentationControllerDidDismiss: presentedVC=%@ complicationsGallery=%@"
+ "[Widget Row] setComplicationsUseBottomLayout: %{bool}u -> %{bool}u animated=%{bool}u"
+ "[Widget Row] setting widgetsUseBottomLayout: %{bool}u"
+ "[Widget Row] updateComplicationLayoutIfCovered: %{bool}u appeared=%{bool}u widgetsUseBottomLayout=%{bool}u"
+ "[Widget Row] updateForComplicationGalleryHeight: %.1f widgetsCoveredByModal=%{bool}u widgetsUseBottomLayout=%{bool}u"
+ "screen"

```

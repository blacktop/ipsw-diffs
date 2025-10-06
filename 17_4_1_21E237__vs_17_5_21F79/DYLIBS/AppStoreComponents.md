## AppStoreComponents

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`

```diff

-6.4.31.0.0
-  __TEXT.__text: 0x92518
+6.4.37.2.1
+  __TEXT.__text: 0x92734
   __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0x718c
+  __TEXT.__objc_methlist: 0x719c
   __TEXT.__const: 0x1434
   __TEXT.__gcc_except_tab: 0x660
-  __TEXT.__cstring: 0x3712
+  __TEXT.__cstring: 0x3722
   __TEXT.__dlopen_cstrs: 0x14f
-  __TEXT.__oslogstring: 0x2ca6
+  __TEXT.__oslogstring: 0x2d12
   __TEXT.__constg_swiftt: 0x6d4
   __TEXT.__swift5_typeref: 0x44a
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0xa8
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2550
+  __TEXT.__unwind_info: 0x2558
   __TEXT.__objc_classname: 0x100d
-  __TEXT.__objc_methname: 0x10b63
-  __TEXT.__objc_methtype: 0x2fc1
+  __TEXT.__objc_methname: 0x10bb1
+  __TEXT.__objc_methtype: 0x303f
   __TEXT.__objc_stubs: 0xbce0
   __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x1630
+  __DATA_CONST.__const: 0x1648
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb000
-  __DATA_CONST.__objc_selrefs: 0x3678
+  __DATA_CONST.__objc_const: 0xb020
+  __DATA_CONST.__objc_selrefs: 0x3680
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x698
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__objc_const: 0xaf0
-  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__cfstring: 0x40e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__const: 0xe30
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xc48
-  __AUTH.__objc_data: 0x5f0
+  __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x768
   __DATA.__data: 0x1cd0

   __DATA.__common: 0x150
   __DATA_DIRTY.__const: 0x15d8
   __DATA_DIRTY.__objc_const: 0x3410
-  __DATA_DIRTY.__objc_data: 0x2280
+  __DATA_DIRTY.__objc_data: 0x2230
   __DATA_DIRTY.__data: 0x8b0
   __DATA_DIRTY.__bss: 0x788
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1690817-AEC7-3D92-93A1-4644F323B7EE
-  Functions: 3588
-  Symbols:   9822
-  CStrings:  4638
+  UUID: 25CC6665-B414-3DBC-AF87-4BA7A16D6758
+  Functions: 3591
+  Symbols:   9831
+  CStrings:  4647
 
Symbols:
+ -[ASCLockupProductDetails productViewController:userDidInteractWithProduct:]
+ -[ASCLockupView productDetailsUserDidInteractWithApp:interactionType:]
+ -[ASCLockupView productDetailsUserDidInteractWithApp:interactionType:].cold.1
+ -[ASCLockupView productDetailsUserDidInteractWithApp:interactionType:].cold.2
+ GCC_except_table34
+ _ASCLockupProductDetailsInteractionTypeDismissed
+ _ASCLockupProductDetailsInteractionTypeOpened
+ _ASCLockupProductDetailsInteractionTypePurchased
+ _objc_msgSend$productDetailsUserDidInteractWithApp:interactionType:
- -[ASCLockupView productDetailsWillOpenApp:]
- -[ASCLockupView productDetailsWillOpenApp:].cold.1
- GCC_except_table33
- _objc_msgSend$productDetailsWillOpenApp:
CStrings:
+ "Product details user did interact with app: %@"
+ "T@\"<ASCMiniProductPagePresenterView>\",R,W,N,V_view"
+ "dismissed"
+ "opened"
+ "productDetailsUserDidInteractWithApp:interactionType:"
+ "productViewController userDidInteractWithProduct: %{public}@"
+ "productViewController:userDidInteractWithProduct:"
+ "v32@0:8@\"ASCLockupProductDetails\"16@\"NSString\"24"
+ "v32@0:8@\"SKStoreProductViewController\"16Q24"
+ "v32@0:8@16Q24"
+ "{?=\"lockupViewDidBeginRequest\"b1\"lockupViewDidFinishRequest\"b1\"lockupViewDidFailRequestWithError\"b1\"lockupViewAppStateDidChange\"b1\"metricsActivityForAdLockupViewToPerformActionOfOfferInState\"b1\"lockupViewDidInvalidateIntrinsicContentSize\"b1\"lockupViewShouldSupportDSIDLessInstalls\"b1\"productDetailsPresentationContextForLockupView\"b1\"lockupViewPreprocessOfferInStateCompletionBlock\"b1\"badgeViewForLockupView\"b1\"lockupViewProductPageWillOpenApp\"b1\"productDetailsUserDidInteractWithAppInteractionType\"b1}"
- "T@\"<ASCMiniProductPagePresenterView>\",R,N,V_view"
- "productDetailsWillOpenApp:"
- "v24@0:8@\"ASCLockupProductDetails\"16"
- "{?=\"lockupViewDidBeginRequest\"b1\"lockupViewDidFinishRequest\"b1\"lockupViewDidFailRequestWithError\"b1\"lockupViewAppStateDidChange\"b1\"metricsActivityForAdLockupViewToPerformActionOfOfferInState\"b1\"lockupViewDidInvalidateIntrinsicContentSize\"b1\"lockupViewShouldSupportDSIDLessInstalls\"b1\"productDetailsPresentationContextForLockupView\"b1\"lockupViewPreprocessOfferInStateCompletionBlock\"b1\"badgeViewForLockupView\"b1\"lockupViewProductPageWillOpenApp\"b1}"

```

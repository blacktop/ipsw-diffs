## PassKitMacHelperTemp

> `/System/Library/PrivateFrameworks/PassKitMacHelperTemp.framework/Versions/A/PassKitMacHelperTemp`

```diff

-1591.4.3.0.0
-  __TEXT.__text: 0x80b0
+1591.5.17.3.0
+  __TEXT.__text: 0x80e4
   __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x918
+  __TEXT.__objc_methlist: 0xc50
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__cstring: 0x452

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x18a0
+  __AUTH_CONST.__objc_const: 0x12b8
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0xb4

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 904D3800-55EA-356D-9793-0B9C16CC3000
-  Functions: 270
-  Symbols:   737
+  UUID: FEFA2FAA-D037-3D22-B481-B09F8230AFF8
+  Functions: 271
+  Symbols:   738
   CStrings:  463
 
Symbols:
+ initUINSSharedApplicationDelegate.cold.1
Functions:
~ -[PKPaymentButton setType:] : 96 -> 88
~ -[PKPaymentButton setHighlighted:] : 460 -> 444
~ -[PassKitMacHelper setUiKitDelegate:] : 100 -> 88
~ -[PassKitMacHelper setCoordinator:] : 100 -> 88
~ -[PassKitMacHelper presentInAppPaymentInterfaceWithPaymentRequest:completion:] : 268 -> 264
~ _initUINSSharedApplicationDelegate : 104 -> 88
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didAuthorizePayment:handler:] : 184 -> 180
~ -[PKPaymentAuthorizationController paymentAuthorizationViewControllerWillAuthorizePayment:] : 140 -> 136
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didRequestMerchantSessionUpdate:] : 208 -> 196
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didRequestMerchantSessionWithURL:merchantSessionUpdate:] : 236 -> 224
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didSelectShippingMethod:handler:] : 232 -> 228
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didSelectShippingContact:handler:] : 232 -> 228
~ -[PKPaymentAuthorizationController paymentAuthorizationViewController:didSelectPaymentMethod:handler:] : 224 -> 220
~ __106+[PKPaymentAuthorizationViewController requestViewControllerWithPaymentRequest:viewController:completion:]_block_invoke.15 : 368 -> 408
~ __106+[PKPaymentAuthorizationViewController requestViewControllerWithPaymentRequest:viewController:completion:]_block_invoke_2.17 : 312 -> 368
~ -[PKPaymentAuthorizationViewController setDelegate:] : 116 -> 112
~ -[PKPaymentAuthorizationViewController setPrivateDelegate:] : 116 -> 112
~ -[PKPaymentAuthorizationViewController setPaymentAuthorizationHostContext:] : 196 -> 192
~ -[PKPaymentAuthorizationViewController setRemoteViewController:] : 492 -> 488
~ __125+[PKCatalystPaymentAuthorizationViewController requestViewControllerWithPaymentRequest:uiKitDelegate:coordinator:completion:]_block_invoke.12 : 384 -> 420
~ __125+[PKCatalystPaymentAuthorizationViewController requestViewControllerWithPaymentRequest:uiKitDelegate:coordinator:completion:]_block_invoke_2.14 : 328 -> 376
~ -[PKCatalystPaymentAuthorizationViewController setUiKitDelegate:] : 372 -> 364
~ -[PKCatalystPaymentAuthorizationViewController setCoordinator:] : 144 -> 140
~ -[PKCatalystPaymentAuthorizationViewController setPaymentAuthorizationHostContext:] : 296 -> 292
~ -[PKCatalystPaymentAuthorizationViewController setRemoteViewController:] : 492 -> 488
+ initUINSSharedApplicationDelegate.cold.1

```

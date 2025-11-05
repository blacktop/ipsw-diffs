## PassKitUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/Versions/A/PassKitUIFoundation`

```diff

-1591.4.3.0.0
-  __TEXT.__text: 0x1c1f0
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x17ac
-  __TEXT.__const: 0x6c8
-  __TEXT.__cstring: 0xc76
+1591.5.17.3.0
+  __TEXT.__text: 0x1d924
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x1a34
+  __TEXT.__const: 0x768
+  __TEXT.__cstring: 0xd1e
   __TEXT.__oslogstring: 0xb2e
-  __TEXT.__gcc_except_tab: 0x454
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__gcc_except_tab: 0x44c
+  __TEXT.__unwind_info: 0x860
+  __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x4d4
-  __TEXT.__objc_methname: 0x58d6
+  __TEXT.__objc_methname: 0x5a3f
   __TEXT.__objc_methtype: 0x1100
-  __TEXT.__objc_stubs: 0x4340
-  __DATA_CONST.__got: 0x3c0
+  __TEXT.__objc_stubs: 0x4600
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f0
+  __DATA_CONST.__objc_selrefs: 0x1758
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x4a68
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x45b0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_ivar: 0x490
   __DATA.__data: 0x420
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x500

   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/MetalPerformanceShaders
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
+  - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore
+  - /System/iOSSupport/System/Library/Frameworks/MapKit.framework/Versions/A/MapKit
   - /System/iOSSupport/System/Library/Frameworks/MetalKit.framework/Versions/A/MetalKit
   - /System/iOSSupport/System/Library/Frameworks/SceneKit.framework/Versions/A/SceneKit
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7FDC3762-5BB7-3B01-B658-CC5EB8BDF101
-  Functions: 656
-  Symbols:   2180
-  CStrings:  1617
+  UUID: A38B2F9B-9084-31BA-A8A9-B16F1E97BDBB
+  Functions: 706
+  Symbols:   2284
+  CStrings:  1667
 
Symbols:
+ +[PKMotionManager sharedManager].cold.1
+ +[PKPeerPayment3DStore sharedInstance].cold.1
+ +[PKPeerPaymentFontHelper chiseledCashFontDescriptor].cold.1
+ -[PKPayLaterCardRenderer _removeInstances:category:time:].cold.1
+ -[PKPayLaterCardRenderer setMagnitudes:].cold.1
+ -[PKRenderLoop invalidate].cold.1
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.1
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.2
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.3
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.4
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.5
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.6
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.7
+ -[PKTextureLoader initForDevice:image:withStorageMode:premultiplyAlpha:colorSpace:renderingIntent:].cold.8
+ -[PKTexturedCardRenderer renderAtTime:].cold.1
+ -[PKTexturedCardRenderer renderAtTime:].cold.2
+ -[PKTexturedCardRenderer renderAtTime:].cold.3
+ -[PKTexturedCardRenderer renderAtTime:].cold.4
+ _CGBitmapContextCreateImage
+ _CGContextDrawImage
+ _CGContextFillRect
+ _CGContextRelease
+ _CGContextSetBlendMode
+ _CGContextSetFillColorWithColor
+ _CGPDFDocumentCreateWithURL
+ _CGPDFDocumentRelease
+ _ImageOverlaidWithColor
+ _ImageRefFromResizedImageAndBackgroundColor
+ _OBJC_CLASS_$_GEOFeatureStyleAttributes
+ _OBJC_CLASS_$_MKIconManager
+ _OBJC_CLASS_$_MKMapService
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _PKBrightColorForMerchantCategory
+ _PKCurrencyCodeForTransitTransactionIcon
+ _PKFloatCeilToPixelWithScale
+ _PKIconForGenericBusiness
+ _PKIconForPDFName
+ _PKIconForRewardsRedemption
+ _PKIconForStyleAttributes
+ _PKIconForTopUpWithCurrency
+ _PKIconForTransitCardRead
+ _PKIconForTransitTransaction
+ _PKIconWithImageAndBackgroundColor
+ _PKMapsColorForMerchant
+ _PKMapsColorForMerchantCategory
+ _PKMapsIconForMerchant
+ _PKMapsIconForMerchantCategory
+ _PKMapsIconForPayLaterMerchant
+ _PKMapsIconFromStylingInfo
+ _PKMapsStylingInfoForMerchant
+ _PKMapsStylingInfoForMerchantCategory
+ _PKMerchantCategoryToString
+ _PKPassKitUIBundle
+ _PKStyleAttributesForTransitType
+ _UIGraphicsBeginImageContextWithOptions
+ _UIGraphicsEndImageContext
+ _UIGraphicsGetCurrentContext
+ _UIGraphicsGetImageFromCurrentImageContext
+ __41-[PKCategoryVisualizationCardView _empty]_block_invoke.cold.1
+ __41-[PKCategoryVisualizationCardView _empty]_block_invoke_2.cold.1
+ __Z15PKCreateCGImageP13CGPDFDocument6CGSized
+ __Z21PKCreateBitmapContext6CGSizebdb
+ _objc_msgSend$amount
+ _objc_msgSend$amounts
+ _objc_msgSend$currency
+ _objc_msgSend$currencyCode
+ _objc_msgSend$drawAtPoint:
+ _objc_msgSend$imageForSize:scale:transparent:
+ _objc_msgSend$imageForStyle:size:forScale:format:transparent:
+ _objc_msgSend$imageWithCGImage:scale:orientation:
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$mapsBrand
+ _objc_msgSend$mapsMerchant
+ _objc_msgSend$merchantCategory
+ _objc_msgSend$newFillColorForStyleAttributes:forScale:
+ _objc_msgSend$styleAttributesForTransitType:
+ _objc_msgSend$stylingForWalletCategory:
+ _objc_msgSend$stylingInfo
+ _objc_msgSend$systemBlackColor
+ _objc_msgSend$tintColorForScale:
+ _objc_msgSend$trainStationStyleAttributes
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$useRawMerchantData
+ _objc_msgSend$whiteColor
+ _objc_retainAutoreleasedReturnValue
- -[PKAuthenticatorEvaluationRequest setUseStockAuthInterface:]
- -[PKAuthenticatorEvaluationRequest useStockAuthInterface]
- -[PKPayLaterCardRenderer _initWithRenderLoop:overlayLoader:].cold.1
- OBJC_IVAR_$_PKAuthenticatorEvaluationRequest._useStockAuthInterface
CStrings:
+ "AUD"
+ "CAD"
+ "CNY"
+ "CardReadTransactionIcon"
+ "DollarTopUpIcon"
+ "GenericBusinessIcon"
+ "GenericCurrencyTopUpIcon"
+ "HKD"
+ "JPY"
+ "KRW"
+ "NZD"
+ "USD"
+ "WonTopUpIcon"
+ "YenYuanTopUpIcon"
+ "amount"
+ "amounts"
+ "currency"
+ "currencyCode"
+ "drawAtPoint:"
+ "imageForSize:scale:transparent:"
+ "imageForStyle:size:forScale:format:transparent:"
+ "imageWithCGImage:scale:orientation:"
+ "initWithCGImage:scale:orientation:"
+ "mapsBrand"
+ "mapsMerchant"
+ "merchantCategory"
+ "newFillColorForStyleAttributes:forScale:"
+ "pdf"
+ "star.circle.fill"
+ "styleAttributesForTransitType:"
+ "stylingForWalletCategory:"
+ "stylingInfo"
+ "systemBlackColor"
+ "tintColorForScale:"
+ "trainStationStyleAttributes"
+ "uppercaseString"
+ "useRawMerchantData"
+ "whiteColor"
- "TB,N,V_useStockAuthInterface"
- "_useStockAuthInterface"
- "setUseStockAuthInterface:"
- "useStockAuthInterface"

```

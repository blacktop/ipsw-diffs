## AppleMediaServicesUIPaymentSheets

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets`

```diff

-6.1.20.2.4
-  __TEXT.__text: 0x192f4
-  __TEXT.__auth_stubs: 0x1150
+6.2.8.0.0
+  __TEXT.__text: 0x1bf58
+  __TEXT.__auth_stubs: 0x11d0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x16c4
-  __TEXT.__cstring: 0x711
-  __TEXT.__swift5_typeref: 0x22b8
-  __TEXT.__swift5_capture: 0x230
-  __TEXT.__constg_swiftt: 0x954
-  __TEXT.__swift5_reflstr: 0x53d
-  __TEXT.__swift5_fieldmd: 0x804
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__swift5_proto: 0xec
-  __TEXT.__swift5_types: 0xb0
+  __TEXT.__const: 0x18f4
+  __TEXT.__cstring: 0x641
+  __TEXT.__swift5_typeref: 0x254c
+  __TEXT.__swift5_capture: 0x288
+  __TEXT.__constg_swiftt: 0xa68
+  __TEXT.__swift5_reflstr: 0x5cd
+  __TEXT.__swift5_fieldmd: 0x8d8
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0x2e8
+  __TEXT.__swift5_proto: 0xf0
+  __TEXT.__swift5_types: 0xc4
   __TEXT.__oslogstring: 0x85
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_methname: 0x2f2
-  __DATA_CONST.__got: 0x3a8
+  __TEXT.__unwind_info: 0x998
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_methname: 0x2c8
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x158
-  __AUTH_CONST.__auth_got: 0x8a8
-  __AUTH_CONST.__auth_ptr: 0x528
-  __AUTH_CONST.__const: 0x18d0
+  __DATA_CONST.__objc_selrefs: 0x140
+  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_ptr: 0x578
+  __AUTH_CONST.__const: 0x1c60
   __AUTH_CONST.__objc_const: 0x490
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x318
-  __DATA.__data: 0x630
-  __DATA.__bss: 0x13a0
+  __AUTH.__data: 0x3a8
+  __DATA.__data: 0x6f8
+  __DATA.__bss: 0x1440
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x150
   __DATA_DIRTY.__data: 0x330

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI
   - /System/Library/PrivateFrameworks/JetEngine.framework/JetEngine
   - /System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 943
-  Symbols:   317
-  CStrings:  90
+  Functions: 1018
+  Symbols:   314
+  CStrings:  86
 
Symbols:
+ _AMSPaymentContentItemCountryKey
+ _AMSPaymentContentItemImageAttachment
+ _AMSPaymentContentItemRatingKey
+ _AMSPaymentSheetContentItemRegionalRating
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _objc_retain_x1
+ _objc_retain_x27
+ _swift_getEnumCaseMultiPayload
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
- _AMSPaymentSheetContentItemRatingAU
- _AMSPaymentSheetContentItemRatingFR
- _AMSPaymentSheetContentItemRatingKR
- _CGBitmapContextCreate
- _CGBitmapContextCreateImage
- _CGColorSpaceCreateWithName
- _CGContextClipToMask
- _CGContextFillRect
- _CGContextSetBlendMode
- _CGContextSetFillColorWithColor
- _CGContextSetInterpolationQuality
- _CGImageGetBitmapInfo
- _CGImageGetBitsPerComponent
- _CGImageGetColorSpace
- _OBJC_CLASS_$_AMSDevice
- _OBJC_CLASS_$_UIFontMetrics
- _kCGColorSpaceSRGB
- _objc_retain_x28
CStrings:
+ "AMSPaymentRequestLayoutStyleAlternativeDistribution"
+ "APPS-AUSTRALIA"
+ "APPS-BRAZIL"
+ "APPS-FRANCE"
+ "APPS-KOREA"
+ "ContentSizeCategory"
+ "MPAA"
+ "Unexpected rating system: "
+ "drawInRect:"
+ "imageWithActions:"
+ "initWithData:"
+ "initWithSize:"
+ "pointSize"
+ "preferredFontForTextStyle:"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
- "CGColor"
- "CGImage"
- "Could not find bundle /System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework"
- "Could not get color for image"
- "Could not get drawing context"
- "Could not load image for rating "
- "Unable to create image from context"
- "Unexpected rating: "
- "ams_primaryText"
- "assetName not found "
- "currentTraitCollection"
- "description"
- "initForTextStyle:"
- "rating_mpaa_nc17"
- "rating_mpaa_pg13"
- "rating_mpaa_unrated"
- "scaledValueForValue:"
- "screenScale"
- "userInterfaceStyle"

```

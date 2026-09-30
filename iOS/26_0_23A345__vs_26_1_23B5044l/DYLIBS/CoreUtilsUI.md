## CoreUtilsUI

> `/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI`

```diff

-800.15.0.0.0
-  __TEXT.__text: 0x64d8
-  __TEXT.__auth_stubs: 0x660
+810.16.0.0.0
+  __TEXT.__text: 0x9294
+  __TEXT.__auth_stubs: 0x960
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__const: 0x7a
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_typeref: 0x12b
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__swift5_capture: 0xc0
-  __TEXT.__cstring: 0x251
-  __TEXT.__oslogstring: 0x1e9
-  __TEXT.__swift_as_entry: 0xc
-  __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__eh_frame: 0x2b8
-  __TEXT.__objc_methname: 0x12c
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x88
+  __TEXT.__const: 0xd8
+  __TEXT.__swift5_typeref: 0x1aa
+  __TEXT.__swift5_capture: 0x10c
+  __TEXT.__cstring: 0x453
+  __TEXT.__oslogstring: 0x23c
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__constg_swiftt: 0x84
+  __TEXT.__swift5_fieldmd: 0x38
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0xd
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__eh_frame: 0x4f0
+  __TEXT.__objc_methname: 0x355
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x180
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x488
   __AUTH_CONST.__objc_const: 0x238
   __AUTH.__objc_data: 0x90
-  __DATA.__data: 0x58
-  __DATA.__bss: 0x10
+  __DATA.__data: 0xa0
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x20
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift
   - /System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AE14D017-6898-3290-A402-C243B8686E43
-  Functions: 121
-  Symbols:   190
-  CStrings:  64
+  UUID: AD8AC448-012A-359D-A9C6-B6FA728F1FA8
+  Functions: 174
+  Symbols:   251
+  CStrings:  106
 
Symbols:
+ _CGAffineTransformMakeScale
+ _CGAffineTransformMakeTranslation
+ _CGRectGetHeight
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CGRectGetWidth
+ _CGRectIntegral
+ _OBJC_CLASS_$_CIColor
+ _OBJC_CLASS_$_CIContext
+ _OBJC_CLASS_$_CIFilter
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy16_8
+ ___swift_project_boxed_opaque_existential_1
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_CoreUtilsUI
+ _block_copy_helper.13
+ _block_descriptor.15
+ _block_destroy_helper.14
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _swift_getForeignTypeMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_n
+ _swift_willThrow
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic Say_____G So24OS_dispatch_queue_serialC8DispatchE10AttributesV
+ _symbolic SbSg
+ _symbolic ScCy___________pG So10CGImageRefa s5ErrorP
+ _symbolic So30UIGraphicsImageRendererContextCIgg_
+ _symbolic So7UIImageC
+ _symbolic _____ 11CoreUtilsUI08CUQRCodeB0O
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ So6CGSizeV
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _type_layout_string So6CGSizeV
- _symbolic _____ 11CoreUtilsUI13CUPlaceholderV
CStrings:
+ "### create rounded QR code failed, falling back to legacy QR code: error=%@"
+ "Adjust mask QR code image failed"
+ "CUQRCodeUtils.generateImage"
+ "Color invert QR code image failed"
+ "Create CIImage from UIImage failed"
+ "Mask to alpha QR code image failed"
+ "QR code output image size invalid"
+ "QRCodeGenerator"
+ "SF symbol not found: "
+ "_systemImageNamed:withConfiguration:"
+ "blackColor"
+ "clearColor"
+ "colorInvertFilter"
+ "configurationWithPointSize:weight:"
+ "create QR code CGImage from CIImage failed"
+ "create masked QR image failed"
+ "createCGImage:fromRect:"
+ "drawInRect:"
+ "extent"
+ "generateImage(message:size:scale:symbolName:forceLegacy:dispatchQueue:)"
+ "imageByApplyingTransform:"
+ "imageWithActions:"
+ "imageWithTintColor:renderingMode:"
+ "initWithColor:"
+ "initWithImage:"
+ "initWithSize:"
+ "labelColor"
+ "maskToAlphaFilter"
+ "outputImage"
+ "roundedQRCodeGeneratorFilter"
+ "setBackgroundImage:"
+ "setCenterSpaceSize:"
+ "setColor0:"
+ "setColor1:"
+ "setCorrectionLevel:"
+ "setInputImage:"
+ "setMessage:"
+ "setRoundedData:"
+ "setScale:"
+ "sourceOutCompositingFilter"
+ "sourceOverCompositingFilter"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"

```

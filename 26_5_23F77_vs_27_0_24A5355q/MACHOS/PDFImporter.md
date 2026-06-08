## PDFImporter

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/PDFImporter.appex/PDFImporter`

```diff

-1451.5.3.0.0
-  __TEXT.__text: 0xd3c
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x3c
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x22
+1527.0.0.0.0
+  __TEXT.__text: 0x1238
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methlist: 0x68
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__cstring: 0x67
   __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x355
-  __TEXT.__objc_methtype: 0x93
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_methname: 0x441
+  __TEXT.__objc_methtype: 0xa4
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xd8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/FileDerivatives.framework/FileDerivatives
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA8D269A-8974-3794-B50E-F46034D0F1C5
-  Functions: 7
-  Symbols:   67
-  CStrings:  61
+  UUID: 29199AE2-E21C-3470-87E6-31350181C3C9
+  Functions: 11
+  Symbols:   93
+  CStrings:  72
 
Symbols:
+ _CFRelease
+ _CGColorSpaceCopyPropertyList
+ _CGColorSpaceCreateDeviceGray
+ _CGImageRelease
+ _FDSApplyAttributeDictionaryToCSSearchableItemAttributeSet
+ _FDSAttributeDictionaryFromImageWithOptions
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSValue
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ ___kCFBooleanTrue
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCGDrawPDFPageAllowUpscaleOptionKey
+ _kCGDrawPDFPageSourceRectOptionKey
+ _kCGDrawPDFPageWhiteBackgroundOptionKey
+ _kFDSImportOptionAllOptions
+ _kFDSImportOptionFallbackOCR
+ _kFDSImportOptionMaxPageCount
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
+ "@40@0:8@16@24@32"
+ "attributeDictionary"
+ "boolValue"
+ "createImageWithData:"
+ "dictionaryWithObjects:forKeys:count:"
+ "drawWithBox:size:colorSpace:options:completion:"
+ "performOCRWithPDFDocument:existingAttributes:options:"
+ "unsignedIntegerValue"
+ "v24@?0@\"CGBitmapFormat\"8@\"NSData\"16"
+ "valueWithBytes:objCType:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"

```

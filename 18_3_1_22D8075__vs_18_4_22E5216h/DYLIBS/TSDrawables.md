## TSDrawables

> `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables`

```diff

-480.2.0.0.0
-  __TEXT.__text: 0x1cda2c
-  __TEXT.__auth_stubs: 0x2fe0
+481.0.0.0.0
+  __TEXT.__text: 0x1cb444
+  __TEXT.__auth_stubs: 0x3050
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x10404
-  __TEXT.__const: 0xc80a
-  __TEXT.__gcc_except_tab: 0xb5e0
-  __TEXT.__cstring: 0x16098
-  __TEXT.__unwind_info: 0x99e0
+  __TEXT.__objc_methlist: 0x11acc
+  __TEXT.__const: 0xc88e
+  __TEXT.__gcc_except_tab: 0xb664
+  __TEXT.__cstring: 0x16162
+  __TEXT.__unwind_info: 0x96a8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x191a
-  __TEXT.__objc_methname: 0x23d7e
-  __TEXT.__objc_methtype: 0x6847
-  __TEXT.__objc_stubs: 0x173e0
-  __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__const: 0x21a0
+  __TEXT.__objc_methname: 0x240c8
+  __TEXT.__objc_methtype: 0x68f4
+  __TEXT.__objc_stubs: 0x17500
+  __DATA_CONST.__got: 0xad0
+  __DATA_CONST.__const: 0x21b0
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ed0
+  __DATA_CONST.__objc_selrefs: 0x80e8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x6a8
-  __AUTH_CONST.__auth_got: 0x1808
+  __AUTH_CONST.__auth_got: 0x1840
   __AUTH_CONST.__const: 0x8198
-  __AUTH_CONST.__cfstring: 0x6540
-  __AUTH_CONST.__objc_const: 0x1ba38
+  __AUTH_CONST.__cfstring: 0x65c0
+  __AUTH_CONST.__objc_const: 0x19278
   __AUTH_CONST.__objc_floatobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__objc_doubleobj: 0x80
+  __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x3cf0
-  __DATA.__objc_ivar: 0x10ac
+  __DATA.__objc_ivar: 0x10b0
   __DATA.__data: 0x1fb8
   __DATA.__bss: 0xeb0
   __DATA.__common: 0x70

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11715
-  Symbols:   6635
-  CStrings:  9274
+  Functions: 11889
+  Symbols:   6648
+  CStrings:  9301
 
Symbols:
+ _CGBitmapContextGetColorSpace
+ _CGColorSpaceGetName
+ _CGColorSpaceIsPQBased
+ _CGContextSetEDRTargetHeadroom
+ _CGImageCreateCopyWithContentHeadroom
+ _CGImagePNGRepresentationWithProperties
+ _TSDCGContextDrawTiledImageRecordingMaxHeadroom
+ _TSDCGContextGetTonemappedHDRContentToSDR
+ _TSDCGContextMarkTonemappedHDRContentToSDR
+ _TSDCGContextSetMaxHDRHeadroom
+ _TSUColorSpaceSupportsHDR
+ _TSUHLGColorSpace
+ _kCGImagePropertyNamedColorSpace
+ _kCGImageSourceDecodeRequestOptions
+ _kCGImageSourceGenerateImageSpecificLumaScaling
+ _kCIFormatRGBAh
- _CGImageHEICRepresentationWithOrientation
- __swift_FORCE_LOAD_$_swiftFileProvider
- _kCIContextOutputColorSpace
CStrings:
+ "-[TSDInfoGeometry parentGeometryWithRelativeGeometry:parentSize:]"
+ "@32@0:8^{CGImage=}16q24"
+ "CIToneMapHeadroom"
+ "Input geometries' sizes don't match"
+ "TB,N,V_shouldOverrideHeadroom"
+ "TB,R,N,VmPreviousRenderTonemappedHDRContentToSDR"
+ "TSDCGContextInfoDictionaryKeyTonemappedHDRContentToSDR"
+ "^{CGImage=}108@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56B88^B92@?100"
+ "^{CGImage=}24@0:8^{CGImage=}16"
+ "^{CGImage=}92@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48B64N^d68^B76@?84"
+ "_shouldOverrideHeadroom"
+ "contentLanguageExporterClass"
+ "createCGImage:fromRect:format:colorSpace:"
+ "dataRepresentation"
+ "i_imageInScaledRect:withTargetIntegralSize:distortedToMatch:preservingContentHeadroom:tonemappedHDRContentToSDR:keepingChildrenPassingTest:"
+ "i_newImageInContext:bounds:integralBounds:distortedToMatch:tonemappedHDRContentToSDR:keepingChildrenPassingTest:"
+ "i_regenerateThumbnailDataIfMissingButExpected"
+ "initWithName:color:width:"
+ "initWithTransformedBoundsOrigin:size:widthValid:heightValid:horizontalFlip:verticalFlip:angle:"
+ "inputSourceHeadroom"
+ "inputTargetHeadroom"
+ "mPreviousRenderTonemappedHDRContentToSDR"
+ "p_createImageByToneMappingHDRImageToSDR:"
+ "p_dataForPNGRepresentationOfImage:redrawnInHDRColorSpaceWithOrientation:"
+ "parentGeometryWithRelativeGeometry:parentSize:"
+ "previousRenderTonemappedHDRContentToSDR"
+ "rectInRootForSelectionAnchorRectOfSelectionPath:"
+ "setShouldOverrideHeadroom:"
+ "shouldOverrideHeadroom"
+ "v16@?0@\"NSMapTable\"8"
- "^{CGImage=}84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48B64N^d68@?76"
- "i_imageInScaledRect:withTargetIntegralSize:distortedToMatch:preservingContentHeadroom:keepingChildrenPassingTest:"
- "serialize"
- "v16@?0@\"TSUPointerKeyDictionary\"8"

```

## asktod

> `/usr/libexec/asktod`

```diff

-23.4.0.0.0
-  __TEXT.__text: 0x30f70
-  __TEXT.__auth_stubs: 0x12b0
+23.7.0.0.0
+  __TEXT.__text: 0x32dac
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_methlist: 0x58
   __TEXT.__const: 0xf28
-  __TEXT.__cstring: 0x358c
-  __TEXT.__objc_methname: 0xd56
+  __TEXT.__cstring: 0x37fc
+  __TEXT.__objc_methname: 0xd9a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x77
   __TEXT.__objc_methtype: 0x936
-  __TEXT.__constg_swiftt: 0x970
-  __TEXT.__swift5_typeref: 0xc01
+  __TEXT.__constg_swiftt: 0x988
+  __TEXT.__swift5_typeref: 0xc17
   __TEXT.__swift5_reflstr: 0x7fd
   __TEXT.__swift5_fieldmd: 0x748
   __TEXT.__swift5_capture: 0x278

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x990
+  __TEXT.__unwind_info: 0x9b8
   __TEXT.__eh_frame: 0x1338
-  __DATA_CONST.__auth_got: 0x958
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x18c0
+  __DATA_CONST.__const: 0x18d0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_classrefs: 0xb0
   __DATA.__objc_const: 0x1520
-  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_selrefs: 0x210
   __DATA.__objc_data: 0x210
-  __DATA.__data: 0x1368
+  __DATA.__data: 0x1398
   __DATA.__common: 0xe8
   __DATA.__bss: 0x1200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 814
-  Symbols:   462
-  CStrings:  479
+  Functions: 824
+  Symbols:   488
+  CStrings:  494
 
Symbols:
+ _$s10Foundation12URLQueryItemV4name5valueACSSh_SSSghtcfC
+ _$s10Foundation12URLQueryItemVMa
+ _$s10Foundation12URLQueryItemVMn
+ _$s10Foundation13URLComponentsV10queryItemsSayAA12URLQueryItemVGSgvg
+ _$s10Foundation13URLComponentsV10queryItemsSayAA12URLQueryItemVGSgvs
+ _$s10Foundation13URLComponentsV3url23resolvingAgainstBaseURLACSgAA0G0Vh_SbtcfC
+ _$s10Foundation13URLComponentsV3urlAA3URLVSgvg
+ _$s10Foundation13URLComponentsVMa
+ _$s10Foundation13URLComponentsVMn
+ _$s10Foundation4DataV15_RepresentationON
+ _$s9AskToCore12IconProviderV017associatedContentD03forAA0D0VAA9ATPayloadC_tF
+ _$s9AskToCore12IconProviderV06clientD03for7isBadgeAA0D0VAA9ATPayloadC_SbtF
+ _$s9AskToCore12IconProviderVACycfC
+ _$s9AskToCore12IconProviderVMa
+ _$s9AskToCore4IconV5imageSo10CGImageRefavg
+ _$s9AskToCore4IconV7isBlankSbvg
+ _$s9AskToCore4IconVMa
+ _$sSo6NSDataC10FoundationE10startIndexSivg
+ _$sSo6NSDataC10FoundationE8endIndexSivg
+ _CFDataCreateMutable
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithData
+ _CGImageDestinationFinalize
+ _kUTTypePNG
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
CStrings:
+ "Attempting to add icon image data to base URL"
+ "CFDataCreateMutable failed"
+ "CGImageDestinationCreateWithData failed"
+ "CGImageDestinationFinalize failed"
+ "Division by zero"
+ "Division results in an overflow"
+ "Icon image data is %ld bytes"
+ "Sending message of %ld bytes to %s"
+ "Swift/IntegerTypes.swift"
+ "Tried adding an icon to a URL, but the given URL was nil"
+ "Tried adding associatedContentIcon data to the URL, but the icon data was nil"
+ "Tried adding clientIcon data to the URL, but the icon data was nil"
+ "base64EncodedStringWithOptions:"
+ "compressedDataUsingAlgorithm:error:"
+ "cornerRadiusIncludedInThumbnailData"

```

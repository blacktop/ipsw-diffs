## ThumbnailExtensionSecure

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/PlugIns/ThumbnailExtensionSecure.appex/ThumbnailExtensionSecure`

```diff

-186.4.1.0.0
-  __TEXT.__text: 0x1cd4
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x780
+186.5.3.0.0
+  __TEXT.__text: 0x2850
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x78
-  __TEXT.__objc_methname: 0x650
-  __TEXT.__oslogstring: 0xf3
+  __TEXT.__objc_methname: 0x6ba
+  __TEXT.__oslogstring: 0x2e7
   __TEXT.__cstring: 0x46
   __TEXT.__objc_classname: 0x30
-  __TEXT.__objc_methtype: 0xb8
-  __TEXT.__unwind_info: 0xe4
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x90
+  __TEXT.__objc_methtype: 0xc7
+  __TEXT.__unwind_info: 0xf4
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_selrefs: 0x230
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x9

   - /System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 29
-  Symbols:   113
-  CStrings:  89
+  Functions: 42
+  Symbols:   127
+  CStrings:  105
 
Symbols:
+ _AVMediaTypeVideo
+ _CGAffineTransformInvert
+ _CGRectApplyAffineTransform
+ _NSStringFromCGAffineTransform
+ _NSStringFromCGSize
+ _NSUnderlyingErrorKey
+ _QLDetermineSizeRespectingAspectRatioAndMinimumDimension
+ _QLThumbnailingImageIOCreateCroppedAndScaledThumbnailToSatisfyConstraints
+ _objc_enumerationMutation
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retain_x25
+ _objc_retain_x27
CStrings:
+ "%@: successfully generated movie thumbnail using AVAssetImageGenerator"
+ "@32@0:8@16^@24"
+ "Could not determine content type of %@: %@"
+ "Could not get content type for %@ (request: %@)"
+ "Could not read attributed string for request %@, error %@"
+ "Final size %{public}@"
+ "Generating thumbnail for %@. itemType = %lu"
+ "No video track in %@"
+ "Request %@: failed to generate image from movie data: %{public}@"
+ "Thumbnails of type %lu are not handled by this extension (request: %@)"
+ "Track dimensions %.0f %.0f, transform %{public}@"
+ "Transformed natural size %{public}@"
+ "countByEnumeratingWithState:objects:count:"
+ "mediaType"
+ "mutableAttributedStringForThumbnailWithURL:documentAttributes:error:"
+ "naturalSize"
+ "preferredTransform"
+ "replyForText:error:"
+ "tracks"
- "Generating thumbnail for %@"
- "mutableAttributedStringForThumbnailWithURL:documentAttributes:"
- "replyForText:"

```

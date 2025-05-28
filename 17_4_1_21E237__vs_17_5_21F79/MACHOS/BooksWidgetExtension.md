## BooksWidgetExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension`

```diff

-6040.0.0.0.0
-  __TEXT.__text: 0x7d890
-  __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x74
+6070.12.1.0.0
+  __TEXT.__text: 0x7ec80
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__const: 0x30a4
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x1dd9
-  __TEXT.__objc_methname: 0x79f
-  __TEXT.__oslogstring: 0x170
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methtype: 0xfa
-  __TEXT.__constg_swiftt: 0x1418
-  __TEXT.__swift5_typeref: 0x912c
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x166b
-  __TEXT.__swift5_fieldmd: 0x1608
+  __TEXT.__cstring: 0x1ef9
+  __TEXT.__constg_swiftt: 0x1448
+  __TEXT.__swift5_typeref: 0x915a
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x168b
+  __TEXT.__swift5_fieldmd: 0x163c
   __TEXT.__swift5_assocty: 0x4d8
-  __TEXT.__swift5_capture: 0xfc
+  __TEXT.__swift5_capture: 0x120
+  __TEXT.__objc_methname: 0x556
   __TEXT.__swift5_proto: 0x1d0
-  __TEXT.__swift5_types: 0x178
+  __TEXT.__swift5_types: 0x17c
+  __TEXT.__objc_classname: 0x40
+  __TEXT.__objc_methtype: 0x72
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x24a0
-  __TEXT.__eh_frame: 0xcbc
-  __DATA_CONST.__auth_got: 0xe78
+  __TEXT.__unwind_info: 0x24c4
+  __TEXT.__eh_frame: 0xd0c
+  __DATA_CONST.__auth_got: 0xe18
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x138
-  __DATA_CONST.__const: 0x4350
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x43b0
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4a8
-  __DATA.__objc_selrefs: 0x2b8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x3110
+  __DATA.__objc_const: 0x368
+  __DATA.__objc_selrefs: 0x230
+  __DATA.__data: 0x30b8
   __DATA.__bss: 0x3878
-  __DATA.__common: 0xa8
+  __DATA.__common: 0xb0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/BKAudiobooks.framework/BKAudiobooks
   - @rpath/BookCore.framework/BookCore
-  Functions: 2231
-  Symbols:   220
-  CStrings:  267
+  Functions: 2230
+  Symbols:   201
+  CStrings:  233
 
Symbols:
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ __Block_copy
+ __Block_release
+ __swift_stdlib_bridgeErrorToNSError
+ _swift_isEscapingClosureAtFileLocation
- _BKLibraryLog
- _CGSizeScaleToScreen
- _OBJC_CLASS_$_BKAssetCoverImageHelper
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSObject
- _OBJC_METACLASS_$_BKAssetCoverImageHelper
- _OBJC_METACLASS_$_NSObject
- __Unwind_Resume
- ___CFConstantStringClassReference
- ___objc_personality_v0
- __os_log_error_impl
- _mainScreenScaleFactor
- _objc_alloc
- _objc_claimAutoreleasedReturnValue
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSendSuper2
- _objc_opt_respondsToSelector
- _objc_retainBlock
- _objc_retain_x2
- _objc_retain_x3
- _objc_storeStrong
CStrings:
+ "Could not check image existence due to url construction failure. (assetID: '%s', type: %s). error: %@"
+ "Could not construct url. (assetID: '%s', type: %s). error: %@"
+ "Creating caches directory for cover at %s"
+ "Failed to cache untreated cover for asset: %s, error: %@"
+ "Failed to delete cached image file (assetID: '%s', type: %s), error: %@"
+ "Received raw store audiobook cover for %s of size %s"
+ "drawInRect:"
+ "imageWithActions:"
+ "initWithSize:"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
- "\x02"
- ".cxx_destruct"
- "@\"AEPluginRegistry\""
- "@\"QLThumbnailGenerator\""
- "@16@0:8"
- "@32@0:8@16@24"
- "BKAssetCoverImageDomain"
- "BKAssetCoverImageHelper"
- "BKAssetCoverImageHelper: Failed to get image because URL is nil"
- "BKAssetCoverImageHelping"
- "Creating caches directory for cover"
- "Failed to create a cover directory in Library/Caches: %@"
- "T@\"AEPluginRegistry\",R,N,V_pluginRegistry"
- "T@\"QLThumbnailGenerator\",R,N,V_thumbnailGenerator"
- "Unable to get cover image from ImageIO for url %{mask.hash}@ (error: %@), giving up"
- "Unable to get cover image from QuickLook for url %{mask.hash}@ (error: %@), falling back on plugin registry..."
- "Unable to get cover image from plugin registry for url %{mask.hash}@ (error: %@), falling back on ImageIO..."
- "_helper:coverImageWithCompletion:"
- "_imageIOCoverImageFromURL:completion:"
- "_pluginRegistry"
- "_pluginRegistryCoverImageFromURL:completion:"
- "_thumbnailGenerator"
- "_thumbnailGeneratorCoverImageFromURL:completion:"
- "coverImageFromURL:completion:"
- "dataWithContentsOfURL:"
- "epub"
- "errorWithDomain:code:userInfo:"
- "helperCoverImage"
- "helperCoverImageWithCompletion:"
- "helperForURL:withOptions:"
- "imageWithData:"
- "initWithThumbnailGenerator:pluginRegistry:"
- "isEqualToString:"
- "lowercaseString"
- "path"
- "pathExtension"
- "pluginForURL:"
- "pluginRegistry"
- "thumbnailGenerator"
- "v16@0:8"
- "v16@?0@\"UIImage\"8"
- "v24@?0@\"UIImage\"8@\"NSError\"16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"UIImage\"@\"NSError\">24"
- "v32@0:8@16@?24"

```

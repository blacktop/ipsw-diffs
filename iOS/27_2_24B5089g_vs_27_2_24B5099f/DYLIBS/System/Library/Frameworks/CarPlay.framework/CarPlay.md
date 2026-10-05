## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-552.3.0.0.0
-  __TEXT.__text: 0x6d23c
-  __TEXT.__objc_methlist: 0x9a30
-  __TEXT.__const: 0x552
-  __TEXT.__cstring: 0x5ae6
-  __TEXT.__oslogstring: 0x3726
+552.6.2.0.0
+  __TEXT.__text: 0x6e160
+  __TEXT.__objc_methlist: 0x9b48
+  __TEXT.__const: 0x562
+  __TEXT.__cstring: 0x5be6
+  __TEXT.__oslogstring: 0x3786
   __TEXT.__gcc_except_tab: 0x934
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x27e8
+  __TEXT.__unwind_info: 0x2820
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f00
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__const: 0x1f50
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43e0
-  __DATA_CONST.__objc_protorefs: 0x160
-  __DATA_CONST.__objc_superrefs: 0x348
+  __DATA_CONST.__objc_selrefs: 0x4448
+  __DATA_CONST.__objc_protorefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__got: 0x878
   __AUTH_CONST.__const: 0xbe8
-  __AUTH_CONST.__cfstring: 0x57a0
-  __AUTH_CONST.__objc_const: 0x21650
+  __AUTH_CONST.__cfstring: 0x5840
+  __AUTH_CONST.__objc_const: 0x218a0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xa34
+  __AUTH.__objc_data: 0x98
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x2110
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2698

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3380
-  Symbols:   6354
-  CStrings:  1111
+  Functions: 3401
+  Symbols:   6397
+  CStrings:  1120
 
Symbols:
+ +[CPListImageRowItemCardElement _setImageSizeForAspectRatioWide:portrait:square:]
+ +[CPListImageRowItemCardElement _setMaximumImageSize:maximumFullHeightImageSize:]
+ +[CPPlaybackItemIdentifier supportsSecureCoding]
+ -[CPListTemplate _playableItemForMatchingIdentifier:]
+ -[CPListTemplate listTemplateWithIdentifier:requestPlaybackConfirmationForMatchingIdentifier:completionHandler:]
+ -[CPPlaybackConfiguration .cxx_destruct]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackAction:elapsedTime:duration:requiresPlaybackConfirmation:]
+ -[CPPlaybackConfiguration playbackConfirmationBlock]
+ -[CPPlaybackConfiguration requiresPlaybackConfirmation]
+ -[CPPlaybackConfiguration setPlaybackConfirmationBlock:]
+ -[CPPlaybackItemIdentifier .cxx_destruct]
+ -[CPPlaybackItemIdentifier elementIndex]
+ -[CPPlaybackItemIdentifier encodeWithCoder:]
+ -[CPPlaybackItemIdentifier identifier]
+ -[CPPlaybackItemIdentifier initWithCoder:]
+ -[CPPlaybackItemIdentifier initWithIdentifier:]
+ -[CPPlaybackItemIdentifier initWithIdentifier:elementIndex:]
+ GCC_except_table135
+ _CPBarButtonMaximumImageSize
+ _CPBarButtonSanitizedImage
+ _OBJC_CLASS_$_CPPlaybackItemIdentifier
+ _OBJC_IVAR_$_CPPlaybackConfiguration._playbackConfirmationBlock
+ _OBJC_IVAR_$_CPPlaybackConfiguration._requiresPlaybackConfirmation
+ _OBJC_IVAR_$_CPPlaybackItemIdentifier._elementIndex
+ _OBJC_IVAR_$_CPPlaybackItemIdentifier._identifier
+ _OBJC_METACLASS_$_CPPlaybackItemIdentifier
+ __OBJC_$_CLASS_METHODS_CPPlaybackItemIdentifier
+ __OBJC_$_CLASS_PROP_LIST_CPPlaybackItemIdentifier
+ __OBJC_$_INSTANCE_METHODS_CPPlaybackItemIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_CPPlaybackItemIdentifier
+ __OBJC_$_PROP_LIST_CPPlaybackItemIdentifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPListClientTemplateDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPPlaybackItemIdentifier
+ __OBJC_CLASS_RO_$_CPPlaybackItemIdentifier
+ __OBJC_METACLASS_RO_$_CPPlaybackItemIdentifier
+ __OBJC_PROTOCOL_REFERENCE_$_CPPlayableItem
+ ___112-[CPListTemplate listTemplateWithIdentifier:requestPlaybackConfirmationForMatchingIdentifier:completionHandler:]_block_invoke
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_10
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_9
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSValue"8"NSValue"16ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSValue"8"NSValue"16"NSValue"24ls32l8
+ __maximumFullHeightImageSize
+ __maximumImageSizeForAspectRatioPortrait
+ __maximumImageSizeForAspectRatioSquare
+ __maximumImageSizeForAspectRatioWide
- GCC_except_table133
- GCC_except_table74
CStrings:
+ "%@ requesting playback confirmation for %{public}@"
+ "Failed to identify a local playable item for %@ %lu"
+ "kCPDarkContentImageKey"
+ "kCPLightContentImageKey"
+ "kCPPlaybackConfigurationRequiresPlaybackConfirmationKey"
+ "kCPPlaybackItemIdentifierElementIndexKey"
+ "kCPPlaybackItemIdentifierIdentifierKey"
+ "v24@?0@\"NSValue\"8@\"NSValue\"16"
+ "v32@?0@\"NSValue\"8@\"NSValue\"16@\"NSValue\"24"
```

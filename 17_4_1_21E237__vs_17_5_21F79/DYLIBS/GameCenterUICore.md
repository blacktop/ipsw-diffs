## GameCenterUICore

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore`

```diff

-818.4.37.2.1
-  __TEXT.__text: 0x26074
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x21f0
+818.5.11.2.2
+  __TEXT.__text: 0x25f04
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x21f8
   __TEXT.__const: 0x4b4
-  __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x3100
-  __TEXT.__oslogstring: 0x1b96
+  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__cstring: 0x3080
+  __TEXT.__oslogstring: 0x1c10
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_typeref: 0x114

   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0xa20
+  __TEXT.__unwind_info: 0xa38
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x41e
-  __TEXT.__objc_methname: 0x6e00
-  __TEXT.__objc_methtype: 0xe94
-  __TEXT.__objc_stubs: 0x5460
+  __TEXT.__objc_methname: 0x6e6e
+  __TEXT.__objc_methtype: 0xe7f
+  __TEXT.__objc_stubs: 0x54e0
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xcc8
+  __DATA_CONST.__const: 0xcf0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x33c8
-  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_selrefs: 0x1e00
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x308
+  __DATA_CONST.__objc_classrefs: 0x310
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__cfstring: 0x1160
   __AUTH_CONST.__objc_const: 0x12e8
   __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x160

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1055
-  Symbols:   3459
+  Symbols:   3464
   CStrings:  1825
 
Symbols:
+ +[UIImage(GKAdditions) _gkImageWithCheckedData:]
+ +[UIImage(GKAdditions) _gkImageWithCheckedData:scale:]
+ -[GKLocalPlayer(Onboarding) shouldShowAnyOnboardingScreenForBundleIdentifier:]
+ GCC_except_table13
+ _GKNewsAppIdentifier
+ _GKNewsGameCenterTesterIdentifier
+ _OBJC_CLASS_$_GKImageRestrictions
+ ___block_descriptor_48_e8_32bs40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e14_v16?0?<v?>8ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r48r_e11_v16?0B8B12lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e14_v16?0?<v?>8ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e5_v8?0lr40l8r48l8r56l8s32l8
+ _objc_msgSend$_gkImageWithCheckedData:
+ _objc_msgSend$_gkImageWithCheckedData:scale:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$cgImageForGamesWithData:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$shouldShowAnyOnboardingScreenForBundleIdentifier:
+ _objc_msgSend$suppressLoginSheet
- +[UIImage(GKAdditions) _gkCGImageWithPNGData:]
- +[UIImage(GKAdditions) _gkImageWithPNGData:]
- +[UIImage(GKAdditions) _gkImageWithPNGData:scale:]
- _CGImageSourceCreateImageAtIndex
- _CGImageSourceCreateWithData
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e11_v16?0B8B12ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___kCFBooleanTrue
- _kCGImageSourceTypeIdentifierHint
- _objc_msgSend$_gkCGImageWithPNGData:
- _objc_msgSend$_gkImageWithPNGData:
- _objc_msgSend$_gkImageWithPNGData:scale:
- _objc_msgSend$dictionary
CStrings:
+ "_gkImageWithCheckedData:"
+ "_gkImageWithCheckedData:scale:"
+ "_handleAuthResponse: Suppress login sheet"
+ "bundleIdentifier"
+ "cgImageForGamesWithData:"
+ "containsObject:"
+ "mainBundle"
+ "shouldShowAnyOnboardingScreen? NO (Skipping residual onboarding flow for News.)"
+ "shouldShowAnyOnboardingScreenForBundleIdentifier:"
+ "suppressLoginSheet"
- "^{CGImage=}24@0:8@16"
- "_gkCGImageWithPNGData:"
- "_gkImageWithPNGData:"
- "_gkImageWithPNGData:scale:"
- "dictionary"
- "image.png"
- "kCGImageSourceFailForDataNotMatchingHint"

```

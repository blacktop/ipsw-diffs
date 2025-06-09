## IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent`

```diff

-1402.600.41.2.8
-  __TEXT.__text: 0x17560
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0xa5c
+1436.100.6.2.12
+  __TEXT.__text: 0x16efc
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0xa4c
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x1c70
-  __TEXT.__cstring: 0xb53
-  __TEXT.__oslogstring: 0x267e
-  __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__gcc_except_tab: 0x1bfc
+  __TEXT.__cstring: 0xad2
+  __TEXT.__oslogstring: 0x25b6
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x13f
-  __TEXT.__objc_methname: 0x3149
-  __TEXT.__objc_methtype: 0xb2f
+  __TEXT.__objc_methname: 0x31c9
+  __TEXT.__objc_methtype: 0xb39
   __TEXT.__objc_stubs: 0x2cc0
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0xd40
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xd60
+  __AUTH_CONST.__cfstring: 0xd20
   __AUTH_CONST.__objc_const: 0xda0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x188
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices
   - /System/Library/PrivateFrameworks/Marco.framework/Marco
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87215D23-A89C-3BA3-AC96-FE18F89DFBC6
-  Functions: 255
-  Symbols:   265
-  CStrings:  1026
+  UUID: 4BB6B183-61D7-379C-95EB-76A05CB207EC
+  Functions: 248
+  Symbols:   260
+  CStrings:  1013
 
Symbols:
+ _OBJC_CLASS_$_IMCommSafetyUIUtilities
+ _OBJC_CLASS_$_IMNicknameAvatarRecipe
+ _OBJC_CLASS_$_MMCSUtilities
- __IMAlwaysLog
- __IMWillLog
- __sl_dlopen
- _abort_report_np
- _failReasonStringForMMCSError
- _free
- _objc_getClass
- _parseMMCSError
CStrings:
+ "@64@0:8@16^@24^@32^@40^@48^@56"
+ "@88@0:8@16@24@32@40@48@56@64B72B76^@80"
+ "Completed nickname parsing (hasImage: %i, hasWallpaper: %i, hasLowResWallpaper: %i, hasAvatarRecipe: %i) from public record: %@"
+ "Wallpaper | encryptedAvatarRecipeData: %@"
+ "_blastdoorNicknameFromPublicRecord:wallpaperRecord:preKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:knownSender:shouldDecodeImageFields:error:"
+ "ard"
+ "avatarRecipe"
+ "avatarRecipeDataTag"
+ "failReasonStringForMMCSError:"
+ "generateNickname:senderContext:forRecordID:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:withKey:processImageFields:completionBlock:"
+ "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:knownSender:shouldDecodeImageFields:queue:completionBlock:"
+ "initWithData:"
+ "initWithFirstName:lastName:avatar:pronouns:wallpaper:avatarRecipe:"
+ "isSwiftUIAvatarRenderingEnabled"
+ "nicknameFromPublicRecord:wallpaperRecord:preKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:avatarRecipeDataTag:knownSender:shouldDecodeImageFields:error:"
+ "parseMMCSError:"
+ "posterImageURLForPosterConfigurationAtURL:"
+ "publicRecordsForNicknameWithPreKey:wallpaperDataTag:lowResWallpaperDataTag:wallpaperMetadataTag:avatarRecipeDataTag:error:"
+ "recipeData"
+ "v76@?0B8@\"IMNickname\"12@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44@\"NSData\"52@\"NSData\"60@\"NSError\"68"
+ "v88@0:8@16@24@32@40@48@56B64B68@72@?80"
- "%@B"
- "%s"
- "@56@0:8@16^@24^@32^@40^@48"
- "@80@0:8@16@24@32@40@48@56B64B68^@72"
- "Completed nickname parsing (hasImage: %i, hasWallpaper: %i, hasLowResWallpaper: %i) from public record: %@"
- "Expected the poster config to have exactly one media"
- "Failed to generate a poster config. Error: %@"
- "Given nil for the poster url, bailing."
- "PFPosterConfiguration"
- "PRSPosterArchiver"
- "Poster is not a photo, stop trying to get an image URL. Config bundle ID: %@"
- "Receiving file transfer failed: %@    error: %@"
- "Unable to find class %s"
- "Upload token handled response dictionary %@"
- "_blastdoorNicknameFromPublicRecord:wallpaperRecord:preKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:knownSender:shouldDecodeImageFields:error:"
- "_getImageURLForPosterDataAt:"
- "assetDirectory"
- "generateNickname:senderContext:forRecordID:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:withKey:processImageFields:completionBlock:"
- "getNicknameWithRecordID:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:knownSender:shouldDecodeImageFields:queue:completionBlock:"
- "initWithFirstName:lastName:avatar:pronouns:wallpaper:"
- "loadFromURL:error:"
- "media"
- "nicknameFromPublicRecord:wallpaperRecord:preKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:knownSender:shouldDecodeImageFields:error:"
- "output.layerStack/portrait-layer_background.HEIC"
- "providerBundleIdentifier"
- "publicRecordsForNicknameWithPreKey:wallpaperDataTag:lowResWallpaperDataTag:wallpaperMetadataTag:error:"
- "softlink:r:path:/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats"
- "softlink:r:path:/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices"
- "subpath"
- "unarchiveConfigurationAtURL:format:error:"
- "v68@?0B8@\"IMNickname\"12@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44@\"NSData\"52@\"NSError\"60"
- "v80@0:8@16@24@32@40@48B56B60@64@?72"

```

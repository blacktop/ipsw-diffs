## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0x1d1e0
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0x3f80
-  __TEXT.__objc_methlist: 0x196c
+750.11.101.0.0
+  __TEXT.__text: 0x1d6d4
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_stubs: 0x3fc0
+  __TEXT.__objc_methlist: 0x1eb8
   __TEXT.__const: 0xa0
   __TEXT.__objc_classname: 0x2ad
-  __TEXT.__objc_methname: 0x4b52
+  __TEXT.__objc_methname: 0x4b76
   __TEXT.__objc_methtype: 0xaad
   __TEXT.__oslogstring: 0x635
-  __TEXT.__cstring: 0x6386
+  __TEXT.__cstring: 0x6392
   __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__unwind_info: 0x6a8
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x2b8
+  __TEXT.__unwind_info: 0x6f0
+  __DATA_CONST.__auth_got: 0x790
+  __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xbd0
   __DATA_CONST.__cfstring: 0x5be0

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_const: 0x33f0
-  __DATA.__objc_selrefs: 0x1280
+  __DATA.__objc_const: 0x2a38
+  __DATA.__objc_selrefs: 0x1368
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x558

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 661
-  Symbols:   381
+  Functions: 683
+  Symbols:   384
   CStrings:  1965
 
Symbols:
+ _ACAccountDataclassCloudPhotos
+ _ACAccountDataclassImagePlayground
+ _ACAccountDataclassMediaStream
+ _ACAccountDataclassSharedStreams
+ _CPLAppBundleIdentifierForContainerIdentifier
+ _OBJC_CLASS_$_CPLScopeChange
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_CPLLibraryInfo
- _kAccountDataclassCloudPhotos
- _kAccountDataclassMediaStream
- _kAccountDataclassSharedStreams
- _objc_retain_x28
CStrings:
+ "/var/mobile/Media/PhotoData/Caches/GraphService/PromptSuggestionsAnalytics.plist"
+ "URL"
+ "filterScopeChange"
+ "internal/storydiagnostics/"
+ "previewImageData"
+ "setPreviewImageData:"
+ "setThumbnailImageData:"
+ "setURL:"
+ "share"
+ "thumbnailImageData"
+ "update scopes set scopeChange = filterScopeChange(scopeChange)"
+ "update scopes set scopeChange = null"
- "-h"
- "-v"
- "/var/mobile/Media/PhotoData/internal/storydiagnostics"
- "com.apple.Dataclass.ImagePlayground"
- "filterLibraryInfo"
- "momentShare"
- "previewData"
- "setPreviewData:"
- "setShareURL:"
- "shareURL"
- "update scopes set libraryInfo = filterLibraryInfo(libraryInfo)"
- "update scopes set libraryInfo = null"

```

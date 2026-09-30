## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/XPCServices/com.apple.Photos.CPLDiagnose.xpc/Contents/MacOS/com.apple.Photos.CPLDiagnose`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x22698
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x40e0
-  __TEXT.__objc_methlist: 0x19a4
+751.0.104.0.0
+  __TEXT.__text: 0x22ce8
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0x4140
+  __TEXT.__objc_methlist: 0x1f00
   __TEXT.__const: 0xc8
   __TEXT.__objc_classname: 0x2b0
-  __TEXT.__objc_methname: 0x4c92
+  __TEXT.__objc_methname: 0x4cd3
   __TEXT.__objc_methtype: 0xaf3
   __TEXT.__oslogstring: 0x7e4
-  __TEXT.__cstring: 0x5dbb
-  __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__unwind_info: 0x738
-  __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x2b8
+  __TEXT.__cstring: 0x5f52
+  __TEXT.__gcc_except_tab: 0x684
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xe38
-  __DATA_CONST.__cfstring: 0x56c0
+  __DATA_CONST.__cfstring: 0x5700
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x140
+  __DATA_CONST.__objc_arraydata: 0x160
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA.__objc_const: 0x34e0
-  __DATA.__objc_selrefs: 0x12d8
+  __DATA.__objc_const: 0x2b28
+  __DATA.__objc_selrefs: 0x13b8
   __DATA.__objc_ivar: 0x220
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x558

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 1AE28228-1112-3578-B1E0-906F541812EB
-  Functions: 738
-  Symbols:   368
-  CStrings:  2638
+  UUID: 65201AC4-7858-3BEB-A433-8CAC53CE8DCA
+  Functions: 760
+  Symbols:   371
+  CStrings:  2650
 
Symbols:
+ _ACAccountDataclassCloudPhotos
+ _ACAccountDataclassImagePlayground
+ _ACAccountDataclassMediaStream
+ _ACAccountDataclassSharedStreams
+ _CPLAppBundleIdentifierForContainerIdentifier
+ _OBJC_CLASS_$_CPLScopeChange
+ _objc_opt_respondsToSelector
- _OBJC_CLASS_$_CPLLibraryInfo
- _kAccountDataclassCloudPhotos
- _kAccountDataclassMediaStream
- _kAccountDataclassSharedStreams
CStrings:
+ "  removing embedding data from %@"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLDaemonProcessProtocol.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLEngineParameters.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Tools/cplctl-support/CPLPhotosDaemon.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Tools/cplctl/CPLCTLCommand.m"
+ "UPDATE Results SET results=null WHERE resultsType=28"
+ "UPDATE Results SET results=null WHERE resultsType=46"
+ "UPDATE Results SET results=null WHERE resultsType=73"
+ "UPDATE Results SET results=null WHERE resultsType=74"
+ "UPDATE Results SET results=null WHERE resultsType=78"
+ "UPDATE Results SET results=null WHERE resultsType=79"
+ "UPDATE Results SET results=null WHERE resultsType=82"
+ "URL"
+ "collectStoryDiagnosticsFiles"
+ "filterScopeChange"
+ "internal/storydiagnostics/"
+ "mediaanalysis.db"
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
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLDaemonProcessProtocol.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Daemon/CPLEngineParameters.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Tools/cplctl-support/CPLPhotosDaemon.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Tools/cplctl/CPLCTLCommand.m"
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

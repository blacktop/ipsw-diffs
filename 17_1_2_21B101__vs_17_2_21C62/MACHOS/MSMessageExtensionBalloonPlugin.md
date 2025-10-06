## MSMessageExtensionBalloonPlugin

> `/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0x25258
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x54c0
-  __TEXT.__objc_methlist: 0x1864
-  __TEXT.__const: 0xf6
-  __TEXT.__gcc_except_tab: 0x6b0
-  __TEXT.__objc_methname: 0x6b32
-  __TEXT.__cstring: 0x235f
-  __TEXT.__oslogstring: 0x2147
-  __TEXT.__objc_classname: 0x428
-  __TEXT.__objc_methtype: 0x16f5
-  __TEXT.__dlopen_cstrs: 0x260
+1262.300.81.2.13
+  __TEXT.__text: 0x1e260
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x54e0
+  __TEXT.__objc_methlist: 0x187c
+  __TEXT.__const: 0xe6
+  __TEXT.__gcc_except_tab: 0x538
+  __TEXT.__objc_methname: 0x6b92
+  __TEXT.__cstring: 0x12af
+  __TEXT.__oslogstring: 0x25f5
+  __TEXT.__objc_classname: 0x427
+  __TEXT.__objc_methtype: 0x177f
   __TEXT.__swift5_typeref: 0x66
   __TEXT.__swift5_capture: 0x30
   __TEXT.__constg_swiftt: 0x120
   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xa4c
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__cfstring: 0xaa0
+  __TEXT.__unwind_info: 0x7f4
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__cfstring: 0x800
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3e28
-  __DATA.__objc_selrefs: 0x1a80
+  __DATA.__objc_const: 0x3e48
+  __DATA.__objc_selrefs: 0x1a90
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x260
+  __DATA.__objc_classrefs: 0x2b0
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x838
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  UUID: 6D762FF1-F238-359B-BFE4-86CC66E42D1E
-  Functions: 906
-  Symbols:   322
-  CStrings:  1706
+  UUID: B046109F-651B-3257-BA88-690512A4812D
+  Functions: 713
+  Symbols:   339
+  CStrings:  1638
 
Symbols:
+ _CKApplicationStateResumeFromInActiveNotification
+ _CKBalloonPluginManagerSnapshotsDidChange
+ _CKBrowserSnapshotPreviewURL
+ _CKFreeSpaceWriteDataToURL
+ _CKIsRunningInCameraAppsClient
+ _CKIsRunningInCarousel
+ _CKIsRunningInFullCKClient
+ _CKIsRunningInMacCatalyst
+ _CKIsRunningInUserGeneratedStickersExtension
+ _CKMessageExtensionBrowserViewControllerDidPrepareForDisplay
+ _CKRemoteViewFailedInstantiationNotification
+ _CKRemoteViewPluginKey
+ _CKShouldShowSURF
+ _IMOSLoggingEnabled
+ _OBJC_CLASS_$_CKAnimatedImage
+ _OBJC_CLASS_$_CKApplicationState
+ _OBJC_CLASS_$_CKBalloonPluginManager
+ _OBJC_CLASS_$_CKBrowserItemPayload
+ _OBJC_CLASS_$_CKConversationList
+ _OBJC_CLASS_$_CKImageData
+ _OBJC_CLASS_$_CKPluginExtensionStateObserver
+ _OBJC_CLASS_$_CKSnapshotCacheKey
+ _OBJC_CLASS_$_CKSnapshotUtilities
+ _OBJC_CLASS_$_CKUIBehavior
+ _OSLogHandleForIMFoundationCategory
- _NSStringFromClass
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
- _free
- _objc_getClass
- _objc_retainAutorelease
CStrings:
+ "LiveBubble. ApplicationState is background and not resuming. messageGUID: %@"
+ "LiveBubble. Calling createRemoteBalloonViewControllerIsResuming: from _handleApplicationStateResumeFromInActive:."
+ "LiveBubble. Calling createRemoteBalloonViewControllerIsResuming: from initWithDataSource:."
+ "LiveBubble. Calling createRemoteBalloonViewControllerIsResuming: from reloadRemoteViewIsResuming:."
+ "LiveBubble. Calling createRemoteBalloonViewControllerIsResuming: from viewDidAppear:."
+ "LiveBubble. Extension will be used to create remote balloon view controller with identifier: %@"
+ "LiveBubble. Plugin extension loaded. bundleID: %@"
+ "LiveBubble. Plugin should not be shown for specified recipients. messageGUID: %@"
+ "LiveBubble. View has not yet been added to a window when trying to set the remote balloon view."
+ "Warning"
+ "_addStickerToStoreWithRepresentations:sourceRect:effect:completion:"
+ "adamID"
+ "clearAllStagedPluginPackages"
+ "com.cobra.cobiarrows.Archery-Extension"
+ "com.cobra.cobidarts.Extension"
+ "com.cobra.cobigolfshots.Extension"
+ "com.cobra.cobihoops.ext"
+ "com.cobra.cobishoot.Extension"
+ "setIsInTranscript:"
+ "v72@0:8@\"NSArray\"16{CGRect={CGPoint=dd}{CGSize=dd}}24q56@?<v@?@\"NSArray\"@\"NSError\">64"
+ "v72@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56@?64"
- "+[MSMessageExtensionDataSource pluginPayloadFromMediaPayload:]"
- "-[MSMessageExtensionBalloonLiveView initWithFrame:dataSource:fromMe:]"
- "-[MSMessageExtensionBalloonLiveView layoutSubviews]"
- "-[MSMessageExtensionBalloonLiveView mininimumSizeThatFits]"
- "-[MSMessageExtensionBalloonLiveView sizeThatFits:]"
- "-[MSMessageExtensionBalloonLiveViewController _applicationStateIsBackground]"
- "-[MSMessageExtensionBalloonLiveViewController _snapshotView]"
- "-[MSMessageExtensionBalloonLiveViewController conversationState]"
- "-[MSMessageExtensionBalloonLiveViewController initWithDataSource:fromMe:conversationID:recipients:]"
- "-[MSMessageExtensionBalloonLiveViewController requestSnapshot]_block_invoke"
- "-[MSMessageExtensionBalloonLoadingView initWithAppIcon:fromMe:]"
- "-[MSMessageExtensionBalloonLoadingView insets]"
- "-[MSMessageExtensionBalloonView initWithFrame:dataSource:fromMe:]"
- "-[MSMessageExtensionBalloonView layoutSubviews]"
- "-[MSMessageExtensionBalloonView sizeThatFits:]"
- "-[MSMessageExtensionBrowserViewController _addRemoteViewController]"
- "-[MSMessageExtensionBrowserViewController _instantiateRemoteViewControllerIfNeeded:]_block_invoke"
- "-[MSMessageExtensionBrowserViewController _postCurrentPluginBrowserViewDidPrepareForDisplay]_block_invoke"
- "-[MSMessageExtensionBrowserViewController _stageRichLink:skipShelf:completionHandler:]_block_invoke"
- "-[MSMessageExtensionBrowserViewController _startDragMediaItem:frameInRemoteView:fence:completionHandler:]_block_invoke"
- "-[MSMessageExtensionBrowserViewController _updateSnapshotForNextLaunch:]_block_invoke"
- "-[MSMessageExtensionBrowserViewController killExtensionProcess]"
- "-[MSMessageExtensionBrowserViewController saveSnapshotForBrowserViewController]"
- "-[MSMessageExtensionBrowserViewController saveSnapshotForBrowserViewController]_block_invoke_3"
- "-[MSMessageExtensionBrowserViewController showSnapshotForSize:]"
- "-[MSMessageExtensionBrowserViewController(PhotosSupport) _stageAssetArchive:skipShelf:completionHandler:]_block_invoke"
- "-[_MSRemoteBalloonViewControllerManager getRemoteViewControllerForExtension:messageIdentifier:contextIdentifier:item:connectionHandler:]"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBalloonLiveView.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBalloonLiveViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBalloonLoadingView.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBalloonView.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBrowserViewController+PhotosSupport.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionBrowserViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/MSMessageExtensionDataSource.m"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/MSMessageExtensionBalloonPlugin/_MSRemoteBalloonViewController.m"
- "CKAnimatedImage"
- "CKApplicationState"
- "CKApplicationStateResumeFromInActiveNotification"
- "CKBalloonPluginManager"
- "CKBalloonPluginManagerSnapshotsDidChange"
- "CKBrowserItemPayload"
- "CKBrowserSnapshotPreviewURL"
- "CKConversationList"
- "CKFreeSpaceWriteDataToURL"
- "CKImageData"
- "CKIsRunningInCameraAppsClient"
- "CKIsRunningInCarousel"
- "CKIsRunningInFullCKClient"
- "CKIsRunningInMacCatalyst"
- "CKIsRunningInUserGeneratedStickersExtension"
- "CKMessageExtensionBrowserViewControllerDidPrepareForDisplay"
- "CKPluginExtensionStateObserver"
- "CKRemoteViewFailedInstantiationNotification"
- "CKRemoteViewPluginKey"
- "CKShouldShowSURF"
- "CKSnapshotCacheKey"
- "CKSnapshotUtilities"
- "CKUIBehavior"
- "Failed to load weak link class: '%@': %s:%i (%s)"
- "Failed to load weak link constant: '%@': %s:%i (%s)"
- "Loaded weak linked class: '%@': %s:%i (%s)"
- "Loaded weak linked constant: '%@': %s:%i (%s)"
- "MessagesWeakLinking"
- "Unable to find class %s"
- "__ck_attributionInfo"
- "_adamID"
- "softlink:r:path:/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit"

```

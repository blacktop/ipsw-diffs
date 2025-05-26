## Messages

> `/System/Library/Frameworks/Messages.framework/Messages`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0x25a20
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x33c4
+1262.300.81.2.13
+  __TEXT.__text: 0x25798
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x343c
   __TEXT.__const: 0x338
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x1add
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__cstring: 0x19e3
   __TEXT.__oslogstring: 0xb72
-  __TEXT.__dlopen_cstrs: 0x262
-  __TEXT.__unwind_info: 0xb50
+  __TEXT.__dlopen_cstrs: 0x17e
+  __TEXT.__unwind_info: 0xb08
   __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methname: 0x9ba7
-  __TEXT.__objc_methtype: 0x28d5
-  __TEXT.__objc_stubs: 0x6600
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x618
+  __TEXT.__objc_methname: 0x9df3
+  __TEXT.__objc_methtype: 0x2974
+  __TEXT.__objc_stubs: 0x6740
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5cb8
-  __DATA_CONST.__objc_selrefs: 0x1f28
+  __DATA_CONST.__objc_const: 0x5d38
+  __DATA_CONST.__objc_selrefs: 0x1fb0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x1030
-  __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH.__objc_data: 0x820
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2e0
+  __DATA.__objc_classrefs: 0x2e8
   __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__data: 0xa70
-  __DATA.__bss: 0x128
+  __DATA.__objc_ivar: 0x344
+  __DATA.__data: 0xa68
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VisionKit.framework/VisionKit
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1292
-  Symbols:   4474
-  CStrings:  2127
+  Functions: 1291
+  Symbols:   4478
+  CStrings:  2145
 
Symbols:
+ -[MSConversation _insertSticker:skipShelf:frameInWindowCoordinates:completionHandler:]
+ -[MSConversation insertSticker:withSourceFrame:completionHandler:]
+ -[_MSMessageAppBundleContext _addStickerToStoreWithRepresentations:sourceRect:effect:completion:]
+ -[_MSMessageAppContext _addStickerToStoreWithRepresentations:sourceRect:effect:completion:]
+ -[_MSMessageAppExtensionContext _addStickerToStoreWithRepresentations:sourceRect:effect:completion:]
+ -[_MSMessageExtensionRemoteViewController _shouldRemoteViewControllerFenceOriginChanges]
+ -[_MSMessageExtensionRemoteViewController isInTranscript]
+ -[_MSMessageExtensionRemoteViewController setIsInTranscript:]
+ -[_MSMessageMediaPayload initWithIMSticker:]
+ -[_MSMessageMediaPayload initWithIMSticker:].cold.1
+ -[_MSMessageMediaPayload setStickerPositionVersion:]
+ -[_MSMessageMediaPayload stickerPositionVersion]
+ -[_MSStickerSendManager insertSticker:forceStage:frameInRemoteView:completionHandler:]
+ _IMBalloonPluginIdentifierMessageExtension
+ _IMIsRunningIniMessageAppExtension
+ _IMIsRunningIniMessageAppsViewService
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$__MSMessageExtensionRemoteViewController._isInTranscript
+ _OBJC_IVAR_$__MSMessageMediaPayload._stickerPositionVersion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IMAnimationTimerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IMAnimationTimerObserver
+ __OBJC_$_PROTOCOL_REFS_IMAnimationTimerObserver
+ __OBJC_LABEL_PROTOCOL_$_IMAnimationTimerObserver
+ __OBJC_PROTOCOL_$_IMAnimationTimerObserver
+ __UIStickerRepresentationRoleAnimated
+ __UIStickerRepresentationRoleKeyboard
+ __UIStickerRepresentationRoleStill
+ ___58-[MSStickerView dragInteraction:itemsForBeginningSession:]_block_invoke.159
+ ___86-[MSConversation _insertSticker:skipShelf:frameInWindowCoordinates:completionHandler:]_block_invoke
+ ___86-[_MSStickerSendManager insertSticker:forceStage:frameInRemoteView:completionHandler:]_block_invoke
+ ___block_literal_global.17
+ ___block_literal_global.21
+ __unnamed_array_storage.125
+ __unnamed_array_storage.128
+ _objc_msgSend$_addStickerToStoreWithRepresentations:sourceRect:effect:completion:
+ _objc_msgSend$_insertSticker:skipShelf:frameInWindowCoordinates:completionHandler:
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$animatedImageCacheURLFromExtension
+ _objc_msgSend$ballonBundleID
+ _objc_msgSend$convertRect:toCoordinateSpace:
+ _objc_msgSend$coordinateSpace
+ _objc_msgSend$fileURL
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$insertSticker:forceStage:frameInRemoteView:completionHandler:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setRole:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$transform
+ _objc_msgSend$uniqueID
- -[MSStickerBrowserView configureStickerView].cold.1
- -[MSStickerBrowserView configureStickerView].cold.2
- -[MSStickerView updateAnimationTimerObserving].cold.7
- -[_MSMessageMediaPayload initWithSticker:].cold.2
- -[_MSPresentationState init].cold.1
- -[_MSStickerSendManager insertSticker:forceStage:frameInScreenCoordinates:completionHandler:]
- GCC_except_table10
- GCC_except_table2
- GCC_except_table3
- GCC_except_table39
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CKAnimationTimerObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CKAnimationTimerObserver
- __OBJC_$_PROTOCOL_REFS_CKAnimationTimerObserver
- __OBJC_LABEL_PROTOCOL_$_CKAnimationTimerObserver
- __OBJC_PROTOCOL_$_CKAnimationTimerObserver
- ___58-[MSStickerView dragInteraction:itemsForBeginningSession:]_block_invoke.156
- ___93-[_MSStickerSendManager insertSticker:forceStage:frameInScreenCoordinates:completionHandler:]_block_invoke
- ___block_literal_global.19
- ___getCKDispatchQueueClass_block_invoke
- ___getCKDispatchQueueClass_block_invoke.cold.1
- ___getCKIsRunningIniMessageAppExtensionSymbolLoc_block_invoke
- ___getCKIsRunningIniMessageAppsViewServiceSymbolLoc_block_invoke
- __unnamed_array_storage.161
- __unnamed_array_storage.164
- _getCKDispatchQueueClass.softClass
- _getCKIsRunningIniMessageAppExtensionSymbolLoc.ptr
- _getCKIsRunningIniMessageAppsViewServiceSymbolLoc.ptr
- _objc_msgSend$__ck_attributionInfo
- _objc_msgSend$addBlock:
- _objc_msgSend$boolValueForKey:withDefault:
- _objc_msgSend$insertSticker:forceStage:frameInScreenCoordinates:completionHandler:
- _objc_msgSend$serialQueueWithDispatchPriority:
CStrings:
+ "\x13\x17&"
+ "@\"<IMAnimatedImageProtocol>\""
+ "@\"<IMImageDataProtocol>\""
+ "@\"NSOperationQueue\""
+ "IMAnimationTimerObserver"
+ "T@\"<IMAnimatedImageProtocol>\",&,N,V_image"
+ "T@\"<IMImageDataProtocol>\",&,N,V__imageData"
+ "T@\"<IMImageDataProtocol>\",&,N,V_imageData"
+ "T@\"NSOperationQueue\",&,N,V_stickerCacheQueue"
+ "TB,N,V_isInTranscript"
+ "TQ,N,V_stickerPositionVersion"
+ "_addStickerToStoreWithRepresentations:sourceRect:effect:completion:"
+ "_insertSticker:skipShelf:frameInWindowCoordinates:completionHandler:"
+ "_isInTranscript"
+ "_shouldRemoteViewControllerFenceOriginChanges"
+ "_stickerPositionVersion"
+ "addOperationWithBlock:"
+ "animatedImageCacheURLFromExtension"
+ "ballonBundleID"
+ "convertRect:toCoordinateSpace:"
+ "coordinateSpace"
+ "fileURL"
+ "initWithIMSticker:"
+ "initWithUUIDString:"
+ "insertSticker:forceStage:frameInRemoteView:completionHandler:"
+ "insertSticker:withSourceFrame:completionHandler:"
+ "isInTranscript"
+ "setIsInTranscript:"
+ "setQualityOfService:"
+ "setRole:"
+ "setStickerPositionVersion:"
+ "setUnderlyingQueue:"
+ "stickerPositionVersion"
+ "transform"
+ "uniqueID"
+ "v72@0:8@\"NSArray\"16{CGRect={CGPoint=dd}{CGSize=dd}}24q56@?<v@?@\"NSArray\"@\"NSError\">64"
+ "v72@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56@?64"
- "\x13\x17\x16"
- "-[MSStickerBrowserView configureStickerView]"
- "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/Messages/Source/StickerBrowser/MSStickerBrowserView.m"
- "@\"CKAnimatedImage\""
- "@\"CKDispatchQueue\""
- "@\"CKImageData\""
- "CKAnimationTimerObserver"
- "CKDispatchQueue"
- "CKIsRunningIniMessageAppExtension"
- "CKIsRunningIniMessageAppsViewService"
- "T@\"CKAnimatedImage\",&,N,V_image"
- "T@\"CKDispatchQueue\",&,N,V_stickerCacheQueue"
- "T@\"CKImageData\",&,N,V__imageData"
- "T@\"CKImageData\",&,N,V_imageData"
- "__ck_attributionInfo"
- "addBlock:"
- "boolValueForKey:withDefault:"
- "insertSticker:forceStage:frameInScreenCoordinates:completionHandler:"
- "serialQueueWithDispatchPriority:"

```

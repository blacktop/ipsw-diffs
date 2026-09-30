## ScreenSharing

> `/System/Library/PrivateFrameworks/ScreenSharing.framework/Versions/A/ScreenSharing`

```diff

-714.2.2.0.0
-  __TEXT.__text: 0x112058
+714.4.6.0.0
+  __TEXT.__text: 0x1128cc
   __TEXT.__auth_stubs: 0x2930
-  __TEXT.__objc_methlist: 0xc3a0
-  __TEXT.__cstring: 0x2941a
-  __TEXT.__const: 0x33a0
-  __TEXT.__oslogstring: 0x13764
-  __TEXT.__gcc_except_tab: 0xda8
+  __TEXT.__objc_methlist: 0xde18
+  __TEXT.__cstring: 0x295ff
+  __TEXT.__const: 0x33d0
+  __TEXT.__oslogstring: 0x138d3
+  __TEXT.__gcc_except_tab: 0xdbc
   __TEXT.__ustring: 0x166
-  __TEXT.__unwind_info: 0x2808
+  __TEXT.__unwind_info: 0x2870
   __TEXT.__objc_classname: 0xe26
-  __TEXT.__objc_methname: 0x242a2
+  __TEXT.__objc_methname: 0x24394
   __TEXT.__objc_methtype: 0x5ce6
-  __TEXT.__objc_stubs: 0x19c80
-  __DATA_CONST.__got: 0xbd8
+  __TEXT.__objc_stubs: 0x19d00
+  __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d88
+  __DATA_CONST.__objc_selrefs: 0x8460
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x300
-  __DATA_CONST.__objc_arraydata: 0x3c0
+  __DATA_CONST.__objc_arraydata: 0x3b8
   __AUTH_CONST.__auth_got: 0x14a8
   __AUTH_CONST.__const: 0x14e0
-  __AUTH_CONST.__cfstring: 0x7620
-  __AUTH_CONST.__objc_const: 0x15100
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__cfstring: 0x7660
+  __AUTH_CONST.__objc_const: 0x12010
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x1ef0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xff4
+  __DATA.__objc_ivar: 0xffc
   __DATA.__data: 0x1770
   __DATA.__bss: 0x7bc
   __DATA.__common: 0x2

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B729534D-D46B-33CF-BBE8-74F0FEB70DB2
-  Functions: 5258
-  Symbols:   12098
-  CStrings:  15049
+  UUID: 9A6ACE9E-47A8-363C-BB2C-585EDC540389
+  Functions: 5262
+  Symbols:   12152
+  CStrings:  15087
 
Symbols:
+ +[SSAddress validHostname:].cold.1
+ +[SSAddressResolver resolver].cold.1
+ +[SSAnnotationRenderer sharedRenderer].cold.1
+ +[SSContactsTokenFieldDelegate validIDSIDColor].cold.1
+ +[SSCredentialsManager initialize].cold.1
+ +[SSEventHelperManager sharedManager].cold.1
+ +[SSEventSession registerForDisplayChanges].cold.1
+ +[SSInputEvent initialize].cold.1
+ +[SSInputEventSourceCoordinator sharedCoordinator].cold.1
+ +[SSSession registerForDisplayChanges].cold.1
+ +[SSSessionView isRedwoodApp].cold.1
+ -[NSString(IDSAdditions) formattedPhoneNumber].cold.1
+ -[RSAKeyPair init].cold.1
+ -[SSAddressResolver addIDSServiceMessageObserver:forSession:].cold.2
+ -[SSAddressResolver resolveURL:forObserver:].cold.2
+ -[SSCallTrackingWindow ssView:didDropRemotePath:atLocalDropDestination:completionHandler:].cold.1
+ -[SSCallWindowController callTrackingWindow].cold.1
+ -[SSCallWindowController handleControlModeMenuKey:].cold.1
+ -[SSCallWindowController removePresenterAllowsRequestingControlObserver].cold.2
+ -[SSCallWindowController removeRemoteControlStateObserver].cold.2
+ -[SSCallWindowController toggleControlObserve:].cold.1
+ -[SSCallWindowController windowDidLoad].cold.2
+ -[SSCallWindowController windowDidLoad].cold.3
+ -[SSCallWindowController windowDidLoad].cold.4
+ -[SSSession captureStreamNumber:toFileURL:].cold.1
+ -[SSSession captureStreamNumber:toFileURL:].cold.2
+ -[SSSession receivedServerInfo]
+ -[SSSession setReceivedServerInfo:]
+ -[SSSessionView captureScreen1:].cold.1
+ -[SSSessionView captureScreen2:].cold.1
+ -[SSSessionView configureViewerForScaling:].cold.1
+ -[SSSessionView isDeviceClamshellCallbackRegistered]
+ -[SSSessionView observeDisplayMonitorForDisplayType:].cold.1
+ -[SSSessionView observeDisplayMonitorForDisplayType:].cold.2
+ -[SSSessionView setIsDeviceClamshellCallbackRegistered:]
+ -[SSSessionView setReferenceHDRModeEnabled:].cold.1
+ -[SSSessionView showConnectionProgressViewWithLabel:identity:].cold.1
+ -[SSSessionView unregisterForIOKitClamshellNotification].cold.1
+ -[SSSessionView unregisterForIOKitClamshellNotification].cold.2
+ CopyPackedScrapDataForPasteboardByName.cold.3
+ CopyTextIntoPasteboard.cold.4
+ GCC_except_table164
+ GCC_except_table172
+ GCC_except_table192
+ GCC_except_table205
+ GCC_except_table293
+ GCC_except_table301
+ GCC_except_table723
+ GCC_except_table724
+ GCC_except_table727
+ GCC_except_table728
+ GCC_except_table729
+ InitKeyMap.cold.2
+ OBJC_IVAR_$_SSSession._receivedServerInfo
+ OBJC_IVAR_$_SSSessionView._isDeviceClamshellCallbackRegistered
+ RFBPostKeyEventCore.cold.1
+ RFBPostKeyEventCore.cold.2
+ SSAbsoluteToMicroseconds.cold.1
+ SSIsInternalBuild.cold.1
+ SSMicroseconds.cold.1
+ SSMicroseconds64.cold.1
+ SSTickCount.cold.1
+ UnpackScrapDataWithFilter.cold.3
+ _CreateClientOpts
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _RFBCodeToSSConnectFailureCode
+ __24-[SSSessionView connect]_block_invoke.1404
+ __24-[SSSessionView connect]_block_invoke.1414
+ __29-[SSSession stSendDragEvent:]_block_invoke.515
+ __31-[SSSessionView captureScreen:]_block_invoke.cold.1
+ __32-[SSSession handleDisplayInfo2:]_block_invoke.779
+ __32-[SSSession handleDisplayInfo2:]_block_invoke.782
+ __32-[SSSession handleDisplayInfo2:]_block_invoke.789
+ __43-[SSSessionView dismissNotificationOverlay]_block_invoke.1767
+ __MergedGlobals
+ __RFBFreeConnectionRefContents_block_invoke.88
+ __ViewerFileSenderThread_block_invoke.310
+ __block_literal_global.1407
+ __block_literal_global.236
+ __block_literal_global.312
+ __block_literal_global.786
+ _objc_msgSend$isDeviceClamshellCallbackRegistered
+ _objc_msgSend$receivedServerInfo
+ _objc_msgSend$setIsDeviceClamshellCallbackRegistered:
+ _objc_msgSend$setReceivedServerInfo:
- CopyPasteboardEntries.cold.1
- CopyPasteboardEntries.cold.2
- CopyPasteboardEntries.cold.3
- CopyPasteboardEntries.cold.4
- GCC_except_table163
- GCC_except_table171
- GCC_except_table191
- GCC_except_table204
- GCC_except_table291
- GCC_except_table300
- GCC_except_table715
- GCC_except_table716
- GCC_except_table717
- GCC_except_table720
- GCC_except_table721
- _RFBServerCommandSupportedCore
- __24-[SSSessionView connect]_block_invoke.1400
- __24-[SSSessionView connect]_block_invoke.1410
- __29-[SSSession stSendDragEvent:]_block_invoke.514
- __32-[SSSession handleDisplayInfo2:]_block_invoke.777
- __32-[SSSession handleDisplayInfo2:]_block_invoke.780
- __32-[SSSession handleDisplayInfo2:]_block_invoke.787
- __43-[SSSessionView dismissNotificationOverlay]_block_invoke.1763
- __RFBFreeConnectionRefContents_block_invoke.87
- __ViewerFileSenderThread_block_invoke.307
- __block_literal_global.1403
- __block_literal_global.233
- __block_literal_global.309
- __block_literal_global.784
- _gPasteboardMutex
- _kAVCMediaStreamOptionCallID
- initPasteboardMutex.onceToken
CStrings:
+ "-[SSSession doesServerSupportFeature:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/NewIn108Lib/CCBigNum.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/AuthRandom.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/AuthUtils.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/Clipboard.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/HEVCFrameRate.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/KerberosUtils.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/KeyMap.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/NWConnectionManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/NetBuffer.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/ODHelper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/RFBCommon.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/SSFileCopy/FileCopyIPC.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/SSFileCopy/FileCopySession.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/UDPSend.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/UDPUtils.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DCTHuffmanDecode.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeCursor.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeMultiVariant.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeRaw.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeZRLE.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeZlib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DeocdeUserInfo.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/RFBViewer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/RemoteBusyCursor.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/SSHUtils.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/ServerMessages.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/Socket.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/UDPReceiver.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/SSAssistanceCursor/SSAssistanceCursorIPC.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/SSPasteboardHelper/SSPasteboardHelperIPC.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAddress.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAddressResolver.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAnnotationRenderer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAnnotationUser.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSApplication.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSBonjourBrowser.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallScrollView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallTrackingView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallTrackingWindow.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallWindowController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionAuthenticationViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionOptions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionProgressViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSContactsTokenField.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCredentialsManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCursorView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSDevicesAndContacts.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSDisplayDetailsConcretePrimitives.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEncodings.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEventHelperManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEventSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileCopy.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransfer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransferTableCellView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransferWindowController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBuffer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferAVCMediaView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferAVConferenceView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferRenderView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInputEvent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInputEventSourceCoordinator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInvitationHelper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSPanningScrollView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSPreauthorizedUDPServer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSSessionView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSVirtualDisplayLocalDisplayMonitor.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/CommonUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/ComputerModelInfo.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/DNSResolver.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/EOSReporter.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/GetMACAddressSample.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/Log.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/NSObject+PerformSelectorOnTargetAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/OSVersionUtils.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/PerformSelectorOnThreadManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDSemaphore.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDThread.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RSAKeyPair.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SSSignposts.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SSTimebase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SocketUtil.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/srp.m"
+ "AllowLocalConnect"
+ "AllowLocalConnect pref set in remote management"
+ "Error creating client options\n"
+ "KDCUnsupportedDomainMigration"
+ "TB,N,V_isDeviceClamshellCallbackRegistered"
+ "TB,V_receivedServerInfo"
+ "_isDeviceClamshellCallbackRegistered"
+ "_receivedServerInfo"
+ "added clamshell notification for %p"
+ "audioOptions %s"
+ "clamshell status now %d  controller %p"
+ "free cursor %p"
+ "free the connection ref %p"
+ "isDeviceClamshellCallbackRegistered"
+ "new connection ref %p"
+ "new cursor image %p"
+ "receivedServerInfo"
+ "self.ioNotificationPort is NULL"
+ "self.serviceNotification not set"
+ "session not ready - return NO for %d  connection ref %p"
+ "set frame update interval to %u"
+ "setIsDeviceClamshellCallbackRegistered:"
+ "setReceivedServerInfo:"
+ "unregisterForIOKitClamshellNotification %d  for %p"
+ "video1Options %s"
+ "video2CallIDDict %s"
+ "video2Options %s"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/NewIn108Lib/CCBigNum.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/AuthRandom.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/AuthUtils.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/Clipboard.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/HEVCFrameRate.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/KerberosUtils.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/KeyMap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/NWConnectionManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/NetBuffer.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/ODHelper.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/RFBCommon.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/SSFileCopy/FileCopyIPC.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/SSFileCopy/FileCopySession.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/UDPSend.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBCommon/UDPUtils.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DCTHuffmanDecode.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeCursor.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeMultiVariant.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeRaw.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeZRLE.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DecodeZlib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/DeocdeUserInfo.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/RFBViewer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/RemoteBusyCursor.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/SSHUtils.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/ServerMessages.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/Socket.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/RFBViewerLib/UDPReceiver.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/SSAssistanceCursor/SSAssistanceCursorIPC.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/SSPasteboardHelper/SSPasteboardHelperIPC.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAddress.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAddressResolver.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAnnotationRenderer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSAnnotationUser.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSApplication.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSBonjourBrowser.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallScrollView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallTrackingView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallTrackingWindow.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCallWindowController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionAuthenticationViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionOptions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSConnectionProgressViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSContactsTokenField.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCredentialsManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSCursorView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSDevicesAndContacts.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSDisplayDetailsConcretePrimitives.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEncodings.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEventHelperManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSEventSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileCopy.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransfer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransferTableCellView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFileTransferWindowController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBuffer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferAVCMediaView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferAVConferenceView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferRenderView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSFrameBufferView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInputEvent.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInputEventSourceCoordinator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSInvitationHelper.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSPanningScrollView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSPreauthorizedUDPServer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSSessionView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/ScreenSharingFramework/Source/SSVirtualDisplayLocalDisplayMonitor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/CommonUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/ComputerModelInfo.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/DNSResolver.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/EOSReporter.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/GetMACAddressSample.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/Log.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/NSObject+PerformSelectorOnTargetAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/OSVersionUtils.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/PerformSelectorOnThreadManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDSemaphore.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDSemaphore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RDThread.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/RSAKeyPair.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SSSignposts.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SSTimebase.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/SocketUtil.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ScreenSharing/common/srp.m"
- "added clamshell notification"
- "clamshell status now %d"
- "video2CallIDDict  %s"

```

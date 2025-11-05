## QuickLookIosmac

> `/System/Library/PrivateFrameworks/QuickLookIosmac.framework/Versions/A/QuickLookIosmac`

```diff

-1002.3.3.0.0
-  __TEXT.__text: 0x4a654
-  __TEXT.__auth_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0x1c7c
-  __TEXT.__cstring: 0x4d8e
+1002.5.2.0.0
+  __TEXT.__text: 0x4ae40
+  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0x1e24
+  __TEXT.__cstring: 0x4d37
   __TEXT.__oslogstring: 0x59be
-  __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x910
+  __TEXT.__const: 0x2d0
+  __TEXT.__gcc_except_tab: 0x908
   __TEXT.__dof_QLSeamles: 0x348
   __TEXT.__dof_QLThumbna: 0x49c
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_classname: 0x28b
   __TEXT.__objc_methname: 0x5776
   __TEXT.__objc_methtype: 0x10ca
   __TEXT.__objc_stubs: 0x4a40
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__got: 0x540
   __DATA_CONST.__const: 0xe78
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c8
+  __DATA_CONST.__objc_selrefs: 0x1648
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0xee0
-  __AUTH_CONST.__const: 0x1fb8
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__const: 0x1f98
   __AUTH_CONST.__cfstring: 0x3b40
-  __AUTH_CONST.__objc_const: 0x34a8
+  __AUTH_CONST.__objc_const: 0x31b8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x780
-  __AUTH.__data: 0x78
+  __AUTH.__data: 0x70
   __DATA.__objc_ivar: 0x2bc
-  __DATA.__data: 0x688
+  __DATA.__data: 0x690
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1448
+  __DATA.__bss: 0x1430
   __DATA.__common: 0xd8
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
+  - /System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis
   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C16C43D-9679-3CB1-98B8-3B339DBF45E2
-  Functions: 1889
-  Symbols:   4168
-  CStrings:  3006
+  UUID: A9A053EB-6EA5-3B52-BC67-0C123595A87C
+  Functions: 1982
+  Symbols:   4269
+  CStrings:  3001
 
Symbols:
+ +[QLDaemonProxy interface].cold.1
+ +[QLPreview inlinePreviewSupportedContentTypes].cold.1
+ +[QLRequestSession _updateCrashReportMessage].cold.1
+ +[QLRequestSession discardAllSessions:].cold.1
+ +[QLRequestSession getSessionAndNotifyPortDeathWithPort:].cold.2
+ +[QLRequestSession getSessionFromReplyPort:].cold.1
+ +[QLRequestSession sessionCount].cold.1
+ +[QLRequestSession sessionFromUUID:].cold.1
+ +[QLRequestSession setupSession:].cold.2
+ +[QLRequestSession setupSession:].cold.3
+ +[QLRequestSession unsetupSession:].cold.2
+ +[QLRequestSession unsetupSession:].cold.3
+ +[QLRequestSession unsetupSession:].cold.4
+ +[QLServerSatelliteManager defaultManager].cold.1
+ +[QLThumbnail dummyForcedGeneratorInfo].cold.1
+ -[QLPreview _sendRequestToServerIfNecessary:].cold.8
+ -[QLPreview generateWithExtension:].cold.2
+ -[QLPreview retrieveDataForProgressiveRendering:].cold.2
+ -[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:].cold.1
+ -[QLRequest dealloc].cold.1
+ -[QLRequest fillXPCRepresentation:messageType:context:data:dataLength:].cold.2
+ -[QLRequest fillXPCRepresentation:messageType:context:data:dataLength:].cold.3
+ -[QLRequest updateWithXPCRepresentation:outData:outDataLength:].cold.6
+ -[QLRequest updateWithXPCRepresentation:outData:outDataLength:].cold.7
+ -[QLRequestSession handleSendDataWithAttachmentURL:lastChunk:].cold.1
+ -[QLRequestSession initWithReplyPort:uuid:].cold.2
+ -[QLRequestSession invalidate].cold.1
+ -[QLRequestSession invalidate].cold.2
+ -[QLServerSatellite _logGeneratorUse:].cold.1
+ -[QLThumbnail _endProcess].cold.2
+ -[QLThumbnail generateLocallyWithQueue:completion:].cold.1
+ GCC_except_table252
+ GCC_except_table253
+ QLGeneralLog.cold.1
+ QLGetServerMachPort.cold.19
+ QLImageIODrawImageInContext.cold.1
+ QLInitInternalLogging.cold.1
+ QLInitLogging.cold.1
+ QLLoadQuickLookUISymbol.cold.1
+ QLPreviewBubbleShow.cold.2
+ QLPreviewDocumentComputePreview.cold.9
+ QLPreviewRequestAppendDataToAttachment.cold.3
+ QLPreviewRequestAppendDataToAttachment.cold.4
+ QLPreviewRequestCreateAttachmentURL.cold.1
+ QLPreviewRequestCreateAttachmentURL.cold.2
+ QLPreviewRequestCreateContext.cold.5
+ QLPreviewRequestSetURLRepresentation.cold.1
+ QLPreviewTypeGetDisplayBundleCount.cold.1
+ QLPreviewTypeGetDisplayBundleIDForUTI.cold.1
+ QLPreviewTypeGetDisplayBundleIDsAndNames.cold.1
+ QLPreviewTypeGetStaticDisplayBundleIDForUTI.cold.1
+ QLPreviewTypeIsDisplayBundleIDSafe.cold.1
+ QLPreviewTypeProcessThirdPartyGeneratorType.cold.1
+ QLRequestSessionPerformAsync.cold.1
+ QLRequestSessionPerformSync.cold.1
+ QLSeamlessClosingRequestSetAssociatedObject.cold.1
+ QLServerCheckIn.cold.1
+ QLThumbnailDispatchAsync.cold.1
+ QLThumbnailDispatchAsync.cold.2
+ QLThumbnailRequestSetImageAtURL.cold.1
+ QLThumbnailRequestSetThumbnailWithURLRepresentation.cold.2
+ QLTypeRegister.cold.1
+ _OBJC_CLASS_$_VCPSearchContext
+ _QLActivateGeneratorWithBundleID.cold.1
+ _QLBubbleUnregister.cold.2
+ _QLCacheVersionCreateFromURLWithGenerator.cold.2
+ _QLCacheVersionCreateFromURLWithGenerator.cold.3
+ _QLCopyAllThumbnailInfo.cold.2
+ _QLCopyCacheInfo.cold.2
+ _QLCopyCachedThumbnailsForURL.cold.2
+ _QLCopyServerStatistics.cold.5
+ _QLCreateQLURLFromCFURLForMIG.cold.2
+ _QLDeactivateGeneratorWithBundleID.cold.1
+ _QLDictionaryValueForContentType.cold.1
+ _QLDumpMachPortRights.cold.1
+ _QLGeneratorAutoDisplayExtension.cold.1
+ _QLGeneratorCopyFileExtension.cold.1
+ _QLGeneratorCopyGeneratorForContentType.cold.1
+ _QLGeneratorCopyGeneratorForFile.cold.2
+ _QLGeneratorCopyGeneratorFromBundleURL.cold.1
+ _QLGeneratorCopyGeneratorsLibrary.cold.1
+ _QLGeneratorDispatchBlock.cold.1
+ _QLGeneratorSetMaxGlobalWeight.cold.1
+ _QLGeneratorWakeUp.cold.1
+ _QLGeneratorWakeUp.cold.2
+ _QLGeneratorWakeUp.cold.3
+ _QLLoadPlugin.cold.6
+ _QLLoadPlugin.cold.7
+ _QLLoadPlugin.cold.8
+ _QLNiceRaiseAssert.cold.2
+ _QLPreviewBubbleCFFinalize.cold.1
+ _QLPreviewRequestCallGenerator.cold.2
+ _QLPreviewRequestCreatePDFContext.cold.1
+ _QLPreviewRequestFillXPCRepresentation.cold.1
+ _QLPreviewRequestSendReply.cold.7
+ _QLRegisterForQuickLookGlobalNotification.cold.1
+ _QLResetServer.cold.3
+ _QLSeamlessOpeningRequestUnregister.cold.2
+ _QLSeamlessOpeningRequestUnregister.cold.3
+ _QLThumbnailQueueDelegateCallback.cold.3
+ _QLThumbnailRequestCFFinalize.cold.1
+ _QLThumbnailRequestCallGenerator.cold.7
+ _QLThumbnailRequestCallGenerator.cold.8
+ _QLThumbnailRequestFillXPCRepresentation.cold.1
+ _QLThumbnailRequestSetupWithDiskStore.cold.2
+ __21-[QLPreview getData:]_block_invoke.337
+ __21-[QLPreview getData:]_block_invoke.341
+ __21-[QLPreview getData:]_block_invoke.341.cold.1
+ __21-[QLPreview getData:]_block_invoke.347
+ __21-[QLPreview getData:]_block_invoke.347.cold.1
+ __21-[QLPreview getData:]_block_invoke.351
+ __21-[QLPreview getData:]_block_invoke.354
+ __34-[QLRequestSession handleGetData:]_block_invoke.cold.1
+ __35-[QLPreview generateWithExtension:]_block_invoke.309
+ __35-[QLPreview generateWithExtension:]_block_invoke.312
+ __36+[QLRequestSession enableInstantOff]_block_invoke.cold.1
+ __36+[QLRequestSession enableInstantOff]_block_invoke.cold.2
+ __59-[QLPreview processProgressiveRendering:completionHandler:]_block_invoke.376
+ __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.269
+ __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.278
+ __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.284
+ __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.284.cold.1
+ __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.284.cold.2
+ __QLSeamlessClosingRequestRegister_block_invoke.cold.2
+ __QLShouldLogForInternalDebug.cold.1
+ __QLUIHelperRegisterForHelperDeath_block_invoke.cold.3
+ ___QLBubbleUnregister_block_invoke.cold.1
+ ___QLGeneratorWakeUp_block_invoke.cold.9
+ ___QLLaunchUpdatingThread_block_invoke.cold.7
+ ___QLLaunchUpdatingThread_block_invoke.cold.8
+ __block_literal_global.340
+ __qlfuture_wait_block_invoke.cold.1
+ _dlopenHelper$MediaAnalysis
+ _dlopenHelperFlag$MediaAnalysis
+ _gotLoadHelper_x8$_OBJC_CLASS_$_VCPSearchContext
+ qlfuture_dispatch.cold.1
+ qlfuture_notify.cold.1
+ qlfuture_wait.cold.1
- GCC_except_table255
- GCC_except_table256
- MediaAnalysisLibrary.frameworkLibrary
- MediaAnalysisLibrary.onceToken
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _VCPSearchContextFunction
- __21-[QLPreview getData:]_block_invoke.336
- __21-[QLPreview getData:]_block_invoke.340
- __21-[QLPreview getData:]_block_invoke.340.cold.1
- __21-[QLPreview getData:]_block_invoke.346
- __21-[QLPreview getData:]_block_invoke.346.cold.1
- __21-[QLPreview getData:]_block_invoke.350
- __21-[QLPreview getData:]_block_invoke.353
- __35-[QLPreview generateWithExtension:]_block_invoke.308
- __35-[QLPreview generateWithExtension:]_block_invoke.311
- __59-[QLPreview processProgressiveRendering:completionHandler:]_block_invoke.375
- __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.268
- __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.277
- __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.283
- __70-[QLPreview retrieveDisplayBundleIDForAdvancedUsage:completionHander:]_block_invoke.283.cold.1
- ___MediaAnalysisLibrary_block_invoke
- __block_literal_global.339
- __block_literal_global.771
- _classVCPSearchContext
- _getVCPSearchContextClass
- _initVCPSearchContext
- _objc_getClass
- initVCPSearchContext.cold.1
- initVCPSearchContext.cold.2
CStrings:
+ "/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis"
- "/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis"
- "MediaAnalysisLibrary"
- "VCPSearchContext"
- "classVCPSearchContext"
- "frameworkLibrary"
- "initVCPSearchContext"

```

## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/Versions/A/DiagnosticExtensionsDaemon`

```diff

 189.0.0.0.0
-  __TEXT.__text: 0x7a774
+  __TEXT.__text: 0x7a748
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x5d38
+  __TEXT.__objc_methlist: 0x68bc
   __TEXT.__const: 0x1f8
   __TEXT.__cstring: 0x4f38
   __TEXT.__gcc_except_tab: 0x1dc4
   __TEXT.__oslogstring: 0x835d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1a78
+  __TEXT.__unwind_info: 0x1b48
   __TEXT.__objc_classname: 0x875
   __TEXT.__objc_methname: 0xeb54
   __TEXT.__objc_methtype: 0x2305

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3758
+  __DATA_CONST.__objc_selrefs: 0x3880
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0x21c0
   __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x13788
+  __AUTH_CONST.__objc_const: 0x12270
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D37724F0-FEAF-3188-88A4-10C3C4C0BA85
-  Functions: 2707
-  Symbols:   6635
+  UUID: 56693293-B9D4-3B56-8C79-21F624B36AF7
+  Functions: 2746
+  Symbols:   6672
   CStrings:  4994
 
Symbols:
+ +[DEDActivity sharedInstance].cold.1
+ +[DEDAnalytics logBugSessionStartWithDeviceType:isRemote:success:errorCode:].cold.1
+ +[DEDAnalytics log].cold.1
+ +[DEDAttachmentGroup archivedClasses].cold.1
+ +[DEDCollectionNotification log].cold.1
+ +[DEDConfiguration sharedInstance].cold.1
+ +[DEDConstants processName].cold.1
+ +[DEDDaemon sharedInstance].cold.1
+ +[DEDDeferredExtensionInfo log].cold.1
+ +[DEDDevice _currentDeviceId].cold.1
+ +[DEDExtension archivedClasses].cold.1
+ +[DEDExtensionIdentifier log].cold.1
+ +[DEDExtensionIdentifierManager log].cold.1
+ +[DEDFeedbackAnalytics logDataLoadWithContentItemCount:formItemsCount:teamCount:errorsCount:startedAt:endedAt:].cold.1
+ +[DEDFeedbackAnalytics logEventWithRequest:httpStatusCode:nsurlErrorCode:success:startedAt:endedAt:].cold.1
+ +[DEDFeedbackAnalytics logFBKBugSessionStartWithDeviceType:isRemote:success:errorCode:startedAt:getSessionEndedAt:showExtensionsEndedAt:getStatusEndedAt:].cold.1
+ +[DEDIDSConnection archivedClasses].cold.1
+ +[DEDIDSInbound archivedClasses].cold.1
+ +[DEDIDSOutbound archivedClasses].cold.1
+ +[DEDManager sharedInstance].cold.1
+ +[DEDPersistence sharedInstance].cold.1
+ +[DEDRequestAdvertiser sharedInstance].cold.1
+ +[DEDSharingConnection checkIn].cold.1
+ +[DEDTestingFinisher log].cold.1
+ +[DEDUtils isInternalInstall].cold.1
+ +[DEDUtils sharedLog].cold.1
+ +[ResourceLoader _rfc1123DateFormatter].cold.1
+ -[DEDAttachmentHandler dedDirectory].cold.1
+ -[DEDBugSession _logOperationQueue].cold.1
+ -[DEDBugSession log].cold.1
+ -[DEDDiagnosticCollector init].cold.1
+ -[DEDRequestAdvertiser encodeRequestRecordAsJSON:].cold.2
+ -[ResourceLoader _simulatedLatency].cold.1
+ DEDIDSConnectionLog.cold.1
+ DEDSessionCleanupLog.cold.1
+ DEDSessionStartLog.cold.1
+ DEDSessionStateLog.cold.1
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table171
+ GCC_except_table219
+ IDSDelLog.cold.1
+ Log.cold.1
+ formatter.cold.1
- GCC_except_table155
- GCC_except_table156
- GCC_except_table169
- GCC_except_table218
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_9

```

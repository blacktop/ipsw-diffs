## eedmediaservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice`

```diff

-2946.0.27.0.3
-  __TEXT.__text: 0x12104
-  __TEXT.__auth_stubs: 0x570
+2946.0.30.0.0
+  __TEXT.__text: 0x15174
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__delay_stubs: 0x160
   __TEXT.__delay_helper: 0x564
-  __TEXT.__objc_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0x624
+  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methlist: 0x6f0
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x3f0
-  __TEXT.__cstring: 0x1a37
-  __TEXT.__oslogstring: 0x2dd2
-  __TEXT.__objc_methname: 0x24de
-  __TEXT.__objc_classname: 0xe3
-  __TEXT.__objc_methtype: 0x88e
-  __TEXT.__unwind_info: 0x340
-  __DATA_CONST.__auth_got: 0x308
+  __TEXT.__gcc_except_tab: 0x434
+  __TEXT.__cstring: 0x1d89
+  __TEXT.__oslogstring: 0x3414
+  __TEXT.__objc_methname: 0x27ee
+  __TEXT.__objc_classname: 0xe4
+  __TEXT.__objc_methtype: 0x8a3
+  __TEXT.__unwind_info: 0x360
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__cfstring: 0xc60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x1090
-  __DATA.__objc_selrefs: 0x940
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_const: 0x1180
+  __DATA.__objc_selrefs: 0x9e8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x318
   __DATA.__bss: 0x28

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 242
-  Symbols:   163
-  CStrings:  821
+  Functions: 264
+  Symbols:   164
+  CStrings:  896
 
Symbols:
+ _dispatch_after
CStrings:
+ "\x0f\x11\x12\x12"
+ "\x1c"
+ " -exceeded MaxAllowedTimeForRequest,"
+ " <CLEEDMediaServiceRequest: ID:%!@(MISSING), uploadURL:%!@(MISSING), callUUID:%!@(MISSING), requestTimestamp:%!@(MISSING), numFiltered:%!l(MISSING)u, numPending:%!l(MISSING)u, numDelay:%!l(MISSING)u, numComplete:%!l(MISSING)u>"
+ "#EED2EMS,%!{(MISSING)public}s, Abort due to upload Mitigations:%!{(MISSING)public}@, returning"
+ "#EED2EMS,%!{(MISSING)public}s, Abort?:%!{(MISSING)public}s, numInFlight:%!{(MISSING)public}lu, numPendingUpload:%!{(MISSING)public}lu, numPendingEncrypt:%!{(MISSING)public}lu, numDelayed:%!{(MISSING)public}lu, numCompleted:%!{(MISSING)public}lu, totalBytesUploadedInCall:%!{(MISSING)public}lf MB"
+ "#EED2EMS,%!{(MISSING)public}s, All media items delayed for requestID:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, ContinuedProcessingTaskRequest:%!{(MISSING)public}@, Title:%!{(MISSING)public}@, Reason:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Delay due to upload Mitigations:%!{(MISSING)public}@, returning"
+ "#EED2EMS,%!{(MISSING)public}s, DelayedMediaServiceItemsListCount:%!{(MISSING)private}lu"
+ "#EED2EMS,%!{(MISSING)public}s, Delaying pending media uploads:%!{(MISSING)public}lu"
+ "#EED2EMS,%!{(MISSING)public}s, Error creating default mitigation object"
+ "#EED2EMS,%!{(MISSING)public}s, Filesize(%!{(MISSING)public}.2lf MB) exceeds limit for:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, MediaServiceItem:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Nothing to process for cachedRequestID:%!{(MISSING)private}s, filteredCount:%!{(MISSING)public}lu, pendingCount:%!{(MISSING)public}lu, delayCount:%!{(MISSING)public}lu, completedCount:%!{(MISSING)public}lu"
+ "#EED2EMS,%!{(MISSING)public}s, ProgressUITask not available, returning."
+ "#EED2EMS,%!{(MISSING)public}s, Successfully read CLEEDMediaService data from cache file:%!{(MISSING)private}s, cacheSize:%!{(MISSING)public}lu, mitigation:%!{(MISSING)public}@, requests:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Task:%!{(MISSING)public}@, TaskStatus:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, Tasks ongoing, pendingUpload:%!{(MISSING)public}lu, pendingEncryption:%!{(MISSING)public}lu, inFlight:%!{(MISSING)public}lu, delayed:%!{(MISSING)public}lu"
+ "#EED2EMS,%!{(MISSING)public}s, Title:%!{(MISSING)public}s, Reason:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, Title:%!{(MISSING)public}s, Reason:%!{(MISSING)public}s, Description:%!{(MISSING)public}@, progress:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Total Count is 0. Nothing to process, early return."
+ "#EED2EMS,%!{(MISSING)public}s, completedCount:%!{(MISSING)public}ld, delayCount:%!{(MISSING)public}ld, totalCount:%!{(MISSING)public}ld, userAbort:%!{(MISSING)public}s, ProgressUITask:%!{(MISSING)public}@, Progress:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, delayQueueCount:%!{(MISSING)private}lu"
+ "#EED2EMS,%!{(MISSING)public}s, extendedSessionEnded, not in emergency mode"
+ "#EED2EMS,%!{(MISSING)public}s, media item not part of delay queue:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, mediaID:%!{(MISSING)private}s, size:%!{(MISSING)private}lu MB"
+ "#EED2EMS,%!{(MISSING)public}s, mediaServiceItem is nil"
+ "#EED2EMS,%!{(MISSING)public}s, self no longer valid, readURL:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, self[%!{(MISSING)public}@] or abort requested, early return."
+ "#EED2EMS,%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}lf MB, mediaServiceItemSize:%!{(MISSING)public}lf MB"
+ "#EED2EMS,%!{(MISSING)public}s, uploadAttempt:%!{(MISSING)public}lu, timeElapsedSinceRequestSecs:%!{(MISSING)public}lld, session:%!{(MISSING)private}@, urlRequest:%!{(MISSING)public}@, resumeData:%!{(MISSING)private}@, "
+ "#EED2EMS,%!{(MISSING)public}s, uploadQuotaExceeded, All Uploads delayed"
+ "#EED2EMS,%!{(MISSING)public}s[currentMitigation:%!{(MISSING)public}@, numRequests:%!{(MISSING)public}lu, extendedSessionEnded:%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}ld]"
+ "#EED2EMS,%!{(MISSING)public}s[requestID:%!{(MISSING)public}@,uploadURL:%!{(MISSING)public}@,callUUID:%!{(MISSING)public}@,requestTimestamp:%!{(MISSING)public}@,sharedInfoPrefix:%!{(MISSING)private}@,combinedSecret:%!{(MISSING)private}@,deviceKeyConfirmation:%!{(MISSING)private}@,Token:%!{(MISSING)private}@,numFiltered:%!{(MISSING)public}lu,numPending:%!{(MISSING)public}lu,numDelayed:%!{(MISSING)public}lu,numCompleted:%!{(MISSING)public}lu]"
+ "%!l(MISSING)f of %!l(MISSING)u Files"
+ "%!l(MISSING)u Photos Paused"
+ "%!l(MISSING)u Photos Sent"
+ "-[CLEEDMediaService checkIfUploadQuotaReached:]"
+ "-[CLEEDMediaService cleanup]"
+ "-[CLEEDMediaService delayMediaUpload]"
+ "-[CLEEDMediaService handleDelayForMediaServiceItem:]"
+ "-[CLEEDMediaService insertMediaServiceItemInUploadList:]"
+ "-[CLEEDMediaService notifyProgressUITaskCompletion]"
+ "-[CLEEDMediaService notifyProgressUITaskCompletion]_block_invoke"
+ "-[CLEEDMediaService processDelayQueueForCachedRequest:]"
+ "-[CLEEDMediaService processMediaServicesEndOfExtendedSessionNotification]"
+ "-[CLEEDMediaService restoreDelayedMediaServiceItems]"
+ "-[CLEEDMediaService triggerAllProcessing]_block_invoke"
+ "-[CLEEDMediaServiceItem handleUploadTaskDelayForItem:response:error:]"
+ "-[CLEEDMediaServiceRequest updateQueueForDelayedMediaItem:]"
+ "Could not send %!l(MISSING)u photos."
+ "No Photos Sent"
+ "Only %!l(MISSING)u Photos Sent"
+ "Preparing to send..."
+ "T@\"NSMutableSet\",&,N,V_delayQueue"
+ "TB,N,V_extendedSessionEnded"
+ "To Emergency Services."
+ "Tq,N,V_totalBytesUploadedDuringCall"
+ "Upload Completed."
+ "_delayQueue"
+ "_extendedSessionEnded"
+ "_totalBytesUploadedDuringCall"
+ "checkIfUploadQuotaReached:"
+ "cleanup"
+ "countOfDelayedItemsInRequest:"
+ "delayMediaUpload"
+ "delayQueue"
+ "delayQueue"
+ "delayRequired"
+ "didApplyDelayMitigation"
+ "didApplyDelayMitigation"
+ "extendedSessionEnded"
+ "extendedSessionEnded"
+ "fDelayedServiceItemsList"
+ "fFinalProgressUITitleUpdated"
+ "handleDelayForMediaServiceItem:"
+ "handleUploadTaskDelayForItem:response:error:"
+ "iPhone will try to send later."
+ "insertMediaServiceItemInUploadList:"
+ "localizedStringWithFormat:"
+ "notifyProgressUITaskCompletion"
+ "numDelayMitigatedItems"
+ "numFileSizeExceeded"
+ "processDelayQueueForCachedRequest:"
+ "processMediaServicesEndOfExtendedSessionNotification"
+ "q"
+ "q16@0:8"
+ "restoreDelayedMediaServiceItems"
+ "setDelayQueue:"
+ "setDidApplyDelayMitigation:"
+ "setExtendedSessionEnded:"
+ "setTotalBytesUploadedDuringCall:"
+ "totalBytesUploadedDuringCall"
+ "totalBytesUploadedDuringCall"
+ "updateQueueForDelayedMediaItem:"
+ "updateTitle:withReason:"
+ "v24@0:8q16"
- "\x0e\x11\x14"
- "\x1b"
- " <CLEEDMediaServiceRequest: ID:%!@(MISSING), uploadURL:%!@(MISSING), callUUID:%!@(MISSING), requestTimestamp:%!@(MISSING), numFiltered:%!l(MISSING)u, numPending:%!l(MISSING)u, numComplete:%!l(MISSING)u>"
- "#EED2EMS,%!{(MISSING)public}s, Abort Requested due to upload Mitigations:%!{(MISSING)public}@, returning"
- "#EED2EMS,%!{(MISSING)public}s, Abort?:%!{(MISSING)public}s, numInFlight:%!{(MISSING)public}lu, numPendingUpload:%!{(MISSING)public}lu, numPendingEncrypt:%!{(MISSING)public}lu, numCompleted:%!{(MISSING)public}lu"
- "#EED2EMS,%!{(MISSING)public}s, AnyInFlightMediaServiceItem?:%!{(MISSING)public}s, pendingCount(incl. in-flight items):%!{(MISSING)public}lu"
- "#EED2EMS,%!{(MISSING)public}s, ContinuedProcessingTaskRequest:%!{(MISSING)public}@, description:%!{(MISSING)public}@, reason:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, Description:%!{(MISSING)public}@, progress:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, Nothing to process for cachedRequestID:%!{(MISSING)private}s, filteredCount:%!{(MISSING)public}lu, pendingCount:%!{(MISSING)public}lu, completedCount:%!{(MISSING)public}lu"
- "#EED2EMS,%!{(MISSING)public}s, Successfully read CLEEDMediaService data from cache file:%!{(MISSING)private}s, cacheSize:%!{(MISSING)public}lu, requests:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, TaskStatus%!{(MISSING)public}s for task:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, Tasks ongoing"
- "#EED2EMS,%!{(MISSING)public}s, mediaID:%!{(MISSING)private}s, sizeBytes:%!{(MISSING)private}lu"
- "#EED2EMS,%!{(MISSING)public}s, session:%!{(MISSING)private}@, urlRequest:%!{(MISSING)public}@, resumeData:%!{(MISSING)private}@, uploadAttempt:%!{(MISSING)public}lu"
- "#EED2EMS,%!{(MISSING)public}s[currentMitigation:%!{(MISSING)public}@, numRequests:%!{(MISSING)public}lu]"
- "#EED2EMS,%!{(MISSING)public}s[requestID:%!{(MISSING)public}@,uploadURL:%!{(MISSING)public}@,callUUID:%!{(MISSING)public}@,requestTimestamp:%!{(MISSING)public}@,sharedInfoPrefix:%!{(MISSING)private}@,combinedSecret:%!{(MISSING)private}@,deviceKeyConfirmation:%!{(MISSING)private}@,Token:%!{(MISSING)private}@,numFiltered:%!{(MISSING)public}lu,numPending:%!{(MISSING)public}lu,numCompleted:%!{(MISSING)public}lu]"
- "%!l(MISSING)f of %!l(MISSING)lu Files"
- "-[CLEEDMediaService handleAbortRequest]"
- "-[CLEEDMediaService handleEncryptionCompletionForServiceItem:encryptedFileURL:authTag:]_block_invoke_2"
- "-[CLEEDMediaService notifyProgressUITaskCompletionWithStatus:]"
- "To Emergency Services"
- "handleAbortRequest"
- "notifyProgressUITaskCompletionWithStatus:"

```

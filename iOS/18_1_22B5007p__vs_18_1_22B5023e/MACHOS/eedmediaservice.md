## eedmediaservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice`

```diff

-2946.0.30.0.0
-  __TEXT.__text: 0x15174
+2946.0.38.0.1
+  __TEXT.__text: 0x1596c
   __TEXT.__auth_stubs: 0x580
   __TEXT.__delay_stubs: 0x160
   __TEXT.__delay_helper: 0x564
-  __TEXT.__objc_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0x6f0
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x434
-  __TEXT.__cstring: 0x1d89
-  __TEXT.__oslogstring: 0x3414
-  __TEXT.__objc_methname: 0x27ee
-  __TEXT.__objc_classname: 0xe4
-  __TEXT.__objc_methtype: 0x8a3
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__objc_stubs: 0x26c0
+  __TEXT.__objc_methlist: 0x744
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x440
+  __TEXT.__cstring: 0x1e02
+  __TEXT.__oslogstring: 0x3452
+  __TEXT.__objc_methname: 0x2a11
+  __TEXT.__objc_classname: 0xe5
+  __TEXT.__objc_methtype: 0x906
+  __TEXT.__unwind_info: 0x368
   __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__cfstring: 0xc60
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__cfstring: 0xd40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x1180
-  __DATA.__objc_selrefs: 0x9e8
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_const: 0x1270
+  __DATA.__objc_selrefs: 0xa60
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x318
   __DATA.__bss: 0x28

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 264
-  Symbols:   164
-  CStrings:  896
+  Functions: 267
+  Symbols:   167
+  CStrings:  930
 
Symbols:
+ _NSFileProtectionKey
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_CLEEDUploadServiceConfig
CStrings:
+ "\x0f\x12\x11\x12\x11"
+ "#EED2EMS,%!{(MISSING)public}s, Abort?:%!{(MISSING)public}s, numInFlight:%!{(MISSING)public}lu, numPendingUpload:%!{(MISSING)public}lu, numPendingEncrypt:%!{(MISSING)public}lu, numDelayed:%!{(MISSING)public}lu, numCompleted:%!{(MISSING)public}lu, totalBytesUploadedInCall:%!{(MISSING)public}.2lf MB"
+ "#EED2EMS,%!{(MISSING)public}s, Completion called for mediaID:%!{(MISSING)public}s, requestID:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Connection to EEDMediaService(EMS) successful, mitigation:%!{(MISSING)public}@, uploadConfig:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Successfully read CLEEDMediaService data from cache file:%!{(MISSING)private}s, cacheSize:%!{(MISSING)public}lu, requests:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, Task:%!{(MISSING)public}@, TaskStatus:%!{(MISSING)public}s, CleanupProgressUITask:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, Title:%!{(MISSING)public}s, Reason:%!{(MISSING)public}s, Progress:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, activeRequest:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, mediaID:%!{(MISSING)private}s"
+ "#EED2EMS,%!{(MISSING)public}s, mediaID:%!{(MISSING)private}s, size:%!{(MISSING)private}.2lf MB"
+ "#EED2EMS,%!{(MISSING)public}s, removingRequest:%!{(MISSING)public}s"
+ "#EED2EMS,%!{(MISSING)public}s, serverUploadStatus:%!{(MISSING)public}ld, mediaID:%!{(MISSING)public}s, URLUploadTask:%!{(MISSING)private}@, [item:%!{(MISSING)private}s,response:%!{(MISSING)public}@,error:%!{(MISSING)public}@], httpResponse:%!{(MISSING)public}@"
+ "#EED2EMS,%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}.2lf MB, mediaServiceItemSize:%!{(MISSING)public}.2lf MB"
+ "#EED2EMS,%!{(MISSING)public}s, uploadAttempt:%!{(MISSING)public}lu, mediaID:%!{(MISSING)public}s, URLUploadTask:%!{(MISSING)private}@, session:%!{(MISSING)private}@, urlRequest:%!{(MISSING)public}@, resumeData:%!{(MISSING)private}@"
+ "#EED2EMS,%!{(MISSING)public}s,No data available to restore from cache"
+ "#EED2EMS,%!{(MISSING)public}s[numRequests:%!{(MISSING)public}lu, extendedSessionEnded:%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}ld]"
+ "%!l(MISSING)u Items"
+ "%!l(MISSING)u Videos"
+ "%!l(MISSING)u items"
+ "%!l(MISSING)u photos"
+ "%!l(MISSING)u videos"
+ "%!s(MISSING) Paused"
+ "%!s(MISSING) Sent"
+ "-[CLEEDMediaService connectToMediaService:uploadConfig:]"
+ "-[CLEEDMediaService removeCompletedRequestsOtherThan:]"
+ "-[CLEEDMediaService setProgressUITaskCompletion]"
+ "@\"CLEEDUploadServiceConfig\""
+ "@28@0:8Q16B24"
+ "Could not send %!s(MISSING)."
+ "HideProgressCircleInUI"
+ "No Items Sent"
+ "Only %!s(MISSING) Sent"
+ "TB,N,V_hasPendingPhotos"
+ "TB,N,V_hasPendingVideos"
+ "_hasPendingPhotos"
+ "_hasPendingVideos"
+ "anyItemsToProcess"
+ "connectToMediaService:uploadConfig:"
+ "fCleanupProgressUITask"
+ "fCurrentMitigation"
+ "fLatestMitigationWasNil"
+ "fProgressUICompletionStatus"
+ "fSessionInvalidated"
+ "fUploadServiceConfig"
+ "getLocalizedStringByMediaTypeWithCount:forTitle:"
+ "hasPendingPhotos"
+ "hasPendingPhotos"
+ "hasPendingVideos"
+ "hasPendingVideos"
+ "iPhone will try to send after the call."
+ "initWithBool:"
+ "initWithNumInflightUploads:maxUploadFileSizeMB:maxUploadQuotaMB:"
+ "maxUploadFileSizeMB"
+ "maxUploadQuotaMB"
+ "numInFlightUploads"
+ "removeCompletedRequestsOtherThan:"
+ "removeObjectsInArray:"
+ "sessionInvalidated"
+ "setHasPendingPhotos:"
+ "setHasPendingVideos:"
+ "setProgressUITaskCompletion"
+ "setUserInfoObject:forKey:"
+ "unionSet:"
+ "v32@0:8@\"CLEEDMitigation\"16@\"CLEEDUploadServiceConfig\"24"
- "\x0f\x11\x12\x12"
- "#EED2EMS,%!{(MISSING)public}s, Abort?:%!{(MISSING)public}s, numInFlight:%!{(MISSING)public}lu, numPendingUpload:%!{(MISSING)public}lu, numPendingEncrypt:%!{(MISSING)public}lu, numDelayed:%!{(MISSING)public}lu, numCompleted:%!{(MISSING)public}lu, totalBytesUploadedInCall:%!{(MISSING)public}lf MB"
- "#EED2EMS,%!{(MISSING)public}s, Completion called for requestID:%!{(MISSING)public}@, mediaItem:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, Connection to EEDMediaService(EMS) successful"
- "#EED2EMS,%!{(MISSING)public}s, Could not restore data from Cache"
- "#EED2EMS,%!{(MISSING)public}s, Error creating default mitigation object"
- "#EED2EMS,%!{(MISSING)public}s, ProgressUITask not available, returning."
- "#EED2EMS,%!{(MISSING)public}s, Successfully read CLEEDMediaService data from cache file:%!{(MISSING)private}s, cacheSize:%!{(MISSING)public}lu, mitigation:%!{(MISSING)public}@, requests:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, Task:%!{(MISSING)public}@, TaskStatus:%!{(MISSING)public}s"
- "#EED2EMS,%!{(MISSING)public}s, Title:%!{(MISSING)public}s, Reason:%!{(MISSING)public}s"
- "#EED2EMS,%!{(MISSING)public}s, mediaID:%!{(MISSING)private}s, size:%!{(MISSING)private}lu MB"
- "#EED2EMS,%!{(MISSING)public}s, mediaServiceItem:%!{(MISSING)private}@"
- "#EED2EMS,%!{(MISSING)public}s, serverUploadStatus:%!{(MISSING)public}ld, URLUploadTask:%!{(MISSING)private}@, [item:%!{(MISSING)private}s,response:%!{(MISSING)public}@,error:%!{(MISSING)public}@], httpResponse:%!{(MISSING)public}@"
- "#EED2EMS,%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}lf MB, mediaServiceItemSize:%!{(MISSING)public}lf MB"
- "#EED2EMS,%!{(MISSING)public}s, uploadAttempt:%!{(MISSING)public}lu, URLUploadTask:%!{(MISSING)private}@, session:%!{(MISSING)private}@, urlRequest:%!{(MISSING)public}@, resumeData:%!{(MISSING)private}@"
- "#EED2EMS,%!{(MISSING)public}s[currentMitigation:%!{(MISSING)public}@, numRequests:%!{(MISSING)public}lu, extendedSessionEnded:%!{(MISSING)public}s, totalBytesUploadedInCall:%!{(MISSING)public}ld]"
- "%!l(MISSING)u Photos Paused"
- "%!l(MISSING)u Photos Sent"
- "-[CLEEDMediaService connectToMediaService]"
- "-[CLEEDMediaService notifyProgressUITaskCompletion]_block_invoke"
- "Could not send %!l(MISSING)u photos."
- "No Photos Sent"
- "Only %!l(MISSING)u Photos Sent"
- "T@\"CLEEDMitigation\",&,N,V_currentMitigation"
- "_currentMitigation"
- "connectToMediaService"
- "currentMitigation"
- "currentMitigation"
- "iPhone will try to send later."
- "setCurrentMitigation:"

```

## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x115b40
-  __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0xea40
-  __TEXT.__objc_methlist: 0x327c
-  __TEXT.__const: 0x1588
-  __TEXT.__gcc_except_tab: 0x9778
-  __TEXT.__cstring: 0x3ded
-  __TEXT.__oslogstring: 0x1becb
-  __TEXT.__objc_classname: 0x7ef
-  __TEXT.__objc_methname: 0x1513a
-  __TEXT.__objc_methtype: 0x353b
+1491.200.63.0.0
+  __TEXT.__text: 0x11ac74
+  __TEXT.__auth_stubs: 0x2200
+  __TEXT.__objc_stubs: 0xee00
+  __TEXT.__objc_methlist: 0x33d4
+  __TEXT.__const: 0x15b8
+  __TEXT.__gcc_except_tab: 0x9630
+  __TEXT.__cstring: 0x3efd
+  __TEXT.__oslogstring: 0x1c13b
+  __TEXT.__objc_classname: 0x83f
+  __TEXT.__objc_methname: 0x1593a
+  __TEXT.__objc_methtype: 0x360b
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0xe26
-  __TEXT.__constg_swiftt: 0x5e0
-  __TEXT.__swift5_reflstr: 0x503
-  __TEXT.__swift5_fieldmd: 0x57c
+  __TEXT.__swift5_typeref: 0xe6e
+  __TEXT.__constg_swiftt: 0x654
+  __TEXT.__swift5_reflstr: 0x563
+  __TEXT.__swift5_fieldmd: 0x5d4
   __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift5_types: 0x6c
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift_as_cont: 0x13c

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3420
+  __TEXT.__unwind_info: 0x34e0
   __TEXT.__eh_frame: 0x1a80
-  __DATA_CONST.__const: 0x5980
-  __DATA_CONST.__cfstring: 0x3d00
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0x5a78
+  __DATA_CONST.__cfstring: 0x3ce0
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x10c8
-  __DATA_CONST.__got: 0x12f8
-  __DATA_CONST.__auth_ptr: 0x330
-  __DATA.__objc_const: 0x3db8
-  __DATA.__objc_selrefs: 0x4180
-  __DATA.__objc_ivar: 0x274
-  __DATA.__objc_data: 0xdc8
-  __DATA.__data: 0xe98
-  __DATA.__common: 0x8
+  __DATA_CONST.__auth_got: 0x1110
+  __DATA_CONST.__got: 0x1320
+  __DATA_CONST.__auth_ptr: 0x338
+  __DATA.__objc_const: 0x4110
+  __DATA.__objc_selrefs: 0x4290
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_data: 0xf30
+  __DATA.__data: 0xef8
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2651
-  Symbols:   920
-  CStrings:  5301
+  Functions: 2710
+  Symbols:   923
+  CStrings:  5366
 
Symbols:
+ _IMTranscriptBackgroundSenderHandleKey
+ _OBJC_CLASS_$_IMDAttachmentDownloadPolicyFilter
+ _swift_deallocPartialClassInstance
CStrings:
+ "    user info: %s"
+ " => Settled on signatures: %s"
+ " urlStrings: %s   owners: %s    signatures: %s  keys: %s  fileSizeStrings: %s"
+ "%{public}s Forcing iMessage unavailable due to satellite connectivity"
+ "?8E"
+ "?;E"
+ "@\"AttachmentDownloadRestriction\""
+ "@\"IMDAttachmentDownloadPolicyFilter\""
+ "@40@0:8B16B20q24q32"
+ "@44@0:8@16^B24B32@?36"
+ "Attachment download context is missing entries (signature = %s, ownerID = %s, fileSizeString = %s, encryptionKey = %{private}s)"
+ "B20@?0@\"_TtC8iMessage24MessageAttachmentRequest\"8B16"
+ "Download progress updated to for transferID %@ %lld of %lld (%lld bps)"
+ "Failed to remap guids after scheduled message sent, will fall back to stored message"
+ "Failed type check! {key: %@, class: %@}"
+ "Ignoring this file (fileSizeString: %s), download not allowed"
+ "Ignoring this file for smallest (fileSizeString: %s), file is invalid or missing size"
+ "Ignoring this file, file is larger than current smallest (fileSizeString: %s), (smallestFileSizeString: %s)"
+ "Message %@ found sensitive after acquisition; failing send."
+ "Message %@ is blocked pending unresolved CommSafety decision"
+ "MessageSpamDecisionResults"
+ "No files are acceptable to download"
+ "Not downloading attachments for message %@ as it is a typing message"
+ "Released pending attachment preview for %@ (%{BOOL}d)"
+ "Scheduled message delivered without edits — keeping stored attachments and remapping %lu incoming transfer records %@"
+ "Scheduled message was delivered with %lu transfers but %lu were stored, can't map them onto each other. Using the incoming attachments instead"
+ "Send of %@ was attempted on airplane mode without wifi enabled, not actually sending the message"
+ "T@\"AttachmentDownloadRestriction\",N,&,VdownloadRestriction"
+ "T@\"IMDAttachmentDownloadPolicyFilter\",R,N,V_attachmentDownloadPolicyFilter"
+ "T@\"NSNumber\",N,R,VfileSize"
+ "TB,N,V_sentWithoutNetwork"
+ "TB,R,N,V_isBlackholed"
+ "TB,R,N,V_shouldTrackForRequery"
+ "Taking this file, we're good to grab it (this: %s)"
+ "Tq,R,N,V_isFiltered"
+ "Tq,R,N,V_spamDetectionSource"
+ "Will download file(s) of size: %s"
+ "_TtC8iMessage24MessageAttachmentRequest"
+ "_attachmentDownloadPolicyFilter"
+ "_automation_messageContextFromTopLevelMessage:"
+ "_generateSURFSnapshotForMessage:completion:"
+ "_handleTransferDownloadFinishedForMessage:messageID:attachmentSuccess:errorType:fileTransferError:failedFileSize:additionalErrorInfo:downloadStartTime:token:toIdentifier:fromIdentifier:account:"
+ "_isBlackholed"
+ "_isFiltered"
+ "_sentWithoutNetwork"
+ "_shouldTrackForRequery"
+ "_spamDetectionSource"
+ "addActiveDownloadForStage:"
+ "attachmentDownloadPolicyFilter"
+ "attachmentRequestsFor:foundAnyFile:isLowQualityModeEnabled:isDownloadAllowed:"
+ "blockingTransferGUIDs:reason:"
+ "copyByStrippingReplyThreadingForBackwardsCompatibility"
+ "deviceIsLockedDownFor:senderOrigin:"
+ "downloadRestriction"
+ "fileExistsForTransfer:"
+ "fileSizeString"
+ "fileTransferCenter"
+ "hasActiveDownloadForStage:"
+ "hasNoNetworkForSending"
+ "hasUnresolvedCommSafetySendDecision"
+ "hasUnresolvedCommSafetySendDecisionWithFileTransferCenter:"
+ "iMessage.MessageAttachmentRequest"
+ "initWithFileTransferCenter:"
+ "initWithIsBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:"
+ "initWithRequestURLString:signature:ownerID:fileSize:encryptionKey:"
+ "initWithUserInfo:"
+ "initWithUserInfo:index:"
+ "isNonBlockingAttachmentReceiveEnabled"
+ "isValid"
+ "logAttachmentRequests:forTransfer:"
+ "noEligibleDestinationsCache"
+ "ownerID"
+ "receiveFileTransfer:topic:path:requestURLString:ownerID:sourceAppID:senderExemptFromLDM:signature:decryptionKey:fileSize:priority:progressBlock:completionBlock:"
+ "receiveFileTransfer:transferGUID:topic:path:requestURLString:ownerID:signature:decryptionKey:fileSize:balloonBundleID:senderContext:senderID:priority:progressBlock:completionBlock:"
+ "removeActiveDownloadForStage:"
+ "requestURLString"
+ "retrieveAttachmentsForMessage:inChat:inlineAttachments:displayID:topic:comingFromStorage:shouldForceAutoDownload:senderContext:blockingTransferGUIDs:individualAttachmentFinishedBlock:completionBlock:lateDownloadCompletionBlock:"
+ "send message: %@  guid: %@  to identifier: %@   chat: %@   callerURI: %@   self: %@   account: %@ associatedMessageGUID: %@  associatedMessageType: %lld  messageItemClass: %@ fileTransferGUID %@ network: %{BOOL}d"
+ "sentWithoutNetwork"
+ "setDownloadRestriction:"
+ "setHadNoEligibleDestinations:forMessageGUID:"
+ "setSentWithoutNetwork:"
+ "shouldTrackForRequery"
+ "updateTemporaryFileTransferGUIDsWithPermanentFileTransferGUIDs:"
+ "v104@0:8@16@24@32@40@48B56B60@64@72@?80@?88@?96"
+ "v104@0:8@16@24B32I36@40Q48@56@64@72@80@88@96"
+ "v16@?0@\"MessageSpamDecisionResults\"8"
+ "v28@?0@\"IMMessageItem\"8@\"NSString\"16B24"
+ "v72@?0@\"IMMessageItem\"8@\"NSString\"16B24I28@\"NSError\"32Q40@\"NSString\"48@\"MessageSpamDecisionResults\"56@?<v@?>64"
- "    user info: %@"
- " => Assigning this one: %@ fileSize: %@"
- " => Settled on signatures: %@"
- " urlStrings: %@   owners: %@    signatures: %@  keys: %@  fileSizeStrings: %@"
- "%@-%d"
- "?1E"
- "?8I"
- "?:I"
- "Downlaod progress updated to for transferID %@ %lld of %lld (%lld bps)"
- "Grabbing the largest file we can find (size: %@)"
- "Ignoring this file, still not allowed to auto download (localFileSizeString: %@), (fileSizeString:%@), shouldAutoDownload:%@ "
- "MessageService: Attachment download context is missing entries (signature = %@, ownerID = %@, fileSizeString = %@, encryptionKey = %@)"
- "Released pending attachment preview for %@ (%b)"
- "Scheduled message delivered without edits — keeping stored attachments and discarding %lu incoming transfer records"
- "Taking this file, we're good to grab it (this: %@ vs fileSizeString: %@)"
- "The first file wasn't allowed to auto download, let's look and see what we have... shouldAutoDownloadFile %@, lowQualityModeEnabled %@"
- "Will download file of size %@ "
- "__imFirstObject"
- "deviceIsLockedDown"
- "receiveFileTransfer:transferGUID:topic:path:requestURLString:ownerID:signature:decryptionKey:fileSize:balloonBundleID:senderContext:senderID:progressBlock:completionBlock:"
- "retrieveAttachmentsForMessage:inChat:inlineAttachments:displayID:topic:comingFromStorage:shouldForceAutoDownload:senderContext:completionBlock:lateDownloadCompletionBlock:"
- "send message: %@  guid: %@  to identifier: %@   chat: %@   callerURI: %@   self: %@   account: %@ associatedMessageGUID: %@  associatedMessageType: %lld  messageItemClass: %@ fileTransferGUID %@"
- "v36@?0B8B12B16q20q28"
- "v88@0:8@16@24@32@40@48B56B60@64@?72@?80"
```

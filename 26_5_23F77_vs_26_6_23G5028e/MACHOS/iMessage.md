## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0xc4fe8
-  __TEXT.__auth_stubs: 0x1c50
+1450.700.11.2.3
+  __TEXT.__text: 0xc8fe8
+  __TEXT.__auth_stubs: 0x1d20
   __TEXT.__objc_stubs: 0xd3e0
   __TEXT.__objc_methlist: 0x29dc
-  __TEXT.__const: 0xe58
-  __TEXT.__gcc_except_tab: 0xa168
-  __TEXT.__cstring: 0x337d
-  __TEXT.__oslogstring: 0x1765b
-  __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0x12924
-  __TEXT.__objc_methtype: 0x2c79
+  __TEXT.__const: 0x1040
+  __TEXT.__gcc_except_tab: 0xa1b0
+  __TEXT.__cstring: 0x33ad
+  __TEXT.__oslogstring: 0x1786b
+  __TEXT.__objc_classname: 0x68f
+  __TEXT.__objc_methname: 0x12994
+  __TEXT.__objc_methtype: 0x2c89
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x67e
-  __TEXT.__constg_swiftt: 0x370
-  __TEXT.__swift5_reflstr: 0x2d6
-  __TEXT.__swift5_fieldmd: 0x368
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift_as_entry: 0x48
-  __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__swift5_capture: 0x308
+  __TEXT.__swift5_typeref: 0x74e
+  __TEXT.__constg_swiftt: 0x480
+  __TEXT.__swift5_reflstr: 0x383
+  __TEXT.__swift5_fieldmd: 0x454
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift5_capture: 0x364
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2350
-  __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0xe38
+  __TEXT.__unwind_info: 0x2410
+  __TEXT.__eh_frame: 0xae8
+  __DATA_CONST.__auth_got: 0xea0
   __DATA_CONST.__got: 0x10f0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x3a88
+  __DATA_CONST.__const: 0x3de0
   __DATA_CONST.__cfstring: 0x3900
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x2e08
+  __DATA.__objc_const: 0x2ee0
   __DATA.__objc_selrefs: 0x3b00
   __DATA.__objc_ivar: 0x1c8
-  __DATA.__objc_data: 0x9c0
-  __DATA.__data: 0xa60
-  __DATA.__bss: 0x8f0
+  __DATA.__objc_data: 0x9c8
+  __DATA.__data: 0xb68
+  __DATA.__bss: 0x9f0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D0802B17-7D69-398E-BD86-F3BF01AA030F
-  Functions: 1674
-  Symbols:   897
-  CStrings:  5149
+  UUID: 1878B7A3-8838-34BD-A8D4-E9FE866FE138
+  Functions: 1738
+  Symbols:   905
+  CStrings:  5160
 
Symbols:
+ _IMBagIntValueWithDefault
+ _IMStringFromTransferState
+ __FTAreIDsEquivalent
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
CStrings:
+ "%{public}s IDS query timed out after %fs, failing %ld piggybacked handler(s)"
+ "%{public}s IDS query timed out or returned unexpected type"
+ "%{public}s Piggybacking on in-flight IDS query with request ID %{public}s for %s"
+ "%{public}s passing result to piggybacked request %{public}s"
+ "?8E"
+ "?:E"
+ "Allowing re-download of missing group photo. Incoming guid: %@ chatGuid: %@"
+ "Missing the item locally. transferGuid: %@, itemGuid: %@"
+ "Rejecting group photo update: transfer GUID already in use. Incoming guid: %@ existing guid: %@ transferState: %@ existsAtLocalPath: %@ chatGuid: %@"
+ "Rejecting group photo update: transfer GUID reuse for different group photo. Incoming guid: %@ existing guid: %@ chatGuid: %@"
+ "Saving context for BIA message with guid %@"
+ "_TtCC12iMessageCore29MessageReachabilityControllerP33_A99EE795A702D4F19DEBDB888277B70518InFlightIDSQueries"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:isBIAMessage:biaReferenceID:completionBlock:"
+ "imessage-ids-query-dedup-version"
+ "inFlightQueries"
+ "lockedInFlightQueries"
+ "v268@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232q240B248@252@?260"
- "?7E"
- "?9E"
- "Overriding isHidden to show because we are missing the item locally. transferGuid: %@, itemGuid: %@"
- "Received group photo with the same guid as we have -- dropping this message. Incoming guid: %@ existing guid: %@ chatGuid: %@"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:completionBlock:"
- "v256@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232q240@?248"

```

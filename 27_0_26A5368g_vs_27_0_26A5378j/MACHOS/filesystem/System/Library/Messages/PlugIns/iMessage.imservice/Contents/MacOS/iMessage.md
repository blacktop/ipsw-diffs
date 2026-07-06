## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

```diff

-  __TEXT.__text: 0x115b28
-  __TEXT.__auth_stubs: 0x2100
-  __TEXT.__objc_stubs: 0xe680
-  __TEXT.__objc_methlist: 0x3034
-  __TEXT.__const: 0x14e8
-  __TEXT.__gcc_except_tab: 0x9980
-  __TEXT.__cstring: 0x3cbd
-  __TEXT.__oslogstring: 0x1b9fb
+  __TEXT.__text: 0x118220
+  __TEXT.__auth_stubs: 0x2170
+  __TEXT.__objc_stubs: 0xe720
+  __TEXT.__objc_methlist: 0x303c
+  __TEXT.__const: 0x1588
+  __TEXT.__gcc_except_tab: 0x9894
+  __TEXT.__cstring: 0x3d7d
+  __TEXT.__oslogstring: 0x1bc5b
   __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x148b9
-  __TEXT.__objc_methtype: 0x3279
+  __TEXT.__objc_methname: 0x14a6e
+  __TEXT.__objc_methtype: 0x32a9
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0xdc6
-  __TEXT.__constg_swiftt: 0x5b0
+  __TEXT.__swift5_typeref: 0xe26
+  __TEXT.__constg_swiftt: 0x5e0
   __TEXT.__swift5_reflstr: 0x4e3
-  __TEXT.__swift5_fieldmd: 0x548
-  __TEXT.__swift5_proto: 0x64
-  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_fieldmd: 0x570
+  __TEXT.__swift5_proto: 0x6c
+  __TEXT.__swift5_types: 0x68
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift_as_cont: 0x13c
-  __TEXT.__swift5_capture: 0x998
+  __TEXT.__swift5_capture: 0x9b8
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2c28
-  __TEXT.__eh_frame: 0x19c8
-  __DATA_CONST.__const: 0x58a0
-  __DATA_CONST.__cfstring: 0x3c60
+  __TEXT.__unwind_info: 0x2c80
+  __TEXT.__eh_frame: 0x1a80
+  __DATA_CONST.__const: 0x5860
+  __DATA_CONST.__cfstring: 0x3d00
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x1090
-  __DATA_CONST.__got: 0x12a8
+  __DATA_CONST.__auth_got: 0x10c8
+  __DATA_CONST.__got: 0x12f0
   __DATA_CONST.__auth_ptr: 0x330
   __DATA.__objc_const: 0x3878
-  __DATA.__objc_selrefs: 0x4078
+  __DATA.__objc_selrefs: 0x40a8
   __DATA.__objc_ivar: 0x248
   __DATA.__objc_data: 0xc88
-  __DATA.__data: 0xdb0
-  __DATA.__bss: 0xf50
+  __DATA.__data: 0xdd8
+  __DATA.__bss: 0x1060
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2563
-  Symbols:   917
-  CStrings:  5741
+  Functions: 2588
+  Symbols:   920
+  CStrings:  5764
 
Sections:
~ __TEXT.__objc_classname : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _IMMetricsCollectorEventCKVEndpointFailure
+ _IMUTITypeForFilename
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ "   Group found, but failed validation. Dropping incoming group message payload %@. senderFailedValidation %{BOOL}d isPlaceholder %{BOOL}d"
+ "   Group found, but sender was not in the set of participants and was rejected. Dropping incoming group message payload %@."
+ "   No group found. A new group chat will get created with the new "
+ "   No group found. Dropping incoming group message payload %@."
+ "@72@0:8@16@24@32@40@48Q56^Q64"
+ "AssignToTransfer skipping stage:Final for transfer %@ — eager upload state is %{public}@, not success"
+ "Attachment preview finished uploading! We're now in preflight preview stage for transfer guid %@ on message guid %@"
+ "B68@0:8@16@24@32@40@48B56@60"
+ "Dropping group photo request -- sender is not a member in the chat."
+ "Early return receiving message before first unlock, ignoring incoming message of type Other from %@"
+ "Group Message Payload is from a known sender %@. The payload will continue processing."
+ "Group Message Payload is incoming on an unknown chat. The message type, %@, is not acceptable for an unknown chat and will be dropped."
+ "Group Message Payload is incoming on chat %@, which is a known chat. The payload will continue processing."
+ "Group Message Payload is incoming, but a chat was not found. The message type, %@, is not acceptable for a non-existant chat and will be dropped."
+ "Group Message Payload is of type %@ that is acceptable for both known and unknown senders. The payload will continue processing."
+ "Incoming group message payload from: %@   payload: %@  isReflection: %{BOOL}d  to: %@, timestamp: %@"
+ "Kickoff gradient send delay of %.0fs for message %@. %@"
+ "Not sending asset as a preview, since isVideo: %{BOOL}d, isOutputURLOfSmallestAttachment: %{BOOL}d, transfer stage: %@ for transfer guid %@ on message guid %@"
+ "Previews"
+ "Successfully configured transfer guid %@"
+ "TransferEagerUploadForceMMCSFailure"
+ "[TEST] Forcing synthetic MMCS upload failure for transfer %s on message %s"
+ "_configurePreviewTransfer:forMessage:usingAttachmentSendContexts:fileSizeKey:"
+ "_findChatFromIdentifier:toIdentifier:displayName:participants:groupID:validationOptions:failedValidations:"
+ "_generateAndAttachGradientsForMessage:completion:"
+ "_shouldAcceptGroupMessagePayloadWithFromIdentifier:toIdentifier:displayName:participants:groupID:isKnownSender:type:"
+ "areMyAliases:forService:"
+ "bestCandidateGroupChatWithFromIdentifier:toIdentifier:displayName:participants:updatingToLatestiMessageGroupID:sortedIdentifiers:serviceName:validationOptions:failedValidations:"
+ "ckv_endpoints"
+ "ckv_policy_failed_tag"
+ "extractCKVPerEndpointMetrics"
+ "isOneOfMyAliases:forService:"
+ "ktError"
+ "plas-gradient-preview-delay"
+ "receiver_type"
+ "setCkvUnderlyingErrorCode:"
+ "setCkvUnderlyingErrorDomain:"
+ "transparency"
+ "underlyingErrorCode"
+ "underlyingErrorDomain"
- "   No group found"
- "%ld transfer(s) for message %@ may need to upload a preview. %@"
- "-thumbnail"
- "B36@0:8@16B24@28"
- "Does not have thumbnails for all transfers for message %@, skipping thumbnail upload. %@"
- "Incoming group message payload from: %@   payload: %@  isReflection: %@  to: %@, timestamp: %@"
- "Not uploading a preview for transfer %@ (%lu/%lu) on message %@ because no thumbnail was available for transfer. %@"
- "Not uploading a preview for transfer %@ (%lu/%lu) on message %@ because no transfer was found. Silently ignoring failure. %@"
- "Received GenericGroupCommand from someone who is not in the group. fromIdentifier: %@ chatGuid: %@"
- "Registering for gradient send after 5s delay on message %@. %@"
- "Thumbnail upload failed for transfer %@ (%lu/%lu) on message %@ with error: %@. %@"
- "Thumbnail upload succeeded for transfer %@ (%lu/%lu) (%llu bytes) on message %@. %@"
- "Thumbnail upload succeeded for transfer %@ on message %@ but already in final stage! %@"
- "Thumbnail uploading completed for message %@. Ready to send preview(s), but may wait until gradient send completes if there is a gradient send in progress for this message. %@"
- "Thumbnail uploads complete for %@ success: %@"
- "Uploading thumbnail preview for transfer %@ (%lu/%lu) on message %@. %@"
- "_generateGradientsForMessage:completion:"
- "_shouldAcceptGroupMessagePayloadWithExistingChat:isKnownSender:type:"
- "_validateChat:containsFromIdentifier:isReflection:"
- "getNumberOfTimesRespondedToThread"
- "isOneOfMyAliases:"
- "uploadThumbnailPreviewForMessage:recipients:completion:"

```

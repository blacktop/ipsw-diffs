## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1447.100.7.2.3
-  __TEXT.__text: 0xb906c
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_stubs: 0xc3e0
-  __TEXT.__objc_methlist: 0x2b64
-  __TEXT.__const: 0xbb0
+1448.100.1.2.41
+  __TEXT.__text: 0xbcaf0
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_stubs: 0xc460
+  __TEXT.__objc_methlist: 0x2b7c
+  __TEXT.__const: 0xbf0
   __TEXT.__gcc_except_tab: 0xb4d0
   __TEXT.__cstring: 0x339d
-  __TEXT.__oslogstring: 0x163e6
+  __TEXT.__oslogstring: 0x168e6
   __TEXT.__objc_classname: 0x548
-  __TEXT.__objc_methname: 0x12401
+  __TEXT.__objc_methname: 0x1253e
   __TEXT.__objc_methtype: 0x2955
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x640
-  __TEXT.__constg_swiftt: 0x36c
+  __TEXT.__swift5_typeref: 0x662
+  __TEXT.__constg_swiftt: 0x38c
   __TEXT.__swift5_reflstr: 0x2b0
   __TEXT.__swift5_fieldmd: 0x35c
   __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift5_capture: 0x284
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift_as_entry: 0x44
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift5_capture: 0x308
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2300
-  __TEXT.__eh_frame: 0x740
-  __DATA_CONST.__auth_got: 0xd68
-  __DATA_CONST.__got: 0xfd8
+  __TEXT.__unwind_info: 0x2388
+  __TEXT.__eh_frame: 0x930
+  __DATA_CONST.__auth_got: 0xd90
+  __DATA_CONST.__got: 0xfe8
   __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x37c0
-  __DATA_CONST.__cfstring: 0x36c0
+  __DATA_CONST.__const: 0x38a8
+  __DATA_CONST.__cfstring: 0x36a0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x32a8
-  __DATA.__objc_selrefs: 0x39c0
+  __DATA.__objc_selrefs: 0x39f8
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0xa58
-  __DATA.__data: 0xa40
+  __DATA.__data: 0xa50
   __DATA.__bss: 0x7b0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 51BCB8FE-9344-3843-B210-69537E1A1C2D
-  Functions: 1641
-  Symbols:   855
-  CStrings:  5039
+  UUID: BD1A7903-575D-303A-AAC1-84310F0D85F8
+  Functions: 1667
+  Symbols:   860
+  CStrings:  5061
 
Symbols:
+ _OBJC_CLASS_$_IDSURI
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
CStrings:
+ "Asked by %s to send background info for chat %@"
+ "Asked to request background for chat if needed. incomingVersion: %llu, toIdentifier: %s, fromIdentifier: %s, chat: %s"
+ "Could not generate a readOnly poster for file %s. Got error: %s Bailing"
+ "Could not generate a readOnly poster for file %s. Response success: %{bool}d Bailing"
+ "Failed to parse background command for %s. Sender: %s"
+ "Found chat for identifier %s, callerURI: %s. Chat: %@"
+ "Found no background version in chat properties %s."
+ "Got a custom background request rate limit of %ld seconds"
+ "Got blastdoorCommand with no type."
+ "Got refresh blastdoorCommand with no backgroundVersion or posterWasRemoved flag."
+ "Got request response blastdoorCommand with no backgroundVersion or posterWasRemoved flag."
+ "Got update blastdoorCommand with no backgroundVersion or posterWasRemoved flag."
+ "Not downloading background for chat displayname: %s, already attempting a download for transfer ID: %s. Chat: %s"
+ "Preparing to fetch background asset for transferID: %s. Request URL: %s. To path: %s Chat: %@"
+ "Preparing to upload group background with transferID: %s"
+ "Refusing to receive transcript background. Sender context indicates untrusted sender."
+ "Successfully uploaded background with transferID %s."
+ "_currentCachedRemoteDevicesForDestinations:service:preferredFromID:listenerID:"
+ "_requestTranscriptBackground:toIdentifier:fromIdentifier:messageIsFromStorage:"
+ "generateReadOnlyPosterConfig:completionBlock:"
+ "initWithPrefixedURI:"
+ "isReceiverHQTransferCapable:fromID:"
+ "isTrustedSender"
+ "requestTranscriptBackground:toIdentifier:fromIdentifier:messageIsFromStorage:"
+ "setShouldNotTranscribeAudio:"
+ "shouldNotTranscribeAudio"
- "Not downloading background for chat %@, already attempting a download for transfer ID: %s"
- "_currentCachedRemoteDevicesForDestinations:service:listenerID:"
- "backwards-compat-enabled-translations"
- "isReceiverHQTransferCapable:"

```

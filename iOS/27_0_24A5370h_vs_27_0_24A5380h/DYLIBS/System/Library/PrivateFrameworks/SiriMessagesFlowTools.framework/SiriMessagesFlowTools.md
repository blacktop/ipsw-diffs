## SiriMessagesFlowTools

> `/System/Library/PrivateFrameworks/SiriMessagesFlowTools.framework/SiriMessagesFlowTools`

```diff

-  __TEXT.__text: 0x1054d0
+  __TEXT.__text: 0x104e18
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0xa874
-  __TEXT.__swift5_typeref: 0x34e6
+  __TEXT.__const: 0xa784
+  __TEXT.__swift5_typeref: 0x34da
   __TEXT.__swift5_reflstr: 0x1dc8
   __TEXT.__swift5_assocty: 0xcf0
-  __TEXT.__constg_swiftt: 0x1a58
-  __TEXT.__swift5_fieldmd: 0x20d8
+  __TEXT.__constg_swiftt: 0x1a3c
+  __TEXT.__swift5_fieldmd: 0x20b0
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_proto: 0x784
-  __TEXT.__swift5_types: 0x248
+  __TEXT.__swift5_proto: 0x780
+  __TEXT.__swift5_types: 0x244
   __TEXT.__swift_as_entry: 0x330
-  __TEXT.__swift_as_ret: 0x3f4
-  __TEXT.__cstring: 0x1c64
-  __TEXT.__swift_as_cont: 0x668
-  __TEXT.__oslogstring: 0x7941
-  __TEXT.__swift5_capture: 0x72c
+  __TEXT.__swift_as_ret: 0x3d8
+  __TEXT.__cstring: 0x1cb4
+  __TEXT.__swift_as_cont: 0x640
+  __TEXT.__oslogstring: 0x7a01
+  __TEXT.__swift5_capture: 0x6ec
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x37c8
-  __TEXT.__eh_frame: 0x8598
+  __TEXT.__unwind_info: 0x3720
+  __TEXT.__eh_frame: 0x82f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6d8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__got: 0x1020
-  __AUTH_CONST.__const: 0x47d8
+  __DATA_CONST.__got: 0xf98
+  __AUTH_CONST.__const: 0x46d0
   __AUTH_CONST.__objc_const: 0x14c0
-  __AUTH_CONST.__auth_got: 0x1fa8
-  __AUTH.__objc_data: 0x150
-  __AUTH.__data: 0x19d8
-  __DATA.__data: 0x2478
-  __DATA.__bss: 0xd6b0
-  __DATA.__common: 0x288
-  __DATA_DIRTY.__data: 0x390
-  __DATA_DIRTY.__bss: 0x880
+  __AUTH_CONST.__auth_got: 0x1fb0
+  __AUTH.__objc_data: 0x98
+  __AUTH.__data: 0xec8
+  __DATA.__data: 0x19b8
+  __DATA.__bss: 0xb4b0
+  __DATA.__common: 0x1c8
+  __DATA_DIRTY.__objc_data: 0xb8
+  __DATA_DIRTY.__data: 0x19c0
+  __DATA_DIRTY.__bss: 0x2a00
+  __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5336
-  Symbols:   7388
-  CStrings:  591
+  Functions: 5285
+  Symbols:   7307
+  CStrings:  596
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
Symbols:
- ___swift_memcpy8_8
- _get_enum_tag_for_layout_string 21SiriMessagesFlowTools27MessageEntityHydrationErrorO
- _get_type_metadata 15Synchronization5MutexVy21SiriMessagesFlowTools23TimedSentMessageContextVSgG noncopyable
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic _____ 21SiriMessagesFlowTools27MessageEntityHydrationErrorO
- _type_layout_string 21SiriMessagesFlowTools27MessageEntityHydrationErrorO
CStrings:
+ "#EditLastMessageSentWithSiriTool routing decision: %{public}s"
+ "#EditLastMessageSentWithSiriTool: hydration failed for non-attributed entity; falling back to cached identifier: %{public}s"
+ "#SendDraftMessageTool using recipients from draft for snippet"
+ "#TimedSentMessageContext bundleIdentifier: empty entityIdentifierValues"
+ "#TimedSentMessageContext typeName: empty entityIdentifierValues"
+ "#TimedSentMessageContext typeName: unhandled TypeIdentifier case=%{public}s"
+ "#UnsendLastMessageSentWithSiriTool execute: cache miss — no sent message context available"
+ "#UnsendLastMessageSentWithSiriTool routing decision: %{public}s"
+ "#UnsendLastMessageSentWithSiriTool searching for tools by schema for app=%{public}s"
+ "#UnsendLastMessageSentWithSiriTool unsupported service: %s"
+ "#UnsendLastMessageSentWithSiriTool: hydration failed for non-attributed entity; proceeding with cached entity reference only: %{public}s"
+ ".attributed(containerId="
+ ".custom(bundleIdentifier="
+ "MESSAGESFLOWTOOL_UNSEND_UNSUPPORTED_ON_SERVICE"
+ "You can’t unsend messages sent using SMS or RCS."
+ "invokeAppIntentForEntity(entity:toolDefinition:callback:skipConfirmation:)"
- "#EditLastMessageSentWithSiriTool %s: Failed to hydrate conversation entity: %s"
- "#MessageEntity hydration failed: Could not find conversation type"
- "#MessageEntity hydration failed: Could not find message type"
- "#SendDraftMessageTool skipping hydration of conversation entity -- using recipients from draft due to latency"
- "#TTSUtil isAvailable for '%s': matchedBaseLanguage=%{bool}d, hasAnyKeyboardForLanguage=%{bool}d"
- "#TimedSentMessageContext: Could not extract type from entityIdentifierValues: %{private}s"
- "#UnsendLastMessageSentWithSiriTool searching for tools by schema for app %s"
- "#UnsendLastMessageSentWithSiriTool: Failed to hydrate entity for snippet: %s"
- "MessageEntity: Failed to hydrate conversation entity - %@"
- "hydrateMessageEntity(sentMessageContext:callback:)"
- "invokeAppIntentForEntity(entity:toolDefinition:bundleIdentifier:typeName:callback:skipConfirmation:)"

```

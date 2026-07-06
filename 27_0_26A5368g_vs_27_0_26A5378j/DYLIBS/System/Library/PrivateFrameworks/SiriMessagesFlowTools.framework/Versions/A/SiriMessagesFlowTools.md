## SiriMessagesFlowTools

> `/System/Library/PrivateFrameworks/SiriMessagesFlowTools.framework/Versions/A/SiriMessagesFlowTools`

```diff

-  __TEXT.__text: 0xf88b8
+  __TEXT.__text: 0xf8764
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0xa784
-  __TEXT.__swift5_typeref: 0x3428
+  __TEXT.__const: 0xa6a4
+  __TEXT.__swift5_typeref: 0x341c
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
   __TEXT.__swift_as_entry: 0x304
-  __TEXT.__swift_as_ret: 0x3b4
-  __TEXT.__cstring: 0x1b64
-  __TEXT.__swift_as_cont: 0x5f8
-  __TEXT.__oslogstring: 0x6c51
-  __TEXT.__swift5_capture: 0x638
+  __TEXT.__swift_as_ret: 0x3a0
+  __TEXT.__cstring: 0x1bb4
+  __TEXT.__swift_as_cont: 0x5d8
+  __TEXT.__oslogstring: 0x6d71
+  __TEXT.__swift5_capture: 0x5f8
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x3778
-  __TEXT.__eh_frame: 0x7db0
+  __TEXT.__unwind_info: 0x36f8
+  __TEXT.__eh_frame: 0x7bd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__got: 0xff8
-  __AUTH_CONST.__const: 0x4558
+  __DATA_CONST.__got: 0xf60
+  __AUTH_CONST.__const: 0x4450
   __AUTH_CONST.__objc_const: 0x14c0
-  __AUTH_CONST.__auth_got: 0x1d50
-  __AUTH.__objc_data: 0x150
-  __AUTH.__data: 0x19d8
-  __DATA.__data: 0x23f0
-  __DATA.__bss: 0xd6b0
-  __DATA.__common: 0x288
-  __DATA_DIRTY.__data: 0x390
-  __DATA_DIRTY.__bss: 0x880
+  __AUTH_CONST.__auth_got: 0x1d58
+  __AUTH.__objc_data: 0x98
+  __AUTH.__data: 0xec8
+  __DATA.__data: 0x1978
+  __DATA.__bss: 0xb4b0
+  __DATA.__common: 0x1c8
+  __DATA_DIRTY.__objc_data: 0xb8
+  __DATA_DIRTY.__data: 0x1958
+  __DATA_DIRTY.__bss: 0x2a00
+  __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5164
-  Symbols:   4478
-  CStrings:  531
+  Functions: 5120
+  Symbols:   4442
+  CStrings:  537
 
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
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic _____ 21SiriMessagesFlowTools27MessageEntityHydrationErrorO
- _type_layout_string 21SiriMessagesFlowTools27MessageEntityHydrationErrorO
- get_type_metadata 15Synchronization5MutexVy21SiriMessagesFlowTools23TimedSentMessageContextVSgG noncopyable
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
- "#TimedSentMessageContext: Could not extract type from entityIdentifierValues: %{private}s"
- "#UnsendLastMessageSentWithSiriTool searching for tools by schema for app %s"
- "#UnsendLastMessageSentWithSiriTool: Failed to hydrate entity for snippet: %s"
- "MessageEntity: Failed to hydrate conversation entity - %@"
- "hydrateMessageEntity(sentMessageContext:callback:)"
- "invokeAppIntentForEntity(entity:toolDefinition:bundleIdentifier:typeName:callback:skipConfirmation:)"

```

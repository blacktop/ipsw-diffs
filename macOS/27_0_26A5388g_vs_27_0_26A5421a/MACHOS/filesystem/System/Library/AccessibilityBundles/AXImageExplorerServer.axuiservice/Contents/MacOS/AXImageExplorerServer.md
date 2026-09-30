## AXImageExplorerServer

> `/System/Library/AccessibilityBundles/AXImageExplorerServer.axuiservice/Contents/MacOS/AXImageExplorerServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`

```diff

-3237.0.0.0.0
-  __TEXT.__text: 0x53cfc
-  __TEXT.__auth_stubs: 0x2600
+3240.0.1.2.0
+  __TEXT.__text: 0x549b0
+  __TEXT.__auth_stubs: 0x2700
   __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x27c
-  __TEXT.__swift5_typeref: 0x637a
-  __TEXT.__const: 0x2ae4
+  __TEXT.__swift5_typeref: 0x6536
+  __TEXT.__const: 0x2b84
   __TEXT.__constg_swiftt: 0x948
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x647
-  __TEXT.__swift5_fieldmd: 0x5c8
+  __TEXT.__swift5_reflstr: 0x6b7
+  __TEXT.__swift5_fieldmd: 0x5f8
   __TEXT.__swift5_assocty: 0x2b0
-  __TEXT.__cstring: 0x105b
-  __TEXT.__swift5_capture: 0x40c
+  __TEXT.__cstring: 0x11db
+  __TEXT.__swift5_capture: 0x3c8
   __TEXT.__swift5_proto: 0xfc
   __TEXT.__swift5_types: 0x84
   __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0xeeb
+  __TEXT.__objc_methname: 0xf5b
   __TEXT.__objc_methtype: 0x406
-  __TEXT.__oslogstring: 0x1249
-  __TEXT.__swift_as_entry: 0x94
-  __TEXT.__swift_as_ret: 0xd8
-  __TEXT.__swift_as_cont: 0x1e8
+  __TEXT.__oslogstring: 0x1349
+  __TEXT.__swift_as_entry: 0x88
+  __TEXT.__swift_as_ret: 0xc0
+  __TEXT.__swift_as_cont: 0x1c4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x11e8
-  __TEXT.__eh_frame: 0x2838
-  __DATA_CONST.__const: 0x12b0
+  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__eh_frame: 0x2598
+  __DATA_CONST.__const: 0x1210
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x1308
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__auth_ptr: 0x810
-  __DATA.__objc_const: 0x830
+  __DATA_CONST.__auth_got: 0x1388
+  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__auth_ptr: 0x830
+  __DATA.__objc_const: 0x870
   __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_data: 0x268
-  __DATA.__data: 0x1be0
-  __DATA.__bss: 0x20b8
+  __DATA.__objc_data: 0x278
+  __DATA.__data: 0x1c50
+  __DATA.__bss: 0x20d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accessibility.framework/Versions/A/Accessibility

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1282
+  Functions: 1288
   Symbols:   203
-  CStrings:  377
+  CStrings:  395
 
Symbols:
+ _AXDateStringForFormatWithTimeZone
+ _AXImageExplorerProcessingSoundEnabled
+ _swift_asyncLet_get_throwing
+ _swift_task_future_wait_throwing
- _AXDateStringForFormat
- _AXDeviceSupportsAppleIntelligence
- _AXImageExplorerGetSilentMode
- _swift_asyncLet_get
CStrings:
+ "$__lazy_storage_$_multimodalGuardrail"
+ "%s cancelled."
+ "%s failed. %@"
+ "%s rejected by an unrecognized safety guardrail. %@"
+ "%s timed out after %ld attempt(s)."
+ "ASK_ABOUT_SCREEN"
+ "Ask about image request"
+ "Fail to prompt Siri request. AXChatProvider is not available."
+ "Failed to ask user prompt. AXChatProvider is not available."
+ "Failed to fetch image description: %s."
+ "Failed to request description. AXChatProvider is not available."
+ "Failed to request description. Creating fallback message for user."
+ "Failed to request description. Image was nil."
+ "Failed to request description. Intelligence is not enabled and vision analysis failed."
+ "INTELLIGENT_IMAGE_DESCRIPTION"
+ "INTELLIGENT_IMAGE_SENSITIVE_CONTENT"
+ "INTELLIGENT_QUESTION_SENSITIVE_CONTENT"
+ "INTELLIGENT_SCREEN_DESCRIPTION"
+ "INTELLIGENT_SCREEN_SENSITIVE_CONTENT"
+ "Image Explorer description request"
+ "Image Explorer question request"
+ "Intelligent description request"
+ "PARENTAL_RESTRICTION_ALERT_MESSAGE"
+ "PARENTAL_RESTRICTION_ALERT_OK"
+ "PARENTAL_RESTRICTION_ALERT_TITLE"
+ "Rejected by output safety guardrail. %s rejectedContent=%{sensitive}s"
+ "Requested description rejected by output safety guardrail. %@"
+ "Safety rejection due to offensive words - providing content to user."
+ "Service got a message: %ld from client: %s."
+ "Service got async message: %ld from client: %s."
+ "Unknown async message: '%ld' from client: '%s'."
+ "Unknown message: '%ld' from client: '%s'."
+ "_showingRestrictionAlert"
+ "_sourceIsItem"
+ "accessibility.magnifier.reduceSensitiveTopics"
- "AFM_FAILED_RESPONSE"
- "AXChatProvider is not available."
- "Failed to ask user prompt. %@"
- "Failed to fetch image description within %ld seconds or due to error."
- "Failed to fetch image description."
- "Failed to fetch model result. %@"
- "Failed to generate image description: empty result."
- "IMAGE_EXPLORER_SENSITIVE_CONTENT"
- "IMAGE_EXPLORER_SENSITIVE_CONTENT_ASK"
- "IMAGE_EXPLORER_SENSITIVE_CONTENT_DESCRIPTION"
- "Service got a message: %ld from client: %s. Payload: %s."
- "Service got async message: %ld from client: %s. Payload: %s."
- "Unknown async message: '%ld' from client: '%s' with payload: '%s'."
- "Unknown message: '%ld' from client: '%s' with payload: '%s'."
- "Will not proceed with presenting Image Explorer. Guardrail evaluation failed: %@"
- "Will not proceed with speak description. Guardrail evaluation failed: %@"
- "multimodalGuardrail"
```

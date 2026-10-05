## IntelligenceFlowPlannerRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime`

```diff

-3605.16.9.501.1
-  __TEXT.__text: 0x71ecb8
+3605.21.1.501.4
+  __TEXT.__text: 0x73e2bc
   __TEXT.__objc_methlist: 0x34c
-  __TEXT.__const: 0x2a580
-  __TEXT.__swift5_typeref: 0xd9f8
-  __TEXT.__oslogstring: 0x2374c
-  __TEXT.__cstring: 0x178ba
-  __TEXT.__constg_swiftt: 0xbedc
-  __TEXT.__swift5_reflstr: 0xae33
-  __TEXT.__swift5_fieldmd: 0xc570
+  __TEXT.__const: 0x2a840
+  __TEXT.__cstring: 0x17b2a
+  __TEXT.__swift5_typeref: 0xdb1e
+  __TEXT.__constg_swiftt: 0xbfa4
+  __TEXT.__swift5_fieldmd: 0xc614
   __TEXT.__swift5_builtin: 0x30c
+  __TEXT.__swift5_reflstr: 0xaef3
   __TEXT.__swift5_assocty: 0x948
-  __TEXT.__swift5_proto: 0x196c
-  __TEXT.__swift5_types: 0xebc
-  __TEXT.__swift_as_entry: 0x1178
-  __TEXT.__swift_as_ret: 0x178c
-  __TEXT.__swift_as_cont: 0x2e78
+  __TEXT.__swift5_proto: 0x1974
+  __TEXT.__swift5_types: 0xecc
+  __TEXT.__oslogstring: 0x23d8c
+  __TEXT.__swift_as_entry: 0x11c8
+  __TEXT.__swift_as_ret: 0x1834
+  __TEXT.__swift_as_cont: 0x2f6c
   __TEXT.__swift5_protos: 0x1d4
-  __TEXT.__swift5_capture: 0x6dcc
+  __TEXT.__swift5_capture: 0x7004
   __TEXT.__swift5_mpenum: 0xd8
   __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__unwind_info: 0x19260
-  __TEXT.__eh_frame: 0x3f320
+  __TEXT.__unwind_info: 0x19438
+  __TEXT.__eh_frame: 0x405f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7b8
-  __DATA_CONST.__objc_classlist: 0x478
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0xa00
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x5358
-  __AUTH_CONST.__const: 0x26e48
-  __AUTH_CONST.__objc_const: 0x9618
+  __DATA_CONST.__got: 0x54a0
+  __AUTH_CONST.__const: 0x27558
+  __AUTH_CONST.__objc_const: 0x96a8
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xb640
+  __AUTH_CONST.__auth_got: 0xb860
   __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x4640
+  __AUTH.__data: 0x4760
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x5290
-  __DATA.__common: 0x129
+  __DATA.__data: 0x5388
+  __DATA.__common: 0x131
   __DATA_DIRTY.__objc_data: 0xc90
-  __DATA_DIRTY.__data: 0x10268
+  __DATA_DIRTY.__data: 0x10220
   __DATA_DIRTY.__bss: 0x8990
   __DATA_DIRTY.__common: 0x4b8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 34682
-  Symbols:   478
-  CStrings:  3770
+  Functions: 35181
+  Symbols:   479
+  CStrings:  3801
 
Symbols:
+ _NSMultipleUnderlyingErrorsKey
CStrings:
+ " Key data points (e.g. for retrieval or list queries, name the items themselves) must appear in the prose or via ui_entity_rendering for entities that have ui_entity_rendering_text_components, or associated renderable entities of web search results — by calling ui_entity_rendering on those entities you have already presented their data to the user, do not restate it in either <"
+ " Questions go in <followUp>, never the response body. When asking the user to choose among candidate entities, use ask_user_to_pick with them instead, as <followUp> cannot present them."
+ "# Tool Catalog Appendix"
+ "## First check\nIf the request is not aimed at you, call `mitigate` and stop.\nNever call `mitigate` if the user is addressing Siri by name.\nTalking about Siri is not addressing Siri."
+ "%s %ld consecutive guardrail violations reached limit of %ld, locking conversation"
+ "%s %ld/%ld consecutive violations, replacing response"
+ "%s Failed to post SafetyIncident: %@"
+ "%s: AgenticPlannerService: fuzzy match found a non-schematized shortcut, but shortcuts can't run on the originating device; declining"
+ "%s: Failed to post selected contextual mitigation before streaming lockout: %@"
+ "%s: In-app search capability query failed, offering search_in_app anyway: %{sensitive}@"
+ "%s: Output content safety rejected by PCC — replacing response"
+ "%s: Skipping search_in_app — no span-matched app supports in-app search: %{public}s"
+ "%s: [RateLimit] kind: %{public}s, pccCode: %{public}s, retryAfter: %{public}s, retryable: %{bool,public}d"
+ "%s: failed to post rate-limit ExecutionError: %@"
+ "%s: finalApprovalWithOverride failed during %s: %@"
+ "%s: finalApprovalWithOverride failed during output safety rejection: %@"
+ "%s: finalApprovalWithSubstitution failed during %s: %@"
+ "%s: insert_text unavailable for this device idiom — suppressing writing instructions"
+ "%{public}s isPassiveCameraEnabled=%{bool,public}d"
+ "%{public}s isTypeToSiri=%{bool,public}d"
+ ": [PCCOutputGuardrail]"
+ "<elided: budget exhausted>"
+ "<expanded below as an underlying node>"
+ "<field depth cap>"
+ ">. By calling ui_entity_rendering on entities with ui_entity_rendering_text_components, or associated renderable entities of web search results you have already presented their data to the user — do not restate it after <"
+ "GMS output stream failed with PCC privacy-proxy error: %@"
+ "Missing dialog resources for %{public}s"
+ "OutputGuardrailLazyModelLoad"
+ "PrivateCloudComputeError"
+ "SpeculativeExecution: Retry path - refinement modified output, abandoning speculative work and retrying"
+ "ToolSequenceSafetyValidator: %s threshold reached — count=%ld, threshold=%ld (transcript: %ld, persisted: %ld)"
+ "[CloudGuardrail] sending %{public}s"
+ "[ForegroundAppSource] Client foreground app %s matched candidates %s"
+ "[ForegroundAppSource] Client reported no foreground app"
+ "[ForegroundAppSource] Local device foreground apps %s"
+ "[MarkdownResponseStreamConsumer]"
+ "[OutputGuardrailLockout] No dialog generated for guardrail replacement"
+ "[PCCPrivacyProxy] underlying error chain deeper than %ld, giving up"
+ "[SanitizerGuardrailModel] Initialized, prewarm deferred to first use (useCaseIdentifier: %s)"
+ "[UnclassifiedInferenceError] hierarchy:\n%{public}s"
+ "[handleCitation] Withholding pill for id=%s; no attributable source for '%{public}s'"
+ "localizedDescription"
+ "mangledSwiftTypeName"
+ "on_screen_context"
+ "recitation rejection"
+ "resuming flow tool after dismissal StatementID: %s"
- " If you ask a question, wrap it in <followUp> — it will be spoken so you must not duplicate the question outside the tag."
- " Key data points (e.g. for retrieval or list queries, name the items themselves) must appear in the prose or via ui_entity_rendering for entities that have ui_entity_rendering_text_components — by calling ui_entity_rendering on those entities you have already presented their data to the user, do not restate it in either <"
- "# Tool Catalog Appendix\n\n"
- "## First check\nIf the user is not making a clear request/question, call `mitigate` and stop"
- "%s: finalApprovalWithOverride failed during recitation rejection: %@"
- ">. By calling ui_entity_rendering on entities with ui_entity_rendering_text_components you have already presented their data to the user — do not restate it after <"
- "Missing .actionNotAllowed dialog resources"
- "SpeculativeExecution: Retry path - refinement modified output, cancelling speculative work and retrying"
- "ToolSequenceSafetyValidator: %s threshold reached — count=%ld, threshold=%ld (persisted: %ld)"
- "[MarkdownResponseStreamConsumer] %ld consecutive guardrail violations reached limit of %ld, locking conversation"
- "[MarkdownResponseStreamConsumer] %ld/%ld consecutive violations, replacing response"
- "[MarkdownResponseStreamConsumer] Failed to post SafetyIncident: %@"
- "[MarkdownResponseStreamConsumer] No dialog generated for guardrail replacement"
- "[handleCitation] No displayName for entity citation id=%s"
- "forceReduceSensitiveContent"
```

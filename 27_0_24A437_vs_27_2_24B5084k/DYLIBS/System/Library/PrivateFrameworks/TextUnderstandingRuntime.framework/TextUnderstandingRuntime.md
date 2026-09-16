## TextUnderstandingRuntime

> `/System/Library/PrivateFrameworks/TextUnderstandingRuntime.framework/TextUnderstandingRuntime`

```diff

-176.3.0.1.0
-  __TEXT.__text: 0x21a704
+186.0.0.0.0
+  __TEXT.__text: 0x21ad88
   __TEXT.__objc_methlist: 0x728
-  __TEXT.__const: 0x12b98
-  __TEXT.__constg_swiftt: 0x3748
-  __TEXT.__swift5_typeref: 0x4d3b
+  __TEXT.__const: 0x12a78
+  __TEXT.__constg_swiftt: 0x3770
+  __TEXT.__swift5_typeref: 0x4cff
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x2f3c
-  __TEXT.__swift5_fieldmd: 0x3f6c
-  __TEXT.__swift5_assocty: 0xf88
-  __TEXT.__swift5_proto: 0x106c
+  __TEXT.__swift5_reflstr: 0x2e8c
+  __TEXT.__swift5_fieldmd: 0x3f04
+  __TEXT.__swift5_assocty: 0xf58
+  __TEXT.__swift5_proto: 0x105c
   __TEXT.__swift5_types: 0x4a4
   __TEXT.__swift_as_entry: 0x580
-  __TEXT.__swift_as_ret: 0x76c
-  __TEXT.__swift_as_cont: 0xd00
-  __TEXT.__cstring: 0x5082
-  __TEXT.__oslogstring: 0x974a
+  __TEXT.__swift_as_ret: 0x774
+  __TEXT.__swift_as_cont: 0xd10
+  __TEXT.__cstring: 0x4852
+  __TEXT.__oslogstring: 0x97aa
   __TEXT.__swift5_capture: 0x1d9c
-  __TEXT.__swift5_protos: 0x8c
+  __TEXT.__swift5_protos: 0x90
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x8b48
-  __TEXT.__eh_frame: 0x156ac
+  __TEXT.__unwind_info: 0x8b00
+  __TEXT.__eh_frame: 0x15694
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf08
+  __DATA_CONST.__objc_selrefs: 0xf00
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xead8
+  __AUTH_CONST.__const: 0xe898
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2ac0
-  __AUTH_CONST.__auth_got: 0x4208
+  __AUTH_CONST.__objc_const: 0x2b20
+  __AUTH_CONST.__auth_got: 0x42a8
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x1008
-  __DATA.__data: 0x2fc0
+  __DATA.__data: 0x2fa0
   __DATA.__common: 0x1c0
   __DATA_DIRTY.__objc_data: 0x530
-  __DATA_DIRTY.__data: 0x3528
-  __DATA_DIRTY.__bss: 0x3380
+  __DATA_DIRTY.__data: 0x34e8
+  __DATA_DIRTY.__bss: 0x3100
   __DATA_DIRTY.__common: 0x328
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12211
-  Symbols:   575
-  CStrings:  998
+  Functions: 12196
+  Symbols:   578
+  CStrings:  995
 
Symbols:
+ _CSEventStatusConfirmed
+ _CSEventStatusUpdated
+ _OBJC_CLASS_$_NSProcessInfo
CStrings:
+ "EventsPipeline: device not eligible for Apple Intelligence, running regex events and returning"
+ "EventsPipeline: document language not supported, running regex events and returning"
+ "IdentificationDocumentEligibilityProcessor: Will skip gating for ID classification: %{bool}d for document kind: %s"
+ "IdentificationDocumentEligibilityProcessor: unsupported request types"
+ "IdentificationDocumentProcessor: Will skip gating for ID classification: %{bool}d for document kind: %s"
+ "OpenEndedExtraction: fixed prompt cost %ld tokens exceeds input budget of %ld tokens; skipping document"
+ "OpenEndedExtractionSchemaDetector: %{public}s missing from adapter metadata; falling back to %{public}s"
+ "Running input safety for use case identifier %s"
+ "Skipping input safety for use case %s since it has already run"
+ "TextUnderstandingRuntime/IdentificationDocumentEligibilityProcessor.swift"
+ "com.apple.textComposition.OpenEndedExtract.applicableactionsmessage"
- "EventsPipeline: device not eligible for Apple Intelligence, geocoding regex events and returning"
- "EventsPipeline: document language not supported, geocoding regex events and returning"
- "IdentificationDocumentProcessor: image dimensions (%ldx%ld) exceed maximum allowed (%ldx%ld), falling back to text-only processing"
- "OEE9MClassifierAdapter: Classification failed: %@"
- "OEE9MClassifierAdapter: Classified document as '%s'"
- "OEE9MClassifierAdapter: applicable actions prompt template unavailable, falling back to legacy classification"
- "OpenEndedExtractionAdapter: Truncated document text from %ld to %ld characters"
- "Task: Classify Content into Structured Information Categories\nObjective:\nAnalyze the following content and classify it into a predefined category based on the presence of structured, actionable information.\nClassification Categories:\n- \"appointment\": Confirmed business appointment with specific date/time\n- \"order_updates\": Order confirmation, purchase receipt, shipping notification\n- \"receipts\": Purchase receipt or transaction confirmation with amount/payment details (no physical delivery)\n- \"invitation\": Event invitation or meeting request\n- \"ticket\": General entertainment or event ticket confirmation\n- \"flight\": Airline booking or flight reservation\n- \"transport_ticket\": Train, bus, or other transportation reservation\n- \"hotel\": Lodging or accommodation reservation\n- \"shipping_updates\": Package tracking or delivery information\n- \"movie\": Specific movie ticket or cinema booking\n- \"restaurant\": Restaurant reservation\n- \"car\": Car rental or automotive service booking\n- \"no_event\": No extractable structured information (marketing emails, newsletters, general promotions)\nClassification Guidelines:\n1. Prioritize specific structured information over generic text\n2. Look for key indicators like:\n   - Dates and times\n   - Ticket/booking references\n   - Reservation details\n   - Explicit event or service confirmations\n   - Transaction amounts and payment details (for receipts)\n3. If no clear structured information is present, default to \"no_event\"\n4. Be cautious of misleading subject lines or promotional language\n5. Receipts differ from orders - receipts are for completed transactions without physical delivery tracking\nOutput:\n- Single lowercase string representing the most appropriate category\n- Examples: \"ticket\", \"flight\", \"receipts\", \"no_event\"\nKey Considerations:\n- Content with ticket purchase language but no concrete booking details should be carefully evaluated\n- Promotional content with ticket-like language should typically be classified as \"no_event\"\n\n[Input Text]"
- "no_event"
- "order_updates"
- "receipts"
- "shipping_updates"
- "transport_ticket"
- "{{ specialToken.chat.role.system }}{{ specialToken.chat.component.turnEnd }}{{ specialToken.chat.role.user }}{{ userContent }}{{ specialToken.chat.component.turnEnd }}{{ specialToken.chat.role.assistant }}"
```

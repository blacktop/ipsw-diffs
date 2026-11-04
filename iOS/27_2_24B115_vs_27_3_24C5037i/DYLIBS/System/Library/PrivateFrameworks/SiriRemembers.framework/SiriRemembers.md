## SiriRemembers

> `/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers`

```diff

-3605.20.1.0.0
-  __TEXT.__text: 0xb11bc
+3610.9.1.0.0
+  __TEXT.__text: 0xb3984
   __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x9bc4
-  __TEXT.__cstring: 0x3461
-  __TEXT.__oslogstring: 0x4165
-  __TEXT.__constg_swiftt: 0x209c
-  __TEXT.__swift5_typeref: 0x28f1
-  __TEXT.__swift5_reflstr: 0x12d2
-  __TEXT.__swift5_fieldmd: 0x25f8
+  __TEXT.__const: 0x9d64
+  __TEXT.__cstring: 0x34b1
+  __TEXT.__oslogstring: 0x4065
+  __TEXT.__constg_swiftt: 0x2064
+  __TEXT.__swift5_typeref: 0x2951
+  __TEXT.__swift5_reflstr: 0x13e2
+  __TEXT.__swift5_fieldmd: 0x2698
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_proto: 0x85c
-  __TEXT.__swift5_types: 0x2bc
-  __TEXT.__swift5_assocty: 0x2d0
+  __TEXT.__swift5_proto: 0x86c
+  __TEXT.__swift5_types: 0x2b4
+  __TEXT.__swift5_assocty: 0x300
   __TEXT.__swift5_capture: 0xccc
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x36f0
-  __TEXT.__eh_frame: 0x4d70
+  __TEXT.__unwind_info: 0x3770
+  __TEXT.__eh_frame: 0x4c90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7648
+  __AUTH_CONST.__const: 0x7938
   __AUTH_CONST.__objc_const: 0x1540
-  __AUTH_CONST.__auth_got: 0x1818
+  __AUTH_CONST.__auth_got: 0x1850
   __AUTH.__data: 0x570
-  __DATA.__data: 0x1530
+  __DATA.__data: 0x1570
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x118
   __DATA_DIRTY.__data: 0x2c38

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5186
-  Symbols:   1639
-  CStrings:  555
+  Functions: 5237
+  Symbols:   1644
+  CStrings:  554
 
Symbols:
+ _associated conformance 13SiriRemembers20MediaDonationBuilderV0C10EntityTypeOSHAASQ
+ _associated conformance 13SiriRemembers20MediaDonationBuilderV0C10EntityTypeOs12CaseIterableAA8AllCasessAFP_Sl
+ _symbolic Say_____G 13SiriRemembers20MediaDonationBuilderV0C10EntityTypeO
+ _symbolic SiSg
+ _symbolic _____ 13SiriRemembers20MediaDonationBuilderV0C10EntityTypeO
+ _symbolic _____3key_SS5valuet 13SiriRemembers17ParameterKeyValueO
+ _symbolic _____ySNySiGG s23_ContiguousArrayStorageC
+ _symbolic _____yShySSGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____3key_SS5valuetG s23_ContiguousArrayStorageC 13SiriRemembers17ParameterKeyValueO
- _swift_retain_x13
- _symbolic _____ 13SiriRemembers17AnswerCallHandlerV
- _symbolic _____ 13SiriRemembers24StartFaceTimeCallHandlerV
- _symbolic _____ 13SiriRemembers25StartTelephonyCallHandlerV
CStrings:
+ ", devicePlatform: "
+ ", durationSeconds: "
+ ", groupIdentifier: "
+ ", handlingStatus: "
+ ", userDonatorType: "
+ "AppIntent event has no body. timestamp=%f"
+ "Cannot convert INInteraction to Donation; invalid bundleId. intent=%s, identifier=%s"
+ "Cannot convert INInteraction to Donation; missing dateInterval. intent=%s, identifier=%s"
+ "Cannot convert INInteraction to Donation; missing id. intent=%s, identifier=%s"
+ "Checking the interaction StartDate with interaction id: %s, type: %s, bundleId: %s, donatedTs: %f, startDateTs: %f"
+ "EntityHashProperties(externalIdentifier: "
+ "Interaction(id: "
+ "MediaDonationBuilder: Creating INPlayMediaIntent with mediaItems: %ld and mediaSearch type: %s"
+ "MediaDonationBuilder: extract INMediaItem for entityType: %s"
+ "MediaDonationBuilder: lnEntityValue typeIdentifier: %s"
+ "MessageDonationBuilder: derived the spokenPhrase from conversationName"
+ "MessageDonationBuilder: the recipients count is %ld"
+ "PhoneDonationBuilder: Extracting person arrays from LNValue with valueType: %s"
+ "PhoneDonationBuilder: Found property for %s in entity"
+ "PhoneDonationBuilder: extract AudioVisualMode entity from entity properties: %s"
+ "SiriSuggestionsBiomeEventBackFiller: Unexpected empty record in eventBody. timestamp=%f"
+ "SiriSuggestionsBiomeEventBackFiller: event at timestamp: %f does not have an interaction id. Skipping..."
+ "The INPlayMediaIntent mediaItems: %ld, mediaSearch type: %s, hasMediaContainer: %{bool}d"
+ "appIntentInteractionIdentifier: "
+ "hashProperties: "
+ "isDonatedBySiri: "
- "AnswerCallHandler: Start extraction of the parameters"
- "AnswerCallIntent"
- "AppIntent event has no body. event=%s"
- "Cannot convert INInteraction to Donation; invalid bundleId: %@"
- "Cannot convert INInteraction to Donation; missing dateInterval: %@"
- "Cannot convert INInteraction to Donation; missing id: %@"
- "Checking the interaction StartDate with interaction %s, donatedTs: %f, startDateTs: %f"
- "MediaDonationBuilder: Creating INPlayMediaIntent with mediaItems: %s and mediaSearch type: %s"
- "MediaDonationBuilder: extract INMediaItem for %s"
- "MediaDonationBuilder: lnEntityValue: %s"
- "MessageDonationBuilder: the recipients is %s"
- "MessageDonationBuilder: the spokenPhrase is %s"
- "PhoneDonationBuilder: Expected linkEnumeration container type, got: "
- "PhoneDonationBuilder: Extracting person arrays from LNValue with valueType: %s and value type: %s"
- "PhoneDonationBuilder: Failed to unarchive LNLinkEnumerationValueType from valueData"
- "PhoneDonationBuilder: Found property %s for %s in entity"
- "PhoneDonationBuilder: Found property '%s' in entity"
- "PhoneDonationBuilder: Processing array container type for phone persons"
- "PhoneDonationBuilder: Processing entity container type for call group"
- "PhoneDonationBuilder: Unsupported container type: "
- "PhoneDonationBuilder: extract AudioVisualMode entity from entity: %s"
- "SiriSuggestionsBiomeEventBackFiller: Unexpected empty record in eventBody: %@"
- "SiriSuggestionsBiomeEventBackFiller: interactionId: %@ does not have an interaction id. Skipping..."
- "StartFaceTimeCallHandler: Start extraction of the parameters"
- "StartTelephonyCallHandler: Start extraction of the parameters"
- "The INPlayMediaIntent mediaSearch: %s"
- "The INPlayMediaIntent: %s"
```

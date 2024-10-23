## feedbackd

> `/usr/libexec/feedbackd`

```diff

-135.2.0.0.0
-  __TEXT.__text: 0x6a2d8
-  __TEXT.__auth_stubs: 0x1d50
+139.1.0.0.0
+  __TEXT.__text: 0x6e5c8
+  __TEXT.__auth_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x13b8
-  __TEXT.__cstring: 0x3861
+  __TEXT.__const: 0x1468
+  __TEXT.__cstring: 0x3a71
   __TEXT.__objc_methname: 0x1429
-  __TEXT.__oslogstring: 0x2358
-  __TEXT.__swift5_typeref: 0xb59
-  __TEXT.__constg_swiftt: 0xae4
-  __TEXT.__swift5_fieldmd: 0x6b0
-  __TEXT.__swift5_reflstr: 0x92e
+  __TEXT.__oslogstring: 0x2578
+  __TEXT.__swift5_typeref: 0xb99
+  __TEXT.__constg_swiftt: 0xb50
+  __TEXT.__swift5_fieldmd: 0x710
+  __TEXT.__swift5_reflstr: 0x95e
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0xe4
-  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_proto: 0xec
+  __TEXT.__swift5_types: 0x94
   __TEXT.__objc_classname: 0x83
   __TEXT.__objc_methtype: 0x258
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x46c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1338
-  __TEXT.__eh_frame: 0x3510
-  __DATA_CONST.__auth_got: 0xea8
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__auth_ptr: 0x3e8
-  __DATA_CONST.__const: 0x15a8
+  __TEXT.__unwind_info: 0x13f8
+  __TEXT.__eh_frame: 0x3600
+  __DATA_CONST.__auth_got: 0xeb0
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__auth_ptr: 0x3f0
+  __DATA_CONST.__const: 0x1608
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x1a58
   __DATA.__objc_selrefs: 0x588
   __DATA.__objc_data: 0x928
-  __DATA.__data: 0x1a68
-  __DATA.__bss: 0x1c90
+  __DATA.__data: 0x1bb8
+  __DATA.__bss: 0x1d90
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1284
-  Symbols:   809
-  CStrings:  732
+  Functions: 1333
+  Symbols:   815
+  CStrings:  752
 
Symbols:
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO15siriWithChatGPTyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO18visualIntelligenceyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO19writingToolsComposeyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO7siriPQAyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainOs23CustomStringConvertibleAAMc
+ _$s15FeedbackService15FBKSInteractionC15StructuredValueO10dictionaryyAESDySSAEGcAEmFWC
+ _$s15FeedbackService15FBKSInteractionC15StructuredValueO6stringyAESScAEmFWC
+ _swift_getTupleTypeLayout2
+ _swift_initEnumMetadataSinglePayload
- _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
- _$s15FeedbackService12FBKSDonationC13DonationErrorOMa
- _$s15FeedbackService12FBKSDonationC13DonationErrorOs0E0AAMc
CStrings:
+ " days\")\n        AND evaluationUuid NOT IN (\n            "
+ " duplicate spotlightID: "
+ "\"\n        )\n        WHERE datetime(eventTimestamp, \"unixepoch\") >= datetime(\"now\", \"-"
+ ".string._0\"\n        ) id\n    FROM \""
+ "ChatGPT Integration in Siri"
+ "Compose with ChatGPT in Writing Tools"
+ "Donation dropped due to: %!{(MISSING)public}s"
+ "Dropping donation due to sampling rate"
+ "Duplicate count for spotlightID %!s(MISSING) is %!l(MISSING)d"
+ "Feature domain: %!s(MISSING) is contained within domains to check spotlight index dupes, will validate"
+ "Found duplicate donation ID: %!s(MISSING)"
+ "No duplicate row for spotlightID existed"
+ "SELECT\n    count(*) count\nFROM (\n    SELECT\n        json_extract(\n            json_extract(\n                originalContent_json,\n                \"$.text\"\n            ),\n            \"$.dictionary._0."
+ "SpotlightID is not a duplicate"
+ "Visual Intelligence"
+ "Will search for id: %!s(MISSING)"
+ "dictionary is not a string"
+ "donation duplicate key is nil"
+ "donation has no structured content"
+ "donation spotlightID is nil"
+ "duplicate row count existed, but count didn't exist"
+ "messageSpotlightID"
+ "structured content is not a dictionary"
- "\"\n        )\n        WHERE evaluationUuid NOT IN (\n            "
- "Donation dropped due to sampling: %!{(MISSING)private,mask.hash}s"
- "Donation not enabled"

```

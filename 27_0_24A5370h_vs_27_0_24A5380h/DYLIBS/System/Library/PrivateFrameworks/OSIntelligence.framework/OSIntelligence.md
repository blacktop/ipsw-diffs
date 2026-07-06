## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-  __TEXT.__text: 0x19648
+  __TEXT.__text: 0x1a5e8
   __TEXT.__objc_methlist: 0x2290
-  __TEXT.__const: 0x198
+  __TEXT.__const: 0x1a8
   __TEXT.__cstring: 0x1a4a
-  __TEXT.__oslogstring: 0x1ec2
-  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__oslogstring: 0x2609
+  __TEXT.__gcc_except_tab: 0x6a8
   __TEXT.__unwind_info: 0x9b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1200
+  __DATA_CONST.__objc_selrefs: 0x1208
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0x1580
   __AUTH_CONST.__objc_const: 0x30e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 919
-  Symbols:   3092
-  CStrings:  579
+  Functions: 921
+  Symbols:   3098
+  CStrings:  609
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_NSNull
+ ___block_descriptor_72_e8_32s40r48r56r64r_e22_v16?0"BMStoreEvent"8lr40l8r48l8r56l8s32l8r64l8
+ _objc_msgSend$null
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke_2
- ___block_descriptor_72_e8_32s40r48r56r64r_e22_v16?0"BMStoreEvent"8lr40l8r48l8r56l8r64l8s32l8
CStrings:
+ "Charging segment extends to end of day: %@ to %@, duration %.1f mins"
+ "Daily charging summary: %ld segments, %.1f total minutes"
+ "Device was charging before midnight, starting new segment at %@"
+ "Duplicate mitigation disable event (level=%ld), already disengaged (ignoring)"
+ "Duplicate mitigation enable event (level=%ld), keeping original start time %@ (already engaged for %.1f mins)"
+ "Duplicate plug-in event while already charging (collapsing to same segment)"
+ "Duplicate unplug event while already unplugged (ignoring)"
+ "Ended charging segment: %@ to %@, duration %.1f mins (total: %.1f mins)"
+ "Engagement span: start=%@, end=%@, total=%.1f mins"
+ "Engagement started before yesterday (%@), clamping to %@"
+ "Mitigation disengaged, cleared engagement tracking (total engagement was %.1f mins)"
+ "Mitigation engaged, started engagement tracking at %@ (level=%ld)"
+ "Negative segment duration detected at end of day: %f seconds"
+ "Negative segment duration detected: %f seconds"
+ "Negative today duration detected: %f minutes (start=%@, now=%@)"
+ "Negative yesterday duration detected: %f minutes (start=%@, midnight=%@)"
+ "No existing engagement data, created new dictionary"
+ "Persisted engagement data for %lu day(s)"
+ "Processing engagement END (engaged→disengaged)"
+ "Recorded today: added %.1f mins (total now %ld mins), count now %ld"
+ "Recorded yesterday: added %.1f mins (total now %ld mins), count now %ld"
+ "Split calculation: includeYesterday=%d, effectiveStart=%@, midnightToday=%@"
+ "Started charging segment #%ld at %@"
+ "State evaluation: isCurrentlyEngaged=%d (since %@), newStateIsEngaged=%d"
+ "Today (%@) existing data: duration=%ld mins, count=%ld"
+ "Today (%@) had no data, initializing"
+ "Yesterday (%@) existing data: duration=%ld mins, count=%ld"
+ "Yesterday (%@) had no data, initializing"
+ "recordMitigationUpdate called: previous level=%ld, new level=%ld, decisionMaker=%ld"
+ "recordMitigationUpdate completed"

```

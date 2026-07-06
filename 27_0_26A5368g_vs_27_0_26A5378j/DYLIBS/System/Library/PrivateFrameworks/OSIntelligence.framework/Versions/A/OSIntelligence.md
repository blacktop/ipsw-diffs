## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence`

```diff

-  __TEXT.__text: 0x18130
+  __TEXT.__text: 0x1916c
   __TEXT.__objc_methlist: 0x21a8
-  __TEXT.__const: 0x178
+  __TEXT.__const: 0x188
   __TEXT.__cstring: 0x180e
-  __TEXT.__oslogstring: 0x1904
-  __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0xa20
+  __TEXT.__oslogstring: 0x204b
+  __TEXT.__gcc_except_tab: 0x640
+  __TEXT.__unwind_info: 0xa28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1138
+  __DATA_CONST.__objc_selrefs: 0x1140
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__got: 0x1a8
   __AUTH_CONST.__const: 0xfe0
   __AUTH_CONST.__cfstring: 0x14a0
   __AUTH_CONST.__objc_const: 0x2fa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 915
-  Symbols:   2022
-  CStrings:  518
+  Functions: 917
+  Symbols:   2026
+  CStrings:  548
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_NSNull
+ _objc_msgSend$null
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

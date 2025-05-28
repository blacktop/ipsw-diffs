## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1870.1.1.3.0
-  __TEXT.__text: 0x121fc8
+1870.2.1.0.0
+  __TEXT.__text: 0x121f2c
   __TEXT.__auth_stubs: 0x1430
   __TEXT.__objc_methlist: 0x132f8
   __TEXT.__const: 0x4f2
   __TEXT.__cstring: 0xaaae
-  __TEXT.__oslogstring: 0xc845
+  __TEXT.__oslogstring: 0xc814
   __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__dlopen_cstrs: 0x2ba
   __TEXT.__ustring: 0x162

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0x1b2
   __TEXT.__swift5_capture: 0xa0
-  __TEXT.__unwind_info: 0x492c
+  __TEXT.__unwind_info: 0x4928
   __TEXT.__objc_classname: 0x1801
   __TEXT.__objc_methname: 0x2abb2
   __TEXT.__objc_methtype: 0x3e06

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8187
-  Symbols:   25044
+  Functions: 8186
+  Symbols:   25042
   CStrings:  9388
 
Symbols:
+ ___99-[EKSpotlightSearch initWithSearchWithCSQuery:inStore:inCalendars:resultHandler:completionHandler:]_block_invoke.14
- -[EKEventStore requestAccessToEntityType:completion:].cold.1
- ___99-[EKSpotlightSearch initWithSearchWithCSQuery:inStore:inCalendars:resultHandler:completionHandler:]_block_invoke_2
CStrings:
+ "Fetched search item had nil start date, skipping showing search result: %@"
- "Calling request access completion handler with no access because this method is deprecated and the app is not a legacy app."

```

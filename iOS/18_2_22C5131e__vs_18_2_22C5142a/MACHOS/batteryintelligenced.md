## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-97.60.7.0.0
-  __TEXT.__text: 0x1ff30
+97.62.1.0.0
+  __TEXT.__text: 0x2086c
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_stubs: 0x2880
-  __TEXT.__objc_methlist: 0x1290
+  __TEXT.__objc_methlist: 0x1298
   __TEXT.__cstring: 0x18cb
   __TEXT.__objc_classname: 0x2e9
   __TEXT.__objc_methtype: 0x5b2
   __TEXT.__const: 0x1d8
-  __TEXT.__oslogstring: 0x33b4
-  __TEXT.__objc_methname: 0x32a8
+  __TEXT.__oslogstring: 0x357c
+  __TEXT.__objc_methname: 0x32bf
   __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__unwind_info: 0x520
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x768

   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x3d48
   __DATA.__objc_selrefs: 0xbd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 618
+  Functions: 629
   Symbols:   193
-  CStrings:  1310
+  CStrings:  1317
 
CStrings:
+ "After processing PPS data, ppsNumRows is now: %@"
+ "Encountered error getting timestamp from PPS event. Unable to compute timeSinceLastReadingMins feature. Continuing to next event."
+ "Encountered error parsing PPS event."
+ "Encountered error parsing PPS event. Continuing to next event."
+ "Encountered missing value for %@. Filling with default value: %ld."
+ "Not enough history to make prediction; after processing now have %d valid rows"
+ "Received %@ rows from PPS."
+ "Skipping current event due to at least one missing value."
+ "Using inputFeaturesNumOfRows = %@ (with takeLatestSMCValues = %ld)"
+ "objectForKey:fromDict:withDefaults:"
- "Encountered error getting timestamp from PPS event. Unable to compute timeSinceLastReadingMins feature."
- "Received %@ rows"
- "removeEvent:"

```

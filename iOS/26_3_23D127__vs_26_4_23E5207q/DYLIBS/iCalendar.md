## iCalendar

> `/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar`

```diff

-1169.2.1.0.0
-  __TEXT.__text: 0x2abdc
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x3914
+1169.4.3.0.0
+  __TEXT.__text: 0x2d0f0
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x3954
   __TEXT.__oslogstring: 0x4c9
   __TEXT.__const: 0x490
   __TEXT.__cstring: 0x2a0f
-  __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__unwind_info: 0xc30
+  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_classname: 0x69b
-  __TEXT.__objc_methname: 0x5aa2
+  __TEXT.__objc_methname: 0x5bad
   __TEXT.__objc_methtype: 0x8b5
-  __TEXT.__objc_stubs: 0x57c0
+  __TEXT.__objc_stubs: 0x5820
   __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__const: 0x16f0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc0
+  __DATA_CONST.__objc_selrefs: 0x1fd8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x5080
   __AUTH_CONST.__objc_const: 0x5cf0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8C46423A-7050-37A6-9D3E-4FD512668888
-  Functions: 1177
-  Symbols:   4264
-  CStrings:  2834
+  UUID: 4D1BB191-BAF9-3930-89BB-08E35B8B4FBF
+  Functions: 1193
+  Symbols:   4294
+  CStrings:  2837
 
Symbols:
+ -[ICSDateValue laterDate:]
+ -[ICSTimeZone(TimeZoneGeneration) lastTransitionDatesInBlocks:]
+ -[ICSTimeZone(TimeZoneGeneration) mostRecentTransitionDateFromRDateOf:onOrBeforeDate:]
+ -[ICSTimeZone(TimeZoneGeneration) mostRecentTransitionDateFromRRuleOf:onOrBeforeDate:]
+ -[ICSTimeZone(TimeZoneGeneration) mostRecentTransitionDateInBlock:lastTransitionDate:onOrBeforeDate:]
+ -[ICSTimeZone(TimeZoneGeneration) mostRecentTransitionDatesInBlocks:lastTransitionDates:onOrBeforeDate:]
+ -[ICSTimeZone(TimeZoneGeneration) relevantTimeZoneBlocks:fromDate:options:]
+ GCC_except_table20
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$lastTransitionDatesInBlocks:
+ _objc_msgSend$mostRecentTransitionDateFromRDateOf:onOrBeforeDate:
+ _objc_msgSend$mostRecentTransitionDateFromRRuleOf:onOrBeforeDate:
+ _objc_msgSend$mostRecentTransitionDateInBlock:lastTransitionDate:onOrBeforeDate:
+ _objc_msgSend$mostRecentTransitionDatesInBlocks:lastTransitionDates:onOrBeforeDate:
+ _objc_msgSend$relevantTimeZoneBlocks:fromDate:options:
+ _objc_retain_x27
- -[ICSTimeZone(TimeZoneGeneration) _previousDSTTransitionForDate:timezone:]
- GCC_except_table15
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_previousDSTTransitionForDate:timezone:
- _objc_msgSend$isEqualToDate:
- _objc_msgSend$set
- _objc_msgSend$timeZone
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "calendarWithIdentifier:"
+ "lastTransitionDatesInBlocks:"
+ "mostRecentTransitionDateFromRDateOf:onOrBeforeDate:"
+ "mostRecentTransitionDateFromRRuleOf:onOrBeforeDate:"
+ "mostRecentTransitionDateInBlock:lastTransitionDate:onOrBeforeDate:"
+ "mostRecentTransitionDatesInBlocks:lastTransitionDates:onOrBeforeDate:"
+ "relevantTimeZoneBlocks:fromDate:options:"
- "_previousDSTTransitionForDate:timezone:"
- "isEqualToDate:"
- "set"
- "timeZone"

```

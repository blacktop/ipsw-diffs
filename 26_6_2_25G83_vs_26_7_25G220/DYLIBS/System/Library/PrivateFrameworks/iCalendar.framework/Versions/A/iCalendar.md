## iCalendar

> `/System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar`

```diff

-1169.4.3.0.0
-  __TEXT.__text: 0x2f014
+1169.4.4.0.0
+  __TEXT.__text: 0x2f114
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0x3954
-  __TEXT.__oslogstring: 0x4c9
-  __TEXT.__const: 0x490
+  __TEXT.__oslogstring: 0x4ed
+  __TEXT.__const: 0x498
   __TEXT.__cstring: 0x2a0f
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__unwind_info: 0xc08

   - /usr/lib/libz.1.dylib
   Functions: 1198
   Symbols:   3023
-  CStrings:  2173
+  CStrings:  2174
 
Functions:
~ -[NSData(VCSEncodings) VCSConvert8bitBufferToUTF8From:] : 308 -> 324
~ -[VCSParserInputStream loadLineBuffer] : 180 -> 208
~ -[VCSParsedLine loadFromCString:withParseState:] : 1212 -> 1420
~ -[VCSProperty initKeywordListProperty:withParseState:property:] : 356 -> 360
CStrings:
+ "Invalid data at %d: parameter %@=%@"
```

## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-925.4.1.0.0
-  __TEXT.__text: 0x95220
+925.5.1.1.0
+  __TEXT.__text: 0x95228
   __TEXT.__auth_stubs: 0x3180
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0xd84
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__cstring: 0x27b0c
+  __TEXT.__cstring: 0x27b11
   __TEXT.__oslogstring: 0x6c
   __TEXT.__unwind_info: 0x17f8
   __TEXT.__objc_classname: 0x7d

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1898BE7-752B-3CEC-95D5-942E78B4586C
+  UUID: D74A3811-D350-3E71-B763-DE79602A27B6
   Functions: 2066
   Symbols:   5384
   CStrings:  4443
Symbols:
+ _APSAudioFormatDescriptionListCreateSenderDefaultList
- _APSAudioFormatDescriptionListCreateIntersection
Functions:
~ _ptpClock_StopForClient : 760 -> 752
~ _APSAudioFormatDescriptionListCreateIntersection -> _APSAudioFormatDescriptionListCreateSenderDefaultList : 264 -> 280
CStrings:
+ "APSAudioFormatDescriptionListCreateSenderDefaultList"
- "APSAudioFormatDescriptionListCreateIntersection"

```

## libSMC.dylib

> `/usr/lib/libSMC.dylib`

```diff

-  __TEXT.__text: 0x50fc
+  __TEXT.__text: 0x5128
   __TEXT.__const: 0xd9a50
   __TEXT.__oslogstring: 0x6d1
   __TEXT.__cstring: 0x265
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__unwind_info: 0x150
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb10
   __DATA_CONST.__got: 0x0
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _SMCMakeUInt32Key -> _SMCOSAccumSampleChannel : 100 -> 288
~ _SMCOSAccumSampleChannel -> _SMCWriteKey : 288 -> 116
~ _SMCOSAccumIsSupported -> _SMCWriteKeyWithKnownSize : 116 -> 360
~ _SMCWriteKeyWithKnownSize -> _SMCMakeUInt32Key : 360 -> 100
~ _lookup1msChannel : 172 -> 192
~ _lookup1secChannel : 172 -> 192
~ _SMCGetAccumStatusFor : 464 -> 468

```

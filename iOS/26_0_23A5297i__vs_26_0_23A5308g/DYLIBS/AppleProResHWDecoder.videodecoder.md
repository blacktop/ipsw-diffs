## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-500.77.0.0.0
-  __TEXT.__text: 0x23060
+500.82.0.0.0
+  __TEXT.__text: 0x231b4
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__const: 0x74120
   __TEXT.__gcc_except_tab: 0x45c
   __TEXT.__cstring: 0x111b
-  __TEXT.__oslogstring: 0x3d0c
+  __TEXT.__oslogstring: 0x3dd3
   __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__auth_got: 0x518

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 2C5F2A49-D7AD-3075-8B31-D4521A3541A0
-  Functions: 469
-  Symbols:   1318
-  CStrings:  373
+  UUID: 34E7932A-7CB0-3F68-9460-84A26264C264
+  Functions: 470
+  Symbols:   1320
+  CStrings:  375
 
Symbols:
+ __ZL25ProResDecoder_SetPropertyP18OpaqueCMBaseObjectPK10__CFStringPKv.cold.7
Functions:
~ __ZL25ProResDecoder_SetPropertyP18OpaqueCMBaseObjectPK10__CFStringPKv : 1476 -> 1508
~ __ZL45ProResDecoder_CopySupportedPropertyDictionaryP20OpaqueVTVideoDecoderPPK14__CFDictionary : 116 -> 284
+ __ZL26ProResDecoder_StartSessionP20OpaqueVTVideoDecoderP27OpaqueVTVideoDecoderSessionPK25opaqueCMFormatDescription.cold.1
CStrings:
+ "ERROR AppleProResHW: %d: %s(): AppleProResHW Invalid Property Dictionary\n"
+ "WARNING AppleProResHW (0x%x): %d: %s(): AppleProResHW property dictionary is NULL - decoder configuration may be incomplete\n"

```

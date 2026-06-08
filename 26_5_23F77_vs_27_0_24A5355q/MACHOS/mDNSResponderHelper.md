## mDNSResponderHelper

> `/usr/sbin/mDNSResponderHelper`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x2ef4
+3066.0.0.502.1
+  __TEXT.__text: 0x2e78
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x151
+  __TEXT.__const: 0x158
   __TEXT.__cstring: 0x2e0
   __TEXT.__oslogstring: 0xce7
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x70
   __DATA.__data: 0x18
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAC1D860-4B9C-3F00-AC84-FB78395BC402
+  UUID: 1BD9AF9D-4B24-3632-A368-B9D0A66FDE01
   Functions: 16
   Symbols:   130
   CStrings:  98
Functions:
~ _PowerSleepSystem : 196 -> 152
~ _SendWakeupPacket : 1176 -> 1184
~ ___init_helper_service_block_invoke -> _handle_sigterm : 768 -> 56
~ ___accept_client_block_invoke -> _diediedie : 2264 -> 268
~ _diediedie -> ___init_helper_service_block_invoke : 268 -> 724
~ _handle_sigterm -> ___accept_client_block_invoke : 56 -> 2220

```

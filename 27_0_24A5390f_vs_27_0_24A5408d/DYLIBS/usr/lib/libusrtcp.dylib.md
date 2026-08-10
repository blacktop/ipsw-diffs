## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-6681.0.514.502.1
-  __TEXT.__text: 0x5b554
+6681.2.2.0.0
+  __TEXT.__text: 0x5bbdc
   __TEXT.__const: 0x244
   __TEXT.__oslogstring: 0xe6be
   __TEXT.__cstring: 0x1a8e

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 334
-  Symbols:   658
+  Functions: 335
+  Symbols:   659
   CStrings:  1120
 
Symbols:
+ _rbbr_apply_cruise_backoff
+ _rbbr_enter_cruise
+ _rbbr_enter_probe_rwnd
- _rbbr_sender_utilizing_rwnd
- _rbbr_update_win
```

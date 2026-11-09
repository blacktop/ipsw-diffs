## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-212.40.2.0.0
-  __TEXT.__text: 0x634dc
+212.42.1.0.0
+  __TEXT.__text: 0x63500
   __TEXT.__const: 0x76ec1
-  __TEXT.__cstring: 0x2ec
+  __TEXT.__cstring: 0x2f9
   __TEXT.__unwind_info: 0x868
   __TEXT.__eh_frame: 0x460
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/liblzma.5.dylib
   Functions: 547
   Symbols:   720
-  CStrings:  49
+  CStrings:  50
 
Functions:
~ _ProcessCommands : 2536 -> 2612
~ _SafeProcessCommands : 2824 -> 2804
~ _lz4raw_decode_buffer : 220 -> 164
~ _DecodeLiteralBlockSwitch : 520 -> 532
~ _DecodeDistanceBlockSwitch : 468 -> 480
~ _DecodeCommandBlockSwitch : 444 -> 456
~ _zlib_stream_get_encode_state_size : 44 -> 8
~ _SafeDecodeCommandBlockSwitch : 800 -> 812
~ _SafeDecodeLiteralBlockSwitch : 880 -> 892
~ _SafeDecodeDistanceBlockSwitch : 824 -> 836
CStrings:
+ "BLOCK_SWITCH"
```

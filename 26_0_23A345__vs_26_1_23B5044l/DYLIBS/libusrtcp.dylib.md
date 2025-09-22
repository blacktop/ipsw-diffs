## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.2.3.0.0
-  __TEXT.__text: 0x5c904
+5569.40.67.0.0
+  __TEXT.__text: 0x5c724
   __TEXT.__auth_stubs: 0x1020
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe78d
+  __TEXT.__oslogstring: 0xe6c3
   __TEXT.__cstring: 0x1a22
   __TEXT.__unwind_info: 0x458
   __DATA_CONST.__got: 0xa0

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2CB3BB58-194B-3A65-8D3A-DF4FB33DF3BC
+  UUID: 2816044D-E906-32C3-A93C-45C0EA453E63
   Functions: 326
   Symbols:   1007
-  CStrings:  1119
+  CStrings:  1116
 
Symbols:
+ _____nw_frame_array_finalize_block_invoke.584
+ _____nw_signpost_is_enabled_block_invoke.493
+ ___block_descriptor_tmp.485
+ ___block_descriptor_tmp.798
+ ___block_descriptor_tmp.8.487
+ ___block_literal_global.486
+ ___block_literal_global.796
+ ___nwlog_should_abort
- _____nw_frame_array_finalize_block_invoke.587
- _____nw_signpost_is_enabled_block_invoke.496
- ___block_descriptor_tmp.488
- ___block_descriptor_tmp.8.490
- ___block_descriptor_tmp.801
- ___block_literal_global.489
- ___block_literal_global.799
- ___nwlog_abort
Functions:
~ _tcp_output : 33316 -> 32820
~ _tcp_input : 38236 -> 38252
CStrings:
+ "%{public}s Assert (u_char *)lp - opt <= MAX_TCPOPTLEN failed"
- "%{public}s %{public}s add 2 counters for AccECN option, optlen=%u"
- "%{public}s %{public}s add all 3 counters for AccECN option, optlen=%u"
- "%{public}s %{public}s add empty AccECN option, optlen=%u"
- "%{public}s %{public}s add single counter for AccECN option, optlen=%u"

```

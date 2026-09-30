## pcapd

> `/usr/libexec/pcapd`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0xbfdc
+66.0.0.0.0
+  __TEXT.__text: 0xc048
   __TEXT.__auth_stubs: 0x820
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0xce7
-  __TEXT.__oslogstring: 0x24ec
+  __TEXT.__oslogstring: 0x24f8
   __TEXT.__unwind_info: 0x178
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 158
+  Functions: 160
   Symbols:   166
   CStrings:  350
 
CStrings:
+ "%{public}s:%d command NOT ALLOWED command: %{public}s from pid: %u\n"
- "%s:%d RRM NOT ALLOWED command: %{public}s from pid: %u\n"

```

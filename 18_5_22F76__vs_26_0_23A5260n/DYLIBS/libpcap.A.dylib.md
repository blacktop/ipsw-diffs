## libpcap.A.dylib

> `/usr/lib/libpcap.A.dylib`

```diff

-140.0.0.0.0
-  __TEXT.__text: 0x2137c
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__const: 0xc330
-  __TEXT.__cstring: 0x6d85
-  __TEXT.__unwind_info: 0x578
+144.0.0.0.0
+  __TEXT.__text: 0x20c40
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__const: 0xc320
+  __TEXT.__cstring: 0x6b9d
+  __TEXT.__unwind_info: 0x530
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x14a8
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__const: 0x10
   __DATA.__data: 0xd7
-  __DATA.__bss: 0x50b
+  __DATA.__bss: 0x503
   __DATA.__common: 0x8
   __DATA_DIRTY.__bss: 0x545
   - /usr/lib/libSystem.B.dylib
-  UUID: EBDE11D5-6C0A-3877-8012-A25382F5E0D5
-  Functions: 506
-  Symbols:   948
-  CStrings:  1099
+  UUID: 8BFCF535-BACF-384E-9C4C-974EF73A5FCE
+  Functions: 495
+  Symbols:   905
+  CStrings:  1074
 
Symbols:
+ _gen_uncond
- _atoi
- _capture_source_types
- _gen_cmp
- _gen_false
- _gen_portatom6
- _gen_true
- _getenv
- _gettimeofday
- _kevent
- _kqueue
- _os_channel_advance_slot
- _os_channel_attr_create
- _os_channel_attr_destroy
- _os_channel_attr_set
- _os_channel_available_slot_count
- _os_channel_create_extended
- _os_channel_destroy
- _os_channel_get_fd
- _os_channel_get_next_slot
- _os_channel_ring_id
- _os_channel_rx_ring
- _skywalk_activate
- _skywalk_close
- _skywalk_create
- _skywalk_debug
- _skywalk_dispatch
- _skywalk_dispatch_ring
- _skywalk_inject
- _skywalk_set_datalink
- _skywalk_stats
- _strsep
- _strtoul
- _uuid_parse
CStrings:
+ "%sulpn"
- "%p\n"
- "%p dlt %d\n"
- "%p priv %p\n"
- "%p, uuid %s, port %u\n"
- "%s: "
- ":"
- "PCAP_SKYWALK_DEBUG"
- "ev %d\n"
- "invalid UUID: %s"
- "kevent: %s"
- "packet injection is not supported in a monitoring channel"
- "pkt %p len %u\n"
- "rx ring %p avail %u\n"
- "rx[%u,%u], tx[%u,%u]\n"
- "skywalk:"
- "skywalk_activate"
- "skywalk_close"
- "skywalk_create"
- "skywalk_dispatch"
- "skywalk_dispatch_ring"
- "skywalk_set_datalink"
- "tx ring %p avail %u\n"
- "unable to create a TX channel: %s"
- "unable to create a kqueue: %s"
- "unable to create an RX channel: %s"
- "unable to create an attribute: %s"

```

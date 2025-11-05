## com.apple.iokit.IOUserEthernet

> `com.apple.iokit.IOUserEthernet`

```diff

-76.0.0.0.0
+76.100.1.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0xa51
-  __TEXT_EXEC.__text: 0x54d0
+  __TEXT.__cstring: 0xc71
+  __TEXT_EXEC.__text: 0x5cac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2ec8
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 9DF8EBFD-955A-3EEB-9E8D-14B48B6623C5
-  Functions: 164
-  Symbols:   799
-  CStrings:  106
+  UUID: F3143D3D-5545-3A50-AC36-0E3A85142446
+  Functions: 166
+  Symbols:   813
+  CStrings:  124
 
Symbols:
+ _mbuf_adj
+ _mbuf_data
+ _mbuf_get_csum_performed
+ _mbuf_get_csum_requested
+ _mbuf_get_gso_info
+ _mbuf_get_lro_info
+ _mbuf_len
+ _mbuf_prepend
+ _mbuf_set_csum_performed
+ _mbuf_set_csum_requested
+ _mbuf_set_gso_info
+ _mbuf_set_lro_info
+ _virtio_mbuf_ingest_header
+ _virtio_mbuf_prepend_header
CStrings:
+ "12111112122212121111111221211111111112111111112222212"
+ "EnableCrossover"
+ "EnableVirtIOHeader"
+ "IOUE %s: GSO requested without seg_size\n"
+ "IOUE %s: GSO size is zero\n"
+ "IOUE %s: GSO_UDP not supported\n"
+ "IOUE %s: TSO requested without CSUM\n"
+ "IOUE %s: gso_hdr_len %d <= %d\n"
+ "IOUE %s: gso_hdr_len %d > %ld\n"
+ "IOUE %s: mbuf_set_csum_requested %d\n"
+ "IOUE %s: mbuf_set_tso_info() %d\n"
+ "IOUE %s: offset %d >= %ld\n"
+ "IOUE %s: packet too short, %zu < %lu\n"
+ "IOUE %s: unrecognized GSO type %d\n"
+ "IOUE %s: unsupported GSO type %d\n"
+ "IOUE mbuf_prepend failed %d\n"
+ "ingest_virtio_header_tx"
+ "populate_virtio_header_tx"
+ "virtio_mbuf_ingest_header"
- "1211111212221212111111122121111111111211111111222212"

```

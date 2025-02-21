## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-4277.82.1.0.0
-  __TEXT.__text: 0xcc55c
-  __TEXT.__auth_stubs: 0x19b0
+4277.100.400.0.0
+  __TEXT.__text: 0xce3a8
+  __TEXT.__auth_stubs: 0x19a0
   __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0x3c5
-  __TEXT.__cstring: 0x8b70
-  __TEXT.__oslogstring: 0x11574
-  __TEXT.__unwind_info: 0xdf0
+  __TEXT.__const: 0x365
+  __TEXT.__cstring: 0x8dc6
+  __TEXT.__oslogstring: 0x11553
+  __TEXT.__unwind_info: 0xdc8
   __TEXT.__objc_classname: 0xa
   __TEXT.__objc_methname: 0x7c5
   __TEXT.__objc_methtype: 0xbd0
   __TEXT.__objc_stubs: 0x640
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x2428
+  __DATA_CONST.__const: 0x2408
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__auth_got: 0xcd8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x25a0
   __AUTH_CONST.__cfstring: 0x1480

   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x4c
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x5a8
+  __DATA.__bss: 0x5f8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x1c
-  __DATA_DIRTY.__bss: 0x738
+  __DATA_DIRTY.__bss: 0x6c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1176
-  Symbols:   1590
-  CStrings:  2726
+  Functions: 1161
+  Symbols:   1589
+  CStrings:  2749
 
Symbols:
+ _nw_protocol_instance_early_data_rejected
- _nw_protocol_instance_ignore_future_path_changes
- _strcmp
CStrings:
+ "%s strict allocator failed"
+ "%s strict_reallocf called with size 0"
+ "%s strict_reallocf(%zu) failed"
+ "%{public}s DCID not found"
+ "%{public}s marking DCID with sequence number %llu as used"
+ "%{public}s sending packet on path %p/%lx with DCID %{public}s"
+ "-[QUICLog createEvent:]"
+ "-[QUICLog packetLost:trigger:]"
+ "-[QUICLog packetReceived:isCoalesced:]"
+ "-[QUICLog packetSent:]"
+ "cubic_create"
+ "ledbat_create"
+ "prague_create"
+ "quic_ack_alloc"
+ "quic_ack_bitstring_create"
+ "quic_cid_array_create"
+ "quic_conn_alloc_globals"
+ "quic_conn_allocate"
+ "quic_conn_copy_data_transfer_snapshot_block_invoke"
+ "quic_conn_mark_dcid_used"
+ "quic_crypto_queue_create"
+ "quic_frame_alloc_CRYPTO"
+ "quic_frame_copy_metadata"
+ "quic_frame_free"
+ "quic_migration_can_migrate"
+ "quic_migration_create"
+ "quic_migration_disable_active_migration"
+ "quic_migration_prepare_parameters"
+ "quic_pacer_alloc"
+ "quic_packet_builder_create"
+ "quic_protector_create"
+ "quic_protector_get_mp_space"
+ "quic_reassq_create"
+ "quic_rtt_create"
+ "quic_shorthand_copyout"
+ "quic_shorthand_create"
+ "quic_tp_create"
- "%s _strict_reallocf called with size 0"
- "%s _strict_reallocf(%zu) failed"
- "%s strict_malloc(%zu) failed"
- "%{public}s invalid preferred address IPv4"
- "%{public}s migration is disabled"
- "%{public}s sending packet on path %p with DCID %{public}s"
- "%{public}s unsupported identifier type 0x%llx"
- "1"
- "_strict_reallocf"
- "quic_frame_find_path_from_path_identifiers"
- "quic_migration_disable"
- "quic_migration_is_disabled"
- "strict_calloc"
- "strict_malloc"

```

## AppleCIOFusion

> `/System/Library/PrivateFrameworks/AppleCIOFusion.framework/AppleCIOFusion`

```diff

-3.0.0.0.0
-  __TEXT.__text: 0x5dc8
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__cstring: 0x2a7
-  __TEXT.__const: 0x4a
-  __TEXT.__oslogstring: 0xb51
-  __TEXT.__gcc_except_tab: 0x398
-  __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__got: 0x50
-  __AUTH_CONST.__auth_got: 0x1c8
+6.0.0.0.0
+  __TEXT.__text: 0xc748
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__cstring: 0x8b3
+  __TEXT.__const: 0x4d
+  __TEXT.__oslogstring: 0x185e
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__got: 0x18
+  __AUTH_CONST.__auth_got: 0x230
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 575E034C-3A22-326F-97CC-AFF6B771AA48
-  Functions: 154
-  Symbols:   76
-  CStrings:  77
+  UUID: 1D2D327B-9707-3AD7-9CE8-E30AC5D981E2
+  Functions: 257
+  Symbols:   82
+  CStrings:  175
 
Symbols:
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__115__thread_structC1Ev
+ __ZNSt3__115__thread_structD1Ev
+ __ZNSt3__119__thread_local_dataEv
+ __ZNSt3__120__libcpp_atomic_waitEPVKvx
+ __ZNSt3__120__throw_system_errorEiPKc
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__123__cxx_atomic_notify_allEPVKv
+ __ZNSt3__123__libcpp_atomic_monitorEPVKv
+ __ZNSt3__16thread4joinEv
+ __ZNSt3__16threadD1Ev
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ ___chkstk_darwin
+ __os_log_debug_impl
+ _cc_clear
+ _ccrng
+ _ciofusion_context_id
+ _malloc_type_aligned_alloc
+ _pthread_create
+ _pthread_setspecific
+ _wmemchr
- __Unwind_Resume
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt19bad_optional_accessD1Ev
- __ZTISt12length_error
- __ZTISt19bad_optional_access
- __ZTVSt12length_error
- __ZTVSt19bad_optional_access
- ___cxa_allocate_exception
- ___cxa_begin_catch
- ___cxa_free_exception
- ___cxa_throw
- ___gxx_personality_v0
- __os_log_default
- _ciofusion_get_send_to_nodes_allowed_masks
- _ciofusion_receive_from_node_async
CStrings:
+ "(%s:%s:%u) AEAD key+iv decrypt node_set: %u, node_rank: %u"
+ "(%s:%s:%u) AEAD key+iv derived for node_set: %u, node_rank: %d"
+ "(%s:%s:%u) AEAD key+iv encrypt node_set: %u, node_rank: %u"
+ "(%s:%s:%u) Activation timed out after %llu milliseconds"
+ "(%s:%s:%u) Did not receive handshake from node"
+ "(%s:%s:%u) Failed to create a connection manager during activation"
+ "(%s:%s:%u) Failed to derive handshake key"
+ "(%s:%s:%u) Failed to get crypto key"
+ "(%s:%s:%u) Failed to get ensemble key"
+ "(%s:%s:%u) Failed to select on the socket"
+ "(%s:%s:%u) Handshake destination rank mismatch"
+ "(%s:%s:%u) Handshake version mismatch"
+ "(%s:%s:%u) IO worker reported an error"
+ "(%s:%s:%u) IV count limit reached"
+ "(%s:%s:%u) Initialize connections"
+ "(%s:%s:%u) Invalid null key pointer."
+ "(%s:%s:%u) Invalid source node rank %u\n"
+ "(%s:%s:%u) MeshConnectionManager - Failed to create TCP listener"
+ "(%s:%s:%u) MeshConnectionManager - Failed to create outgoing socket to node %u"
+ "(%s:%s:%u) MeshConnectionManager - Failed to establish outgoing connection to node %u."
+ "(%s:%s:%u) MeshConnectionManager - Failed to receive handshake from a connecting node"
+ "(%s:%s:%u) MeshConnectionManager - Failed to send handshake to node %u"
+ "(%s:%s:%u) MeshConnectionManager - Incoming connection established from node %u"
+ "(%s:%s:%u) MeshConnectionManager - Invalid number of hostnames (got %zu, expected %u)"
+ "(%s:%s:%u) MeshConnectionManager - Outgoing connection established to node %u"
+ "(%s:%s:%u) MeshConnectionManager - Received an invalid rank %u from a connecting node."
+ "(%s:%s:%u) Node count in Ensemble info [%u] cannot exceed the ensemble node count."
+ "(%s:%s:%u) Node is not part of the mask [%llu]. Exiting."
+ "(%s:%s:%u) Node is not part of the mask. Exiting."
+ "(%s:%s:%u) Only Ring mode is supported"
+ "(%s:%s:%u) SO_RCVBUF: %d"
+ "(%s:%s:%u) SO_SNDBUF: %d"
+ "(%s:%s:%u) TcpConnectionListener - Accepted connection on socket %d"
+ "(%s:%s:%u) TcpConnectionListener - Failed to set buffer sizes"
+ "(%s:%s:%u) TcpConnectionListener - Listening on port %d"
+ "(%s:%s:%u) TcpPendingConnection - Connect completed immediately on socket %d"
+ "(%s:%s:%u) TcpPendingConnection - Connect in progress on socket %d"
+ "(%s:%s:%u) TcpPendingConnection - Failed to resolve hostname: %s"
+ "(%s:%s:%u) TcpPendingConnection - Failed to set buffer sizes"
+ "(%s:%s:%u) The current node is not directly connected to the set of nodes in the mask argument."
+ "(%s:%s:%u) WorkerThread starting\n"
+ "(%s:%s:%u) WorkerThread terminating\n"
+ "(%s:%s:%u) alloc context: data size: %llu, chunk_size: %u, chunk_extent: %u, chunk_count: %u"
+ "(%s:%s:%u) connection closed while reading handshake"
+ "(%s:%s:%u) connection closed while receiving"
+ "(%s:%s:%u) connection closed while receiving from node %u"
+ "(%s:%s:%u) connection closed while sending"
+ "(%s:%s:%u) connection closed while writing handshake"
+ "(%s:%s:%u) connection count mismatch"
+ "(%s:%s:%u) decode handshake"
+ "(%s:%s:%u) decode_handshake: decryption failed"
+ "(%s:%s:%u) decode_handshake: invalid src_rank"
+ "(%s:%s:%u) decryption failed"
+ "(%s:%s:%u) decryption worker task failed"
+ "(%s:%s:%u) derive AEAD key"
+ "(%s:%s:%u) encode handshake"
+ "(%s:%s:%u) encryption failed"
+ "(%s:%s:%u) encryption worker task failed"
+ "(%s:%s:%u) errno=%d (%s) MeshConnectionManager - select failed"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Accept failed"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to bind socket"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to create socket"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to listen on socket"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to set SO_REUSEADDR"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to set TCP_NODELAY"
+ "(%s:%s:%u) errno=%d (%s) TcpConnectionListener - Failed to set non-blocking"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - Connect failed"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - Failed to create socket"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - Failed to set SO_REUSEADDR"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - Failed to set TCP_NODELAY"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - Failed to set non-blocking"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - complete_connect getsockopt failed"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection - connect failed"
+ "(%s:%s:%u) errno=%d (%s) TcpPendingConnection::debug_select - select failed"
+ "(%s:%s:%u) errno=%d (%s) setsockopt SO_RCVBUF"
+ "(%s:%s:%u) errno=%d (%s) setsockopt SO_SNDBUF"
+ "(%s:%s:%u) get_field CryptoKey failed"
+ "(%s:%s:%u) hostname entry %u is NULL"
+ "(%s:%s:%u) invalid access"
+ "(%s:%s:%u) invalid context allocation size: %llu"
+ "(%s:%s:%u) invalid data size"
+ "(%s:%s:%u) invalid incoming info struct, hostnames non NULL"
+ "(%s:%s:%u) invalid node_mask"
+ "(%s:%s:%u) invalid node_rank: %u"
+ "(%s:%s:%u) invalid null info pointer"
+ "(%s:%s:%u) invalid parameters"
+ "(%s:%s:%u) invlalid null info pointer"
+ "(%s:%s:%u) key+iv array size: %zu bytes for %u node masks"
+ "(%s:%s:%u) malloc failed"
+ "(%s:%s:%u) missing hostnames in ensemble info."
+ "(%s:%s:%u) node: %u, peer_mask: 0x%llx, crypto_workers: %u io_workers: %u"
+ "(%s:%s:%u) read failed: %d"
+ "(%s:%s:%u) read handshake: %d"
+ "(%s:%s:%u) recv failed: %d"
+ "(%s:%s:%u) rng generate"
+ "(%s:%s:%u) rng init"
+ "(%s:%s:%u) send failed: %d"
+ "(%s:%s:%u) send worker task failed"
+ "(%s:%s:%u) set_field CryptoKey failed"
+ "(%s:%s:%u) size [%llu] out of range or misaligned"
+ "(%s:%s:%u) too many chunks, size: %llu, chunk_size: %llu"
+ "(%s:%s:%u) too many valid masks"
+ "(%s:%s:%u) worker not ready"
+ "(%s:%s:%u) write handshake: %d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/ByteSegment.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/Crypto.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/Handshake.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/MeshTcpConnectionManager.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/TcpConnection.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/WorkerThread.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionConfig/FusionConfig.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionSupport/FusionMesh.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionSupport/IOContext.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionSupport/IOContext.h"
+ "CIOF-HANDSHK"
+ "activate"
+ "allocate"
+ "allocate_aligned"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "chunk_data"
+ "chunk_data_and_tag"
+ "common_aead_derive_key_and_iv"
+ "connect"
+ "crypto_rng"
+ "debug_select"
+ "decode_handshake"
+ "get_chunk_size"
+ "initialize_connections"
+ "listen"
+ "poll"
+ "receive_and_verify_handshake"
+ "receive_from_node"
+ "run"
+ "send_handshake"
+ "send_to_nodes"
+ "set_buffer_sizes"
+ "start_decrypt"
+ "start_encrypt"
+ "start_receive"
+ "start_send"
+ "start_terminate"
+ "thread constructor failed"
+ "try_accept"
+ "validate_mask"
- "(%s:%s:%u) CryptoKey size mismatch"
- "(%s:%s:%u) hostname entry %u should be NULL"
- "(%s:%s:%u) invalid incoming info struct, hostname entry non NULL: %u"
- "(%s:%s:%u) invalid node_id: %u"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/AppleCIOFusionFramework/Crypto.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionConfig/KextInterface.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionSupport/FusionSupport.cpp"
- "Did not receive handshake from node.\n"
- "Failed to parse handshake\n"
- "Failed to read handshake from the socket. Error: %d\n"
- "Failed to select on the socket\n"
- "Failed to write handshake to the socket.\n"
- "Handshake message length mismatch\n"
- "Handshake message type mismatch\n"
- "Handshake sender rank mismatch\n"
- "Handshake version mismatch\n"
- "MeshConnectionManager - Failed to connect to node %u"
- "MeshConnectionManager - Failed to create TCP listener"
- "MeshConnectionManager - Failed to create outgoing socket to node %u"
- "MeshConnectionManager - Failed to receive handshake from a connecting node"
- "MeshConnectionManager - Failed to send handshake to node %u"
- "MeshConnectionManager - Incoming connection established from node %u"
- "MeshConnectionManager - Invalid number of hostnames"
- "MeshConnectionManager - Outgoing connection established to node %u"
- "MeshConnectionManager - select failed: %s"
- "TcpConnectionListener - Accept failed: %s"
- "TcpConnectionListener - Accepted connection on socket %d"
- "TcpConnectionListener - Failed to bind socket: %s"
- "TcpConnectionListener - Failed to create socket: %s"
- "TcpConnectionListener - Failed to listen on socket: %s"
- "TcpConnectionListener - Failed to set SO_REUSEADDR: %s"
- "TcpConnectionListener - Failed to set TCP_NODELAY: %s"
- "TcpConnectionListener - Failed to set non-blocking: %s"
- "TcpConnectionListener - Listening on port %d"
- "TcpPendingConnection - Connect completed immediately on socket %d"
- "TcpPendingConnection - Connect failed: %s"
- "TcpPendingConnection - Connect in progress on socket %d"
- "TcpPendingConnection - Failed to create socket: %s"
- "TcpPendingConnection - Failed to resolve hostname: %s"
- "TcpPendingConnection - Failed to set SO_REUSEADDR: %s"
- "TcpPendingConnection - Failed to set TCP_NODELAY: %s"
- "TcpPendingConnection - Failed to set non-blocking: %s"
- "TcpPendingConnection - complete_connect getsockopt failed: %s"
- "TcpPendingConnection - connect failed: %s"
- "aead_derive_key_and_iv"
- "basic_string"

```

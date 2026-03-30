## AppleCIOFusionConfig

> `/System/Library/PrivateFrameworks/AppleCIOFusionConfig.framework/AppleCIOFusionConfig`

```diff

-3.0.0.0.0
-  __TEXT.__text: 0x3748
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__cstring: 0x1c5
-  __TEXT.__gcc_except_tab: 0x32c
+6.0.0.0.0
+  __TEXT.__text: 0x7cd8
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__cstring: 0x4a0
   __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x890
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__got: 0x38
-  __AUTH_CONST.__auth_got: 0x168
+  __TEXT.__oslogstring: 0x113e
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__got: 0x18
+  __AUTH_CONST.__auth_got: 0x1b0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: DB332118-1B30-36C7-A871-767A5FE6A9E5
-  Functions: 109
-  Symbols:   58
-  CStrings:  56
+  UUID: 523C84B2-05B9-3433-BD1E-DE57E4AE1922
+  Functions: 175
+  Symbols:   65
+  CStrings:  113
 
Symbols:
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZdaPvSt19__type_descriptor_t
+ __ZdlPv
+ __ZnamSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___chkstk_darwin
+ __os_log_debug_impl
+ _cc_clear
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccgcm_one_shot
+ _cchkdf
+ _ccrng
+ _ccsha256_di
+ _ciofusionconfig_reset
+ _memcpy
+ _memmove
- __Unwind_Resume
- __ZNSt19bad_optional_accessD1Ev
- __ZSt9terminatev
- __ZTISt19bad_optional_access
- __ZTVSt19bad_optional_access
- ___cxa_allocate_exception
- ___cxa_begin_catch
- ___cxa_throw
- ___gxx_personality_v0
- __os_log_default
CStrings:
+ "(%s:%s:%u) AES-GCM decryption failed"
+ "(%s:%s:%u) AES-GCM encryption failed"
+ "(%s:%s:%u) Did not receive handshake from node"
+ "(%s:%s:%u) Failed to derive handshake key"
+ "(%s:%s:%u) Failed to get crypto key"
+ "(%s:%s:%u) Failed to select on the socket"
+ "(%s:%s:%u) Handshake destination rank mismatch"
+ "(%s:%s:%u) Handshake version mismatch"
+ "(%s:%s:%u) Invalid null key pointer."
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
+ "(%s:%s:%u) SO_RCVBUF: %d"
+ "(%s:%s:%u) SO_SNDBUF: %d"
+ "(%s:%s:%u) TcpConnectionListener - Accepted connection on socket %d"
+ "(%s:%s:%u) TcpConnectionListener - Failed to set buffer sizes"
+ "(%s:%s:%u) TcpConnectionListener - Listening on port %d"
+ "(%s:%s:%u) TcpPendingConnection - Connect completed immediately on socket %d"
+ "(%s:%s:%u) TcpPendingConnection - Connect in progress on socket %d"
+ "(%s:%s:%u) TcpPendingConnection - Failed to resolve hostname: %s"
+ "(%s:%s:%u) TcpPendingConnection - Failed to set buffer sizes"
+ "(%s:%s:%u) buffer size mismatch"
+ "(%s:%s:%u) connection closed while reading handshake"
+ "(%s:%s:%u) connection closed while writing handshake"
+ "(%s:%s:%u) decode handshake"
+ "(%s:%s:%u) decode_handshake: decryption failed"
+ "(%s:%s:%u) decode_handshake: invalid src_rank"
+ "(%s:%s:%u) encode handshake"
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
+ "(%s:%s:%u) hkdf failed"
+ "(%s:%s:%u) hostname entry %u is NULL"
+ "(%s:%s:%u) invalid ensemble_key size %zu"
+ "(%s:%s:%u) invalid incoming info struct, hostnames non NULL"
+ "(%s:%s:%u) invalid node_rank: %u"
+ "(%s:%s:%u) invalid null info pointer"
+ "(%s:%s:%u) invlalid null info pointer"
+ "(%s:%s:%u) iv count overflow"
+ "(%s:%s:%u) missing hostnames in ensemble info."
+ "(%s:%s:%u) read handshake: %d"
+ "(%s:%s:%u) rng generate"
+ "(%s:%s:%u) rng init"
+ "(%s:%s:%u) set_field CryptoKey failed"
+ "(%s:%s:%u) tag size mismatch"
+ "(%s:%s:%u) write handshake: %d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/Crypto.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/Handshake.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/MeshTcpConnectionManager.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/Common/TcpConnection.cpp"
+ "CIOF-HANDSHK"
+ "aead_decrypt"
+ "aead_encrypt"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "common_aead_derive_key_and_iv"
+ "connect"
+ "crypto_rng"
+ "debug_select"
+ "decode_handshake"
+ "listen"
+ "poll"
+ "receive_and_verify_handshake"
+ "send_handshake"
+ "set_buffer_sizes"
+ "try_accept"
- "(%s:%s:%u) CryptoKey size mismatch"
- "(%s:%s:%u) hostname entry %u should be NULL"
- "(%s:%s:%u) invalid incoming info struct, hostname entry non NULL: %u"
- "(%s:%s:%u) invalid node_id: %u"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCIOFusion/src/AppleCIOFusion/FusionConfig/KextInterface.cpp"
- "ConnectionManager - Failed to create TCP listener"
- "ConnectionManager - Failed to create outgoing socket"
- "ConnectionManager - Failed to recreate outgoing socket after connect failure"
- "ConnectionManager - Incoming connection established"
- "ConnectionManager - Outgoing connection established"
- "ConnectionManager - hostname is null"
- "ConnectionManager - select failed: %s"
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

```

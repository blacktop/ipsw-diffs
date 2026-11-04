## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-625.2.8.10.6
-  __TEXT.__text: 0xaa34d0
+626.1.12.10.3
+  __TEXT.__text: 0xaa34bc
   __TEXT.__objc_methlist: 0x14cc
   __TEXT.__const: 0xa6ff8
   __TEXT.__cstring: 0x56a7a

   __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__auth_got: 0xa20
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x18
   __DATA.__objc_ivar: 0x250

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 18614
-  Symbols:   23842
+  Symbols:   23843
   CStrings:  9154
 
Symbols:
+ _srtp_crypto_alloc_typed
+ _strdup
- _srtp_crypto_alloc
Functions:
~ __ZN6webrtc25DtlsTransportInternalImpl18CompleteDtlsInStunEb : 404 -> 272
~ __ZN6webrtc16make_ref_countedINS_10I010BufferEJRiS2_S2_iiELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 452 -> 444
~ __ZN6webrtc10I420BufferC2Eii : 296 -> 288
~ __ZN6webrtc16make_ref_countedINS_10I420BufferEJRiS2_ELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 440 -> 432
~ __ZN6webrtc16make_ref_countedINS_10I420BufferEJRiS2_S2_S2_S2_ELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 456 -> 448
~ __ZN6webrtc16make_ref_countedINS_10I422BufferEJRiS2_ELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 420 -> 412
~ __ZN6webrtc16make_ref_countedINS_10I444BufferEJRiS2_ELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 400 -> 392
~ __ZN6webrtc16make_ref_countedINS_10NV12BufferEJRiS2_ELPS1_0EEENS_13scoped_refptrIT_EEDpOT0_ : 436 -> 428
~ _WebRtcOpus_EncoderCreate : 336 -> 344
~ _WebRtcOpus_MultistreamEncoderCreate : 368 -> 376
~ _WebRtcOpus_DecoderCreate : 312 -> 320
~ _WebRtcOpus_MultistreamDecoderCreate : 316 -> 324
~ __ZN4absl22internal_any_invocable12LocalInvokerILb0EvRZN6webrtc8TurnPort18ResolveTurnAddressERKNS2_13SocketAddressEE3$_0JEEET0_PNS0_15TypeErasedStateEDpNS0_18ForwardedParameterIT2_E4typeE : 876 -> 964
~ __ZN4bssl21x509_verify_signatureEPK13X509_algor_stPK14asn1_string_stNS_4SpanIKhLm18446744073709551615EEEP11evp_pkey_st : 468 -> 472
~ __ZN4bssl14ERR_save_stateEv : 560 -> 480
~ __ZN4bssl17ERR_restore_stateEPKNS_17err_save_state_stE : 448 -> 380
~ __ZL13we_are_forkedv : 44 -> 32
~ __ZN4bsslL25tls_seal_align_prefix_lenEPKNS_7SSLImplE : 188 -> 220
~ __ZN4bssl19ssl_get_new_sessionEPNS_13SSL_HANDSHAKEE : 1096 -> 1088
~ _srtp_aes_gcm_openssl_alloc : 732 -> 748
~ _srtp_aes_icm_openssl_alloc : 684 -> 700
~ _srtp_crypto_alloc -> _srtp_crypto_alloc_typed : 160 -> 156
~ _srtp_crypto_kernel_init : 1116 -> 1136
~ _srtp_crypto_kernel_load_debug_module : 288 -> 296
~ _srtp_crypto_kernel_load_cipher_type : 344 -> 352
~ _srtp_crypto_kernel_load_auth_type : 344 -> 352
~ _bitvector_alloc : 228 -> 236
~ _srtp_hmac_alloc : 624 -> 640
~ _srtp_null_auth_alloc : 284 -> 292
~ _srtp_null_cipher_alloc : 248 -> 256
~ _srtp_stream_clone : 796 -> 812
~ _srtp_stream_alloc : 1392 -> 1412
~ _srtp_create : 468 -> 484
~ _srtp_update_stream : 908 -> 924
```

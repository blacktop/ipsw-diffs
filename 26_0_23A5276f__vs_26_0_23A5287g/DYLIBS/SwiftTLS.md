## SwiftTLS

> `/System/Library/PrivateFrameworks/SwiftTLS.framework/SwiftTLS`

```diff

-108.0.7.0.0
-  __TEXT.__text: 0x88804
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__const: 0x6300
-  __TEXT.__swift5_typeref: 0xc4c
-  __TEXT.__constg_swiftt: 0x14e0
-  __TEXT.__swift5_reflstr: 0x1e83
-  __TEXT.__swift5_fieldmd: 0x22b8
-  __TEXT.__swift5_proto: 0x2cc
-  __TEXT.__swift5_types: 0x210
+108.0.11.0.0
+  __TEXT.__text: 0x8f598
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__const: 0x6b00
+  __TEXT.__swift5_typeref: 0xcb6
+  __TEXT.__constg_swiftt: 0x1574
+  __TEXT.__swift5_reflstr: 0x21a3
+  __TEXT.__swift5_fieldmd: 0x24a4
+  __TEXT.__swift5_proto: 0x2e0
+  __TEXT.__swift5_types: 0x21c
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x70
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__oslogstring: 0x2d25
-  __TEXT.__cstring: 0xcf1
-  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__oslogstring: 0x2f95
+  __TEXT.__cstring: 0x1011
+  __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__unwind_info: 0x1790
-  __TEXT.__eh_frame: 0x2f2c
-  __DATA_CONST.__got: 0x220
+  __TEXT.__unwind_info: 0x1860
+  __TEXT.__eh_frame: 0x2fd4
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2ae8
-  __AUTH_CONST.__objc_const: 0x1f0
+  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__const: 0x2c08
+  __AUTH_CONST.__objc_const: 0x2a8
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x1f68
-  __DATA.__data: 0x1058
-  __DATA.__bss: 0x5080
-  __DATA.__common: 0x60
+  __AUTH.__data: 0x2038
+  __DATA.__data: 0x1168
+  __DATA.__bss: 0x5300
+  __DATA.__common: 0xa8
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate

   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 17CBDA8C-DDBB-3478-BECA-F883F6B64AFE
-  Functions: 1970
-  Symbols:   682
-  CStrings:  318
+  UUID: 629AA980-04C0-38B9-8BB0-539BA374D435
+  Functions: 2050
+  Symbols:   704
+  CStrings:  350
 
Symbols:
+ __DATA__TtC8SwiftTLS11PAKELimiter
+ __IVARS__TtC8SwiftTLS11PAKELimiter
+ __METACLASS_DATA__TtC8SwiftTLS11PAKELimiter
+ ___swift_memcpy121_8
+ ___swift_memcpy122_8
+ ___swift_memcpy25_8
+ ___swift_memcpy49_8
+ _associated conformance 8SwiftTLS13knownTLSAlertOSHAASQ
+ _associated conformance 8SwiftTLS14PAKECredentialVSHAASQ
+ _get_type_metadata 15Synchronization5MutexVySDy8SwiftTLS14PAKECredentialVs6UInt32VGG.3
+ _objc_opt_self
+ _objc_release_x28
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_runtimeSupportsNoncopyableTypes
+ _symbolic SDy__________G 8SwiftTLS14PAKECredentialV s6UInt32V
+ _symbolic _____ 8SwiftTLS11PAKELimiterC
+ _symbolic _____ 8SwiftTLS13knownTLSAlertO
+ _symbolic _____ 8SwiftTLS14PAKECredentialV
+ _symbolic _____Sg 8SwiftTLS5AlertV
+ _symbolic _____ySDy__________GG 15Synchronization5MutexVAARi_zrlE 8SwiftTLS14PAKECredentialV s6UInt32V
+ _symbolic _____y__________G s18_DictionaryStorageC 8SwiftTLS14PAKECredentialV s6UInt32V
+ _type_layout_string 8SwiftTLS14PAKECredentialV
+ _type_layout_string 8SwiftTLS16PAKEServerRecordV
- ___swift_get_extra_inhabitant_index.8Tm
- ___swift_memcpy73_8
- ___swift_store_extra_inhabitant_index.9Tm
CStrings:
+ "First data TLS server received did not match a valid Client Hello"
+ "PAKE credential exhausted"
+ "PAKECredentials"
+ "TLS client unexpectedly processed network data before sending client hello. This should never happen."
+ "TLS error occurred from processing network data before handshake started: %s"
+ "_TtC8SwiftTLS11PAKELimiter"
+ "bad certificate status response"
+ "certificate expired"
+ "certificate required"
+ "certificate revoked"
+ "certificate unknown"
+ "client claiming PAKE attempt failed"
+ "client credential already tracked by PAKE Limiter"
+ "error restoring PAKE Credential Attempt"
+ "error restoring PAKE Credential Attempt. This should never happen."
+ "failed to process Server Hello pake share %@"
+ "illegal parameter"
+ "inappropriate fallback"
+ "insufficient security"
+ "missing extension"
+ "new client credential added to PAKE Limiter"
+ "new server credential added to PAKE Limiter"
+ "no application protocol"
+ "protocol version"
+ "restored PAKE credential attempt"
+ "selected PAKE credential has no attempts remaining"
+ "server credential already tracked by PAKE Limiter"
+ "unexpected message"
+ "unknown psk identity"
+ "unrecognized name"
+ "unsupported certificate"
+ "unsupported extension"

```

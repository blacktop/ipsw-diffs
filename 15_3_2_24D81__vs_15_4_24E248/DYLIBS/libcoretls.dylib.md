## libcoretls.dylib

> `/usr/lib/libcoretls.dylib`

```diff

 186.0.0.0.0
-  __TEXT.__text: 0x1217c
+  __TEXT.__text: 0x11f10
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__const: 0x310
+  __TEXT.__const: 0x2e8
   __TEXT.__cstring: 0x3dc7
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__unwind_info: 0x3f0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x8e0
+  __DATA_CONST.__const: 0x8f0
   __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x4a8
   __AUTH_CONST.__cfstring: 0x20

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
-  UUID: 54006172-9144-3320-8739-D1D273ACB8EA
-  Functions: 362
-  Symbols:   519
+  UUID: A18907DD-0734-3978-962F-63E80353B232
+  Functions: 363
+  Symbols:   530
   CStrings:  504
 
Symbols:
+ SSLEncodeKeyExchange.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _SSLSignServerKeyExchangeTls12
+ _SSLVerifySignedServerKeyExchange
+ _SSLVerifySignedServerKeyExchangeTls12
+ sslGetPubKeyFromBits.cold.1
+ sslRsaEncrypt.cold.1
+ tls_metric_client_finished.cold.1
+ tls_metric_destroyed.cold.1
+ tls_metric_insecure_dh_param.cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslAesGcmCipher.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslAlertMessage.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslCert.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslChangeCipher.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslCrypto.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslDecode.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshake.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshakeFinish.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshakeHello.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslKeyExchange.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/symCipher.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/tls_handshake.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/tls_record.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslAesGcmCipher.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslAlertMessage.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslCert.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslChangeCipher.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslCrypto.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslDecode.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshake.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshakeFinish.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslHandshakeHello.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/sslKeyExchange.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/symCipher.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/tls_handshake.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/coreTLS/lib/tls_record.c"

```

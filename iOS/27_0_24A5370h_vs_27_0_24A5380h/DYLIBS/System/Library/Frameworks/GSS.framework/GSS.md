## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-  __TEXT.__text: 0x27124
-  __TEXT.__const: 0x43a
-  __TEXT.__cstring: 0x3abb
+  __TEXT.__text: 0x27fd0
+  __TEXT.__const: 0x44a
+  __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__unwind_info: 0x738
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1378
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2b8
   __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__auth_got: 0xf68
+  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH.__data: 0x1360
   __DATA.__data: 0xd10
   __DATA.__bss: 0x28c
   __DATA.__common: 0x94
-  __DATA_DIRTY.__data: 0x1360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 668
-  Symbols:   2151
-  CStrings:  650
+  Functions: 673
+  Symbols:   2163
+  CStrings:  660
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Symbols:
+ __gsskrb5_make_header
+ _krb5_decrypt_ivec
+ _krb5_encrypt_ivec
CStrings:
+ "encdata.length == 8"
+ "get_mic.c"
+ "mic_des3"
+ "tmp.length == datalen"
+ "tmp.length == input_message_buffer->length - len"
+ "unwrap.c"
+ "unwrap_des3"
+ "wrap.c"
+ "wrap_des3"
+ "\xff\xff"

```

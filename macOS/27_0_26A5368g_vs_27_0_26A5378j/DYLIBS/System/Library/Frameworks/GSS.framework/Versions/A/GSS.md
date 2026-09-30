## GSS

> `/System/Library/Frameworks/GSS.framework/Versions/A/GSS`

```diff

-  __TEXT.__text: 0x48ce4
-  __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x3d0c
+  __TEXT.__text: 0x4a914
+  __TEXT.__const: 0x494
+  __TEXT.__cstring: 0x3da0
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__unwind_info: 0x348
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1390
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x488
   __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__auth_got: 0x1020
-  __AUTH.__data: 0x288
+  __AUTH_CONST.__auth_got: 0x1030
+  __AUTH.__data: 0x15e8
   __DATA.__data: 0xed8
   __DATA.__bss: 0x29c
   __DATA.__common: 0x8c
-  __DATA_DIRTY.__data: 0x13a0
+  __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 742
-  Symbols:   1731
-  CStrings:  680
+  Functions: 747
+  Symbols:   1738
+  CStrings:  689
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Symbols:
+ _krb5_decrypt_ivec
+ _krb5_encrypt_ivec
+ _mic_des3
+ _sub_wrap_size
+ _unwrap_des3
+ _verify_mic_des3
+ _wrap_des3
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

```

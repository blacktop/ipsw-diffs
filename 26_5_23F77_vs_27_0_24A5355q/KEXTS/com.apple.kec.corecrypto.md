## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-1922.122.1.0.0
-  __TEXT.__cstring: 0x4c7d
-  __TEXT.__const: 0x196e0
+2097.0.0.0.0
+  __TEXT.__cstring: 0x4d8c
+  __TEXT.__const: 0x1b5a0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x6a6ac
+  __TEXT_EXEC.__text: 0x6db84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9340
-  __DATA.__bss: 0x29e0
+  __DATA.__bss: 0x2a00
   __DATA.__common: 0x140
+  __DATA_CONST.__const: 0x42a8
   __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__auth_ptr: 0x178
-  __DATA_CONST.__const: 0x3fc8
-  UUID: FE36ADEC-348B-3C8A-BE6D-2D60A910526E
-  Functions: 1847
+  __DATA_CONST.__auth_ptr: 0x190
+  UUID: 8A881D11-8D6A-356B-92EF-C2C6E52A4443
+  Functions: 1960
   Symbols:   0
-  CStrings:  463
+  CStrings:  470
 
CStrings:
+ "AES_ECB_ARM_ALIGNED"
+ "AES_XTS_ARM_ALIGNED"
+ "SHA256_VNG_ARM_ALIGNED"
+ "ccdit_managed_context_begin MUST have been called"
+ "ccrng failed assert cbc_info->block_size = %lu\n"
+ "ccrng failed assert key_nbytes = %lu\n"
+ "ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n"

```

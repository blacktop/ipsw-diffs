## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-1922.122.1.0.0
-  __TEXT.__cstring: 0x4c7d sha256:8700fdaa56b763cda2e74ede24332c370903cdb0d16daa08a7b78492fb1ccf63
-  __TEXT.__const: 0x196e0 sha256:9733b0ea367d7ef7636d45925968ab18559df397bbe38ad3545fda6c8f640e16
-  __TEXT.__fips_hmacs: 0x20 sha256:514a69e945f37bd8caccbd92c7b17dc9387a3bf6c0f97a9e8fb03623040ff97d
-  __TEXT_EXEC.__text: 0x6a6ac sha256:e957a5b59c8b4ceed234262ba797278c416cc4faa45a14107e28fd245794e55f
+2097.0.0.0.0
+  __TEXT.__cstring: 0x4d8c sha256:a39380a9ea6b971c2ab5a5801e404cbc27dfcdc7d0b038f85eb8d14174e593bd
+  __TEXT.__const: 0x1b5a0 sha256:afe45cffcb87cdd72871cfbcea0e5c535b372efaca1e14845e047bf5dad84327
+  __TEXT.__fips_hmacs: 0x20 sha256:5f3530ecdaf5af79f981387313f088c6e49eb6cc542708d427a078198256e4af
+  __TEXT_EXEC.__text: 0x6db84 sha256:c79e9e3dc8a7b4e5000f667b1db272f39a024e39a3a7be6ffd3757883707b2af
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9340 sha256:f246d5d906eba476ddda3a86fdea20b4809e0c826dac4a3e89bdac847f0df025
-  __DATA.__bss: 0x29e0 sha256:e0080fb45c4c76ec3143dc390903b85d2d3d7d72594137e366a43b64a49ba83e
+  __DATA.__data: 0x9340 sha256:8b25a472d5b4e2a783049c69bdfc84a17a02c39656506b7e57de1155c6b0fdbd
+  __DATA.__bss: 0x2a00 sha256:ee0d534dd385f4c26c52ee121654897b783c0754c6512886e53578dce4b24735
   __DATA.__common: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
-  __DATA_CONST.__auth_got: 0x128 sha256:bb72bd7108976b5b5547266526f909d57f2f804f22cdcd23cdd0b241b34885b0
-  __DATA_CONST.__got: 0x10 sha256:216bb52551348bf1260c531f4c538027f7d410cbc1777063338f40619f43b442
-  __DATA_CONST.__auth_ptr: 0x178 sha256:9665ac8fd2ec5cbdc6a02585a678cad89581a50ec2bc4662abc16da427f1f29e
-  __DATA_CONST.__const: 0x3fc8 sha256:bd3edd6ad52573d91a3ba896ec51b3364a76cf00472948d7227f85d464fd16e7
-  UUID: FE36ADEC-348B-3C8A-BE6D-2D60A910526E
-  Functions: 1847
+  __DATA_CONST.__const: 0x42a8 sha256:10553fb1f50151412cba3d23f6e04dd3feb4b34995b7d574dbecfe49b262de00
+  __DATA_CONST.__auth_got: 0x128 sha256:58ca5c7d6b141df3c05712f8498901bfc6ecd7c2e330798b31da492a1367c955
+  __DATA_CONST.__got: 0x10 sha256:a4bdd3fe2c1d28853456dc2136bf130c1f42622b356f393bda41bf172cf62586
+  __DATA_CONST.__auth_ptr: 0x190 sha256:1505da9d009d1c8ac5a596cfdb701625826fa2b0e0cb26371e822315e75d2ba2
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

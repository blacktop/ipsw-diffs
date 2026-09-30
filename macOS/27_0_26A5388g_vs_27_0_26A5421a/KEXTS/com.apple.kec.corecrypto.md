## com.apple.kec.corecrypto

> `com.apple.kec.corecrypto`

```diff

-2109.0.17.0.0
-  __TEXT.__cstring: 0x4218
-  __TEXT.__const: 0x10140
+2109.0.22.0.0
+  __TEXT.__cstring: 0x447d
+  __TEXT.__const: 0x10180
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x69f84
+  __TEXT_EXEC.__text: 0x6da04
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0x29e0
   __DATA.__bss: 0x27c0

   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x188
-  Functions: 1942
-  Symbols:   2108
-  CStrings:  347
+  Functions: 1947
+  Symbols:   2116
+  CStrings:  368
 
Symbols:
+ ___copy_assignment_8_8_t0w16_pa0_42493_16_pa0_9870_24_pa0_60491_32_pa0_55059_40_pa0_12009_48_pa2_16338_56_pa2_19169_64
+ ___copy_assignment_8_8_t0w16_pa0_53749_16_pa0_54423_24_pa2_28518_32
+ ___copy_assignment_8_8_t0w16_pa0_56220_16_pa0_52116_24_pa2_29440_32
+ ___copy_assignment_8_8_t0w16_pa0_6908_16_pa0_15199_24_pa2_44169_32
+ ___copy_assignment_8_8_t0w16_pa0_6943_16_pa0_16199_24_pa0_20536_32_pa0_3805_40_pa0_49655_48_pa2_39956_56_pa2_57666_64
+ ___copy_assignment_8_8_t0w16_pa0_9268_16_pa0_46422_24_pa2_36887_32
+ ___copy_assignment_8_8_t0w24_pa0_18425_24_pa0_20237_32_pa0_36020_40_pa0_40644_48_pa0_56591_56_pa0_4241_64_pa2_30758_72
+ ___copy_assignment_8_8_t0w24_pa0_54061_24_pa0_9080_32_pa0_19860_40_pa0_6512_48_pa0_3468_56_pa0_60028_64_pa2_2379_72_t80w1
+ ___copy_assignment_8_8_t0w24_pa0_61651_24_pa0_61484_32_pa0_17609_40_pa2_21019_48
+ _init_ctr
+ _rej_rnd_kat
+ _rej_sig_sha256_kat
+ _validate_inputs
- ___copy_assignment_8_8_t0w16_pa0_42493_16_pa0_9870_24_pa0_60491_32_pa0_55059_40_pa0_12009_48_t56w16
- ___copy_assignment_8_8_t0w16_pa0_6943_16_pa0_16199_24_pa0_20536_32_pa0_3805_40_pa0_49655_48_t56w16
- ___copy_assignment_8_8_t0w24_pa0_18425_24_pa0_20237_32_pa0_36020_40_pa0_40644_48_pa0_56591_56_pa0_4241_64_t72w8
- ___copy_assignment_8_8_t0w24_pa0_54061_24_pa0_9080_32_pa0_19860_40_pa0_6512_48_pa0_3468_56_pa0_60028_64_t72w9
- ___copy_assignment_8_8_t0w24_pa0_61651_24_pa0_61484_32_pa0_17609_40_t48w8
CStrings:
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n"
+ "FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n"
+ "cckem_decapsulate"
+ "cckem_encapsulate"
+ "cckem_generate_key"
+ "cckem_generate_key_with_seed"
+ "cckem_mlkem1024"
+ "cckem_mlkem768"
+ "ccmldsa65"
+ "ccmldsa87"
+ "ccmldsa_generate_key"
+ "ccmldsa_generate_key_with_seed"
+ "ccmldsa_sign"
+ "ccmldsa_sign_prehashed"
+ "ccmldsa_sign_with_context"
+ "ccmldsa_verify"
+ "ccmldsa_verify_prehashed"
+ "ccmldsa_verify_with_context"
+ "fipspost_post_mldsa_sign_rejection_kat"
```

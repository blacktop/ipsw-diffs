## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-912.89.1.0.0
-  __TEXT.__const: 0x4b240 sha256:c7d130a86b55329925a26184d6d1bb102297fce0eead3dd4e04940554e662411
-  __TEXT.__cstring: 0x46e4a sha256:29fc07430589277d3a8229fd8949ba71fdf3aba37624eaec8f2a3fc4acaabe5e
-  __TEXT.__os_log: 0x5b67f sha256:5bb8202e38d9f5d8956ad2be36b6de50d4bc5a9ed4e4f29398a93967181ba9f2
-  __TEXT_EXEC.__text: 0x1c6a50 sha256:143df25b68ac5775336881c211c70b33725dccda876a1e916c24e7c3ca0bd74c
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2c8 sha256:2c8d7799bbb67b666859b7ef9d694246a861498bced706d561102f3e6df57208
+913.8.0.0.0
+  __TEXT.__const: 0x4b760 sha256:7b1628168ce9485269ed6c33cd3bff9ea95e09d6d1c1283d83d26b3a52563921
+  __TEXT.__cstring: 0x4736f sha256:77df643291e48abbd3797901315d098b24b78db926f737ea5cb762182041fee7
+  __TEXT.__os_log: 0x5bc39 sha256:22a909562ab57e151db139d8a58f64ab421ceaad65cc1823e3aebdf0be6f7176
+  __TEXT_EXEC.__text: 0x1c9b10 sha256:2efc35ba86eba89e2bd6be1e4caae712844ed3f424e13f569738f667fa083199
+  __TEXT_EXEC.__auth_stubs: 0x7b0 sha256:c9f2f40f2a1cc3a41ebb4ad4ce24cbb504a28e5f65865f5e44c1db6397eaf516
+  __DATA.__data: 0x2c8 sha256:910a6d32cc948bc21be25764ca9616a05d294658ac1cd42962f4f993de9df8af
   __DATA.__common: 0x130 sha256:e2fc162ed9124452d23c85e81d60a0c228f414c3214a5de635737e25fbd29ac1
   __DATA.__bss: 0x3c0 sha256:3dc463a76fc170607c07b104c3cb531362ce7d6e10c1a34e0c0f370aeae08ce8
-  __DATA_CONST.__mod_init_func: 0x38 sha256:6d8dbcd67a0a965053bd220abedde72f2e3aff35b69d1ab60a6a9bc872695177
-  __DATA_CONST.__mod_term_func: 0x38 sha256:e4fa3de23a632a7741f6f759b234955ef874d103d6092f317811b4c91bbe7034
-  __DATA_CONST.__const: 0xaff0 sha256:36045d7461046c1d8879896c66a7a83c7ba112317f9e317306442b1b417e2641
-  __DATA_CONST.__kalloc_type: 0x5300 sha256:3011391791ab79e4a2d990af0f47623bfd8dfc0c4d94ce3cbba8848c42792a79
-  __DATA_CONST.__kalloc_var: 0x1e00 sha256:7bcb70ff727c33ec6f27fb9b03b52c1c5fde1ce326f2857d564899579acd8470
-  __DATA_CONST.__auth_got: 0x3d8 sha256:78e715ef383f635faf3ae1f65df871816006bc573918f2d90794fa4a639f9060
-  __DATA_CONST.__got: 0xe8 sha256:a5c6b80588d40aae2a434e59752a7aed4bbdbf17e68fe03b7907e882c1e0ae2c
-  __DATA_CONST.__auth_ptr: 0x8 sha256:1649d5cf5a1076f338c67612cfcf5616ac951abee6cce719af2fcb7f366a5957
-  UUID: E2BF715C-3842-3291-AA40-2075DABF2D95
+  __DATA_CONST.__mod_init_func: 0x38 sha256:d28cc40fdbc00fb8e8fe50260ec77292aed7be67e97e7292e66cde027b718690
+  __DATA_CONST.__mod_term_func: 0x38 sha256:52f15f160d0bc4bd4b65351c601b3ec35891a14cc267d25f6625f12be77ba8c4
+  __DATA_CONST.__const: 0xb020 sha256:aa2bffef21c81f058380c0c6d65d072a236299f68ad237db4e958c438c680898
+  __DATA_CONST.__kalloc_type: 0x5300 sha256:1b81da7ba975942bd67c04db028ddcb62f343706ead02bc5d1bbff861578b0cc
+  __DATA_CONST.__kalloc_var: 0x1e00 sha256:835f17f83b8096a0770cb2ac227b5b6549fa30e0789817559c004f52aee6b031
+  __DATA_CONST.__auth_got: 0x3d8 sha256:84bc18cbb2ea092562c913942c0164909472a158ede272aff8d964f38b7a29ae
+  __DATA_CONST.__got: 0xe8 sha256:4af89965075eb78939d838c4a36c587acc37717f3ffa812d2c441c065b73083d
+  __DATA_CONST.__auth_ptr: 0x8 sha256:421c256509b78f15fcc341b197a04d2df8fb111d83b4f873e2db29cb4ff5cc8b
+  UUID: C840DD30-8F12-37D7-A253-14583FB73EBF
   Functions: 2994
   Symbols:   0
-  CStrings:  9730
+  CStrings:  9762
 
CStrings:
+ "%lld %d AVE %s: %p %lld MCTFEnableFeedback %d"
+ "%lld %d AVE %s: %p %lld MCTFEnableFeedback %d\n"
+ "%lld %d AVE %s: %p %lld MCTFEnableGating %d"
+ "%lld %d AVE %s: %p %lld MCTFEnableGating %d\n"
+ "%lld %d AVE %s: %p MCTFEnableFeedback %d"
+ "%lld %d AVE %s: %p MCTFEnableFeedback %d\n"
+ "%lld %d AVE %s: %p MCTFEnableGating %d"
+ "%lld %d AVE %s: %p MCTFEnableGating %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 HiRes compressed input %p %d %p %lld | 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 HiRes compressed input %p %d %p %lld | 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 HiRes linear %p %d %p %lld | 0x%llx 0x%llx %d %d"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 HiRes linear %p %d %p %lld | 0x%llx 0x%llx %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 LoRes compressed input %p %d %p %lld | 0x%llx %d"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 LoRes compressed input %p %d %p %lld | 0x%llx %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 LoRes linear %p %d %p %lld | 0x%llx 0x%llx %d %d"
+ "%lld %d AVE %s: %s:%d %s | invalid DMV2 LoRes linear %p %d %p %lld | 0x%llx 0x%llx %d %d\n"
+ "%lld %d AVE %s: %s:%d DMV2 HiResInput %p %d %lld %p %lld | compress=%d"
+ "%lld %d AVE %s: %s:%d DMV2 HiResInput %p %d %lld %p %lld | compress=%d\n"
+ "%lld %d AVE %s: %s:%d DMV2 LoResInput %p %d %lld %p %lld | compress=%d"
+ "%lld %d AVE %s: %s:%d DMV2 LoResInput %p %d %lld %p %lld | compress=%d\n"
+ "%p %lld MCTFEnableFeedback %d"
+ "%p %lld MCTFEnableFeedback %d\n"
+ "%p %lld MCTFEnableGating %d"
+ "%p %lld MCTFEnableGating %d\n"
+ "%p MCTFEnableFeedback %d"
+ "%p MCTFEnableFeedback %d\n"
+ "%p MCTFEnableGating %d"
+ "%p MCTFEnableGating %d\n"
+ "111211111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222"
+ "19:40:52"
+ "913.8.0"
+ "DMVHiResInput"
+ "DMVLoResInput"
+ "Jun 18 2026"
+ "pComp->saCPBuf[AVE_BufIdx_Luma].sCIBuf.saIBuf[AVE_BufIdx_Data].iAddr != 0 && pComp->saCPBuf[AVE_BufIdx_Luma].sCPInfo.iHeaderStride != 0"
+ "pLin->saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0 && pLin->saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iSize != 0 && pLin->saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iStride != 0 && (pLin->saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iStride % 64 == 0) && (pLin->saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iStride % 64 == 0)"
- "1112111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222"
- "21:27:09"
- "912.89.1"
- "Jun  1 2026"

```

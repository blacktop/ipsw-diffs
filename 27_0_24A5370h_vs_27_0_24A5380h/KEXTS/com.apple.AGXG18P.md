## com.apple.AGXG18P

> `com.apple.AGXG18P`

```diff

   __TEXT.__const: 0x42f4
   __TEXT.__os_log: 0x1064
-  __TEXT.__cstring: 0xfba3
-  __TEXT_EXEC.__text: 0xd3dc4
-  __TEXT_EXEC.__auth_stubs: 0x1a90
+  __TEXT.__cstring: 0xfcb7
+  __TEXT_EXEC.__text: 0xd4520
+  __TEXT_EXEC.__auth_stubs: 0x1a80
   __DATA.__data: 0x15c0
   __DATA.__common: 0x10
   __DATA.__bss: 0x4d40

   __DATA_CONST.__const: 0x11318
   __DATA_CONST.__kalloc_type: 0x2480
   __DATA_CONST.__kalloc_var: 0x2670
-  __DATA_CONST.__auth_got: 0xd48
+  __DATA_CONST.__auth_got: 0xd40
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 3420
   Symbols:   0
-  CStrings:  2023
+  CStrings:  2027
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ sub_fffffe000849dbac -> sub_fffffe0008495b9c : 22384 -> 22380
~ sub_fffffe00084a331c -> sub_fffffe000849b308 : 672 -> 704
~ sub_fffffe00084a8784 -> sub_fffffe00084a0790 : 204 -> 368
~ sub_fffffe00084b8ecc -> sub_fffffe00084b0f7c : 400 -> 448
~ sub_fffffe00084b905c -> sub_fffffe00084b113c : 328 -> 376
~ sub_fffffe00084c2e70 -> sub_fffffe00084baf80 : 1776 -> 1676
~ sub_fffffe00084ce228 -> sub_fffffe00084c62d4 : 416 -> 404
~ sub_fffffe00084d8254 -> sub_fffffe00084d02f4 : 1976 -> 1984
~ sub_fffffe00084d8e40 -> sub_fffffe00084d0ee8 : 5204 -> 5136
~ sub_fffffe00084dc0b0 -> sub_fffffe00084d4114 : 3380 -> 3364
~ sub_fffffe00084e822c -> sub_fffffe00084e0280 : 356 -> 364
~ sub_fffffe00084e83e8 -> sub_fffffe00084e0444 : 16 -> 20
~ sub_fffffe00084e83f8 -> sub_fffffe00084e0458 : 220 -> 224
~ sub_fffffe00084e88f0 -> sub_fffffe00084e0954 : 1852 -> 1820
~ sub_fffffe00084ea970 -> sub_fffffe00084e29b4 : 24 -> 20
~ sub_fffffe00084ea988 -> sub_fffffe00084e29c8 : 24 -> 20
~ sub_fffffe00084ea9a0 -> sub_fffffe00084e29dc : 24 -> 20
~ sub_fffffe00084ea9b8 -> sub_fffffe00084e29f0 : 24 -> 20
~ sub_fffffe00084ea9d0 -> sub_fffffe00084e2a04 : 24 -> 20
~ sub_fffffe00084ea9e8 -> sub_fffffe00084e2a18 : 24 -> 20
~ sub_fffffe00084eb204 -> sub_fffffe00084e3230 : 152 -> 148
~ sub_fffffe00084eb29c -> sub_fffffe00084e32c4 : 152 -> 148
~ sub_fffffe00084faa84 -> sub_fffffe00084f2aa8 : 532 -> 528
~ sub_fffffe00084fba64 -> sub_fffffe00084f3a84 : 292 -> 316
~ sub_fffffe00084fbb88 -> sub_fffffe00084f3bc0 : 540 -> 544
~ sub_fffffe00084fbda4 -> sub_fffffe00084f3de0 : 568 -> 572
~ sub_fffffe00084fbfdc -> sub_fffffe00084f401c : 536 -> 540
~ sub_fffffe00084fc1f4 -> sub_fffffe00084f4238 : 576 -> 592
~ sub_fffffe00084fd5b0 -> sub_fffffe00084f5604 : 9600 -> 9596
~ sub_fffffe0008501c08 -> sub_fffffe00084f9c58 : 9052 -> 8944
~ sub_fffffe0008503f64 -> sub_fffffe00084fbf48 : 904 -> 860
~ sub_fffffe0008507794 -> sub_fffffe00084ff74c : 7480 -> 7776
~ sub_fffffe00085094cc -> sub_fffffe00085015ac : 9788 -> 10172
~ sub_fffffe0008510fac -> sub_fffffe000850920c : 5452 -> 5744
~ sub_fffffe0008517628 -> sub_fffffe000850f9ac : 108 -> 112
~ sub_fffffe0008517694 -> sub_fffffe000850fa1c : 324 -> 316
~ sub_fffffe0008517828 -> sub_fffffe000850fba8 : 2684 -> 2776
~ sub_fffffe00085198a8 -> sub_fffffe0008511c84 : 8680 -> 9020
~ sub_fffffe0008529bb8 -> sub_fffffe00085220e8 : 860 -> 828
~ sub_fffffe000853bf44 -> sub_fffffe0008534454 : 3620 -> 3628
~ sub_fffffe00085434d8 -> sub_fffffe000853b9f0 : 1288 -> 1276
~ sub_fffffe00085520f4 -> sub_fffffe000854a600 : 536 -> 540
~ sub_fffffe000855230c -> sub_fffffe000854a81c : 1268 -> 1832
~ sub_fffffe0008559890 -> sub_fffffe0008551fd4 : 316 -> 324
CStrings:
+ "121111122"
+ "3.44.10"
+ "AGXk: %s:%d:%s: !!! Out-of-range command_stage_mask 0x%x\n"
+ "Jun 30 2026 21:10:44"
+ "com.apple.agx.thmcounters"
+ "sfe_tier3"
+ "thm_activations"
+ "void AGXCommandBuffer::mergeSubmitEventForStage(uint32_t, const sIOGPUEvent *, const sIOGPUEvent *, uint64_t)"
+ "void AGXCommandBuffer::updateBarrierEvent(uint32_t, sIOGPUEvent *, sIOGPUEvent *, uint64_t)"
- "1211111"
- "3.44.9"
- "Jun 18 2026 19:39:50"
- "cltmlimit_qp"
- "gpu-cltm-limit-mrc-period"

```

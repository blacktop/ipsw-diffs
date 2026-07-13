## com.apple.AGXG18P

> `com.apple.AGXG18P`

```diff

   __TEXT.__const: 0x42f4
   __TEXT.__os_log: 0xfff
-  __TEXT.__cstring: 0x1213f
-  __TEXT_EXEC.__text: 0xd4920
+  __TEXT.__cstring: 0x12243
+  __TEXT_EXEC.__text: 0xd4850
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1594
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x3bb0
   Functions: 3470
   Symbols:   0
-  CStrings:  2096
+  CStrings:  2099
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
Functions:
~ sub_fffffe00083216e4 -> sub_fffffe000830d6e4 : 404 -> 452
~ sub_fffffe0008321878 -> sub_fffffe000830d8a8 : 224 -> 272
~ sub_fffffe0008329dd0 -> sub_fffffe0008315e30 : 6024 -> 5844
~ sub_fffffe000832ca74 -> sub_fffffe0008318a20 : 4312 -> 4188
CStrings:
+ "AGXk: %s:%d:%s: !!! Out-of-range command_stage_mask 0x%x\n"
+ "Jul  9 2026 23:35:48"
+ "void AGXCommandBuffer::mergeSubmitEventForStage(uint32_t, const sIOGPUEvent *, const sIOGPUEvent *, uint64_t)"
+ "void AGXCommandBuffer::updateBarrierEvent(uint32_t, sIOGPUEvent *, sIOGPUEvent *, uint64_t)"
- "Jun 28 2026 20:09:35"

```

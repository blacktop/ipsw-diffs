## com.apple.AGXG13G

> `com.apple.AGXG13G`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-353.12.0.0.0
+353.14.0.0.0
   __TEXT.__const: 0x26fc
   __TEXT.__os_log: 0x1251
-  __TEXT.__cstring: 0x101a5
-  __TEXT_EXEC.__text: 0xbaa30
+  __TEXT.__cstring: 0x102a9
+  __TEXT_EXEC.__text: 0xba930
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1f90
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x3ed0
   Functions: 2759
   Symbols:   4576
-  CStrings:  1879
+  CStrings:  1882
 
Functions:
~ __ZN16AGXCommandBuffer18updateBarrierEventEjP10IOGPUEventS1_y : 404 -> 452
~ __ZN16AGXCommandBuffer24mergeSubmitEventForStageEjPK10IOGPUEventS2_y : 224 -> 272
~ __ZN15AGXCommandQueue19processComputeSetupER22AGXCLCommandDescriptorP18AGXAllocationList2RK24AGXHardwareKernelCommandRK23AGXSegmentKernelCommandP21CompositeSubtypeStateRK31AGXComputeHardwareKernelCommandyy : 6452 -> 6276
~ __ZN15AGXCommandQueue22processFastRenderSetupER22AGX3DCommandDescriptoryyRK24AGXHardwareKernelCommandRK34AGXFastRenderHardwareKernelCommandRK23AGXSegmentKernelCommandP21CompositeSubtypeStateP18AGXAllocationList2 : 3852 -> 3676
CStrings:
+ "AGXk: %s:%d:%s: !!! Out-of-range command_stage_mask 0x%x\n"
+ "Jul 11 2026 18:44:33"
+ "void AGXCommandBuffer::mergeSubmitEventForStage(uint32_t, const sIOGPUEvent *, const sIOGPUEvent *, uint64_t)"
+ "void AGXCommandBuffer::updateBarrierEvent(uint32_t, sIOGPUEvent *, sIOGPUEvent *, uint64_t)"
- "Jun 21 2026 20:48:47"
```

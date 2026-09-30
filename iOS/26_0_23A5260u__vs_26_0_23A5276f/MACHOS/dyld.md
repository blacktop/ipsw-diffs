## dyld

> `/usr/lib/dyld`

```diff

-1318.0.0.0.0
-  __TEXT.__text: 0x89b8c
+1321.0.0.0.0
+  __TEXT.__text: 0x89a90
   __TEXT.__const: 0x22f0
-  __TEXT.__cstring: 0xfd96
+  __TEXT.__cstring: 0xfd93
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_ptr: 0x90
   __DATA_CONST.__const: 0x6f00

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0x70
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 8448A1C4-D759-3AC7-BD9E-1CEAA5714ACD
+  UUID: 8955619B-E236-3D86-9DB1-2E4141BF277A
   Functions: 2873
   Symbols:   3986
   CStrings:  1973
Symbols:
+ _ZL15hactivateRegionbbyyy.cold.1
+ _ZZN3lsl13MemoryManager4initEPPKcS3_PvENK3$_0clEv.cold.1
+ __ZL15hactivateRegionbbyyy
+ __ZNK15DyldSharedCache13forEachRegionEU13block_pointerFvPKvyyjjyyRbE
+ __ZZN3lsl13MemoryManager4initEPPKcS3_PvENK3$_0clEv
+ __block_descriptor_tmp.165
+ __block_descriptor_tmp.189
+ __block_descriptor_tmp.235
- _ZL22hactivateFileAllocatorbbbPv.cold.1
- _ZL22hactivateFileAllocatorbbbPv.cold.2
- _ZL22hactivateFileAllocatorbbbPv.cold.3
- __ZL22hactivateFileAllocatorbbbPv
- __ZNK15DyldSharedCache13forEachRegionEU13block_pointerFvPKvyyjjyRbE
- __block_descriptor_tmp.164
- __block_descriptor_tmp.236
CStrings:
+ "1321"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Jun 14 07:57:28 PDT 2025; root:libignition-58~5924/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sat Jun 14 07:57:28 PDT 2025; root:libignition-58~5924/libignition_core/RELEASE_ARM64E"
+ "hactivateRegion"
+ "v64@?0r^v8Q16Q24I32I36Q40Q48^B56"
- "1318"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Jun  1 20:36:40 PDT 2025; root:libignition-58~4709/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sun Jun  1 20:36:40 PDT 2025; root:libignition-58~4709/libignition_core/RELEASE_ARM64E"
- "tproMappingCount == 1"
- "v56@?0r^v8Q16Q24I32I36Q40^B48"

```

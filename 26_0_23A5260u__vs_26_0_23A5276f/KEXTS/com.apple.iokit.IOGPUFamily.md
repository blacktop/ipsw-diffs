## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-124.1.0.0.0
-  __TEXT.__cstring: 0x5a91
-  __TEXT.__os_log: 0x4886
+126.0.0.0.0
+  __TEXT.__cstring: 0x5a92
+  __TEXT.__os_log: 0x48be
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x4180c
+  __TEXT_EXEC.__text: 0x415cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x820

   __DATA_CONST.__kalloc_type: 0x1100
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0xa0
-  UUID: 1081778F-9A65-31A6-845A-582BE344C588
+  UUID: 0FF62F55-4C8F-3B11-9A12-D559A0B79086
   Functions: 1877
   Symbols:   0
-  CStrings:  846
+  CStrings:  847
 
Functions:
~ __ZN18IOGPUVirtualMemory18describeAllocationEP12OSDictionary : 1368 -> 1352
~ __ZN13IOGPUResource4freeEv : 1032 -> 1008
~ __ZN13IOGPUResource16newResourceGroupEP5IOGPUP11IOGPUDevicej : 500 -> 548
~ sub_fffffff00a52c7cc -> sub_fffffff00a577924 : 204 -> 260
~ sub_fffffff00a52fe78 -> sub_fffffff00a57b008 : 1320 -> 1324
~ __ZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcej : 5100 -> 4480
~ sub_fffffff00a5428cc -> sub_fffffff00a58d7f4 : 200 -> 208
~ __ZN17IOGPUCommandQueue20processKernelCommandEPK18IOGPUKernelCommandS2_ : 5276 -> 5296
~ __ZN17IOGPUCommandQueue21schedule_shared_eventEjybj : 644 -> 652
~ sub_fffffff00a5520e0 -> sub_fffffff00a59d02c : 444 -> 384
~ __ZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcej.cold.1 -> sub_fffffff00a5a5e24 : 44 -> 16
~ sub_fffffff00a55af40 -> __ZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcej.cold.3 : 16 -> 44
~ __ZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcej.cold.6 -> sub_fffffff00a5a5ec8 : 44 -> 16
~ sub_fffffff00a55afe4 -> __ZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcej.cold.6 : 16 -> 44
CStrings:
+ "%s: newResourceGroup failed to initialize resource map\n"
+ "111122222"
- "11112222"

```

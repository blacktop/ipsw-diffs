## com.apple.driver.AppleLSIFusionMPT

> `com.apple.driver.AppleLSIFusionMPT`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-416.0.0.0.0
-  __TEXT.__cstring: 0x34b9
+416.0.2.0.0
+  __TEXT.__cstring: 0x3504
   __TEXT.__const: 0x160
-  __TEXT_EXEC.__text: 0x14cc8
+  __TEXT_EXEC.__text: 0x14ccc
   __TEXT_EXEC.__auth_stubs: 0x7c0
   __DATA.__data: 0x118
   __DATA.__common: 0x1a8

   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
   __DATA_CONST.__const: 0x4190
-  __DATA_CONST.__kalloc_type: 0x280
-  __DATA_CONST.__kalloc_var: 0x1e0
+  __DATA_CONST.__kalloc_type: 0x300
+  __DATA_CONST.__kalloc_var: 0x370
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0xc0
   Functions: 528
-  Symbols:   1042
-  CStrings:  389
+  Symbols:   1049
+  CStrings:  394
 
Symbols:
+ _IOFreeTypeImpl
+ _IOMallocTypeImpl
+ __ZZN16AppleLSIFusionFC20ScanForTargetDevicesEjE21kalloc_type_view_1008
+ __ZZN16AppleLSIFusionFC21InitializeTargetForIDEyE20kalloc_type_view_775
+ __ZZN17AppleLSIFusionMPT20InitializeControllerEvE21kalloc_type_view_1279
+ __ZZN17AppleLSIFusionMPT23AllocateAuxiliaryFramesEbjE21kalloc_type_view_2334
+ __ZZN17AppleLSIFusionMPT23AllocateAuxiliaryFramesEbjE21kalloc_type_view_2371
+ __ZZN17AppleLSIFusionMPT25DeallocateAuxiliaryFramesEbjE21kalloc_type_view_2462
+ __ZZN17AppleLSIFusionMPT4freeEvE21kalloc_type_view_1580
- _IOFree
- _IOMalloc
Functions:
~ __ZN17AppleLSIFusionMPT20InitializeControllerEv : 608 -> 580
~ __ZN17AppleLSIFusionMPT23AllocateAuxiliaryFramesEbj : 732 -> 712
~ __ZN17AppleLSIFusionMPT25DeallocateAuxiliaryFramesEbj : 312 -> 328
~ _OUTLINED_FUNCTION_14 : 12 -> 32
~ _OUTLINED_FUNCTION_15 : 32 -> 12
~ __ZN16AppleLSIFusionFC21InitializeTargetForIDEy : 420 -> 424
~ __ZN16AppleLSIFusionFC20ScanForTargetDevicesEj : 2204 -> 2208
~ __ZN17AppleLSIFusionMPT4freeEv : 276 -> 288
~ _ZN17AppleLSIFusionMPT23AllocateAuxiliaryFramesEbj.cold.1 : 52 -> 68
CStrings:
+ "1"
+ "1122222"
+ "site.AppleFibreChannelDeviceData"
+ "site.IODMACommand *"
+ "site.void *"
```

## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-13.0.28.0.0
-  __TEXT.__const: 0x460
-  __TEXT.__cstring: 0xe84
-  __TEXT.__os_log: 0x1aa8
-  __TEXT_EXEC.__text: 0x1a874
+13.0.31.0.0
+  __TEXT.__const: 0x470
+  __TEXT.__cstring: 0xeac
+  __TEXT.__os_log: 0x1b11
+  __TEXT_EXEC.__text: 0x1ab80
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x240

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4d30
   __DATA_CONST.__kalloc_type: 0x7c0
-  UUID: 3C9CE710-C3DA-3AA2-AB8B-14DE9C189EDD
+  UUID: 8EB2A5C6-2E74-3173-94F8-51BFE13CE52B
   Functions: 615
   Symbols:   830
-  CStrings:  275
+  CStrings:  278
 
Symbols:
+ __block_descriptor_tmp.43
+ __block_descriptor_tmp.49
- __block_descriptor_tmp.40
Functions:
~ sub_5a9c : 4688 -> 4692
~ sub_6e2c -> sub_6e30 : 304 -> 300
~ sub_a084 : 64 -> 72
~ sub_a0c4 -> sub_a0cc : 64 -> 332
~ sub_a104 -> sub_a218 : 200 -> 24
~ sub_a1cc -> sub_a230 : 176 -> 200
~ sub_a27c -> sub_a2f8 : 588 -> 176
~ sub_a4c8 -> sub_a3a8 : 428 -> 588
~ sub_a674 -> sub_a5f4 : 296 -> 428
~ sub_a79c -> sub_a7a0 : 20 -> 296
~ sub_a7b0 -> sub_a8c8 : 24 -> 20
~ sub_aa78 -> sub_ab8c : 972 -> 1000
~ _OUTLINED_FUNCTION_19 -> _OUTLINED_FUNCTION_20 : 24 -> 12
~ _OUTLINED_FUNCTION_21 : 12 -> 32
~ _OUTLINED_FUNCTION_23 : 32 -> 24
~ sub_16768 -> sub_16898 : 852 -> 1004
~ sub_16d48 -> sub_16f10 : 484 -> 520
~ sub_183bc -> sub_185a8 : 96 -> 104
~ sub_1a694 -> sub_1a888 : 732 -> 932
~ _IOCircularDataQueueReset : 152 -> 156
~ _IOCircularDataQueueEnqueueCopy : 456 -> 508
~ _IOCircularDataQueueCursorAccess : 312 -> 336
CStrings:
+ "Input.NormalizedThumbstickMaxzoneRadius"
+ "[%#010llx] Input report %#0.2x payload [%#0.2x] (%zu bytes) has invalid checksum '%#0.8x'; expected '%#0.8x'."
+ "[%#010llx] Input report %#0.2x payload has length (%zu bytes), which is less than the minimum expected length (%zu bytes). Ignoring."

```

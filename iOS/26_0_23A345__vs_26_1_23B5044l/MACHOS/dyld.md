## dyld

> `/usr/lib/dyld`

```diff

-1323.3.0.0.0
+1331.0.0.0.0
   __TEXT.__text: 0x8af68
-  __TEXT.__const: 0x2300
-  __TEXT.__cstring: 0xfe73
+  __TEXT.__const: 0x2340
+  __TEXT.__cstring: 0xfe42
   __TEXT.__unwind_info: 0x4f8
   __DATA_CONST.__auth_ptr: 0x90
   __DATA_CONST.__const: 0x6e40

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0x71
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 211A824B-618C-3DAF-A790-499FCAC0D702
-  Functions: 2887
-  Symbols:   4000
-  CStrings:  1984
+  UUID: FE4142CE-36B3-3428-862A-87E25EF9766C
+  Functions: 2886
+  Symbols:   3999
+  CStrings:  1982
 
Symbols:
+ __Block_byref_object_copy_.19
+ __Block_byref_object_copy_.294
+ __Block_byref_object_copy_.63
+ __Block_byref_object_dispose_.20
+ __Block_byref_object_dispose_.295
+ __Block_byref_object_dispose_.64
+ __block_descriptor_tmp.102
+ __block_descriptor_tmp.271
+ __block_descriptor_tmp.276
+ __block_descriptor_tmp.278
+ __block_descriptor_tmp.281
+ __block_descriptor_tmp.288
+ __block_descriptor_tmp.290
+ __block_descriptor_tmp.292
+ __block_descriptor_tmp.296
+ __block_descriptor_tmp.299
+ __block_descriptor_tmp.302
+ __block_descriptor_tmp.305
+ __block_descriptor_tmp.308
+ __block_descriptor_tmp.58
+ __block_descriptor_tmp.93
- __Block_byref_object_copy_.21
- __Block_byref_object_copy_.295
- __Block_byref_object_copy_.65
- __Block_byref_object_dispose_.22
- __Block_byref_object_dispose_.296
- __Block_byref_object_dispose_.66
- ___ZNK6mach_o6Header19platformAndVersionsEv_block_invoke.cold.1
- __block_descriptor_tmp.121
- __block_descriptor_tmp.127
- __block_descriptor_tmp.272
- __block_descriptor_tmp.277
- __block_descriptor_tmp.280
- __block_descriptor_tmp.282
- __block_descriptor_tmp.289
- __block_descriptor_tmp.291
- __block_descriptor_tmp.294
- __block_descriptor_tmp.298
- __block_descriptor_tmp.300
- __block_descriptor_tmp.303
- __block_descriptor_tmp.306
- __block_descriptor_tmp.310
Functions:
~ ____ZNK6mach_o6Header19platformAndVersionsEv_block_invoke : 100 -> 88
~ __ZN5dyld412RuntimeState16setObjCNotifiersENS_16ReadOnlyCallbackIPFvPKcPK11mach_headerEEENS1_IPFvS6_PvS6_PKvEEENS1_IPFvPK29_dyld_objc_notify_mapped_infoEEENS1_IPFvjSI_U13block_pointerFvjEEEE : 1148 -> 1160
- ___ZNK6mach_o6Header19platformAndVersionsEv_block_invoke.cold.1
~ _dyld_parse_boot_arg_int : 424 -> 436
~ __ZNK5dyld416ReadOnlyCallbackIPFvjPK29_dyld_objc_notify_mapped_infoU13block_pointerFvjEEEclIJRjRS3_RS5_EEEvDpOT_ : 560 -> 592
CStrings:
+ "1331"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Sep 16 20:22:53 PDT 2025; root:libignition-58~17977/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Sep 16 20:22:53 PDT 2025; root:libignition-58~17977/libignition_core/RELEASE_ARM64E"
- "1323.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Aug 26 20:17:33 PDT 2025; root:libignition-58~15009/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Aug 26 20:17:33 PDT 2025; root:libignition-58~15009/libignition_core/RELEASE_ARM64E"
- "err.noError()"
- "platformAndVersions_block_invoke"

```

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
-  Symbols:   7290
-  CStrings:  1984
+  UUID: FE4142CE-36B3-3428-862A-87E25EF9766C
+  Functions: 2886
+  Symbols:   7288
+  CStrings:  1982
 
Symbols:
+ ___Block_byref_object_copy_.19
+ ___Block_byref_object_copy_.294
+ ___Block_byref_object_copy_.63
+ ___Block_byref_object_dispose_.20
+ ___Block_byref_object_dispose_.295
+ ___Block_byref_object_dispose_.64
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.271
+ ___block_descriptor_tmp.276
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.281
+ ___block_descriptor_tmp.288
+ ___block_descriptor_tmp.290
+ ___block_descriptor_tmp.292
+ ___block_descriptor_tmp.296
+ ___block_descriptor_tmp.299
+ ___block_descriptor_tmp.302
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.308
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.93
- ___Block_byref_object_copy_.21
- ___Block_byref_object_copy_.295
- ___Block_byref_object_copy_.65
- ___Block_byref_object_dispose_.22
- ___Block_byref_object_dispose_.296
- ___Block_byref_object_dispose_.66
- ____ZNK6mach_o6Header19platformAndVersionsEv_block_invoke.cold.1
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.272
- ___block_descriptor_tmp.277
- ___block_descriptor_tmp.280
- ___block_descriptor_tmp.282
- ___block_descriptor_tmp.289
- ___block_descriptor_tmp.291
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.298
- ___block_descriptor_tmp.300
- ___block_descriptor_tmp.303
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.310
Functions:
~ ____ZNK6mach_o6Header19platformAndVersionsEv_block_invoke : 100 -> 88
~ __ZN5dyld412RuntimeState16setObjCNotifiersENS_16ReadOnlyCallbackIPFvPKcPK11mach_headerEEENS1_IPFvS6_PvS6_PKvEEENS1_IPFvPK29_dyld_objc_notify_mapped_infoEEENS1_IPFvjSI_U13block_pointerFvjEEEE : 1148 -> 1160
- ____ZNK6mach_o6Header19platformAndVersionsEv_block_invoke.cold.1
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

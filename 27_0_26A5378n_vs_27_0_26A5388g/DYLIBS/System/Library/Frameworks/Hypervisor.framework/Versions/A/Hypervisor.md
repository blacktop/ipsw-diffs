## Hypervisor

> `/System/Library/Frameworks/Hypervisor.framework/Versions/A/Hypervisor`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

-306.0.1.0.0
-  __TEXT.__text: 0x84a9c
+308.0.0.0.0
+  __TEXT.__text: 0x8675c
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x557b
-  __TEXT.__gcc_except_tab: 0x2dfc
-  __TEXT.__cstring: 0x286e
-  __TEXT.__oslogstring: 0x9b
+  __TEXT.__const: 0x559b
+  __TEXT.__gcc_except_tab: 0x2e40
+  __TEXT.__cstring: 0x28a1
+  __TEXT.__oslogstring: 0x1b1
   __TEXT.__unwind_info: 0x1c10
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__const: 0x42c0
   __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__weak_auth_got: 0x40
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH.__objc_data: 0x190
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2478
-  Symbols:   3234
-  CStrings:  672
+  Functions: 2482
+  Symbols:   3240
+  CStrings:  682
 
Symbols:
+ GCC_except_table1911
+ GCC_except_table1937
+ GCC_except_table1940
+ GCC_except_table1951
+ GCC_except_table1962
+ GCC_except_table1966
+ GCC_except_table1970
+ GCC_except_table235
+ GCC_except_table240
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table265
+ GCC_except_table271
+ GCC_except_table278
+ GCC_except_table284
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table294
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table307
+ GCC_except_table315
+ GCC_except_table317
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table327
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table356
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table369
+ GCC_except_table374
+ GCC_except_table376
+ GCC_except_table378
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table396
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table55
+ GCC_except_table60
+ __ZN2Hv4Vcpu22crash_on_vcpu_kick_hvcEv
+ __ZN4Base19is_internal_variantEv
+ __ZNK2Hv2Vm24get_vcpu_affinity_levelsEj
+ __ZNK6HvCore10Hypervisor12VcpuTopology34get_affinity_levels_from_cpu_indexEy
+ __ZNSt3__110lock_guardIN4Base9Threading5MutexEED1B9fqe220106Ev
+ _os_parse_boot_arg_string
+ _os_variant_has_internal_content
- GCC_except_table1910
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table1950
- GCC_except_table1961
- GCC_except_table1964
- GCC_except_table1969
- GCC_except_table236
- GCC_except_table241
- GCC_except_table243
- GCC_except_table248
- GCC_except_table250
- GCC_except_table252
- GCC_except_table254
- GCC_except_table261
- GCC_except_table269
- GCC_except_table276
- GCC_except_table283
- GCC_except_table285
- GCC_except_table289
- GCC_except_table291
- GCC_except_table293
- GCC_except_table295
- GCC_except_table297
- GCC_except_table299
- GCC_except_table314
- GCC_except_table316
- GCC_except_table320
- GCC_except_table323
- GCC_except_table325
- GCC_except_table329
- GCC_except_table333
- GCC_except_table338
- GCC_except_table340
- GCC_except_table342
- GCC_except_table346
- GCC_except_table357
- GCC_except_table363
- GCC_except_table365
- GCC_except_table370
- GCC_except_table375
- GCC_except_table377
- GCC_except_table379
- GCC_except_table390
- GCC_except_table393
- GCC_except_table395
- GCC_except_table398
- GCC_except_table403
- GCC_except_table407
- GCC_except_table410
- GCC_except_table54
- GCC_except_table56
- __ZN3Arm8Emulator16check_mdcr_trapsENS_7MdcrEl2E
CStrings:
+ "  vcpu[%u]: expected_mpidr=0x%llx ro.vmpidr=0x%llx rw.vmpidr=0x%llx"
+ "  vcpu[%u]: expected_mpidr=<unset> ro.vmpidr=0x%llx rw.vmpidr=0x%llx"
+ "  vcpu[%u]: is actively being destroyed"
+ "AMAIR2_EL12"
+ "MAIR2_EL12"
+ "PFAR_EL12"
+ "SCTLR2_EL12"
+ "TCR2_EL12"
+ "[VCPU-KICK-FAIL] declined by host kernel: caller_cpu=%u target_phys_id=0x%llx. Dumping vcpus state: "
+ "com.apple.virtualization"
+ "vcpu_kick_hvc failed!"
+ "vz_disable_bear_traps"
- "HCR_EL2.TGE is not supported."
- "Trap to EL2 when HCR_EL2.TGE is supported."
```

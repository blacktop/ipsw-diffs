## com.apple.driver.AppleMobileDispH19P-DCP

> `com.apple.driver.AppleMobileDispH19P-DCP`

```diff

-700.50.104.1.0
+700.50.108.0.0
   __TEXT.__const: 0x1920
-  __TEXT.__cstring: 0x74d5
-  __TEXT_EXEC.__text: 0x25c08
+  __TEXT.__cstring: 0x78cd
+  __TEXT_EXEC.__text: 0x26218
   __TEXT_EXEC.__auth_stubs: 0xe60
   __DATA.__data: 0x2e0
   __DATA.__common: 0x100
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x50e8
+  __DATA_CONST.__const: 0x5100
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0xf0
   __DATA_CONST.__auth_got: 0x730
   __DATA_CONST.__got: 0xd0
-  Functions: 1480
+  Functions: 1484
   Symbols:   0
-  CStrings:  603
+  CStrings:  615
 
Functions:
+ sub_fffffe0009299b88
+ sub_fffffe000929c7b4
+ sub_fffffe00092a32c8
~ __ZN23IOMobileFramebufferShim10swap_startEPjP12IOUserClient : 360 -> 448
~ __ZN23IOMobileFramebufferShim29set_config_requires_dual_pipeEv : 224 -> 284
~ __ZN23IOMobileFramebufferShim20set_digital_out_modeEjj : 7216 -> 8500
+ sub_fffffe00092bb744
CStrings:
+ "%s: Dual pipe: fb %u issuing secondary modeset on fb %u (timing %u color %u)\n"
+ "%s: Dual pipe: fb %u primary VFTG link check done in %u ms, localStatus %u\n"
+ "%s: Dual pipe: fb %u primary modeset thread finished in %u ms, status 0x%x\n"
+ "%s: Dual pipe: fb %u waiting for primary VFTG link check, timeout %u ms\n"
+ "%s: Dual pipe: fb %u waiting for primary modeset thread, timeout %u ms\n"
+ "%s: Skipping redundant modeset (timing=%u, color=%u)\n"
+ "%s: modeset: fb %u is_dual=%d adm_forced=%d vftg_cfg=%d paired=%d hpd_dual_ok=%d timing=%u color=%u (%ux%u@%uHz)\n"
+ "%s: modeset: fb %u set_digital_out_mode returning 0x%x (timing %u color %u dual %d)\n"
+ "AED: fb %u could not read ADM pipe-count intent (0x%x); modesetting as single pipe\n"
+ "Dual pipe: fb %u issuing secondary modeset on fb %u (timing %u color %u)\n"
+ "Dual pipe: fb %u primary VFTG link check done in %u ms, localStatus %u\n"
+ "Dual pipe: fb %u primary modeset thread finished in %u ms, status 0x%x\n"
+ "Dual pipe: fb %u waiting for primary VFTG link check, timeout %u ms\n"
+ "Dual pipe: fb %u waiting for primary modeset thread, timeout %u ms\n"
+ "Skipping redundant modeset (timing=%u, color=%u)\n"
+ "dual pipe: rejected swap_start on secondary fb %u (client %p)"
+ "modeset: fb %u is_dual=%d adm_forced=%d vftg_cfg=%d paired=%d hpd_dual_ok=%d timing=%u color=%u (%ux%u@%uHz)\n"
+ "modeset: fb %u set_digital_out_mode returning 0x%x (timing %u color %u dual %d)\n"
- "%s: AED: Skipping spurious modeset (timing=%u, color=%u, is_dual=%d unchanged, intent toggled %d->%d)\n"
- "%s: Merge Config: Primary VFTG enable time %dms\n"
- "%s: Primary modeset time %dms\n"
- "AED: Skipping spurious modeset (timing=%u, color=%u, is_dual=%d unchanged, intent toggled %d->%d)\n"
- "Merge Config: Primary VFTG enable time %dms\n"
- "Primary modeset time %dms\n"
```

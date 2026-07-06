## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

```diff

-  __TEXT.__cstring: 0x102c8
+  __TEXT.__cstring: 0x10469
   __TEXT.__const: 0x740
-  __TEXT_EXEC.__text: 0x5bea0
+  __TEXT_EXEC.__text: 0x5c590
   __TEXT_EXEC.__auth_stubs: 0xdf0
   __DATA.__data: 0x46c
   __DATA.__common: 0x578
   __DATA.__bss: 0x10
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xe3d8
+  __DATA_CONST.__const: 0xe448
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x690
   __DATA_CONST.__auth_got: 0x6f8
   __DATA_CONST.__got: 0x188
-  Functions: 3578
+  Functions: 3588
   Symbols:   0
-  CStrings:  1749
+  CStrings:  1760
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "%s::%d:fCompletionLoops: %d\n"
+ "%s::%d:nvme: CORE_DEBUG_EXPORT_STATS failed with status 0x%x\n"
+ "%s::%d:nvme: ParseSanitizeCounters: maxElements < elements\n"
+ "%s::%d:nvme: Sanitize counter keyNum: %u value: 0x%016llx\n"
+ "SanitizeDone"
+ "SanitizeFailed"
+ "SanitizeStart"
+ "nvme-completion-loops"
+ "sanitize-counters"
+ "virtual IOReturn AppleANS2NVMeController::GetSanitizeCounters()"
+ "virtual bool IONVMeController::InitializeController()"
+ "virtual void AppleANS2NVMeController::ParseSanitizeCounters(uint8_t *)"
- "( inNumDwords <= NVMeFieldMax ( kNVMeGetLogPageNumDwordsLen ) )"

```

## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.80.3.0.0
-  __TEXT.__cstring: 0x25fe
+1360.100.4.0.0
+  __TEXT.__cstring: 0x27fc
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xca98
+  __TEXT_EXEC.__text: 0xbf20
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0
   __DATA.__bss: 0x130
-  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 0E07E9C9-56F8-308C-9505-7AFE807DF518
-  Functions: 156
+  UUID: 882C7F61-E717-30A9-8F41-6ABF8E8DB3DF
+  Functions: 167
   Symbols:   0
-  CStrings:  353
+  CStrings:  356
 
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:10:27 Feb  5 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:10:27 Feb  5 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:10:27 Feb  5 2026\n"
+ "%s::start: %s _pmuNub: %p built 21:10:27 Feb  5 2026\n"
+ "/Library/Caches/com.apple.xbs/41E15A5C-6C9A-441B-9FBB-82EE3AF1CF24/TemporaryDirectory.EhPcDg/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
+ "SOCD: Attempted to read past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %u\n"
+ "SOCD: Container goes past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %llu\n"
+ "SOCD: Container goes past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %u\n"
+ "SOCD: Container size too small. Size: %llu, header size: %u\n"
+ "SOCD: Container size too small. Size: %u, header size: %u\n"
+ "SOCD: Failed to read container data at 0x%x: 0x%x\n"
+ "SOCD: Failed to read/invalidate container header at 0x%x: 0x%x\n"
+ "SOCD: Failed to read/invalidate container mutexes at 0x%x: 0x%x\n"
+ "SOCD: Found valid container of size %llu at 0x%x\n"
+ "SOCD: Found valid container of size %u at 0x%x\n"
+ "SOCD: Found valid magic at 0x%x\n"
+ "SOCD: Total duration %llu ns\n"
- "\"AppleDialogPMU::%s failed to alloc %d bytes\" @%s:%d"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:48:02 Jan 26 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:48:02 Jan 26 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:48:03 Jan 26 2026\n"
- "%s::start: %s _pmuNub: %p built 20:48:03 Jan 26 2026\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
- "SOCD"
- "SOCD: Failed to read socd container\n"
- "SOCD: Failed to reset magic\n"
- "SOCD: Magic value %02Xh %02Xh %02Xh %02Xh\n"
- "SOCD: PMU %llu ns, TOTAL %llu ns (%u, %u)\n"
- "SOCD: failed to read magic value\n"
- "SOCD: failed to read trigger counters\n"
- "_handleSOCD"

```

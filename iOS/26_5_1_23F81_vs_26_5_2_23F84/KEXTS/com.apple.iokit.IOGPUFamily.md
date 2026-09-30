## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-  __TEXT.__cstring: 0x5e27
-  __TEXT.__os_log: 0x4bbf
+  __TEXT.__cstring: 0x5e6c
+  __TEXT.__os_log: 0x4c09
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x3f9b4
+  __TEXT_EXEC.__text: 0x3fbbc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x898

   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0xa0
-  Functions: 1982
+  Functions: 1987
   Symbols:   0
-  CStrings:  878
+  CStrings:  882
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__assert : content changed
CStrings:
+ "%s: resource does not own its backing (resType=0x%x child=%u device_cache=%s)\n"
+ "%s: resource does not own its backing (resType=0x%x)\n"
+ "IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const"
+ "IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)"
+ "IOReturn IOGPUSysMemory::replace_backing_ranges_locked(task_t, IOAddressRange *, uint32_t, bool)"
+ "NO"
+ "YES"
- "Attempting to detach memory for invalid resource type: %u\n"
- "virtual IOReturn IOGPUSysMemory::replace_backing_bytes(task_t, mach_vm_address_t, uint64_t)"
- "virtual IOReturn IOGPUSysMemory::replace_backing_ranges(task_t, IOAddressRange *, uint32_t, bool)"

```

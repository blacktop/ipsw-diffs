## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-  __TEXT.__cstring: 0x616e
-  __TEXT.__os_log: 0x521d
+  __TEXT.__cstring: 0x61b3
+  __TEXT.__os_log: 0x5267
   __TEXT.__const: 0x8c
-  __TEXT_EXEC.__text: 0x421a0
+  __TEXT_EXEC.__text: 0x424b8
   __TEXT_EXEC.__auth_stubs: 0xdc0
   __DATA.__data: 0x460
   __DATA.__common: 0x898

   __DATA_CONST.__auth_got: 0x6e0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1997
+  Functions: 2001
   Symbols:   0
-  CStrings:  916
+  CStrings:  920
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
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

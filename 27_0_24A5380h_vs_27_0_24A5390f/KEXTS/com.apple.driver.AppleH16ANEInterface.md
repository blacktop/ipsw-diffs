## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-10.15.4.0.0
-  __TEXT.__const: 0x1030
-  __TEXT.__cstring: 0x11588
-  __TEXT.__os_log: 0x3ac29
-  __TEXT_EXEC.__text: 0x1476a8
-  __TEXT_EXEC.__auth_stubs: 0x1250
+10.16.2.0.0
+  __TEXT.__const: 0x1020
+  __TEXT.__cstring: 0x1158a
+  __TEXT.__os_log: 0x3ace0
+  __TEXT_EXEC.__text: 0x149aa4
+  __TEXT_EXEC.__auth_stubs: 0x1270
   __DATA.__data: 0x482c
-  __DATA.__common: 0x7b0
+  __DATA.__common: 0x7b8
   __DATA.__bss: 0x818
   __DATA_CONST.__mod_init_func: 0x2f0
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0xf950
+  __DATA_CONST.__const: 0xf990
   __DATA_CONST.__kalloc_type: 0x6c80
   __DATA_CONST.__kalloc_var: 0x8890
-  __DATA_CONST.__auth_got: 0x928
+  __DATA_CONST.__auth_got: 0x938
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 4916
+  Functions: 4921
   Symbols:   0
-  CStrings:  5201
+  CStrings:  5203
 
CStrings:
+ "%s: %s:   surface=%p uuid=0x%llx mode=%u\n"
+ "%s: %s: Client program size : %llu maxMapSize: %llu minMapSize %llu\n"
+ "%s: %s: Disabling acc power rail (refcount 1 -> 0)\n"
+ "%s: %s: Enabling acc power rail (refcount 0 -> 1)\n"
+ "%s: %s: evaluateLocalFence: trylock failed for dep 0x%llx, request 0x%llx — falling back to LocalStrict\n"
+ "/.resolve/2%.*s"
+ "[ERROR] %s: %s: Ignoring stale firmware ack for un-sent command at ANE address 0x%llx (sentToFW=false)\n"
- "%s: %s:   surface=%p uuid=0x%llx\n"
- "%s: %s: Client program size : %llu maxMapSize: %u minMapSize %u\n"
- "/.resolve/2%s"
- "[ERROR] %s: %s: Failed to allocate anecMutableWeightFileData for %u entries\n"
- "[ERROR] %s: %s: Failed to allocate symbol storage for %u entries\n"
```

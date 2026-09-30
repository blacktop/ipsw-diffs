## com.apple.driver.AppleMSG

> `com.apple.driver.AppleMSG`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__got`

```diff

-420.0.0.0.0
+420.0.1.0.0
   __TEXT.__const: 0x362
-  __TEXT.__os_log: 0x11b24
-  __TEXT.__cstring: 0x6880
-  __TEXT_EXEC.__text: 0x39d04
-  __TEXT_EXEC.__auth_stubs: 0x770
+  __TEXT.__os_log: 0x11b64
+  __TEXT.__cstring: 0x694f
+  __TEXT_EXEC.__text: 0x39e6c
+  __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0xd0
   __DATA.__common: 0x250
   __DATA.__bss: 0x5f0
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x44b8
-  __DATA_CONST.__kalloc_type: 0x400
-  __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__const: 0x44d8
+  __DATA_CONST.__kalloc_type: 0x480
+  __DATA_CONST.__kalloc_var: 0x5a0
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0xb0
-  Functions: 1765
+  Functions: 1772
   Symbols:   0
-  CStrings:  1003
+  CStrings:  1013
 
CStrings:
+ "1"
+ "21:20:48"
+ "Jul 14 2026"
+ "clock-gates"
+ "responseStruct != nullptr"
+ "site.IOLogicalAddress"
+ "site.IOMemoryMap *"
+ "site.MSGDebugStateCommandResponse"
+ "site.struct msg_lut_entry_t"
+ "site.struct reg_updates"
+ "site.struct sync_config_t"
+ "site.uint32_t"
- "21:00:09"
- "Jun 30 2026"
```

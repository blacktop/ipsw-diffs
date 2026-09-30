## com.apple.driver.ApplePPMCPMS

> `com.apple.driver.ApplePPMCPMS`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1191.0.16.0.0
+1191.0.27.0.0
   __TEXT.__const: 0x1150
-  __TEXT.__cstring: 0xf84a
-  __TEXT.__os_log: 0x3e3d
-  __TEXT_EXEC.__text: 0x52f7c
+  __TEXT.__cstring: 0xf888
+  __TEXT.__os_log: 0x3eb3
+  __TEXT_EXEC.__text: 0x5326c
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x164
   __DATA.__common: 0x500
   __DATA.__bss: 0x1c8
   __DATA_CONST.__mod_init_func: 0xe0
   __DATA_CONST.__mod_term_func: 0xb0
-  __DATA_CONST.__const: 0x5af0
+  __DATA_CONST.__const: 0x5b00
   __DATA_CONST.__kalloc_type: 0x900
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2168
+  Functions: 2170
   Symbols:   0
-  CStrings:  1855
+  CStrings:  1858
 
CStrings:
+ "%s::%s:Error: PPMInterfaceAPICallBack failed with 0x%08x\n\n"
+ "ApplePPMInterfaceAPIFunction"
+ "SystemCapability%s_Battery%d"
+ "virtual IOReturn ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)"
- "virtual void ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)"
```

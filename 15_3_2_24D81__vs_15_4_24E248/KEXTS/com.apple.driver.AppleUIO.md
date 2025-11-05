## com.apple.driver.AppleUIO

> `com.apple.driver.AppleUIO`

```diff

-69.60.20.0.0
-  __TEXT.__cstring: 0x948
+106.0.0.0.0
+  __TEXT.__cstring: 0x9cd
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0x2b84
+  __TEXT_EXEC.__text: 0x2ccc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
-  __DATA.__common: 0x100
+  __DATA.__data: 0x168
+  __DATA.__common: 0x108
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2dd0
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 19FE8594-2702-3A0F-AEB7-3A60EF01694B
-  Functions: 121
-  Symbols:   544
-  CStrings:  77
+  UUID: 34DDD5D8-82CF-3E6B-9405-DD2697553B0A
+  Functions: 123
+  Symbols:   554
+  CStrings:  86
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ __ZN11AppleUIOMem16memorySizeSysctlEP10sysctl_oidPviP10sysctl_req
+ _sysctl__kern_children
+ _sysctl__kern_uio
+ _sysctl__kern_uio_children
+ _sysctl__kern_uio_mem_size
+ _sysctl_handle_int
+ _sysctl_register_oid
+ _sysctl_unregister_oid
CStrings:
+ "21:17:19"
+ "IU"
+ "Mar 19 2025"
+ "N"
+ "UIO memory size"
+ "UIO sysctl"
+ "UIO: %-30s IOBMD::withOptions(size=%u) failed\n"
+ "UIO: %-30s UIO Memory being used\n"
+ "UIO: %-30s failed to get new sysctl value, err %d\n"
+ "mem_size"
+ "memorySizeSysctl"
+ "uio"
- "20:39:44"
- "Jan  2 2025"
- "UIO: %-30s IOBufferMemoryDescriptor::withOptions(%d) failed\n"

```

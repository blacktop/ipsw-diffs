## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-128.3.0.0.0
-  __TEXT.__cstring: 0x5d6e
-  __TEXT.__os_log: 0x48f2
+129.2.2.0.0
+  __TEXT.__cstring: 0x5dd0
+  __TEXT.__os_log: 0x4a9d
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x42ecc
+  __TEXT_EXEC.__text: 0x431b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x898

   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0xa0
-  UUID: A45C3053-42ED-3D64-BB79-C9F585059E79
-  Functions: 1970
+  UUID: A2DB7C96-FB7A-367A-9FA3-0820E9E40FEB
+  Functions: 1971
   Symbols:   0
-  CStrings:  863
+  CStrings:  874
 
CStrings:
+ "%s: Invalid virtual_page_size(%u)\n"
+ "%s: Out of bounds access to residency data\n"
+ "%s: Overflow adding metadata length to byte count\n"
+ "%s: Overflow adding residency data length to byte count\n"
+ "%s: Overflow aligning metadata length\n"
+ "%s: Overflow aligning residency data length\n"
+ "%s: Overflow aligning virtual length\n"
+ "%s: Residency data length(%llu) less than required minimum size(%llu)\n"
+ "%s: virtual_page_size(%u) is not a power of 2\n"
+ "iogpu_force_mapped_memory"
+ "virtual void IOGPUVirtualMemory::updateResidencyData(uint32_t, uint8_t)"

```

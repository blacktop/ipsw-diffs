## com.apple.driver.AppleCentauriManager

> `com.apple.driver.AppleCentauriManager`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__got`

```diff

-124.0.0.0.1
-  __TEXT.__cstring: 0x5c00
+127.0.0.0.0
+  __TEXT.__cstring: 0x5cb1
   __TEXT.__const: 0x180
-  __TEXT_EXEC.__text: 0x1ac24
-  __TEXT_EXEC.__auth_stubs: 0x6d0
+  __TEXT_EXEC.__text: 0x1ace8
+  __TEXT_EXEC.__auth_stubs: 0x6e0
   __DATA.__data: 0x188
   __DATA.__common: 0xf0
   __DATA.__bss: 0x50

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1980
   __DATA_CONST.__kalloc_type: 0x1c0
-  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0xf8
   Functions: 641
   Symbols:   0
-  CStrings:  729
+  CStrings:  733
 
Functions:
~ __ZN20AppleCentauriManager10portEnableEbbb : 1704 -> 1824
~ sub_fffffe0008a51d00 -> _OUTLINED_FUNCTION_96 : 20 -> 12
~ _OUTLINED_FUNCTION_96 -> sub_fffffe0008a62054 : 12 -> 20
~ __ZN20AppleCentauriManager20collectStateSnapshotEP9IOServicePP6OSData : 3720 -> 3796
CStrings:
+ "%s::%s: DLLLA link-up detected, link status: 0x%04x \n"
+ "%s::%s: DLLLA link-up timeout after 100ms, link status: 0x%04x \n"
+ "%s::%s: Looking for DLLLA link-up \n"
+ "%s::%s: PCIe Express capability not found on root port (capHeader = 0x%08x) \n"
+ "AppleCentauri-127"
+ "Version: %s\n"
- "%s::%s: Secondary Vendor ID Device ID: 0x%08x \n"
- "%s::%s: SecondarySpaceBusNum: 0x%02x \n"
```

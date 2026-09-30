## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 314.120.5.0.0
-  __TEXT.__text: 0x9880
+  __TEXT.__text: 0x98dc
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0x1040
   __TEXT.__objc_methlist: 0x14
Functions:
~ ___RMEIsAutoSubmitEnabled_block_invoke : 56 -> 60
~ _RMEGetDefaultLargeExemptedProcesses : 104 -> 152
~ _RMEPopulateDefaultPrefs : 1664 -> 1704
```

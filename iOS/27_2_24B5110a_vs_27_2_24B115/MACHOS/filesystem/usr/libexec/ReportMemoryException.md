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

 369.40.1.0.0
-  __TEXT.__text: 0x916c
+  __TEXT.__text: 0x91c8
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_stubs: 0x1000
   __TEXT.__objc_methlist: 0x2c
Functions:
~ ___RMEIsAutoSubmitEnabled_block_invoke : 56 -> 60
~ _RMEGetDefaultLargeExemptedProcesses : 88 -> 136
~ _RMEPopulateDefaultPrefs : 1564 -> 1604
```

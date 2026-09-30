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

-365.0.0.0.0
-  __TEXT.__text: 0x9844
+369.0.0.0.0
+  __TEXT.__text: 0x97f8
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0xf60
   __TEXT.__objc_methlist: 0x2c
Functions:
~ _RMEPopulateDefaultPrefs : 1800 -> 1728
~ ___RMEIsAutoSubmitEnabled_block_invoke : 60 -> 56
```

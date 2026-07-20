## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-877.0.3.0.0
+877.0.6.0.0
   __TEXT.__cstring: 0x10469
   __TEXT.__const: 0x740
-  __TEXT_EXEC.__text: 0x5c590
+  __TEXT_EXEC.__text: 0x5c5dc
   __TEXT_EXEC.__auth_stubs: 0xdf0
   __DATA.__data: 0x46c
   __DATA.__common: 0x578
Functions:
~ __ZN23AppleANS2NVMeController20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 624 -> 636
~ __ZN23AppleANS2NVMeController17PPMArrivalHandlerEPvP9IOServiceP10IONotifier : 420 -> 484
```

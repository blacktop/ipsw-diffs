## com.apple.iokit.IODisplayPortFamily

> `com.apple.iokit.IODisplayPortFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-775.0.2.0.0
-  __TEXT.__cstring: 0x87e0
-  __TEXT.__os_log: 0x9fc4
+775.0.3.0.0
+  __TEXT.__cstring: 0x87b7
+  __TEXT.__os_log: 0x9f68
   __TEXT.__const: 0x440
-  __TEXT_EXEC.__text: 0x5b9c8
+  __TEXT_EXEC.__text: 0x5b648
   __TEXT_EXEC.__auth_stubs: 0xaf0
   __DATA.__data: 0xc8
   __DATA.__common: 0x5d8

   __DATA_CONST.__got: 0x170
   Functions: 2623
   Symbols:   0
-  CStrings:  1628
+  CStrings:  1625
 
Functions:
~ __ZN21IODPServiceUserClient12_retrainLinkEPS_PvP25IOExternalMethodArguments -> sub_fffffe0009fee374 : 912 -> 16
CStrings:
- "Attempting to retrain link\n"
- "IOAV[%d] %s<0x%llx>::%s: Attempting to retrain link\n"
- "_retrainLink"
```

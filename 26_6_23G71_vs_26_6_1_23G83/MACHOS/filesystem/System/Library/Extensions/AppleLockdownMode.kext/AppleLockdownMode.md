## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

 80.120.2.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x4892
-  __TEXT_EXEC.__text: 0x15000
+  __TEXT.__cstring: 0x48db
+  __TEXT_EXEC.__text: 0x150e0
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__kalloc_var: 0x14a0
   Functions: 211
   Symbols:   516
-  CStrings:  494
+  CStrings:  497
 
Functions:
~ _DeserializeCredential : 1380 -> 1384
~ _LibSer_SEPControl_Deserialize : 352 -> 492
~ _LibSer_SEPControlResponse_Deserialize : 208 -> 288
CStrings:
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
```

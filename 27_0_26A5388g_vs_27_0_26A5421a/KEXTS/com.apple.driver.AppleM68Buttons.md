## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

```diff

 132.0.0.0.0
-  __TEXT.__cstring: 0x4f9a
+  __TEXT.__cstring: 0x4fe3
   __TEXT.__const: 0x208
   __TEXT.__os_log: 0x61f
-  __TEXT_EXEC.__text: 0x1db74
+  __TEXT_EXEC.__text: 0x1dc58
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0xca
   __DATA.__common: 0x88

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 327
   Symbols:   952
-  CStrings:  629
+  CStrings:  632
 
Functions:
~ _DeserializeCredential : 1520 -> 1524
~ _LibSer_SEPControl_Deserialize : 364 -> 508
~ _LibSer_SEPControlResponse_Deserialize : 216 -> 296
CStrings:
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
```

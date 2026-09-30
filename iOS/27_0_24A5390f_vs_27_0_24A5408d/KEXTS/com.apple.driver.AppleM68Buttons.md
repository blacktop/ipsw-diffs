## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

```diff

 132.0.0.0.0
-  __TEXT.__cstring: 0x4eb6
+  __TEXT.__cstring: 0x4eff
   __TEXT.__const: 0x208
   __TEXT.__os_log: 0x61f
-  __TEXT_EXEC.__text: 0x1d0d0
+  __TEXT_EXEC.__text: 0x1d1b0
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0xca
   __DATA.__common: 0x88

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 328
   Symbols:   0
-  CStrings:  629
+  CStrings:  632
 
Functions:
~ _DeserializeCredential : 1440 -> 1444
~ _LibSer_SEPControl_Deserialize : 356 -> 496
~ _LibSer_SEPControlResponse_Deserialize : 208 -> 288
CStrings:
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
```

## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

-128.0.5.0.0
+128.0.8.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x48cf
-  __TEXT_EXEC.__text: 0x150a0
+  __TEXT.__cstring: 0x4918
+  __TEXT_EXEC.__text: 0x15180
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 211
   Symbols:   0
-  CStrings:  495
+  CStrings:  498
 
Functions:
~ _DeserializeCredential : 1440 -> 1444
~ _LibSer_SEPControl_Deserialize : 356 -> 496
~ _LibSer_SEPControlResponse_Deserialize : 208 -> 288
CStrings:
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
```

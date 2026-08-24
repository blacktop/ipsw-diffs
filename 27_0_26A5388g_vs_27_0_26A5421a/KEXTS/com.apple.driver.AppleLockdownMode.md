## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

-128.0.5.0.0
+128.0.8.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x49b3
-  __TEXT_EXEC.__text: 0x15620
+  __TEXT.__cstring: 0x49fc
+  __TEXT_EXEC.__text: 0x15704
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 211
   Symbols:   619
-  CStrings:  495
+  CStrings:  498
 
Functions:
~ _DeserializeCredential : 1520 -> 1524
~ _LibSer_SEPControl_Deserialize : 364 -> 508
~ _LibSer_SEPControlResponse_Deserialize : 216 -> 296
CStrings:
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
```

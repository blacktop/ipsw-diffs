## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

 80.120.2.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x4976
-  __TEXT_EXEC.__text: 0x15010
+  __TEXT.__cstring: 0x49bf
+  __TEXT_EXEC.__text: 0x150f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__kalloc_var: 0x14a0
   Functions: 211
   Symbols:   619
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

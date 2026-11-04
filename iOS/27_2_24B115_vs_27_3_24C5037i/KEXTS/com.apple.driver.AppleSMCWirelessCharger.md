## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-155.40.5.0.0
+155.60.4.0.0
   __TEXT.__const: 0x8c
-  __TEXT.__cstring: 0x3850
+  __TEXT.__cstring: 0x38a0
   __TEXT.__os_log: 0x5f0
-  __TEXT_EXEC.__text: 0x10d18
+  __TEXT_EXEC.__text: 0x10e6c
   __TEXT_EXEC.__auth_stubs: 0x5e0
   __DATA.__data: 0xcd
   __DATA.__common: 0x90

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 212
   Symbols:   0
-  CStrings:  470
+  CStrings:  472
 
Functions:
~ sub_fffffe00096af5c0 -> sub_fffffe00097783c0 : 5484 -> 5620
~ sub_fffffe00096bed70 -> sub_fffffe0009787bf8 : 1992 -> 2192
~ sub_fffffe00096bf538 -> sub_fffffe0009788488 : 112 -> 116
CStrings:
+ "%s: Failed to set WAEQ to %d (ret=%d)\n"
+ "chg-disable-inductive-fw-reload-on-crash"
```

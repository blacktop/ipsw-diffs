## com.apple.driver.AppleMesaSEPDriver

> `com.apple.driver.AppleMesaSEPDriver`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-10321.40.6.0.0
-  __TEXT.__const: 0x128
+10321.40.10.0.0
+  __TEXT.__const: 0x134
   __TEXT.__cstring: 0x5e4d
   __TEXT.__os_log: 0x2ea1
-  __TEXT_EXEC.__text: 0x28438
+  __TEXT_EXEC.__text: 0x28580
   __TEXT_EXEC.__auth_stubs: 0x6b0
   __DATA.__data: 0xc4
   __DATA.__common: 0x150
Functions:
~ __ZN18AppleMesaSEPDriver19asyncCaptureHandlerEP18IOTimerEventSource : 5008 -> 5192
~ __ZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbh : 4868 -> 5012
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: Mesa-10321.40.10~12, %s file: %s, line: %d\n"
- "AssertMacros: %s (value = 0x%lx), version: Mesa-10321.40.6~149, %s file: %s, line: %d\n"
```

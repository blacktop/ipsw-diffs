## com.apple.iokit.IOVideoFamily

> `com.apple.iokit.IOVideoFamily`

```diff

-5633.0.0.0.0
+5634.0.0.0.0
   __TEXT.__cstring: 0x230
-  __TEXT_EXEC.__text: 0x45e4
-  __TEXT_EXEC.__auth_stubs: 0x190
+  __TEXT_EXEC.__text: 0x45c8
+  __TEXT_EXEC.__auth_stubs: 0x180
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2de0
   __DATA_CONST.__kalloc_type: 0x100
-  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x70
   Functions: 264
-  Symbols:   707
+  Symbols:   706
   CStrings:  35
 
Symbols:
+ _IOFreeData
+ _IOMallocZeroData
- _IOFreeAligned
- _IOMallocAligned
- _bzero
Functions:
~ __ZN13IOVideoDevice4freeEv : 120 -> 152
~ __ZN13IOVideoDevice24registerNotificationPortEP8ipc_portjj : 232 -> 184
~ __ZN13IOVideoDevice21sendMultiNotificationEjPK25IOVideoDeviceNotification : 300 -> 288
```

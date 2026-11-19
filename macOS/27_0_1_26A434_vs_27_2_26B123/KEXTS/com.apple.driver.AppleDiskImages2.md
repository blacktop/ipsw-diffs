## com.apple.driver.AppleDiskImages2

> `com.apple.driver.AppleDiskImages2`

```diff

-598.0.1.0.0
-  __TEXT.__cstring: 0x3a53
-  __TEXT.__os_log: 0x2480
+598.40.4.0.0
+  __TEXT.__cstring: 0x3ad4
+  __TEXT.__os_log: 0x2522
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x127a0
+  __TEXT_EXEC.__text: 0x1285c
   __TEXT_EXEC.__auth_stubs: 0x5b0
   __DATA.__data: 0x4e8
   __DATA.__common: 0x148

   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xa0
   Functions: 401
-  Symbols:   1160
-  CStrings:  397
+  Symbols:   1162
+  CStrings:  400
 
Symbols:
+ __ZZN19DIDeviceRequestPool25AllocateBuffersForRequestEP15DIDeviceRequestmbPFbPvES2_E11_os_log_fmt
+ __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_8
Functions:
~ __ZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardEbP19IOStorageAttributesb : 800 -> 792
~ __ZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequest : 588 -> 580
~ __ZN20AppleDiskImageDevice23requestGracefulShutdownEb : 1168 -> 1280
~ __ZN19DIDeviceRequestPool25AllocateBuffersForRequestEP15DIDeviceRequestmbPFbPvES2_ : 748 -> 840
CStrings:
+ "598.40.4"
+ "IOReturn DIDeviceRequestPool::AllocateBuffersForRequest(DIDeviceRequest *, size_t, bool, abort_request_allocation_fn_t, void *)"
+ "[%d (ctx)] %s::%d: Requested %zu buffers - does not fit the request buffer count\n"
+ "[%d] %s::%d: Flush did not complete - ejecting device instead of going dormant\n"
- "598.0.1"
```

## com.apple.driver.AppleDiskImages2

> `com.apple.driver.AppleDiskImages2`

```diff

-598.40.3.0.0
-  __TEXT.__cstring: 0x3996
-  __TEXT.__os_log: 0x2480
+598.40.4.0.0
+  __TEXT.__cstring: 0x3a16
+  __TEXT.__os_log: 0x2522
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x11d84
+  __TEXT_EXEC.__text: 0x11e2c
   __TEXT_EXEC.__auth_stubs: 0x5b0
   __DATA.__data: 0x4e8
   __DATA.__common: 0x148

   __DATA_CONST.__got: 0xa0
   Functions: 400
   Symbols:   0
-  CStrings:  397
+  CStrings:  400
 
Functions:
~ __ZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardEbP19IOStorageAttributesb : 756 -> 748
~ __ZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequest : 580 -> 572
~ __ZN20AppleDiskImageDevice23requestGracefulShutdownEb : 1152 -> 1244
~ __ZN19DIDeviceRequestPool25AllocateBuffersForRequestEP15DIDeviceRequestmbPFbPvES2_ : 748 -> 840
CStrings:
+ "598.40.4"
+ "IOReturn DIDeviceRequestPool::AllocateBuffersForRequest(DIDeviceRequest *, size_t, bool, abort_request_allocation_fn_t, void *)"
+ "[%d (ctx)] %s::%d: Requested %zu buffers - does not fit the request buffer count\n"
+ "[%d] %s::%d: Flush did not complete - ejecting device instead of going dormant\n"
- "598.40.3"
```

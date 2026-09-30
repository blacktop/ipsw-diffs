## com.apple.driver.AppleDiskImages2

> `com.apple.driver.AppleDiskImages2`

```diff

-379.60.1.0.0
-  __TEXT.__cstring: 0x2163
-  __TEXT.__os_log: 0x11a2
-  __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0xd698
+385.101.1.0.0
+  __TEXT.__cstring: 0x2221
+  __TEXT.__os_log: 0x11d7
+  __TEXT.__const: 0x90
+  __TEXT_EXEC.__text: 0xdb9c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x498
-  __DATA.__common: 0x118
+  __DATA.__data: 0x4e8
+  __DATA.__common: 0x120
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0xa0

   __DATA_CONST.__const: 0x2ef8
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: E9FCF138-3197-3511-9CB8-93CD92A9AEF3
-  Functions: 293
-  Symbols:   928
-  CStrings:  277
+  UUID: 87B60C7A-7829-3CC2-8CAC-BCD9EEF3CD5D
+  Functions: 296
+  Symbols:   993
+  CStrings:  281
 
Symbols:
+ _ZN19DIDeviceRequestPool12AbortRequestEj.cold.1
+ _ZN19DIDeviceRequestPool12AbortRequestEj.cold.2
+ _ZN19DIDeviceRequestPool12AbortRequestEj.cold.3
+ _ZN19DIDeviceRequestPool12AbortRequestEj.cold.4
+ _ZN19DIDeviceRequestPool14ReleaseBuffersEv.cold.1
+ _ZN19DIDeviceRequestPool15ReleaseRequestsEv.cold.1
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.1
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.2
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.3
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.4
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.1
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.2
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.3
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.4
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.5
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.6
+ _ZN19DIDeviceRequestPool17GetPendingRequestEj.cold.7
+ _ZN19DIDeviceRequestPool20MarkRequestAsPendingEP15DIDeviceRequest.cold.1
+ _ZN19DIDeviceRequestPool20MarkRequestAsPendingEP15DIDeviceRequest.cold.2
+ _ZN19DIDeviceRequestPool20MarkRequestAsPendingEP15DIDeviceRequest.cold.3
+ _ZN19DIDeviceRequestPool20MarkRequestAsPendingEP15DIDeviceRequest.cold.4
+ _ZN19DIDeviceRequestPool6CreateEmymjPFmPviES0_.cold.1
+ _ZN20AppleDiskImageDevice11ClearDeviceEv.cold.1
+ _ZN20AppleDiskImageDevice13doSynchronizeEyyj.cold.1
+ _ZN20AppleDiskImageDevice19AddOwnerCredentialsEv.cold.1
+ _ZN20AppleDiskImageDevice19AddOwnerCredentialsEv.cold.2
+ _ZN20AppleDiskImageDevice20initWriteSeqCountersEv.cold.1
+ _ZN20AppleDiskImageDevice9DIOThreadEv.cold.1
+ _ZN20DIDeviceIOUserClient20findNotificationPortEj.cold.1
+ _ZN20DIDeviceIOUserClient20findNotificationPortEj.cold.2
+ _ZN20DIDeviceIOUserClient20findNotificationPortEj.cold.3
+ _ZN20DIDeviceIOUserClient20findNotificationPortEj.cold.4
+ _ZN20DIDeviceIOUserClient20findNotificationPortEj.cold.5
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.1
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.2
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.3
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.4
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.5
+ _ZN20DIDeviceIOUserClient24registerNotificationPortEP8ipc_portjj.cold.6
+ _ZN20DIDeviceIOUserClient4freeEv.cold.1
+ _ZN20DIDeviceIOUserClient4freeEv.cold.2
+ _ZN20DIDeviceIOUserClient4freeEv.cold.3
+ _ZN20DIDeviceIOUserClient4freeEv.cold.4
+ _ZN25AppleDiskImagesController12CreateDeviceEP20DICreateDeviceParamsP19DICreateDeviceReplyR11OSSharedPtrI20AppleDiskImageDeviceE.cold.1
+ _ZN25AppleDiskImagesController12CreateDeviceEP20DICreateDeviceParamsP19DICreateDeviceReplyR11OSSharedPtrI20AppleDiskImageDeviceE.cold.2
+ _ZN28DIRequestPoolPendingIterator11initRequestEv.cold.1
+ _ZN28DIRequestPoolPendingIterator11initRequestEv.cold.2
+ _ZN28DIRequestPoolPendingIterator11initRequestEv.cold.3
+ _ZN28DIRequestPoolPendingIterator11initRequestEv.cold.4
+ _ZN28DIRequestPoolPendingIterator11initRequestEv.cold.5
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.1
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.2
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.3
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.4
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.5
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.6
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.7
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.8
+ _ZNK20AppleDiskImageDevice13getSeqCounterEyb.cold.9
+ _ZNK20AppleDiskImageDevice16getSeqCounterIdxEy.cold.1
+ __ZN20AppleDiskImageDevice19prepareUnmapCommandEP15DIDeviceRequestP26IOBlockStorageDeviceExtentb
+ __ZN20AppleDiskImageDevice22AddStorageFeaturesDictEbb
+ __ZN20AppleDiskImageDevice38PrepareMappedBuffersMightFaultForUnmapEP15DIDeviceRequestP26IOBlockStorageDeviceExtent
+ __ZZN20AppleDiskImageDevice22AddStorageFeaturesDictEbbE11_os_log_fmt
+ __ZZN6DIRefTI14DISharedBufferE3dieEvE20kalloc_type_view_108
+ __ZZN6DIRefTI14DISharedBufferEnwEmE20kalloc_type_view_114
+ __ZZN6DIRefTI15DIDeviceRequestE3dieEvE20kalloc_type_view_108
+ __ZZN6DIRefTI15DIDeviceRequestEnwEmE20kalloc_type_view_114
+ _g_thread_mapped_buf_unmaps
+ _sysctl__debug_didevice_thread_mapped_buf_unmaps
- __ZN20AppleDiskImageDevice22AddStorageFeaturesDictEb
- __ZZN6DIRefTI14DISharedBufferE3dieEvE20kalloc_type_view_107
- __ZZN6DIRefTI14DISharedBufferEnwEmE20kalloc_type_view_113
- __ZZN6DIRefTI15DIDeviceRequestE3dieEvE20kalloc_type_view_107
- __ZZN6DIRefTI15DIDeviceRequestEnwEmE20kalloc_type_view_113
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp"
+ "385.101.1"
+ "[%d] %s::%d: Storage features: unmap=%d, barrier=%d\n"
+ "bool AppleDiskImageDevice::AddStorageFeaturesDict(bool, bool)"
+ "didevice count of page faulted buffers that initiated read/write requests"
+ "didevice count of page faulted buffers that initiated unmap requests"
+ "didevice_thread_mapped_buf_unmaps"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp"
- "379.60.1"
- "didevice count of mapped buffers writes by thread"

```

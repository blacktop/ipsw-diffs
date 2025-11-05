## com.apple.driver.AppleTrustedAccessory

> `com.apple.driver.AppleTrustedAccessory`

```diff

-145.60.1.0.0
+147.100.3.0.0
   __TEXT.__const: 0x238
   __TEXT.__cstring: 0x3d96
   __TEXT.__os_log: 0x37ef
-  __TEXT_EXEC.__text: 0x22c98
+  __TEXT_EXEC.__text: 0x22f28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1e0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x4210
   __DATA_CONST.__kalloc_type: 0x400
-  UUID: 119ED944-D869-3B4F-92F0-CF3CFF8B643C
-  Functions: 401
-  Symbols:   1243
+  UUID: B1784723-DDCF-3E27-B7F6-4E91723E38E8
+  Functions: 400
+  Symbols:   1253
   CStrings:  664
 
Symbols:
+ _ZN21AppleTrustedAccessory12transferDataE18TADataTransferTypePKvm.cold.1
+ _ZN21AppleTrustedAccessory12transferDataE18TADataTransferTypePKvm.cold.2
+ _ZN21AppleTrustedAccessory12transferDataE18TADataTransferTypePKvm.cold.3
+ _ZN21AppleTrustedAccessory9getReportEP18IOMemoryDescriptor15IOHIDReportTypejjU13block_pointerFviE.cold.1
+ _ZN21AppleTrustedAccessory9setReportEP18IOMemoryDescriptor15IOHIDReportTypejjU13block_pointerFviE.cold.1
+ _ZN28AppleTrustedAccessoryManager14performCommandEPK8ta_cmd_tPKvmP18IOMemoryDescriptorPj.cold.1
+ _ZN28AppleTrustedAccessoryManager14performCommandEPK8ta_cmd_tPKvmP18IOMemoryDescriptorPj.cold.2
+ _ZN28AppleTrustedAccessoryManager14performCommandEPK8ta_cmd_tPKvmP18IOMemoryDescriptorPj.cold.3
+ _ZN28AppleTrustedAccessoryManager14performCommandEPK8ta_cmd_tPKvmP18IOMemoryDescriptorPj.cold.4
+ _ZN28AppleTrustedAccessoryManager14performCommandEPK8ta_cmd_tPKvmP18IOMemoryDescriptorPj.cold.5
+ _ZN28AppleTrustedAccessoryManager21accessoryEventHandlerEP18IOTimerEventSource.cold.1
+ _ZN28AppleTrustedAccessoryManager22scheduleAccessoryEventEP16TAAccessoryEventb.cold.1
+ _ZN28AppleTrustedAccessoryManager40analyticsAttachCoreAnalyticsServiceGatedEP9IOService.cold.1
+ _ZN28AppleTrustedAccessoryManager6cancelEP9IOService18atam_status_code_t.cold.1
+ _ZN30AppleTrustedAccessoryAnalytics13taUIDToStringEPKh.cold.1
+ _ZN30AppleTrustedAccessoryAnalytics22logAnalyticsDictionaryEPK8OSStringPK12OSDictionary.cold.1
+ _ZN30AppleTrustedAccessoryAnalytics22logAnalyticsDictionaryEPK8OSStringPK12OSDictionary.cold.2
+ _ZN38AppleTrustedAccessoryManagerUserClient5startEP9IOService.cold.1
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.1
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.2
+ _ZNK7libkern17bounded_array_refIcN9os_detail21panic_trapping_policyEE5sliceEmm.cold.3
- _ZN28AppleTrustedAccessoryManager13pairAccessoryEPKhPKvm.cold.1
- _ZN28AppleTrustedAccessoryManager13pairAccessoryEPKhPKvm.cold.2
- _ZN28AppleTrustedAccessoryManager13pairAccessoryEPKhPKvm.cold.3
- _ZN28AppleTrustedAccessoryManager13pairAccessoryEPKhPKvm.cold.4
- _ZN28AppleTrustedAccessoryManager17startSecureIntentEP9IOServicePK41cmd_start_secure_intent_operation_in_v1_t.cold.1
- _ZN28AppleTrustedAccessoryManager18authorizeAccessoryEjPKhPKvmS3_m.cold.1
- _ZN28AppleTrustedAccessoryManager18authorizeAccessoryEjPKhPKvmS3_m.cold.2
- _ZN28AppleTrustedAccessoryManager18authorizeAccessoryEjPKhPKvmS3_m.cold.3
- _ZN28AppleTrustedAccessoryManager25cacheDirectAttestationKeyEb.cold.1
- _ZN28AppleTrustedAccessoryManager26sendAccessoryManifestToSEPEP21AppleTrustedAccessoryb.cold.1
- _ZN28AppleTrustedAccessoryManager26sendAccessoryManifestToSEPEP21AppleTrustedAccessoryb.cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessory.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessoryManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/TrustedAccessoryAnalytics/AppleTrustedAccessoryAnalytics.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessory.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/AppleTrustedAccessory/AppleTrustedAccessoryManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/TrustedAccessory_Kernel/TrustedAccessoryAnalytics/AppleTrustedAccessoryAnalytics.cpp"

```

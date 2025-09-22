## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-13.0.39.0.0
+13.1.4.0.0
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0xeac
   __TEXT.__os_log: 0x1b00
-  __TEXT_EXEC.__text: 0x1ac60
+  __TEXT_EXEC.__text: 0x1ad60
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x240

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4d30
   __DATA_CONST.__kalloc_type: 0x7c0
-  UUID: 36C15852-76EB-3E9F-8E96-E6BC46F3CAAF
+  UUID: ECE52263-9E28-325B-A1F1-8BFA35B28810
   Functions: 614
   Symbols:   829
   CStrings:  276
Symbols:
+ __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_544
+ __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_686
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_569
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_604
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_711
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_745
- __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_524
- __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_666
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_549
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_584
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_691
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_725
Functions:
~ __ZN13IOHIDGCDevice22_providerMaybeUnseizedEv : 152 -> 196
~ __ZN13IOHIDGCDevice16_tryOpenProviderEjy : 632 -> 676
~ __ZN13IOHIDGCDevice27_openProviderThreadCallbackEPv : 16 -> 100
~ __ZN13IOHIDGCDevice13closeProviderEv : 452 -> 496
~ __ZN13IOHIDGCDevice24openProviderInBackgroundEv : 216 -> 256

```

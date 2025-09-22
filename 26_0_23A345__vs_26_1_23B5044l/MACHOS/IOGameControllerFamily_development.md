## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.0.39.0.0
+13.1.4.0.0
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0x21c6
   __TEXT.__os_log: 0x845c
-  __TEXT_EXEC.__text: 0x2bc7c
+  __TEXT_EXEC.__text: 0x2bd80
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5558
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: DDC23DE7-C953-3876-9A31-63E4A17E6EA0
+  UUID: D19B4DCF-DFDA-3DB7-94FD-5A0EE80A93DD
   Functions: 889
   Symbols:   1993
   CStrings:  577
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
~ __ZN13IOHIDGCDevice16_tryOpenProviderEjy : 716 -> 760
~ __ZN13IOHIDGCDevice27_openProviderThreadCallbackEPv : 16 -> 100
~ __ZN13IOHIDGCDevice24openProviderInBackgroundEv : 244 -> 288
~ __ZN13IOHIDGCDevice13closeProviderEv : 532 -> 576

```

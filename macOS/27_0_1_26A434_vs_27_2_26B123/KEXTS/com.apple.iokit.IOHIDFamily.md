## com.apple.iokit.IOHIDFamily

> `com.apple.iokit.IOHIDFamily`

```diff

-2360.1.2.0.0
-  __TEXT.__cstring: 0x4d79
+2360.40.13.0.1
+  __TEXT.__cstring: 0x4d84
   __TEXT.__os_log: 0x4930
   __TEXT.__const: 0x1d90
-  __TEXT_EXEC.__text: 0xa5288
+  __TEXT_EXEC.__text: 0xa53c0
   __TEXT_EXEC.__auth_stubs: 0xd50
   __DATA.__data: 0xbea
   __DATA.__common: 0xe88

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 3858
   Symbols:   5374
-  CStrings:  1237
+  CStrings:  1238
 
Symbols:
+ __ZZN19IOHIDElementPrivate14setCalibrationEjjjjjjiE21kalloc_type_view_2081
- __ZZN19IOHIDElementPrivate14setCalibrationEjjjjjjiE21kalloc_type_view_2076
Functions:
~ _HIDGetCaps : 612 -> 636
~ _HIDGetCapabilities : 612 -> 636
~ _HIDGetCollectionNodes : 236 -> 260
~ _HIDGetCollectionExtendedNodes : 248 -> 272
~ __ZN17IOHIDEventService17publishPropertiesEv : 448 -> 460
~ _OUTLINED_FUNCTION_6 : 16 -> 20
~ _OUTLINED_FUNCTION_7 -> _OUTLINED_FUNCTION_9 : 20 -> 16
~ _HIDGetNextUsageValueInfo : 432 -> 472
~ _HIDGetNextButtonInfo : 432 -> 472
~ __ZN14IOHIDInterface22SendDebugBuffer_InvokeE5IORPCP15OSMetaClassBasePFiS2_P18IOMemoryDescriptorE : 228 -> 232
~ __ZN14IOHIDInterface23GetElementValues_InvokeE5IORPCP15OSMetaClassBasePFiS2_jP18IOMemoryDescriptorE : 232 -> 236
~ __ZN14IOHIDInterface23SetElementValues_InvokeE5IORPCP15OSMetaClassBasePFiS2_jP18IOMemoryDescriptorE : 232 -> 236
~ __ZN14IOHIDInterface26GetSupportedCookies_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP24IOBufferMemoryDescriptorE : 180 -> 184
~ __ZN14IOHIDInterface22AddReportToPool_InvokeE5IORPCP15OSMetaClassBasePFiS2_P24IOBufferMemoryDescriptorE : 228 -> 232
~ __ZN14IOHIDInterface11Open_InvokeE5IORPCP15OSMetaClassBasePFiS2_P9IOServicejP8OSActionE : 276 -> 280
~ __ZN14IOHIDInterface12Close_InvokeE5IORPCP15OSMetaClassBasePFiS2_P9IOServicejE : 232 -> 236
~ __ZN14IOHIDInterface16SetReport_InvokeE5IORPCP15OSMetaClassBasePFiS2_P18IOMemoryDescriptor15IOHIDReportTypejjE : 236 -> 240
~ __ZN14IOHIDInterface16GetReport_InvokeE5IORPCP15OSMetaClassBasePFiS2_P18IOMemoryDescriptor15IOHIDReportTypejjE : 236 -> 240
~ __ZN14IOHIDInterface22ReportAvailable_InvokeE5IORPCP15OSMetaClassBasePFvS2_yjj15IOHIDReportTypeP18IOMemoryDescriptorP8OSActionEPK11OSMetaClass : 260 -> 264
~ __ZN11IOHIDDevice13_Start_InvokeE5IORPCP15OSMetaClassBasePFiS2_P9IOServiceE : 228 -> 232
~ __ZN11IOHIDDevice21CompleteReport_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionijEPK11OSMetaClass : 196 -> 200
~ __ZN11IOHIDDevice21_ProcessReport_InvokeE5IORPCP15OSMetaClassBasePFvS2_20HIDReportCommandTypeP18IOMemoryDescriptor15IOHIDReportTypejjP8OSActionE : 244 -> 248
~ __ZN11IOHIDDevice20_HandleReport_InvokeE5IORPCP15OSMetaClassBasePFiS2_yP18IOMemoryDescriptorj15IOHIDReportTypejE : 240 -> 244
~ __ZN11IOHIDDevice19_SetProperty_InvokeE5IORPCP15OSMetaClassBasePFvS2_P24IOBufferMemoryDescriptorE : 184 -> 188
~ __ZN17IOHIDEventService9_DispatchEPS_5IORPC : 1600 -> 1548
~ __ZN17IOHIDEventService22_CompleteSetLED_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActioniyE : 192 -> 196
~ __ZN17IOHIDEventService19SetLEDAction_InvokeE5IORPCP15OSMetaClassBasePFvS2_jjbyP8OSActionEPK11OSMetaClass : 208 -> 212
~ __ZN17IOHIDEventService29_CompleteSetProperties_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActioniyE : 192 -> 196
~ __ZN17IOHIDEventService24SetUserProperties_InvokeE5IORPCP15OSMetaClassBasePFvS2_P12OSDictionaryyP8OSActionEPK11OSMetaClass : 240 -> 244
~ __ZN17IOHIDEventService25_CompleteCopyEvent_InvokeE5IORPCP15OSMetaClassBasePFvS2_P8OSActionP24IOBufferMemoryDescriptoryE : 240 -> 244
~ __ZN17IOHIDEventService16CopyEvent_InvokeE5IORPCP15OSMetaClassBasePFvS2_P12OSDictionaryyP8OSActionEPK11OSMetaClass : 240 -> 244
~ __ZN17IOHIDEventService13_Start_InvokeE5IORPCP15OSMetaClassBasePFiS2_P9IOServiceE : 228 -> 232
~ __ZN17IOHIDEventService21EventAvailable_InvokeE5IORPCP15OSMetaClassBasePFiS2_jE : 164 -> 168
~ __ZN17IOHIDEventService21SetEventMemory_InvokeE5IORPCP15OSMetaClassBasePFiS2_P24IOBufferMemoryDescriptorE : 228 -> 232
~ __ZN17IOHIDEventService40_DispatchRelativeScrollWheelEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_yiiijbE : 184 -> 188
~ __ZN17IOHIDEventService36_DispatchAbsolutePointerEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_yiijjbE : 184 -> 188
~ __ZN17IOHIDEventService36_DispatchRelativePointerEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_yiijjbE : 184 -> 188
~ __ZN17IOHIDEventService29_DispatchKeyboardEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_yjjjjbE : 184 -> 188
~ __ZN17IOHIDEventService13SetLED_InvokeE5IORPCP15OSMetaClassBasePFvS2_jbE : 144 -> 148
~ __ZN17IOHIDEventService18SetLEDState_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjbE : 176 -> 180
~ __ZN17IOHIDEventService30handleCopyMatchingEvent_InvokeE5IORPCP15OSMetaClassBasePFiS2_P12OSDictionaryPP10IOHIDEventE : 252 -> 256
~ __ZN19IOHIDElementPrivate12enqueueValueEP18_IOHIDElementValue : 432 -> 464
~ __ZN16IOHIDEventDriver39createDigitizerTransducerEventForReportEP19DigitizerTransduceryj : 4212 -> 4232
CStrings:
+ "TCCService"
```

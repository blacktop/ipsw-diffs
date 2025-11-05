## IOUSBLib

> `/System/Library/Extensions/IOUSBHostFamily.kext/Contents/PlugIns/IOUSBLib.bundle/Contents/MacOS/IOUSBLib`

```diff

-1402.60.3.0.0
-  __TEXT.__text: 0x8788
+1402.100.21.0.0
+  __TEXT.__text: 0x89a8
   __TEXT.__auth_stubs: 0x410
   __TEXT.__cstring: 0x26b
-  __TEXT.__const: 0x74
+  __TEXT.__const: 0x7c
   __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__unwind_info: 0x1d8
   __DATA_CONST.__auth_got: 0x210

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D6452948-353A-3303-B737-53689E4A323F
+  UUID: 9F8E92C8-69D6-379C-AA76-705BCCC5CA8A
   Functions: 275
   Symbols:   367
   CStrings:  60
Functions:
~ __ZN13IOUSBIUnknown13factoryAddRefEv : 164 -> 152
~ __ZN13IOUSBIUnknown14factoryReleaseEv : 168 -> 156
~ __ZN13IOUSBIUnknown24_versionNumberFromStringEPK10__CFString : 560 -> 548
~ __ZN16IOUSBDeviceClass5startEPK14__CFDictionaryj : 1960 -> 1968
~ __ZN16IOUSBDeviceClass21CacheConfigDescriptorEv : 376 -> 388
~ __ZN16IOUSBDeviceClass4stopEv : 72 -> 80
~ __ZN16IOUSBDeviceClass14GetDeviceClassEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass17GetDeviceSubClassEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass17GetDeviceProtocolEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass15GetDeviceVendorEPt : 40 -> 44
~ __ZN16IOUSBDeviceClass16GetDeviceProductEPt : 40 -> 44
~ __ZN16IOUSBDeviceClass22GetDeviceReleaseNumberEPt : 40 -> 44
~ __ZN16IOUSBDeviceClass16GetDeviceAddressEPt : 40 -> 44
~ __ZN16IOUSBDeviceClass26GetDeviceBusPowerAvailableEPj : 40 -> 44
~ __ZN16IOUSBDeviceClass14GetDeviceSpeedEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass25GetNumberOfConfigurationsEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass13GetLocationIDEPj : 40 -> 44
~ __ZN16IOUSBDeviceClass35USBDeviceGetManufacturerStringIndexEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass30USBDeviceGetProductStringIndexEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass35USBDeviceGetSerialNumberStringIndexEPh : 40 -> 44
~ __ZN16IOUSBDeviceClass29GetConfigurationDescriptorPtrEhPP28IOUSBConfigurationDescriptor : 132 -> 144
~ __ZN16IOUSBDeviceClass16SetConfigurationEh : 188 -> 196
~ __ZN16IOUSBDeviceClass18SetConfigurationV2Ehbb : 188 -> 196
~ __ZN16IOUSBDeviceClass16GetConfigurationEPh : 192 -> 196
~ __ZN16IOUSBDeviceClass21CreateDeviceAsyncPortEPj : 304 -> 312
~ __ZN16IOUSBDeviceClass13USBDeviceOpenEb : 456 -> 460
~ __ZN16IOUSBDeviceClass14USBDeviceCloseEv : 128 -> 136
~ __ZN16IOUSBDeviceClass11ResetDeviceEv : 124 -> 132
~ __ZN16IOUSBDeviceClass20USBDeviceReEnumerateEj : 272 -> 276
~ __ZN16IOUSBDeviceClass16USBDeviceSuspendEb : 184 -> 192
~ __ZN16IOUSBDeviceClass22USBDeviceAbortPipeZeroEv : 124 -> 132
~ __ZN16IOUSBDeviceClass23GetUSBDeviceInformationEPj : 192 -> 196
~ __ZN16IOUSBDeviceClass17RequestExtraPowerEjjPj : 204 -> 208
~ __ZN16IOUSBDeviceClass16ReturnExtraPowerEjj : 172 -> 176
~ __ZN16IOUSBDeviceClass22GetExtraPowerAllocatedEjPj : 196 -> 200
~ __ZN16IOUSBDeviceClass30GetBandwidthAvailableForDeviceEPj : 76 -> 80
~ __ZN16IOUSBDeviceClass23RegisterForNotificationEyPFvPviS0_S0_ES0_Py : 44 -> 52
~ __ZN16IOUSBDeviceClass22UnregisterNotificationEy : 44 -> 52
~ __ZN16IOUSBDeviceClass23AcknowledgeNotificationEy : 44 -> 52
~ __ZN16IOUSBDeviceClass13DeviceRequestEP17IOUSBDevRequestTO : 372 -> 376
~ __ZN16IOUSBDeviceClass18DeviceRequestAsyncEP17IOUSBDevRequestTOPFvPviS2_ES2_ : 352 -> 356
~ __ZN16IOUSBDeviceClass23CreateInterfaceIteratorEP25IOUSBFindInterfaceRequestPj : 220 -> 224
~ __ZN16IOUSBDeviceClass17GetBusFrameNumberEPyP12UnsignedWide : 168 -> 172
~ __ZN16IOUSBDeviceClass22GetBusMicroFrameNumberEPyP12UnsignedWide : 168 -> 172
~ __ZN16IOUSBDeviceClass25GetBusFrameNumberWithTimeEPyP12UnsignedWide : 168 -> 172
~ __ZN19IOUSBInterfaceClass5startEPK14__CFDictionaryj : 1028 -> 1036
~ __ZN19IOUSBInterfaceClass4stopEv : 72 -> 80
~ __ZN19IOUSBInterfaceClass17GetInterfaceClassEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass20GetInterfaceSubClassEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass20GetInterfaceProtocolEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass23GetInterfaceStringIndexEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass15GetDeviceVendorEPt : 40 -> 44
~ __ZN19IOUSBInterfaceClass16GetDeviceProductEPt : 40 -> 44
~ __ZN19IOUSBInterfaceClass22GetDeviceReleaseNumberEPt : 40 -> 44
~ __ZN19IOUSBInterfaceClass21GetConfigurationValueEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass18GetInterfaceNumberEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass19GetAlternateSettingEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass15GetNumEndpointsEPh : 40 -> 44
~ __ZN19IOUSBInterfaceClass13GetLocationIDEPj : 40 -> 44
~ __ZN19IOUSBInterfaceClass9GetDeviceEPj : 40 -> 44
~ __ZN19IOUSBInterfaceClass24CreateInterfaceAsyncPortEPj : 304 -> 312
~ __ZN19IOUSBInterfaceClass16USBInterfaceOpenEb : 388 -> 392
~ __ZN19IOUSBInterfaceClass17USBInterfaceCloseEv : 336 -> 324
~ __ZN19IOUSBInterfaceClass14RegisterDriverEv : 108 -> 112
~ __ZN19IOUSBInterfaceClass21SetAlternateInterfaceEh : 196 -> 204
~ __ZN19IOUSBInterfaceClass22GetBusMicroFrameNumberEPyP12UnsignedWide : 168 -> 172
~ __ZN19IOUSBInterfaceClass17GetBusFrameNumberEPyP12UnsignedWide : 168 -> 172
~ __ZN19IOUSBInterfaceClass25GetBusFrameNumberWithTimeEPyP12UnsignedWide : 168 -> 172
~ __ZN19IOUSBInterfaceClass16GetFrameListTimeEPj : 64 -> 68
~ __ZN19IOUSBInterfaceClass21GetBandwidthAvailableEPj : 76 -> 80
~ __ZN19IOUSBInterfaceClass19SetDeviceIdlePolicyEj : 168 -> 172
~ __ZN19IOUSBInterfaceClass17SetPipeIdlePolicyEhj : 172 -> 176
~ __ZN19IOUSBInterfaceClass21GetEndpointPropertiesEhhhPhPtS0_ : 248 -> 252
~ __ZN19IOUSBInterfaceClass23GetEndpointPropertiesV3EP23IOUSBEndpointProperties : 228 -> 232
~ __ZN19IOUSBInterfaceClass14ControlRequestEhP17IOUSBDevRequestTO : 380 -> 384
~ __ZN19IOUSBInterfaceClass19ControlRequestAsyncEhP17IOUSBDevRequestTOPFvPviS2_ES2_ : 356 -> 360
~ __ZN19IOUSBInterfaceClass8ReadPipeEhPvPjjj : 252 -> 260
~ __ZN19IOUSBInterfaceClass13ReadPipeAsyncEhPvjjjPFvS0_iS0_ES0_ : 276 -> 284
~ __ZN19IOUSBInterfaceClass9WritePipeEhPvjjj : 224 -> 232
~ __ZN19IOUSBInterfaceClass14WritePipeAsyncEhPvjjjPFvS0_iS0_ES0_ : 280 -> 288
~ __ZN19IOUSBInterfaceClass17GetPipePropertiesEhPhS0_S0_PtS0_ : 288 -> 296
~ __ZN19IOUSBInterfaceClass19GetPipePropertiesV2EhPhS0_S0_PtS0_S0_S0_S1_ : 352 -> 360
~ __ZN19IOUSBInterfaceClass19GetPipePropertiesV3EhP23IOUSBEndpointProperties : 216 -> 220
~ __ZN19IOUSBInterfaceClass13GetPipeStatusEh : 184 -> 192
~ __ZN19IOUSBInterfaceClass9AbortPipeEh : 184 -> 192
~ __ZN19IOUSBInterfaceClass14ClearPipeStallEhb : 188 -> 196
~ __ZN19IOUSBInterfaceClass13SetPipePolicyEhth : 196 -> 204
~ __ZN19IOUSBInterfaceClass15SupportsStreamsEhPj : 204 -> 208
~ __ZN19IOUSBInterfaceClass13CreateStreamsEhj : 188 -> 196
~ __ZN19IOUSBInterfaceClass20GetConfiguredStreamsEhPj : 220 -> 228
~ __ZN19IOUSBInterfaceClass17ReadStreamsPipeTOEhjPvPjjj : 252 -> 260
~ __ZN19IOUSBInterfaceClass18WriteStreamsPipeTOEhjPvjjj : 220 -> 228
~ __ZN19IOUSBInterfaceClass22ReadStreamsPipeAsyncTOEhjPvjjjPFvS0_iS0_ES0_ : 268 -> 276
~ __ZN19IOUSBInterfaceClass23WriteStreamsPipeAsyncTOEhjPvjjjPFvS0_iS0_ES0_ : 272 -> 280
~ __ZN19IOUSBInterfaceClass16AbortStreamsPipeEhj : 188 -> 196
~ __ZN19IOUSBInterfaceClass23RegisterForNotificationEyPFvPviS0_S0_ES0_Py : 88 -> 96
~ __ZN19IOUSBInterfaceClass22UnregisterNotificationEy : 44 -> 52
~ __ZN19IOUSBInterfaceClass23AcknowledgeNotificationEy : 44 -> 52
~ __ZN19IOUSBInterfaceClass18ReadIsochPipeAsyncEhPvyjP14IOUSBIsocFramePFvS0_iS0_ES0_ : 304 -> 316
~ __ZN19IOUSBInterfaceClass19WriteIsochPipeAsyncEhPvyjP14IOUSBIsocFramePFvS0_iS0_ES0_ : 308 -> 320
~ __ZN19IOUSBInterfaceClass28LowLatencyReadIsochPipeAsyncEhPvyjjP24IOUSBLowLatencyIsocFramePFvS0_iS0_ES0_ : 308 -> 320
~ __ZN19IOUSBInterfaceClass29LowLatencyWriteIsochPipeAsyncEhPvyjjP24IOUSBLowLatencyIsocFramePFvS0_iS0_ES0_ : 312 -> 324
~ __ZN19IOUSBInterfaceClass22LowLatencyCreateBufferEPPvyj : 516 -> 520
~ __ZN19IOUSBInterfaceClass23LowLatencyDestroyBufferEPv : 324 -> 316
~ __ZN19IOUSBInterfaceClass21CacheConfigDescriptorEv : 448 -> 460

```

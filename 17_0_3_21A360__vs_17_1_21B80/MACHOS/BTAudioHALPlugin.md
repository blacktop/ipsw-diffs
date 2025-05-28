## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-170.50.4.1.5
-  __TEXT.__text: 0x600f8
-  __TEXT.__auth_stubs: 0x10d0
+171.11.1.1.1
+  __TEXT.__text: 0x62514
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0x1260
-  __TEXT.__init_offsets: 0x98
+  __TEXT.__init_offsets: 0x9c
   __TEXT.__objc_methlist: 0x5b0
   __TEXT.__const: 0x151c
   __TEXT.__gcc_except_tab: 0x1618
   __TEXT.__cstring: 0x3796
-  __TEXT.__oslogstring: 0xd37b
+  __TEXT.__oslogstring: 0xe6a6
   __TEXT.__objc_classname: 0xc6
   __TEXT.__objc_methname: 0x20f6
   __TEXT.__objc_methtype: 0x10cd
-  __TEXT.__unwind_info: 0x1798
+  __TEXT.__unwind_info: 0x17c8
   __TEXT.__eh_frame: 0x1dc
-  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__auth_got: 0x888
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3bd0
+  __DATA_CONST.__const: 0x3bf0
   __DATA_CONST.__cfstring: 0xb80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20

   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0xb08
-  __DATA.__bss: 0xaa00
+  __DATA.__bss: 0xaa10
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 2191
-  Symbols:   412
-  CStrings:  1792
+  Functions: 2274
+  Symbols:   414
+  CStrings:  1870
 
Symbols:
+ _log10f
+ _vDSP_svesq
CStrings:
+ "#Error BTAudioXpcConnection::SendAdaptiveVolumeRampEndConfig null args"
+ "#Error BTAudioXpcConnection::SendAdaptiveVolumeRampEndConfig null values[0]"
+ "#Error BTAudioXpcConnection::SendAudioContentTypeMsg null value"
+ "#Error BTAudioXpcConnection::SendAudioDeliveryChangeCompletedMsg null value"
+ "#Error BTAudioXpcConnection::SendCallScreeningState null args"
+ "#Error BTAudioXpcConnection::SendDynamicLatencyAudioAndInputAggregationStatePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendDynamicLatencyAudioAndInputAggregationStatePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendDynamicLatencyFrameCount null args"
+ "#Error BTAudioXpcConnection::SendDynamicLatencyFrameCount null values[0]"
+ "#Error BTAudioXpcConnection::SendExpanseInA2DPChanged null args"
+ "#Error BTAudioXpcConnection::SendExpanseInA2DPChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendExpanseStatePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendExpanseStatePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendGameStatePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendGameStatePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendHFPCodecTypeMsg null msg"
+ "#Error BTAudioXpcConnection::SendHFPCodecTypeMsg null payload"
+ "#Error BTAudioXpcConnection::SendInputVolumePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendInputVolumePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendMsg null msg"
+ "#Error BTAudioXpcConnection::SendMsg null values[0]"
+ "#Error BTAudioXpcConnection::SendMsg null values[1]"
+ "#Error BTAudioXpcConnection::SendSampleRate null args"
+ "#Error BTAudioXpcConnection::SendSampleRate null values[0]"
+ "#Error BTAudioXpcConnection::SendSelectCodecMsg null value"
+ "#Error BTAudioXpcConnection::SendSelectScoDataSourceMsg null msg"
+ "#Error BTAudioXpcConnection::SendSelectScoDataSourceMsg null values[0]"
+ "#Error BTAudioXpcConnection::SendSelectScoDataSourceMsg null values[1]"
+ "#Error BTAudioXpcConnection::SendSelectScoDataSourceMsg null values[2]"
+ "#Error BTAudioXpcConnection::SendSetAllowScoForTBT null args"
+ "#Error BTAudioXpcConnection::SendSetAllowScoForTBT null values[0]"
+ "#Error BTAudioXpcConnection::SendSetDosimetrySensitivity null args"
+ "#Error BTAudioXpcConnection::SendSetDosimetrySensitivity null values[0]"
+ "#Error BTAudioXpcConnection::SendSetDosimetryVolumeCurve null args"
+ "#Error BTAudioXpcConnection::SendSetDosimetryVolumeCurve null values[0]"
+ "#Error BTAudioXpcConnection::SendSetListenMode null args"
+ "#Error BTAudioXpcConnection::SendSetListenMode null values[0]"
+ "#Error BTAudioXpcConnection::SendSetOwnershipState null msg"
+ "#Error BTAudioXpcConnection::SendSetOwnershipState null msgValues[0]"
+ "#Error BTAudioXpcConnection::SendSetOwnershipState null payloadValues[0]"
+ "#Error BTAudioXpcConnection::SendSetOwnershipState null payloadValues[1]"
+ "#Error BTAudioXpcConnection::SendSoftwareVolumeEnabled null args"
+ "#Error BTAudioXpcConnection::SendSoftwareVolumeEnabled null values[0]"
+ "#Error BTAudioXpcConnection::SendSpatialAudioActive null args"
+ "#Error BTAudioXpcConnection::SendSpatialAudioActive null values[0]"
+ "#Error BTAudioXpcConnection::SendSpatialAudioAllowed null args"
+ "#Error BTAudioXpcConnection::SendSpatialAudioAllowed null values[0]"
+ "#Error BTAudioXpcConnection::SendSpatialAudioAppBasedConfig null args"
+ "#Error BTAudioXpcConnection::SendSpatialAudioAppBasedConfig null values[0]"
+ "#Error BTAudioXpcConnection::SendSpatialAudioModeEnabled null args"
+ "#Error BTAudioXpcConnection::SendSpatialAudioModeEnabled null values[0]"
+ "#Error BTAudioXpcConnection::SendStartMsg null args"
+ "#Error BTAudioXpcConnection::SendStartMsg null values[0]"
+ "#Error BTAudioXpcConnection::SendStartMsg null values[1]"
+ "#Error BTAudioXpcConnection::SendVoiceOverStatePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendVoiceOverStatePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendVolumePropertyChanged null args"
+ "#Error BTAudioXpcConnection::SendVolumePropertyChanged null values[0]"
+ "#Error BTAudioXpcConnection::SendWirelessSplitterEnabled null args"
+ "#Error BTAudioXpcConnection::SendWirelessSplitterEnabled null values[0]"
+ "BTAudioDetect invalid decoder config"
+ "BTAudioDetect output invalid buffer addr"
+ "BTAudioDetect output invalid buffer addr for virtual"
+ "BTAudioDetect output invalid decodedBytes"
+ "BTAudioDetect output invalid inBufferFrameSize"
+ "BTAudioDetect output invalid inBufferFrameSize for virtual"
+ "BTAudioDetect output invalid numBytestoDecode"
+ "BTAudioDetect virtual avgPwr %fdB,intv %u/%u,processed %llu,delivered %llu,rate %f"
+ "Creating audio level"
+ "InitializeCommonAccessoryFeatureFromDevice"
+ "Input Decode: Requested %lu bytes, but only read %lu bytes instead. Decoded a total of %lu bytes"
+ "Set VolumeCurve"
+ "Set VolumeCurve with NULL"
+ "Update VolumeCurve"
+ "Update VolumeCurve with NULL"
+ "UpdateAccessoryFeatureFromDevice"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyDosimetryVolumeCurve"
+ "kBTAudioMsgPropertySpatialAudioAppBasedMode get Dict"

```

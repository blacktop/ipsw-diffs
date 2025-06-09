## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

-25.4.0.0.0
-  __TEXT.__text: 0x12e84
+30.45.3.0.0
+  __TEXT.__text: 0x1327c
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x14d4
+  __TEXT.__objc_methlist: 0x150c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4185
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__cstring: 0x4359
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_classname: 0x127
-  __TEXT.__objc_methname: 0x4eb1
-  __TEXT.__objc_methtype: 0x886
-  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__objc_methname: 0x4fa3
+  __TEXT.__objc_methtype: 0x8b5
+  __TEXT.__objc_stubs: 0x2040
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x2950
+  __AUTH_CONST.__objc_const: 0x2988
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B317E53-2E02-347C-8AF5-6B030850EA5D
-  Functions: 530
-  Symbols:   1763
-  CStrings:  1590
+  UUID: A1A5F281-BEE4-3CD4-B022-67D9984753C5
+  Functions: 539
+  Symbols:   1786
+  CStrings:  1607
 
Symbols:
+ -[HMDeviceRecord setSharedRegionStatus:]
+ -[HMDeviceRecord sharedRegionStatus]
+ -[HMServiceClient getHearingModeDeviceRecordForIdentifier:]
+ GCC_except_table21
+ GCC_except_table44
+ GCC_except_table45
+ _OBJC_IVAR_$_HMDeviceRecord._sharedRegionStatus
+ _OUTLINED_FUNCTION_4
+ ___61-[HMServiceClient fetchHearingModeDeviceRecordForIdentifier:]_block_invoke
+ ___61-[HMServiceClient fetchHearingModeDeviceRecordForIdentifier:]_block_invoke_2
+ ___61-[HMServiceClient fetchHearingModeDeviceRecordForIdentifier:]_block_invoke_2.cold.1
+ ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.449
+ ___block_descriptor_48_e8_32s40r_e24_v16?0"HMDeviceRecord"8lr40l8s32l8
+ _objc_msgSend$clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.446
CStrings:
+ "### sync fetch for HMDeviceRecord id: %@ failed with XPC %{error}"
+ "### sync fetch for HMDeviceRecord id: %@ failed with XPC error: %{error}"
+ "-[HMServiceClient fetchHearingModeDeviceRecordForIdentifier:]_block_invoke"
+ "-[HMServiceClient fetchHearingModeDeviceRecordForIdentifier:]_block_invoke_2"
+ "-[HMServiceClient getHearingModeDeviceRecordForIdentifier:]"
+ "HMDeviceRecord UUID %@, settings received: version: %d, LEFT ear loss_01_dBHL: %lf, RIGHT ear loss_01_dBHL: %lf, leftGain: %lf, rightGain: %lf, tone: %lf, amplification: %lf, balance: %lf, beamFormer: %lf, noiseSuppression: %lf"
+ "HeadphoneDeeplinkingV1"
+ "HeadphoneFeatures"
+ "TB,N,V_sharedRegionStatus"
+ "_sharedRegionStatus"
+ "clientSyncFetchHearingModeDeviceRecordForIdentifier:recordHandler:"
+ "getHearingModeDeviceRecordForIdentifier:"
+ "setSharedRegionStatus:"
+ "sharedRegionStatus"
+ "sync fetch for HMDeviceRecord id: %@ returned: %@ "
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v16@?0@\"HMDeviceRecord\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HMDeviceRecord\">24"
- "HMDeviceRecord UUID %@, received settings: version: %d, LEFT ear loss_01_dBHL: %lf, RIGHT ear loss_01_dBHL: %lf, leftGain: %lf, rightGain: %lf, tone: %lf, amplification: %lf, balance: %lf, beamFormer: %lf, noiseSuppression: %lf"

```

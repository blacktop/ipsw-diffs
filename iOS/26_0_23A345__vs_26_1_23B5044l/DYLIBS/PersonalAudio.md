## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-495.0.0.0.0
-  __TEXT.__text: 0x16d20
-  __TEXT.__auth_stubs: 0x520
+496.2.0.0.0
+  __TEXT.__text: 0x14f50
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_methlist: 0xd90
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x48c
-  __TEXT.__cstring: 0x24b7
-  __TEXT.__oslogstring: 0x246
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__cstring: 0x12a6
+  __TEXT.__oslogstring: 0xb8e
   __TEXT.__dlopen_cstrs: 0x1c1
   __TEXT.__unwind_info: 0x590
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x2fbc
+  __TEXT.__objc_methname: 0x2fda
   __TEXT.__objc_methtype: 0x40b
-  __TEXT.__objc_stubs: 0x2e20
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__objc_stubs: 0x2e40
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x940
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xe50
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x1f80
+  __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48

   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xe0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2018848A-29E6-365D-A65D-B5C5B6E51FE7
-  Functions: 443
-  Symbols:   1684
-  CStrings:  1218
+  UUID: EA6DF0F8-BBE0-32FE-BBF7-1AFE6338179D
+  Functions: 447
+  Symbols:   1693
+  CStrings:  1111
 
Symbols:
+ -[PASettings archivedDataFromConfiguration:].cold.1
+ -[PASettings configurationFromData:].cold.1
+ GCC_except_table9
+ _HCLogAudioAccommodations
+ ___26-[PAAccessoryManager init]_block_invoke.11
+ ___26-[PAAccessoryManager init]_block_invoke.14
+ ___26-[PAAccessoryManager init]_block_invoke.18
+ ___26-[PAAccessoryManager init]_block_invoke.20
+ ___26-[PAAccessoryManager init]_block_invoke.26
+ ___26-[PAAccessoryManager init]_block_invoke.5
+ ___26-[PAAccessoryManager init]_block_invoke.8
+ ___39-[PAHMSManager setupHearingModeService]_block_invoke.7
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.41
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.42
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.43
+ ___block_literal_global.10
+ ___block_literal_global.169
+ ___block_literal_global.29
+ ___block_literal_global.46
+ ___block_literal_global.76
+ ___getAXHeardControllerClass_block_invoke
+ ___getAXHeardControllerClass_block_invoke.cold.1
+ _getAXHeardControllerClass.softClass
+ _objc_msgSend$isTransparencyUpdatePending
+ _objc_msgSend$sharedServer
- _PAEngineeringLog
- _PAInitializeLogging
- ___26-[PAAccessoryManager init]_block_invoke.10
- ___26-[PAAccessoryManager init]_block_invoke.16
- ___26-[PAAccessoryManager init]_block_invoke.22
- ___26-[PAAccessoryManager init]_block_invoke.28
- ___26-[PAAccessoryManager init]_block_invoke.40
- ___26-[PAAccessoryManager init]_block_invoke.45
- ___26-[PAAccessoryManager init]_block_invoke_2.51
- ___39-[PAHMSManager setupHearingModeService]_block_invoke.19
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.91
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.95
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.99
- ___block_literal_global.102
- ___block_literal_global.115
- ___block_literal_global.181
- ___block_literal_global.36
- ___block_literal_global.47
- ___block_literal_global.54
- ___block_literal_global.87
- _objc_msgSend$UTF8String
- _objc_retain_x27
CStrings:
+ "AXHeardController"
+ "Skipping transparency update for %@ because we have newer updates pending."
+ "isTransparencyUpdatePending"
+ "sharedServer"
- "%s:%d %@"
- "%{public}s"
- "+[PAConfiguration configurationWithAudiogram:]"
- "+[PAConfiguration configurationWithLeftMediaLoss:rightMediaLoss:leftSpeechLoss:andRightSpeechLoss:]"
- "+[PAConfiguration configurationWithMediaOffsets:andSpeechOffsets:]"
- "-[PAAccessoryManager init]_block_invoke"
- "-[PAAccessoryManager init]_block_invoke_2"
- "-[PAAccessoryManager routesDidChange:]"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory]"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_3"
- "-[PAAccessoryManager sendUpdateToAccessory]"
- "-[PAAccessoryManager sendUpdateToAccessory]_block_invoke"
- "-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_4"
- "-[PAConfiguration onBudsMediaSettingsForRoute:]"
- "-[PAConfiguration pureToneAverageForSpeech:]"
- "-[PAConfiguration readSettingsFromPreset:]"
- "-[PAConfiguration settingsFromConfiguration:]"
- "-[PAConfiguration transparencySettingsForAddress:]"
- "-[PAConfiguration transparencySettingsv4ForAddress:]"
- "-[PADatabaseManager logMessage:]"
- "-[PADatabaseManager saveConfiguration:]_block_invoke"
- "-[PAHMSManager hearingAidEnabledForAddress:]_block_invoke"
- "-[PAHMSManager ownVoiceSupportedForAddress:]_block_invoke"
- "-[PAHMSManager ppeEnrolledForAddress:]_block_invoke"
- "-[PAHMSManager regionSupportedForHearingProtection:]_block_invoke"
- "-[PAHMSManager sendConfigUpdate:forAddress:]"
- "-[PAHMSManager sendConfigUpdate:forAddress:]_block_invoke"
- "-[PAHMSManager sendConfigUpdate:forAddress:]_block_invoke_2"
- "-[PAHMSManager setupHearingModeService]_block_invoke"
- "-[PAHMSManager setupHearingModeService]_block_invoke_3"
- "-[PAHMSManager toggleHearingAidForAddress:]_block_invoke"
- "-[PASettings archivedDataFromConfiguration:]"
- "-[PASettings configurationFromData:]"
- "-[PASettings logMessage:]"
- "-[PASettings setAccommodationTypes:forRouteUID:]"
- "-[PASettings setPersonalMediaConfiguration:forRouteUID:]"
- "-[PASettings setPersonalMediaEnabled:forRouteUID:]"
- "-[PASettings updateConfiguration:forRouteID:]"
- "-[PAStimulus play]"
- "BOOL paBluetoothDeviceSupportsSSL(BluetoothDevice *__strong _Nonnull)"
- "NSArray<BluetoothDevice *> *paPairedDevicesSupportingTransparencyAccommodations(void)"
- "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL)"
- "NSArray<NSDictionary *> *paRoutesOfSubtypeOrProduct(NSSet *__strong, NSSet *__strong, BOOL)_block_invoke"
- "UTF8String"
- "void setCurrentDeviceToTransparencyMode(void)"

```

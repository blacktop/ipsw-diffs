## carkitd

> `/usr/libexec/carkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-808.6.0.0.0
-  __TEXT.__text: 0x95e38
+808.9.1.0.0
+  __TEXT.__text: 0x96440
   __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_stubs: 0x11c00
-  __TEXT.__objc_methlist: 0x7dfc
+  __TEXT.__objc_stubs: 0x11e40
+  __TEXT.__objc_methlist: 0x7e2c
   __TEXT.__const: 0x712
   __TEXT.__gcc_except_tab: 0x1a60
-  __TEXT.__cstring: 0x6ad2
-  __TEXT.__objc_methname: 0x19364
-  __TEXT.__oslogstring: 0x11d71
+  __TEXT.__cstring: 0x6b42
+  __TEXT.__objc_methname: 0x19694
+  __TEXT.__oslogstring: 0x11dc1
   __TEXT.__objc_classname: 0x112b
-  __TEXT.__objc_methtype: 0x4a1e
+  __TEXT.__objc_methtype: 0x4ace
   __TEXT.__dlopen_cstrs: 0x16e
   __TEXT.__swift5_typeref: 0x1ca
   __TEXT.__constg_swiftt: 0x14c

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x110
-  __TEXT.__unwind_info: 0x3058
-  __DATA_CONST.__const: 0x3730
-  __DATA_CONST.__cfstring: 0x8220
+  __TEXT.__unwind_info: 0x3068
+  __DATA_CONST.__const: 0x3760
+  __DATA_CONST.__cfstring: 0x8280
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x280

   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xc88
-  __DATA_CONST.__got: 0x9c8
+  __DATA_CONST.__got: 0x9d0
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA.__objc_const: 0x14a38
-  __DATA.__objc_selrefs: 0x5248
-  __DATA.__objc_ivar: 0x7e8
+  __DATA.__objc_const: 0x14a88
+  __DATA.__objc_selrefs: 0x52d8
+  __DATA.__objc_ivar: 0x7f0
   __DATA.__objc_data: 0x1d58
   __DATA.__data: 0x1e70
   __DATA.__common: 0x30

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3478
-  Symbols:   752
-  CStrings:  6937
+  Functions: 3485
+  Symbols:   754
+  CStrings:  6966
 
Symbols:
+ _CAFCharacteristicTypeVehicleHandling
+ _CAFCharacteristicTypeVehicleHandlingWithAI
+ _OBJC_CLASS_$_CRVehicleMessagingSupport
+ __swift_FORCE_LOAD_$_swiftAccelerate
- _CAFCharacteristicTypeMessageAIProcessing
- _CAFCharacteristicTypeMessageHandling
CStrings:
+ "@\"CRVehicleMessagingSupport\""
+ "@\"CRVehicleMessagingSupport\"32@0:8@\"CRPairingPromptFlowController\"16@\"CRPairingAirPlaySessionInfo\"24"
+ "T@\"CRVehicleMessagingSupport\",&,N,V_presentedVehicleMessagingSupport"
+ "TB,N,V_awaitingVehicleMessagingAIPrompt"
+ "TB,R,N,V_supportsVehicleHandlesMessagingWithAI"
+ "_awaitingVehicleMessagingAIPrompt"
+ "_finishVehicleMessagingWithSelection:acceptedAIPrompt:"
+ "_hasAcceptedVehicleMessagingAIPrompt"
+ "_presentVehicleHandlesMessagingWithAIPromptWithCompletion:"
+ "_presentedVehicleMessagingSupport"
+ "_setVehicleMessagingSelection:acceptedAIPrompt:forPromptFlow:"
+ "_supportsVehicleHandlesMessagingWithAI"
+ "_updateContactsSyncStatusFromBluetoothForVehicle:"
+ "_updateMessageAccessForVehicle:previousVehicleHandlesMessagingStatus:"
+ "_vehicleMessagingSupport"
+ "appIntegrationOptions"
+ "appIntegrationOptionsMode"
+ "awaitingVehicleMessagingAIPrompt"
+ "builtInSelection"
+ "contactsSyncEnabledForBluetoothAddress:"
+ "contactsSyncStatus"
+ "failed to find the device (%{private, mask.hash}@) to read contacts sync settings"
+ "hasAcceptedVehicleHandlesMessagingWithAIPrompt"
+ "initWithSupportsRouteSharing:userVisibleReason:brand:supportsVideoPlayback:supportsLodWidgets:supportsSiriMixable:supportsEnhancedSiriVoice:supportsDolbyAtmos:supportsSpatialAudio:supportsLiveActivities:supportsVehicleHandlesMessaging:supportsVehicleHandlesMessagingWithAI:"
+ "isAIOptional"
+ "offersAI"
+ "offersBuiltIn"
+ "pairingPromptFlow:receivedVehicleMessagingSelection:acceptedAIPrompt:"
+ "presentVehicleHandlesMessagingPromptForVehicleBrand:needsAIConsent:responseHandler:"
+ "presentVehicleHandlesMessagingWithAIPromptForVehicleBrand:responseHandler:"
+ "presentedVehicleMessagingSupport"
+ "received response for vehicle handles messaging with AI prompt: %{public}@"
+ "selectionForAIPromptAccepted:"
+ "setAppIntegrationOptionsMode:"
+ "setAwaitingVehicleMessagingAIPrompt:"
+ "setContactsSyncStatus:"
+ "setHasAcceptedVehicleHandlesMessagingWithAIPrompt:"
+ "setPresentedVehicleMessagingSupport:"
+ "setSupportsVehicleHandlesMessagingWithAI:"
+ "setVehicleHandlesMessagingWithAIStatus:"
+ "setVehicleMessagingSelection:"
+ "setting contacts sync status from Bluetooth: %{public}@"
+ "supportWithHandling:handlingWithAI:"
+ "supportsRouteSharing: %@, supportsVideoPlayback: %@, supportsLodWidgets: %@, supportsSiriMixable:%@, supportsEnhancedSiriVoice: %@, supportsDolbyAtmos: %@, supportsSpatialAudio: %@, supportsLiveActivities: %@, supportsVehicleHandlesMessaging: %@, supportsVehicleHandlesMessagingWithAI: %@"
+ "supportsVehicleHandlesMessagingWithAI"
+ "v28@0:8Q16B24"
+ "v36@0:8@\"CRPairingPromptFlowController\"16Q24B32"
+ "v36@0:8@\"NSString\"16B24@?<v@?B>28"
+ "v36@0:8@16Q24B32"
+ "v36@0:8Q16B24@28"
+ "vehicle handles messaging with AI permission"
+ "vehicle handles messaging with AI prompt received response: %{public}@"
+ "vehicle messaging selection: %lu, accepted AI prompt: %{public}@"
+ "vehicleHandlesMessagingWithAIStatus"
+ "vehicleMessagingSupportForPairingPromptFlow:sessionInfo:"
- "B32@0:8@\"CRPairingPromptFlowController\"16@\"CRPairingAirPlaySessionInfo\"24"
- "TB,R,N,V_supportsVehicleMessageAIProcessing"
- "_presentVehicleMessageAIProcessingPromptWithCompletion:"
- "_setVehicleHandlesMessagingStatus:forPromptFlow:"
- "_setVehicleMessageAIProcessingStatus:forPromptFlow:"
- "_supportsVehicleMessageAIProcessing"
- "initWithSupportsRouteSharing:userVisibleReason:brand:supportsVideoPlayback:supportsLodWidgets:supportsSiriMixable:supportsEnhancedSiriVoice:supportsDolbyAtmos:supportsSpatialAudio:supportsLiveActivities:supportsVehicleHandlesMessaging:supportsVehicleMessageAIProcessing:"
- "pairingPromptFlow:receivedVehicleHandlesMessagingResponse:"
- "pairingPromptFlow:receivedVehicleMessageAIProcessingResponse:"
- "presentVehicleHandlesMessagingPromptForVehicleName:responseHandler:"
- "presentVehicleMessageAIProcessingPromptForVehicleName:responseHandler:"
- "received response for vehicle message processing prompt: %{public}@"
- "routeSharingUserVisibleBrand"
- "setSupportsVehicleMessageAIProcessing:"
- "setVehicleMessageAIProcessingStatus:"
- "supportsRouteSharing: %@, supportsVideoPlayback: %@, supportsLodWidgets: %@, supportsSiriMixable:%@, supportsEnhancedSiriVoice: %@, supportsDolbyAtmos: %@, supportsSpatialAudio: %@, supportsLiveActivities: %@, supportsVehicleHandlesMessaging: %@, supportsVehicleMessageAIProcessing: %@"
- "supportsVehicleHandlesMessagingForPairingPromptFlow:sessionInfo:"
- "supportsVehicleMessageAIProcessing"
- "supportsVehicleMessageAIProcessingForPairingPromptFlow:sessionInfo:"
- "vehicle handles messaging accepted"
- "vehicle handles messaging declined"
- "vehicle message processing accepted"
- "vehicle message processing declined"
- "vehicle message processing permission"
- "vehicle message processing prompt received response: %{public}@"
- "vehicleMessageAIProcessingStatus"
```

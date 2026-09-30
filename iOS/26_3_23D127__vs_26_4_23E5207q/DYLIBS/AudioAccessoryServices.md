## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-33.1.0.0.0
-  __TEXT.__text: 0x40024
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x526c
-  __TEXT.__const: 0x2a0
-  __TEXT.__gcc_except_tab: 0x1598
-  __TEXT.__cstring: 0xb811
-  __TEXT.__unwind_info: 0x10b8
-  __TEXT.__objc_classname: 0x63c
-  __TEXT.__objc_methname: 0xb707
-  __TEXT.__objc_methtype: 0x13f9
-  __TEXT.__objc_stubs: 0x5ac0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xe50
-  __DATA_CONST.__objc_classlist: 0x178
+34.25.1.1.1
+  __TEXT.__text: 0x49f5c
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x5a0c
+  __TEXT.__const: 0x2e0
+  __TEXT.__gcc_except_tab: 0x16b4
+  __TEXT.__cstring: 0xd6c6
+  __TEXT.__unwind_info: 0x1620
+  __TEXT.__objc_classname: 0x705
+  __TEXT.__objc_methname: 0xc5fd
+  __TEXT.__objc_methtype: 0x167c
+  __TEXT.__objc_stubs: 0x6260
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2460
+  __DATA_CONST.__objc_selrefs: 0x2758
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x440
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2420
-  __AUTH_CONST.__objc_const: 0x95f0
-  __AUTH.__objc_data: 0x7d0
+  __DATA_CONST.__objc_superrefs: 0x158
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__objc_const: 0xa2e8
+  __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x8e4
-  __DATA.__data: 0xcc8
+  __DATA.__objc_ivar: 0x998
+  __DATA.__data: 0xe88
   __DATA.__common: 0x8
-  __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__data: 0x230
-  __DATA_DIRTY.__bss: 0x20
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__data: 0x2a0
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A137C7A6-91A2-3BF0-A406-0E69864D2DD3
-  Functions: 2167
-  Symbols:   6564
-  CStrings:  4090
+  UUID: 0C726EDF-533D-3A34-A81C-8383FACAE201
+  Functions: 2480
+  Symbols:   7405
+  CStrings:  4430
 
Symbols:
+ +[AA3PDeviceRoutingControl supportsSecureCoding]
+ +[AAAccessoryFeatureFlagConfiguration createQueryMessage]
+ +[AAAccessoryFeatureFlagConfiguration createQueryMessage].cold.1
+ +[AAAccessoryFeatureFlagConfiguration createSetFeatureFlagMessage:]
+ +[AAAccessoryFeatureFlagConfiguration supportsSecureCoding]
+ +[AAAccessoryFeatureFlagEntry supportsSecureCoding]
+ +[AAAccessoryFeatureFlagRules defaultRules]
+ +[AAAccessoryFeatureFlagRules defaultRules].cold.1
+ +[AAAssetHelper productColorAssetExists:withColor:]
+ +[AAAssetHelper productHasColors:isCase:]
+ +[AAControllerSharedXPCManager sharedManager]
+ +[AAControllerSharedXPCManager sharedManager].cold.1
+ +[AAHeadphoneActivityProvider supportsSecureCoding]
+ -[AA3PDeviceRoutingControl .cxx_destruct]
+ -[AA3PDeviceRoutingControl _ensureXPCStarted]
+ -[AA3PDeviceRoutingControl _handleServerDied]
+ -[AA3PDeviceRoutingControl _interrupted]
+ -[AA3PDeviceRoutingControl _interrupted].cold.1
+ -[AA3PDeviceRoutingControl _invalidated]
+ -[AA3PDeviceRoutingControl _invalidated].cold.1
+ -[AA3PDeviceRoutingControl _invalidated].cold.2
+ -[AA3PDeviceRoutingControl _reportError:]
+ -[AA3PDeviceRoutingControl _reportError:].cold.1
+ -[AA3PDeviceRoutingControl clientID]
+ -[AA3PDeviceRoutingControl description]
+ -[AA3PDeviceRoutingControl deviceAddress]
+ -[AA3PDeviceRoutingControl dispatchQueue]
+ -[AA3PDeviceRoutingControl encodeWithCoder:]
+ -[AA3PDeviceRoutingControl initWithCoder:]
+ -[AA3PDeviceRoutingControl init]
+ -[AA3PDeviceRoutingControl invalidate]
+ -[AA3PDeviceRoutingControl setClientID:]
+ -[AA3PDeviceRoutingControl setDeviceAddress:]
+ -[AA3PDeviceRoutingControl setDispatchQueue:]
+ -[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:]
+ -[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:].cold.1
+ -[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:].cold.2
+ -[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:].cold.3
+ -[AA3PDeviceRoutingControl setProperty:value:]
+ -[AA3PDeviceRoutingControl setProperty:value:].cold.1
+ -[AA3PDeviceRoutingControl setProperty:value:].cold.2
+ -[AA3PDeviceRoutingControl setTestListenerEndpoint:]
+ -[AA3PDeviceRoutingControl testListenerEndpoint]
+ -[AAAccessoryFeatureFlagConfiguration .cxx_destruct]
+ -[AAAccessoryFeatureFlagConfiguration _applyConfigurationUpdate:]
+ -[AAAccessoryFeatureFlagConfiguration _isConfigurationUpdateMessageValid:]
+ -[AAAccessoryFeatureFlagConfiguration _isConfigurationUpdateMessageValid:].cold.1
+ -[AAAccessoryFeatureFlagConfiguration _isConfigurationUpdateMessageValid:].cold.2
+ -[AAAccessoryFeatureFlagConfiguration encodeWithCoder:]
+ -[AAAccessoryFeatureFlagConfiguration featureFlags]
+ -[AAAccessoryFeatureFlagConfiguration handleUpdate:]
+ -[AAAccessoryFeatureFlagConfiguration identifier]
+ -[AAAccessoryFeatureFlagConfiguration initWithCoder:]
+ -[AAAccessoryFeatureFlagConfiguration initWithIdentifier:]
+ -[AAAccessoryFeatureFlagConfiguration routed]
+ -[AAAccessoryFeatureFlagConfiguration setFeatureFlags:]
+ -[AAAccessoryFeatureFlagConfiguration setRouted:]
+ -[AAAccessoryFeatureFlagEntry .cxx_destruct]
+ -[AAAccessoryFeatureFlagEntry appendMessageToBuffer:]
+ -[AAAccessoryFeatureFlagEntry coreID]
+ -[AAAccessoryFeatureFlagEntry description]
+ -[AAAccessoryFeatureFlagEntry encodeWithCoder:]
+ -[AAAccessoryFeatureFlagEntry featureID]
+ -[AAAccessoryFeatureFlagEntry initWithCoder:]
+ -[AAAccessoryFeatureFlagEntry initWithFeatureID:coreID:state:payload:]
+ -[AAAccessoryFeatureFlagEntry messageSize]
+ -[AAAccessoryFeatureFlagEntry payload]
+ -[AAAccessoryFeatureFlagEntry state]
+ -[AAAccessoryFeatureFlagRules .cxx_destruct]
+ -[AAAccessoryFeatureFlagRules addRuleForFeatureID:stateDeterminer:]
+ -[AAAccessoryFeatureFlagRules addRuleForFeatureID:stateDeterminer:payloadGenerator:]
+ -[AAAccessoryFeatureFlagRules applyRulesToAccessory:]
+ -[AAAccessoryFeatureFlagRules applyRulesToAccessory:].cold.1
+ -[AAAccessoryFeatureFlagRules applyRulesToAccessory:].cold.2
+ -[AAAccessoryFeatureFlagRules applyRulesToAccessory:].cold.3
+ -[AAAccessoryFeatureFlagRules init]
+ -[AAController _activate:]
+ -[AAController _registerWithSharedManager:]
+ -[AAController _registerWithSharedManager:].cold.1
+ -[AAController _registerWithSharedManager:].cold.2
+ -[AAController _requestAllAADeviceInfosWithCompletionHandler:]
+ -[AAController _requestAllAADeviceInfosWithCompletionHandler:].cold.1
+ -[AAController _setFeatureFlagMessageReceived:fromDevice:]
+ -[AAController requestAllAADeviceInfosWithCompletionHandler:]
+ -[AAController sendFeatureFlagMessage:destinationIdentifier:completionHandler:]
+ -[AAController sendPTEventMessage:destinationIdentifier:completionHandler:]
+ -[AAController setFeatureFlagMessageHandler]
+ -[AAController setSetFeatureFlagMessageHandler:]
+ -[AAControllerSharedXPCManager .cxx_destruct]
+ -[AAControllerSharedXPCManager _activateSharedConnection]
+ -[AAControllerSharedXPCManager _activateSharedConnection].cold.1
+ -[AAControllerSharedXPCManager _distributeXPCMessage:]
+ -[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]
+ -[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:].cold.1
+ -[AAControllerSharedXPCManager _handleActivationReply:]
+ -[AAControllerSharedXPCManager _handleActivationReply:].cold.1
+ -[AAControllerSharedXPCManager _handleActivationReply:].cold.2
+ -[AAControllerSharedXPCManager _handleConnectionInterruption]
+ -[AAControllerSharedXPCManager _handleConnectionInterruption].cold.1
+ -[AAControllerSharedXPCManager _handleConnectionInvalidation]
+ -[AAControllerSharedXPCManager _handleXPCEvent:]
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.1
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.2
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.3
+ -[AAControllerSharedXPCManager _handleXPCEvent:].cold.4
+ -[AAControllerSharedXPCManager _invalidateConnection]
+ -[AAControllerSharedXPCManager _processPendingMessages]
+ -[AAControllerSharedXPCManager _processPendingMessages].cold.1
+ -[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]
+ -[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:].cold.1
+ -[AAControllerSharedXPCManager connectionActive]
+ -[AAControllerSharedXPCManager dealloc]
+ -[AAControllerSharedXPCManager init]
+ -[AAControllerSharedXPCManager init].cold.1
+ -[AAControllerSharedXPCManager invalidateCalled]
+ -[AAControllerSharedXPCManager invalidate]
+ -[AAControllerSharedXPCManager managerQueue]
+ -[AAControllerSharedXPCManager pendingMessages]
+ -[AAControllerSharedXPCManager registerController:completion:]
+ -[AAControllerSharedXPCManager registeredControllers]
+ -[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]
+ -[AAControllerSharedXPCManager setConnectionActive:]
+ -[AAControllerSharedXPCManager setInvalidateCalled:]
+ -[AAControllerSharedXPCManager setManagerQueue:]
+ -[AAControllerSharedXPCManager setPendingMessages:]
+ -[AAControllerSharedXPCManager setRegisteredControllers:]
+ -[AAControllerSharedXPCManager unregisterController:]
+ -[AADeviceBatteryInfo reportLowBatteryFromMain]
+ -[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]
+ -[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:].cold.1
+ -[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]
+ -[AAHeadphoneActivityProvider .cxx_destruct]
+ -[AAHeadphoneActivityProvider _activate:]
+ -[AAHeadphoneActivityProvider _activate:].cold.1
+ -[AAHeadphoneActivityProvider _activateDirect:]
+ -[AAHeadphoneActivityProvider _activateDirect:].cold.1
+ -[AAHeadphoneActivityProvider _activateXPC:reactivate:]
+ -[AAHeadphoneActivityProvider _activateXPC:reactivate:].cold.1
+ -[AAHeadphoneActivityProvider _activateXPC:reactivate:].cold.2
+ -[AAHeadphoneActivityProvider _ensureXPCStarted]
+ -[AAHeadphoneActivityProvider _interrupted]
+ -[AAHeadphoneActivityProvider _interrupted].cold.1
+ -[AAHeadphoneActivityProvider _invalidateDirect]
+ -[AAHeadphoneActivityProvider _invalidated]
+ -[AAHeadphoneActivityProvider _invalidated].cold.1
+ -[AAHeadphoneActivityProvider _invalidated].cold.2
+ -[AAHeadphoneActivityProvider _reportError:]
+ -[AAHeadphoneActivityProvider _reportError:].cold.1
+ -[AAHeadphoneActivityProvider activateWithCompletion:]
+ -[AAHeadphoneActivityProvider clientID]
+ -[AAHeadphoneActivityProvider conversationAwarenessStateUpdateHandler]
+ -[AAHeadphoneActivityProvider conversationAwarenessStateUpdated:forDeviceAddress:]
+ -[AAHeadphoneActivityProvider conversationAwarenessStateUpdated:forDeviceAddress:].cold.1
+ -[AAHeadphoneActivityProvider dispatchQueue]
+ -[AAHeadphoneActivityProvider encodeWithCoder:]
+ -[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]
+ -[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]
+ -[AAHeadphoneActivityProvider headphoneActivityProviderFlags]
+ -[AAHeadphoneActivityProvider initWithCoder:]
+ -[AAHeadphoneActivityProvider init]
+ -[AAHeadphoneActivityProvider interruptionHandler]
+ -[AAHeadphoneActivityProvider invalidate]
+ -[AAHeadphoneActivityProvider invalidationHandler]
+ -[AAHeadphoneActivityProvider setClientID:]
+ -[AAHeadphoneActivityProvider setConversationAwarenessStateUpdateHandler:]
+ -[AAHeadphoneActivityProvider setDispatchQueue:]
+ -[AAHeadphoneActivityProvider setHeadphoneActivityProviderFlags:]
+ -[AAHeadphoneActivityProvider setInterruptionHandler:]
+ -[AAHeadphoneActivityProvider setInvalidationHandler:]
+ -[AAHeadphoneActivityProvider setSleepStateUpdateHandler:]
+ -[AAHeadphoneActivityProvider setTestListenerEndpoint:]
+ -[AAHeadphoneActivityProvider sleepStateUpdateHandler]
+ -[AAHeadphoneActivityProvider sleepStateUpdated:sleepTimestamp:forDeviceAddress:]
+ -[AAHeadphoneActivityProvider sleepStateUpdated:sleepTimestamp:forDeviceAddress:].cold.1
+ -[AAHeadphoneActivityProvider testListenerEndpoint]
+ -[AASensorService _sendPTEventToAccessory:value:completion:]
+ -[AASensorService sendPTEventToAccessory:value:completion:]
+ -[AudioAccessoryDevice color]
+ -[AudioAccessoryDevice lastSeenConnectedOnHeadTime]
+ -[AudioAccessoryDevice setColor:]
+ -[AudioAccessoryDevice setLastSeenConnectedOnHeadTime:]
+ -[AudioAccessoryDevice setSmartRoutingVersion:]
+ -[AudioAccessoryDevice smartRoutingVersion]
+ -[BTMagicPairingSettings crownRotationDirection]
+ -[BTMagicPairingSettings setCrownRotationDirection:]
+ -[_FeatureFlagRule .cxx_destruct]
+ -[_FeatureFlagRule payloadGenerator]
+ -[_FeatureFlagRule setPayloadGenerator:]
+ -[_FeatureFlagRule setStateDeterminer:]
+ -[_FeatureFlagRule stateDeterminer]
+ GCC_except_table17
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table67
+ _NSStringFromClass
+ _OBJC_CLASS_$_AA3PDeviceRoutingControl
+ _OBJC_CLASS_$_AAAccessoryFeatureFlagConfiguration
+ _OBJC_CLASS_$_AAAccessoryFeatureFlagEntry
+ _OBJC_CLASS_$_AAAccessoryFeatureFlagRules
+ _OBJC_CLASS_$_AAControllerSharedXPCManager
+ _OBJC_CLASS_$_AAHeadphoneActivityProvider
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$__FeatureFlagRule
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._activateCalled
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._activateCompletion
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._clientID
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._deviceAddress
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._direct
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._dispatchQueue
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._invalidateCalled
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._invalidateDone
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._testListenerEndpoint
+ _OBJC_IVAR_$_AA3PDeviceRoutingControl._xpcCnx
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagConfiguration._featureFlags
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagConfiguration._identifier
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagConfiguration._routed
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagEntry._coreID
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagEntry._featureID
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagEntry._payload
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagEntry._state
+ _OBJC_IVAR_$_AAAccessoryFeatureFlagRules._rulesByFeatureID
+ _OBJC_IVAR_$_AAController._registeredWithManager
+ _OBJC_IVAR_$_AAController._setFeatureFlagMessageHandler
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._connectionActive
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._connectionEstablished
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._invalidateCalled
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._managerQueue
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._pendingActivations
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._pendingMessages
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._registeredControllers
+ _OBJC_IVAR_$_AAControllerSharedXPCManager._sharedXPCConnection
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._activateCalled
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._activateCompletion
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._clientID
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._conversationAwarenessStateUpdateHandler
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._direct
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._dispatchQueue
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._headphoneActivityProviderFlags
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._interruptionHandler
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._invalidateCalled
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._invalidateDone
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._invalidationHandler
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._sleepStateUpdateHandler
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._testListenerEndpoint
+ _OBJC_IVAR_$_AAHeadphoneActivityProvider._xpcCnx
+ _OBJC_IVAR_$_AudioAccessoryDevice._color
+ _OBJC_IVAR_$_AudioAccessoryDevice._lastSeenConnectedOnHeadTime
+ _OBJC_IVAR_$_AudioAccessoryDevice._smartRoutingVersion
+ _OBJC_IVAR_$_BTMagicPairingSettings._crownRotationDirection
+ _OBJC_IVAR_$__FeatureFlagRule._payloadGenerator
+ _OBJC_IVAR_$__FeatureFlagRule._stateDeterminer
+ _OBJC_METACLASS_$_AA3PDeviceRoutingControl
+ _OBJC_METACLASS_$_AAAccessoryFeatureFlagConfiguration
+ _OBJC_METACLASS_$_AAAccessoryFeatureFlagEntry
+ _OBJC_METACLASS_$_AAAccessoryFeatureFlagRules
+ _OBJC_METACLASS_$_AAControllerSharedXPCManager
+ _OBJC_METACLASS_$_AAHeadphoneActivityProvider
+ _OBJC_METACLASS_$__FeatureFlagRule
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ __OBJC_$_CLASS_METHODS_AA3PDeviceRoutingControl
+ __OBJC_$_CLASS_METHODS_AAAccessoryFeatureFlagConfiguration
+ __OBJC_$_CLASS_METHODS_AAAccessoryFeatureFlagEntry
+ __OBJC_$_CLASS_METHODS_AAAccessoryFeatureFlagRules
+ __OBJC_$_CLASS_METHODS_AAControllerSharedXPCManager
+ __OBJC_$_CLASS_METHODS_AAHeadphoneActivityProvider
+ __OBJC_$_CLASS_PROP_LIST_AA3PDeviceRoutingControl
+ __OBJC_$_CLASS_PROP_LIST_AAAccessoryFeatureFlagConfiguration
+ __OBJC_$_CLASS_PROP_LIST_AAAccessoryFeatureFlagEntry
+ __OBJC_$_CLASS_PROP_LIST_AAHeadphoneActivityProvider
+ __OBJC_$_INSTANCE_METHODS_AA3PDeviceRoutingControl
+ __OBJC_$_INSTANCE_METHODS_AAAccessoryFeatureFlagConfiguration
+ __OBJC_$_INSTANCE_METHODS_AAAccessoryFeatureFlagEntry
+ __OBJC_$_INSTANCE_METHODS_AAAccessoryFeatureFlagRules
+ __OBJC_$_INSTANCE_METHODS_AAControllerSharedXPCManager
+ __OBJC_$_INSTANCE_METHODS_AAHeadphoneActivityProvider
+ __OBJC_$_INSTANCE_METHODS__FeatureFlagRule
+ __OBJC_$_INSTANCE_VARIABLES_AA3PDeviceRoutingControl
+ __OBJC_$_INSTANCE_VARIABLES_AAAccessoryFeatureFlagConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AAAccessoryFeatureFlagEntry
+ __OBJC_$_INSTANCE_VARIABLES_AAAccessoryFeatureFlagRules
+ __OBJC_$_INSTANCE_VARIABLES_AAControllerSharedXPCManager
+ __OBJC_$_INSTANCE_VARIABLES_AAHeadphoneActivityProvider
+ __OBJC_$_INSTANCE_VARIABLES__FeatureFlagRule
+ __OBJC_$_PROP_LIST_AA3PDeviceRoutingControl
+ __OBJC_$_PROP_LIST_AAAccessoryFeatureFlagConfiguration
+ __OBJC_$_PROP_LIST_AAAccessoryFeatureFlagEntry
+ __OBJC_$_PROP_LIST_AAControllerSharedXPCManager
+ __OBJC_$_PROP_LIST_AAHeadphoneActivityProvider
+ __OBJC_$_PROP_LIST__FeatureFlagRule
+ __OBJC_CLASS_PROTOCOLS_$_AA3PDeviceRoutingControl
+ __OBJC_CLASS_PROTOCOLS_$_AAAccessoryFeatureFlagConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AAAccessoryFeatureFlagEntry
+ __OBJC_CLASS_PROTOCOLS_$_AAHeadphoneActivityProvider
+ __OBJC_CLASS_RO_$_AA3PDeviceRoutingControl
+ __OBJC_CLASS_RO_$_AAAccessoryFeatureFlagConfiguration
+ __OBJC_CLASS_RO_$_AAAccessoryFeatureFlagEntry
+ __OBJC_CLASS_RO_$_AAAccessoryFeatureFlagRules
+ __OBJC_CLASS_RO_$_AAControllerSharedXPCManager
+ __OBJC_CLASS_RO_$_AAHeadphoneActivityProvider
+ __OBJC_CLASS_RO_$__FeatureFlagRule
+ __OBJC_METACLASS_RO_$_AA3PDeviceRoutingControl
+ __OBJC_METACLASS_RO_$_AAAccessoryFeatureFlagConfiguration
+ __OBJC_METACLASS_RO_$_AAAccessoryFeatureFlagEntry
+ __OBJC_METACLASS_RO_$_AAAccessoryFeatureFlagRules
+ __OBJC_METACLASS_RO_$_AAControllerSharedXPCManager
+ __OBJC_METACLASS_RO_$_AAHeadphoneActivityProvider
+ __OBJC_METACLASS_RO_$__FeatureFlagRule
+ ___38-[AA3PDeviceRoutingControl invalidate]_block_invoke
+ ___38-[AA3PDeviceRoutingControl invalidate]_block_invoke.cold.1
+ ___41-[AAHeadphoneActivityProvider _activate:]_block_invoke
+ ___41-[AAHeadphoneActivityProvider _activate:]_block_invoke.cold.1
+ ___41-[AAHeadphoneActivityProvider _activate:]_block_invoke.cold.2
+ ___41-[AAHeadphoneActivityProvider invalidate]_block_invoke
+ ___41-[AAHeadphoneActivityProvider invalidate]_block_invoke.cold.1
+ ___42-[AAControllerSharedXPCManager invalidate]_block_invoke
+ ___42-[AAControllerSharedXPCManager invalidate]_block_invoke.cold.1
+ ___43+[AAAccessoryFeatureFlagRules defaultRules]_block_invoke
+ ___43-[AAController _registerWithSharedManager:]_block_invoke
+ ___43-[AAController _registerWithSharedManager:]_block_invoke.cold.1
+ ___43-[AAController _registerWithSharedManager:]_block_invoke.cold.2
+ ___45+[AAControllerSharedXPCManager sharedManager]_block_invoke
+ ___45-[AA3PDeviceRoutingControl _ensureXPCStarted]_block_invoke
+ ___45-[AA3PDeviceRoutingControl _ensureXPCStarted]_block_invoke_2
+ ___45-[AA3PDeviceRoutingControl _handleServerDied]_block_invoke
+ ___45-[AA3PDeviceRoutingControl _handleServerDied]_block_invoke.cold.1
+ ___46-[AA3PDeviceRoutingControl setProperty:value:]_block_invoke
+ ___46-[AA3PDeviceRoutingControl setProperty:value:]_block_invoke.cold.1
+ ___47-[AAHeadphoneActivityProvider _activateDirect:]_block_invoke
+ ___47-[AAHeadphoneActivityProvider _activateDirect:]_block_invoke_2
+ ___48-[AAHeadphoneActivityProvider _ensureXPCStarted]_block_invoke
+ ___48-[AAHeadphoneActivityProvider _ensureXPCStarted]_block_invoke_2
+ ___48-[AAHeadphoneActivityProvider _invalidateDirect]_block_invoke
+ ___48-[AAHeadphoneActivityProvider _invalidateDirect]_block_invoke_2
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke.cold.1
+ ___53-[AAControllerSharedXPCManager unregisterController:]_block_invoke.cold.2
+ ___54-[AAControllerSharedXPCManager _distributeXPCMessage:]_block_invoke
+ ___54-[AAHeadphoneActivityProvider activateWithCompletion:]_block_invoke
+ ___54-[AAHeadphoneActivityProvider activateWithCompletion:]_block_invoke.cold.1
+ ___55-[AAHeadphoneActivityProvider _activateXPC:reactivate:]_block_invoke
+ ___55-[AAHeadphoneActivityProvider _activateXPC:reactivate:]_block_invoke.cold.1
+ ___55-[AAHeadphoneActivityProvider _activateXPC:reactivate:]_block_invoke.cold.2
+ ___55-[AAHeadphoneActivityProvider _activateXPC:reactivate:]_block_invoke_2
+ ___57+[AAAccessoryFeatureFlagConfiguration createQueryMessage]_block_invoke
+ ___57-[AAControllerSharedXPCManager _activateSharedConnection]_block_invoke
+ ___58-[AAController _setFeatureFlagMessageReceived:fromDevice:]_block_invoke
+ ___58-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]_block_invoke
+ ___58-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]_block_invoke_2
+ ___58-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]_block_invoke_2.cold.1
+ ___59-[AASensorService sendPTEventToAccessory:value:completion:]_block_invoke
+ ___60-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke
+ ___60-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke.cold.1
+ ___60-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke_2
+ ___60-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke_2.cold.1
+ ___61-[AAController requestAllAADeviceInfosWithCompletionHandler:]_block_invoke
+ ___61-[AAController requestAllAADeviceInfosWithCompletionHandler:]_block_invoke.cold.1
+ ___61-[AAControllerSharedXPCManager _handleConnectionInterruption]_block_invoke
+ ___61-[AAControllerSharedXPCManager _handleConnectionInterruption]_block_invoke_2
+ ___61-[AAControllerSharedXPCManager _handleConnectionInvalidation]_block_invoke
+ ___62-[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:]_block_invoke
+ ___62-[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:]_block_invoke.cold.1
+ ___62-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke
+ ___62-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke.cold.1
+ ___62-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke.cold.2
+ ___62-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke.cold.3
+ ___62-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke_2
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke.cold.1
+ ___62-[AAControllerSharedXPCManager registerController:completion:]_block_invoke.cold.2
+ ___68-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke
+ ___68-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke.cold.1
+ ___68-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke_2
+ ___68-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke_2.cold.1
+ ___70-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]_block_invoke
+ ___72-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke
+ ___72-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke.cold.1
+ ___72-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke_2
+ ___72-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke_2.cold.1
+ ___72-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke_3
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke.cold.1
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke_2
+ ___74-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke_3
+ ___75-[AAController sendPTEventMessage:destinationIdentifier:completionHandler:]_block_invoke
+ ___75-[AAController sendPTEventMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2
+ ___75-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2.cold.1
+ ___79-[AAController sendFeatureFlagMessage:destinationIdentifier:completionHandler:]_block_invoke
+ ___79-[AAController sendFeatureFlagMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke.cold.1
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_2
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_2.cold.1
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_3
+ ___88-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_3.cold.1
+ ____addDefaultRules_block_invoke
+ ___block_descriptor_32_e5_B8?0l
+ ___block_descriptor_40_e8_32bs_e20_v20?0C8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e31_v28?0C8"NSDate"12"NSError"20ls32l8
+ ___block_descriptor_40_e8_32bs_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.120
+ ___block_literal_global.140
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.370
+ ___block_literal_global.42
+ _createQueryMessage.onceToken
+ _createQueryMessage.result
+ _defaultRules.onceToken
+ _defaultRules.rules
+ _dispatch_after
+ _dispatch_time
+ _gLogCategory_AA3PDeviceRoutingControl
+ _gLogCategory_AAAccessoryFeatureFlagConfiguration
+ _gLogCategory_AAAccessoryFeatureFlagRules
+ _gLogCategory_AAControllerSharedXPCManager
+ _gLogCategory_AAHeadphoneActivityProvider
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_activateSharedConnection
+ _objc_msgSend$_applyConfigurationUpdate:
+ _objc_msgSend$_distributeXPCMessage:
+ _objc_msgSend$_ensureSharedConnectionWithCompletion:
+ _objc_msgSend$_handleActivationReply:
+ _objc_msgSend$_handleConnectionInterruption
+ _objc_msgSend$_handleConnectionInvalidation
+ _objc_msgSend$_handleXPCEvent:
+ _objc_msgSend$_invalidateConnection
+ _objc_msgSend$_isConfigurationUpdateMessageValid:
+ _objc_msgSend$_processPendingMessages
+ _objc_msgSend$_registerWithSharedManager:
+ _objc_msgSend$_requestAllAADeviceInfosWithCompletionHandler:
+ _objc_msgSend$_sendMessage:controller:queue:replyHandler:
+ _objc_msgSend$_sendPTEventToAccessory:value:completion:
+ _objc_msgSend$_setFeatureFlagMessageReceived:fromDevice:
+ _objc_msgSend$activateHeadphoneActivityProvider:completion:
+ _objc_msgSend$addRuleForFeatureID:stateDeterminer:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$appendMessageToBuffer:
+ _objc_msgSend$colorCodeBest
+ _objc_msgSend$colorFlags
+ _objc_msgSend$connectedServices
+ _objc_msgSend$containsObject:
+ _objc_msgSend$coreID
+ _objc_msgSend$date
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$deviceInfoChangeHandler
+ _objc_msgSend$deviceManagerFetchAccessoryFeatureFlagConfiguration:
+ _objc_msgSend$deviceManagerFetchAudioAccessoryDeviceForIdentifier:deviceHandler:
+ _objc_msgSend$featureFlags
+ _objc_msgSend$featureID
+ _objc_msgSend$getConversationAwarenessStateForDeviceAddress:btAddress:completion:
+ _objc_msgSend$getSleepStateForDeviceAddress:btAddress:completion:
+ _objc_msgSend$headphoneActivityProviderActivate:completion:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithFeatureID:coreID:state:payload:
+ _objc_msgSend$interruptionHandler
+ _objc_msgSend$invalidateHeadphoneActivityProvider:completion:
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$messageSize
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$payloadGenerator
+ _objc_msgSend$productColorAssetExists:withColor:
+ _objc_msgSend$productHasColors:isCase:
+ _objc_msgSend$registerController:completion:
+ _objc_msgSend$reportLowBatteryFromMain
+ _objc_msgSend$sendMessage:controller:queue:replyHandler:
+ _objc_msgSend$sensorServiceSendPTEvent:value:completion:
+ _objc_msgSend$set3PDeviceInEarState:inEarStatePrimary:inEarStateSecondary:
+ _objc_msgSend$set3PDeviceProperty:property:value:
+ _objc_msgSend$setLastSeenConnectedOnHeadTime:
+ _objc_msgSend$setPayloadGenerator:
+ _objc_msgSend$setSmartRoutingVersion:
+ _objc_msgSend$setStateDeterminer:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$smartRoutingVersion
+ _objc_msgSend$stateDeterminer
+ _objc_msgSend$unregisterController:
+ _objc_msgSend$unsignedCharValue
+ _sharedManager.sOnceToken
+ _sharedManager.sSharedManager
+ _xpc_array_get_count
+ _xpc_copy
- +[AAAssetHelper _productColorAssetExists:withColor:]
- -[AAController _activateXPC:]
- -[AAController _activateXPC:].cold.1
- -[AAController _activateXPCCompleted:]
- -[AAController _activateXPCCompleted:].cold.1
- -[AAController _activateXPCCompleted:].cold.2
- -[AAController _activate]
- -[AAController _ensureXPCStarted]
- -[AAController coreBluetoothInternalFlag]
- -[AAController setCoreBluetoothInternalFlag:]
- -[AAController xpcReceivedMessage:].cold.2
- -[AAController xpcReceivedMessage:].cold.3
- GCC_except_table13
- GCC_except_table21
- GCC_except_table49
- _OBJC_IVAR_$_AAController._activateCompletion
- _OBJC_IVAR_$_AAController._coreBluetoothInternalFlag
- _OBJC_IVAR_$_AAController._xpcCnx
- ___29-[AAController _activateXPC:]_block_invoke
- ___33-[AAController _ensureXPCStarted]_block_invoke
- ___38-[AAController _activateXPCCompleted:]_block_invoke
- ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
- ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_literal_global.116
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.366
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_activateXPCCompleted:
- _objc_msgSend$_productColorAssetExists:withColor:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
- _xpc_connection_copy_invalidation_reason
- _xpc_dictionary_get_array
CStrings:
+ "### ### getConversationAwarenessStateForDeviceAddress failed: %@, %@"
+ "### ### getSleepStateForDeviceAddress failed: %@, %@"
+ "### Failed to fetch accessory feature flag configuration: %{error}"
+ "### Registration with manager failed: CID 0x%X, %@"
+ "### Requesting all AADeviceInfo failed with error: %@"
+ "### SetInEarState XPC error: %{error}"
+ "### SetInEarState failed to start XPC"
+ "### SetInEarState no XPC"
+ "### SetProperty XPC error: %{error}"
+ "### SetProperty failed to start XPC"
+ "### SetProperty no XPC"
+ "### XPC receive Set Feature Flag message failed: %@"
+ "### fetchAccessoryFeatureFlagConfigurations failed with XPC %{error}"
+ "### fetchAccessoryFeatureFlagConfigurations failed with XPC error: %{error}"
+ "### getConversationAwarenessStateForDeviceAddress failed"
+ "### getSleepStateForDeviceAddress failed"
+ "### sendPTEventToAccessory Error: %{error}"
+ "### sendPTEventToAccessory XPC Error: %{error}"
+ "-[AA3PDeviceRoutingControl _handleServerDied]_block_invoke"
+ "-[AA3PDeviceRoutingControl _interrupted]"
+ "-[AA3PDeviceRoutingControl _invalidated]"
+ "-[AA3PDeviceRoutingControl _reportError:]"
+ "-[AA3PDeviceRoutingControl invalidate]_block_invoke"
+ "-[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:]"
+ "-[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:]_block_invoke"
+ "-[AA3PDeviceRoutingControl setProperty:value:]"
+ "-[AA3PDeviceRoutingControl setProperty:value:]_block_invoke"
+ "-[AAAccessoryFeatureFlagConfiguration _applyConfigurationUpdate:]"
+ "-[AAAccessoryFeatureFlagConfiguration _isConfigurationUpdateMessageValid:]"
+ "-[AAAccessoryFeatureFlagRules applyRulesToAccessory:]"
+ "-[AAController _registerWithSharedManager:]"
+ "-[AAController _registerWithSharedManager:]_block_invoke"
+ "-[AAController _requestAllAADeviceInfosWithCompletionHandler:]"
+ "-[AAController _requestAllAADeviceInfosWithCompletionHandler:]_block_invoke"
+ "-[AAController _setFeatureFlagMessageReceived:fromDevice:]"
+ "-[AAController _setFeatureFlagMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController activateWithCompletion:]"
+ "-[AAController requestAllAADeviceInfosWithCompletionHandler:]_block_invoke"
+ "-[AAController sendFeatureFlagMessage:destinationIdentifier:completionHandler:]_block_invoke"
+ "-[AAController sendPTEventMessage:destinationIdentifier:completionHandler:]_block_invoke"
+ "-[AAControllerSharedXPCManager _activateSharedConnection]"
+ "-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]"
+ "-[AAControllerSharedXPCManager _handleActivationReply:]"
+ "-[AAControllerSharedXPCManager _handleConnectionInterruption]"
+ "-[AAControllerSharedXPCManager _handleXPCEvent:]"
+ "-[AAControllerSharedXPCManager _processPendingMessages]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2"
+ "-[AAControllerSharedXPCManager init]"
+ "-[AAControllerSharedXPCManager invalidate]_block_invoke"
+ "-[AAControllerSharedXPCManager registerController:completion:]_block_invoke"
+ "-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke"
+ "-[AAControllerSharedXPCManager unregisterController:]_block_invoke"
+ "-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]"
+ "-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke"
+ "-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:]_block_invoke_2"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]_block_invoke"
+ "-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:]_block_invoke_2"
+ "-[AAHeadphoneActivityProvider _activate:]"
+ "-[AAHeadphoneActivityProvider _activate:]_block_invoke"
+ "-[AAHeadphoneActivityProvider _activateDirect:]"
+ "-[AAHeadphoneActivityProvider _activateXPC:reactivate:]"
+ "-[AAHeadphoneActivityProvider _activateXPC:reactivate:]_block_invoke"
+ "-[AAHeadphoneActivityProvider _interrupted]"
+ "-[AAHeadphoneActivityProvider _invalidated]"
+ "-[AAHeadphoneActivityProvider _reportError:]"
+ "-[AAHeadphoneActivityProvider activateWithCompletion:]_block_invoke"
+ "-[AAHeadphoneActivityProvider conversationAwarenessStateUpdated:forDeviceAddress:]"
+ "-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke"
+ "-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_2"
+ "-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:]_block_invoke_3"
+ "-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke"
+ "-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke_2"
+ "-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:]_block_invoke_3"
+ "-[AAHeadphoneActivityProvider invalidate]_block_invoke"
+ "-[AAHeadphoneActivityProvider sleepStateUpdated:sleepTimestamp:forDeviceAddress:]"
+ "-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke"
+ "-[AASensorService _sendPTEventToAccessory:value:completion:]_block_invoke_2"
+ "<%@ featureID:0x%x state:%d coreID:0x%x payloadLength:%d>"
+ "@\"NSMutableSet\""
+ "@24@0:8^@16"
+ "@36@0:8C16C20B24@28"
+ "AA3PDeviceRoutingControl"
+ "AA3PDeviceRoutingControl, CID 0x%X address %@"
+ "AAAccessoryFeatureFlagConfiguration"
+ "AAAccessoryFeatureFlagEntry"
+ "AAAccessoryFeatureFlagRules"
+ "AAControllerSharedXPCManager"
+ "AAHeadphoneActivityProvider"
+ "Active"
+ "AirFlagsDebug"
+ "Already registered with manager: CID 0x%X"
+ "B24@0:8I16B20"
+ "B8@?0"
+ "BTMagicPairingSettings[%@]: Name(%lu): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, CR: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
+ "CID 0x%X, reporting conversation awareness state update %d for device %@"
+ "CID 0x%X, reporting sleep state update %d for sleepTimestamp %@ device %@"
+ "Controller not registered"
+ "Empty message"
+ "Entry for featureID:0x%x requires update from %@ to %@"
+ "GAAD"
+ "Manager invalidated"
+ "No XPC connection"
+ "No audio accessory device array"
+ "No conversation awareness state update handler set for client ID 0x%X"
+ "No deviceInfoChangeHandler set on AAController"
+ "No rule found for featureID:0x%x"
+ "No sleep state update handler set for client ID 0x%X"
+ "NotActive"
+ "Offset (%u) + payloadLength (%u) exceeds length of message (%u)"
+ "Offset (%u) + sizeof(payloadLength) (%lu) exceeds length of message (%u)"
+ "Offset (%u) + sizeof(stateAndFeatureID) (%lu) exceeds length of message (%u)"
+ "PassthroughAlert"
+ "PassthroughConfirm"
+ "PassthroughEnd"
+ "Received feature flag entry %@ for %@"
+ "Registered with manager: CID 0x%X"
+ "Registering with shared manager: CID 0x%X"
+ "Requesting all AADeviceInfo"
+ "Retrieved %d AADeviceInfo objects, calling deviceInfoChangeHandler for each"
+ "Set Feature Flag message received: source %@, data <%@>"
+ "SetFeatureFlag"
+ "SetInEarState CID 0x%X inEarStatePrimary %s inEarStateSecondary %s"
+ "SetProperty CID 0x%X property %@ value %@"
+ "SleepDetected"
+ "SleepInterrupted"
+ "Start2"
+ "State for featureID:0x%x matches intended state:%d"
+ "T@\"NSData\",&,N,V_crownRotationDirection"
+ "T@\"NSData\",R,N,V_payload"
+ "T@\"NSDate\",C,N,V_lastSeenConnectedOnHeadTime"
+ "T@\"NSDictionary\",C,V_featureFlags"
+ "T@\"NSMutableArray\",&,N,V_pendingMessages"
+ "T@\"NSMutableSet\",&,N,V_registeredControllers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_managerQueue"
+ "T@?,C,N,V_conversationAwarenessStateUpdateHandler"
+ "T@?,C,N,V_payloadGenerator"
+ "T@?,C,N,V_setFeatureFlagMessageHandler"
+ "T@?,C,N,V_sleepStateUpdateHandler"
+ "T@?,C,N,V_stateDeterminer"
+ "TB,N,V_connectionActive"
+ "TB,N,V_invalidateCalled"
+ "TB,R,N,V_state"
+ "TC,N,V_color"
+ "TC,N,V_smartRoutingVersion"
+ "TC,R,N,V_coreID"
+ "TC,R,N,V_featureID"
+ "TI,N,V_headphoneActivityProviderFlags"
+ "Unsupported version: %d"
+ "Updating feature flag entry from %@ to %@ for %@"
+ "[%p] ### Register controller failed: %@"
+ "[%p] ### Shared XPC connection interrupted"
+ "[%p] ### Shared XPC connection invalidated"
+ "[%p] ### Shared connection activation failed: %@"
+ "[%p] ### XPC error: %@, %@"
+ "[%p] AAControllerSharedXPCManager initialized"
+ "[%p] Activating shared XPC connection"
+ "[%p] Attempting to reestablish connection after interruption"
+ "[%p] Establishing shared XPC connection"
+ "[%p] Invalidating AAControllerSharedXPCManager"
+ "[%p] No more registered controllers, keeping connection alive for reuse"
+ "[%p] Processing %lu pending messages"
+ "[%p] Queued message for controller %@, pending count: %lu"
+ "[%p] Received XPC reply for controller %@: %@"
+ "[%p] Registered controller %@, total: %lu"
+ "[%p] Sending XPC message for controller %@: %@"
+ "[%p] Shared XPC connection activated successfully"
+ "[%p] Unregistered controller %@, remaining: %lu"
+ "[%p] XPC event: %@"
+ "_FeatureFlagRule"
+ "_activateSharedConnection"
+ "_applyConfigurationUpdate:"
+ "_connectionActive"
+ "_connectionEstablished"
+ "_conversationAwarenessStateUpdateHandler"
+ "_coreID"
+ "_distributeXPCMessage:"
+ "_ensureSharedConnectionWithCompletion:"
+ "_featureFlags"
+ "_featureID"
+ "_handleActivationReply:"
+ "_handleConnectionInterruption"
+ "_handleConnectionInvalidation"
+ "_handleXPCEvent:"
+ "_headphoneActivityProviderFlags"
+ "_invalidateConnection"
+ "_isConfigurationUpdateMessageValid:"
+ "_lastSeenConnectedOnHeadTime"
+ "_managerQueue"
+ "_payload"
+ "_payloadGenerator"
+ "_pendingActivations"
+ "_pendingMessages"
+ "_processPendingMessages"
+ "_registerWithSharedManager:"
+ "_registeredControllers"
+ "_registeredWithManager"
+ "_requestAllAADeviceInfosWithCompletionHandler:"
+ "_rulesByFeatureID"
+ "_sendMessage:controller:queue:replyHandler:"
+ "_sendPTEventToAccessory:value:completion:"
+ "_setFeatureFlagMessageHandler"
+ "_setFeatureFlagMessageReceived:fromDevice:"
+ "_sharedXPCConnection"
+ "_sleepStateUpdateHandler"
+ "_smartRoutingVersion"
+ "_stateDeterminer"
+ "activateHeadphoneActivityProvider:completion:"
+ "addRuleForFeatureID:stateDeterminer:"
+ "addRuleForFeatureID:stateDeterminer:payloadGenerator:"
+ "appendBytes:length:"
+ "appendData:"
+ "appendMessageToBuffer:"
+ "applyRulesToAccessory:"
+ "clCd"
+ "color %u, "
+ "colorCodeBest"
+ "colorFlags"
+ "com.apple.AAControllerSharedXPCManager"
+ "connectedServices"
+ "connectionActive"
+ "containsObject:"
+ "controller"
+ "conversationAwarenessStateUpdateHandler"
+ "conversationAwarenessStateUpdated:forDeviceAddress:"
+ "coreID"
+ "createQueryMessage"
+ "createSetFeatureFlagMessage:"
+ "date"
+ "decodeObjectOfClasses:forKey:"
+ "defaultRules"
+ "deviceManagerFetchAccessoryFeatureFlagConfiguration:"
+ "deviceManagerFetchAudioAccessoryDeviceForIdentifier:deviceHandler:"
+ "featureFlags"
+ "featureID"
+ "fetchAccessoryFeatureFlagConfigurationsWithError:"
+ "fetchAudioAccessoryDeviceForIdentifier:"
+ "getConversationAwarenessStateForDeviceAddress conversationAwarenessState %s, error: %@"
+ "getConversationAwarenessStateForDeviceAddress:btAddress:completion:"
+ "getConversationAwarenessStateForDeviceAddress:completion:"
+ "getSleepStateForDeviceAddress for %@"
+ "getSleepStateForDeviceAddress sleepState %s, sleepDetectionTimestamp %@, error: %@"
+ "getSleepStateForDeviceAddress:btAddress:completion:"
+ "getSleepStateForDeviceAddress:completion:"
+ "handleUpdate:"
+ "hapf"
+ "headphoneActivityProviderActivate:completion:"
+ "headphoneActivityProviderFlags"
+ "initWithCapacity:"
+ "initWithFeatureID:coreID:state:payload:"
+ "invalidateCalled"
+ "invalidateHeadphoneActivityProvider:completion:"
+ "lastSeenConnectedOnHeadTime"
+ "lscoht"
+ "lst on head '%@', "
+ "managerQueue"
+ "messageSize"
+ "numberWithUnsignedChar:"
+ "objectForKey:"
+ "payload"
+ "payloadGenerator"
+ "pendingMessages"
+ "productColorAssetExists:withColor:"
+ "productHasColors:isCase:"
+ "queue"
+ "registerController:completion:"
+ "registeredControllers"
+ "replyHandler"
+ "reportLowBatteryFromMain"
+ "request"
+ "requestAllAADeviceInfosWithCompletionHandler:"
+ "sendFeatureFlagMessage message to destination %@ (len=%llu)"
+ "sendFeatureFlagMessage:destinationIdentifier:completionHandler:"
+ "sendMessage:controller:queue:replyHandler:"
+ "sendPTEventMessage message to destination %@"
+ "sendPTEventMessage:destinationIdentifier:completionHandler:"
+ "sendPTEventToAccessory:value:completion:"
+ "sensorServiceSendPTEvent:value:completion:"
+ "set3PDeviceInEarState:inEarStatePrimary:inEarStateSecondary:"
+ "set3PDeviceProperty:property:value:"
+ "setConnectionActive:"
+ "setConversationAwarenessStateUpdateHandler:"
+ "setFeatureFlagMessageHandler"
+ "setFeatureFlags:"
+ "setHeadphoneActivityProviderFlags:"
+ "setInEarState:inEarStateSecondary:"
+ "setInvalidateCalled:"
+ "setLastSeenConnectedOnHeadTime:"
+ "setManagerQueue:"
+ "setPayloadGenerator:"
+ "setPendingMessages:"
+ "setProperty:value:"
+ "setRegisteredControllers:"
+ "setSetFeatureFlagMessageHandler:"
+ "setSleepStateUpdateHandler:"
+ "setSmartRoutingVersion:"
+ "setStateDeterminer:"
+ "setWithArray:"
+ "sharedManager"
+ "sleepStateUpdateHandler"
+ "sleepStateUpdated:sleepTimestamp:forDeviceAddress:"
+ "smartRoutingVersion"
+ "srVer %s, "
+ "srVs"
+ "stateDeterminer"
+ "sync fetch for AudioAccessoryDevice btAddress: %@ returned: %@ "
+ "unregisterController:"
+ "unsignedCharValue"
+ "v20@?0C8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8i16i20"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v28@0:8C16@\"NSString\"20"
+ "v28@0:8C16@20"
+ "v28@0:8C16@?20"
+ "v28@?0C8@\"NSDate\"12@\"NSError\"20"
+ "v32@0:8@\"AA3PDeviceRoutingControl\"16i24i28"
+ "v32@0:8@\"AAHeadphoneActivityProvider\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16i24i28"
+ "v36@0:8@\"NSString\"16C24@?<v@?@\"NSError\">28"
+ "v36@0:8C16@\"NSDate\"20@\"NSString\"28"
+ "v36@0:8C16@20@28"
+ "v36@0:8C16@?20@?28"
+ "v40@0:8@\"AA3PDeviceRoutingControl\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSDate\"@\"NSError\">32"
+ "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSError\">32"
+ "v48@0:8@16@24@32@?40"
+ "\xf0/"
- "### Activate failed: CID 0x%X, %@"
- "### Invalidated unexpectedly for reason %s"
- "### XPC error: %@, %@"
- "-[AAController _activateXPC:]"
- "-[AAController _activateXPCCompleted:]"
- "-[AAController _activate]"
- "Activate: CID 0x%X"
- "Activated: CID 0x%X"
- "BTMagicPairingSettings[%@]: Name(%lu): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
- "Re-activate: CID 0x%X"
- "TI,N,V_coreBluetoothInternalFlag"
- "_activateXPCCompleted:"
- "_coreBluetoothInternalFlag"
- "_productColorAssetExists:withColor:"
- "coreBluetoothInternalFlag"
- "setCoreBluetoothInternalFlag:"
- "\xf0."

```

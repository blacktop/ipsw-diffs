## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-  __TEXT.__text: 0x3d7b4
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x4140
-  __TEXT.__objc_methlist: 0x2bc4
-  __TEXT.__cstring: 0x322b
-  __TEXT.__objc_classname: 0x792
-  __TEXT.__objc_methtype: 0x1396
-  __TEXT.__const: 0x320
-  __TEXT.__objc_methname: 0x5868
-  __TEXT.__oslogstring: 0x7425
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0xb28
-  __DATA_CONST.__const: 0xbc8
-  __DATA_CONST.__cfstring: 0x3900
-  __DATA_CONST.__objc_classlist: 0x1d8
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__text: 0x41c70
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0x4920
+  __TEXT.__objc_methlist: 0x314c
+  __TEXT.__cstring: 0x354b
+  __TEXT.__objc_classname: 0x855
+  __TEXT.__objc_methtype: 0x1537
+  __TEXT.__const: 0x338
+  __TEXT.__objc_methname: 0x62e3
+  __TEXT.__oslogstring: 0x7924
+  __TEXT.__gcc_except_tab: 0x340
+  __TEXT.__unwind_info: 0xc78
+  __DATA_CONST.__const: 0xcf8
+  __DATA_CONST.__cfstring: 0x3b60
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__objc_arraydata: 0xcd0
-  __DATA_CONST.__objc_arrayobj: 0x558
-  __DATA_CONST.__objc_intobj: 0xd80
-  __DATA_CONST.__objc_doubleobj: 0x60
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_arraydata: 0xd70
+  __DATA_CONST.__objc_arrayobj: 0x5a0
+  __DATA_CONST.__objc_intobj: 0xf00
+  __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x6d50
-  __DATA.__objc_selrefs: 0x1520
-  __DATA.__objc_ivar: 0x2c8
-  __DATA.__objc_data: 0x1270
-  __DATA.__data: 0x408
-  __DATA.__bss: 0x220
+  __DATA.__objc_const: 0x79f0
+  __DATA.__objc_selrefs: 0x1778
+  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_data: 0x1400
+  __DATA.__data: 0x528
+  __DATA.__bss: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1350
-  Symbols:   265
-  CStrings:  2766
+  Functions: 1492
+  Symbols:   271
+  CStrings:  2977
 
Sections:
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _BIThermalPredictionErrorDomain
+ _OBJC_CLASS_$_BIThermalPredictionOutput
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSXPCConnection
+ _objc_storeWeak
CStrings:
+ ")"
+ "@\"<TLCPredictorDelegate>\""
+ "@\"BIThermalPredictionOutput\""
+ "@\"NSError\""
+ "@\"NSHashTable\""
+ "@\"NSMapTable\""
+ "@\"TLCPredictor\""
+ "@\"_CDClientContext\""
+ "@32@0:8q16@24"
+ "@48@0:8d16d24d32d40"
+ "@56@0:8d16d24d32d40^@48"
+ "Accepted connection from pid %d"
+ "Attempted to register nil client"
+ "Attempted to unregister nil client"
+ "BIThermalPredictionClientProtocol"
+ "BIThermalPredictionProtocol"
+ "Battery level %u not in target range for TLC prediction"
+ "BatteryTemperatureReader returning value %@"
+ "Cleaned up stale clients, %lu valid clients remain"
+ "Confidence"
+ "Connection from pid %d interrupted"
+ "Connection from pid %d invalidated"
+ "Could not load battery_thermals_tlc.mlmodelc in the bundle resource"
+ "CurrentSOC"
+ "CurrentTemp"
+ "Device is plugged in, initializing session"
+ "Device is plugged out, reseting session"
+ "Device unplugged, invalidating TLC prediction"
+ "FF: TLCPredictor %s"
+ "Failed to create feature provider: %@"
+ "Failed to load ML model %@"
+ "Invalid data startSOC=%.2f, startTemp=%.2f°C, currentSOC=%.2f, currentTemp=%.2f°C"
+ "Is PluggedIn %ld "
+ "ML model not loaded, cannot run prediction"
+ "ML model output: %@"
+ "ML model prediction failed: %@"
+ "ML prediction: willHitTLC=%@, confidence=%.2f, method=MLModel"
+ "ModelMethod"
+ "ModelVersion"
+ "Rejected connection from pid %d"
+ "Result"
+ "Running TLC prediction: startSOC=%.2f, startTemp=%.2f°C, currentSOC=%.2f, currentTemp=%.2f°C"
+ "T@\"<TLCPredictorDelegate>\",W,N,V_delegate"
+ "T@\"BIThermalPredictionOutput\",&,V_storedPrediction"
+ "T@\"MLModel\",&,N,V_mlModel"
+ "T@\"NSDictionary\",&,N,V_classProbability"
+ "T@\"NSError\",&,V_storedError"
+ "T@\"NSHashTable\",&,N,V_registeredClients"
+ "T@\"NSMapTable\",&,N,V_connectionToClientMap"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_clientNotificationQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"TLCPredictor\",&,N,V_predictor"
+ "T@\"_CDClientContext\",&,N,V_context"
+ "T@\"_CDContextualChangeRegistration\",&,N,V_pluggedInReg"
+ "T@\"_CDContextualChangeRegistration\",&,N,V_triggerReg"
+ "TB,N,V_isCurrentlyPluggedIn"
+ "TB,N,V_started"
+ "TLCPrediction"
+ "TLCPredictor"
+ "TLCPredictor ML model loaded successfully"
+ "TLCPredictor context store registration fired with registrationID and info: %@, %@"
+ "TLCPredictor started"
+ "TLCPredictorDelegate"
+ "Td,N,V_CurrentSOC"
+ "Td,N,V_CurrentTemp"
+ "Td,N,V_sessionStartSOC"
+ "Td,N,V_sessionStartTemp"
+ "ThermalPredictionService"
+ "ThermalPredictionService started"
+ "Tq,N,V_sessionTLCPredicted"
+ "TriggerLevel"
+ "Unable to get battery properties: %d"
+ "Using fallback prediction: willHitTLC=%d, confidence=%.2f, method=Fallback"
+ "_CurrentSOC"
+ "_CurrentTemp"
+ "_classProbability"
+ "_clientNotificationQueue"
+ "_connectionToClientMap"
+ "_delegate"
+ "_isCurrentlyPluggedIn"
+ "_mlModel"
+ "_pluggedInReg"
+ "_predictor"
+ "_registeredClients"
+ "_sessionStartSOC"
+ "_sessionStartTemp"
+ "_sessionTLCPredicted"
+ "_started"
+ "_storedError"
+ "_storedPrediction"
+ "_triggerReg"
+ "batteryExternalConnectedKey"
+ "battery_thermals_tlc"
+ "battery_thermals_tlcInput"
+ "battery_thermals_tlcOutput"
+ "classProbability"
+ "cleanupStaleClients"
+ "clientNotificationQueue"
+ "com.apple.batteryintelligence.thermal.reconnect"
+ "com.apple.batteryintelligenced.pluggedInState"
+ "com.apple.batteryintelligenced.thermalprediction"
+ "com.apple.batteryintelligenced.thermalprediction-read"
+ "com.apple.batteryintelligenced.thermalpredictionservice"
+ "com.apple.batteryintelligenced.thermalpredictionservice.notifications"
+ "com.apple.batteryintelligenced.tlcpredictor"
+ "com.apple.batteryintelligenced.tlcpredictor.contextstore-handler"
+ "com.apple.batteryintelligenced.tlcpredictor.contextstore-registration"
+ "com.apple.batteryintelligenced.tlcpredictor.setUpContextStoreRegistration"
+ "connectionToClientMap"
+ "createPredictionOutputWithResults:"
+ "currentBatteryTemperature"
+ "currentConnection"
+ "currentError"
+ "currentPrediction"
+ "delegate"
+ "dictionaryValue"
+ "didReceivePredictionUpdate:error:"
+ "fallbackPredictionWithInputs:"
+ "featureValueWithDictionary:error:"
+ "featureValueWithDouble:"
+ "featureValueWithInt64:"
+ "handlePredictionTriggerWithBatteryLevels:"
+ "initInternal"
+ "initWithCurrentSOC:CurrentTemp:sessionStartSOC:sessionStartTemp:"
+ "initWithSessionTLCPredicted:classProbability:"
+ "int64Value"
+ "invalidatePredictionWithError:"
+ "isCurrentlyPluggedIn"
+ "isPluggedInWithContext:"
+ "keyPathForPluginStatus"
+ "loadMLModel"
+ "pluggedInReg"
+ "predicateForChangeAtKeyPath:"
+ "predictTLCWithHandler:"
+ "predictionFromCurrentSOC:CurrentTemp:sessionStartSOC:sessionStartTemp:error:"
+ "predictor"
+ "predictor:didUpdatePrediction:"
+ "recordPredictionResult:currentSOC:"
+ "registerForUpdatesWithClient:"
+ "registeredClients"
+ "runMLModelWithInputs:"
+ "runPredictionWithCurrentTemp:currentSOC:startTemp:startSOC:"
+ "sessionStartSOC"
+ "sessionStartTemp"
+ "sessionTLCPredicted"
+ "setClassProbability:"
+ "setClientNotificationQueue:"
+ "setConnectionToClientMap:"
+ "setCurrentSOC:"
+ "setCurrentTemp:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIsCurrentlyPluggedIn:"
+ "setMlModel:"
+ "setPluggedInReg:"
+ "setPredictor:"
+ "setRegisteredClients:"
+ "setRemoteObjectInterface:"
+ "setSessionStartSOC:"
+ "setSessionStartTemp:"
+ "setSessionTLCPredicted:"
+ "setStarted:"
+ "setStoredError:"
+ "setStoredPrediction:"
+ "setTriggerReg:"
+ "setWillHitTLC:"
+ "started"
+ "stop"
+ "storedError"
+ "storedPrediction"
+ "triggerReg"
+ "triggerTLCPredictionForCurrentState"
+ "unregisterClient:"
+ "updateSession"
+ "v24@0:8@\"<BIThermalPredictionClientProtocol>\"16"
+ "v24@0:8@?<v@?@\"BIThermalPredictionOutput\"@\"NSError\">16"
+ "v32@0:8@\"BIThermalPredictionOutput\"16@\"NSError\"24"
+ "v32@0:8@16@\"BIThermalPredictionOutput\"24"
+ "v32@0:8@16d24"
+ "v48@0:8d16d24d32d40"
+ "weakObjectsHashTable"
+ "weakToWeakObjectsMapTable"

```

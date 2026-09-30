## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3405.23.2.0.0
-  __TEXT.__text: 0x96fb1c
+3406.11.1.0.0
+  __TEXT.__text: 0x970e24
   __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0xcd864
+  __TEXT.__objc_methlist: 0xcda04
   __TEXT.__const: 0x11830
-  __TEXT.__cstring: 0x76eb7
+  __TEXT.__cstring: 0x76f59
   __TEXT.__constg_swiftt: 0x6220
   __TEXT.__swift5_typeref: 0x1864
   __TEXT.__swift5_builtin: 0x38cc

   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x29930
+  __TEXT.__unwind_info: 0x29980
   __TEXT.__eh_frame: 0x1f98
-  __TEXT.__objc_classname: 0x1525e
-  __TEXT.__objc_methname: 0x11b3fb
-  __TEXT.__objc_methtype: 0x27232
-  __TEXT.__objc_stubs: 0x672a0
-  __DATA_CONST.__got: 0x4b80
-  __DATA_CONST.__const: 0x33738
-  __DATA_CONST.__objc_classlist: 0x4a48
+  __TEXT.__objc_classname: 0x1527d
+  __TEXT.__objc_methname: 0x11b6a4
+  __TEXT.__objc_methtype: 0x272a6
+  __TEXT.__objc_stubs: 0x673c0
+  __DATA_CONST.__got: 0x4b88
+  __DATA_CONST.__const: 0x33800
+  __DATA_CONST.__objc_classlist: 0x4a50
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35538
+  __DATA_CONST.__objc_selrefs: 0x355d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7330
+  __DATA_CONST.__objc_superrefs: 0x7338
   __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x20b00
-  __AUTH_CONST.__cfstring: 0x673a0
-  __AUTH_CONST.__objc_const: 0x1167e0
+  __AUTH_CONST.__cfstring: 0x67460
+  __AUTH_CONST.__objc_const: 0x116a10
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0xe448
-  __DATA.__objc_ivar: 0xdd8c
+  __AUTH.__objc_data: 0xe498
+  __DATA.__objc_ivar: 0xdda8
   __DATA.__data: 0x1fb0
   __DATA.__bss: 0x18300
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E8C4B922-2EAD-38D5-A3E1-7FD668F07187
-  Functions: 74418
-  Symbols:   185198
-  CStrings:  76222
+  UUID: 3BB8BAC1-13DF-3BBA-A156-E13043CB7719
+  Functions: 74454
+  Symbols:   185291
+  CStrings:  76267
 
Symbols:
+ -[GATSchemaGATClientEvent deleteModelAgentCaptured]
+ -[GATSchemaGATClientEvent hasModelAgentCaptured]
+ -[GATSchemaGATClientEvent modelAgentCaptured]
+ -[GATSchemaGATClientEvent setHasModelAgentCaptured:]
+ -[GATSchemaGATClientEvent setModelAgentCaptured:]
+ -[GATSchemaGATModelAgentCaptured deleteRequestedAgent]
+ -[GATSchemaGATModelAgentCaptured deleteSettingsAgent]
+ -[GATSchemaGATModelAgentCaptured dictionaryRepresentation]
+ -[GATSchemaGATModelAgentCaptured hasRequestedAgent]
+ -[GATSchemaGATModelAgentCaptured hasSettingsAgent]
+ -[GATSchemaGATModelAgentCaptured hash]
+ -[GATSchemaGATModelAgentCaptured initWithDictionary:]
+ -[GATSchemaGATModelAgentCaptured initWithJSON:]
+ -[GATSchemaGATModelAgentCaptured isEqual:]
+ -[GATSchemaGATModelAgentCaptured jsonData]
+ -[GATSchemaGATModelAgentCaptured readFrom:]
+ -[GATSchemaGATModelAgentCaptured requestedAgent]
+ -[GATSchemaGATModelAgentCaptured setHasRequestedAgent:]
+ -[GATSchemaGATModelAgentCaptured setHasSettingsAgent:]
+ -[GATSchemaGATModelAgentCaptured setRequestedAgent:]
+ -[GATSchemaGATModelAgentCaptured setSettingsAgent:]
+ -[GATSchemaGATModelAgentCaptured settingsAgent]
+ -[GATSchemaGATModelAgentCaptured writeTo:]
+ -[GATSchemaGATModelAgentCaptured(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHDeviceDynamicContext deleteIsSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext hasIsSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext isSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext setHasIsSoundAnalysisEnabled:]
+ -[ORCHSchemaORCHDeviceDynamicContext setIsSoundAnalysisEnabled:]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered deleteOfferedAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered hasOfferedAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered offeredAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered setHasOfferedAgent:]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered setOfferedAgent:]
+ OBJC_IVAR_$_GATSchemaGATClientEvent._modelAgentCaptured
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._has
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._requestedAgent
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._settingsAgent
+ OBJC_IVAR_$_ORCHSchemaORCHDeviceDynamicContext._isSoundAnalysisEnabled
+ OBJC_IVAR_$_POMMESSchemaPOMMESKnowledgeFallbackOffered._offeredAgent
+ _GATSchemaGATModelAgentCapturedReadFrom
+ _OBJC_CLASS_$_GATSchemaGATModelAgentCaptured
+ _OBJC_IVAR_$_GATSchemaGATClientEvent._hasModelAgentCaptured
+ _OBJC_METACLASS_$_GATSchemaGATModelAgentCaptured
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATModelAgentCaptured(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATModelAgentCaptured
+ __OBJC_$_PROP_LIST_GATSchemaGATModelAgentCaptured
+ __OBJC_CLASS_RO_$_GATSchemaGATModelAgentCaptured
+ __OBJC_METACLASS_RO_$_GATSchemaGATModelAgentCaptured
+ _objc_msgSend$deleteModelAgentCaptured
+ _objc_msgSend$isSoundAnalysisEnabled
+ _objc_msgSend$modelAgentCaptured
+ _objc_msgSend$offeredAgent
+ _objc_msgSend$setIsSoundAnalysisEnabled:
+ _objc_msgSend$setModelAgentCaptured:
+ _objc_msgSend$setOfferedAgent:
+ _objc_msgSend$setSettingsAgent:
+ _objc_msgSend$settingsAgent
+ _qname_GATSchemaGATClientEvent_WhichEvent_Type_modelAgentCaptured
CStrings:
+ "@\"GATSchemaGATModelAgentCaptured\""
+ "FLOWAPPRESOLUTIONTYPE_NOT_SUPPORTED_INTENT"
+ "GATSchemaGATModelAgentCaptured"
+ "T@\"GATSchemaGATModelAgentCaptured\",&,N,V_modelAgentCaptured"
+ "TB,N,V_hasModelAgentCaptured"
+ "TB,N,V_isSoundAnalysisEnabled"
+ "Ti,N,V_offeredAgent"
+ "Ti,N,V_settingsAgent"
+ "_hasModelAgentCaptured"
+ "_isSoundAnalysisEnabled"
+ "_modelAgentCaptured"
+ "_offeredAgent"
+ "_settingsAgent"
+ "com.apple.aiml.siri.gat.GATClientEvent.GATModelAgentCaptured"
+ "deleteIsSoundAnalysisEnabled"
+ "deleteModelAgentCaptured"
+ "deleteOfferedAgent"
+ "deleteSettingsAgent"
+ "hasIsSoundAnalysisEnabled"
+ "hasModelAgentCaptured"
+ "hasOfferedAgent"
+ "hasSettingsAgent"
+ "isSoundAnalysisEnabled"
+ "modelAgentCaptured"
+ "offeredAgent"
+ "setHasIsSoundAnalysisEnabled:"
+ "setHasModelAgentCaptured:"
+ "setHasOfferedAgent:"
+ "setHasSettingsAgent:"
+ "setIsSoundAnalysisEnabled:"
+ "setModelAgentCaptured:"
+ "setOfferedAgent:"
+ "setSettingsAgent:"
+ "settingsAgent"
+ "{?=\"isKnowledgeFallbackConfirmationShown\"b1\"offeredAgent\"b1}"
+ "{?=\"requestedAgent\"b1\"settingsAgent\"b1}"
+ "{?=\"thermalState\"b1\"motionActivity\"b1\"timeSinceAssistantDaemonStartedInMs\"b1\"headGesturesSupported\"b1\"headGesturesEnabled\"b1\"acceptProceedGesture\"b1\"declineDismissGesture\"b1\"isWifiEnabled\"b1\"bluetoothState\"b1\"flashlightLevel\"b1\"isChatGPTEnabled\"b1\"isSoundAnalysisEnabled\"b1}"
- "{?=\"isKnowledgeFallbackConfirmationShown\"b1}"
- "{?=\"thermalState\"b1\"motionActivity\"b1\"timeSinceAssistantDaemonStartedInMs\"b1\"headGesturesSupported\"b1\"headGesturesEnabled\"b1\"acceptProceedGesture\"b1\"declineDismissGesture\"b1\"isWifiEnabled\"b1\"bluetoothState\"b1\"flashlightLevel\"b1\"isChatGPTEnabled\"b1}"

```

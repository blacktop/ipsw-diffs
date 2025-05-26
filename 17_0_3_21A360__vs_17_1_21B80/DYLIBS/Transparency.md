## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-867.2.1.0.0
-  __TEXT.__text: 0x25d8c
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x2174
-  __TEXT.__cstring: 0x1687
-  __TEXT.__oslogstring: 0x1175
+948.0.0.0.1
+  __TEXT.__text: 0x2746c
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_methlist: 0x2284
+  __TEXT.__cstring: 0x1748
+  __TEXT.__oslogstring: 0x1278
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__unwind_info: 0xc6c
+  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__unwind_info: 0xcd4
   __TEXT.__objc_classname: 0x488
-  __TEXT.__objc_methname: 0x4af6
-  __TEXT.__objc_methtype: 0x11a8
-  __TEXT.__objc_stubs: 0x39e0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0xd48
+  __TEXT.__objc_methname: 0x4d62
+  __TEXT.__objc_methtype: 0x11b7
+  __TEXT.__objc_stubs: 0x3c00
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35e0
-  __DATA_CONST.__objc_selrefs: 0x1280
-  __AUTH_CONST.__cfstring: 0x2700
+  __DATA_CONST.__objc_const: 0x3770
+  __DATA_CONST.__objc_selrefs: 0x1338
+  __AUTH_CONST.__cfstring: 0x2820
   __AUTH_CONST.__objc_const: 0x1a8
-  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x1f8
+  __DATA.__objc_classrefs: 0x200
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x1f8
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x3f8
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__const: 0xdc0
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__const: 0xe80
   __DATA_DIRTY.__objc_const: 0x1238
   __DATA_DIRTY.__objc_data: 0xbe0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1063
-  Symbols:   3710
-  CStrings:  1461
+  Functions: 1099
+  Symbols:   3832
+  CStrings:  1509
 
Symbols:
+ +[TransparencySettings cfPrefsJson]
+ +[TransparencySettings devicePlatform]
+ +[TransparencySettings jsonArrayFromPlistArray:]
+ +[TransparencySettings jsonDictFromPlistDict:]
+ +[TransparencySettings transparencyVersionStr]
+ -[KTLoggableData markExpiryDate]
+ -[KTLoggableData setMarkExpiryDate:]
+ -[KTSelfStatusResult accountKey]
+ -[KTSelfStatusResult pendingStatusChanges]
+ -[KTSelfStatusResult serverOptIn]
+ -[KTSelfStatusResult setAccountKey:]
+ -[KTSelfStatusResult setPendingStatusChanges:]
+ -[KTSelfStatusResult setServerOptIn:]
+ -[KTStatusResult pendingStatusChanges]
+ -[KTStatusResult serverOptIn]
+ -[KTStatusResult setPendingStatusChanges:]
+ -[KTStatusResult setServerOptIn:]
+ -[TransparencyAnalytics addNFSReporting:]
+ -[TransparencyAnalytics nfsObserver]
+ -[TransparencyAnalytics nfsReporting]
+ -[TransparencyAnalytics setNfsObserver:]
+ -[TransparencyDaemon maybeUpdateMonitorState]
+ -[TransparencyDaemon transparencyClearKTRegistrationData:]
+ GCC_except_table132
+ GCC_except_table73
+ GCC_except_table74
+ _CFPreferencesCopyMultiple
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_KTLoggableData._markExpiryDate
+ _OBJC_IVAR_$_KTSelfStatusResult._accountKey
+ _OBJC_IVAR_$_KTSelfStatusResult._pendingStatusChanges
+ _OBJC_IVAR_$_KTSelfStatusResult._serverOptIn
+ _OBJC_IVAR_$_KTStatusResult._pendingStatusChanges
+ _OBJC_IVAR_$_KTStatusResult._serverOptIn
+ _OBJC_IVAR_$_TransparencyAnalytics._nfsObserver
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.309
+ ___22-[KTStatus getStatus:]_block_invoke.219
+ ___22-[KTStatus getStatus:]_block_invoke.223
+ ___22-[KTStatus getStatus:]_block_invoke_2.224
+ ___26-[KTStatus getSelfStatus:]_block_invoke.230
+ ___26-[KTStatus getSelfStatus:]_block_invoke.233
+ ___26-[KTStatus getSelfStatus:]_block_invoke_2.234
+ ___38+[TransparencySettings devicePlatform]_block_invoke
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.370
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.361
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.301
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.304
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.113
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke_2
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.258
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.261
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.262
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.267
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.270
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.271
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.344
+ ___48+[TransparencySettings jsonArrayFromPlistArray:]_block_invoke
+ ___48+[TransparencySettings jsonArrayFromPlistArray:]_block_invoke_2
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.239
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.242
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.244
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.324
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.326
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.249
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.252
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.253
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.312
+ ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.329
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.335
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.315
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.364
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.341
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke_2
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.373
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.338
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.358
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.355
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.318
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.332
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.376
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.379
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.122
+ ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.126
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.382
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.367
+ ___block_descriptor_32_e46_v24?0"<transparencyd_protocol>"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
+ ___block_literal_global.107
+ ___block_literal_global.218
+ ___block_literal_global.232
+ ___block_literal_global.236
+ ___block_literal_global.248
+ ___block_literal_global.251
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.260
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.273
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.314
+ ___block_literal_global.317
+ ___block_literal_global.323
+ ___block_literal_global.328
+ ___block_literal_global.331
+ ___block_literal_global.334
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.360
+ ___block_literal_global.363
+ ___block_literal_global.366
+ ___block_literal_global.369
+ ___block_literal_global.372
+ ___block_literal_global.375
+ ___block_literal_global.378
+ ___block_literal_global.381
+ ___block_literal_global.81
+ ___block_literal_global.95
+ _devicePlatform.deviceClass
+ _devicePlatform.onceToken
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kKTStatusSelfDevices
+ _kKTStatusServerOptInState
+ _kTransparencyFlagForceCDPWaiting
+ _objc_msgSend$allObjects
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$jsonArrayFromPlistArray:
+ _objc_msgSend$jsonDictFromPlistDict:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$markExpiryDate
+ _objc_msgSend$maybeUpdateMonitorState
+ _objc_msgSend$nfsObserver
+ _objc_msgSend$pendingStatusChanges
+ _objc_msgSend$serverOptIn
+ _objc_msgSend$setMarkExpiryDate:
+ _objc_msgSend$setNfsObserver:
+ _objc_msgSend$setPendingStatusChanges:
+ _objc_msgSend$setServerOptIn:
+ _objc_msgSend$status
+ _objc_msgSend$transparencyClearKTRegistrationData:
+ _objc_msgSend$weakObjectsHashTable
- GCC_except_table127
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.299
- ___22-[KTStatus getStatus:]_block_invoke.184
- ___22-[KTStatus getStatus:]_block_invoke.188
- ___22-[KTStatus getStatus:]_block_invoke_2.189
- ___26-[KTStatus getSelfStatus:]_block_invoke.195
- ___26-[KTStatus getSelfStatus:]_block_invoke.198
- ___26-[KTStatus getSelfStatus:]_block_invoke_2.199
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.357
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.348
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.223
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.226
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.227
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.232
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.235
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.236
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.331
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.204
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.207
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.209
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.314
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.316
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.214
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.217
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.218
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.302
- ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.319
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.325
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.305
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.351
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.360
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.328
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.345
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.342
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.308
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.322
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.363
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.366
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.112
- ___70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.116
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.369
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.354
- ___block_literal_global.114
- ___block_literal_global.183
- ___block_literal_global.186
- ___block_literal_global.191
- ___block_literal_global.194
- ___block_literal_global.197
- ___block_literal_global.201
- ___block_literal_global.203
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.216
- ___block_literal_global.220
- ___block_literal_global.222
- ___block_literal_global.225
- ___block_literal_global.231
- ___block_literal_global.301
- ___block_literal_global.304
- ___block_literal_global.307
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.321
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.341
- ___block_literal_global.344
- ___block_literal_global.347
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.356
- ___block_literal_global.359
- ___block_literal_global.362
- ___block_literal_global.365
- ___block_literal_global.368
- ___block_literal_global.84
- _objc_msgSend$noteLaunchSequence:
CStrings:
+ "\x16\x14"
+ " "
+ "    markedExpiryDate:%@\n"
+ "%lld"
+ "@\"NSHashTable\""
+ "KTStatus: optIn = %@, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, pendingChanges: %@\n"
+ "Sending maybeUpdateMonitorState"
+ "Sending performAndWaitForSelfValidate"
+ "Sending transparencyClearKTRegistrationData:"
+ "T@\"NSDate\",&,V_markExpiryDate"
+ "T@\"NSHashTable\",&,V_nfsObserver"
+ "TB,V_pendingStatusChanges"
+ "TQ,V_serverOptIn"
+ "_markExpiryDate"
+ "_nfsObserver"
+ "_pendingStatusChanges"
+ "_serverOptIn"
+ "addNFSReporting:"
+ "allObjects"
+ "b"
+ "cfPrefsJson"
+ "devicePlatform"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumerateObjectsUsingBlock:"
+ "forceCDPWaiting"
+ "jsonArrayFromPlistArray:"
+ "jsonDictFromPlistDict:"
+ "jsonFromPlist: failed to convert key (class: %@) %@, using description"
+ "jsonFromPlist: failed to convert obj (class: %@) %@, using description"
+ "lowercaseString"
+ "markExpiry"
+ "markExpiryDate"
+ "markedExpiryDate"
+ "maybeUpdateMonitorState"
+ "maybeUpdateMonitorState failed with: %@"
+ "nfsObserver"
+ "nfsReporting"
+ "pendingChanges"
+ "pendingStatusChanges"
+ "serverOptIn"
+ "serverOptInState"
+ "serverOptedIn"
+ "setMarkExpiryDate:"
+ "setNfsObserver:"
+ "setPendingStatusChanges:"
+ "setServerOptIn:"
+ "status"
+ "transparencyClearKTRegistrationData:"
+ "transparencyVersionStr"
+ "v32@?0@8@16^B24"
+ "v32@?0@8Q16^B24"
+ "weakObjectsHashTable"
- "\x16\x13"
- "A"
- "KTStatus: optIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@"
- "Sending performAndWaitForSelfValdiate"

```

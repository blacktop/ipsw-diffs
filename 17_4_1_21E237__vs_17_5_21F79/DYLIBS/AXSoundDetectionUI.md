## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-406.16.1.0.0
-  __TEXT.__text: 0x51308
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x1f80
-  __TEXT.__const: 0x700
-  __TEXT.__gcc_except_tab: 0x28c
-  __TEXT.__oslogstring: 0x3be3
-  __TEXT.__cstring: 0x3043
+406.22.0.0.0
+  __TEXT.__text: 0x54940
+  __TEXT.__auth_stubs: 0x1210
+  __TEXT.__objc_methlist: 0x2094
+  __TEXT.__const: 0x8a0
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__oslogstring: 0x3d60
+  __TEXT.__cstring: 0x382b
   __TEXT.__dlopen_cstrs: 0x13e
-  __TEXT.__swift5_typeref: 0x670
-  __TEXT.__swift5_capture: 0x23c
-  __TEXT.__constg_swiftt: 0x6c4
-  __TEXT.__swift5_reflstr: 0x211
-  __TEXT.__swift5_fieldmd: 0x26c
+  __TEXT.__swift5_typeref: 0x75c
+  __TEXT.__swift5_capture: 0x2a4
+  __TEXT.__constg_swiftt: 0x7f0
+  __TEXT.__swift5_reflstr: 0x301
+  __TEXT.__swift5_fieldmd: 0x33c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x34
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x1964
-  __TEXT.__eh_frame: 0x838
-  __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x4d36
-  __TEXT.__objc_methtype: 0xdba
-  __TEXT.__objc_stubs: 0x4480
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__unwind_info: 0x1c68
+  __TEXT.__eh_frame: 0x9d0
+  __TEXT.__objc_classname: 0x482
+  __TEXT.__objc_methname: 0x4fac
+  __TEXT.__objc_methtype: 0xe36
+  __TEXT.__objc_stubs: 0x4660
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x7f0
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7898
-  __DATA_CONST.__objc_selrefs: 0x14f0
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_classrefs: 0x2c0
+  __DATA_CONST.__objc_const: 0x7c98
+  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_classrefs: 0x2e0
   __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__objc_const: 0xbe0
-  __AUTH_CONST.__const: 0xf28
-  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__const: 0x1298
+  __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x890
-  __AUTH.__objc_data: 0x15b0
-  __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x1b8
-  __DATA.__objc_data: 0x210
-  __DATA.__data: 0xb38
-  __DATA.__bss: 0x770
-  __DATA.__common: 0x48
+  __AUTH_CONST.__auth_got: 0x918
+  __AUTH.__objc_data: 0x1598
+  __AUTH.__data: 0x2e0
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_data: 0x260
+  __DATA.__data: 0xc10
+  __DATA.__bss: 0x920
+  __DATA.__common: 0x50
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 010DA747-42FE-362A-B066-313208F835C3
-  Functions: 1579
-  Symbols:   3667
-  CStrings:  1807
+  UUID: A5A97904-C6FD-3DA9-A439-CFC15AE91487
+  Functions: 1718
+  Symbols:   3801
+  CStrings:  1890
 
Symbols:
+ -[AXSDDetectorStore detectorWithIdentifier:].cold.1
+ -[AXSDKShotController kickoffTrainingForDetector:].cold.1
+ -[AXSDKShotDetector lastAttemptedTrainingDate]
+ -[AXSDKShotDetector modelFailed]
+ -[AXSDKShotDetector setLastAttemptedTrainingDate:]
+ -[AXSDKShotDetector setModelFailed:]
+ -[AXSDKShotDetector setTrainings:]
+ -[AXSDKShotDetector shouldRetrain]
+ -[AXSDKShotDetector trainings]
+ -[AXSDListenEngine audioFormat]
+ -[AXSDListenEngine notifyListeningFinishedAudioFile:]
+ -[AXSDListenEngine notifyListeningFinishedAudioFile:].cold.1
+ -[AXSDListenEngine notifyListeningReceivedAudioFile:]
+ -[AXSDListenEngine notifyListeningReceivedAudioFile:].cold.1
+ -[AXSDListenEngine pipeInFile:]
+ -[AXSDListenEngine pipeInFile:].cold.1
+ -[AXSDSettings(AXSoundDetectionUIAdditions) updateKShotDetector:]
+ -[AXSDSoundDetectionController _pipedInFileUpdated]
+ -[AXSDSoundDetectionController pipeInFile:]
+ -[AXSDSoundDetectionController pipeInFile:].cold.1
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table39
+ _AXIsSoundDetectionMedinaSupportEnabled
+ _OBJC_CLASS_$_AXDispatchTimer
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_AXSDKShotDetector._lastAttemptedTrainingDate
+ _OBJC_IVAR_$_AXSDKShotDetector._modelFailed
+ _OBJC_IVAR_$_AXSDKShotDetector._trainings
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC18AXSoundDetectionUI16AXSDKShotMonitor
+ __IVARS__TtC18AXSoundDetectionUI16AXSDKShotMonitor
+ __METACLASS_DATA__TtC18AXSoundDetectionUI16AXSDKShotMonitor
+ __OBJC_$_INSTANCE_METHODS__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation(AXSoundDetectionUI|AXSoundDetectionUI1|AXSoundDetectionUI2|AXSoundDetectionUI3)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __OBJC_CLASS_PROTOCOLS_$__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation(AXSoundDetectionUI|AXSoundDetectionUI2|AXSoundDetectionUI3)
+ __OBJC_LABEL_PROTOCOL_$__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __OBJC_PROTOCOL_$__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __OBJC_PROTOCOL_REFERENCE_$__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __PROTOCOLS__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation.37
+ __PROTOCOLS__TtC18AXSoundDetectionUI34AXSASecureControllerImplementation.2
+ __PROTOCOLS__TtC18AXSoundDetectionUI44AXSDKShotNSRecordingControllerImplementation.51
+ __PROTOCOL_INSTANCE_METHODS__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __PROTOCOL_METHOD_TYPES__TtP18AXSoundDetectionUI14AXSDAutomation_
+ __PROTOCOL__TtP18AXSoundDetectionUI14AXSDAutomation_
+ ___31-[AXSDListenEngine audioFormat]_block_invoke
+ ___36-[AXSDSoundDetectionController init]_block_invoke
+ ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.23
+ ___49-[AXSDListenEngine _carPlayIsConnectedDidChange:]_block_invoke.98
+ ___52-[AXSDListenEngine notifyListeningEncounteredError:]_block_invoke
+ ___52-[AXSDListenEngine notifyListeningStartedWithError:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ _associated conformance 18AXSoundDetectionUI23AXSDKShotRecordingErrorOSHAASQ
+ _block_copy_helper.80
+ _block_descriptor.82
+ _block_destroy_helper.81
+ _objc_msgSend$_createSDDetectors
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$description
+ _objc_msgSend$isTrainingComplete
+ _objc_msgSend$kickoffMLTrainingOfDetector:error:
+ _objc_msgSend$lastAttemptedTrainingDate
+ _objc_msgSend$listenEngineFinishedAudioFile:
+ _objc_msgSend$listenEngineReceivedAudioFile:
+ _objc_msgSend$notifyListeningFinishedAudioFile:
+ _objc_msgSend$notifyListeningReceivedAudioFile:
+ _objc_msgSend$pipeInFile:
+ _objc_msgSend$pipeInFilePath:error:
+ _objc_msgSend$setLastAttemptedTrainingDate:
+ _objc_msgSend$setTrainings:
+ _objc_msgSend$startListeningOnQueue:
+ _objc_msgSend$trainings
+ _objc_msgSend$unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:
+ _swift_deallocClassInstance
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_initEnumMetadataSinglePayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s18AXSoundDetectionUI14AXSDAutomationP
+ _symbolic SDy_____SaySo17SNDetectionResultCGGSg So22AXSDSoundDetectionTypea
+ _symbolic SaySo17SNDetectionResultCG
+ _symbolic So11AVAudioFileC
+ _symbolic So15AXDispatchTimerC
+ _symbolic _____ 18AXSoundDetectionUI16AXSDKShotMonitorC
+ _symbolic _____ 18AXSoundDetectionUI23AXSDKShotRecordingErrorO
+ _symbolic _____ 18AXSoundDetectionUI9AXSDErrorO
+ _symbolic _____7fileURL_t 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____y_____SaySo17SNDetectionResultCGG s18_DictionaryStorageC So22AXSDSoundDetectionTypea
- -[AXSDDetector modelFailed]
- -[AXSDListenEngine _pipedInFileUpdated].cold.2
- -[AXSDListenEngine _pipedInFileUpdated].cold.3
- GCC_except_table25
- GCC_except_table31
- __OBJC_$_INSTANCE_METHODS__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation(AXSoundDetectionUI|AXSoundDetectionUI1|AXSoundDetectionUI2)
- __OBJC_CLASS_PROTOCOLS_$__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation(AXSoundDetectionUI1|AXSoundDetectionUI2)
- __PROTOCOLS__TtC18AXSoundDetectionUI30AXSDNSControllerImplementation.13
- __PROTOCOLS__TtC18AXSoundDetectionUI34AXSASecureControllerImplementation.3
- __PROTOCOLS__TtC18AXSoundDetectionUI44AXSDKShotNSRecordingControllerImplementation.49
- ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.19
- ___49-[AXSDListenEngine _carPlayIsConnectedDidChange:]_block_invoke.94
- _objc_msgSend$kickoffMLTrainingOfDetector:
- _objc_msgSend$unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:
CStrings:
+ "\x02!"
+ "%@, Name: %@, Category: %@, Is Ready: %@, Model URL: %@, Recordings: %@, Model Failed: %@, Trainings: %@, Last Attempted Training Date: %@"
+ "@\"NSDate\""
+ "@\"NSDictionary\"32@0:8@\"NSString\"16^@24"
+ "@\"NSDictionary\"32@0:8@\"NSURL\"16^@24"
+ "@32@0:8@16^@24"
+ "AXSDKShotMonitor: %s start retraining of detector."
+ "AXSDKShotMonitor: Checking if detector should be retrained: %@."
+ "AXSDKShotMonitor: Not checking detectors. Currently training a KShot Model."
+ "AXSDKShotMonitor: Start Monitoring"
+ "AXSDKShotMonitor: Stop Monitoring"
+ "Attempting to retrain detector. Detector: %@"
+ "B32@0:8@\"AXSDKShotDetector\"16^@24"
+ "B32@0:8@16^@24"
+ "Detector is already marked as failed. Not attempting retraining. Detector: %@"
+ "Error while piping file. Error: %@"
+ "Initializing NS Sound Detection Controller"
+ "It's too early to attempt retrain of detector. Waiting: %f. Current time difference is: %f. Not attempting retraining. Detector: %@"
+ "KShot Controller: Error kicking off training for detector: %@. Error: %@"
+ "KShot Controller: Kicking off training of detector: %@"
+ "Listen Engine: Notify Listening Finished Audio File: %@"
+ "Listen Engine: Notify Listening Received Audio File: %@"
+ "Medina is Enabled. Are KShot Detectors Ready: %@"
+ "T@\"AVAudioFormat\",R"
+ "T@\"NSDate\",&,N,V_lastAttemptedTrainingDate"
+ "TB,N,V_modelFailed"
+ "TQ,N,V_trainings"
+ "Trying to retrieve a detector with an invalid identifier. Identifier: %@"
+ "[%s]: AUTOMATION: piped in file: %s"
+ "[%s]: BEGIN actively training kshot model"
+ "[%s]: END actively training kshot model"
+ "[%s]: Finished processing audio file: %@."
+ "[%s]: Received audio file: %@ with audio format: %@"
+ "[%s]: Sound Actions is already listening. startListening is a no-op."
+ "[%s]: Starting detector manager with audio format: %@"
+ "[%s]: Stopping detector manager."
+ "[%s]: attempted %ld trainings. marking detector as failed. Detector: %@"
+ "[%s]: handle ML error with detector: %@."
+ "[%s]: handle ML result with detector: %@ - model URL: %s"
+ "[%s]: piped in fileURL: %s is not a valid file URL"
+ "[%s]: start listening with queue: %@"
+ "[%s]: unable to train detector. Hallucinator asset is not downloaded."
+ "[%s]: unable to train detector. Model Weights asset is not downloaded."
+ "[%s]: updating dispatch queue to: %@"
+ "_TtC18AXSoundDetectionUI16AXSDKShotMonitor"
+ "_TtP18AXSoundDetectionUI14AXSDAutomation_"
+ "_lastAttemptedTrainingDate"
+ "_modelFailed"
+ "_trainings"
+ "afterDelay:processBlock:"
+ "audioFormat"
+ "cancel"
+ "dispatchTimer"
+ "initWithTargetSerialQueue:"
+ "is actively training kshot model"
+ "isActivelyTraining"
+ "isActivelyTrainingAKShotModel"
+ "kickoffMLTrainingOfDetector:error:"
+ "lastAttemptedTrainingDate"
+ "listenEngineFinishedAudioFile:"
+ "listenEngineReceivedAudioFile:"
+ "maxNumberOfTrainings"
+ "maximumActiveTrainingDuration"
+ "monitoringTask"
+ "notifyListeningFinishedAudioFile:"
+ "notifyListeningReceivedAudioFile:"
+ "pipeInFile:"
+ "pipeInFilePath:error:"
+ "pipeInFileURL:error:"
+ "recentDetections"
+ "retrainInterval"
+ "setAutomaticallyCancelPendingBlockUponSchedulingNewBlock:"
+ "setLabel:"
+ "setLastAttemptedTrainingDate:"
+ "setTrainings:"
+ "shouldRetrain"
+ "sleepLength"
+ "trainings"
+ "unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:"
+ "updateKShotDetector:"
+ "v24@0:8@\"AVAudioFile\"16"
+ "v24@0:8@\"OS_dispatch_queue\"16"
- "Feed buffer: %@"
- "Initializing Non Secure Sound Detection Controller"
- "[%@] Identifier: %@, Category: %@, Is Ready: %@, Model URL: %@, Recordings: %@"
- "[%s]: non-secure handle ML result with detector: %@ - model URL: %s"
- "com.apple.accessibility.soundactions.processing"
- "kickoffMLTrainingOfDetector:"
- "unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:"

```

## Speech

> `/System/Library/Frameworks/Speech.framework/Versions/A/Speech`

```diff

-3404.78.1.0.0
-  __TEXT.__text: 0x1c9a28
-  __TEXT.__auth_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0x40d4
+3405.13.1.0.0
+  __TEXT.__text: 0x1cb350
+  __TEXT.__auth_stubs: 0x2d70
+  __TEXT.__objc_methlist: 0x41bc
   __TEXT.__const: 0xaa78
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xa9f2
+  __TEXT.__cstring: 0xaa11
   __TEXT.__constg_swiftt: 0x45ac
   __TEXT.__swift5_typeref: 0x6180
   __TEXT.__swift5_reflstr: 0x3787

   __TEXT.__swift5_assocty: 0xde0
   __TEXT.__swift5_proto: 0x754
   __TEXT.__swift5_types: 0x338
-  __TEXT.__oslogstring: 0x3629
+  __TEXT.__oslogstring: 0x3651
   __TEXT.__swift5_capture: 0x226c
   __TEXT.__swift5_acfuncs: 0x500
   __TEXT.__swift_as_entry: 0x868

   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__gcc_except_tab: 0x7f4
-  __TEXT.__unwind_info: 0x8040
+  __TEXT.__unwind_info: 0x8060
   __TEXT.__eh_frame: 0x10f9c
-  __TEXT.__objc_classname: 0xa00
-  __TEXT.__objc_methname: 0xd34d
-  __TEXT.__objc_methtype: 0x26e0
-  __TEXT.__objc_stubs: 0x4bc0
-  __DATA_CONST.__got: 0xe38
-  __DATA_CONST.__const: 0x798
-  __DATA_CONST.__objc_classlist: 0x408
+  __TEXT.__objc_classname: 0xa46
+  __TEXT.__objc_methname: 0xd462
+  __TEXT.__objc_methtype: 0x2704
+  __TEXT.__objc_stubs: 0x4cc0
+  __DATA_CONST.__got: 0xe48
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29a0
+  __DATA_CONST.__objc_selrefs: 0x2a00
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x16c0
-  __AUTH_CONST.__auth_ptr: 0x1028
+  __AUTH_CONST.__auth_got: 0x16c8
+  __AUTH_CONST.__auth_ptr: 0x1008
   __AUTH_CONST.__const: 0xae28
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0xbd80
+  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__objc_const: 0xbf00
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0x21f8
+  __AUTH.__objc_data: 0x2248
   __AUTH.__data: 0x4900
-  __DATA.__objc_ivar: 0x508
-  __DATA.__data: 0x5948
-  __DATA.__bss: 0xc9c0
+  __DATA.__objc_ivar: 0x510
+  __DATA.__data: 0x59a8
+  __DATA.__bss: 0xc9d0
   __DATA.__common: 0x380
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11928
-  Symbols:   9218
-  CStrings:  3713
+  Functions: 11939
+  Symbols:   9255
+  CStrings:  3733
 
Symbols:
+ +[SFSpeechProfileResourceMonitor sharedMonitor]
+ -[SFSpeechProfileContainerManager resourceAvailableForPersona:]
+ -[SFSpeechProfileContainerManager resourceUnavailableForPersona:]
+ -[SFSpeechProfileResourceMonitor .cxx_destruct]
+ -[SFSpeechProfileResourceMonitor _initWithQueue:]
+ -[SFSpeechProfileResourceMonitor _startSession]
+ -[SFSpeechProfileResourceMonitor _stopSession]
+ -[SFSpeechProfileResourceMonitor addObserver:]
+ -[SFSpeechProfileResourceMonitor init]
+ -[SFSpeechProfileResourceMonitor observers]
+ -[SFSpeechProfileResourceMonitor registerLaunchOnDemand]
+ -[SFSpeechProfileResourceMonitor removeObserver:]
+ -[SFSpeechProfileResourceMonitor setObservers:]
+ GCC_except_table1006
+ GCC_except_table1025
+ GCC_except_table1047
+ GCC_except_table1052
+ GCC_except_table1133
+ GCC_except_table1158
+ GCC_except_table1326
+ GCC_except_table1338
+ GCC_except_table1344
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1348
+ GCC_except_table1349
+ GCC_except_table1350
+ GCC_except_table1353
+ GCC_except_table755
+ GCC_except_table856
+ GCC_except_table890
+ GCC_except_table900
+ GCC_except_table902
+ GCC_except_table911
+ GCC_except_table954
+ OBJC_IVAR_$_SFSpeechProfileResourceMonitor._observers
+ OBJC_IVAR_$_SFSpeechProfileResourceMonitor._queue
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_SFSpeechProfileResourceMonitor
+ _OBJC_METACLASS_$_SFSpeechProfileResourceMonitor
+ __Block_byref_object_copy_.1475
+ __Block_byref_object_copy_.1625
+ __Block_byref_object_copy_.1758
+ __Block_byref_object_copy_.2110
+ __Block_byref_object_copy_.2297
+ __Block_byref_object_copy_.2887
+ __Block_byref_object_dispose_.1476
+ __Block_byref_object_dispose_.1626
+ __Block_byref_object_dispose_.1759
+ __Block_byref_object_dispose_.2111
+ __Block_byref_object_dispose_.2298
+ __Block_byref_object_dispose_.2888
+ __OBJC_$_CLASS_METHODS_SFSpeechProfileResourceMonitor
+ __OBJC_$_INSTANCE_METHODS_SFSpeechProfileResourceMonitor
+ __OBJC_$_INSTANCE_VARIABLES_SFSpeechProfileResourceMonitor
+ __OBJC_$_PROP_LIST_SFSpeechProfileContainerManager
+ __OBJC_$_PROP_LIST_SFSpeechProfileResourceMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_SFSpeechProfileResourceMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SFSpeechProfileContainerManager
+ __OBJC_CLASS_RO_$_SFSpeechProfileResourceMonitor
+ __OBJC_LABEL_PROTOCOL_$_SFSpeechProfileResourceMonitorDelegate
+ __OBJC_METACLASS_RO_$_SFSpeechProfileResourceMonitor
+ __OBJC_PROTOCOL_$_SFSpeechProfileResourceMonitorDelegate
+ ___46-[SFSpeechProfileResourceMonitor addObserver:]_block_invoke
+ ___47+[SFSpeechProfileResourceMonitor sharedMonitor]_block_invoke
+ ___49-[SFSpeechProfileResourceMonitor removeObserver:]_block_invoke
+ __block_literal_global.1494
+ __block_literal_global.1654
+ __block_literal_global.1860
+ __block_literal_global.2089
+ __block_literal_global.2330
+ __block_literal_global.236
+ __block_literal_global.254
+ __block_literal_global.2692
+ __block_literal_global.281
+ __block_literal_global.289
+ __block_literal_global.2936
+ _kSFSpeechProfileResourceId
+ _objc_exception_throw
+ _objc_msgSend$_startSession
+ _objc_msgSend$_stopSession
+ _objc_msgSend$addObserver:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$observers
+ _objc_msgSend$releaseContainerForPersona:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$sharedMonitor
+ block_copy_helper.348
+ block_copy_helper.364
+ block_copy_helper.409
+ block_copy_helper.426
+ block_copy_helper.442
+ block_copy_helper.453
+ block_copy_helper.464
+ block_copy_helper.475
+ block_copy_helper.486
+ block_copy_helper.497
+ block_copy_helper.529
+ block_copy_helper.536
+ block_copy_helper.553
+ block_copy_helper.564
+ block_descriptor.350
+ block_descriptor.366
+ block_descriptor.411
+ block_descriptor.428
+ block_descriptor.444
+ block_descriptor.455
+ block_descriptor.466
+ block_descriptor.477
+ block_descriptor.488
+ block_descriptor.499
+ block_descriptor.531
+ block_descriptor.538
+ block_descriptor.555
+ block_descriptor.566
+ block_destroy_helper.349
+ block_destroy_helper.365
+ block_destroy_helper.410
+ block_destroy_helper.427
+ block_destroy_helper.443
+ block_destroy_helper.454
+ block_destroy_helper.465
+ block_destroy_helper.476
+ block_destroy_helper.487
+ block_destroy_helper.498
+ block_destroy_helper.530
+ block_destroy_helper.537
+ block_destroy_helper.554
+ block_destroy_helper.565
+ sharedInstance.onceToken.1859
+ sharedInstance.onceToken.1906
+ sharedInstance.sharedManager.1861
+ sharedInstance.sharedManager.1907
+ sharedMonitor.onceToken
+ sharedMonitor.sharedMonitor
- GCC_except_table1009
- GCC_except_table1031
- GCC_except_table1036
- GCC_except_table1117
- GCC_except_table1142
- GCC_except_table1302
- GCC_except_table1310
- GCC_except_table1314
- GCC_except_table1322
- GCC_except_table1328
- GCC_except_table1329
- GCC_except_table1332
- GCC_except_table1333
- GCC_except_table1337
- GCC_except_table739
- GCC_except_table840
- GCC_except_table874
- GCC_except_table884
- GCC_except_table886
- GCC_except_table895
- GCC_except_table938
- GCC_except_table990
- __Block_byref_object_copy_.1427
- __Block_byref_object_copy_.1538
- __Block_byref_object_copy_.1671
- __Block_byref_object_copy_.2022
- __Block_byref_object_copy_.2205
- __Block_byref_object_copy_.2795
- __Block_byref_object_dispose_.1428
- __Block_byref_object_dispose_.1539
- __Block_byref_object_dispose_.1672
- __Block_byref_object_dispose_.2023
- __Block_byref_object_dispose_.2206
- __Block_byref_object_dispose_.2796
- __block_literal_global.1445
- __block_literal_global.1567
- __block_literal_global.1773
- __block_literal_global.2003
- __block_literal_global.2236
- __block_literal_global.233
- __block_literal_global.251
- __block_literal_global.2600
- __block_literal_global.278
- __block_literal_global.2844
- __block_literal_global.286
- block_copy_helper.351
- block_copy_helper.358
- block_copy_helper.408
- block_copy_helper.430
- block_copy_helper.441
- block_copy_helper.452
- block_copy_helper.463
- block_copy_helper.474
- block_copy_helper.484
- block_copy_helper.491
- block_copy_helper.530
- block_copy_helper.541
- block_copy_helper.552
- block_copy_helper.559
- block_descriptor.353
- block_descriptor.360
- block_descriptor.410
- block_descriptor.432
- block_descriptor.443
- block_descriptor.454
- block_descriptor.465
- block_descriptor.476
- block_descriptor.486
- block_descriptor.493
- block_descriptor.532
- block_descriptor.543
- block_descriptor.554
- block_descriptor.561
- block_destroy_helper.352
- block_destroy_helper.359
- block_destroy_helper.409
- block_destroy_helper.431
- block_destroy_helper.442
- block_destroy_helper.453
- block_destroy_helper.464
- block_destroy_helper.475
- block_destroy_helper.485
- block_destroy_helper.492
- block_destroy_helper.531
- block_destroy_helper.542
- block_destroy_helper.553
- block_destroy_helper.560
- sharedInstance.onceToken.1772
- sharedInstance.onceToken.1819
- sharedInstance.sharedManager.1774
- sharedInstance.sharedManager.1820
CStrings:
+ "%s Refreshing container for persona: %@"
+ "-[SFSpeechProfileContainerManager resourceAvailableForPersona:]"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/EAR-XPC/NSXPCActorSystem.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Assets/AssetsInstallationRequest.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/CommandRecognizer.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/EndpointDetector.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/LanguageDetector.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/LanguageDetectorWorker.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Misc.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/ObjCSpeechAnalyzer.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/PhoneticTranscriber.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechAnalyzer.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechAnalyzerClientInterface.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechDetector.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechRecognizerWorker.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TaskHint.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TimeUtilities.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Transcriber.swift"
+ "/AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TranscriberResults.swift"
+ "@\"NSHashTable\""
+ "SFSpeechProfileResourceMonitor"
+ "SFSpeechProfileResourceMonitorDelegate"
+ "T@\"NSHashTable\",&,N,V_observers"
+ "_startSession"
+ "_stopSession"
+ "addObserver:"
+ "com.apple.siri.speech-profile"
+ "exceptionWithName:reason:userInfo:"
+ "init unsupported"
+ "observers"
+ "registerLaunchOnDemand"
+ "removeObject:"
+ "resourceAvailableForPersona:"
+ "resourceUnavailableForPersona:"
+ "resourceUnavailableSoonForPersona:"
+ "setObservers:"
+ "sharedMonitor"
+ "v24@0:8@\"NSString\"16"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/EAR-XPC/NSXPCActorSystem.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Assets/AssetsInstallationRequest.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/CommandRecognizer.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/EndpointDetector.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/LanguageDetector.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/LanguageDetectorWorker.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Misc.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/ObjCSpeechAnalyzer.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/PhoneticTranscriber.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechAnalyzer.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechAnalyzerClientInterface.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechDetector.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/SpeechRecognizerWorker.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TaskHint.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TimeUtilities.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Transcriber.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/TranscriberResults.swift"
- "PhoneticEmbedder was initialized with a locale with insufficient information: "

```

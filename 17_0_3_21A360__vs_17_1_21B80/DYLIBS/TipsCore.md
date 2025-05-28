## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-712.0.0.0.0
-  __TEXT.__text: 0x85b7c
-  __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x8c88
-  __TEXT.__const: 0x1078
-  __TEXT.__cstring: 0x4f16
-  __TEXT.__oslogstring: 0x1ae1
-  __TEXT.__gcc_except_tab: 0x1180
+719.0.0.0.0
+  __TEXT.__text: 0x8e15c
+  __TEXT.__auth_stubs: 0x18a0
+  __TEXT.__objc_methlist: 0x8b80
+  __TEXT.__const: 0x1188
+  __TEXT.__cstring: 0x5126
+  __TEXT.__oslogstring: 0x19ee
+  __TEXT.__gcc_except_tab: 0x10e4
   __TEXT.__ustring: 0x118
   __TEXT.__dlopen_cstrs: 0x209
-  __TEXT.__swift5_typeref: 0x72d
-  __TEXT.__constg_swiftt: 0x8ec
-  __TEXT.__swift5_reflstr: 0x561
-  __TEXT.__swift5_fieldmd: 0x5c8
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_typeref: 0x873
+  __TEXT.__constg_swiftt: 0xa84
+  __TEXT.__swift5_reflstr: 0x5f1
+  __TEXT.__swift5_fieldmd: 0x680
+  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xac
-  __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_capture: 0x27c
+  __TEXT.__swift5_proto: 0xb0
+  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_capture: 0x360
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2d30
-  __TEXT.__eh_frame: 0x360
-  __TEXT.__objc_classname: 0x10c6
-  __TEXT.__objc_methname: 0x11568
-  __TEXT.__objc_methtype: 0x1d27
-  __TEXT.__objc_stubs: 0xb580
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x23b0
-  __DATA_CONST.__objc_classlist: 0x508
+  __TEXT.__unwind_info: 0x3634
+  __TEXT.__eh_frame: 0xa58
+  __TEXT.__objc_classname: 0x10d1
+  __TEXT.__objc_methname: 0x110e0
+  __TEXT.__objc_methtype: 0x1cae
+  __TEXT.__objc_stubs: 0xb3a0
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__const: 0x23e8
+  __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa890
-  __DATA_CONST.__objc_selrefs: 0x3f90
+  __DATA_CONST.__objc_const: 0xa8a8
+  __DATA_CONST.__objc_selrefs: 0x3ec0
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__cfstring: 0x5de0
-  __AUTH_CONST.__objc_const: 0x4cc8
-  __AUTH_CONST.__const: 0x1fc8
+  __AUTH_CONST.__cfstring: 0x5e20
+  __AUTH_CONST.__objc_const: 0x4d10
+  __AUTH_CONST.__const: 0x21b8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH.__objc_data: 0x1230
-  __AUTH.__data: 0x408
+  __AUTH_CONST.__auth_ptr: 0x78
+  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH.__objc_data: 0x1318
+  __AUTH.__data: 0x620
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x620
-  __DATA.__objc_superrefs: 0x388
-  __DATA.__objc_ivar: 0x8d4
-  __DATA.__data: 0x10c0
-  __DATA.__bss: 0x12d0
+  __DATA.__objc_classrefs: 0x628
+  __DATA.__objc_superrefs: 0x380
+  __DATA.__objc_ivar: 0x8ac
+  __DATA.__data: 0x1250
+  __DATA.__bss: 0x1350
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2808
-  __DATA_DIRTY.__data: 0x338
-  __DATA_DIRTY.__bss: 0x2e8
+  __DATA_DIRTY.__objc_data: 0x2838
+  __DATA_DIRTY.__data: 0x358
+  __DATA_DIRTY.__bss: 0x2c8
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4310
-  Symbols:   11107
-  CStrings:  4646
+  Functions: 4436
+  Symbols:   11027
+  CStrings:  4604
 
Symbols:
+ +[TPSCommonDefines isMacUI]
+ +[TPSCommonDefines isPadUI]
+ +[TPSCommonDefines isPhoneUI]
+ +[TPSCommonDefines isVisionUI]
+ +[TPSContextualBiomeAppInFocusEvent observationDateFromEvent:]
+ -[TPSAppController networkMonitorToken]
+ -[TPSAppController setNetworkMonitorToken:]
+ -[TPSContextualBiomeAppInFocusEvent _filteringPredicate]
+ -[TPSContextualBiomeAppInFocusEvent filterHandler]
+ -[TPSContextualBiomeAppInFocusEvent publisherFromStartTime:]
+ -[TPSWidgetController fetchWidgetAssetsForDocument:preferCacheIfAvailable:completionHandler:].cold.2
+ GCC_except_table53
+ GCC_except_table55
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMAppInFocus
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_TPSContextualBiomeAppInFocusEvent
+ _OBJC_IVAR_$_TPSAppController._networkMonitorToken
+ _OBJC_METACLASS_$_TPSContextualBiomeAppInFocusEvent
+ _TPSAnimationSourceOrganic
+ _TPSURLSessionErrorCodeNoContent
+ _TPSURLSessionErrorDomain
+ _TPSWidgetControllerErrorDomain
+ __CLASS_PROPERTIES_TPSNetworkPathMonitor
+ __DATA_TPSNetworkPathMonitor
+ __DATA__TtC8TipsCore14NetworkMonitor
+ __DATA__TtC8TipsCoreP33_3C3E78E32FD3541F35ED5B8FF99C55CA18SerialTaskExecutor
+ __IVARS_TPSNetworkPathMonitor
+ __IVARS__TtC8TipsCore14NetworkMonitor
+ __IVARS__TtC8TipsCoreP33_3C3E78E32FD3541F35ED5B8FF99C55CA18SerialTaskExecutor
+ __METACLASS_DATA_TPSNetworkPathMonitor
+ __METACLASS_DATA__TtC8TipsCore14NetworkMonitor
+ __METACLASS_DATA__TtC8TipsCoreP33_3C3E78E32FD3541F35ED5B8FF99C55CA18SerialTaskExecutor
+ __OBJC_$_CLASS_METHODS_TPSContextualBiomeAppInFocusEvent
+ __OBJC_$_INSTANCE_METHODS_TPSContextualBiomeAppInFocusEvent
+ __OBJC_CLASS_RO_$_TPSContextualBiomeAppInFocusEvent
+ __OBJC_METACLASS_RO_$_TPSContextualBiomeAppInFocusEvent
+ ___141-[TPSWidgetController updateWidgetDocumentWithDocumentsMap:documentsDeliveryInfoMap:deliveryInfoMap:preferHardwareWelcome:completionHandler:]_block_invoke.26
+ ___24-[TPSAppController init]_block_invoke
+ ___31+[TPSCommonDefines deviceClass]_block_invoke
+ ___50-[TPSContextualBiomeAppInFocusEvent filterHandler]_block_invoke
+ ___56-[TPSContextualBiomeAppInFocusEvent _filteringPredicate]_block_invoke
+ ___56-[TPSContextualBiomeAppInFocusEvent _filteringPredicate]_block_invoke_2
+ ___56-[TPSContextualBiomeAppInFocusEvent _filteringPredicate]_block_invoke_3
+ ___56-[TPSContextualBiomeAppInFocusEvent _filteringPredicate]_block_invoke_4
+ ___63-[TPSWidgetController updatePreferredWidget:completionHandler:]_block_invoke_2.cold.4
+ ___block_descriptor_33_e39_B24?0"BMAppInFocus"8"NSDictionary"16l
+ ___block_descriptor_36_e39_B24?0"BMAppInFocus"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e39_B24?0"BMAppInFocus"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32bs40r_e27_v24?0"NSURL"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32bs_e27_v24?0"NSURL"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e37_v32?0"NSURL"8"NSURL"16"NSError"24ls40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e53_v40?0"TPSDocument"8"NSURL"16"NSURL"24"NSError"32ls48l8r56l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0ls32l8s64l8w72l8s40l8s48l8s56l8
+ ___block_literal_global.197
+ ___block_literal_global.206
+ ___block_literal_global.28
+ ___block_literal_global.65
+ _deviceClass.deviceClass
+ _deviceClass.onceToken
+ _objc_msgSend$App
+ _objc_msgSend$InFocus
+ _objc_msgSend$addObserverForKey:using:
+ _objc_msgSend$deviceClass
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$networkMonitorToken
+ _objc_msgSend$networkStateDidChange:
+ _objc_msgSend$publisherWithOptions:
+ _objc_msgSend$removeObserverForKey:
+ _objc_msgSend$starting
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_retain_n
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic BD
+ _symbolic SDy_____ySbYbcG 10Foundation4UUIDV
+ _symbolic SbIeghy_
+ _symbolic SbytIeghnr_
+ _symbolic ScPSg
+ _symbolic ScTyyt______pGSg s5ErrorP
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 7Network13NWPathMonitorC
+ _symbolic _____ 8TipsCore14NetworkMonitorC
+ _symbolic _____ 8TipsCore18SerialTaskExecutor33_3C3E78E32FD3541F35ED5B8FF99C55CALLC
+ _symbolic _____ 8TipsCore19NetworkMonitorProxyC
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s6UInt32V
+ _symbolic _____3key_yyc5valuet 10Foundation4UUIDV
+ _symbolic _____3key_yyc5valuetSg 10Foundation4UUIDV
+ _symbolic _____IeyBhy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg 7Network6NWPathV
+ _symbolic _____Sg 7Network6NWPathV6StatusO
+ _symbolic _____SgXw 8TipsCore14NetworkMonitorC
+ _symbolic _____SgXw 8TipsCore19NetworkMonitorProxyC
+ _symbolic _____SgXwz_Xx 8TipsCore14NetworkMonitorC
+ _symbolic _____SgXwz_Xx 8TipsCore19NetworkMonitorProxyC
+ _symbolic _____Sg_ABt 7Network6NWPathV6StatusO
+ _symbolic ______pIeghHzo_ s5ErrorP
+ _symbolic ______yyct 10Foundation4UUIDV
+ _symbolic _____y_____ySbYbcG s18_DictionaryStorageC 10Foundation4UUIDV
+ _symbolic _____yytG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yyt_____G s13ManagedBufferC So16os_unfair_lock_sV
- +[TPSNetworkPathMonitor sharedMonitor]
- -[TPSCommonDefines isMacUI]
- -[TPSCommonDefines isPadUI]
- -[TPSCommonDefines isPhoneUI]
- -[TPSNetworkPathMonitor .cxx_destruct]
- -[TPSNetworkPathMonitor _cancelPendingNotifications]
- -[TPSNetworkPathMonitor _initializeMonitorIfNeeded]
- -[TPSNetworkPathMonitor _initializeMonitor]
- -[TPSNetworkPathMonitor _networkPathUpdated:]
- -[TPSNetworkPathMonitor _notifyObserversWithDelay:usingBlock:]
- -[TPSNetworkPathMonitor _uninitializeMonitor]
- -[TPSNetworkPathMonitor addObserver:selector:]
- -[TPSNetworkPathMonitor currentPath]
- -[TPSNetworkPathMonitor dealloc]
- -[TPSNetworkPathMonitor description]
- -[TPSNetworkPathMonitor init]
- -[TPSNetworkPathMonitor isNetworkConstrained]
- -[TPSNetworkPathMonitor isNetworkError:]
- -[TPSNetworkPathMonitor isNetworkExpensive]
- -[TPSNetworkPathMonitor isNetworkReachable]
- -[TPSNetworkPathMonitor monitorQueue]
- -[TPSNetworkPathMonitor networkPathMonitorActive]
- -[TPSNetworkPathMonitor notifyTimer]
- -[TPSNetworkPathMonitor observers]
- -[TPSNetworkPathMonitor pathMonitor]
- -[TPSNetworkPathMonitor removeObserver:]
- -[TPSNetworkPathMonitor setCurrentPath:]
- -[TPSNetworkPathMonitor setMonitorQueue:]
- -[TPSNetworkPathMonitor setNetworkConstrained:]
- -[TPSNetworkPathMonitor setNetworkExpensive:]
- -[TPSNetworkPathMonitor setNetworkPathMonitorActive:]
- -[TPSNetworkPathMonitor setNetworkReachable:]
- -[TPSNetworkPathMonitor setNotifyTimer:]
- -[TPSNetworkPathMonitor setObservers:]
- -[TPSNetworkPathMonitor setPathMonitor:]
- -[TPSNetworkPathMonitor setShouldNotify:]
- -[TPSNetworkPathMonitor shouldNotify]
- -[TPSNetworkPathMonitor start]
- -[TPSNetworkPathMonitor stop]
- -[TPSNetworkPathMonitor usesCellularConnection]
- -[TPSNetworkPathMonitor usesWifiConnection]
- -[TPSWidgetController attemptWidgetUpdateWith:].cold.4
- -[TPSWidgetController updateWidgetDocumentWithDocumentsMap:documentsDeliveryInfoMap:deliveryInfoMap:preferHardwareWelcome:completionHandler:].cold.3
- GCC_except_table35
- GCC_except_table48
- GCC_except_table50
- _OBJC_CLASS_$_NSInvocation
- _OBJC_CLASS_$_NSMapTable
- _OBJC_IVAR_$_TPSCommonDefines._phoneUI
- _OBJC_IVAR_$_TPSNetworkPathMonitor._currentPath
- _OBJC_IVAR_$_TPSNetworkPathMonitor._monitorQueue
- _OBJC_IVAR_$_TPSNetworkPathMonitor._networkConstrained
- _OBJC_IVAR_$_TPSNetworkPathMonitor._networkExpensive
- _OBJC_IVAR_$_TPSNetworkPathMonitor._networkPathMonitorActive
- _OBJC_IVAR_$_TPSNetworkPathMonitor._networkReachable
- _OBJC_IVAR_$_TPSNetworkPathMonitor._notifyTimer
- _OBJC_IVAR_$_TPSNetworkPathMonitor._observers
- _OBJC_IVAR_$_TPSNetworkPathMonitor._pathMonitor
- _OBJC_IVAR_$_TPSNetworkPathMonitor._shouldNotify
- __OBJC_$_INSTANCE_VARIABLES_TPSNetworkPathMonitor
- __OBJC_$_PROP_LIST_TPSNetworkPathMonitor
- __OBJC_CLASS_RO_$_TPSNetworkPathMonitor
- __OBJC_METACLASS_RO_$_TPSNetworkPathMonitor
- ___141-[TPSWidgetController updateWidgetDocumentWithDocumentsMap:documentsDeliveryInfoMap:deliveryInfoMap:preferHardwareWelcome:completionHandler:]_block_invoke.24
- ___27-[TPSCommonDefines isMacUI]_block_invoke
- ___27-[TPSCommonDefines isPadUI]_block_invoke
- ___29-[TPSNetworkPathMonitor stop]_block_invoke
- ___30-[TPSNetworkPathMonitor start]_block_invoke
- ___38+[TPSNetworkPathMonitor sharedMonitor]_block_invoke
- ___40-[TPSNetworkPathMonitor removeObserver:]_block_invoke
- ___43-[TPSNetworkPathMonitor _initializeMonitor]_block_invoke
- ___43-[TPSNetworkPathMonitor isNetworkExpensive]_block_invoke
- ___43-[TPSNetworkPathMonitor isNetworkReachable]_block_invoke
- ___43-[TPSNetworkPathMonitor usesWifiConnection]_block_invoke
- ___45-[TPSNetworkPathMonitor _networkPathUpdated:]_block_invoke
- ___45-[TPSNetworkPathMonitor _networkPathUpdated:]_block_invoke.16
- ___45-[TPSNetworkPathMonitor isNetworkConstrained]_block_invoke
- ___46-[TPSNetworkPathMonitor addObserver:selector:]_block_invoke
- ___47-[TPSNetworkPathMonitor usesCellularConnection]_block_invoke
- ___62-[TPSNetworkPathMonitor _notifyObserversWithDelay:usingBlock:]_block_invoke
- ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
- ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32bs40r_e15_v16?0"NSURL"8lr40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_48_e8_32bs_e15_v16?0"NSURL"8ls32l8
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40bs48w_e25_v24?0"NSURL"8"NSURL"16lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e41_v32?0"TPSDocument"8"NSURL"16"NSURL"24lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.16
- ___block_literal_global.177
- ___block_literal_global.182
- ___block_literal_global.193
- ___block_literal_global.202
- ___block_literal_global.21
- ___block_literal_global.53
- __dispatch_source_type_timer
- _dispatch_assert_queue$V2
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _dispatch_time
- _isMacUI.isMac
- _isMacUI.onceToken
- _isPadUI.isiPad
- _isPadUI.onceToken
- _nw_path_create_evaluator_for_endpoint
- _nw_path_evaluator_copy_path
- _nw_path_get_status
- _nw_path_is_constrained
- _nw_path_is_equal
- _nw_path_is_expensive
- _nw_path_monitor_cancel
- _nw_path_monitor_create
- _nw_path_monitor_set_queue
- _nw_path_monitor_set_update_handler
- _nw_path_monitor_start
- _nw_path_uses_interface_type
- _objc_msgSend$_cancelPendingNotifications
- _objc_msgSend$_initializeMonitor
- _objc_msgSend$_initializeMonitorIfNeeded
- _objc_msgSend$_networkPathUpdated:
- _objc_msgSend$_notifyObserversWithDelay:usingBlock:
- _objc_msgSend$_uninitializeMonitor
- _objc_msgSend$addObserver:selector:
- _objc_msgSend$currentPath
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$isNetworkReachable
- _objc_msgSend$monitorQueue
- _objc_msgSend$networkPathMonitorActive
- _objc_msgSend$notifyTimer
- _objc_msgSend$observers
- _objc_msgSend$pathMonitor
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setNetworkPathMonitorActive:
- _objc_msgSend$setNotifyTimer:
- _objc_msgSend$setPathMonitor:
- _objc_msgSend$setSelector:
- _objc_msgSend$setShouldNotify:
- _objc_msgSend$setTarget:
- _objc_msgSend$shouldNotify
- _objc_msgSend$weakToStrongObjectsMapTable
- _sharedMonitor.onceToken
- _sharedMonitor.s_networkMonitor
CStrings:
+ "\x1f\x01"
+ "$defaultActor"
+ "@\"NSUUID\""
+ "App"
+ "App.InFocus"
+ "Asset not available in document %@"
+ "B24@?0@\"BMAppInFocus\"8@\"NSDictionary\"16"
+ "InFocus"
+ "Network status change detected: "
+ "RealityDevice"
+ "T@\"NSUUID\",&,N,V_networkMonitorToken"
+ "T@\"TPSNetworkPathMonitor\",N,R"
+ "TPSContextualBiomeAppInFocusEvent"
+ "TPSURLSessionError"
+ "TipsCore.NetworkMonitorProxy"
+ "_TtC8TipsCore14NetworkMonitor"
+ "_TtC8TipsCoreP33_3C3E78E32FD3541F35ED5B8FF99C55CA18SerialTaskExecutor"
+ "_networkMonitorToken"
+ "addObserverForKey:using:"
+ "apple-vision"
+ "com.apple.tips.TPSWidgetController"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "isVisionUI"
+ "lastNetworkPath"
+ "monitor"
+ "monitoringTask"
+ "networkMonitorToken"
+ "organic"
+ "previousTask"
+ "publisherWithOptions:"
+ "removeObserverForKey:"
+ "serialTasks"
+ "setNetworkMonitorToken:"
+ "starting"
+ "v12@?0B8"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v32@?0@\"NSURL\"8@\"NSURL\"16@\"NSError\"24"
+ "v40@?0@\"TPSDocument\"8@\"NSURL\"16@\"NSURL\"24@\"NSError\"32"
- "\x15"
- "\x1f"
- "<%@: %p path=%@ reachable=%@ active=%@]>"
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_nw_path>\""
- "@\"NSObject<OS_nw_path_monitor>\""
- "NO"
- "Network reachability changed (%{public}i -> %{public}i). Notifying observers"
- "Overriding widget document from client failed. Network unreachable...skipping update"
- "T@\"NSMapTable\",&,N,V_observers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_monitorQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_notifyTimer"
- "T@\"NSObject<OS_nw_path>\",&,N,V_currentPath"
- "T@\"NSObject<OS_nw_path_monitor>\",&,N,V_pathMonitor"
- "TB,N,GisNetworkConstrained,V_networkConstrained"
- "TB,N,GisNetworkExpensive,V_networkExpensive"
- "TB,N,GisNetworkReachable,V_networkReachable"
- "TB,N,V_networkPathMonitorActive"
- "TB,N,V_shouldNotify"
- "TB,R,D,N,GisPadUI"
- "TB,R,N,GisMacUI"
- "TB,R,N,GisPhoneUI,V_phoneUI"
- "Unknown error"
- "Updating with new path. Reachable: %{public}i, Cellular: %{public}i, Expensive: %{public}i, Constrained: %{public}i"
- "YES"
- "_cancelPendingNotifications"
- "_currentPath"
- "_initializeMonitor"
- "_initializeMonitorIfNeeded"
- "_monitorQueue"
- "_networkConstrained"
- "_networkExpensive"
- "_networkPathMonitorActive"
- "_networkPathUpdated:"
- "_networkReachable"
- "_notifyObserversWithDelay:usingBlock:"
- "_notifyTimer"
- "_observers"
- "_pathMonitor"
- "_phoneUI"
- "_shouldNotify"
- "_uninitializeMonitor"
- "addObserver:selector:"
- "com.apple.tips.NetworkPathMonitor"
- "currentPath"
- "invocationWithMethodSignature:"
- "invoke"
- "isNetworkConstrained"
- "isNetworkExpensive"
- "isNetworkReachable"
- "macUI"
- "monitorQueue"
- "networkConstrained"
- "networkExpensive"
- "networkPathMonitorActive"
- "networkReachable"
- "notifyTimer"
- "padUI"
- "phoneUI"
- "removeObserver:"
- "setArgument:atIndex:"
- "setCurrentPath:"
- "setMonitorQueue:"
- "setNetworkConstrained:"
- "setNetworkExpensive:"
- "setNetworkPathMonitorActive:"
- "setNetworkReachable:"
- "setNotifyTimer:"
- "setObservers:"
- "setPathMonitor:"
- "setSelector:"
- "setShouldNotify:"
- "setTarget:"
- "shouldNotify"
- "usesCellularConnection"
- "usesWifiConnection"
- "v16@?0@\"NSObject<OS_nw_path>\"8"
- "v32@0:8@16:24"
- "v32@0:8d16@?24"
- "v32@?0@\"TPSDocument\"8@\"NSURL\"16@\"NSURL\"24"
- "weakToStrongObjectsMapTable"

```

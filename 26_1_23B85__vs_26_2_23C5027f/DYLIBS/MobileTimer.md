## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2303.1.8.101.0
-  __TEXT.__text: 0x1082dc
-  __TEXT.__auth_stubs: 0x1830
-  __TEXT.__objc_methlist: 0xd7cc
-  __TEXT.__const: 0x1540
-  __TEXT.__oslogstring: 0x10ff3
-  __TEXT.__cstring: 0x9656
-  __TEXT.__gcc_except_tab: 0x14ac
+2303.2.1.0.0
+  __TEXT.__text: 0x10c02c
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_methlist: 0xd92c
+  __TEXT.__const: 0x1730
+  __TEXT.__oslogstring: 0x11023
+  __TEXT.__cstring: 0x9816
+  __TEXT.__gcc_except_tab: 0x14a8
   __TEXT.__dlopen_cstrs: 0x837
   __TEXT.__ustring: 0x1a
-  __TEXT.__swift5_typeref: 0x904
-  __TEXT.__swift5_reflstr: 0x2ad
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0x548
-  __TEXT.__swift5_fieldmd: 0x334
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x64
-  __TEXT.__swift5_capture: 0xf88
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift_as_entry: 0x104
-  __TEXT.__swift_as_ret: 0x108
-  __TEXT.__unwind_info: 0x4968
-  __TEXT.__eh_frame: 0x30c0
+  __TEXT.__swift5_typeref: 0xa18
+  __TEXT.__swift5_reflstr: 0x31d
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__constg_swiftt: 0x610
+  __TEXT.__swift5_fieldmd: 0x3b8
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x74
+  __TEXT.__swift5_capture: 0x108c
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift_as_entry: 0x120
+  __TEXT.__swift_as_ret: 0x124
+  __TEXT.__unwind_info: 0x46b8
+  __TEXT.__eh_frame: 0x32d8
   __TEXT.__objc_classname: 0x1955
-  __TEXT.__objc_methname: 0x17f2a
-  __TEXT.__objc_methtype: 0x4248
-  __TEXT.__objc_stubs: 0x11d60
-  __DATA_CONST.__got: 0xc48
-  __DATA_CONST.__const: 0x42b8
-  __DATA_CONST.__objc_classlist: 0x688
+  __TEXT.__objc_methname: 0x180f9
+  __TEXT.__objc_methtype: 0x42ac
+  __TEXT.__objc_stubs: 0x11e20
+  __DATA_CONST.__got: 0xc78
+  __DATA_CONST.__const: 0x42c8
+  __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6060
+  __DATA_CONST.__objc_selrefs: 0x60d8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc28
-  __AUTH_CONST.__const: 0x39e0
+  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__const: 0x3ce8
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x28d90
+  __AUTH_CONST.__objc_const: 0x29028
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2da0
-  __AUTH.__data: 0x3c8
-  __DATA.__objc_ivar: 0x960
-  __DATA.__data: 0x2b38
+  __AUTH.__objc_data: 0x2f38
+  __AUTH.__data: 0x4b8
+  __DATA.__objc_ivar: 0x968
+  __DATA.__data: 0x2ba8
   __DATA.__common: 0x68
-  __DATA.__bss: 0x11a0
+  __DATA.__bss: 0x13a0
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AlarmKitFoundation.framework/AlarmKitFoundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 90A84166-2BFF-308B-8272-B75B5F57C804
-  Functions: 6604
-  Symbols:   18360
-  CStrings:  8390
+  UUID: 09ACAE60-1F6C-34D5-8031-8DC125104189
+  Functions: 6719
+  Symbols:   18449
+  CStrings:  8428
 
Symbols:
+ -[MTAlarmKit _withLock:]
+ -[MTAlarmKit lock]
+ -[MTAlarmKit setLock:]
+ -[MTStopwatchManager eventCore]
+ -[MTStopwatchManager registerDeleteEventBlock:forObserver:]
+ -[MTStopwatchManager registerRefreshBlock:forObserver:]
+ -[MTStopwatchManager registerUpdateEventBlock:forObserver:]
+ -[MTStopwatchManager setEventCore:]
+ -[MTStopwatchManager unregisterObserver:]
+ -[MTStopwatchManagerExportedObject _didReceiveStopwatchServerReadyNotification:]
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$__TtC11MobileTimer11ChannelCore
+ _OBJC_CLASS_$__TtC11MobileTimer12ChannelEvent
+ _OBJC_IVAR_$_MTAlarmKit._lock
+ _OBJC_IVAR_$_MTStopwatchManager._eventCore
+ _OBJC_METACLASS_$__TtC11MobileTimer11ChannelCore
+ _OBJC_METACLASS_$__TtC11MobileTimer12ChannelEvent
+ __CLASS_METHODS__TtC11MobileTimer12ChannelEvent
+ __DATA__TtC11MobileTimer11ChannelCore
+ __DATA__TtC11MobileTimer12ChannelEvent
+ __DATA__TtC11MobileTimerP33_11DD200D293CC9F5FDAB771F4826812915CallbackWrapper
+ __INSTANCE_METHODS__TtC11MobileTimer11ChannelCore
+ __INSTANCE_METHODS__TtC11MobileTimer12ChannelEvent
+ __IVARS__TtC11MobileTimer11ChannelCore
+ __IVARS__TtC11MobileTimer12ChannelEvent
+ __IVARS__TtC11MobileTimerP33_11DD200D293CC9F5FDAB771F4826812915CallbackWrapper
+ __METACLASS_DATA__TtC11MobileTimer11ChannelCore
+ __METACLASS_DATA__TtC11MobileTimer12ChannelEvent
+ __METACLASS_DATA__TtC11MobileTimerP33_11DD200D293CC9F5FDAB771F4826812915CallbackWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTStopwatchManagerProtocol
+ ___35-[MTAlarmKit didFinishLoadingStore]_block_invoke
+ ___36-[MTStopwatchManager getStopwatches]_block_invoke.56
+ ___55-[MTAlarmKit initWithCoreDataStore:notificationCenter:]_block_invoke
+ ___80-[MTStopwatchManagerExportedObject _didReceiveStopwatchServerReadyNotification:]_block_invoke
+ ___80-[MTStopwatchManagerExportedObject _didReceiveStopwatchServerReadyNotification:]_block_invoke_2
+ ___block_literal_global.54
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 11MobileTimer16ChannelEventNameOSHAASQ
+ _associated conformance 11MobileTimer16ChannelEventNameOs12CaseIterableAA8AllCasessADP_Sl
+ _block_copy_helper.20
+ _block_descriptor.22
+ _block_destroy_helper.21
+ _objc_msgSend$eventCore
+ _objc_msgSend$name:
+ _objc_msgSend$refreshWithPayload:
+ _objc_msgSend$sendWithEvent:completionHandler:
+ _objc_msgSend$subscribeWithCallback:forObserver:eventName:
+ _objc_msgSend$unsubscribeWithObserver:
+ _objectdestroy.35Tm
+ _swift_deletedMethodError
+ _symbolic $ss12CaseIterableP
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic IeyB_
+ _symbolic SDyS2SGSg
+ _symbolic SDySSSo10NSMapTableCySo8NSObjectC_____GG 11MobileTimer15CallbackWrapper33_11DD200D293CC9F5FDAB771F48268129LLC
+ _symbolic Say_____G 11MobileTimer15CallbackWrapper33_11DD200D293CC9F5FDAB771F48268129LLC
+ _symbolic Say_____G 11MobileTimer16ChannelEventNameO
+ _symbolic Si
+ _symbolic So12NSDictionaryCSgIeyBy_
+ _symbolic _____ 11MobileTimer11ChannelCoreC
+ _symbolic _____ 11MobileTimer12ChannelEventC
+ _symbolic _____ 11MobileTimer15CallbackWrapper33_11DD200D293CC9F5FDAB771F48268129LLC
+ _symbolic _____ 11MobileTimer16ChannelEventNameO
+ _symbolic _____SgXw 11MobileTimer11ChannelCoreC
+ _symbolic _____SgXwz_Xx 11MobileTimer11ChannelCoreC
+ _symbolic _____ySSSo10NSMapTableCG s18_DictionaryStorageC
+ _symbolic _____y_____G 23AsyncAlgorithmsInternal0A7ChannelC 11MobileTimer0D5EventC
+ _symbolic _____y______G 23AsyncAlgorithmsInternal0A7ChannelC8IteratorV 11MobileTimer0D5EventC
+ _symbolic ySDyS2SGSgXB
- -[MTStopwatchManagerExportedObject _didReceiveTimerServerReadyNotification:]
- ___36-[MTStopwatchManager getStopwatches]_block_invoke.55
- ___76-[MTStopwatchManagerExportedObject _didReceiveTimerServerReadyNotification:]_block_invoke
CStrings:
+ "%{public}@ end of initializing"
+ "%{public}@ received didFinishLoadingStore, proceeding to start AlarmKit: %{public}@"
+ "@\"_TtC11MobileTimer11ChannelCore\""
+ "MobileTimer.ChannelEvent"
+ "T@\"_TtC11MobileTimer11ChannelCore\",&,N,V_eventCore"
+ "_TtC11MobileTimer11ChannelCore"
+ "_TtC11MobileTimer12ChannelEvent"
+ "_TtC11MobileTimerP33_11DD200D293CC9F5FDAB771F4826812915CallbackWrapper"
+ "_didReceiveStopwatchServerReadyNotification:"
+ "_eventCore"
+ "callback"
+ "channel"
+ "com.apple.mobiletimer.eventchannel"
+ "deleteWithPayload:"
+ "eventCore"
+ "eventTask"
+ "init()"
+ "initWithEventName:payload:"
+ "name:"
+ "observersByEventName"
+ "observersQueue"
+ "payload"
+ "refreshWithPayload:"
+ "registerDeleteEventBlock:forObserver:"
+ "registerRefreshBlock:forObserver:"
+ "registerUpdateEventBlock:forObserver:"
+ "sendWithEvent:completionHandler:"
+ "setEventCore:"
+ "subscribeWithCallback:forObserver:eventName:"
+ "unsubscribeWithObserver:"
+ "updateWithPayload:"
+ "v24@0:8@\"NSObject\"16"
+ "v32@0:8@\"_TtC11MobileTimer12ChannelEvent\"16@?<v@?>24"
+ "v32@0:8@?<v@?@\"NSDictionary\">16@\"NSObject\"24"
+ "v40@0:8@?16@24@32"
+ "weakToStrongObjectsMapTable"
- "%{public}@ received didFinishLoadingStore, proceeding to start AlarmKit"

```

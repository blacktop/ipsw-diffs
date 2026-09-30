## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.0.31.0.0
-  __TEXT.__text: 0xf7d00
-  __TEXT.__auth_stubs: 0x1750
+13.0.32.0.0
+  __TEXT.__text: 0xf93e8
+  __TEXT.__auth_stubs: 0x1780
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xf924
+  __TEXT.__objc_methlist: 0xfa3c
   __TEXT.__const: 0x3364
-  __TEXT.__cstring: 0x9b67
-  __TEXT.__gcc_except_tab: 0x56f0
-  __TEXT.__oslogstring: 0x9672
+  __TEXT.__cstring: 0x9da4
+  __TEXT.__gcc_except_tab: 0x578c
+  __TEXT.__oslogstring: 0x9729
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x2ac
   __TEXT.__swift5_reflstr: 0x13f

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x4fe8
-  __TEXT.__objc_classname: 0x40a7
-  __TEXT.__objc_methname: 0x1880f
-  __TEXT.__objc_methtype: 0x79ee
-  __TEXT.__objc_stubs: 0xefc0
+  __TEXT.__unwind_info: 0x5088
+  __TEXT.__objc_classname: 0x410f
+  __TEXT.__objc_methname: 0x189ea
+  __TEXT.__objc_methtype: 0x7a51
+  __TEXT.__objc_stubs: 0xf0c0
   __DATA_CONST.__got: 0xb28
-  __DATA_CONST.__const: 0x2ce0
-  __DATA_CONST.__objc_classlist: 0x940
+  __DATA_CONST.__const: 0x2d58
+  __DATA_CONST.__objc_classlist: 0x958
   __DATA_CONST.__objc_catlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x798
+  __DATA_CONST.__objc_protolist: 0x7a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5100
+  __DATA_CONST.__objc_selrefs: 0x5148
   __DATA_CONST.__objc_protorefs: 0x4b8
-  __DATA_CONST.__objc_superrefs: 0x888
+  __DATA_CONST.__objc_superrefs: 0x8a0
   __DATA_CONST.__objc_arraydata: 0x570
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH_CONST.__const: 0x1418
-  __AUTH_CONST.__cfstring: 0xb080
-  __AUTH_CONST.__objc_const: 0x47c90
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__const: 0x1438
+  __AUTH_CONST.__cfstring: 0xb240
+  __AUTH_CONST.__objc_const: 0x480c0
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x5190
+  __AUTH.__objc_data: 0x5280
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x1724
-  __DATA.__data: 0x5b90
+  __DATA.__objc_ivar: 0x1764
+  __DATA.__data: 0x5bf0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1540
+  __DATA.__bss: 0x1550
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 6B44FD7B-3735-3BB0-BBD6-6C831CC64631
-  Functions: 6899
-  Symbols:   25766
-  CStrings:  9551
+  UUID: 6572BB63-E951-3163-9715-B684C58E32D6
+  Functions: 6942
+  Symbols:   25915
+  CStrings:  9619
 
Symbols:
+ +[_GCCurrentApplicationForegroundMonitor currentProcessFollowsRegularActivationPolicy]
+ +[_GCGameOverlayMonitor currentProcessIsOverlayUI]
+ +[_GCGameOverlayMonitor currentProcessIsOverlayUI].cold.1
+ +[_GCGameOverlayMonitor sharedInstance]
+ +[_GCGameOverlayMonitor sharedInstance].cold.1
+ -[GCDeviceSession gameOverlayPresentationChanged:]
+ -[_GCCurrentApplicationForegroundMonitor dealloc]
+ -[_GCGameOverlayMonitor .cxx_destruct]
+ -[_GCGameOverlayMonitor _refreshState]
+ -[_GCGameOverlayMonitor addObserver:]
+ -[_GCGameOverlayMonitor addObserver:notifyCurrent:]
+ -[_GCGameOverlayMonitor dealloc]
+ -[_GCGameOverlayMonitor init]
+ -[_GCGameOverlayMonitor init].cold.1
+ -[_GCGameOverlayMonitor isOverlayPresented]
+ -[_GCGameOverlayMonitor removeObserver:]
+ -[_GCGameOverlayMonitor setOverlayPresented:]
+ -[_GCHIDEventSubject isPaused]
+ -[_GCHIDEventSubject pausedForReasons]
+ -[_GCHIDEventSubject setPausedForReasons:]
+ -[_GCHIDEventSubjectAuditor .cxx_destruct]
+ -[_GCHIDEventSubjectAuditor dealloc]
+ -[_GCHIDEventSubjectAuditor initWithSubject:]
+ -[_GCHIDEventSubjectAuditor init]
+ -[_GCHIDEventSubjectAuditor noteEventPublicationPausedForReasonsChanged:]
+ -[_GCHIDEventSubjectAuditor noteHIDEventPublished:]
+ -[_GCHIDEventSubjectAuditor noteHIDEventReceived:]
+ -[_GCHIDEventSubjectAuditor noteObserverAddedForService:]
+ -[_GCHIDServiceAuditor .cxx_destruct]
+ -[_GCHIDServiceAuditor initWithServiceInfo:]
+ -[_GCHIDServiceAuditor noteHIDEventPublished:]
+ -[_GCHIDServiceAuditor noteHIDEventReceived:]
+ -[_GCHIDServiceAuditor serviceInfo]
+ -[_GCHIDServiceAuditor state]
+ GCC_except_table80
+ _OBJC_CLASS_$__GCGameOverlayMonitor
+ _OBJC_CLASS_$__GCHIDEventSubjectAuditor
+ _OBJC_CLASS_$__GCHIDServiceAuditor
+ _OBJC_IVAR_$__GCCurrentApplicationForegroundMonitor._state
+ _OBJC_IVAR_$__GCGameOverlayMonitor._observers
+ _OBJC_IVAR_$__GCGameOverlayMonitor._overlayPresentationObserver
+ _OBJC_IVAR_$__GCGameOverlayMonitor._overlayPresented
+ _OBJC_IVAR_$__GCGameOverlayMonitor._state
+ _OBJC_IVAR_$__GCGameOverlayMonitor.stats
+ _OBJC_IVAR_$__GCHIDEventSubject._auditor
+ _OBJC_IVAR_$__GCHIDEventSubject._pausedForReasons
+ _OBJC_IVAR_$__GCHIDEventSubjectAuditor._lock
+ _OBJC_IVAR_$__GCHIDEventSubjectAuditor._pausedForReasonsChangeCount
+ _OBJC_IVAR_$__GCHIDEventSubjectAuditor._serviceAuditors
+ _OBJC_IVAR_$__GCHIDEventSubjectAuditor._state
+ _OBJC_IVAR_$__GCHIDEventSubjectAuditor._subject
+ _OBJC_IVAR_$__GCHIDServiceAuditor._latestReceivedEvents
+ _OBJC_IVAR_$__GCHIDServiceAuditor._publishedEventCount
+ _OBJC_IVAR_$__GCHIDServiceAuditor._receivedEventCount
+ _OBJC_IVAR_$__GCHIDServiceAuditor._serviceInfo
+ _OBJC_METACLASS_$__GCGameOverlayMonitor
+ _OBJC_METACLASS_$__GCHIDEventSubjectAuditor
+ _OBJC_METACLASS_$__GCHIDServiceAuditor
+ __OBJC_$_CLASS_METHODS__GCGameOverlayMonitor
+ __OBJC_$_CLASS_PROP_LIST__GCCurrentApplicationForegroundMonitor
+ __OBJC_$_CLASS_PROP_LIST__GCGameOverlayMonitor
+ __OBJC_$_INSTANCE_METHODS__GCGameOverlayMonitor
+ __OBJC_$_INSTANCE_METHODS__GCHIDEventSubjectAuditor
+ __OBJC_$_INSTANCE_METHODS__GCHIDServiceAuditor
+ __OBJC_$_INSTANCE_VARIABLES__GCGameOverlayMonitor
+ __OBJC_$_INSTANCE_VARIABLES__GCHIDEventSubjectAuditor
+ __OBJC_$_INSTANCE_VARIABLES__GCHIDServiceAuditor
+ __OBJC_$_PROP_LIST_GCDeviceSession.430
+ __OBJC_$_PROP_LIST__GCGameOverlayMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCGameOverlayPresentationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCGameOverlayPresentationObserver
+ __OBJC_CLASS_RO_$__GCGameOverlayMonitor
+ __OBJC_CLASS_RO_$__GCHIDEventSubjectAuditor
+ __OBJC_CLASS_RO_$__GCHIDServiceAuditor
+ __OBJC_LABEL_PROTOCOL_$__GCGameOverlayPresentationObserver
+ __OBJC_METACLASS_RO_$__GCGameOverlayMonitor
+ __OBJC_METACLASS_RO_$__GCHIDEventSubjectAuditor
+ __OBJC_METACLASS_RO_$__GCHIDServiceAuditor
+ __OBJC_PROTOCOL_$__GCGameOverlayPresentationObserver
+ ___29-[_GCGameOverlayMonitor init]_block_invoke
+ ___29-[_GCGameOverlayMonitor init]_block_invoke.89
+ ___29-[_GCGameOverlayMonitor init]_block_invoke_2
+ ___39+[_GCGameOverlayMonitor sharedInstance]_block_invoke
+ ___45-[_GCHIDEventSubjectAuditor initWithSubject:]_block_invoke
+ ___45-[_GCHIDEventSubjectAuditor initWithSubject:]_block_invoke_2
+ ___46-[_GCCurrentApplicationForegroundMonitor init]_block_invoke
+ ___50+[_GCGameOverlayMonitor currentProcessIsOverlayUI]_block_invoke
+ ___51-[_GCGameOverlayMonitor addObserver:notifyCurrent:]_block_invoke
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239.cold.1
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239.cold.2
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239.cold.3
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239.cold.4
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.239.cold.5
+ ___block_descriptor_40_e8_32s_e47_v32?0"NSNumber"8"_GCHIDServiceAuditor"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e65_"NSString"24?0^{os_state_hints_s=I*II}8"NSMutableDictionary"16lw32l8
+ ___block_descriptor_44_e8_32bs_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8ls32l8
+ ___block_literal_global.228
+ ___block_literal_global.236
+ ___block_literal_global.241
+ ___block_literal_global.249
+ ___gc_state_add_dictionary_handler_block_invoke
+ __gc_state_dictionary_builder
+ _currentProcessIsOverlayUI.IsGameOverlayUI
+ _currentProcessIsOverlayUI.onceToken
+ _objc_msgSend$currentProcessFollowsRegularActivationPolicy
+ _objc_msgSend$gameOverlayPresentationChanged:
+ _objc_msgSend$gc_dateWithMachAbsoluteTime:
+ _objc_msgSend$isOverlayPresented
+ _objc_msgSend$isPaused
+ _objc_msgSend$pausedForReasons
+ _objc_msgSend$serviceID
+ _objc_msgSend$setOverlayPresented:
+ _objc_msgSend$setPausedForReasons:
+ _os_state_add_handler
+ _os_state_remove_handler
- -[_GCHIDEventSubject isStopped]
- -[_GCHIDEventSubject setStopped:]
- _OBJC_IVAR_$__GCHIDEventSubject._stopped
- __OBJC_$_PROP_LIST_GCDeviceSession.428
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.226.cold.7
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.228
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245.cold.1
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245.cold.2
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245.cold.3
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245.cold.4
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.245.cold.5
- ___block_literal_global.231
- ___block_literal_global.238
- ___block_literal_global.250
- _kGlyphFlagProtocolXboxLogo_block_invoke.settingsUserDefaults
- _objc_msgSend$isStopped
CStrings:
+ "%#010llx"
+ "@\"NSString\"24@?0^{os_state_hints_s=I*II}8@\"NSMutableDictionary\"16"
+ "@\"_GCHIDEventSubjectAuditor\""
+ "AQ"
+ "Failed load 'dashboardVisibilityChanged' notification state: %#x"
+ "Failed to register for 'dashboardVisibilityChanged' notification: %#x"
+ "FollowsRegularActivationPolicy"
+ "GCCurrentApplicationForegroundMonitor"
+ "GCGameOverlayMonitor"
+ "GCHIDEventSubject"
+ "Game Overlay Dismissed"
+ "Game Overlay Presented"
+ "IsInBackground"
+ "LatestReceivedEventTimes"
+ "OverlayIsPresented"
+ "OverlayPresentationStateChangedCount"
+ "PausedForReasons"
+ "PausedForReasonsChangeCount"
+ "PublishedEventCount"
+ "ReceivedEventCount"
+ "Session event delivery policy will change: %{public}@"
+ "T@\"GCSProfile\",R"
+ "T@\"GCSProfile\",R,V_settingsProfile"
+ "T@\"NSSet\",C"
+ "TB,R,GisOverlayPresented"
+ "TB,R,GisPaused"
+ "[5{?=\"eventTimestampMAT\"Q}]"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_GCGameOverlayMonitor"
+ "_GCGameOverlayPresentationObserver"
+ "_GCHIDEventSubjectAuditor"
+ "_GCHIDServiceAuditor"
+ "_auditor"
+ "_latestReceivedEvents"
+ "_overlayPresentationObserver"
+ "_overlayPresented"
+ "_pausedForReasons"
+ "_pausedForReasonsChangeCount"
+ "_publishedEventCount"
+ "_receivedEventCount"
+ "_serviceAuditors"
+ "_subject"
+ "com.apple.GameOverlayUI"
+ "com.apple.GameOverlayUI.dashboardVisibilityChanged"
+ "currentProcessFollowsRegularActivationPolicy"
+ "currentProcessIsOverlayUI"
+ "gameOverlayPresentationChanged:"
+ "gc_dateWithMachAbsoluteTime:"
+ "isOverlayPresented"
+ "isPaused"
+ "overlayPresented"
+ "paused"
+ "pausedForReasons"
+ "serviceID"
+ "setOverlayPresented:"
+ "setPausedForReasons:"
+ "stats"
+ "v32@?0@\"NSNumber\"8@\"_GCHIDServiceAuditor\"16^B24"
+ "{?=\"overlayPresentationChangedCount\"Q}"
- "Session event delivery polict will change: %{BOOL}d"
- "T@\"GCSProfile\",R,N"
- "T@\"GCSProfile\",R,N,V_settingsProfile"
- "TB,GisStopped"
- "bluetoothPrefsMenuLongPressAction"
- "isStopped"

```

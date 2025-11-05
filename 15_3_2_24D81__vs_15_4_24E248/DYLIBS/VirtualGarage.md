## VirtualGarage

> `/System/Library/PrivateFrameworks/VirtualGarage.framework/Versions/A/VirtualGarage`

```diff

-2340.23.11.14.1
-  __TEXT.__text: 0x25860
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x16b4
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x281b
-  __TEXT.__oslogstring: 0x37ca
-  __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__unwind_info: 0x7f8
-  __TEXT.__objc_classname: 0x368
-  __TEXT.__objc_methname: 0x4206
-  __TEXT.__objc_methtype: 0xb5e
-  __TEXT.__objc_stubs: 0x3460
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__objc_classlist: 0x90
+2340.24.9.12.11
+  __TEXT.__text: 0x26e00
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x1c34
+  __TEXT.__const: 0x170
+  __TEXT.__cstring: 0x28f6
+  __TEXT.__oslogstring: 0x3ad4
+  __TEXT.__gcc_except_tab: 0xeec
+  __TEXT.__unwind_info: 0x848
+  __TEXT.__objc_classname: 0x3c2
+  __TEXT.__objc_methname: 0x43eb
+  __TEXT.__objc_methtype: 0xbbf
+  __TEXT.__objc_stubs: 0x35e0
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x1020
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfd8
+  __DATA_CONST.__objc_selrefs: 0x10d0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x34c0
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x13a0
+  __AUTH_CONST.__objc_const: 0x2fd8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1dc
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x940
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_ivar: 0x58
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 793CB833-D52E-393B-BDCD-967885DBA783
-  Functions: 671
-  Symbols:   1917
-  CStrings:  1566
+  UUID: 7FD004D6-B55E-3596-B290-C33FE6EA9282
+  Functions: 694
+  Symbols:   1991
+  CStrings:  1618
 
Symbols:
+ +[VGOEMExtensionConnectionBroker sharedInstance]
+ -[VGChargingNetworkAvailabilityProvider countryCodeDidChange:]
+ -[VGOEMExtensionConnectionBroker .cxx_destruct]
+ -[VGOEMExtensionConnectionBroker _connectionWithIntent:]
+ -[VGOEMExtensionConnectionBroker init]
+ -[VGOEMExtensionConnectionBroker resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:]
+ -[_VGOEMExtensionConnection .cxx_destruct]
+ -[_VGOEMExtensionConnection _complete]
+ -[_VGOEMExtensionConnection addConnectionErrorHandler:]
+ -[_VGOEMExtensionConnection addConnectionTimeoutHandler:]
+ -[_VGOEMExtensionConnection addIntentCompletionHandler:]
+ -[_VGOEMExtensionConnection dealloc]
+ -[_VGOEMExtensionConnection initWithConnection:]
+ -[_VGOEMExtensionConnection resumeWithCompletion:]
+ -[_VGOEMExtensionConnectionKey .cxx_destruct]
+ -[_VGOEMExtensionConnectionKey description]
+ -[_VGOEMExtensionConnectionKey hash]
+ -[_VGOEMExtensionConnectionKey initWithIntent:]
+ -[_VGOEMExtensionConnectionKey isEqual:]
+ GCC_except_table24
+ OBJC_IVAR_$_VGOEMExtensionConnectionBroker._extensionMap
+ OBJC_IVAR_$_VGOEMExtensionConnectionBroker._lock
+ OBJC_IVAR_$__VGOEMExtensionConnection._completion
+ OBJC_IVAR_$__VGOEMExtensionConnection._completionLock
+ OBJC_IVAR_$__VGOEMExtensionConnection._connection
+ OBJC_IVAR_$__VGOEMExtensionConnection._connectionErrorHandlers
+ OBJC_IVAR_$__VGOEMExtensionConnection._connectionTimeoutHandlers
+ OBJC_IVAR_$__VGOEMExtensionConnection._handlersLock
+ OBJC_IVAR_$__VGOEMExtensionConnection._intentCompletionHandlers
+ OBJC_IVAR_$__VGOEMExtensionConnectionKey._intent
+ _GEOCountryConfigurationCountryCodeDidChangeNotification
+ _OBJC_$_PROP_LIST_VGOEMApplication.184
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_VGOEMExtensionConnectionBroker
+ _OBJC_CLASS_$__VGOEMExtensionConnection
+ _OBJC_CLASS_$__VGOEMExtensionConnectionKey
+ _OBJC_METACLASS_$_VGOEMExtensionConnectionBroker
+ _OBJC_METACLASS_$__VGOEMExtensionConnection
+ _OBJC_METACLASS_$__VGOEMExtensionConnectionKey
+ _VGGetVGOEMExtensionConnectionBrokerLog
+ _VGGetVGOEMExtensionConnectionLog
+ __43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.31
+ __43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.32
+ __50-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke.22
+ __55-[VGOEMApplication stopSendingChargeUpdatesForVehicle:]_block_invoke.59
+ __56-[VGOEMApplication startSendingChargeUpdatesForVehicle:]_block_invoke.57
+ __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.37
+ __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.38
+ __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.39
+ __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.51
+ __OBJC_$_CLASS_METHODS_VGOEMExtensionConnectionBroker
+ __OBJC_$_CLASS_PROP_LIST_VGOEMExtensionConnectionBroker
+ __OBJC_$_INSTANCE_METHODS_VGOEMExtensionConnectionBroker
+ __OBJC_$_INSTANCE_METHODS__VGOEMExtensionConnection
+ __OBJC_$_INSTANCE_METHODS__VGOEMExtensionConnectionKey
+ __OBJC_$_INSTANCE_VARIABLES_VGOEMExtensionConnectionBroker
+ __OBJC_$_INSTANCE_VARIABLES__VGOEMExtensionConnection
+ __OBJC_$_INSTANCE_VARIABLES__VGOEMExtensionConnectionKey
+ __OBJC_CLASS_RO_$_VGOEMExtensionConnectionBroker
+ __OBJC_CLASS_RO_$__VGOEMExtensionConnection
+ __OBJC_CLASS_RO_$__VGOEMExtensionConnectionKey
+ __OBJC_METACLASS_RO_$_VGOEMExtensionConnectionBroker
+ __OBJC_METACLASS_RO_$__VGOEMExtensionConnection
+ __OBJC_METACLASS_RO_$__VGOEMExtensionConnectionKey
+ ___133-[VGOEMExtensionConnectionBroker resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:]_block_invoke
+ ___48+[VGOEMExtensionConnectionBroker sharedInstance]_block_invoke
+ ___48-[_VGOEMExtensionConnection initWithConnection:]_block_invoke
+ ___50-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke
+ ___62-[VGChargingNetworkAvailabilityProvider countryCodeDidChange:]_block_invoke
+ ___VGGetVGOEMExtensionConnectionBrokerLog_block_invoke
+ ___VGGetVGOEMExtensionConnectionLog_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e48_v24?0"INIntentResponse"8"INCExtensionError"16lw32l8
+ ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e56_v24?0"INListCarsIntentResponse"8"INCExtensionError"16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e70_v24?0"INGetCarPowerLevelStatusIntentResponse"8"INCExtensionError"16lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ __block_literal_global.77
+ _objc_msgSend$_complete
+ _objc_msgSend$addConnectionErrorHandler:
+ _objc_msgSend$addConnectionTimeoutHandler:
+ _objc_msgSend$addIntentCompletionHandler:
+ _objc_msgSend$carName
+ _objc_msgSend$initWithConnection:
+ _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
+ _objc_msgSend$launchId
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:
+ _objc_msgSend$resumeWithCompletion:
+ _objc_msgSend$sharedInstance
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[VGChargingNetworkAvailabilityProvider _localeChanged:]
- -[VGOEMApplication _connectionWithIntent:]
- GCC_except_table29
- OBJC_IVAR_$_VGChargingNetworkAvailabilityProvider._activeCountryCode
- OBJC_IVAR_$_VGChargingNetworkAvailabilityProvider._activeLanguageCode
- _NSCurrentLocaleDidChangeNotification
- _OBJC_$_PROP_LIST_VGOEMApplication.182
- __43-[VGOEMApplication listCarsWithCompletion:]_block_invoke.25
- __55-[VGOEMApplication stopSendingChargeUpdatesForVehicle:]_block_invoke.55
- __56-[VGOEMApplication startSendingChargeUpdatesForVehicle:]_block_invoke.54
- __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.34
- __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.35
- __58-[VGOEMApplication getStateOfChargeForVehicle:completion:]_block_invoke.48
- ___42-[VGOEMApplication _connectionWithIntent:]_block_invoke
- ___56-[VGChargingNetworkAvailabilityProvider _localeChanged:]_block_invoke
- ___block_descriptor_64_e8_32s40bs48w_e41_v24?0"<INCExtensionProxy>"8"NSError"16lw48l8s40l8s32l8
- ___block_descriptor_64_e8_32s40bs48w_e56_v24?0"INListCarsIntentResponse"8"INCExtensionError"16lw48l8s40l8s32l8
- ___block_descriptor_72_e8_32s40s48bs56w_e41_v24?0"<INCExtensionProxy>"8"NSError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56w_e70_v24?0"INGetCarPowerLevelStatusIntentResponse"8"INCExtensionError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- _fmod
- _objc_msgSend$languageCode
CStrings:
+ "!"
+ "-[VGOEMExtensionConnectionBroker resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:]_block_invoke"
+ "-[_VGOEMExtensionConnection initWithConnection:]_block_invoke"
+ "-[_VGOEMExtensionConnection resumeWithCompletion:]_block_invoke"
+ "<%@ %p, intent: %@, id: %@, hash: %lu>"
+ "@\"INIntent\""
+ "@\"NSMapTable\""
+ "@?"
+ "Started a new streaming Intent %@ with %@"
+ "T@\"VGOEMExtensionConnectionBroker\",R,N"
+ "VGOEMExtensionConnection"
+ "VGOEMExtensionConnectionBroker"
+ "[%{public}@] Connection has already been resumed"
+ "[%{public}p] Added new request to extension map: %@"
+ "[%{public}p] Adding connection error handler: %@"
+ "[%{public}p] Adding connection timeout handler: %@"
+ "[%{public}p] Adding intent completion handler: %@"
+ "[%{public}p] Coalescing duplicate connection request: %@"
+ "[%{public}p] Completed connection request: %@"
+ "[%{public}p] Connection timed out: %@"
+ "[%{public}p] Creating intent connection for intent (%@) with timeout (%.2f) trust check: (%ld)"
+ "[%{public}p] Deallocating"
+ "[%{public}p] Executing %lu connection error handler(s)"
+ "[%{public}p] Executing %lu connection timeout handler(s)"
+ "[%{public}p] Executing %lu intent completion handler(s)"
+ "[%{public}p] Got error resuming connection: %@"
+ "[%{public}p] Got intent response: %@, error: %@"
+ "[%{public}p] Initializing with connection: %@"
+ "[%{public}p] Received new connection request: %@"
+ "[%{public}p] Removed request from extension map: %@"
+ "[%{public}p] Resuming connection"
+ "[%{public}p] Successfully resumed connection; starting intent handling"
+ "_VGOEMExtensionConnection"
+ "_VGOEMExtensionConnectionKey"
+ "_complete"
+ "_completion"
+ "_completionLock"
+ "_connectionErrorHandlers"
+ "_connectionTimeoutHandlers"
+ "_extensionMap"
+ "_handlersLock"
+ "_intent"
+ "_intentCompletionHandlers"
+ "_lock"
+ "addConnectionErrorHandler:"
+ "addConnectionTimeoutHandler:"
+ "addIntentCompletionHandler:"
+ "carName"
+ "countryCodeDidChange:"
+ "countryCodeDidChange:, will reload networks "
+ "initWithConnection:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "launchId"
+ "objectForKey:"
+ "removeObjectForKey:"
+ "resumeConnectionWithIntent:connectionTimeoutHandler:connectionErrorHandler:intentCompletionHandler:"
+ "resumeWithCompletion:"
+ "sharedInstance"
+ "v24@?0@\"INIntentResponse\"8@\"INCExtensionError\"16"
+ "v48@0:8@16@?24@?32@?40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "-[VGChargingNetworkAvailabilityProvider _localeChanged:]_block_invoke"
- "-[VGChargingNetworkAvailabilityProvider initWithDelegate:]_block_invoke"
- "-[VGOEMApplication _connectionWithIntent:]_block_invoke"
- "Creating connection for OEMApp: (%@), with timeout %.2f"
- "Started a new Intent %@ with %@"
- "_activeCountryCode"
- "_activeLanguageCode"
- "_localeChanged:"
- "_localeChanged:, oldCountryCode: %@, newCountryCode: %@, oldLanguageCode: %@, newLanguageCode: %@ -> will not reload networks"
- "_localeChanged:, oldCountryCode: %@, newCountryCode: %@, oldLanguageCode: %@, newLanguageCode: %@ -> will reload networks"
- "languageCode"

```

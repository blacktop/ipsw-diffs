## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-491.120.4.0.0
-  __TEXT.__text: 0x2bbf8
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__oslogstring: 0x497c
-  __TEXT.__cstring: 0x1d0a
-  __TEXT.__unwind_info: 0x858
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0x97f
-  __TEXT.__objc_methtype: 0x56e
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__objc_classlist: 0x8
+504.0.0.0.2
+  __TEXT.__text: 0x30604
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__const: 0x200
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__oslogstring: 0x5720
+  __TEXT.__cstring: 0x2051
+  __TEXT.__unwind_info: 0x900
+  __TEXT.__objc_classname: 0x8e
+  __TEXT.__objc_methname: 0xc8c
+  __TEXT.__objc_methtype: 0x5a9
+  __TEXT.__objc_stubs: 0xaa0
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x340
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa70
-  __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x3e0
-  __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x2d9
-  __DATA.__bss: 0x98
+  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__objc_const: 0x5d0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x2e1
+  __DATA.__bss: 0xb0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__bss: 0x280
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D05888DC-FBB8-384A-9977-E094B15620EB
-  Functions: 679
-  Symbols:   2093
-  CStrings:  1407
+  UUID: F02C1D31-5E22-34D9-94CE-81A8E07C3DFE
+  Functions: 756
+  Symbols:   2340
+  CStrings:  1588
 
Symbols:
+ +[CNHotspotSessionManager eventTypeString:]
+ +[CNHotspotSessionManager hotspotSessionQueue]
+ +[CNHotspotSessionManager hotspotSessionQueue].cold.1
+ +[CNHotspotSessionManager sessionStatusString:]
+ +[CNHotspotSessionManager sessionTypeString:]
+ -[CNHotspotSessionManager .cxx_destruct]
+ -[CNHotspotSessionManager context]
+ -[CNHotspotSessionManager currentSessionStatus]
+ -[CNHotspotSessionManager dealloc]
+ -[CNHotspotSessionManager handler]
+ -[CNHotspotSessionManager hotspotSession]
+ -[CNHotspotSessionManager init]
+ -[CNHotspotSessionManager invalidate]
+ -[CNHotspotSessionManager queue]
+ -[CNHotspotSessionManager runloopMode]
+ -[CNHotspotSessionManager runloop]
+ -[CNHotspotSessionManager scheduleRequestCompletionHandler:]
+ -[CNHotspotSessionManager setContext:]
+ -[CNHotspotSessionManager setCurrentSessionStatus:]
+ -[CNHotspotSessionManager setHandler:]
+ -[CNHotspotSessionManager setHotspotSession:]
+ -[CNHotspotSessionManager setQueue:]
+ -[CNHotspotSessionManager setRunloop:]
+ -[CNHotspotSessionManager setRunloopMode:]
+ -[CNHotspotSessionManager startWithConfigurationID:sessionType:]
+ -[CNHotspotSessionManager stop]
+ GCC_except_table19
+ GCC_except_table4
+ GCC_except_table8
+ _ApplyProviderConfigurationsToPluginList
+ _CFAllocatorAllocateTyped
+ _CNEvaluatedNetworksGetEvaluationProvider
+ _CNEvaluatedNetworksRemovalApplier
+ _CNEvaluatedNetworksRemove
+ _CNGetHotspotSessionStatusString
+ _CNHotspotSessionRequestCompletionHandler
+ _CNPluginStateClearProviderSession
+ _CNPluginStateGetApplicationIDOfProvider
+ _CNPluginStateGetAuthenticationProvider
+ _CNPluginStateGetEvaluationProvider
+ _CNPluginStateIsAuthenticationProvider
+ _CNPluginStateIsEvaluationProvider
+ _CNPluginStateIsProvider
+ _CNPluginStateListCopyPrevaluatedSSIDs
+ _CNPluginStateListEvaluationProviderStopper
+ _CNPluginStateListIsPreevaluatedSSIDListSet
+ _CNPluginStateListProviderListCollector
+ _CNPluginStateListStopHotspotEvaluationProviders
+ _CNPluginStateStartHotspotProvider
+ _CNPluginStateStartProviderSession
+ _CNPluginStateStopHotspotAuthenticationProvider
+ _CNPluginStateStopHotspotEvaluationProvider
+ _CNPluginStateStopHotspotProvider
+ _CheckAppExtensionPoint
+ _CommandHandlerGetAuditToken
+ _DeinitHotspotProviderConfigurationChangeMonitor
+ _FetchHotspotProviderConfigurations
+ _HandleHotspotProviderConfigurationChange
+ _InitHotspotProviderConfigurationChangeMonitor
+ _IsProcessHotspotAuthenticationProvider
+ _IsProcessHotspotEvaluationProvider
+ _NetIFWiFiNetworkSetCaptivePortalClientAuthURL
+ _OBJC_CLASS_$_CNHotspotSessionManager
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NEConfigurationManager
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_CNHotspotSessionManager._context
+ _OBJC_IVAR_$_CNHotspotSessionManager._currentSessionStatus
+ _OBJC_IVAR_$_CNHotspotSessionManager._handler
+ _OBJC_IVAR_$_CNHotspotSessionManager._hotspotSession
+ _OBJC_IVAR_$_CNHotspotSessionManager._queue
+ _OBJC_IVAR_$_CNHotspotSessionManager._runloop
+ _OBJC_IVAR_$_CNHotspotSessionManager._runloopMode
+ _OBJC_METACLASS_$_CNHotspotSessionManager
+ _S_evaluatedNetworks
+ _S_handler
+ _S_queue
+ _S_token
+ _SearchEvaluationProviderUsingConfigurationID
+ _UnconfiguredHotspotProviderCollector
+ _UnconfiguredProviderRemovalApplier
+ __AMCopyExtensionPointIdentifierForAuditToken
+ __AMInvalidateHotspotProviderSession
+ __AMStartHotspotProviderSessionWithIdentifier
+ __AMStopHotspotProviderSession
+ __OBJC_$_CLASS_METHODS_CNHotspotSessionManager
+ __OBJC_$_INSTANCE_METHODS_CNHotspotSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_CNHotspotSessionManager
+ __OBJC_$_PROP_LIST_CNHotspotSessionManager
+ __OBJC_CLASS_RO_$_CNHotspotSessionManager
+ __OBJC_METACLASS_RO_$_CNHotspotSessionManager
+ ___46+[CNHotspotSessionManager hotspotSessionQueue]_block_invoke
+ ___60-[CNHotspotSessionManager scheduleRequestCompletionHandler:]_block_invoke
+ ___64-[CNHotspotSessionManager startWithConfigurationID:sessionType:]_block_invoke
+ ___64-[CNHotspotSessionManager startWithConfigurationID:sessionType:]_block_invoke.69
+ ___CopyHotspotProviderConfigurations_block_invoke
+ ___FetchHotspotProviderConfigurations_block_invoke
+ ___InitHotspotProviderConfigurationChangeMonitor_block_invoke
+ ___ScheduleConfigurationChangeHandler_block_invoke
+ ___block_descriptor_32_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e15_v32?08Q16^B24lr32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e8_v12?0i8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e12_v20?0i8^v12lw48l8s32l8s40l8
+ ___block_descriptor_tmp.177
+ ___block_literal_global.5
+ __handleIPv6OnlyEvaluationFailure
+ _audit_token_has_entitlement_value
+ _hotspotSessionQueue.g_queue
+ _hotspotSessionQueue.onceToken
+ _kCAPPORTClientAuthenticationURL
+ _kCNAuthenticationProviderIdentifier
+ _kCNHotspotApplicationIdentifier
+ _kCNProviderConfigurationIdentifier
+ _kCNProviderEvaluatedSSIDs
+ _kCNSCaptivePortalClientAuthenticationURLProperty
+ _kHotSpotProviderEntitlementValue
+ _kHotspotHelperEntitlement
+ _kNetworkExtensionEntitlement
+ _my_CFArrayCopyIntersectionArray
+ _ne_session_cancel
+ _ne_session_create
+ _ne_session_get_status
+ _ne_session_release
+ _ne_session_set_event_handler
+ _ne_session_start
+ _ne_session_stop
+ _notify_register_dispatch
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$UUIDString
+ _objc_msgSend$application
+ _objc_msgSend$array
+ _objc_msgSend$authenticationProviderBundleIdentifier
+ _objc_msgSend$bundleRecordForAuditToken:error:
+ _objc_msgSend$currentSessionStatus
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$evaluatedSSIDs
+ _objc_msgSend$evaluationProviderBundleIdentifier
+ _objc_msgSend$eventTypeString:
+ _objc_msgSend$extensionPointRecord
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$hotspot
+ _objc_msgSend$hotspotSession
+ _objc_msgSend$hotspotSessionQueue
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$intersectOrderedSet:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$loadConfigurationsWithCompletionQueue:handler:
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$queue
+ _objc_msgSend$scheduleRequestCompletionHandler:
+ _objc_msgSend$sessionStatusString:
+ _objc_msgSend$sessionTypeString:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setCurrentSessionStatus:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$setHotspotSession:
+ _objc_msgSend$sharedManagerForAllUsers
+ _objc_msgSend$startWithConfigurationID:sessionType:
+ _objc_msgSend$stop
+ _objc_release_x1
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x24
+ _objc_retain_x9
- _CFAllocatorAllocate
- _CNPluginStateListIssueCommand
- ___block_descriptor_tmp.178
- _prefs_set_value
CStrings:
+ "!"
+ "%@ hotspot session([%p]) status did not change for configuration [%@]"
+ "%@: (%s): hotspot session([%p]) received event:[%@]"
+ "%@: (%s): hotspot session([%p]) received session status:[%@]"
+ "%@: dealloc"
+ "%@: network [%@] is captive Confidence: %s"
+ "%@: starting hotspot (session:[%p] type:[%@])"
+ "%s entry in S_plugins for evaluation provider: [%@] \t    authentication provider: [%@] configuration id: [%@] application id: [%@]"
+ "%s: loaded NE configurations successfully"
+ "-[CNHotspotSessionManager startWithConfigurationID:sessionType:]_block_invoke"
+ "@20@0:8i16"
+ "Authentication"
+ "AuthenticationProviderIdentifier"
+ "B28@0:8@16i24"
+ "CNHotspotSessionManager"
+ "CNHotspotSessionManager_Queue"
+ "CNScanListFilterSetIsEnabled: %s enabled"
+ "Canceled"
+ "CaptiveNetworkSupport-504.0.0.0.2"
+ "ClientAuthenticationURL: %@:"
+ "ConfigurationChangeHandled"
+ "Connected"
+ "Connecting"
+ "Disconnected"
+ "Disconnecting"
+ "Evaluation"
+ "FetchHotspotProviderConfigurations_block_invoke"
+ "Hotspot Provider Configuration Change Monitor is already initialized"
+ "Hotspot Provider Configuration Module"
+ "Hotspot session status changed to %@ for provider [%@]"
+ "HotspotApplicationIdentifier"
+ "Invalid"
+ "Not sending evaluate command to [%@]"
+ "Not sending filter command to [%@]"
+ "ProviderConfigurationIdentifier"
+ "ProviderEvaluatedSSIDs"
+ "Reasserting"
+ "Setting ClientAuthenticationURL to %@ for interface %@"
+ "StatusChanged"
+ "T^?,V_handler"
+ "T^v,N,V_hotspotSession"
+ "T^v,V_context"
+ "Ti,V_currentSessionStatus"
+ "UUIDString"
+ "Unsupported"
+ "WLAN from %@"
+ "Wi-Fi Info list based on the pre-evaluated SSIDs: %@"
+ "Wi-Fi from %@"
+ "[%@] %s authorized to receive supported interfaces"
+ "[%@] is no longer maintaining captive network [%@]"
+ "[%@] is not valid hotspot authentication provider"
+ "[%@] is not valid hotspot evaluation provider"
+ "[%@] is pre-evaluated by [%@]"
+ "[%@] responded to authenticate command"
+ "[%@] responded to log-off command"
+ "[%@] responded to maintain command"
+ "[%@] responded to present-ui command"
+ "^v"
+ "^v16@0:8"
+ "_context"
+ "_currentSessionStatus"
+ "_handler"
+ "_hotspotSession"
+ "added hotspot helper [%@] to preferences"
+ "app extension [%@] (pid %d) is a valid hotspot provider"
+ "application"
+ "application name for [%@] is [%@]"
+ "array"
+ "authenticationProviderBundleIdentifier"
+ "bundleRecordForAuditToken:error:"
+ "client authentication URL %s available"
+ "client-authentication-url"
+ "com.apple.developer.networking.networkextension"
+ "com.apple.neconfigurationchanged"
+ "com.apple.networkextension.hotspot-authentication"
+ "com.apple.networkextension.hotspot-evaluation"
+ "context"
+ "created new"
+ "currentSessionStatus"
+ "dealloc"
+ "enumerateObjectsUsingBlock:"
+ "evaluate"
+ "evaluated SSIDs for [%@]: %@"
+ "evaluatedSSIDs"
+ "evaluationProviderBundleIdentifier"
+ "eventTypeString:"
+ "extensionPointRecord"
+ "failed to find bundle record for the given audit token, error: [%@]"
+ "failed to find evaluation provider from authentication provider [%@]"
+ "failed to load NE configurations with error %@"
+ "failed to register for notification for [%s] with status %u"
+ "failed to start hotspot session"
+ "filter"
+ "found extension point identifier [%@]"
+ "found hotspot provider configuration: [%@] with identifier: [%@] [%@]"
+ "found hotspot provider configurations: %@"
+ "getUUIDBytes:"
+ "handler"
+ "hotspot"
+ "hotspot provider [%@] is registered"
+ "hotspot provider session (type=%@) already exists for %@"
+ "hotspot provider session (type=%@) status is already %@"
+ "hotspot provider started (configuration:[%@] provider:[%@])"
+ "hotspot provider stopped (configuration:[%@] provider:[%@])"
+ "hotspot session was cancelled for configuration [%@]"
+ "hotspot session([%p]) status changed to connected for configuration [%@]"
+ "hotspot session([%p]) status changed to disconnected for configuration [%@]"
+ "hotspot-provider"
+ "hotspotSession"
+ "hotspotSessionQueue"
+ "i"
+ "i16@0:8"
+ "initWithUUIDString:"
+ "intersectOrderedSet:"
+ "intersection of scanned and pre-evaluated SSIDs: %@"
+ "invalidated hotspot session"
+ "invalidating hotspot provider [%@] (type=%@)"
+ "is"
+ "is not"
+ "isEnabled"
+ "loadConfigurationsWithCompletionQueue:handler:"
+ "making hotspot provider [%@] best plugin"
+ "making plugin [%@] best plugin"
+ "missing '%@'=>'%@' entitlement"
+ "ne_session_create() failed to create hotspot session"
+ "no evaluated SSIDs configured"
+ "no hotspot provider configurations found, removing all the provider states"
+ "orderedSetWithArray:"
+ "re-sending API query"
+ "re-sending Authenticate command to builtin"
+ "received API query response"
+ "received hotspot provider configuration change notification"
+ "received kCNPResultAPIQueryRequired authentication result"
+ "recived NE configuration change notification"
+ "removing provider [%@] due to its configuration removal"
+ "removing state and evaluated SSIDs for [%@] due to its configuration removal"
+ "removing state for [%@] due to configuration removal"
+ "scheduleRequestCompletionHandler:"
+ "sending %s command to [%@]"
+ "sessionStatusString:"
+ "sessionTypeString:"
+ "setContext:"
+ "setCurrentSessionStatus:"
+ "setHandler:"
+ "setHotspotSession:"
+ "sharedManagerForAllUsers"
+ "startWithConfigurationID:sessionType:"
+ "starting hotspot provider session (type=%@) for %@"
+ "stop"
+ "stopping [%@] due to configuration removal"
+ "stopping [%@] due to its configuration removal"
+ "stopping hotspot provider [%@] (type=%@)"
+ "unable to issue command since the provider [%@] is not started, starting provider"
+ "unable to proceed with token authentication as the login URLs don't match"
+ "unable to register evaluation provider [%@] (pid: %d) because of missing entitlement"
+ "updated existing"
+ "v12@?0i8"
+ "v20@?0i8^v12"
+ "v24@0:8^v16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@?0@8Q16^B24"
- "CaptiveNetworkSupport-491.120.4"
- "Not sending filter command to %@"
- "found application bundle identifier [%@] for pid %d"

```

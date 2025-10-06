## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-371.60.3.0.0
-  __TEXT.__text: 0xf91ac
-  __TEXT.__auth_stubs: 0x1a60
-  __TEXT.__objc_stubs: 0x23c0
+381.102.1.0.0
+  __TEXT.__text: 0xf21c0
+  __TEXT.__auth_stubs: 0x1960
+  __TEXT.__objc_stubs: 0x2220
   __TEXT.__init_offsets: 0x20
-  __TEXT.__objc_methlist: 0x508
-  __TEXT.__cstring: 0xb482
-  __TEXT.__const: 0xa5e4
-  __TEXT.__gcc_except_tab: 0xda00
-  __TEXT.__oslogstring: 0x10ac5
+  __TEXT.__objc_methlist: 0x478
+  __TEXT.__cstring: 0xad1f
+  __TEXT.__const: 0x950c
+  __TEXT.__gcc_except_tab: 0xca94
+  __TEXT.__oslogstring: 0x1108d
   __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methname: 0x25e0
-  __TEXT.__objc_methtype: 0x1676
-  __TEXT.__unwind_info: 0x6734
+  __TEXT.__objc_methname: 0x24be
+  __TEXT.__objc_methtype: 0x165d
+  __TEXT.__unwind_info: 0x62e0
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xd48
-  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__auth_got: 0xcc8
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x92a0
-  __DATA_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__const: 0x9058
+  __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1378
-  __DATA.__objc_selrefs: 0x9a0
-  __DATA.__objc_classrefs: 0x190
-  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_selrefs: 0x938
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x2e0
-  __DATA.__bss: 0x478
+  __DATA.__data: 0x610
+  __DATA.__bss: 0x480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CCEC19FE-AF2A-358B-BF11-106EBE5A798A
-  Functions: 5343
-  Symbols:   612
-  CStrings:  2956
+  UUID: 58DF378B-EB5E-35CF-82FA-2A4842EB58FC
+  Functions: 5091
+  Symbols:   592
+  CStrings:  2885
 
Symbols:
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ _sqlite3_prepare_v3
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERj
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERx
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
- __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj
- __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZNSt3__19to_stringEx
- __ZTINSt3__18ios_base7failureE
- __ZTTNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
- __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZTVNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- _getxattr
- _objc_retain_x28
- _rename
- _setxattr
- _sqlite3_prepare_v2
- _strerror_r
- _strstr
- _xpc_connection_get_name
CStrings:
+ "==== STARTUP WIPE STATE QUEUED: CONTAINS LEGACY TRANSFORM STATE"
+ "China"
+ "China mainland"
+ "Evaluating active config conditionals"
+ "Hong Kong"
+ "Hong Kong (China)"
+ "I8@?0"
+ "ISOAlpha2CountryCode"
+ "Macao"
+ "Macao (China)"
+ "T@\"NSString\",?,R,C"
+ "Taiwan"
+ "Taiwan (China)"
+ "[%{public}s XPC Connection] Received xpc object of unexpected type"
+ "[%{public}s XPC Connection] managed connection recieved connection interrupted: %s"
+ "[%{public}s XPC Connection] managed connection recieved connection invalidated: %s"
+ "[%{public}s XPC Connection] managed connection recieved unknown error: %s"
+ "[%{public}s XPC Server] Resuming server"
+ "[%{public}s XPC Server] Setting new client connection handler. %zu active connections"
+ "[%{public}s XPC Server] Suspending server"
+ "[%{public}s XPC Server] received xpc object of unexpected type"
+ "[%{public}s XPC Server] recieved connection interrupted: %s"
+ "[%{public}s XPC Server] recieved connection invalidated: %s"
+ "[%{public}s XPC Server] recieved unknown error: %s"
+ "[CD] GetTelephonyInfo: %s unknown: %s"
+ "[CD] GetTelephonyInfo: Failed to get the data preferred context"
+ "[Config Store] DATABASE INITIALIZATION: begin schema migration"
+ "[Config Store] ERROR: Failed to prepare conditional transform evaluation statement; %s"
+ "[Config Store] ERROR: Failed to prepare conditional transform evaluation statement[null database]"
+ "[Config Store] ERROR: Failed to prepare transaction for conditional transform evaluation; %s"
+ "[Config Store] ERROR: Failed to prepare transaction for conditional transform evaluation[null database]"
+ "[Config Store] External Config Evaluation: {visited: %{public}zd, evaluated: %{public}zd, enableIfPresent: %{public}zd, enabled: %{public}zd}"
+ "[Config Store] Failed during eligible-modify-eventnames-with-type query; %s"
+ "[Config Store] Failed during eligible-modify-eventnames-with-type query[null database]"
+ "[Config Store] Failed during evaluate-conditional-external-configurations-insert; rolling all changes back.; %s"
+ "[Config Store] Failed during evaluate-conditional-external-configurations-insert; rolling all changes back.[null database]"
+ "[Config Store] Failed during evaluate-conditional-external-configurations-query; rolling all changes back.; %s"
+ "[Config Store] Failed during evaluate-conditional-external-configurations-query; rolling all changes back.[null database]"
+ "[Config Store] Failed during evaluate-conditional-transforms-insert; rolling all changes back.; %s"
+ "[Config Store] Failed during evaluate-conditional-transforms-insert; rolling all changes back.[null database]"
+ "[Config Store] Failed during evaluate-conditional-transforms-query; rolling all changes back.; %s"
+ "[Config Store] Failed during evaluate-conditional-transforms-query; rolling all changes back.[null database]"
+ "[Config Store] Failed to create transaction for writing state for aggregating transform %{public}s; %s"
+ "[Config Store] Failed to create transaction for writing state for aggregating transform %{public}s[null database]"
+ "[Config Store] Failed to create transaction for writing state for identity transform %{public}s; %s"
+ "[Config Store] Failed to create transaction for writing state for identity transform %{public}s[null database]"
+ "[Config Store] Failed to create transaction for writing state for reservoir transform %{public}s; %s"
+ "[Config Store] Failed to create transaction for writing state for reservoir transform %{public}s[null database]"
+ "[Config Store] Sampling Transform Evaluation: {visited: %{public}zd, evaluated: %{public}zd, enableIfPresent: %{public}zd, enabled: %{public}zd}"
+ "[Config Store] WARNING: Conditional external configurations query weirdness: got a row but no enableIf definition? (evaluate-conditional-external-configurations-query)"
+ "[Config Store] WARNING: Conditional transforms query weirdness: got a row but no uuid? (evaluate-conditional-transforms-query)"
+ "[Config Store] WARNING: Event query weirdness: got a row but no transform definition? (transforms-for-event)"
+ "[Config Store] WARNING: Event query weirdness: got a row but no transform uuid? (transforms-for-event)"
+ "[Config Store] WARNING: modify-eventdef query weirdness: got a row but no type?"
+ "[Config Store] WARNING: modify-eventnames-with-type query weirdness: got a row but no name?"
+ "[DefaultSink] Retrieved transform definition for %{public}s with %zu bytes"
+ "[DefaultSink] WARNING: found transform state for %s but no definition in config. Is the corret config active?"
+ "[DefaultSink] emitting messages for persisted xform states"
+ "[LegacyContains] Found contents in legacy transform state directory: %{public}s"
+ "[LegacyWipe] Failed to check existence or contents of legacy transform state directory %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove legacy allowlist %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove legacy budget usage path %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove legacy budget usage temp path %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove legacy config %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove legacy transform staging path %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove_all legacy journal path %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove_all legacy markov path %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Failed to remove_all legacy transform state directory %{public}s (boost: %{public}s): "
+ "[LegacyWipe] Removed all in legacy journal directory: %{public}s"
+ "[LegacyWipe] Removed all in legacy markov path: %{public}s"
+ "[LegacyWipe] Removed legacy allowlist: %{public}s"
+ "[LegacyWipe] Removed legacy budget usage path: %{public}s"
+ "[LegacyWipe] Removed legacy budget usage temp path: %{public}s"
+ "[LegacyWipe] Removed legacy config: %{public}s"
+ "[LegacyWipe] Removed legacy transform staging path: %{public}s"
+ "[LegacyWipe] Removed legacy transform state directory: %{public}s"
+ "[MTShim Connection] Processing MT xpc event on the work queue"
+ "[ModifyEventManager] Retrieving Modify Event Definitions for %{public}s."
+ "[RolloverManager] *** BEGINNING PERFORM ROLLOVER (reason: %{public}s, options: %{public}s)"
+ "[RolloverManager] *** COMPLETED PERFORM ROLLOVER (reason: %{public}s, options: %{public}s)"
+ "[State Store] DATABASE INITIALIZATION: begin schema migration"
+ "[State Store] Failed during iterate-transform-uuids-query; %s"
+ "[State Store] Failed during iterate-transform-uuids-query[null database]"
+ "[State Store] Failed during retrieve-transform-state-query; %s"
+ "[State Store] Failed during retrieve-transform-state-query[null database]"
+ "[TelephonyStateHelpers]: Failed to get the CarrierBundle version: %s"
+ "[TelephonyStateHelpers]: Failed to get the CarrierName from the bundle: %s"
+ "[TelephonyStateHelpers]: Failed to get the ISOAlpha2CountryCode from country bundle: %s"
+ "[TelephonyStateHelpers]: Failed to get the iso country code"
+ "[TelephonyStateHelpers]: Failed to get the serving MCC: %s"
+ "[TelephonyStateHelpers]: Failed to get the subscriber MCC: %s"
+ "analyticsd.AppUsageQueue"
+ "analyticsd.CadenceManagerQueue"
+ "analyticsd.ClientManagerQueue"
+ "analyticsd.ConfigurerQueue"
+ "analyticsd.DaemonPerfManagerQueue"
+ "analyticsd.DaemonState"
+ "analyticsd.DefaultQueriedStateCacheQueue"
+ "analyticsd.DeviceKeyManagerQueue"
+ "analyticsd.EventBrokerQueue"
+ "analyticsd.LocationStateResolverQueue"
+ "analyticsd.MTShim ConnectionAnalyticsStartupQueue"
+ "analyticsd.MessageTracerShimQueue"
+ "analyticsd.ModifyEventManagerQueue"
+ "analyticsd.MotionStateResolver.CoreMotion.CallbackQueue"
+ "analyticsd.MotionStateResolverQueue.myQueue"
+ "analyticsd.NetworkingStateResolver.NetworkStateRelay.myQueue"
+ "analyticsd.NetworkingStateResolver.WiFiStateRelay.myQueue"
+ "analyticsd.NetworkingStateResolverQueue"
+ "analyticsd.PowerStateResolverQueue"
+ "analyticsd.RolloverManagerQueue"
+ "analyticsd.SqliteDeviceConfigurationStoreQueue"
+ "analyticsd.SqliteStateStoreQueue"
+ "analyticsd.TransformManagerQueue"
+ "analyticsd.TrialCellularWireless.CallbackQueue"
+ "config.sqlite"
+ "currentConfiguration.json"
+ "devTaskedConfig.json"
+ "events.allowlist"
+ "events.whitelist"
+ "i8@?0"
+ "identity/budget_info.json"
+ "identity/budget_info.stage"
+ "journals"
+ "state.sqlite"
+ "v24@?0r*8^v16"
+ "{CacheStats=iiQQQQi}8@?0"
+ "{DatabaseStats=QQqq}8@?0"
+ "{SqliteMigrationResult=iiiB}8@?0"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}}8@?0"
+ "{optional<QueriedStateCacheEntry>=(?=c{QueriedStateCacheEntry={basic_json<std::map, std::vector, std::string, bool, long long, unsigned long long, double, std::allocator, nlohmann::adl_serializer, std::vector<unsigned char>>=C(json_value=^v^v^v^vBqQd)}{time_point<std::chrono::system_clock, std::chrono::duration<long long, std::ratio<1, 1000000>>>={duration<long long, std::ratio<1, 1000000>>=q}}{duration<long long, std::ratio<1, 1000000>>=q}B})B}8@?0"
+ "{pair<std::string, double>={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}}d}8@?0"
+ "{time_point<std::chrono::system_clock, std::chrono::duration<long long, std::ratio<1, 1000000>>>={duration<long long, std::ratio<1, 1000000>>=q}}8@?0"
- " -> "
- " to "
- "%lld"
- "(!is_end())&&(\"attempt to dereference end directory iterator\")"
- ") using file "
- "): "
- "/config.sqlite"
- "/currentConfiguration.json"
- "/devTaskedConfig.json"
- "/events.allowlist"
- "/events.whitelist"
- "/identity/budget_info.json"
- "/identity/budget_info.stage"
- "/journals"
- "/state"
- "/state.sqlite"
- "<exception during read>"
- "<unavailable>"
- "="
- "=="
- "=== Migrating existing persisted transform state"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
- "Analytics Fault 2: %{public}s | errno %{public}d '%{public}s' | %{public}s uuid: %{public}s (stat {size: %{public}lld mode: 0x%{public}X mtime: %{public}ld.%{public}09ld errno: %{public}d '%{public}s'} contents: %s)"
- "AnalyticsMainQueue"
- "Failed to create initial state directory (boost: "
- "Failed to migrate legacy uuid filepath (boost: "
- "Failed to perform file status checks in iterator of iterateUuidFolder (boost: "
- "Failed to perform file status checks in subiterator of iterateUuidFolder (boost: "
- "MessageTracerShimQueue"
- "Success"
- "Transform] FAULT: Exception (boost: "
- "Transform] FAULT: Exception (ios: "
- "Transform] FAULT: Exception (json: "
- "Transform] FAULT: Exception (stl: "
- "Transform] FAULT: Exception using file "
- "["
- "[%{public}sTransform] ERROR: Failed to open file for '%s' to persist: %s"
- "[%{public}sTransform] ERROR: Failed to open file for persist: %s"
- "[%{public}sTransform] ERROR: transform %s state file doesn't exist."
- "[%{public}sTransform] Failed to create transaction for peristing transform %s"
- "[%{public}sTransform] Failed to create transaction for persisting transform state %s"
- "[%{public}sTransform] The cost of a transform should not be evaluated when using SQLite for transform state."
- "[%{public}sTransform] The cost() of a transform should not be evaluated when using SQLite for transform state."
- "[%{public}sTransform] created aggregate %s"
- "[%{public}sTransform] created transform %s"
- "[%{public}sTransform] initialized from file for transform %s"
- "[%{public}sTransform] initializing budget and statistics from file for aggregate %s"
- "[%{public}sTransform] transform '%s' is unexpectedly initialized prior to synchronizing"
- "[CD] TelephonyInfo: %s unknown: %s"
- "[Config Store] DATABASE INITIALIZATION: begin migration"
- "[Config Store] ERROR: Failed to insert row for disabled external_config; rolling all changes back.; %s"
- "[Config Store] ERROR: Failed to insert row for disabled external_config; rolling all changes back.[null database]"
- "[Config Store] ERROR: Failed to prepare evaluation statement; %s"
- "[Config Store] ERROR: Failed to prepare evaluation statement[null database]"
- "[Config Store] Evaluation: %zd external_configs had enableIf predicates; %zd of those were enabled."
- "[Config Store] Evaluation: {visited: %{public}zd, evaluated: %{public}zd, enableIfPresent: %{public}zd, enabled: %{public}zd}"
- "[Config Store] Failed during eligible-modify-eventnames query; %s"
- "[Config Store] Failed during eligible-modify-eventnames query[null database]"
- "[Config Store] Failed to create transaction for disabled_transforms table edits; %s"
- "[Config Store] Failed to create transaction for disabled_transforms table edits[null database]"
- "[Config Store] Retrieving Modify Event Definitions for %{public}s."
- "[Config Store] WARNING: Event query weirdness: got a row but no definition? (transforms-for-event)"
- "[DaemonState] ERROR: Couldn't retrieve bootTime to determine first launch after boot"
- "[DaemonState] NOTICE: Using SQLite for transform state"
- "[DaemonState] NOTICE: Using flat files for transform state"
- "[LegacyWipe] Failed to remove legacy allowlist (boost: "
- "[LegacyWipe] Failed to remove legacy config (boost: "
- "[LegacyWipe] Failed to remove_all legacy budget usage path (boost: "
- "[LegacyWipe] Failed to remove_all legacy budget usage temp path (boost: "
- "[LegacyWipe] Failed to remove_all legacy journal path (boost: "
- "[LegacyWipe] Failed to remove_all legacy markov path (boost: "
- "[LegacyWipe] Removed all legacy budget usage path: %s"
- "[LegacyWipe] Removed all legacy budget usage temp path: %s"
- "[LegacyWipe] Removed all legacy journal path: %s"
- "[LegacyWipe] Removed legacy allowlist: %s"
- "[LegacyWipe] Removed legacy config: %s"
- "[MTShim Conection] Processing MT xpc event on the work queue"
- "[MTShim Conection] Received xpc event on the MT queue"
- "[MTShim Conection] Received xpc object of unexpected type"
- "[MTShim Conection] managed connection recieved connection interrupted: %s"
- "[MTShim Conection] managed connection recieved connection invalidated: %s"
- "[MTShim Conection] managed connection recieved unknown error: %s"
- "[MTShim Server] Unable to create reply to xpc event (client disconnecting?)"
- "[Removed all legacy markov path: %s"
- "[State Store] DATABASE INITIALIZATION: begin migration"
- "[TESTING] ignoring config %s"
- "[TelephonyStateRelay]: Failed to get the CarrierBundle version: %s"
- "[TelephonyStateRelay]: Failed to get the CarrierName from the bundle: %s"
- "[TelephonyStateRelay]: Failed to get the ISO country code: %s"
- "[TelephonyStateRelay]: Failed to get the serving MCC: %s"
- "[TelephonyStateRelay]: Failed to get the subscriber MCC: %s"
- "[Transform Manager] Retrieved transform definition for %{public}s with %zu bytes"
- "[Transform Manager] WARNING: found transform state for %s but no definition in config. Is the corret config active?"
- "[Transform Manager] clearing potential transform staging files"
- "[Transform Manager] creating transform directories if not already present"
- "[Transform Manager] emitting messages for persisted xform states"
- "[Transform Manager] removing transform staging files if any exist"
- "[Transform Manager] running transform cache with parameters: {size: %u}"
- "[Transform] The cost() of a transform should not be evaluated when using SQLite for transform state."
- "[UuidUtils] ERROR: could not delete empty folder %s due to error: %s"
- "[XPC Connection] Received xpc object of unexpected type"
- "[XPC Connection] managed connection recieved connection interrupted: %s"
- "[XPC Connection] managed connection recieved connection invalidated: %s"
- "[XPC Connection] managed connection recieved unknown error: %s"
- "[XPC Server] Resuming server %s"
- "[XPC Server] Setting new client connection handler. %zu active connections"
- "[XPC Server] Suspending server %s"
- "[XPC Server] XPC Server %s: listening"
- "[XPC Server] received xpc object of unexpected type"
- "[XPC Server] recieved connection interrupted: %s"
- "[XPC Server] recieved connection invalidated: %s"
- "[XPC Server] recieved unknown error: %s"
- "_FLUSHED"
- "_getCarrierBundleVersion"
- "_getCarrierNameFromBundle:"
- "_getCarrierNameWithISO2CountryCode:forCarrierType:"
- "_getCountryNameFrom:"
- "_getIsoCountryCode:"
- "_getServingMcc"
- "_getServingMnc"
- "_getSubscriberMcc"
- "_getSubscriberMnc"
- "_isValidCarrierName:"
- "_isValidMobileCode:"
- "_isValidRegistration:"
- "abandoned transform state. lingering staging files present"
- "acceptTransformedEvent"
- "after loading state"
- "aggregate staging failure; "
- "app-usage-sync"
- "base64_from_binary.hpp"
- "boost::filesystem::file_size"
- "boost::filesystem::rename"
- "boot_time"
- "checking length"
- "closing file"
- "com.apple.analyticsd.CoreMotion.CallbackQueue"
- "com.apple.analyticsd.DaemonPerfManagerQueue"
- "com.apple.analyticsd.LocationStateResolver"
- "com.apple.analyticsd.MotionStateResolver"
- "com.apple.analyticsd.NetworkStateRelay.myQueue"
- "com.apple.analyticsd.NetworkingStateResolver"
- "com.apple.analyticsd.PowerStateResolver"
- "com.apple.analyticsd.TrialCellularWirelessCallbackQueue"
- "com.apple.analyticsd.WiFiStateRelay.myQueue"
- "com.apple.analyticsd.appUsageQueue"
- "config-dump"
- "config-reload"
- "copyMobileSubscriberIsoCountryCode:error:"
- "creating output directory"
- "dereference"
- "directory.hpp"
- "failed to delete directory at path %s"
- "failed to delete file at path %s"
- "failing open"
- "flatFiles"
- "flushing file"
- "getting file size"
- "initializing budget and statistics from file"
- "initializing budget and statistics from file begin"
- "initializing budget from file"
- "initializing from file"
- "initializing from file begin"
- "intrusive_ptr.hpp"
- "list-transforms-in-cache"
- "loading budget info"
- "loading event count"
- "loading samples"
- "loading state data"
- "moving file"
- "opening file"
- "persist to file"
- "persistToFile"
- "persistToStoreWithTransaction"
- "persisting to file"
- "persisting to store with transaction"
- "processing event "
- "px != 0"
- "query-clear"
- "reading events"
- "reading filesize"
- "reading samples"
- "reading state data"
- "removed directory at path %s"
- "removed file at path %s"
- "removed transform staging path: %s"
- "removing previous file"
- "removing tmp file"
- "renaming previous file"
- "reservoir staging failure; "
- "retrieving events from file"
- "retrieving events from file begin"
- "save-log"
- "saving budget info"
- "saving count info"
- "saving event info"
- "saving row info"
- "saving samples"
- "set-clear-config-after-reboot"
- "set-tasking"
- "set-tasking-old"
- "store-locale-info"
- "t < 64"
- "use_sqlite_for_transform_states"
- "v128@?0{Message={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}}{basic_json<std::map, std::vector, std::string, bool, long long, unsigned long long, double, std::allocator, nlohmann::adl_serializer, std::vector<unsigned char>>=C(json_value=^v^v^v^vBqQd)}{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}})B}IdB}8"
- "v24@?0{basic_json<std::map, std::vector, std::string, bool, long long, unsigned long long, double, std::allocator, nlohmann::adl_serializer, std::vector<unsigned char>>=C(json_value=^v^v^v^vBqQd)}8"
- "v32@?0r*8{basic_json<std::map, std::vector, std::string, bool, long long, unsigned long long, double, std::allocator, nlohmann::adl_serializer, std::vector<unsigned char>>=C(json_value=^v^v^v^vBqQd)}16"
- "validating state data"

```

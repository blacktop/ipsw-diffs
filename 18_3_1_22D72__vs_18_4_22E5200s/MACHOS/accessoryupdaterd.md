## accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x4e714
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_stubs: 0x7840
-  __TEXT.__objc_methlist: 0x3198
-  __TEXT.__cstring: 0xb940
-  __TEXT.__const: 0x3b0
-  __TEXT.__objc_methname: 0x8cbf
-  __TEXT.__oslogstring: 0x4617
-  __TEXT.__objc_classname: 0x66f
-  __TEXT.__objc_methtype: 0x1b33
-  __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__ustring: 0x12c
+1207.100.54.502.1
+  __TEXT.__text: 0x52b60
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_stubs: 0x7600
+  __TEXT.__objc_methlist: 0x3b3c
+  __TEXT.__const: 0x400
+  __TEXT.__objc_methname: 0x8fea
+  __TEXT.__cstring: 0x7c45
+  __TEXT.__objc_classname: 0x69e
+  __TEXT.__objc_methtype: 0x1b3a
+  __TEXT.__oslogstring: 0x683d
+  __TEXT.__gcc_except_tab: 0x548
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x1238
-  __DATA_CONST.__auth_got: 0x918
-  __DATA_CONST.__got: 0x3e0
+  __TEXT.__unwind_info: 0x1310
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x14d0
-  __DATA_CONST.__cfstring: 0x8140
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0x15b0
+  __DATA_CONST.__cfstring: 0x57c0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xa0c8
-  __DATA.__objc_selrefs: 0x22c0
-  __DATA.__objc_ivar: 0x51c
-  __DATA.__objc_data: 0xf50
-  __DATA.__data: 0xb25
+  __DATA.__objc_const: 0x92b8
+  __DATA.__objc_selrefs: 0x2330
+  __DATA.__objc_ivar: 0x534
+  __DATA.__objc_data: 0xf00
+  __DATA.__data: 0xb85
   __DATA.__bss: 0x1290
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1878
-  Symbols:   425
-  CStrings:  3721
+  Functions: 2155
+  Symbols:   398
+  CStrings:  3570
 
Symbols:
+ _OBJC_CLASS_$_UARPSandboxExtension
+ _dispatch_source_cancel
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_release_x9
+ _objc_retainBlock
+ _objc_retain_x25
+ _objc_retain_x4
+ _objc_storeWeak
+ _os_parse_boot_arg_int
+ _xpc_copy
- _CFEqual
- _CFUserNotificationUpdate
- _OBJC_CLASS_$_NSNotificationCenter
- _XPC_ACTIVITY_MAY_REBOOT_DEVICE
- __xpc_error_connection_invalid
- __xpc_type_connection
- __xpc_type_dictionary
- _addObjectToXpcDictionary
- _clientHasEntitlement
- _dumpXPCObject
- _notify_check
- _notify_get_state
- _objectFinalizer
- _sandbox_extension_consume
- _sandbox_extension_issue_file
- _sandbox_extension_release
- _sendMessageToExternalClient
- _sendMessageToInternalClient
- _sendReplyMessageToClient
- _strdup
- _time
- _xpc_connection_cancel
- _xpc_connection_create_mach_service
- _xpc_connection_get_context
- _xpc_connection_resume
- _xpc_connection_set_context
- _xpc_connection_set_event_handler
- _xpc_connection_set_finalizer_f
- _xpc_connection_set_target_queue
- _xpc_copy_description
- _xpc_dictionary_create_reply
- _xpc_dictionary_get_audit_token
- _xpc_dictionary_get_data
- _xpc_dictionary_get_remote_connection
- _xpc_dictionary_set_data
- _xpc_dictionary_set_double
- _xpc_dictionary_set_uint64
- _xpc_retain
CStrings:
+ "\x01#1\x11\x11"
+ "\x06\x13"
+ "\x14"
+ " %s: Write Accessory Settings changes %@ / %@"
+ "%@ checking for %@"
+ "%s: Invalid key value / pair = %@ / %@"
+ "%s: Sending darwin notification for restarting pending"
+ "%s: setting %@"
+ "%s: unknown key/value pair %@/%@"
+ "%s: watching shared dispatch group"
+ "-[AUDController beginIdleTimer]_block_invoke"
+ "-[AUDController watchSharedGroup]"
+ "-[AUDStateMachineManager dispatchStateMachineCommand:]"
+ "-[AUDStateMachineManager issueNotification:request:]"
+ "-[AUDeveloperSettingsDatabase accessoryList]_block_invoke"
+ "-[AUDeveloperSettingsDatabase updateAccessoryWithSerialNumber:info:]"
+ "-[AUHelperService userPreferenceUpdateAccessorySettings:withKey:]"
+ "@\"<AUDStateMachineDelegate>\""
+ "@\"AUDStateMachineClient\""
+ "@\"AUDStateMachineManager\""
+ "@32@0:8@16o^@24"
+ "@36@0:8i16@20@28"
+ "AUDController"
+ "AUDStateMachineClient"
+ "AUDStateMachineDelegate"
+ "AUDStateMachineManager"
+ "AUDeveloperSettingsUpdateAccessory:withKey:"
+ "AULegacyCommand"
+ "AULegacyEvent - Type:%d Filter:%@ Options:%@"
+ "Accessory disabled by defaults write. Ignoring %@"
+ "Active FW update detected for service %{public}@, queue up %{public}@"
+ "Advancing state machine"
+ "AirPods2022Seed"
+ "AirPodsDeveloperSeed"
+ "Asking user if they want to install optional update"
+ "CHECK IN state for activity: %{public}s"
+ "Can't dispatch event without valid command"
+ "Can't load plugin with invalid filter name: %{public}@ plugin name: %{public}@"
+ "Cannot disable stream events since state machine has no filter"
+ "Cannot enable stream events since state machine has no filter"
+ "Cannot handle NULL stream event"
+ "Cannot issue notification for invalid state machine"
+ "Cannot mark step complete without a valid state machine"
+ "Cannot notify accessory disconnected without state machine"
+ "Cannot queue up events for NULL state machine"
+ "Checking exclusion group (%{public}@) for already queued commands"
+ "Clearing state for new event stream"
+ "Completed step:Bootstrap successful:NO"
+ "Could not create filter for notification %{public}@"
+ "Creating new state machine for command: %{public}@"
+ "CrystalSeedUpdate"
+ "Current queuedEvents=%{public}@"
+ "Default stepName=%{public}@, nextStep=%{public}@, stepInfo=%{public}@"
+ "Defaults read for UARP periodic firmware check interval found = %{public}lld"
+ "Defaults read for periodic firmware check interval found = %{public}lld"
+ "Dequeue duplicate connection event: %{public}@"
+ "Device class detached:%{public}@ error:%{public}@"
+ "Disabling stream events for device class: %{public}@"
+ "Does not need multi-update queue up command:%{public}@"
+ "Dropping attach event since state machine is busy in exclusion group %{public}@"
+ "Empty set of exclusion group filters for %{public}@"
+ "Enabling stream events for suspended device class: %{public}@"
+ "Error dispatch query request is no longer supported"
+ "Error no policies detected for device idle check"
+ "Error setting continue status for device idle activity"
+ "Error setting continue status for launch activity"
+ "Error setting done status for device idle activity"
+ "Error setting done status for launch activity"
+ "Event queued up [%{public}lu] - [%{public}@ : %{public}@]"
+ "ExclusionGroupFilter: %{public}@ (%{public}@)"
+ "Failed to allocate service policy for plugin:%{public}@"
+ "Failed to allocate service policy for service:%{public}@"
+ "Failed to convert filter dictionary to xpc dictionary"
+ "Failed to convert filter type to string"
+ "Failed to covert fud command %{public}d into a string value for client"
+ "Failed to create notification"
+ "Failed to create stame machine for plugin: %{public}@"
+ "Failed to create storage directory at path:%{public}@ error:%{public}@"
+ "Failed to fetch plugin info dictionary at path:%{public}@"
+ "Failed to fetch service info dictionary at path:%{public}@"
+ "Failed to find legacy plugin directory"
+ "Failed to find policy owning filter: %{public}@"
+ "Failed to get NSBundle to MAU framework for localized strings"
+ "Failed to get bundle for localization"
+ "Failed to get filter in policy:%{public}@"
+ "Failed to get filter type from %{public}@"
+ "Failed to get localized accessory name for %{public}@"
+ "Failed to initialize daemon, exiting"
+ "Failed to initialize legacy storage with path:%{public}@"
+ "Failed to load plugin bundle at path:%{public}@"
+ "Failed to load service bundle at path:%{public}@"
+ "Failed to localize messages"
+ "Failed to save declined accessory at url %{public}@"
+ "Failed to set continue status for periodic launch"
+ "Failed to set done status for periodic launch"
+ "Failed to set state machine for filter: %{public}@"
+ "Filter %{public}@ needs check"
+ "Got device attach event for %{public}@ updateInProgress=%{public}d queue=%{public}@"
+ "Handler: Device Idle Check Kicked Off - STATE=%{public}ld"
+ "Handler: Idle Exiting, dropping event"
+ "Handler: Periodic Firmware Check Kicked Off - STATE=%{public}ld"
+ "Handler: UARP Periodic Firmware Check Kicked Off - STATE=%{public}ld"
+ "Idle Exiting, dropping event for filter:%{public}s"
+ "Ignoring puck arrived notifications until FW issues resolved - %{public}@"
+ "Ignoring unsupported command %{public}@"
+ "Initializing daemon for secondary launch"
+ "Initializing daemon on first launch"
+ "Invalid input params, ignoring event"
+ "Kicking off device check event for %{public}@, xpcFilter=%{public}@"
+ "Kicking off queued=%@ queue=%@"
+ "Kicking off queued=%{public}@ queue=%{public}@"
+ "Kicking off queuedEvent=%{public}@"
+ "Kickstarting accessory with continue event: %{public}@"
+ "Manager not active, dropping command %{public}@"
+ "Missing last remote find date in from command: %{public}@"
+ "Missing last remote find date options from command: %{public}@"
+ "Modal Default Client - Advancing state machine"
+ "Modal Default Client - Not advancing state machine"
+ "Modal Default Client - queue=%@"
+ "No CFUserNotification to take down"
+ "No exclusion group provided"
+ "No filter found with name: %{public}@"
+ "No matching filter for owning filter %{public}@"
+ "No policy for owning filter %{public}@"
+ "Not advancing state machine"
+ "Not advancing state machine - queue=%@"
+ "Performing apply command"
+ "Performing bootstrap command"
+ "Performing done command, queueCount=%{public}lu"
+ "Performing download command"
+ "Performing find command"
+ "Performing finish command"
+ "Performing next command."
+ "Performing prepare command"
+ "Plugin disabled by defaults write. Ignoring %{public}@"
+ "Plugin policy is invalid, can't load it for service:%{public}@"
+ "Policy is invalid, can't load it for plugin:%{public}@"
+ "Prefs for disablePlugin:%{public}@ disableAcc:%{public}@"
+ "RUN Handler called for activity: %{public}s"
+ "RUN state for activity: %{public}s"
+ "Registering First Launch XPC activity %{public}s with criteria = %{public}@"
+ "Registering XPC activity %{public}s with XPC_ACTIVITY_CHECK_IN"
+ "Registering filter with XPC stream: %{public}@"
+ "Registering filter with XPC stream: %{public}s"
+ "Remaining queuedEvents=%{public}@"
+ "Removing accessory from database %@"
+ "Resuming state machine"
+ "Saving declined accessory at url %{public}@"
+ "Set acc for statemachine %{public}@ %{public}@"
+ "Setting event handler for Plugin:%{public}@ Filter:%{public}@"
+ "Started idle timer"
+ "State machine exists: active=%{public}d for [%{public}@ : %{public}@]"
+ "State machine in exclusion group (%{public}@) is busy, dropping stream event"
+ "Step Complete for plugin:%{public}@ status:%{public}d info=%{public}@"
+ "Step Progress for plugin:%{public}@"
+ "Step completed step:%{public}@ device:%{public}@ successful:%{public}@ next-step:%{public}@ silentUpdate=%{public}d error:%{public}@"
+ "StepRunning - step:%{public}@  device:%{public}@ progress:%{public}f overall-progress:%{public}f stepInfo=%{public}@"
+ "Still has pending work in dispatch group"
+ "Stopping idle timer"
+ "Stream event happened for filter: %{public}@"
+ "Successfully loaded plugin policy for: %{public}@"
+ "Successfully loaded service policy for: %{public}@"
+ "SupportsDeveloperSettings"
+ "T@\"<AUDStateMachineDelegate>\",W,V_delegate"
+ "T@\"AUDAccessory\",C,V_accessory"
+ "T@\"NSArray\",R,V_partnerSerialNumbers"
+ "T@\"NSDictionary\",R,V_commandOptions"
+ "T@\"NSObject<OS_xpc_object>\",R,V_eventOptions"
+ "T@\"NSString\",C,V_activeDeviceClass"
+ "T@\"NSString\",R,C,V_filter"
+ "T@\"NSString\",R,V_activeVersion"
+ "T@\"NSString\",R,V_assetLocation"
+ "T@\"NSString\",R,V_assetURLOverride"
+ "T@\"NSString\",R,V_customBuild"
+ "T@\"NSString\",R,V_customTrain"
+ "T@\"NSString\",R,V_downloadedVersion"
+ "T@\"NSString\",R,V_dropboxVersion"
+ "T@\"NSString\",R,V_hwFusing"
+ "T@\"NSString\",R,V_hwRevision"
+ "T@\"NSString\",R,V_modelNumber"
+ "T@\"NSString\",R,V_serialNumber"
+ "T@\"NSString\",R,V_supplementalAssetLocation"
+ "T@\"NSString\",R,V_supplementalCustomBuild"
+ "T@\"NSString\",R,V_supplementalCustomTrain"
+ "TB,R,V_accessoryReachable"
+ "TB,R,V_authListingEnabled"
+ "TB,R,V_otaDisabled"
+ "TB,R,V_personalizationRequired"
+ "TB,R,V_supportsDeveloperSettings"
+ "TB,V_isConnectionEvent"
+ "TB,V_isInstallerUpdate"
+ "There is no exclusion group found for the filter: %{public}@"
+ "There is no plugin bundle for: %{public}@"
+ "There is no policy for the filter: %{public}@"
+ "There was no policy owning filter '%{public}@', dropping event."
+ "Ti,R,V_commandType"
+ "Timer source fired"
+ "UARP updater service %@ disabled by boot-arg %@"
+ "UARPSettingsAccessory"
+ "Unknown state for value:%{public}d"
+ "Unrecognized state machine command: %{public}d"
+ "Update for %{public}@ already in progress. Queue up %{public}@"
+ "Updated queue=%@"
+ "Updated queuedEvents=%@"
+ "Updated queuedEvents=%{public}@"
+ "Updating database with %@ / %@"
+ "User response was: %{public}lu ignorePromptResponse=%{public}d updateInprogress=%{public}d"
+ "Waiting on pending user restore prompts"
+ "[Seed Consent Required or Next Step is Prepare]: shouldUpdate: %{public}s"
+ "_accessoryReachable"
+ "_activeDeviceClass"
+ "_activeVersion"
+ "_assetLocation"
+ "_assetURLOverride"
+ "_authListingEnabled"
+ "_clientQueue"
+ "_commandOptions"
+ "_commandType"
+ "_criticalSectionSemaphore"
+ "_customBuild"
+ "_customTrain"
+ "_downloadedVersion"
+ "_dropboxVersion"
+ "_eventFlags"
+ "_eventOptions"
+ "_filter"
+ "_forceRestart"
+ "_frameworkBundle"
+ "_hwFusing"
+ "_hwRevision"
+ "_ignorePromptResponse"
+ "_installerUpdateActive"
+ "_isConnectionEvent"
+ "_lastUpdateTime"
+ "_legacyUpdaterStorage"
+ "_modalDeviceClass"
+ "_modelNumber"
+ "_notification"
+ "_originalSettings"
+ "_otaDisabled"
+ "_partnerSerialNumbers"
+ "_pendingDeviceAttachedEvents"
+ "_personalizationRequired"
+ "_queuedAccessories"
+ "_serialNumber"
+ "_stateMachineClient"
+ "_stateMachineManager"
+ "_supplementalAssetLocation"
+ "_supplementalCustomBuild"
+ "_supplementalCustomTrain"
+ "_supportsDeveloperSettings"
+ "_updateInProgress"
+ "_useProgressBar"
+ "accessoryList"
+ "activeDeviceClass"
+ "addCommandToQueue:withFilter:stateMachine:"
+ "assets"
+ "audcontroller.timeoutQueue"
+ "audstatemachineclient.queue"
+ "austatemachinemgr.client.workQueue"
+ "austatemachinemgr.workQueue"
+ "automaticUpdatesDisabledByBootArgForService:"
+ "cleanupInstallUpdateForAccessory:handler:"
+ "com.apple.aud.processing.queue"
+ "commandOptions"
+ "commandType"
+ "copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:"
+ "copyAccessoryWithSerialNumber:"
+ "customBuild"
+ "customTrain"
+ "disable_%@"
+ "dispatchCommand:"
+ "dispatchStateMachineCommand:"
+ "dispatchStatelessCommand:"
+ "doDeviceCheck:"
+ "doneWithOptions:filter:"
+ "encodeAsChangedDictionary"
+ "encodeAsDictionary"
+ "eventOptions"
+ "https://basejumper.apple.com"
+ "hwFusing"
+ "initWithCommand:forFilter:options:"
+ "initWithDictionary:"
+ "initializeController"
+ "isCommandQueryRequest:"
+ "isCommandStateless:"
+ "isEqualToArray:"
+ "isInstallerUpdate"
+ "kickOffQueuedCommand:successful:"
+ "legacy"
+ "mobileAssetCacheDuration"
+ "notifyAccessoryAttachedWithCommand:"
+ "otaDisabled"
+ "performNextStepWithOptions:filter:"
+ "promptUserForRestart"
+ "setAccessoryReachable:"
+ "setActiveVersion:"
+ "setAssetLocation:"
+ "setAssetURLOverride:"
+ "setAuthListingEnabled:"
+ "setCustomBuild:"
+ "setCustomTrain:"
+ "setDownloadedVersion:"
+ "setDropboxVersion:"
+ "setHwFusing:"
+ "setIsInstallerUpdate:"
+ "setLastRemoteFindWithCommand:"
+ "setOtaDisabled:"
+ "setPersonalizationRequired:"
+ "setSupplementalAssetLocation:"
+ "setSupplementalCustomBuild:"
+ "setSupplementalCustomTrain:"
+ "setSupportsDeveloperSettings:"
+ "stringByAppendingString:"
+ "supplementalCustomBuild"
+ "supplementalCustomTrain"
+ "uarpCreateFileHandleForWritingToURL:error:"
+ "updateAccessory:"
+ "updateAccessoryWithSerialNumber:info:"
+ "userPreferenceUpdateAccessorySettings:withKey:"
+ "v24@0:8i16B20"
+ "v28@0:8B16@?20"
+ "v32@?0@8@16^B24"
+ "\xc1"
- " Info Dict: %@"
- "%@.events"
- "%@/MarimbaSeed"
- "%d"
- "%s Archived Data %@"
- "%s Received Notification Request: %d, %@"
- "%s: Archiving Failure"
- "%s: Archiving Failure Error: %@"
- "%s: Cannot Generate Sandbox Extension Token for %@ "
- "%s: Generating Read-Write Sandbox Extension Token for %@ "
- "%s: Ignoring non-dictionary xpc msg"
- "%s: dictionary = %@"
- "%s: failed to cosume sandbox token"
- "%s: seting %@:%@"
- "%s: shouldCheck = %d, useDropboxPath = %llu"
- "%s[Seed Consent Required or Next Step is Prepare]: shouldUpdate: %s"
- "+[UARPSandboxExtension readWriteTokenStringWithURL:]"
- "--------------------- Kicking off Device Idle Firmware check ------------------------"
- "--------------------- Kicking off May Reboot Firmware check ------------------------"
- "--------------------- Kicking off Periodic Firmware check ------------------------"
- "--------------------- Kicking off UARP Periodic Firmware check ------------------------"
- "--------------------- NEW API EVENT ------------------------"
- "--------------------- NEW CONNECTION ------------------------"
- "--------------------- NEW EAOVERHID STREAM EVENT ------------------------"
- "--------------------- NEW INTERNAL API EVENT ------------------------"
- "--------------------- NEW STREAM EVENT ------------------------"
- "-[AUDeveloperSettingsDatabase seedParticipationDictionary]"
- "-[DefaultModalClient stepComplete:deviceClass:successful:info:error:]_block_invoke_2"
- "-[FudController beginIdleTimer]_block_invoke"
- "-[FudController doSimulateIdleCheck]"
- "-[FudController handleXPCAPIEvent:]_block_invoke_2"
- "-[FudController watchSharedGroup]"
- "-[FudIpcDispatch accessoryDisconnected:error:]"
- "-[FudIpcDispatch disableStreamEventsForStateMachine:]"
- "-[FudIpcDispatch dispatchEvent:]"
- "-[FudIpcDispatch dispatchQueryEvent:]"
- "-[FudIpcDispatch dispatchStateMachineEvent:]"
- "-[FudIpcDispatch dispatchStatelessEvent:]"
- "-[FudIpcDispatch enableStreamEventsForStateMachine:]"
- "-[FudIpcDispatch getPluginWithName:forFilter:delegate:info:options:]"
- "-[FudIpcDispatch getStorage]"
- "-[FudIpcDispatch isStateMachineAcceptingNewStreamEvents:]"
- "-[FudIpcDispatch isStateMachineBusyInExclusionGroup:]"
- "-[FudIpcDispatch isStateMachineForFilterAcceptingNewStreamEvents:]"
- "-[FudIpcDispatch issueNotification:request:]"
- "-[FudIpcDispatch issueNotification:request:]_block_invoke"
- "-[FudIpcDispatch notifyAccessoryAttachedWithEvent:]"
- "-[FudIpcDispatch queueUpEventForAccessory:stateMachine:]"
- "-[FudIpcDispatch registerClientWithEvent:error:]"
- "-[FudIpcDispatch sendDeviceClassAttached:toClient:]"
- "-[FudIpcDispatch sendReplyToDictionary:forCommand:withStatus:withError:]"
- "-[FudIpcDispatch setLastRemoteFindWithEvent:]"
- "-[FudIpcDispatch setupClientSessionWithEvent:error:]"
- "-[FudIpcDispatch stepComplete:stateMachine:status:error:info:]"
- "-[FudIpcDispatch stepProgress:stateMachine:progress:overallProgress:]"
- "-[FudIpcDispatch stepWillBegin:stateMachine:]"
- "-[FudIpcDispatch unregisterClientWithEvent:error:]"
- "-[UARPSandboxExtension initWithTokenString:]"
- "/var/db/fud"
- "@\"FudIpcDispatch\""
- "@\"MobileAccessoryUpdater\""
- "@\"NSObject<OS_dispatch_queue_attr>\""
- "@44@0:8i16@20@28@36"
- "Accessory disabled by defaults write. Ignoring %@ accessory=%@"
- "Active FW update detected for service %@, queue up %@"
- "AppleTV"
- "Asking user if they want to install optional update..."
- "Attemping to send external message to client:%@"
- "B32@0:8@16^@24"
- "B40@0:8@16i24B28@32"
- "Calling: %s"
- "Can't check if query event since it's nil"
- "Can't check state on nil event"
- "Can't create client info with nil name"
- "Can't create event with filter identifier"
- "Can't create stream event dictionary"
- "Can't deserialize with nil decoder"
- "Can't deserialize without client name"
- "Can't disable stream events since state machine has no filter!"
- "Can't dispatch NULL event, dropping it."
- "Can't dispatch command with no type."
- "Can't dispatch event without filter name"
- "Can't do next step query without filter name"
- "Can't do query with nil event"
- "Can't encode with nil encodoer"
- "Can't get clients for nil plugin name"
- "Can't handle API event with NULL client identifier"
- "Can't handle NULL broken connection"
- "Can't handle NULL internal message"
- "Can't handle NULL internal xpc api event"
- "Can't handle NULL xpc connection"
- "Can't handle NULL xpc stream event"
- "Can't handle device detached with nil device class"
- "Can't handle internal message without user info"
- "Can't handle nil internal message"
- "Can't load plugin with invalid filter name: %@ plugin name: %@"
- "Can't process NULL xpc event"
- "Can't queue up events for NULL state machine"
- "Can't register client with NULL plugin and group identifier"
- "Can't register for nil plugin name"
- "Can't register for plugin events with nil client identifier"
- "Can't register invalid client '%@'"
- "Can't register with nil client name"
- "Can't register with nil event"
- "Can't reply to NULL dictionary"
- "Can't reply to nil data"
- "Can't report completion with NULL state machine"
- "Can't report progress with NULL state machine"
- "Can't send NULL message back to client"
- "Can't send attached event without client"
- "Can't send attached event without device class"
- "Can't send message with NULL client connection"
- "Can't setup connection with nil event."
- "Can't setup session since connection information was NULL in inbound event"
- "Can't setup session since this client '%@' isn't registered for any events"
- "Can't take down CFUserNotification since it's nil"
- "Can't unregister a client that is not currently registered."
- "Can't unregister client without name"
- "Can't unregister with NULL event"
- "Checking exclusion group (%@) for already queued events..."
- "Clearing state for new event stream..."
- "Client '%@' can't register for unknown plugin '%@'"
- "Client '%@' isn't registered for any plugins"
- "Client disconnected: %@"
- "Client is already registered for plugin, preventing double registration. client:%@ plugin:%@"
- "ClientIdentifier"
- "ClientInfo"
- "ClientRegistrationName"
- "Command"
- "Complete"
- "Created XPC Listener = %p"
- "Creating new state machine for event: %@"
- "CrystalD"
- "Debugging event: %s"
- "Debugging inbound connection number %llu: %s"
- "Default client failed to register with group. Maybe no plugins match registration group?!?"
- "DefaultModalClient"
- "Defaults read for UARP periodic firmware check interval found = %lld"
- "Defaults read for periodic firmware check interval found = %lld"
- "Dequeue duplicate connection event: %@"
- "Disabiling stream events for device class: %@"
- "Disconnected client currently isn't registered for any plugins, can't unregister them."
- "Dispatching query event"
- "Dropping attach event since state machine in exclusion group (%@) is busy"
- "Dumping event "
- "Empty set of exclusion groups found for group: %@"
- "Enabling stream events for suspended device class: %@"
- "Error"
- "Error, nil policy for plugin: %@"
- "Error: Client is not entitled"
- "Event queued up [%lu] - [%@ : %@]"
- "ExclusionGroupFilter: %@ (%@)"
- "Failed to allocate dictionary for disconnect"
- "Failed to allocate dictionary for event types"
- "Failed to allocate fud state path"
- "Failed to allocate options for MAU init"
- "Failed to allocate plugin policy"
- "Failed to allocate policies"
- "Failed to allocate processing queue"
- "Failed to allocate queued array for MAU init"
- "Failed to allocate room for default clients"
- "Failed to allocate service policy"
- "Failed to allocate xpc dictionary for attached event"
- "Failed to allocate xpc dictionary for progress"
- "Failed to allocate xpc dictionary for step complete"
- "Failed to convert identifer to cstring"
- "Failed to convert msg to xpc dict"
- "Failed to covert fud command %d into a string value for client"
- "Failed to create FudEvent from xpc message"
- "Failed to create FudIpcDispatch instance from fud storage"
- "Failed to create MAU updater for DMC: %@"
- "Failed to create default modal client"
- "Failed to create earlyInstance"
- "Failed to create event"
- "Failed to create fud xpc listener"
- "Failed to create header string"
- "Failed to create info Dict from xpcevent"
- "Failed to create plugin directory URL"
- "Failed to create question notification"
- "Failed to create reply dictionary from inbound dict"
- "Failed to create response dictionary, can't reply to client now"
- "Failed to create stame machine for plugin: %@"
- "Failed to create storage directory at path:%@ error:%@"
- "Failed to create update message"
- "Failed to fetch plugin info dictionary"
- "Failed to fetch service info dictionary"
- "Failed to find policy owning filter: %@"
- "Failed to get client object"
- "Failed to get device class C string"
- "Failed to get file manager"
- "Failed to get filter in policy"
- "Failed to get filter type cstring"
- "Failed to get fud bundle for localization"
- "Failed to get policy for filter ending event"
- "Failed to get state machine for filter:%@"
- "Failed to get storage object"
- "Failed to get xpc connection from inbound dictionary"
- "Failed to initialize client"
- "Failed to load plugin bundle"
- "Failed to load service bundle"
- "Failed to register client: %@"
- "Failed to register client:%@ for group:%@"
- "Failed to save declined accessory at url %@"
- "Failed to send message to client, suspending their queue."
- "Failed to send message to client."
- "Failed to set state machine for filter: %@"
- "Failed to unregister client '%@' from plugin '%@', continuing..."
- "Filter %@ needs MayReboot check"
- "Filter %@ needs device idle check"
- "Filter %@ needs installer check"
- "Filter %@ needs periodic check"
- "FilterIdentifier"
- "Fud got an API event..."
- "Fud got internal API event..."
- "FudController"
- "FudEvent"
- "FudEvent - Client:%@ Type:%d Filter:%@ Data:%s Options:%@"
- "FudIPCDispatch: stepComplete():  plugin:%@ status:%d info=%@"
- "FudIpcDispatch"
- "FudSM successful=%d aOperation=%d aCommand=%d nextStateMachineStep=%d nextFudCommand=%d nextStepString=%@"
- "Got an internal client message"
- "Got disconnection from unmanaged connection"
- "GroupIdentifier"
- "Handler: Device Idle Check Kicked Off - STATE=%ld"
- "Handler: May Reboot Check Kicked Off - STATE=%ld"
- "Handler: Periodic Firmware Check Kicked Off - STATE=%ld"
- "Handler: UARP Periodic Firmware Check Kicked Off - STATE=%ld"
- "Ignoring puck arrived notifications until FW issues resolved - %@"
- "Initializing fud..."
- "Internal"
- "InternalClient"
- "InternalMessage"
- "Invalid Filtername"
- "Invalid xpcevent"
- "IsInternalClient"
- "Kicking off FUDGenericKextUpdater Plugin earlyboot path"
- "Kicking off device idle firmware check event for %@, xpcFilter=%@"
- "Kicking off installer check event for %@, xpcFilter=%@"
- "Kicking off may reboot event for %@, xpcFilter=%@"
- "Kicking off periodic check event for %@, xpcFilter=%@"
- "Kicking off queuedEvent=%@"
- "Kickstarting accessory with continue event: %@"
- "MAUInternalMessageFudNotification"
- "MayRebootLaunch"
- "Missing LAST_REMOTE_FIND_DATE parameter in SET_LAST_REMOTE_FIND event."
- "Missing filter name in SET_LAST_REMOTE_FIND event."
- "Missing filter name in state machine!"
- "Missing options in SET_LAST_REMOTE_FIND event."
- "Modal Client - Updated queue=%@"
- "Modal Default Client - Advancing state machine...+"
- "Modal Default Client - Advancing state machine...-"
- "Modal Default Client - Can't show UI for '%@' since we're already showing a UI for '%@'"
- "Modal Default Client - DEFAULT - aStepName=%@, nextStep=%@, stepInfo=%@"
- "Modal Default Client - Device Attached:%@ Next-Step:%@"
- "Modal Default Client - Device class detached:%@ error:%@"
- "Modal Default Client - Got device attach event for %@ updateInProgress=%d queue[%lu]=%@"
- "Modal Default Client - Kicking off queued=%@ queue=%@"
- "Modal Default Client - Not advancing state machine+"
- "Modal Default Client - Not advancing state machine-"
- "Modal Default Client - completed step:%@ device:%@ successful:%@ next-step:%@ silentUpdate=%d error:%@"
- "Modal Default Client - queue[%lu]=%@"
- "Modal Default Client - step:%@  device:%@ progress:%f overall-progress:%f stepInfo=%@"
- "Modal Default Client - stepInfo=%@"
- "Modal Default Client - updated queue=%@"
- "Modal UI"
- "Next operation is: %lld"
- "NextStep"
- "No clients to notify installer update is active"
- "No clients to send disconnect message to"
- "No exclusion group"
- "No exclusion group in filter: %@"
- "No filter found with name: %@"
- "No filter owns this state machine, can't deliver event to client now"
- "No filter owns this state machine, can't deliver progress to client now"
- "No filter owns this state machine, can't queue up events"
- "No matching filter found with filter name: %@"
- "No set of exclusion groups found for group: %@"
- "No valid client to notify installer update is active"
- "NotificationRequest"
- "Notifying client about attached event. client:%@ device:%@"
- "Notifying client to setup connection to fud"
- "OverallProgress"
- "Percent Complete"
- "Performing apply command..."
- "Performing bootstrap command..."
- "Performing done command... queueCount=%lu"
- "Performing download command..."
- "Performing find command..."
- "Performing finish command..."
- "Performing next command..."
- "Performing prepare command..."
- "Plugin disabled by defaults write. Ignoring %@ plugin=%@"
- "Plugin policy is invalid, can't load it. bundle:%@"
- "Plugin policy is invalid, can't load it. service:%@"
- "PluginsList"
- "Prefs for disablePlugin: %@ disableAcc: %@"
- "Processing disconnection for connection: %X"
- "Progress"
- "RUN Handler called for activity: %s"
- "Registering First Launch XPC activity %s with criteria = %@"
- "Registering XPC activity %s with XPC_ACTIVITY_CHECK_IN"
- "Registering filter with XPC stream: %@"
- "Registering filter with XPC stream: %s"
- "Registering internal default clients..."
- "Resetting state"
- "Response"
- "Resuming client queue ref:%@"
- "Resuming event queue for client: %@"
- "Resuming fud..."
- "Resuming state machine..."
- "Saving declined accessory at url %@"
- "Sending query response."
- "Set acc for statemachine %@ %@"
- "Setting context on connection:%X value:%@"
- "Setting event handler for Plugin:%@ Filter:%@"
- "Started timer source countdown..."
- "State machine in exclusion group (%@) is busy, dropping stream event..."
- "Status"
- "Stopping idle timer..."
- "Stream event happened for filter: %@"
- "Successfully loaded plugin policy for: %@"
- "Successfully loaded service policy for: %@"
- "Successfully registered client '%@' for identifier '%@'"
- "Successfully registered default client"
- "Successfully unregistered client '%@' from plugin '%@'"
- "Suspending client queue ref:%@"
- "Synthesizing stream event for: %s"
- "T@\"AUDAccessory\",&,V_accessory"
- "T@\"NSDictionary\",&,VclientOptions"
- "T@\"NSObject<OS_dispatch_queue>\",R,VworkQueue"
- "T@\"NSObject<OS_xpc_object>\",R,Vconnection"
- "T@\"NSObject<OS_xpc_object>\",R,Vdata"
- "T@\"NSString\",&,VclientName"
- "T@\"NSString\",&,VmodalDeviceClass"
- "T@\"NSString\",R,Vname"
- "TB,VdidRequestReconnect"
- "TB,VisConnectionEvent"
- "TB,VisInternalClient"
- "TB,VsendResponse"
- "TB,VsynthesizedEvent"
- "Taking notification down."
- "There are %lu clients registered for this plugin event"
- "There are %lu registered clients for filter: %@"
- "There are no plugins with group name '%@'"
- "There are no registered clients for plugin '%@'"
- "There is no plugin bundle for: %@"
- "There is no policy for the filter: %@"
- "There was no policy owning filter '%@', dropping event."
- "Ti,R,Vtype"
- "Timer source fired!"
- "Trying to load plugin: %@"
- "Trying to load service: %@"
- "UARPSandboxExtension"
- "Unknown internal API event received: %d"
- "Unknown query operation requested"
- "Unknown state for value:%d"
- "Unrecognized state machine command: %d"
- "Updated queuedEvents[%lu]=%@"
- "Updating Title Format"
- "UseDropboxLocation"
- "User response was: %lu ignorePromptResponse=%d updateInprogress=%d"
- "You need storage to run dispatch class!"
- "_attr"
- "_defaultClients"
- "_fudIpcDispatch"
- "_fudStorage"
- "_isMayRebootLaunch"
- "_isSimulatedDeviceIdleLaunch"
- "_numProcessedConnection"
- "_sandboxExtensionHandle"
- "_simulateIdleUseFilepath"
- "addEventToQueue:withFilter:stateMachine:"
- "addObserver:selector:name:object:"
- "attr"
- "clientName"
- "clientOptions"
- "clientOptions = %@"
- "com.apple.MobileAccessoryUpdater.FUDGenericKextUpdater"
- "com.apple.MobileAccessoryUpdater.auSimulateIdle"
- "com.apple.MobileAccessoryUpdater.auSimulateIdleLaunch"
- "com.apple.MobileAccessoryUpdater.defaultmodalclient"
- "com.apple.MobileAccessoryUpdater.dispatch.workQueue"
- "com.apple.MobileAccessoryUpdater.fud.timeoutQueue"
- "com.apple.MobileAccessoryUpdater.mayRebootCheck"
- "com.apple.app-sandbox.read-write"
- "com.apple.fud.defaultmodalclient"
- "com.apple.fud.processing.queue"
- "com.apple.fud.updateTriggered"
- "com.apple.mobileaccessoryupdater.externalclientaccess"
- "completed step:Bootstrap successful:NO"
- "connection"
- "criticalSectionSemaphore"
- "data"
- "defaultCenter"
- "dictionaryWithObject:forKey:"
- "didRequestReconnect"
- "didSuspendEventQueue"
- "dispatchEvent:"
- "dispatchQueryEvent:"
- "dispatchStateMachineEvent:"
- "dispatchStatelessEvent:"
- "doDeviceIdleCheck"
- "doInstallerCheck"
- "doMayRebootCheck"
- "doPeriodicCheck"
- "doSimulateIdleCheck"
- "event: %@, eventType = %llu, pluginName = %@, options = %@"
- "eventFlags"
- "eventQueue"
- "forceRestart"
- "frameworkBundle"
- "getClientWithName:"
- "getRegisteredClientsForPlugin:"
- "handleBrokenConnection:"
- "handleInternalAPIEvent:"
- "handleInternalClientMessage:"
- "handleXPCAPIEvent:"
- "handling CHECK IN state for activity: %s"
- "https://basejumper.apple.com/assets"
- "https://basejumper.apple.com/livability"
- "ignorePromptResponse"
- "initWithEventType:filter:client:data:"
- "initWithGroup:"
- "initWithName:connection:"
- "initWithName:connection:isInternalClient:"
- "initWithPluginIdentifier:isGroupIdentifier:delegate:isInternalClient:options:error:"
- "initializeFud"
- "installerUpdateActive"
- "isEventQueryRequest:"
- "isEventStateless:"
- "isInternalClient"
- "isInternalEvent"
- "isStateMachineAcceptingNewStreamEvents:"
- "lastUpdateTime"
- "migrateExistingDefaults"
- "modalDeviceClass"
- "notification"
- "notifications"
- "notifyAccessoryAttachedWithEvent:"
- "notifyClientsOfInstallerUpdate:"
- "pendingDeviceAttachedEvents"
- "pluginList is: %@"
- "pluginToClients"
- "policies = NULL"
- "processAPIDict:"
- "processEvent:"
- "processingQueue"
- "queryNextStep:"
- "queuedAccessories"
- "queuedEvents"
- "queuedEvents[%lu]=%@"
- "registerClient:withGroup:"
- "registerClient:withPlugin:"
- "registerClientWithEvent:error:"
- "removeObserver:name:object:"
- "seedParticipation"
- "seedParticipationDictionary"
- "sendDeviceClassAttached:toClient:"
- "sendMessage:"
- "sendReplyToDictionary:forCommand:withStatus:withError:"
- "sendResponse"
- "setActivityForMayRebootLaunch:"
- "setClientName:"
- "setClientOptions:"
- "setConnection:"
- "setDidRequestReconnect:"
- "setIsInternalClient:"
- "setLastRemoteFindWithEvent:"
- "setModalDeviceClass:"
- "setSendResponse:"
- "setSynthesizedEvent:"
- "setupClientSessionWithEvent:error:"
- "startDefaultClients"
- "state machine exists: active=%d for [%@ : %@]"
- "storage"
- "synthesizedEvent"
- "unregisterAllClients"
- "unregisterClient:fromPlugin:"
- "unregisterClientFromAllPlugins:"
- "unregisterClientWithEvent:error:"
- "updateInProgress"
- "updated queuedEvents[%lu]=%@"
- "updater"
- "useProgressBar"

```

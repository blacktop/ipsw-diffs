## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-455.30.6.9.11
-  __TEXT.__text: 0x21efa4
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x16d40
-  __TEXT.__objc_methlist: 0xf7dc
-  __TEXT.__const: 0x2db30
-  __TEXT.__gcc_except_tab: 0x2ce8
-  __TEXT.__objc_methname: 0x1c990
-  __TEXT.__oslogstring: 0x11519
-  __TEXT.__cstring: 0x8eb8
-  __TEXT.__objc_classname: 0x1a80
-  __TEXT.__objc_methtype: 0x3195
+455.30.6.9.18
+  __TEXT.__text: 0x22df1c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_stubs: 0x172e0
+  __TEXT.__objc_methlist: 0xf9ac
+  __TEXT.__const: 0x2dc60
+  __TEXT.__gcc_except_tab: 0x2dcc
+  __TEXT.__objc_methname: 0x1d0d3
+  __TEXT.__oslogstring: 0x11e1c
+  __TEXT.__cstring: 0x9298
+  __TEXT.__objc_classname: 0x1a9a
+  __TEXT.__objc_methtype: 0x3175
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x35d0
+  __TEXT.__unwind_info: 0x3678
   __TEXT.__eh_frame: 0x3a0
-  __DATA_CONST.__auth_got: 0x860
+  __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xd978
-  __DATA_CONST.__cfstring: 0xa860
-  __DATA_CONST.__objc_classlist: 0x6d8
+  __DATA_CONST.__const: 0xecf8
+  __DATA_CONST.__cfstring: 0xab80
+  __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19d50
-  __DATA.__objc_selrefs: 0x67e8
-  __DATA.__objc_ivar: 0x10d8
-  __DATA.__objc_data: 0x44f0
-  __DATA.__data: 0x2450
-  __DATA.__bss: 0x808
-  __DATA.__common: 0x1c
+  __DATA.__objc_const: 0x19f40
+  __DATA.__objc_selrefs: 0x6950
+  __DATA.__objc_ivar: 0x10f0
+  __DATA.__objc_data: 0x4540
+  __DATA.__data: 0x2400
+  __DATA.__bss: 0x818
+  __DATA.__common: 0x69
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1AF425AF-6B31-342F-92BE-F5D1E01C28CE
-  Functions: 6039
-  Symbols:   637
-  CStrings:  9939
+  UUID: 5379220D-ED2B-34CA-B553-B09E5D595FDF
+  Functions: 6137
+  Symbols:   640
+  CStrings:  10109
 
Symbols:
+ _NSLog
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _dispatch_activate
+ _sysctlbyname
- _FMDRepairDeviceThisDeviceIdentifier
- _OBJC_CLASS_$_FMDRepairDevice
CStrings:
+ "%@ already submitted"
+ "%s - Failed to get follow up strings with error: %@"
+ "%s: Cleared CFU for %@"
+ "%s: Failed with error: %@"
+ "%s: Requested a CFU for %@"
+ "%s: timed out"
+ "-[FMDCoreFollowUpManager _forceTheftAndLossCFU]_block_invoke"
+ "-[FMDCoreFollowUpManager submitTheftAndLossReminderBackgroundTask:]_block_invoke"
+ "-[FMDFMIPXPCServer clearRepairCFUWithDeviceID:reply:]"
+ "-[FMDFMIPXPCServer postRepairCFUWithDeviceID:reply:]"
+ "-[FMDSharedConfigurationManager clearRepairCFUWithDeviceID:completion:]_block_invoke"
+ "-[FMDSharedConfigurationManager clearRepairCFUWithDeviceID:completion:]_block_invoke_2"
+ "-[FMDSharedConfigurationManager postRepairCFUWithDeviceID:completion:]_block_invoke"
+ "-[FMDSharedConfigurationManager postRepairCFUWithDeviceID:completion:]_block_invoke_2"
+ "@64@0:8@16@24@32@40q48@56"
+ "@72@0:8@16@24@32@40q48@56@64"
+ "AUTHORIZE_REPAIR"
+ "AUTHORIZE_REPAIR_TEARDOWN"
+ "AppleTV"
+ "AppleTV_Watch"
+ "AppleTV_Watches"
+ "B16@?0@\"NSError\"8"
+ "B20@?0B8@\"NSError\"12"
+ "B24@?0Q8@\"NSError\"16"
+ "Bail on scheduling TnL reminder timer. Reminder interval (%ld)."
+ "Before first unlock. Submit reminder TnL task."
+ "Clear repair CFU for deviceID %@"
+ "Cleared the Enable Repair CFU for %@"
+ "Cleared the Theft and Loss CFU"
+ "Could not read accessory registry connected accessories from disk %@"
+ "Could not update config with error (%@). Use existing/cached values."
+ "Create repair CFU for deviceID %@"
+ "DAEMON API - primaryAppleAccountRemoved"
+ "Device does not have coverage. Make best effort to clear the CFU."
+ "Device got TnL coverage. Immediately display the CFU."
+ "Device is covered by Theft and Loss when turning off FMiP, scheduling CFU"
+ "Device is not covered by Theft and Loss when turning off FMiP, clearing CFU"
+ "Enable Repair CFU posted for %@"
+ "Error getting boot session UUID"
+ "Error getting boot session UUID size"
+ "FMDAccessoryRegistry saveConnectedAccessoriesToDisk %@"
+ "FMDConnectedAccessoryFailedReadEventName"
+ "FMDCoreFollowUpManager"
+ "Failed to clear the Enable Repair CFU for %@ with error: %@"
+ "Failed to clear the Theft and Loss CFU with error: %@"
+ "Failed to get T&L coverage (clearing T&L CFU), error: %@"
+ "Failed to get T&L coverage: %@"
+ "Failed to look up the serial number. Unable to proceed with CFU work."
+ "Failed to post Enable Repair CFU for %@ with error: %@"
+ "Failed to queue up the Theft and Loss CFU with error: %@"
+ "Failed to register task %@"
+ "Failed to submit task %@"
+ "First unlock. Register for TnL CFU."
+ "Last FMiP signout: %@"
+ "Mac"
+ "Mac_Watch"
+ "Mac_Watches"
+ "Missing device serial number."
+ "No serial number or device identifier"
+ "Not triggering the CFU. error (%@), fmipState (%lu)"
+ "REL"
+ "REPAIR"
+ "Repair CFU intent is missing deviceID"
+ "Submitted task %@ to run after first unlock"
+ "T@\"FMDCoreFollowUpManager\",R,N"
+ "T@\"FMDataArchiver\",&,N,V_connectedAccessoriesDataArchiver"
+ "T@\"NSMutableDictionary\",&,N,V_connectedAccessoryIdentifiersToBootId"
+ "T@\"NSString\",&,N,V_currentBootUUID"
+ "T@\"NSString\",R,N,V_deviceIdentifier"
+ "T@\"NSString\",R,N,V_serialNumber"
+ "Task %@ ran but there's no record of a last Find My iPhone Sign out"
+ "Theft and Loss CFU posted"
+ "Theft and Loss CFU should not be posted, clearing"
+ "Unhandled Theft and Loss context: %lu"
+ "Unhandled cmd %@"
+ "Unhandled configuration - coverage (%lu), device class (%lu)"
+ "User signed out of FMIP %@"
+ "User signed out, clearing CFU"
+ "Watches"
+ "XPC error for %s: %li"
+ "XPC error for clearTheftAndLossCFU: %li"
+ "XPC error for postTheftAndLossCFU: %li"
+ "_connectedAccessoriesDataArchiver"
+ "_connectedAccessoryIdentifiersToBootId"
+ "_currentBootUUID"
+ "_deviceIdentifier"
+ "_forceTheftAndLossCFU"
+ "_getDeviceClassesFromCoverage:"
+ "_getTheftAndLossFollowUpStringsWithCompletion:"
+ "_handleRepairCFUIntent:serverContext:"
+ "_handleTheftAndLossReminderBackgroundTask"
+ "_initWithAccount:ephemeralToken:dsid:callingClient:mode:serialNumber:deviceIdentifier:"
+ "_registerTheftAndLossCFUBackgroundTask"
+ "archiverFromURL:"
+ "bootSessionUUID"
+ "clearFindMySignOutTimeFile"
+ "clearRepairCFUWithDeviceID:completion:"
+ "clearRepairCFUWithDeviceID:reply:"
+ "clearTheftAndLossCFU: Cleared a CFU"
+ "clearTheftAndLossCFU: Failed with error: %@"
+ "clearTheftAndLossCFU: Timed out"
+ "clearTheftAndLossCFUWithCompletion:"
+ "com.apple.findmy.theftandlosscfu"
+ "com.apple.findmy.theftandlosscfu.firstunlock"
+ "com.apple.icloud.findmydeviced.connectedAccessories"
+ "com.apple.newdeviceoutreach.coverageupdated"
+ "connectedAccessoriesDataArchiver"
+ "connectedAccessoriesStorageLocation"
+ "connectedAccessoryIdentifiersToBootId"
+ "currentBootUUID"
+ "deviceCoverageWithSerialNumber: %@, timed out"
+ "deviceForRepair"
+ "deviceIdentifier"
+ "doNotUseDefaultConfigs"
+ "fmipStateWithCompletion:"
+ "followUpStrings"
+ "getTheftAndLossCoverageWithSerialNumber:completion:"
+ "getTheftAndLossCoverageWithSerialNumber:timeout:completion:"
+ "handleNDOCoverageUpdate"
+ "iPad"
+ "iPad_Watch"
+ "iPad_Watches"
+ "iPhone"
+ "iPhone_Watch"
+ "iPhone_Watches"
+ "initWithAccount:ephemeralToken:dsid:callingClient:mode:deviceIdentifier:"
+ "initWithAccount:ephemeralToken:dsid:callingClient:mode:serialNumber:"
+ "kern.bootsessionuuid"
+ "not using default configs"
+ "postRepairCFUWithDeviceID:completion:"
+ "postRepairCFUWithDeviceID:reply:"
+ "postTheftAndLossCFU: Failed with error: %@"
+ "postTheftAndLossCFU: Requested a CFU (shouldEnable: %d)"
+ "postTheftAndLossCFU: timed out"
+ "postTheftAndLossCFU:completion:"
+ "primaryAppleAccountRemoved"
+ "processRepairRequest:"
+ "processRepairTeardownRequest:"
+ "readConnectedAccessoriesFromDisk"
+ "readFindMySignOutTimeFromFile"
+ "registerAndSubmitBGSTForFirstUnlock"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "reminderInMins"
+ "requestTheftAndLossCFU:"
+ "sanitizeConnectedAccessoriesWithoutMatchingBootId"
+ "saveConnectedAccessoriesDictToDisk"
+ "scheduleAfter"
+ "setConnectedAccessoriesDataArchiver:"
+ "setConnectedAccessoryIdentifiersToBootId:"
+ "setCurrentBootUUID:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "submitTaskRequest %@ to run in %f seconds."
+ "submitTaskRequest for %@ failed with error (%@)."
+ "submitTaskRequest:error:"
+ "submitTheftAndLossReminderBackgroundTask:"
+ "taskRequestForIdentifier:"
+ "using default configs"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@?0@\"FMDSharedConfigurationFollowUpEntry\"8@\"NSError\"16"
+ "v40@0:8@16d24@?32"
+ "writeFindMySignOutTimeToFile"
- "%s: Cleared a CFU"
- "%s: Requested a CFU"
- "-[FMDSharedConfigurationManager clearTheftAndLossCFU]"
- "-[FMDSharedConfigurationManager clearTheftAndLossCFU]_block_invoke_3"
- "-[FMDSharedConfigurationManager postTheftAndLossCFU:shouldEnable:]"
- "-[FMDSharedConfigurationManager postTheftAndLossCFU:shouldEnable:]_block_invoke_3"
- "@32@0:8@16^B24"
- "@56@0:8@16@24@32@40q48"
- "Request is not for the current device"
- "deviceEligibleForRepairWithContext for repairMode"
- "deviceEligibleForRepairWithContext for trade in mode"
- "deviceEligibleForRepairWithContext:completion:"
- "initWithClientIdentifier:isThisDevice:"
- "initWithDeviceIdentifier:ephemeralToken:dsid:callingClient:mode:"
- "isThisDevice"
- "postTheftAndLossCFU:shouldEnable:"
- "repair"
- "requestTheftAndLossCFUWithStrings:andReply:"
- "searchIdentifiers"
- "selectedDevices"
- "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"

```

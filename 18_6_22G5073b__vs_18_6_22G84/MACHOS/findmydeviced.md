## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.36.4.2.9
-  __TEXT.__text: 0x247bf8
+438.36.4.2.12
+  __TEXT.__text: 0x24a27c
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x16bc0
-  __TEXT.__objc_methlist: 0xf8ec
-  __TEXT.__const: 0x2cd00
-  __TEXT.__gcc_except_tab: 0x2d5c
-  __TEXT.__objc_methname: 0x1c880
-  __TEXT.__oslogstring: 0x10fab
-  __TEXT.__cstring: 0x8cb7
-  __TEXT.__objc_classname: 0x1aba
+  __TEXT.__objc_stubs: 0x16f40
+  __TEXT.__objc_methlist: 0xf9d4
+  __TEXT.__const: 0x2cd10
+  __TEXT.__gcc_except_tab: 0x2d7c
+  __TEXT.__objc_methname: 0x1cc19
+  __TEXT.__oslogstring: 0x11601
+  __TEXT.__cstring: 0x8ee7
+  __TEXT.__objc_classname: 0x1ad1
   __TEXT.__objc_methtype: 0x3197
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x3560
+  __TEXT.__unwind_info: 0x35b0
   __TEXT.__eh_frame: 0x378
   __DATA_CONST.__auth_got: 0x848
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__got: 0x928
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xdba8
-  __DATA_CONST.__cfstring: 0xa7c0
-  __DATA_CONST.__objc_classlist: 0x6d8
+  __DATA_CONST.__const: 0xdd38
+  __DATA_CONST.__cfstring: 0xaa00
+  __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19fb8
-  __DATA.__objc_selrefs: 0x6788
-  __DATA.__objc_ivar: 0x10cc
-  __DATA.__objc_data: 0x44f0
+  __DATA.__objc_const: 0x1a0d8
+  __DATA.__objc_selrefs: 0x6868
+  __DATA.__objc_ivar: 0x10d4
+  __DATA.__objc_data: 0x4540
   __DATA.__data: 0x24c0
-  __DATA.__bss: 0x800
+  __DATA.__bss: 0x810
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F4B37C51-A13E-3543-BBB3-FA12B643E2E6
-  Functions: 6042
-  Symbols:   646
-  CStrings:  9877
+  UUID: FD78BF13-0B13-3EA2-9F75-0128F9541119
+  Functions: 6087
+  Symbols:   648
+  CStrings:  9985
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
CStrings:
+ "%@ already submitted"
+ "%s - Failed to get follow up strings with error: %@"
+ "-[FMDCoreFollowUpManager _forceTheftAndLossCFU]_block_invoke"
+ "-[FMDCoreFollowUpManager submitTheftAndLossReminderBackgroundTask:]_block_invoke"
+ "AppleTV"
+ "AppleTV_Watch"
+ "AppleTV_Watches"
+ "Bail on scheduling TnL reminder timer. Reminder interval (%ld)."
+ "Before first unlock. Submit reminder TnL task."
+ "Cleared the Theft and Loss CFU"
+ "Could not update config with error (%@). Use existing/cached values."
+ "DAEMON API - primaryAppleAccountRemoved"
+ "Device does not have coverage. Make best effort to clear the CFU."
+ "Device got TnL coverage. Immediately display the CFU."
+ "Device is covered by Theft and Loss when turning off FMiP, scheduling CFU"
+ "Device is not covered by Theft and Loss when turning off FMiP, clearing CFU"
+ "FMDCoreFollowUpManager"
+ "Failed to clear the Theft and Loss CFU with error: %@"
+ "Failed to get T&L coverage (clearing T&L CFU), error: %@"
+ "Failed to get T&L coverage: %@"
+ "Failed to look up the serial number. Unable to proceed with CFU work."
+ "Failed to queue up the Theft and Loss CFU with error: %@"
+ "Failed to register task %@"
+ "Failed to submit task %@"
+ "First unlock. Register for TnL CFU."
+ "Last FMiP signout: %@"
+ "Mac"
+ "Mac_Watch"
+ "Mac_Watches"
+ "Not triggering the CFU. error (%@), fmipState (%lu)"
+ "SecureLocationMonitor didUpdateLocations entered"
+ "SecureLocationMonitor didUpdateLocations for satellite location"
+ "Submitted task %@ to run after first unlock"
+ "T@\"FMDCoreFollowUpManager\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stewieLocationManagerQueue"
+ "Task %@ ran but there's no record of a last Find My iPhone Sign out"
+ "Theft and Loss CFU posted"
+ "Theft and Loss CFU should not be posted, clearing"
+ "Unhandled Theft and Loss context: %lu"
+ "Unhandled configuration - coverage (%lu), device class (%lu)"
+ "User signed out of FMIP %@"
+ "User signed out, clearing CFU"
+ "Watches"
+ "_forceTheftAndLossCFU"
+ "_getDeviceClassesFromCoverage:"
+ "_getTheftAndLossFollowUpStringsWithCompletion:"
+ "_handleTheftAndLossReminderBackgroundTask"
+ "_registerTheftAndLossCFUBackgroundTask"
+ "_stewieLocationManagerQueue"
+ "clearFindMySignOutTimeFile"
+ "clearTheftAndLossCFU"
+ "com.apple.findmy.theftandlosscfu"
+ "com.apple.findmy.theftandlosscfu.firstunlock"
+ "com.apple.findmydevice.stewieLocationManagerQueue"
+ "com.apple.newdeviceoutreach.coverageupdated"
+ "doNotUseDefaultConfigs"
+ "fmipStateWithCompletion:"
+ "followUpStrings"
+ "handleNDOCoverageUpdate"
+ "iPad"
+ "iPad_Watch"
+ "iPad_Watches"
+ "iPhone"
+ "iPhone_Watch"
+ "iPhone_Watches"
+ "not using default configs"
+ "primaryAppleAccountRemoved"
+ "readFindMySignOutTimeFromFile"
+ "registerAndSubmitBGSTForFirstUnlock"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "reminderInMins"
+ "requestTheftAndLossCFU:"
+ "scheduleAfter"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setScheduleAfter:"
+ "setStewieLocationManagerQueue:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "stewieLocationManagerQueue"
+ "submitTaskRequest %@ to run in %f seconds."
+ "submitTaskRequest for %@ failed with error (%@)."
+ "submitTaskRequest:error:"
+ "submitTheftAndLossReminderBackgroundTask:"
+ "taskRequestForIdentifier:"
+ "using default configs"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@?0@\"FMDSharedConfigurationFollowUpEntry\"8@\"NSError\"16"
+ "writeFindMySignOutTimeToFile"

```

## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.36.4.2.4
-  __TEXT.__text: 0x247f24
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0x16e20
-  __TEXT.__objc_methlist: 0xf904
+438.36.4.2.9
+  __TEXT.__text: 0x247bf8
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_stubs: 0x16bc0
+  __TEXT.__objc_methlist: 0xf8ec
   __TEXT.__const: 0x2cd00
-  __TEXT.__gcc_except_tab: 0x2d20
-  __TEXT.__objc_methname: 0x1ca02
-  __TEXT.__oslogstring: 0x110f9
-  __TEXT.__cstring: 0x8e47
-  __TEXT.__objc_classname: 0x1ad1
-  __TEXT.__objc_methtype: 0x30fe
+  __TEXT.__gcc_except_tab: 0x2d5c
+  __TEXT.__objc_methname: 0x1c880
+  __TEXT.__oslogstring: 0x10fab
+  __TEXT.__cstring: 0x8cb7
+  __TEXT.__objc_classname: 0x1aba
+  __TEXT.__objc_methtype: 0x3197
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x3558
+  __TEXT.__unwind_info: 0x3560
   __TEXT.__eh_frame: 0x378
-  __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xdb18
-  __DATA_CONST.__cfstring: 0xa880
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__const: 0xdba8
+  __DATA_CONST.__cfstring: 0xa7c0
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1a058
-  __DATA.__objc_selrefs: 0x6800
+  __DATA.__objc_const: 0x19fb8
+  __DATA.__objc_selrefs: 0x6788
   __DATA.__objc_ivar: 0x10cc
-  __DATA.__objc_data: 0x4540
+  __DATA.__objc_data: 0x44f0
   __DATA.__data: 0x24c0
-  __DATA.__bss: 0x810
+  __DATA.__bss: 0x800
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D4D8B401-53F4-3605-BDCB-CB49B6897FF2
-  Functions: 6045
-  Symbols:   647
-  CStrings:  9916
+  UUID: F4B37C51-A13E-3543-BBB3-FA12B643E2E6
+  Functions: 6042
+  Symbols:   646
+  CStrings:  9877
 
Symbols:
+ _dispatch_activate
- _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
- _OBJC_CLASS_$_BGSystemTaskScheduler
Functions (added):
+ sub_100032f9c
+ sub_100033374
+ sub_1000334a0
+ sub_1000335b0
+ sub_100033b20
+ sub_1000341f0
+ sub_10003462c
+ sub_1000347cc
+ sub_100034dd0
+ sub_1000354f4
+ sub_100085b80
+ sub_100085c3c

Functions (removed):
- sub_1000d4ef4
- sub_100101318
- sub_10023ee04
- sub_100245e7c
- sub_100247fc4
- sub_1002492b8
- sub_1002495d4
- sub_100249cc8
- sub_10024a00c
- sub_10024a198
- sub_10024a36c
- sub_10024a3d4
- sub_10024a564
- sub_10024a700
- sub_10024a714
CStrings:
+ "-[FMDFMIPXPCServer postTheftAndLossCFUWithEntry:reply:]"
+ "B16@?0@\"NSError\"8"
+ "B20@?0B8@\"NSError\"12"
+ "B24@?0Q8@\"NSError\"16"
+ "XPC error for clearTheftAndLossCFU: %li"
+ "XPC error for postTheftAndLossCFU: %li"
+ "awarenessStrings"
+ "clearTheftAndLossCFU: Cleared a CFU"
+ "clearTheftAndLossCFU: Failed with error: %@"
+ "clearTheftAndLossCFU: Timed out"
+ "clearTheftAndLossCFUWithCompletion:"
+ "deviceCoverageWithSerialNumber: %@, timed out"
+ "getTheftAndLossCoverageWithSerialNumber:completion:"
+ "getTheftAndLossCoverageWithSerialNumber:timeout:completion:"
+ "liteLocationPublishRequestNotification:"
+ "postTheftAndLossCFU: Failed with error: %@"
+ "postTheftAndLossCFU: Requested a CFU (shouldEnable: %d)"
+ "postTheftAndLossCFU: timed out"
+ "postTheftAndLossCFU:completion:"
+ "postTheftAndLossCFUWithEntry:reply:"
+ "requestTheftAndLossCFUWithStrings:andReply:"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?B@\"NSError\">24"
+ "v40@0:8@16d24@?32"
- "%s: Cleared a CFU"
- "%s: Requested a CFU"
- "%s: Timed out"
- "-[FMDFMIPXPCServer requestTheftAndLossCFUWithReply:]"
- "-[FMDSharedConfigurationManager clearTheftAndLossCFU]"
- "-[FMDSharedConfigurationManager clearTheftAndLossCFU]_block_invoke_3"
- "-[FMDSharedConfigurationManager requestTheftAndLossCFU]"
- "-[FMDSharedConfigurationManager requestTheftAndLossCFU]_block_invoke_3"
- "Application Support"
- "Calling process is missing container entitlements"
- "FMDCoreFollowUpManager"
- "Failed to clear the Theft and Loss CFU with error: %@"
- "Failed to create container directories"
- "Failed to queue up the Theft and Loss CFU with error: %@"
- "Failed to read contents with error: %@"
- "Failed to remove file (%@) with error %@."
- "Failed to write the timestamp to %@ with error %@."
- "Invalid URL (%@) for the timestamp file."
- "Library"
- "No contents"
- "No record of the last sign out. Bailing."
- "Removed (%@)."
- "SignOutTimestamp"
- "T@\"FMDCoreFollowUpManager\",R,N"
- "Unhandled Theft and Loss context: %lu"
- "Wrote (%@) to (%@)."
- "clearFindMySignOutTimeFile"
- "clearTheftAndLossCFU"
- "com.apple.findmy.theftandlosscfu"
- "com.apple.icloud.searchparty.secureLocations.stewiePublishRequest"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "fileExistsAtPath:isDirectory:"
- "fm_dictionaryWithContentsOfURL:error:"
- "forceDownloadWithReply completed with error: %@"
- "forceDownloadWithReply:"
- "group.com.apple.icloud.findmydevice.followup"
- "readFindMySignOutTimeFromFile"
- "registerForTaskWithIdentifier failed"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "requestTheftAndLossCFU"
- "requestTheftAndLossCFU:"
- "requestTheftAndLossCFUWithReply:"
- "setRequiresExternalPower:"
- "setRequiresNetworkConnectivity:"
- "setScheduleAfter:"
- "setTaskCompleted"
- "sharedScheduler"
- "signOutTimestampFileURL"
- "submitTaskRequest for %@ failed with error (%@)"
- "submitTaskRequest:error:"
- "submitted task %@"
- "taskRequestForIdentifier:"
- "theftandloss.plist"
- "v16@?0@\"BGSystemTask\"8"
- "writeFindMySignOutTimeToFile"
- "writeToURL:error:"

```

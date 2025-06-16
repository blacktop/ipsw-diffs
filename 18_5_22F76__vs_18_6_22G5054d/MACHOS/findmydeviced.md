## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.35.2.11.19
-  __TEXT.__text: 0x2461d0
+438.36.4.2.4
+  __TEXT.__text: 0x247f24
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0x16b20
-  __TEXT.__objc_methlist: 0xf854
-  __TEXT.__const: 0x2cc50
-  __TEXT.__gcc_except_tab: 0x2cb0
-  __TEXT.__objc_methname: 0x1c71f
-  __TEXT.__oslogstring: 0x10e6c
-  __TEXT.__cstring: 0x8c57
-  __TEXT.__objc_classname: 0x1aba
+  __TEXT.__objc_stubs: 0x16e20
+  __TEXT.__objc_methlist: 0xf904
+  __TEXT.__const: 0x2cd00
+  __TEXT.__gcc_except_tab: 0x2d20
+  __TEXT.__objc_methname: 0x1ca02
+  __TEXT.__oslogstring: 0x110f9
+  __TEXT.__cstring: 0x8e47
+  __TEXT.__objc_classname: 0x1ad1
   __TEXT.__objc_methtype: 0x30fe
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x3508
+  __TEXT.__unwind_info: 0x3558
   __TEXT.__eh_frame: 0x378
   __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__got: 0x928
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xda48
-  __DATA_CONST.__cfstring: 0xa7e0
-  __DATA_CONST.__objc_classlist: 0x6d8
+  __DATA_CONST.__const: 0xdb18
+  __DATA_CONST.__cfstring: 0xa880
+  __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19fa0
-  __DATA.__objc_selrefs: 0x6740
+  __DATA.__objc_const: 0x1a058
+  __DATA.__objc_selrefs: 0x6800
   __DATA.__objc_ivar: 0x10cc
-  __DATA.__objc_data: 0x44f0
-  __DATA.__data: 0x2558
-  __DATA.__bss: 0x800
+  __DATA.__objc_data: 0x4540
+  __DATA.__data: 0x24c0
+  __DATA.__bss: 0x810
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E2A6DD39-D455-3BAF-9AD9-44D63356DF94
-  Functions: 6012
-  Symbols:   645
-  CStrings:  9855
+  UUID: D4D8B401-53F4-3605-BDCB-CB49B6897FF2
+  Functions: 6045
+  Symbols:   647
+  CStrings:  9916
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
CStrings:
+ "%s: Cleared a CFU"
+ "%s: Requested a CFU"
+ "%s: Timed out"
+ "-[FMDFMIPXPCServer clearTheftAndLossCFUWithReply:]"
+ "-[FMDFMIPXPCServer requestTheftAndLossCFUWithReply:]"
+ "-[FMDSharedConfigurationManager clearTheftAndLossCFU]"
+ "-[FMDSharedConfigurationManager clearTheftAndLossCFU]_block_invoke_3"
+ "-[FMDSharedConfigurationManager requestTheftAndLossCFU]"
+ "-[FMDSharedConfigurationManager requestTheftAndLossCFU]_block_invoke_3"
+ "Application Support"
+ "Calling process is missing container entitlements"
+ "FMDCoreFollowUpManager"
+ "Failed to clear the Theft and Loss CFU with error: %@"
+ "Failed to create container directories"
+ "Failed to queue up the Theft and Loss CFU with error: %@"
+ "Failed to read contents with error: %@"
+ "Failed to remove file (%@) with error %@."
+ "Failed to write the timestamp to %@ with error %@."
+ "Invalid URL (%@) for the timestamp file."
+ "Library"
+ "No contents"
+ "No record of the last sign out. Bailing."
+ "Removed (%@)."
+ "SignOutTimestamp"
+ "T@\"FMDCoreFollowUpManager\",R,N"
+ "Unhandled Theft and Loss context: %lu"
+ "Wrote (%@) to (%@)."
+ "clearFindMySignOutTimeFile"
+ "clearTheftAndLossCFU"
+ "clearTheftAndLossCFU:"
+ "clearTheftAndLossCFUWithReply:"
+ "com.apple.findmy.theftandlosscfu"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "fileExistsAtPath:isDirectory:"
+ "fm_dictionaryWithContentsOfURL:error:"
+ "forceDownloadWithReply completed with error: %@"
+ "forceDownloadWithReply:"
+ "group.com.apple.icloud.findmydevice.followup"
+ "readFindMySignOutTimeFromFile"
+ "registerForTaskWithIdentifier failed"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "requestTheftAndLossCFU"
+ "requestTheftAndLossCFU:"
+ "requestTheftAndLossCFUWithReply:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "signOutTimestampFileURL"
+ "submitTaskRequest for %@ failed with error (%@)"
+ "submitTaskRequest:error:"
+ "submitted task %@"
+ "taskRequestForIdentifier:"
+ "theftandloss.plist"
+ "v16@?0@\"BGSystemTask\"8"
+ "writeFindMySignOutTimeToFile"
+ "writeToURL:error:"
- "doNotUseDefaultConfigs"
- "not using default configs"
- "using default configs"

```

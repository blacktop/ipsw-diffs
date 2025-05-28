## softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

-732.0.3.0.0
-  __TEXT.__text: 0x52928
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0xc460
-  __TEXT.__objc_methlist: 0x3e60
-  __TEXT.__objc_methname: 0xd1db
-  __TEXT.__cstring: 0xc6c2
+746.40.12.0.0
+  __TEXT.__text: 0x53b4c
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_stubs: 0xc640
+  __TEXT.__objc_methlist: 0x3ea0
+  __TEXT.__objc_methname: 0xd35f
+  __TEXT.__cstring: 0xcbd8
   __TEXT.__objc_classname: 0x57b
-  __TEXT.__objc_methtype: 0x1ff4
+  __TEXT.__objc_methtype: 0x204f
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x4fc
+  __TEXT.__gcc_except_tab: 0x534
   __TEXT.__oslogstring: 0x782
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1788
-  __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x1da0
-  __DATA_CONST.__cfstring: 0x7560
+  __TEXT.__unwind_info: 0x17d0
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__const: 0x1dc8
+  __DATA_CONST.__cfstring: 0x7860
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x9990
-  __DATA.__objc_selrefs: 0x3688
+  __DATA.__objc_const: 0x99d0
+  __DATA.__objc_selrefs: 0x3710
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x4d8
   __DATA.__objc_superrefs: 0x118

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2017
-  Symbols:   433
-  CStrings:  3678
+  Functions: 2031
+  Symbols:   435
+  CStrings:  3730
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _XPC_ACTIVITY_RANDOM_INITIAL_DELAY
+ _xpc_dictionary_set_uint64
- _kCDSleepAutoSuSuEndKey
CStrings:
+ "%s: %@, deleteKeepAlive: %@"
+ "%s: Current free space without purging: %llu"
+ "%s: Found SUCoreDescriptor: %@"
+ "%s: Needed bytes: %llu"
+ "%s: Old installationSize: %llu"
+ "%s: Post CacheDelete neededBytes: %llu; amountPurgeable: %llu"
+ "%s: Refreshed installationSize: %llu"
+ "%s: [DEFAULTS] space purge failed"
+ "%s: [DEFAULTS] space purge succeeded"
+ "%s: [DEFAULTS] spacePurgeTime set, sleeping %d secs"
+ "%s: canceling %@"
+ "%s: haveEnoughSpace: %@"
+ "+[SUSpace makeRoomForUpdate:completion:]"
+ "-[SUDDMManager _handleScanResults:]"
+ "-[SUDDMManager _handleScanResults:]_block_invoke"
+ "-[SUDDMManager scanRequestDidFinishForOptions:results:error:]"
+ "-[SUDownloader _downloadFinished:]"
+ "-[SUManagerServer currentAutoInstallOperationForecast:]_block_invoke"
+ "-[SUManagerServer newOSDetected:deleteKeepAlive:]"
+ "B24@?0@\"SUCoreDDMDeclaration\"8@\"SUDescriptor\"16"
+ "Current declaration is good, nothing to do here"
+ "No declarations available, nothing to do here"
+ "No descriptors available"
+ "No update found for DDM declaration %@ with error %@"
+ "Nothing relevant found..."
+ "Overriding suEndDate with time interval: %f : %@"
+ "Overriding suStartDate with time interval: %f : %@"
+ "Overriding unlockEndDate with time interval: %f : %@"
+ "Overriding unlockStartDate with time interval: %f : %@"
+ "SU_MDM_CONFLICTS_WITH_DDM_ERROR"
+ "Scan failed with error %@"
+ "Scan found an update and a previously prepared update is present"
+ "Scan found an update and no previously prepared update present"
+ "Scan found preferred descriptor {%@} and alternate descriptor {%@}\nwith error %@\nfor scan options %@"
+ "Scan triggered by ddm, nothing to do here"
+ "The last scan error %@ is fatal, notifying the status channel."
+ "Update found for declaration: %@ [%p], %@"
+ "_handleScanResults:"
+ "_isForecastExpired"
+ "_nonFatalScanError:"
+ "_queue_canGetAutoInstallOperation"
+ "cancelInstallAlertRegistrationButKeepAlive"
+ "clearing autoInstallOperation for reason: %@, destroying keybag stash: %@"
+ "com.apple.SoftwareUpdateServices.followup.InsufficientDiskSpace"
+ "components:fromDate:"
+ "copyAutoInstallOperationForecast:error:"
+ "currentAutoInstallOperationForecast:"
+ "dateFromComponents:"
+ "destroying keybag stash %@"
+ "failed"
+ "isPromoted"
+ "newOSDetected:deleteKeepAlive:"
+ "refreshInstallationSize"
+ "setHour:"
+ "setMinute:"
+ "setPromoted:"
+ "setSecond:"
+ "spacePurgeTime"
+ "suStartDate = %@, suEndDate = %@"
+ "succeeded"
+ "v24@0:8@?<v@?@\"SUAutoInstallForecast\"@\"NSError\">16"
+ "v28@0:8@\"NSString\"16B24"
+ "v32@0:8^@16^@24"
- "Current free space without purging: %llu"
- "Duet failed to return kCDSleepAutoSuSuEndKey"
- "Duet failed to return kCDSleepAutoSuSuStartKey"
- "No update found for DDM declaration %@"
- "Overriding sustart date with time interval: %f : %@"
- "Padding SU auto install expiration date to %@"
- "Scan found a update and a previously prepared update is present"
- "Scan found a update and no previously prepared update present"
- "_CDSleepForAutoSu returned default values. Adding randomized delay of %d minutes %d seconds"
- "clearing autoInstallOperation for reason: %@"
- "su end date has already passed"

```

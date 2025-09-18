## assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

-3301.21.2.1.2
-  __TEXT.__text: 0x982c
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x5c0
+3302.23.5.1.1
+  __TEXT.__text: 0x9d88
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0x610
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x14a1
-  __TEXT.__oslogstring: 0xd39
-  __TEXT.__objc_methname: 0x188c
-  __TEXT.__objc_classname: 0x1e8
-  __TEXT.__objc_methtype: 0x7ee
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x538
+  __TEXT.__cstring: 0x14fd
+  __TEXT.__oslogstring: 0xdab
+  __TEXT.__objc_methname: 0x19f8
+  __TEXT.__objc_classname: 0x20b
+  __TEXT.__objc_methtype: 0x8ab
+  __TEXT.__unwind_info: 0x2dc
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x580
   __DATA_CONST.__cfstring: 0x340
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x17a0
-  __DATA.__objc_selrefs: 0x628
+  __DATA.__objc_const: 0x19b8
+  __DATA.__objc_selrefs: 0x668
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x94
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x608
-  __DATA.__bss: 0x70
+  __DATA.__objc_classrefs: 0x100
+  __DATA.__objc_superrefs: 0x50
+  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x668
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D10952E9-2276-35D8-AED7-B1ED719CD9EA
-  Functions: 183
-  Symbols:   131
-  CStrings:  608
+  UUID: D58FC8A5-7537-3C60-AF96-DF15BEBA38B2
+  Functions: 193
+  Symbols:   139
+  CStrings:  637
 
Symbols:
+ _AFMachAbsoluteTimeGetMilliseconds
+ _HMAssistantSyncDataGeneratedNotification
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
+ _kAssistantDarwinNotificationSpeechCaptureFinished
+ _mach_absolute_time
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _strcmp
CStrings:
+ "%s Homemanager cache update took %llu milliseconds"
+ "%s Started initialization of homemanager with configuration %@"
+ "-[HomeKitStore homeManagerDidUpdateHomes:]_block_invoke"
+ "-[HomeKitStore init]"
+ "@\"HMHomeManager\""
+ "ASHomeKitStore"
+ "HMHomeManagerDelegate"
+ "HomeKitStore"
+ "defaultPrivateConfiguration"
+ "fetchStartTime"
+ "homeManager"
+ "homeManager:didAddHome:"
+ "homeManager:didReceiveAddAccessoryRequest:"
+ "homeManager:didRemoveHome:"
+ "homeManager:didUpdateAuthorizationStatus:"
+ "homeManagerDidUpdateHomes:"
+ "homeManagerDidUpdatePrimaryHome:"
+ "initWithConfiguration:"
+ "isSyncDisabledForFullUoDDevices"
+ "refreshCache"
+ "setCachePolicy:"
+ "setOptions:"
+ "sharedInstance"
+ "v24@0:8@\"HMHomeManager\"16"
+ "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
+ "v32@0:8@\"HMHomeManager\"16Q24"
+ "v32@0:8@16@24"
+ "v32@0:8@16Q24"

```

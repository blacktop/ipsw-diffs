## ManagedConfigurationUEA

> `/System/Library/UserEventPlugins/ManagedConfigurationUEA.plugin/ManagedConfigurationUEA`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0xce0
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x280
-  __TEXT.__objc_methlist: 0x36c
+2420.1.1.0.0
+  __TEXT.__text: 0xf64
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x7f
-  __TEXT.__objc_methname: 0x7f4
+  __TEXT.__cstring: 0xa3
+  __TEXT.__objc_methname: 0xa2b
   __TEXT.__oslogstring: 0x1e3
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methtype: 0x581
-  __TEXT.__unwind_info: 0xa0
-  __DATA.__auth_got: 0x148
-  __DATA.__got: 0x68
+  __TEXT.__objc_classname: 0x96
+  __TEXT.__objc_methtype: 0x5a6
+  __TEXT.__unwind_info: 0xb8
+  __DATA.__auth_got: 0x150
+  __DATA.__got: 0x70
   __DATA.__const: 0x20
-  __DATA.__cfstring: 0x120
+  __DATA.__cfstring: 0x140
   __DATA.__objc_classlist: 0x8
+  __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x20
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3b8
-  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_const: 0x470
+  __DATA.__objc_selrefs: 0x308
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D23B243-FADF-35AE-8AFB-1C766A33C09D
-  Functions: 17
-  Symbols:   63
-  CStrings:  174
+  UUID: 7B9D17E2-BED9-30D6-8127-16688E14BED4
+  Functions: 24
+  Symbols:   67
+  CStrings:  201
 
Symbols:
+ OBJC_IVAR_$_MCUEAPlugin._userActivityHandle
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _dispatch_get_global_queue
CStrings:
+ "!"
+ "@24@0:8d16"
+ "B24@0:8@?16"
+ "B24@0:8^@16"
+ "DMCSystemTasks"
+ "Q"
+ "T@\"NSString\",R,N"
+ "_userActivityHandle"
+ "cancelReturnToServiceTaskRequestWithError:"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.managedconfiguration.rrts"
+ "dealloc"
+ "deregisterRapidReturnToService"
+ "deregisterTaskWithIdentifier:"
+ "initWithIdentifier:"
+ "rapidReturnToServiceTaskIdentifier"
+ "rapidReturnToServiceTaskRequest"
+ "rapidReturnToServiceTaskRequestWithTimeout:"
+ "registerForRapidReturnToServiceWithLaunchHandler:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresUserInactivity:"
+ "setScheduleAfter:"
+ "taskRequestForIdentifier:"

```

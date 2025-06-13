## softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

-746.40.12.0.0
-  __TEXT.__text: 0x53b4c
+746.60.8.0.0
+  __TEXT.__text: 0x5415c
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0xc640
-  __TEXT.__objc_methlist: 0x3ea0
-  __TEXT.__objc_methname: 0xd35f
-  __TEXT.__cstring: 0xcbd8
+  __TEXT.__objc_stubs: 0xc6e0
+  __TEXT.__objc_methlist: 0x3ed8
+  __TEXT.__objc_methname: 0xd3e1
+  __TEXT.__cstring: 0xcd0c
   __TEXT.__objc_classname: 0x57b
   __TEXT.__objc_methtype: 0x204f
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x534
-  __TEXT.__oslogstring: 0x782
+  __TEXT.__oslogstring: 0x86d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x17d0
+  __TEXT.__unwind_info: 0x17d8
   __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x1dc8
-  __DATA_CONST.__cfstring: 0x7860
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x1da0
+  __DATA_CONST.__cfstring: 0x7920
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x99d0
-  __DATA.__objc_selrefs: 0x3710
+  __DATA.__objc_const: 0x99f0
+  __DATA.__objc_selrefs: 0x3738
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x4d8
   __DATA.__objc_superrefs: 0x118

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 53FFE40E-2CB0-3BAF-B06B-67F457A0030C
-  Functions: 2031
-  Symbols:   435
-  CStrings:  4693
+  UUID: C6E5695A-22ED-38C1-A49F-B7D1032EC820
+  Functions: 2036
+  Symbols:   437
+  CStrings:  4716
 
Symbols:
+ _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
+ _kSUCoreControllerEventOTAAutoTriggered
CStrings:
+ "%@ Checking if engine parameter is brain error that should be retried, %@"
+ "%@ Engine parameter is brain retry error"
+ "%@ engine error parameter does not have a brain should retry failure code"
+ "%@ engine error parameter is not in SU domain"
+ "%s: disableAutoInstallJitter default is set, ignoring jitter"
+ "-[SUAutoInstallManager noteAutoInstallOperationWantsToBegin]"
+ "-[SUAutoInstallManager trySchedulingAutoInstallAgainLater]"
+ "Attempted to defer autoInstallStart activity but failed."
+ "Could not install due to %@."
+ "LoadTrustCachePurgedBrain"
+ "Will retry to auto install in %d seconds"
+ "Window ends on %@; cannot reschedule auto install on %@"
+ "[Auto Install Jitter] Starting auto installation in %d seconds"
+ "autoInstallRetryDelay"
+ "defaultDelay = %@"
+ "delay is set to %d seconds by default"
+ "disableAutoInstallJitter"
+ "isBrainReloadError:"
+ "reportOTAAutoTriggeredEvent"
+ "trySchedulingAutoInstallAgainLater"
- "Attempted to defer autoInstallStart activity but failed. Rescheduling for 15 minutes from now"
- "Could not install due to %@, retrying in 15 mins."
- "Install Update Failed on AutoSU. Going to schedule retry"

```

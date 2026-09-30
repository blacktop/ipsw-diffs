## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1218.40.23.0.1
-  __TEXT.__text: 0x1ccc00
-  __TEXT.__auth_stubs: 0x26e0
-  __TEXT.__objc_stubs: 0x1a760
-  __TEXT.__objc_methlist: 0x11d40
-  __TEXT.__cstring: 0xf635
-  __TEXT.__objc_classname: 0x2b37
-  __TEXT.__objc_methname: 0x200fa
-  __TEXT.__objc_methtype: 0x6b9a
-  __TEXT.__const: 0x31a8
-  __TEXT.__gcc_except_tab: 0x4a20
-  __TEXT.__oslogstring: 0x1002d
-  __TEXT.__dlopen_cstrs: 0x56
+1218.40.31.0.0
+  __TEXT.__text: 0x1cc550
+  __TEXT.__auth_stubs: 0x26a0
+  __TEXT.__objc_stubs: 0x1a7c0
+  __TEXT.__objc_methlist: 0x11d70
+  __TEXT.__cstring: 0xf5d8
+  __TEXT.__objc_classname: 0x2b5f
+  __TEXT.__objc_methname: 0x2017c
+  __TEXT.__objc_methtype: 0x6bb7
+  __TEXT.__const: 0x3198
+  __TEXT.__gcc_except_tab: 0x499c
+  __TEXT.__oslogstring: 0x10065
   __TEXT.__swift5_typeref: 0xe34
   __TEXT.__swift5_capture: 0x7e0
   __TEXT.__constg_swiftt: 0x1290

   __TEXT.__swift5_proto: 0x168
   __TEXT.__swift5_types: 0xd8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6c58
-  __TEXT.__eh_frame: 0x10f0
-  __DATA_CONST.__auth_got: 0x1380
-  __DATA_CONST.__got: 0xd30
+  __TEXT.__unwind_info: 0x6c08
+  __TEXT.__eh_frame: 0x1128
+  __DATA_CONST.__auth_got: 0x1360
+  __DATA_CONST.__got: 0xd58
   __DATA_CONST.__auth_ptr: 0x370
-  __DATA_CONST.__const: 0x12948
-  __DATA_CONST.__cfstring: 0xd3e0
-  __DATA_CONST.__objc_classlist: 0xb88
+  __DATA_CONST.__const: 0x12908
+  __DATA_CONST.__cfstring: 0xd420
+  __DATA_CONST.__objc_classlist: 0xb90
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x330
+  __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x6c8

   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0x2d658
-  __DATA.__objc_selrefs: 0x7aa0
-  __DATA.__objc_ivar: 0x100c
-  __DATA.__objc_data: 0x8128
-  __DATA.__data: 0x6178
+  __DATA.__objc_const: 0x2da90
+  __DATA.__objc_selrefs: 0x7ab8
+  __DATA.__objc_ivar: 0x1010
+  __DATA.__objc_data: 0x8178
+  __DATA.__data: 0x61d8
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x3888
+  __DATA.__bss: 0x3858
   __DATA.__common: 0x298
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10257
-  Symbols:   1166
-  CStrings:  10728
+  Functions: 10240
+  Symbols:   1167
+  CStrings:  10730
 
Symbols:
+ _FLGroupIdentifierAccount
+ _OBJC_CLASS_$_FLFollowUpNotification
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_FLFollowUpItem
+ _OBJC_CLASS_$_FLFollowUpAction
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
CStrings:
+ "_rebootTracker"
+ "Device has rebooted since last initializing, fetching CK records"
+ "\x0f\x05\x1b"
+ "KTRebootTracker"
+ "@\"<KTRebootTrackerProtocol>\""
+ "rebootTracker"
+ "T@\"<KTRebootTrackerProtocol>\",&,V_rebootTracker"
+ "lastRebootTime"
+ "getLastRebootTime"
+ "noCloudKitAccount"
+ "urisNeedOptInApplication:error:"
+ "setRebootTracker:"
+ "Unable to find trusted key for SPKI hash: %!{(MISSING)public}@"
+ "KTRebootTrackerProtocol"
+ "evaluateCloudDataWithApplication:error:"
+ "process-incoming"
+ "evaluateLogDataWithApplication:error:"
- "%!s(MISSING)"
- "FLFollowUpNotification"
- "urisNeedOptInAndReturnError:"
- "\x0f\x05\x1a"
- "evaluateCloudDataAndReturnError:"
- "CoreFollowUp is not available"
- "evaluateLogDataAndReturnError:"
- "FLGroupIdentifierAccount"
- "FLFollowUpAction"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp"
- "fetch-triggered"
- "Unable to find class %!s(MISSING)"
- "FLFollowUpController"
- "FLFollowUpItem"

```

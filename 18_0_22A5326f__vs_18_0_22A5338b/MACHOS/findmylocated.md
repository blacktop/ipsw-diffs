## findmylocated

> `/usr/libexec/findmylocated`

```diff

-93.30.6.4.10
-  __TEXT.__text: 0x28da74
-  __TEXT.__auth_stubs: 0x3530
+93.30.6.4.14
+  __TEXT.__text: 0x293030
+  __TEXT.__auth_stubs: 0x3540
   __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x9492
-  __TEXT.__cstring: 0x5f6f
-  __TEXT.__swift5_typeref: 0x2eec
-  __TEXT.__swift5_reflstr: 0x3145
+  __TEXT.__const: 0x9442
+  __TEXT.__cstring: 0x5fff
+  __TEXT.__swift5_typeref: 0x2f0c
+  __TEXT.__swift5_reflstr: 0x3165
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__constg_swiftt: 0x2bf4
+  __TEXT.__constg_swiftt: 0x2c18
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_fieldmd: 0x3ad0
-  __TEXT.__swift5_proto: 0x994
+  __TEXT.__swift5_fieldmd: 0x3adc
+  __TEXT.__swift5_proto: 0x990
   __TEXT.__swift5_types: 0x2bc
   __TEXT.__objc_methname: 0x1423
   __TEXT.__objc_classname: 0x75
   __TEXT.__objc_methtype: 0x400
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__oslogstring: 0xa90b
-  __TEXT.__swift5_capture: 0x1b50
+  __TEXT.__oslogstring: 0xaaab
+  __TEXT.__swift5_capture: 0x1bc8
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__info_plist: 0x54b
-  __TEXT.__unwind_info: 0xac98
-  __TEXT.__eh_frame: 0x233b4
-  __DATA_CONST.__auth_got: 0x1a98
-  __DATA_CONST.__got: 0xf70
-  __DATA_CONST.__auth_ptr: 0xf40
-  __DATA_CONST.__const: 0x7920
+  __TEXT.__info_plist: 0x541
+  __TEXT.__unwind_info: 0xae48
+  __TEXT.__eh_frame: 0x23ac4
+  __DATA_CONST.__auth_got: 0x1aa0
+  __DATA_CONST.__got: 0xf88
+  __DATA_CONST.__auth_ptr: 0xf80
+  __DATA_CONST.__const: 0x7978
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x2b50
+  __DATA.__objc_const: 0x2b70
   __DATA.__objc_selrefs: 0x500
   __DATA.__objc_data: 0x7b0
-  __DATA.__data: 0x86b8
-  __DATA.__bss: 0x12a00
-  __DATA.__common: 0xb28
+  __DATA.__data: 0x87b8
+  __DATA.__bss: 0x12980
+  __DATA.__common: 0xb30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8091
-  Symbols:   1640
-  CStrings:  1676
+  Functions: 8151
+  Symbols:   1644
+  CStrings:  1687
 
Symbols:
+ _$s10FindMyBase10SystemInfoO0aB13DaemonSupportE15DeviceLockStateO17beforeFirstUnlockyA2FmFWC
+ _$s10FindMyBase10SystemInfoO0aB13DaemonSupportE15DeviceLockStateOSQADMc
+ _$s10FindMyBase13WorkItemQueueC21enqueueAndAwaitResultyyyyYaYbKcYaKFTjTu
+ _swift_initEnumMetadataSinglePayload
CStrings:
+ "%!{(MISSING)public}s APNS has already been set up"
+ "%!{(MISSING)public}s Account is nil!"
+ "%!{(MISSING)public}s Checking if settings from DB is nil"
+ "%!{(MISSING)public}s Generating a new key..."
+ "%!{(MISSING)public}s Not starting up before first unlock!"
+ "%!{(MISSING)public}s failed due to %!{(MISSING)public}@"
+ "%!{(MISSING)public}s failed to setup APNS account %!{(MISSING)public}@"
+ "%!{(MISSING)public}s isInitialized:%!{(MISSING)bool}d"
+ ".available(account: "
+ "APNS message: %!s(MISSING)."
+ "Daemon has already initialized, updating DataManager state so we can respond to incoming requests"
+ "Did receive APNS public token: %!{(MISSING)private,mask.hash}s"
+ "Init client failed due to %!{(MISSING)public}@"
+ "Unable to decode APNS message due to %!{(MISSING)public}@"
+ "Unable to update account info due to %!{(MISSING)public}@"
+ "didSetupAPNSAccount"
+ "monitorAccountState()"
+ "refreshClientWithThrottle(timestamp:)"
+ "setupAPNS(account:)"
- "%!{(MISSING)public}s Unable to retrieve DataManager!"
- ".missingCentralManager"
- "APS message: %!s(MISSING)."
- "Did receive APS public token: %!{(MISSING)private,mask.hash}s"
- "Init client failed due to %!{(MISSING)public}s"
- "Unable to decode APS message due to %!{(MISSING)public}s"
- "Unable to update account info due to %!{(MISSING)public}s"
- "refreshClientWithThrottle"

```

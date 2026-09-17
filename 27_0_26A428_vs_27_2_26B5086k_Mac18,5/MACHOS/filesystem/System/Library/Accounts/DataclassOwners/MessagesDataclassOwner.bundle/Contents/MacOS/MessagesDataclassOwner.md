## MessagesDataclassOwner

> `/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/Contents/MacOS/MessagesDataclassOwner`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x22a0
-  __TEXT.__auth_stubs: 0x1a0
+1491.200.63.0.0
+  __TEXT.__text: 0x2324
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x2e8
   __TEXT.__cstring: 0x131
-  __TEXT.__oslogstring: 0x79f
-  __TEXT.__objc_methname: 0x821
+  __TEXT.__oslogstring: 0x7f0
+  __TEXT.__objc_methname: 0x82c
   __TEXT.__objc_classname: 0x3a
   __TEXT.__objc_methtype: 0x23e
   __TEXT.__unwind_info: 0x158

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0xc0
   __DATA.__objc_const: 0x280
   __DATA.__objc_selrefs: 0x280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 31
-  Symbols:   58
+  Symbols:   59
   CStrings:  170
 
Symbols:
+ _IMCloudKitCanToggleMiCSwitchWithBroadcastState
Functions:
~ sub_1cc4 : 896 -> 856
~ sub_20a4 -> sub_207c : 604 -> 696
~ sub_2518 -> sub_254c : 620 -> 680
~ sub_2784 -> sub_27f4 : 280 -> 300
CStrings:
+ "Asking imagent to set Messages in iCloud enabled: %d (our local view of enablement is %d)"
+ "Not eligible as account does not support DeviceToDeviceEncryption"
+ "Signal eligible_semaphore, canToggleMiCSwitch: %@"
+ "Timeout eligible_semaphore; letting the request through for imagent to judge"
+ "Timeout enable_semaphore; accepting the request and leaving the switch for imagent to reconcile"
+ "removeObserver:name:object:"
- "Not eligible as account does not support DeviceToDeviceEncryption, or iCloud & iMsg accounts do not match up"
- "Signal eligible_semaphore, isEligible: %@"
- "Timeout eligible_semaphore, isEligible: %@"
- "Timeout enable_semaphore, didSucceed: %d"
- "mocAccountsMatch"
- "setCloudEnable: Did nothing as it was already enabled/disabled"
```

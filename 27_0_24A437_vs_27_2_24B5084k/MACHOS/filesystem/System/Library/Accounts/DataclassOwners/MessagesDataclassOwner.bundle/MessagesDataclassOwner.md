## MessagesDataclassOwner

> `/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/MessagesDataclassOwner`

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

-1491.100.1.2.25
-  __TEXT.__text: 0x20a8
-  __TEXT.__auth_stubs: 0x290
+1491.200.63.2.1
+  __TEXT.__text: 0x211c
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x600
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x2e4
   __TEXT.__cstring: 0x124
-  __TEXT.__oslogstring: 0x79f
-  __TEXT.__objc_methname: 0x84a
+  __TEXT.__oslogstring: 0x7f0
+  __TEXT.__objc_methname: 0x855
   __TEXT.__objc_classname: 0x3a
   __TEXT.__objc_methtype: 0x23e
   __TEXT.__unwind_info: 0x148

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0x280
   __DATA.__objc_selrefs: 0x290

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 27
-  Symbols:   74
+  Symbols:   75
   CStrings:  171
 
Symbols:
+ _IMCloudKitCanToggleMiCSwitchWithBroadcastState
Functions:
~ sub_1bd0 : 864 -> 828
~ sub_1f8c -> sub_1f68 : 580 -> 664
~ sub_23d4 -> sub_2404 : 600 -> 652
~ sub_262c -> sub_2690 : 264 -> 280
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

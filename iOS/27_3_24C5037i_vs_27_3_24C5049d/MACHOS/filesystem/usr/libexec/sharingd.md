## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2131.30.43.2.1
-  __TEXT.__text: 0x681958
-  __TEXT.__auth_stubs: 0xb240
-  __TEXT.__objc_stubs: 0x37a20
-  __TEXT.__objc_methlist: 0x1e7ac
-  __TEXT.__cstring: 0x3f651
-  __TEXT.__objc_methname: 0x4f1b5
+2131.30.65.0.0
+  __TEXT.__text: 0x683188
+  __TEXT.__auth_stubs: 0xb280
+  __TEXT.__objc_stubs: 0x37aa0
+  __TEXT.__objc_methlist: 0x1e7ec
+  __TEXT.__cstring: 0x3f761
+  __TEXT.__objc_methname: 0x4f285
   __TEXT.__objc_classname: 0x5b57
   __TEXT.__objc_methtype: 0xbcd2
-  __TEXT.__const: 0x16108
-  __TEXT.__gcc_except_tab: 0x68e0
-  __TEXT.__oslogstring: 0x3deb8
+  __TEXT.__const: 0x160f8
+  __TEXT.__gcc_except_tab: 0x68ec
+  __TEXT.__oslogstring: 0x3e0b8
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__swift5_typeref: 0x81c0

   __TEXT.__swift5_types: 0x5fc
   __TEXT.__swift_as_entry: 0xe68
   __TEXT.__swift_as_cont: 0x2240
-  __TEXT.__swift5_capture: 0x52dc
+  __TEXT.__swift5_capture: 0x52ec
   __TEXT.__swift_as_ret: 0xf88
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x19d68
-  __TEXT.__eh_frame: 0x25a74
-  __DATA_CONST.__const: 0x1cf78
-  __DATA_CONST.__cfstring: 0x19960
+  __TEXT.__unwind_info: 0x19d70
+  __TEXT.__eh_frame: 0x25a84
+  __DATA_CONST.__const: 0x1cfa0
+  __DATA_CONST.__cfstring: 0x19a00
   __DATA_CONST.__objc_classlist: 0xe20
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x748

   __DATA_CONST.__objc_dictobj: 0x1720
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x5930
-  __DATA_CONST.__got: 0x3b78
+  __DATA_CONST.__auth_got: 0x5950
+  __DATA_CONST.__got: 0x3b88
   __DATA_CONST.__auth_ptr: 0x4488
-  __DATA.__objc_const: 0x389d8
-  __DATA.__objc_selrefs: 0x11200
-  __DATA.__objc_ivar: 0x2960
+  __DATA.__objc_const: 0x38a08
+  __DATA.__objc_selrefs: 0x11228
+  __DATA.__objc_ivar: 0x2964
   __DATA.__objc_data: 0xa3b8
-  __DATA.__data: 0x14b38
+  __DATA.__data: 0x14b48
   __DATA.__common: 0x980
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26535
-  Symbols:   5090
-  CStrings:  27717
+  Functions: 26543
+  Symbols:   5096
+  CStrings:  27738
 
Symbols:
+ _$s7Sharing30CancellableCheckedContinuationC6resume8throwingys5Error_p_tF
+ _$s7Sharing30CancellableCheckedContinuationC8onCancelyyyyYbcF
+ _$s7Sharing30CancellableCheckedContinuationCAAytRszlE6resumeyyF
+ _$s7Sharing34withCancellableCheckedContinuation8function_xSS_yAA0cdE0CyxGYbctYaKlF
+ _$s7Sharing34withCancellableCheckedContinuation8function_xSS_yAA0cdE0CyxGYbctYaKlFTu
+ _OBJC_CLASS_$_CPSClipURL
CStrings:
+ "App Clips unsupported, skipping AppClip request for %s"
+ "AutoUnlockUpsellStateFromNonFaceIDDevice"
+ "Clearing upsell. HasPasscode:%@, HasCapableWatch:%@, FaceIDEnabled:%@, BlockedByManagement:%@, DeviceSupportsAutoUnlock:%@, AlreadyEnabled:%@"
+ "Client error retry skipped, %@ not in medium bubble or state not medium/close (%d)\n"
+ "Could not create biometric device for descriptor %@: %@"
+ "Could not force bio lockout for %@: %@"
+ "Detected bio lockout, but token still armed. Must be accidental biolockout."
+ "Face ID proxy device, not requiring a mask detection for upsell"
+ "FindMyProxyOptedIn"
+ "Skipping upsell. HasPasscode:%@, FaceIDEnabled:%@, SFDeviceSupportsAutoUnlock:%@, SDAutoUnlockDisallowedDueToManagement:%@"
+ "T@\"NSArray\",R,C,N,V_biometricDevices"
+ "UNLOCK_PHONE_FOLLOWUP_ACTION"
+ "UNLOCK_PHONE_FOLLOWUP_BODY"
+ "UNLOCK_PHONE_FOLLOWUP_TITLE"
+ "UNLOCK_PHONE_UPSELL_BODY_DUO"
+ "Upsell state was not written by a non-Face ID phone, resetting upsell defaults"
+ "_biometricDevices"
+ "biometricDevices"
+ "clearUpsellNotificationIfNoLongerEligible"
+ "handleAppClip(url:)"
+ "hasAnyPhoneAutoUnlockCapableWatch"
+ "recordUpsellStateDevice"
+ "resetUpsellStateIfFromFaceIDDevice"
- "Could not force bio lockout"
- "Skipping upsell. FaceIDEnabled:%@, SFDeviceSupportsAutoUnlock:%@, SDAutoUnlockDisallowedDueToManagement:%@"
```

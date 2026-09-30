## findmylocated

> `/usr/libexec/findmylocated`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-141.31.6.16.16
-  __TEXT.__text: 0x548c30
-  __TEXT.__auth_stubs: 0x5d10
+141.31.6.16.17
+  __TEXT.__text: 0x552c94
+  __TEXT.__auth_stubs: 0x5d30
   __TEXT.__objc_stubs: 0x2000
   __TEXT.__objc_methlist: 0xf4c
-  __TEXT.__const: 0x20378
-  __TEXT.__cstring: 0xb9f2
-  __TEXT.__swift5_typeref: 0x7124
-  __TEXT.__constg_swiftt: 0x70a0
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x7dad
-  __TEXT.__swift5_fieldmd: 0x8fa8
+  __TEXT.__const: 0x20648
+  __TEXT.__cstring: 0xbb12
+  __TEXT.__swift5_typeref: 0x71fe
+  __TEXT.__constg_swiftt: 0x717c
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0x7e7d
+  __TEXT.__swift5_fieldmd: 0x90ac
   __TEXT.__swift5_assocty: 0x958
-  __TEXT.__swift5_proto: 0x1780
-  __TEXT.__swift5_types: 0x7e4
+  __TEXT.__swift5_proto: 0x1784
+  __TEXT.__swift5_types: 0x7f8
   __TEXT.__objc_classname: 0x12a6
-  __TEXT.__objc_methname: 0x4ee5
+  __TEXT.__objc_methname: 0x4f25
   __TEXT.__objc_methtype: 0x11e8
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__oslogstring: 0x192ec
-  __TEXT.__swift_as_entry: 0x16e8
-  __TEXT.__swift_as_ret: 0x2898
-  __TEXT.__swift_as_cont: 0x4480
-  __TEXT.__swift5_capture: 0x4db8
+  __TEXT.__swift5_mpenum: 0x50
+  __TEXT.__oslogstring: 0x194ac
+  __TEXT.__swift_as_entry: 0x1720
+  __TEXT.__swift_as_ret: 0x290c
+  __TEXT.__swift_as_cont: 0x4508
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x17c60
-  __TEXT.__eh_frame: 0x48ec0
-  __DATA_CONST.__const: 0x18268
+  __TEXT.__swift5_capture: 0x4e5c
+  __TEXT.__unwind_info: 0x187d0
+  __TEXT.__eh_frame: 0x49788
+  __DATA_CONST.__const: 0x18588
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x2e90
+  __DATA_CONST.__auth_got: 0x2ea0
   __DATA_CONST.__got: 0x1da8
-  __DATA_CONST.__auth_ptr: 0x1858
-  __DATA.__objc_const: 0x6358
+  __DATA_CONST.__auth_ptr: 0x1888
+  __DATA.__objc_const: 0x6398
   __DATA.__objc_selrefs: 0xd60
   __DATA.__objc_data: 0x1430
-  __DATA.__data: 0xeea0
-  __DATA.__common: 0x13c0
+  __DATA.__data: 0xf080
+  __DATA.__common: 0x13d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17506
-  Symbols:   2827
-  CStrings:  3858
+  Functions: 17653
+  Symbols:   2830
+  CStrings:  3873
 
Symbols:
+ _$sSL2leoiySbx_xtFZTj
+ _$ss12StaticStringV11descriptionSSvg
+ _$ss12StaticStringVMn
CStrings:
+ "$__lazy_storage_$_cacheExpiryScheduler"
+ "%{public}s expired Friend:%{private,mask.hash}s\nexpiresByGroupId:%{private,mask.hash}s\nlocationSharingState:%{private,mask.hash}s"
+ "%{public}s missing XPC alarm event handler"
+ "%{public}s not eligible, since we have non-nil, non-stale serverSettings already."
+ "%{public}s: No LocalStorageService; skipping donation"
+ "Elapsed: %{public}s"
+ "Expiry alarm fired: %{public}s"
+ "Force refreshClient, since server settings are nil or stale in local DB."
+ "LabelStore: labels changed for %{public}ld users, re-donating Person Entities"
+ "No upcoming expiry; alarm cleared"
+ "Re-arming after %{public}s"
+ "Waking at %{public}s for %{public}s"
+ "_retrieveAndDonatePersonEntities(impactedUsers:)"
+ "com.apple.findmy.findmylocate.ExpiryAlarm"
+ "determineIfAnyUpdatesNeeded(previousMeDevice:previousShareMyLocationState:previousFriendshipRequestsAllowed:)"
+ "expiryAlarmDebounceTask"
+ "registerExpiryAlarmHandler()"
+ "updateLocalStorage(with:)"
- "%{public}s expired Friend:%{private,mask.hash}s\nexpiresByGroupId:%{private,mask.hash}s"
- "%{public}s not eligible, since we have non-nil serverSettings already."
- "Force refreshClient, since we have nil server settings in local DB."
```

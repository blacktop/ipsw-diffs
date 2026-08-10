## demod

> `/usr/libexec/demod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1871.0.42.0.0
-  __TEXT.__text: 0xf66fc
+1871.0.51.0.0
+  __TEXT.__text: 0xf6b40
   __TEXT.__auth_stubs: 0x2110
-  __TEXT.__objc_stubs: 0x1b6c0
+  __TEXT.__objc_stubs: 0x1b6a0
   __TEXT.__objc_methlist: 0xdb24
   __TEXT.__const: 0x530
-  __TEXT.__cstring: 0x10d22
+  __TEXT.__cstring: 0x10ed2
   __TEXT.__objc_classname: 0x188a
   __TEXT.__objc_methtype: 0x409b
-  __TEXT.__gcc_except_tab: 0x4750
-  __TEXT.__oslogstring: 0x1cc3c
-  __TEXT.__objc_methname: 0x21321
+  __TEXT.__gcc_except_tab: 0x4790
+  __TEXT.__oslogstring: 0x1cd8c
+  __TEXT.__objc_methname: 0x2130c
   __TEXT.__swift5_typeref: 0x112
   __TEXT.__swift5_capture: 0xcc
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__unwind_info: 0x3ab8
   __TEXT.__eh_frame: 0x3d0
   __DATA_CONST.__const: 0x3260
-  __DATA_CONST.__cfstring: 0xeca0
+  __DATA_CONST.__cfstring: 0xed80
   __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x418
-  __DATA_CONST.__objc_intobj: 0x4b0
+  __DATA_CONST.__objc_intobj: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x938
   __DATA_CONST.__objc_arrayobj: 0x468
   __DATA_CONST.__objc_doubleobj: 0x10

   __DATA_CONST.__got: 0xf20
   __DATA_CONST.__auth_ptr: 0x190
   __DATA.__objc_const: 0x19828
-  __DATA.__objc_selrefs: 0x8200
+  __DATA.__objc_selrefs: 0x81f8
   __DATA.__objc_ivar: 0xb38
   __DATA.__objc_data: 0x4800
   __DATA.__data: 0x29f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6088
+  Functions: 6092
   Symbols:   1056
-  CStrings:  10924
+  CStrings:  10934
 
CStrings:
+ "/var/mobile/Library/AgentSessionKitBackupStaging"
+ "/var/mobile/Library/IdentityServices/Persistence/com.apple.identityservices.dailyDeviceAddedNotificationData"
+ "/var/mobile/Library/IdentityServices/Persistence/com.apple.identityservicesd.offgrid.provisioning.store"
+ "/var/mobile/Library/IdentityServices/Persistence/com.apple.identityservicesd.waking-push-priority"
+ "Backup AgentSessionKitBackupStaging - Cannot find RelativePathsNotToBackupInMegaBackup under HomeDomain."
+ "Backup AgentSessionKitBackupStaging - Cannot find RelativePathsNotToBackupToService under HomeDomain."
+ "Backup AgentSessionKitBackupStaging - Cannot find RelativePathsToOnlyBackupEncrypted under HomeDomain."
+ "CleanHomeConfig"
+ "Library/AgentSessionKitBackupStaging"
+ "No primary home.  Carry on."
+ "com.apple.CompanionSetupKit"
- "standardUserDefaults"
```

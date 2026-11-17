## com.apple.CloudSharingUI.AddParticipants

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-240.2.4.0.0
-  __TEXT.__text: 0x9f148
+240.2.6.0.0
+  __TEXT.__text: 0x9fc3c
   __TEXT.__auth_stubs: 0x1a50
   __TEXT.__objc_stubs: 0x18e0
-  __TEXT.__objc_methlist: 0x5f0
+  __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x4550
   __TEXT.__cstring: 0x272d
-  __TEXT.__objc_methname: 0x30a9
+  __TEXT.__objc_methname: 0x3319
   __TEXT.__objc_classname: 0x39d
-  __TEXT.__objc_methtype: 0x1178
-  __TEXT.__constg_swiftt: 0xe2c
+  __TEXT.__objc_methtype: 0x1308
+  __TEXT.__constg_swiftt: 0xe44
   __TEXT.__swift5_typeref: 0x27fd
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0x12d3
   __TEXT.__swift5_fieldmd: 0x1008
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_capture: 0x1d88
-  __TEXT.__oslogstring: 0x3e93
+  __TEXT.__oslogstring: 0x3f83
   __TEXT.__swift5_proto: 0x150
   __TEXT.__swift5_types: 0xcc
   __TEXT.__swift_as_entry: 0x100

   __TEXT.__swift_as_cont: 0x484
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1d50
+  __TEXT.__unwind_info: 0x1d70
   __TEXT.__eh_frame: 0x4040
   __DATA_CONST.__const: 0x5d18
   __DATA_CONST.__cfstring: 0x20

   __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__auth_ptr: 0x6d0
-  __DATA.__objc_const: 0x1510
-  __DATA.__objc_selrefs: 0x870
+  __DATA.__objc_const: 0x1528
+  __DATA.__objc_selrefs: 0x8a0
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x5e0
+  __DATA.__objc_data: 0x5f8
   __DATA.__data: 0x1e90
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2418
+  Functions: 2428
   Symbols:   312
-  CStrings:  949
+  CStrings:  963
 
CStrings:
+ "Sending SharePrivacyChange, transition %ld, source %ld"
+ "addToCloudKitSharing:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:withReply:"
+ "callForCloudKitAddToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:reply:"
+ "callForFileSharing:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:reply:"
+ "callForForciblyShareFolder:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:reply:"
+ "changeAccessSetting: new %s, current %s, source %ld, hasCKShare %{bool}d, isOwner %{bool}d"
+ "changeAccessSetting: no owned CKShare yet, not sending SharePrivacyChange"
+ "forciblyShareFolder:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:withReply:"
+ "startFileSharingWithURLWrapper:emailAddresses:phoneNumbers:optionsGroups:privacyChangeSource:withReply:"
+ "v64@0:8@\"FPSandboxingURLWrapper\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40q48@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">56"
+ "v64@0:8@\"NSURL\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40q48@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40q48@?56"
+ "v72@0:8@\"CKShare\"16@\"CKContainerSetupInfo\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48q56@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48q56@?64"
```

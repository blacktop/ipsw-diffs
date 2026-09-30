## com.apple.CloudSharingUI.CloudSharing

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing`

```diff

-213.0.0.0.0
-  __TEXT.__text: 0xc37d4
-  __TEXT.__auth_stubs: 0x2450
+215.0.0.0.0
+  __TEXT.__text: 0xc554c
+  __TEXT.__auth_stubs: 0x2460
   __TEXT.__objc_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x1654
-  __TEXT.__const: 0xa294
+  __TEXT.__const: 0xa3c4
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x7505
-  __TEXT.__objc_methname: 0x4d20
-  __TEXT.__oslogstring: 0x2be9
+  __TEXT.__cstring: 0x7555
+  __TEXT.__objc_methname: 0x4d22
+  __TEXT.__oslogstring: 0x2f09
   __TEXT.__objc_classname: 0x351
   __TEXT.__objc_methtype: 0x1944
-  __TEXT.__swift5_typeref: 0xbfd8
-  __TEXT.__swift5_fieldmd: 0x1db4
+  __TEXT.__swift5_typeref: 0xc14c
+  __TEXT.__swift5_fieldmd: 0x1dd8
   __TEXT.__constg_swiftt: 0x1a54
-  __TEXT.__swift5_reflstr: 0x2414
+  __TEXT.__swift5_reflstr: 0x2484
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x918
   __TEXT.__swift5_capture: 0x1314

   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2a58
-  __TEXT.__eh_frame: 0x52d8
-  __DATA_CONST.__auth_got: 0x1238
-  __DATA_CONST.__got: 0xc80
+  __TEXT.__unwind_info: 0x2a98
+  __TEXT.__eh_frame: 0x5360
+  __DATA_CONST.__auth_got: 0x1240
+  __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0xee0
-  __DATA_CONST.__const: 0x5288
+  __DATA_CONST.__const: 0x5300
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x37e0
+  __DATA.__objc_const: 0x3820
   __DATA.__objc_selrefs: 0x14a8
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xee0
-  __DATA.__data: 0x49a8
-  __DATA.__bss: 0x6ba0
+  __DATA.__data: 0x49f8
+  __DATA.__bss: 0x6be0
   __DATA.__common: 0x78
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8A0B9FE2-2798-3CF1-8B44-B752FF5A535D
-  Functions: 3758
+  UUID: 69EF1AF6-587A-325D-B881-209CCA26FCAF
+  Functions: 3783
   Symbols:   384
-  CStrings:  1765
+  CStrings:  1772
 
CStrings:
+ "For Co-owners changeNewParticipantsCanBeCoOwners, newState: %s, oldState: %s"
+ "PeopleViewModel Combine3: sharingMode: %s, currentUserCanInvite: %{bool}d, ckShare.allowsAccessRequests: %s, isFolderSubshare: %{bool}d"
+ "_coOwnerNewParticipantsCanBeCoOwners"
+ "allowAccessRequestsSPIOverride"
+ "allowsAccessRequests"
+ "changeRequestAccessAllowed non-SPI call and the SPI has already set a value"
+ "changeRequestAccessAllowed: no share, or current user can't manage access requests. newAccessAllowed: %{bool}d, oldAccessAllowed: %{bool}d, is a share: %{bool}d, currentUserCanManageAccessRequests: %{bool}d, oldShareAccessAllowed: [none], saveShare: %{bool}d (ignored)"
+ "doBRSharingFileOrFolderSave about to save share with allowsAccessRequests: %{bool}d"
+ "optionsModel ckShareModel.$ckShare about to set anyoneCanRequestAccessPublisher to ckShare's allowsAccessRequests: %{bool}d"
+ "saveShare completed CloudDocs (fileURL) operation \"%s\"\n %@\n allowsAccessRequests: %{bool}d"
+ "saveShare performing CloudDocs (fileURL) operation \"%s\" -- %@\n allowsAccessRequests: %{bool}d"
+ "saveShare succeeded, rootRecordID: %s, share allowAccessRequests: %{bool,public}d"
+ "setAllowsAccessRequests:"
- "PeopleViewModel Combine3: sharingMode: %s, currentUserCanInvite: %{bool}d, isFolderSubshare: %{bool}d"
- "accessRequestsEnabled"
- "enableAccessRequests:"
- "saveShare completed CloudDocs (fileURL) operation \"%s\" -- %@"
- "saveShare performing CloudDocs (fileURL) operation \"%s\" -- %@"
- "saveShare succeeded, rootRecordID: %s"

```

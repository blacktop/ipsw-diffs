## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2351.0.0.0.0
-  __TEXT.__text: 0xdd8a8
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0xa3f8
+2352.1.1.0.0
+  __TEXT.__text: 0xde3c8
+  __TEXT.__auth_stubs: 0x16a0
+  __TEXT.__objc_methlist: 0xa410
   __TEXT.__const: 0x10e4
-  __TEXT.__cstring: 0x1572b
-  __TEXT.__oslogstring: 0x802e
+  __TEXT.__cstring: 0x1579d
+  __TEXT.__oslogstring: 0x820a
   __TEXT.__gcc_except_tab: 0xf60
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2c70
+  __TEXT.__unwind_info: 0x2c88
   __TEXT.__objc_classname: 0xc51
-  __TEXT.__objc_methname: 0x1c506
+  __TEXT.__objc_methname: 0x1c551
   __TEXT.__objc_methtype: 0x2119
-  __TEXT.__objc_stubs: 0xd1e0
-  __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0x4b68
+  __TEXT.__objc_stubs: 0xd200
+  __DATA_CONST.__got: 0xa48
+  __DATA_CONST.__const: 0x4b78
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x57c8
+  __DATA_CONST.__objc_selrefs: 0x57e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_got: 0xb60
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x21f0
-  __AUTH_CONST.__cfstring: 0x18820
+  __AUTH_CONST.__const: 0x2210
+  __AUTH_CONST.__cfstring: 0x188e0
   __AUTH_CONST.__objc_const: 0xdfc8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1180
   __DATA.__objc_ivar: 0x958
-  __DATA.__data: 0xb48
-  __DATA.__bss: 0xc79
+  __DATA.__data: 0xb50
+  __DATA.__bss: 0xc89
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4694
-  Symbols:   6715
-  CStrings:  8474
+  Functions: 4703
+  Symbols:   6739
+  CStrings:  8492
 
Symbols:
+ _MCPathWithoutPrivatePathComponent
+ _MCDestinationPathIsSafeFromSymlinkAttacks
+ _acl_set_fd_np
+ _MCMakePathDeletableBySettingACL
+ _kSystemUsersGroupName
+ _MCFeatureRCSAllowed
+ _NSFileTypeSymbolicLink
+ _acl_set_qualifier
+ _NSFileType
+ _acl_add_perm
+ _acl_clear_perms
+ _MCFixHostileSymlinks
+ _acl_init
+ _acl_get_permset
+ _mbr_identifier_to_uuid
+ _MCFeatureMailSummaryAllowed
+ _MCUserProfileLibraryDirectory
+ _MCReplaceSymlinkWithDirectory
+ _acl_set_tag_type
+ _acl_set_permset
+ _acl_create_entry
CStrings:
+ "private"
+ "UserConfigurationProfiles"
+ "systemusers"
+ "Destination path contains suspicious symlink: %!{(MISSING)public}@"
+ "Symbolic link removed from %!{(MISSING)public}@"
+ "allowMailSummary"
+ "Error reading attributes for %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "allowRCSMessaging"
+ "isRCSMessagingAllowed"
+ "Error removing symbolic link for %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Error setting ACL on symbolic link before removal for %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "isMailSummaryAllowed"
+ "stringByResolvingSymlinksInPath"
+ "FEATURE_RCS_MESSAGING"
+ "Finished check for symbolic links in user and system group folder"
+ "MCDestinationPathIsSafeFromSymlinkAttacks path:\n\t%!{(MISSING)public}@\nresolved:\n\t%!{(MISSING)public}@"
+ "Error creating directory %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "ALLOWED_DEVICE_IDS"
+ "FEATURE_MAIL_SUMMARY"
+ "ALLOWED_DEVICE_NAMES"
- "Library/UserConfigurationProfiles"
- "ALLOWED_DEVICES"

```

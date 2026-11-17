## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-1857.2.6.0.0
-  __TEXT.__text: 0x2fe18
-  __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x6e4
-  __TEXT.__gcc_except_tab: 0x449c
+1857.2.10.0.0
+  __TEXT.__text: 0x32fcc
+  __TEXT.__auth_stubs: 0x1da0
+  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__objc_methlist: 0x6f4
+  __TEXT.__gcc_except_tab: 0x4910
   __TEXT.__const: 0x8fa
-  __TEXT.__cstring: 0x1d22
-  __TEXT.__oslogstring: 0x1550
-  __TEXT.__objc_methname: 0x24e7
+  __TEXT.__cstring: 0x1f52
+  __TEXT.__oslogstring: 0x16be
+  __TEXT.__objc_methname: 0x25d0
   __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methtype: 0xbdf
   __TEXT.__swift5_typeref: 0xb6

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x13f0
+  __TEXT.__unwind_info: 0x1520
   __TEXT.__eh_frame: 0xe0
-  __DATA_CONST.__const: 0x1408
-  __DATA_CONST.__cfstring: 0x1860
+  __DATA_CONST.__const: 0x1478
+  __DATA_CONST.__cfstring: 0x1c00
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x230
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0xde8
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_got: 0xee0
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0x7b8
-  __DATA.__objc_selrefs: 0x8e0
+  __DATA.__objc_selrefs: 0x930
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x1d0
-  __DATA.__data: 0x348
+  __DATA.__data: 0x358
   __DATA.__thread_vars: 0x30
-  __DATA.__thread_bss: 0x10
+  __DATA.__thread_data: 0x10
+  __DATA.__thread_bss: 0x8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 707
-  Symbols:   755
-  CStrings:  901
+  Functions: 749
+  Symbols:   798
+  CStrings:  954
 
Symbols:
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _NSURLVolumeTotalCapacityKey
+ _NSURLVolumeURLKey
+ _OBJC_CLASS_$_NSUserDefaults
+ _PurgeSpaceIfNeeded
+ __Z19kTStringLiteralDataIJLc48ELc120EEE
+ __Z19kTStringLiteralDataIJLc60ELc110ELc111ELc110ELc101ELc62EEE
+ __ZN10TCFURLInfo13EverybodyUUIDEv
+ __ZN12ROSPVolumeID11SetVolumeIDEPK8__CFData
+ __ZN12ROSPVolumeIDC2EPK7__CFURL
+ __ZNSt19bad_optional_accessD1Ev
+ __ZNSt3__119piecewise_constructE
+ __ZTISt19bad_optional_access
+ __ZTVSt19bad_optional_access
+ _acl_add_flag_np
+ _acl_add_perm
+ _acl_clear_perms
+ _acl_create_entry_np
+ _acl_delete_entry
+ _acl_delete_perm
+ _acl_get_entry
+ _acl_get_flag_np
+ _acl_get_flagset_np
+ _acl_get_perm_np
+ _acl_get_permset
+ _acl_get_qualifier
+ _acl_get_tag_type
+ _acl_set_flagset_np
+ _acl_set_permset
+ _acl_set_qualifier
+ _acl_set_tag_type
+ _archive_write_set_format_option
+ _fflagstostr
+ _fts_close
+ _fts_open
+ _fts_read
+ _lchflags
+ _mbr_check_membership
+ _mbr_gid_to_uuid
+ _mbr_uid_to_uuid
+ _mbr_uuid_to_id
+ _uuid_compare
+ _uuid_copy
- __ZN10TCFURLInfo19GetVolumeIdentifierEPK7__CFURL
CStrings:
+ " for new items"
+ "%#x"
+ ","
+ "/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete"
+ "; "
+ "<none>"
+ "B8@?0"
+ "CACHE_DELETE_AMOUNT"
+ "CACHE_DELETE_URGENCY"
+ "CACHE_DELETE_VOLUME"
+ "CacheDeleteCopyPurgeableSpaceWithInfo"
+ "CacheDeletePurgeSpaceWithInfo"
+ "Can't open up unarchived item (%{errno}d)"
+ "DSArchiveStoreNFCEntryNames"
+ "Failed fetching NSURLVolumeIsLocalKey for unarchived folder: %{public}@, %@"
+ "Failed to allow the owner ahead of an unarchived item's group denies (%{errno}d)"
+ "Failed to exempt the owner from an unarchived item's denies (%{errno}d)"
+ "Failed to open up unarchived folder (%{errno}d)"
+ "Group membership lookup failed (%d), so group denies may keep blocking the owner"
+ "Leaving ACLs alone on a network volume"
+ "Opened up %{public}@: %{public}@"
+ "UTF-8"
+ "_entryPathnameForItemArchivePath:"
+ "addObjectsFromArray:"
+ "add_file"
+ "add_subdirectory"
+ "allowed the owner %@ ahead of group denies%s"
+ "append"
+ "array"
+ "boolForKey:"
+ "chown"
+ "componentsJoinedByString:"
+ "delete"
+ "delete_child"
+ "execute"
+ "fileSize"
+ "flags %@ -> %@"
+ "hdrcharset"
+ "list"
+ "mode %04o -> %04o"
+ "none"
+ "precomposedStringWithCanonicalMapping"
+ "r*24@0:8@16"
+ "read"
+ "removeCachedResourceValueForKey:"
+ "removed %@ from the owner's deny"
+ "removed the ACL"
+ "resourceValuesForKeys:error:"
+ "search"
+ "standardUserDefaults"
+ "v16@?0^{__CFDictionary=}8"
+ "write"
+ "writeattr"
+ "writeextattr"
+ "writesecurity"
- "Failed fetching NSURLVolumeIsLocalKey for source: %@"
- "Failed fetching NSURLVolumeIsLocalKey for target: %@"
```

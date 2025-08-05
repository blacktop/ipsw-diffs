## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x52e48
+2632.0.77.0.1
+  __TEXT.__text: 0x53bac
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__cstring: 0x19348
+  __TEXT.__cstring: 0x19901
   __TEXT.__const: 0x85f8
-  __TEXT.__unwind_info: 0xb48
+  __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7904DF49-5082-38C0-BA58-D7A37785DD10
-  Functions: 938
+  UUID: 808E26F1-E5A0-33C9-AA64-8BDDB93B50E4
+  Functions: 944
   Symbols:   203
-  CStrings:  1940
+  CStrings:  1958
 
CStrings:
+ "2632.0.77.0.1"
+ "can't add attribution tag for clonegroup: %s (%d)\n"
+ "can't add dir stats key for clonegroup: %s (%d)\n"
+ "can't allocate memory to insert a new clonegroup value\n"
+ "can't cross check inode (id %llu) with its corresponding clonegroup record: %d (%s)\n"
+ "clone group mapping record missing for (group_id %llu, private_id %llu, file_id %llu)\n"
+ "clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n"
+ "clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n"
+ "clonegroup records of (private_id %llu) count (%u) != dstream_id refcount (%u)\n"
+ "clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect attribution tag (%llu)\n"
+ "clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect dir-stats key (%llu)\n"
+ "compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n"
+ "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) repair: %s\n"
+ "file (id %llu) isn't purgeable but its matching clonegroup record flags (0x%x) suggest it is\n"
+ "file (id %llu) purgeable_flags (0x%x) disagree with its matching clonegroup record flags (0x%x)\n"
+ "file_id %llu (group_id %llu, private_id %llu) has different clonegroup group_id (%llu)\n"
+ "found clone mapping in a volume with initialized clonegroup tree\n"
+ "found multiple clonegroup records for file_id %llu\n"
+ "missing clone group record for file_id %llu (private_id %llu, group_id %llu)\n"
+ "number of files in clonegroup (%u) != dstream reference count (%u)\n"
+ "private_id (%llu) has multiple clonegroup ids (%llu, %llu)\n"
- "2632.0.68.0.3"
- "failed to enqueue clone group mapping (group_id %llu, private_id %llu, file_id %llu) for deletion: %s\n"
- "missing clone group record for file_id %llu\n"

```

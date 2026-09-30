## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

```diff

   __TEXT.__const: 0xc35
   __TEXT.__cstring: 0x5196
-  __TEXT.__os_log: 0x17e36
-  __TEXT_EXEC.__text: 0x83e38
+  __TEXT.__os_log: 0x17fea
+  __TEXT_EXEC.__text: 0x8401c
   __TEXT_EXEC.__auth_stubs: 0x1580
   __DATA.__data: 0x12d8
   __DATA.__bss: 0x107c

   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 797
-  Symbols:   4000
-  CStrings:  2649
+  Symbols:   4007
+  CStrings:  2656
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ smb1fs_smb_findclose.kalloc_type_view_5683
+ smbfs_get_maximum_access.kalloc_type_view_1721
+ smbfs_get_maximum_access.kalloc_type_view_1742
+ smbfs_smb_findopen.kalloc_type_view_5946
+ smbfs_smb_reopen_file.kalloc_type_view_5033
+ smbfs_smb_reopen_file.kalloc_type_view_5109
- smb1fs_smb_findclose.kalloc_type_view_5639
- smbfs_get_maximum_access.kalloc_type_view_1707
- smbfs_get_maximum_access.kalloc_type_view_1728
- smbfs_smb_findopen.kalloc_type_view_5902
- smbfs_smb_reopen_file.kalloc_type_view_4989
- smbfs_smb_reopen_file.kalloc_type_view_5065
Functions:
~ _packattrblk : 4184 -> 4220
~ _FindFileRef : 1324 -> 1332
~ _smbfs_build_path : 668 -> 656
~ _smbfs_smb_unix_read_symlink : 712 -> 780
~ _smbfs_unix_whoami : 628 -> 912
~ _smb_fphelp : 1088 -> 1072
~ _smbfs_sysctl : 2764 -> 2768
~ _smbfs_enum_dir : 6292 -> 6332
~ _smbfs_add_dir_entry_attr : 3228 -> 3232
~ _smb_sm_negotiate : 2172 -> 2184
~ _smb_sm_ssnsetup : 828 -> 832
~ _smbfs_getsecurity : 2824 -> 2960
~ _smbfs_setsecurity : 2408 -> 2332
~ _smb_compression_allowed : 808 -> 800
CStrings:
+ "%s: ACE %u ace_len=%u exceeds buffer boundary, file(%s)\n"
+ "%s: ACE %u has invalid ace_len=%u (< %zu), possible malicious server, file(%s)\n"
+ "%s: UNIX_LINK nmlen=%zu would overflow target_allocsize\n"
+ "%s: WHOAMI invalid fields: reserved=%u cnt_gid=%d sids_cnt=%d\n"
+ "%s: WHOAMI kalloc_data of %zu bytes for ntwrk_gids failed\n"
+ "%s: WHOAMI total_bytes=%zu exceeds session_txmax=%u\n"
+ "%s: WHOAMI truncated gid list at index %u of %u (err=%d)\n"
+ "%s: minauth=kerberos required"
+ "%s: minauth=kerberos required so NTLM not allowed"
+ "%s: minauth=kerberos required so SMBV_RAW_NTLMSSP not allowed"
- "%s: Kerberos access is set"
- "%s: Kerberos access is set so NTLM not allowed"
- "%s: Kerberos access is set so SMBV_RAW_NTLMSSP not allowed"

```

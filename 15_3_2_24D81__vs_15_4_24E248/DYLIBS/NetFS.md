## NetFS

> `/System/Library/Frameworks/NetFS.framework/Versions/A/NetFS`

```diff

 61.0.0.0.0
-  __TEXT.__text: 0xb7c4
+  __TEXT.__text: 0xb6bc
   __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x98
   __TEXT.__oslogstring: 0x807
   __TEXT.__cstring: 0x11ba
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x1d
   __TEXT.__objc_methname: 0x2f9
   __TEXT.__objc_methtype: 0x277

   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_protorefs: 0x8
   __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0x188
+  __AUTH_CONST.__objc_const: 0x60
   __DATA.__data: 0x2b0
   __DATA.__bss: 0x9
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90AC4AD1-24E2-32F6-9680-50FFEF89D45C
-  Functions: 197
-  Symbols:   447
+  UUID: 4E30BB71-4C68-3B82-B26A-F14EE19DEFB8
+  Functions: 194
+  Symbols:   445
   CStrings:  313
 
Symbols:
- _OtherConsoleUserOwnsMount
Functions:
~ _FindPluginByFSInLibrary : 116 -> 112
~ _ScanAllPluginsInLibrary : 1556 -> 1552
~ _LoadPlugin : 1352 -> 1372
~ _piston_smb1_readmsg : 480 -> 476
~ _piston_smb2_readmsg : 484 -> 480
~ _netfs_getLibraryEntryOverXPC : 1036 -> 1040
~ _NetFSGetSupportedSchemes : 624 -> 612
~ _NetFSMountHomeDirectoryWithAuthentication : 2356 -> 2740
~ _findservermountpoint : 1836 -> 1844
- _OtherConsoleUserOwnsMount
~ _NetFSUnmountHomeDirectory : 460 -> 456
- sub_1a581a5dc
~ _GetRemountInfoInterfaceForMounter : 560 -> 540
~ _GetNetFSMountInterface_V1ForMounter : 592 -> 572
~ _GetURLRemountInfo : 524 -> 528
~ _copy_opts_to_dict : 552 -> 540
~ _mountinfo_to_mountpoints : 316 -> 308
~ _netfs_Mount : 1280 -> 1276
~ _get_last_component : 172 -> 176
~ _CreateUniqueMountpoint : 616 -> 608
~ _NetFSMountURLSync : 376 -> 380
~ _NetFSMountURLProbe : 1532 -> 1508
~ _stripbasename : 336 -> 340
~ _piston_set_server : 232 -> 228
~ _piston_set_treeconn_status : 80 -> 68
~ _piston_get_treeconn_status : 60 -> 56
~ _piston_set_session_status : 80 -> 68
~ _piston_get_session_status : 60 -> 56
~ _piston_smb1_alloc_hdr : 232 -> 228
~ _piston_smb1_next_mid : 76 -> 64
~ _piston_smb1_set_tid : 80 -> 68
~ _piston_smb1_set_uid : 80 -> 68
~ _piston_smb2_next_msgid : 76 -> 64
~ _piston_smb2_alloc_hdr : 216 -> 212
- _OUTLINED_FUNCTION_1
~ _smb2_curr_credits : 60 -> 56
~ _smb2_add_credits_granted : 88 -> 76
~ _piston_make_utf16_treestr : 216 -> 212
~ _piston_utf8_to_utf16 : 176 -> 164
~ piston_sndmsgbufs.cold.1 : 136 -> 124
~ piston_sndmsgbufs.cold.2 : 124 -> 136
~ piston_smb1_readmsg.cold.2 : 140 -> 128
~ piston_smb1_readmsg.cold.4 : 128 -> 140
~ piston_smb2_readmsg.cold.2 : 140 -> 128
~ piston_smb2_readmsg.cold.4 : 128 -> 140
~ piston_open_sock.cold.1 : 152 -> 172
~ piston_open_sock.cold.2 : 180 -> 132
~ piston_open_sock.cold.4 : 132 -> 176
~ piston_open_sock.cold.5 : 176 -> 148
~ piston_read_n.cold.1 : 148 -> 144
~ piston_smb1_negotiate_easy.cold.1 : 128 -> 124
~ piston_smb1_negotiate_easy.cold.2 : 124 -> 128
~ piston_smb2_negotiate_easy.cold.1 : 128 -> 124
~ piston_smb2_negotiate_easy.cold.2 : 124 -> 128
~ piston_set_user_creds.cold.1 : 124 -> 132
~ piston_set_user_creds.cold.2 : 124 -> 132
~ piston_set_realm.cold.1 : 124 -> 132
~ piston_set_share.cold.1 : 124 -> 132
~ piston_smb1_set_native_os.cold.1 : 124 -> 132
~ piston_smb1_set_native_lanman.cold.1 : 124 -> 132
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/NetFSFramework/URLMount.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/NetFSFramework/URLMount.c"

```

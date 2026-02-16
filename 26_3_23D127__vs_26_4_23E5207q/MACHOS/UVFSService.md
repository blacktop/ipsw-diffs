## UVFSService

> `/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService`

```diff

-741.0.3.0.0
-  __TEXT.__text: 0x2393c
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x1580
-  __TEXT.__cstring: 0x11b7
+741.100.13.0.0
+  __TEXT.__text: 0x228c4
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0x1578
+  __TEXT.__cstring: 0x1211
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x410a
-  __TEXT.__objc_methtype: 0x14f4
-  __TEXT.__oslogstring: 0x3e4a
+  __TEXT.__objc_methname: 0x4134
+  __TEXT.__objc_methtype: 0x14f9
+  __TEXT.__oslogstring: 0x3ea8
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__unwind_info: 0x580
-  __DATA_CONST.__auth_got: 0x4b0
+  __TEXT.__gcc_except_tab: 0x8d4
+  __TEXT.__unwind_info: 0x578
+  __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x23c8
+  __DATA.__objc_const: 0x2398
   __DATA.__objc_selrefs: 0x1028
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x278
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4512EEFB-9FA6-3D4E-B0E8-AD9054F29B7D
-  Functions: 746
-  Symbols:   287
-  CStrings:  1535
+  UUID: 86A3BDEA-7DE9-31C9-B2CC-41F25EFD808E
+  Functions: 759
+  Symbols:   279
+  CStrings:  1534
 
Symbols:
+ _OBJC_CLASS_$_FSMachPort
+ _OBJC_CLASS_$_FSSharedMutableBuffer
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_LiveFSMachPort
- _OBJC_CLASS_$_LiveFSSharedMutableBuffer
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%s: unregister with LiveFS service for volume %@ using LIVEFSMOUNTCLIENT_UNMOUNT_FORGET | LIVEFSMOUNTCLIENT_UNMOUNT_FSKITD_WAS_TERMINATED"
+ "%s:fd(%d):error(%@)"
+ "%s:start:deviceName(%@):volumeNames(%@)"
+ "-[userFSVolume invalidateFileNodesForConnection:terminateVolume:]_block_invoke"
+ "getAppleDoubleFromCacheWithBaseFile:named:inDirectory:"
+ "getAttrSubset"
+ "i44@0:8r^Q16I24Q28@?<v@?I^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}*>36"
+ "i64@0:8@\"NSDictionary\"16^Q24^Q32^i40^@48^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}56"
+ "i64@0:8@16^Q24^Q32^i40^@48^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}56"
+ "invalidateFileNodesForConnection:terminateVolume:"
+ "reclaimAndRemoveFromCache"
+ "serviceExitingForDevice:volumeNames:withReply:"
+ "v24@0:8^{_scandir_matching_reply=C^{_FSDirEntryAttr}Q}16"
+ "v28@0:8Q16B24"
+ "v28@?0I8r^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}12r*20"
+ "v28@?0i8Q12@\"NSData\"20"
+ "v32@0:8^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16@24"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v56@0:8^{_scandir_matching_request=^*^*^{_FSFileAttributes}QQ}16^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24^Q32^Q40@48"
- "%s: volume has KOIO disabled."
- "%s:start:%@"
- "@\"LiveFSAppleDouble\""
- "LISetXattr, setting appledouble not opened for Writing to nil"
- "T@\"LiveFSAppleDouble\",&,V_lfn_appledouble"
- "_lfn_appledouble"
- "i44@0:8r^Q16I24Q28@?<v@?I^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}*>36"
- "i64@0:8@\"NSDictionary\"16^Q24^Q32^i40^@48^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}56"
- "i64@0:8@16^Q24^Q32^i40^@48^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}56"
- "lfn_appledouble"
- "purpose"
- "reclaimFile"
- "serviceExitingForDevice:withReply:"
- "setLfn_appledouble:"
- "v20@?0i8Q12"
- "v24@0:8^{_scandir_matching_reply=C^{_LIDirEntryAttr}Q}16"
- "v28@?0I8r^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}12r*20"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16@24"
- "v56@0:8^{_scandir_matching_request=^*^*^{_LIFileAttributes}QQ}16^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}24^Q32^Q40@48"

```

## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2899.60.1.0.1
-  __TEXT.__text: 0x272280
+2899.60.7.0.0
+  __TEXT.__text: 0x272204
   __TEXT.__auth_stubs: 0x3360
-  __TEXT.__objc_stubs: 0x29200
-  __TEXT.__objc_methlist: 0x17784
+  __TEXT.__objc_stubs: 0x29220
+  __TEXT.__objc_methlist: 0x17794
   __TEXT.__const: 0x17c0
-  __TEXT.__cstring: 0x6f1e1
-  __TEXT.__objc_methname: 0x37d5c
+  __TEXT.__cstring: 0x6f1ca
+  __TEXT.__objc_methname: 0x37d9e
   __TEXT.__constg_swiftt: 0x7cc
   __TEXT.__swift5_typeref: 0xd08
   __TEXT.__swift5_reflstr: 0xe12

   __TEXT.__objc_classname: 0x1fab
   __TEXT.__objc_methtype: 0x64f8
   __TEXT.__swift5_capture: 0x3ec
-  __TEXT.__oslogstring: 0x32b48
+  __TEXT.__oslogstring: 0x32b0c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc08c
+  __TEXT.__gcc_except_tab: 0xc040
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x6910
   __TEXT.__eh_frame: 0x1c88
   __DATA_CONST.__auth_got: 0x19c0
-  __DATA_CONST.__got: 0xda0
+  __DATA_CONST.__got: 0xd98
   __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x83e8
+  __DATA_CONST.__const: 0x83c0
   __DATA_CONST.__cfstring: 0x1c940
   __DATA_CONST.__objc_classlist: 0xa10
   __DATA_CONST.__objc_catlist: 0xd0

   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA.__objc_const: 0x25418
-  __DATA.__objc_selrefs: 0xbf90
+  __DATA.__objc_selrefs: 0xbf98
   __DATA.__objc_ivar: 0x1b34
   __DATA.__objc_data: 0x7000
   __DATA.__data: 0x24d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EDB7F193-F470-36D2-A9D8-D1E2FA0A7733
-  Functions: 9495
-  Symbols:   1343
-  CStrings:  27412
+  UUID: 601BA9F5-3D3A-359F-BECE-B7889D21876A
+  Functions: 9497
+  Symbols:   1342
+  CStrings:  27411
 
Symbols:
- _OBJC_CLASS_$_ICQOfferManager
CStrings:
+ "-[MBBackupScheduler _onFollowUpQueue_warnUserOfDelayedRestoreWithAccount:]"
+ "-[MBBackupScheduler _onFollowUpQueue_warnUserOfLateBackupWithAccount:]"
+ "_onFollowUpQueue_warnUserOfDelayedRestoreWithAccount:"
+ "_onFollowUpQueue_warnUserOfLateBackupWithAccount:"
+ "_postAndRefreshBackgroundRestoreFollowUps:"
+ "fsctl(APFSIOC_MAKE_OBJECT_DATALESS) error (%d) %s"
+ "internalIgnoreSetDatalessErrors"
- "-[MBBackupScheduler _onQueue_warnUserOfDelayedRestoreWithAccount:]"
- "-[MBBackupScheduler _onQueue_warnUserOfLateBackupWithAccount:]"
- "Not posting restore finished follow up because of ICQ offer"
- "_onQueue_warnUserOfDelayedRestoreWithAccount:"
- "_onQueue_warnUserOfLateBackupWithAccount:"
- "postBackupRestoredOffer:"
- "set_dataless_attribute error"

```

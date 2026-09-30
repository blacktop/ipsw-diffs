## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2899.0.2.0.0
-  __TEXT.__text: 0x2899c8
-  __TEXT.__auth_stubs: 0x3610
-  __TEXT.__objc_stubs: 0x291e0
-  __TEXT.__objc_methlist: 0x17794
-  __TEXT.__const: 0x2240
-  __TEXT.__cstring: 0x6ff2a
-  __TEXT.__objc_methname: 0x37d90
+2899.0.8.0.0
+  __TEXT.__text: 0x28a2d8
+  __TEXT.__auth_stubs: 0x3620
+  __TEXT.__objc_stubs: 0x292a0
+  __TEXT.__objc_methlist: 0x177ec
+  __TEXT.__const: 0x22a0
+  __TEXT.__cstring: 0x7002e
+  __TEXT.__objc_methname: 0x37e49
   __TEXT.__constg_swiftt: 0xa8c
   __TEXT.__swift5_typeref: 0x107d
-  __TEXT.__swift5_reflstr: 0x1655
-  __TEXT.__swift5_fieldmd: 0x159c
+  __TEXT.__swift5_reflstr: 0x1675
+  __TEXT.__swift5_fieldmd: 0x15a8
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x160
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_proto: 0x168
   __TEXT.__swift5_types: 0xf0
   __TEXT.__objc_classname: 0x1fab
   __TEXT.__objc_methtype: 0x652e
-  __TEXT.__swift5_capture: 0x444
-  __TEXT.__oslogstring: 0x3291e
+  __TEXT.__swift5_capture: 0x454
+  __TEXT.__oslogstring: 0x32938
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__gcc_except_tab: 0xc1d8
+  __TEXT.__gcc_except_tab: 0xc1f4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6ce0
+  __TEXT.__unwind_info: 0x6d00
   __TEXT.__eh_frame: 0x2320
-  __DATA_CONST.__auth_got: 0x1b18
-  __DATA_CONST.__got: 0xde8
+  __DATA_CONST.__auth_got: 0x1b20
+  __DATA_CONST.__got: 0xdf0
   __DATA_CONST.__auth_ptr: 0x348
-  __DATA_CONST.__const: 0x8d68
-  __DATA_CONST.__cfstring: 0x1c9c0
+  __DATA_CONST.__const: 0x8da0
+  __DATA_CONST.__cfstring: 0x1ca40
   __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x718
   __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0xd28
+  __DATA_CONST.__objc_arraydata: 0xd38
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
-  __DATA.__objc_const: 0x25510
-  __DATA.__objc_selrefs: 0xc020
+  __DATA.__objc_const: 0x25558
+  __DATA.__objc_selrefs: 0xc058
   __DATA.__objc_ivar: 0x1b34
-  __DATA.__objc_data: 0x7148
-  __DATA.__data: 0x2978
-  __DATA.__bss: 0x3268
+  __DATA.__objc_data: 0x7150
+  __DATA.__data: 0x2988
+  __DATA.__bss: 0x3368
   __DATA.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81FED964-9036-34EC-9F1A-A527CDA791E2
-  Functions: 9792
-  Symbols:   1398
-  CStrings:  27523
+  UUID: 565127B8-4243-3072-8ACC-B7916F577F9E
+  Functions: 9811
+  Symbols:   1397
+  CStrings:  27543
 
Symbols:
+ _kMBManagerManualBackupStartedNotification
+ _swift_dynamicCastObjCClass
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia
CStrings:
+ "-[MBCKManager boostManualBackupWithAccount:completionHandler:]"
+ "=domain-engine= Restore root does not exist at %@"
+ "Failed to setup backup: %@"
+ "Not running manual backup (%d)"
+ "Restore root does not exist"
+ "_boostManualBackup:"
+ "boostManualBackupWithAccount:completionHandler:"
+ "forceCacheReset"
+ "kMBMessageBoostManualBackup"
+ "manualBackupInProgress"
+ "setUnboostManualBackupHandler:"
+ "unboostManualBackup"
+ "unboostManualBackupHandler"
- "unboostBackgroundRestoreHandler called: %{public}@"

```

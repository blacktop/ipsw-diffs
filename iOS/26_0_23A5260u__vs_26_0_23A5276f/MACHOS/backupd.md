## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2877.0.0.0.0
-  __TEXT.__text: 0x289484
+2891.0.0.0.0
+  __TEXT.__text: 0x2895d0
   __TEXT.__auth_stubs: 0x3610
-  __TEXT.__objc_stubs: 0x291e0
-  __TEXT.__objc_methlist: 0x1778c
+  __TEXT.__objc_stubs: 0x29200
+  __TEXT.__objc_methlist: 0x1779c
   __TEXT.__const: 0x2240
-  __TEXT.__cstring: 0x6fc57
-  __TEXT.__objc_methname: 0x37dad
+  __TEXT.__cstring: 0x6fe4b
+  __TEXT.__objc_methname: 0x37dce
   __TEXT.__constg_swiftt: 0xa8c
   __TEXT.__swift5_typeref: 0x107d
   __TEXT.__swift5_reflstr: 0x1655

   __TEXT.__objc_classname: 0x1fad
   __TEXT.__objc_methtype: 0x6517
   __TEXT.__swift5_capture: 0x444
-  __TEXT.__oslogstring: 0x32788
+  __TEXT.__oslogstring: 0x328c7
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__gcc_except_tab: 0xc0c0
+  __TEXT.__gcc_except_tab: 0xc1b4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6c78
+  __TEXT.__unwind_info: 0x6cb0
   __TEXT.__eh_frame: 0x2320
   __DATA_CONST.__auth_got: 0x1b18
-  __DATA_CONST.__got: 0xdd0
-  __DATA_CONST.__auth_ptr: 0x340
-  __DATA_CONST.__const: 0x8d38
-  __DATA_CONST.__cfstring: 0x1c8a0
+  __DATA_CONST.__got: 0xdd8
+  __DATA_CONST.__auth_ptr: 0x348
+  __DATA_CONST.__const: 0x8d68
+  __DATA_CONST.__cfstring: 0x1c9a0
   __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x718
-  __DATA_CONST.__objc_intobj: 0x3c0
+  __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xd28
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA.__objc_const: 0x25528
-  __DATA.__objc_selrefs: 0xc020
+  __DATA.__objc_selrefs: 0xc028
   __DATA.__objc_ivar: 0x1b38
   __DATA.__objc_data: 0x7148
   __DATA.__data: 0x2978
-  __DATA.__bss: 0x3258
+  __DATA.__bss: 0x3268
   __DATA.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5DA32BC2-6F6C-337A-ACE3-B363E99C02A7
-  Functions: 9788
-  Symbols:   1399
-  CStrings:  27494
+  UUID: DF275999-EC6A-3CE8-BBC3-2A59781D5EF4
+  Functions: 9793
+  Symbols:   1396
+  CStrings:  27519
 
Symbols:
+ _$sSbN
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "=ATC= %@"
+ "=ckrestore-engine= Excluding legacy app placeholder for %{public}@"
+ "=ckrestore-engine= Sanitized ATC restore error: %@"
+ "=scheduler= [Off condition after %.1fs] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, managerStates:%@, changes:%{public}@"
+ "=scheduler= [Off condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, managerStates:%@, changes:%{public}@"
+ "=scheduler= [On condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, managerStates:%@, changes:%{public}@"
+ "=verifier= Marking verification success for %@ because container %@ was removed during verification"
+ "No account found, returning idle restore state"
+ "bg-restore"
+ "com.apple.backupd.backupOnCellularEnablement"
+ "com.apple.private.restrict-post.MobileBackup.BackupOverCellularEnabledState"
+ "fg-restore"
+ "finishing-restore"
+ "idle"
+ "sanitizedATCRestoreError:"
+ "serviceStates"
+ "setup"
- "=scheduler= [Off condition after %.1fs] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, changes:%{public}@"
- "=scheduler= [Off condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, changes:%{public}@"
- "=scheduler= [On condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, changes:%{public}@"
- "isIdle"

```

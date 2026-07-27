## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-5980.160.2.0.0
-  __TEXT.__text: 0x10f444
+5980.160.4.0.0
+  __TEXT.__text: 0x10fb5c
   __TEXT.__auth_stubs: 0x12f0
-  __TEXT.__objc_methlist: 0x107d8
+  __TEXT.__objc_methlist: 0x10840
   __TEXT.__const: 0x214
-  __TEXT.__gcc_except_tab: 0x3638
-  __TEXT.__cstring: 0x2321a
+  __TEXT.__gcc_except_tab: 0x36c8
+  __TEXT.__cstring: 0x232ba
   __TEXT.__oslogstring: 0x402
   __TEXT.__ustring: 0x135c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x3398
+  __TEXT.__unwind_info: 0x33c0
   __TEXT.__objc_classname: 0x178f
-  __TEXT.__objc_methname: 0x25937
-  __TEXT.__objc_methtype: 0x2ddb
-  __TEXT.__objc_stubs: 0x1cfa0
+  __TEXT.__objc_methname: 0x259a9
+  __TEXT.__objc_methtype: 0x2dce
+  __TEXT.__objc_stubs: 0x1d0a0
   __DATA_CONST.__got: 0xf48
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8500
+  __DATA_CONST.__objc_selrefs: 0x8530
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x6a0
   __AUTH_CONST.__auth_got: 0x990
   __AUTH_CONST.__const: 0x1bf0
-  __AUTH_CONST.__cfstring: 0x197a0
-  __AUTH_CONST.__objc_const: 0x17180
+  __AUTH_CONST.__cfstring: 0x19800
+  __AUTH_CONST.__objc_const: 0x171b0
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x3a88
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x1274
-  __DATA.__data: 0x1308
+  __DATA.__objc_ivar: 0x1278
+  __DATA.__data: 0x1310
   __DATA.__bss: 0x170
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5666
-  Symbols:   13134
-  CStrings:  10680
+  Functions: 5676
+  Symbols:   13154
+  CStrings:  10690
 
Symbols:
+ -[SMDCustomize_XPCClientConnection clearCustomizeLatch]
+ -[SMDCustomize_XPCClientConnection dealloc]
+ -[SMDCustomize_XPCClientConnection invalidate]
+ -[SMDCustomize_XPCClientConnection observeValueForKeyPath:ofObject:change:context:]
+ -[SMDCustomize_XPCClientConnection observedSystem]
+ -[SMDCustomize_XPCClientConnection setObservedSystem:]
+ -[SMDPairing_XPCClientConnection invalidate]
+ -[SMPairingManager _startScanning]
+ -[SMPairingManager scanning]
+ -[SMPairingManager setScanning:]
+ -[SMSystem_Daemon_TimeMachineBased retrieveBackupsWithSession:]
+ OBJC_IVAR_$_SMDCustomize_XPCClientConnection._observedSystem
+ OBJC_IVAR_$_SMPairingManager._scanning
+ ___33-[SMPairingManager startScanning]_block_invoke
+ ___63-[SMSystem_Daemon_TimeMachineBased retrieveBackupsWithSession:]_block_invoke
+ _kCustomizeSystemStateContext
+ _objc_msgSend$_startScanning
+ _objc_msgSend$clearCustomizeLatch
+ _objc_msgSend$finishSession:
+ _objc_msgSend$observedSystem
+ _objc_msgSend$retrieveBackupsWithSession:
+ _objc_msgSend$scanning
+ _objc_msgSend$setObservedSystem:
+ _objc_msgSend$setScanning:
+ _objc_msgSend$stopScanning
+ _objc_msgSend$storageVolume
- -[SMSystem_Daemon_TimeMachineBased setTimeMachineSession:]
- -[SMSystem_Daemon_TimeMachineBased timeMachineSession]
- OBJC_IVAR_$_SMSystem_Daemon_TimeMachineBased._timeMachineSession
- ___51-[SMSystem_Daemon_TimeMachineBased retrieveBackups]_block_invoke
- _objc_msgSend$setTimeMachineSession:
- _objc_msgSend$timeMachineSession
CStrings:
+ "-[SMSystem_Daemon_TimeMachineBased retrieveBackupsWithSession:]"
+ "Finishing TMSession for mount point: %@"
+ "Finishing TMSession for mount point: %@ (%d systems created)"
+ "Started TMSession for mount point: %@"
+ "T@\"SMSystem_Daemon\",&,V_observedSystem"
+ "TB,V_scanning"
+ "_observedSystem"
+ "_scanning"
+ "_startScanning"
+ "clearCustomizeLatch"
+ "finishSession:"
+ "observedSystem"
+ "retrieveBackupsWithSession:"
+ "scanning"
+ "setObservedSystem:"
+ "setScanning:"
- "-[SMSystem_Daemon_TimeMachineBased retrieveBackups]"
- "@\"TMSession\""
- "T@\"TMSession\",&,V_timeMachineSession"
- "_timeMachineSession"
- "setTimeMachineSession:"
- "timeMachineSession"
```

## backupd

> `/System/Library/CoreServices/TimeMachine/backupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`

```diff

-2609.3.0.0.0
-  __TEXT.__text: 0x14d650
-  __TEXT.__auth_stubs: 0x3fd0
-  __TEXT.__objc_stubs: 0x8780
+2612.1.0.0.0
+  __TEXT.__text: 0x14d4b0
+  __TEXT.__auth_stubs: 0x3fb0
+  __TEXT.__objc_stubs: 0x87a0
   __TEXT.__objc_methlist: 0x2ff0
-  __TEXT.__const: 0x8770
-  __TEXT.__gcc_except_tab: 0xc38
-  __TEXT.__cstring: 0x1173a
-  __TEXT.__objc_methname: 0xac59
-  __TEXT.__objc_classname: 0x101c
-  __TEXT.__objc_methtype: 0x2ab1
-  __TEXT.__swift5_typeref: 0x3621
-  __TEXT.__constg_swiftt: 0x2b28
-  __TEXT.__swift5_reflstr: 0x2813
-  __TEXT.__swift5_fieldmd: 0x2a24
-  __TEXT.__swift5_capture: 0x25c8
+  __TEXT.__const: 0x8890
+  __TEXT.__gcc_except_tab: 0xc44
+  __TEXT.__cstring: 0x1194a
+  __TEXT.__objc_methname: 0xacb1
+  __TEXT.__objc_classname: 0x100c
+  __TEXT.__objc_methtype: 0x2b11
+  __TEXT.__swift5_typeref: 0x362f
+  __TEXT.__constg_swiftt: 0x2b30
+  __TEXT.__swift5_reflstr: 0x2843
+  __TEXT.__swift5_fieldmd: 0x2a3c
+  __TEXT.__swift5_capture: 0x2668
   __TEXT.__swift5_builtin: 0x258
   __TEXT.__swift5_assocty: 0x968
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__swift5_proto: 0x710
-  __TEXT.__swift5_types: 0x3a0
-  __TEXT.__swift_as_entry: 0x320
-  __TEXT.__swift_as_ret: 0x2e0
-  __TEXT.__swift_as_cont: 0x4cc
+  __TEXT.__swift5_proto: 0x734
+  __TEXT.__swift5_types: 0x3a8
+  __TEXT.__swift_as_entry: 0x340
+  __TEXT.__swift_as_ret: 0x300
+  __TEXT.__swift_as_cont: 0x4fc
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4900
-  __TEXT.__eh_frame: 0xa028
-  __DATA_CONST.__const: 0x8740
-  __DATA_CONST.__cfstring: 0x5360
+  __TEXT.__unwind_info: 0x49e0
+  __TEXT.__eh_frame: 0xa440
+  __DATA_CONST.__const: 0x8868
+  __DATA_CONST.__cfstring: 0x53e0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0x2000
-  __DATA_CONST.__got: 0xeb8
-  __DATA_CONST.__auth_ptr: 0xa70
-  __DATA.__objc_const: 0x7918
-  __DATA.__objc_selrefs: 0x2658
+  __DATA_CONST.__auth_got: 0x1ff0
+  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__auth_ptr: 0xa78
+  __DATA.__objc_const: 0x7938
+  __DATA.__objc_selrefs: 0x2660
   __DATA.__objc_ivar: 0x2bc
   __DATA.__objc_data: 0x28d8
-  __DATA.__data: 0x4c00
-  __DATA.__bss: 0xa548
+  __DATA.__data: 0x4be8
+  __DATA.__bss: 0xa558
   __DATA.__common: 0x128
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5201
-  Symbols:   1716
-  CStrings:  3619
+  Functions: 5246
+  Symbols:   1714
+  CStrings:  3630
 
Symbols:
- _fsync
- _futimes
CStrings:
+ "@52@0:8@16Q24i32@36@44"
+ "Checkpoint barrier F_FULLFSYNC failed - error: %d %s"
+ "Checkpoint barrier: couldn't open container '%@' to fsync - error: %d %s"
+ "Failing in-progress backup: space-based purge is removing its %@ '%@'."
+ "Reference snapshot moving backwards from "
+ "Reference snapshot moving backwards: "
+ "_pendingFailureError"
+ "advanceReferenceLocalSnapshot(on:to:)"
+ "backUp(sources:toMountedDestination:backupStore:rulesEngine:fileProviderManager:deviceUnlockedAssertion:phaseReporter:indexer:thinningManager:ioWorkerQueue:cancelClosure:)"
+ "failCurrentBackupWithResultCode:diskName:orTerminateByDate:completionHandler:"
+ "fsck exited with termination status %d but the destination's backing store is full - treating as a recoverable disk-full condition rather than corruption, output:\n%@"
+ "purgeLocalSnapshotsForVolumeGroupContaining:targetBytesFree:urgency:configuration:issuer:"
+ "tm_errorWithResult:msgParams:"
+ "v48@0:8q16@\"NSString\"24@\"NSDate\"32@?<v@?>40"
+ "v48@0:8q16@24@32@?40"
- "@44@0:8@16Q24i32@36"
- "backUp(sources:toMountedDestination:backupStore:rulesEngine:fileProviderManager:deviceUnlockedAssertion:phaseReporter:indexer:thinningManager:ioWorkerQueue:)"
- "doubleSyncToDisk"
- "purgeLocalSnapshotsForVolumeGroupContaining:targetBytesFree:urgency:configuration:"
```

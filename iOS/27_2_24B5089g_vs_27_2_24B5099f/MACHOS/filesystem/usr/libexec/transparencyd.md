## transparencyd

> `/usr/libexec/transparencyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_acfuncs`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-1766.40.50.0.0
-  __TEXT.__text: 0x33c3bc
-  __TEXT.__auth_stubs: 0x49f0
-  __TEXT.__objc_stubs: 0x1ea00
-  __TEXT.__objc_methlist: 0x16300
+1766.40.56.0.0
+  __TEXT.__text: 0x33cd8c
+  __TEXT.__auth_stubs: 0x49e0
+  __TEXT.__objc_stubs: 0x1ea20
+  __TEXT.__objc_methlist: 0x16310
   __TEXT.__objc_classname: 0x4214
-  __TEXT.__cstring: 0x15130
-  __TEXT.__objc_methname: 0x26c52
-  __TEXT.__const: 0x23ff8
-  __TEXT.__gcc_except_tab: 0x5054
-  __TEXT.__oslogstring: 0x1517a
-  __TEXT.__objc_methtype: 0x8a31
-  __TEXT.__swift5_typeref: 0x4430
+  __TEXT.__cstring: 0x151f0
+  __TEXT.__objc_methname: 0x26c92
+  __TEXT.__const: 0x240a8
+  __TEXT.__gcc_except_tab: 0x50bc
+  __TEXT.__oslogstring: 0x152ca
+  __TEXT.__objc_methtype: 0x8a41
+  __TEXT.__swift5_typeref: 0x443e
   __TEXT.__swift5_capture: 0x1dd0
-  __TEXT.__constg_swiftt: 0x5104
-  __TEXT.__swift5_reflstr: 0x316e
+  __TEXT.__constg_swiftt: 0x5120
+  __TEXT.__swift5_reflstr: 0x317e
   __TEXT.__swift5_fieldmd: 0x4628
-  __TEXT.__swift5_proto: 0xd14
-  __TEXT.__swift5_types: 0x444
-  __TEXT.__swift5_assocty: 0x910
-  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_proto: 0xd20
+  __TEXT.__swift5_types: 0x448
+  __TEXT.__swift5_assocty: 0x928
+  __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift_as_entry: 0x35c
   __TEXT.__swift_as_ret: 0x31c
   __TEXT.__swift_as_cont: 0x5e0
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_acfuncs: 0xdc
-  __TEXT.__unwind_info: 0x117b8
-  __TEXT.__eh_frame: 0xc1c8
-  __DATA_CONST.__const: 0x1f250
-  __DATA_CONST.__cfstring: 0xed40
+  __TEXT.__unwind_info: 0x117d8
+  __TEXT.__eh_frame: 0xc1f8
+  __DATA_CONST.__const: 0x1f2d8
+  __DATA_CONST.__cfstring: 0xee60
   __DATA_CONST.__objc_classlist: 0xdf0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x440

   __DATA_CONST.__objc_arraydata: 0x1e8
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x240
-  __DATA_CONST.__auth_got: 0x2508
-  __DATA_CONST.__got: 0x16e8
+  __DATA_CONST.__auth_got: 0x2500
+  __DATA_CONST.__got: 0x16d8
   __DATA_CONST.__auth_ptr: 0x12b0
   __DATA.__objc_const: 0x33dd0
-  __DATA.__objc_selrefs: 0x8d18
+  __DATA.__objc_selrefs: 0x8d28
   __DATA.__objc_ivar: 0x118c
   __DATA.__objc_data: 0xab60
   __DATA.__data: 0xe5e8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 20629
-  Symbols:   2278
-  CStrings:  12085
+  Functions: 20639
+  Symbols:   2277
+  CStrings:  12101
 
Symbols:
+ _$s11Distributed0A23TargetInvocationDecoderP18decodeNextArgumentqd__yKlFTj
- _$s14XPCDistributed9XPCSystemC17InvocationDecoderV18decodeNextArgumentxyKSeRzSERzlF
- _swift_conformsToProtocol2
CStrings:
+ "StaticKeyOrphanGCEvent"
+ "StaticKeyOrphanGCReaped"
+ "anyHandleStillMatchesAContact:moc:"
+ "changeOptInState: IDS account showed up while waiting for Ready, going on"
+ "changeOptInState: timed out waiting for Ready, account status may be stale"
+ "examined"
+ "garbageCollectOrphanedStaticKeys abandoning pass: all %lu pins resolved as not-found"
+ "garbageCollectOrphanedStaticKeys keeping %@: identifier unresolvable but a handle still matches a contact"
+ "ktDutyCycleGateAttemptFloor"
+ "ktDutyCycleGateRun"
+ "ktDutyCycleGateSuccessFloor"
+ "ktRunDutyCycleFallback"
+ "ktRunDutyCycleForced"
+ "ktRunDutyCycleScheduled"
+ "rpcReasonEventNamesForRequest:"
+ "runDutyCycleInternal:trigger:"
+ "v32@0:8@?16Q24"
- "runDutyCycleInternal:"
```

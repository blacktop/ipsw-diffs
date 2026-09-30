## mobilerepaird

> `/usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1307.2.4.0.0
-  __TEXT.__text: 0x1c820
+1307.40.46.0.0
+  __TEXT.__text: 0x1cc00
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x3660
-  __TEXT.__objc_methlist: 0x17fc
+  __TEXT.__objc_stubs: 0x36c0
+  __TEXT.__objc_methlist: 0x181c
   __TEXT.__const: 0x152
-  __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__objc_methname: 0x3f4a
+  __TEXT.__gcc_except_tab: 0x974
+  __TEXT.__objc_methname: 0x3fb9
   __TEXT.__cstring: 0x3de6
-  __TEXT.__oslogstring: 0x2ad9
+  __TEXT.__oslogstring: 0x2cb7
   __TEXT.__objc_classname: 0x55f
   __TEXT.__objc_methtype: 0xce2
   __TEXT.__ustring: 0x12a

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8b0
-  __DATA_CONST.__const: 0xbc0
+  __TEXT.__unwind_info: 0x8c8
+  __DATA_CONST.__const: 0xc20
   __DATA_CONST.__cfstring: 0x3e40
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2e28
-  __DATA.__objc_selrefs: 0x1058
+  __DATA.__objc_selrefs: 0x1070
   __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0xe20
   __DATA.__data: 0x458

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 594
+  Functions: 600
   Symbols:   292
-  CStrings:  1549
+  CStrings:  1557
 
CStrings:
+ "CRShipModeOperationScheduler: cancel disengage of ship-charge limit failed: 0x%08x (%@); lock left engaged"
+ "CRShipModeOperationScheduler: notify failed for %{public}@; releasing ship-charge limit"
+ "CRShipModeOperationScheduler: released ship-charge limit after failed notify"
+ "CRShipModeOperationScheduler: released ship-charge limit latched by cancelled discharge"
+ "CRShipModeOperationScheduler: ship-charge limit release failed (ioReturn=0x%08x, error=%{public}@); lock left engaged"
+ "_releaseShipChargeLimitForDroppedDischarge"
+ "_releaseShipLockAfterFailedNotifyFor:"
+ "_tearDownDischargeAfterCancel"
```

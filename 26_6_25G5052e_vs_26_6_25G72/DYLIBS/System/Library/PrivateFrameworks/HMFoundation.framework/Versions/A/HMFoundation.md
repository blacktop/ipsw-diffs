## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__eh_frame`
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
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1418.7.15.0.0
-  __TEXT.__text: 0x93270
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x76a4
+1418.7.18.0.0
+  __TEXT.__text: 0x93660
+  __TEXT.__auth_stubs: 0x1e40
+  __TEXT.__objc_methlist: 0x76cc
   __TEXT.__const: 0x2bf8
   __TEXT.__dlopen_cstrs: 0x10a
-  __TEXT.__cstring: 0x2f31
+  __TEXT.__cstring: 0x2f54
   __TEXT.__swift5_typeref: 0xa0e
   __TEXT.__swift5_capture: 0x608
   __TEXT.__swift_as_entry: 0x17c

   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x3f46
+  __TEXT.__oslogstring: 0x3ff3
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x1b08
+  __TEXT.__gcc_except_tab: 0x1b60
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x3080
+  __TEXT.__unwind_info: 0x3090
   __TEXT.__eh_frame: 0x31f8
   __TEXT.__objc_classname: 0x107f
-  __TEXT.__objc_methname: 0xc3d0
+  __TEXT.__objc_methname: 0xc462
   __TEXT.__objc_methtype: 0x2662
-  __TEXT.__objc_stubs: 0x91c0
+  __TEXT.__objc_stubs: 0x9200
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3088
+  __DATA_CONST.__objc_selrefs: 0x30a0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__auth_got: 0xf30
   __AUTH_CONST.__const: 0x3138
   __AUTH_CONST.__cfstring: 0x4800
-  __AUTH_CONST.__objc_const: 0xdd40
+  __AUTH_CONST.__objc_const: 0xdd70
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x10e0

   __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x22f0
   __DATA.__bss: 0x684
-  __DATA_DIRTY.__objc_ivar: 0x564
+  __DATA_DIRTY.__objc_ivar: 0x568
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x230
   __DATA_DIRTY.__bss: 0x5c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3500
-  Symbols:   6424
-  CStrings:  3866
+  Functions: 3503
+  Symbols:   6430
+  CStrings:  3875
 
Symbols:
+ -[HMFMemoryMonitor setTriggerSuppressionExpiry:]
+ -[HMFMemoryMonitor triggerProcessMemoryWarning]
+ -[HMFMemoryMonitor triggerSuppressionExpiry]
+ _objc_msgSend$setTriggerSuppressionExpiry:
+ _objc_msgSend$triggerSuppressionExpiry
+ _sysctlbyname
CStrings:
+ "%{public}@Error (%s) sending internal memory pressure event"
+ "%{public}@Success sending internal memory pressure event"
+ "%{public}@Suppressing observer dispatch for provoked %@"
+ "T@\"NSDate\",C,V_triggerSuppressionExpiry"
+ "_triggerSuppressionExpiry"
+ "kern.memorystatus_vm_pressure_send"
+ "setTriggerSuppressionExpiry:"
+ "triggerProcessMemoryWarning"
+ "triggerSuppressionExpiry"
```

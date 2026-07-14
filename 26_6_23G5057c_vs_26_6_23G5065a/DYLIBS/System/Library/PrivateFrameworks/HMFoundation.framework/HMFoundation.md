## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

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

```diff

-  __TEXT.__text: 0x8f5a0
-  __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x78d4
+  __TEXT.__text: 0x8f954
+  __TEXT.__auth_stubs: 0x21a0
+  __TEXT.__objc_methlist: 0x78fc
   __TEXT.__const: 0x2bf8
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x305a
+  __TEXT.__cstring: 0x307d
   __TEXT.__swift5_typeref: 0xa0e
   __TEXT.__swift5_capture: 0x608
   __TEXT.__swift_as_entry: 0x17c

   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x42c8
+  __TEXT.__oslogstring: 0x4375
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x1c30
+  __TEXT.__gcc_except_tab: 0x1c88
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x31b0
+  __TEXT.__unwind_info: 0x31c0
   __TEXT.__eh_frame: 0x3210
   __TEXT.__objc_classname: 0x1135
-  __TEXT.__objc_methname: 0xc8e7
+  __TEXT.__objc_methname: 0xc979
   __TEXT.__objc_methtype: 0x27d8
-  __TEXT.__objc_stubs: 0x9400
+  __TEXT.__objc_stubs: 0x9440
   __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3128
+  __DATA_CONST.__objc_selrefs: 0x3140
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__auth_got: 0x10e0
   __AUTH_CONST.__const: 0x2150
   __AUTH_CONST.__cfstring: 0x4b40
-  __AUTH_CONST.__objc_const: 0xe3c8
+  __AUTH_CONST.__objc_const: 0xe3f8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1130

   __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x2558
   __DATA.__bss: 0x720
-  __DATA_DIRTY.__objc_ivar: 0x5b0
+  __DATA_DIRTY.__objc_ivar: 0x5b4
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3509
-  Symbols:   6542
-  CStrings:  3973
+  Functions: 3512
+  Symbols:   6548
+  CStrings:  3982
 
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

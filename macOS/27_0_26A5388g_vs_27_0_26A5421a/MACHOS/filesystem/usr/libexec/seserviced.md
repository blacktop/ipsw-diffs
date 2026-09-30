## seserviced

> `/usr/libexec/seserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-70.37.0.0.0
-  __TEXT.__text: 0xe51f4
+70.39.1.0.0
+  __TEXT.__text: 0xe5238
   __TEXT.__auth_stubs: 0x29c0
   __TEXT.__objc_stubs: 0x3f40
   __TEXT.__objc_methlist: 0x1d4c
-  __TEXT.__const: 0x9868
+  __TEXT.__const: 0x9888
   __TEXT.__gcc_except_tab: 0x624
-  __TEXT.__objc_methname: 0x5851
+  __TEXT.__objc_methname: 0x5801
   __TEXT.__oslogstring: 0x4772
   __TEXT.__cstring: 0x891b
   __TEXT.__objc_classname: 0x8e8
   __TEXT.__objc_methtype: 0x1fd9
-  __TEXT.__constg_swiftt: 0x1948
-  __TEXT.__swift5_typeref: 0x1a74
+  __TEXT.__constg_swiftt: 0x193c
+  __TEXT.__swift5_typeref: 0x1a88
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x18ed
-  __TEXT.__swift5_fieldmd: 0x200c
+  __TEXT.__swift5_reflstr: 0x18fd
+  __TEXT.__swift5_fieldmd: 0x2028
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__swift5_proto: 0x574
-  __TEXT.__swift5_types: 0x248
+  __TEXT.__swift5_types: 0x24c
   __TEXT.__swift5_capture: 0x480
   __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift_as_entry: 0x110

   __TEXT.__swift5_protos: 0x10
   __TEXT.__unwind_info: 0x2c18
   __TEXT.__eh_frame: 0x59d4
-  __DATA_CONST.__const: 0x6d70
+  __DATA_CONST.__const: 0x6df8
   __DATA_CONST.__cfstring: 0x2a20
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__auth_got: 0x14f0
   __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__auth_ptr: 0x638
-  __DATA.__objc_const: 0x5668
+  __DATA_CONST.__auth_ptr: 0x640
+  __DATA.__objc_const: 0x5628
   __DATA.__objc_selrefs: 0x1410
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0x1ad8
-  __DATA.__data: 0x337a
+  __DATA.__data: 0x333a
   __DATA.__bss: 0xa0b0
   __DATA.__common: 0x308
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3461
-  Symbols:   1154
-  CStrings:  2411
+  Functions: 3463
+  Symbols:   1155
+  CStrings:  2409
 
Symbols:
+ _$s15Synchronization5MutexVMn
CStrings:
+ "counters"
+ "macOS (27.0) - SecureElementService-70.39.1"
- "countsKeyedByCountEvents"
- "elapsedTimesKeyedByEvents"
- "invalidationReason"
- "macOS (27.0) - SecureElementService-70.37"
```

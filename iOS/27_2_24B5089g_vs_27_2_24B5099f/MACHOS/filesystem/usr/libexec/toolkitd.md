## toolkitd

> `/usr/libexec/toolkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-5111.0.2.0.0
-  __TEXT.__text: 0x9b2d8
-  __TEXT.__auth_stubs: 0x2e20
-  __TEXT.__objc_stubs: 0x1a20
+5113.0.1.1.1
+  __TEXT.__text: 0x9bbe0
+  __TEXT.__auth_stubs: 0x2e60
+  __TEXT.__objc_stubs: 0x1a40
   __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x46bc
+  __TEXT.__const: 0x46cc
   __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methname: 0x12e8
+  __TEXT.__objc_methname: 0x1328
   __TEXT.__objc_methtype: 0x1fe
   __TEXT.__constg_swiftt: 0xd38
-  __TEXT.__swift5_typeref: 0x1807
-  __TEXT.__swift5_reflstr: 0x1084
-  __TEXT.__swift5_fieldmd: 0x10b4
-  __TEXT.__cstring: 0x221d
-  __TEXT.__oslogstring: 0x18fc
+  __TEXT.__swift5_typeref: 0x1815
+  __TEXT.__swift5_reflstr: 0x10a4
+  __TEXT.__swift5_fieldmd: 0x10cc
+  __TEXT.__cstring: 0x223d
+  __TEXT.__oslogstring: 0x194c
   __TEXT.__swift5_capture: 0xd44
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x330
   __TEXT.__swift5_proto: 0x1c4
   __TEXT.__swift5_types: 0x148
   __TEXT.__swift_as_entry: 0x1dc
-  __TEXT.__swift_as_cont: 0x40c
-  __TEXT.__swift_as_ret: 0x224
+  __TEXT.__swift_as_cont: 0x414
+  __TEXT.__swift_as_ret: 0x228
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_mpenum: 0xc8
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x23e0
-  __TEXT.__eh_frame: 0x5f30
+  __TEXT.__unwind_info: 0x2408
+  __TEXT.__eh_frame: 0x5fc0
   __DATA_CONST.__const: 0x4350
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x1718
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__auth_ptr: 0x758
-  __DATA.__objc_const: 0x738
-  __DATA.__objc_selrefs: 0x718
+  __DATA_CONST.__auth_got: 0x1738
+  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__auth_ptr: 0x768
+  __DATA.__objc_const: 0x780
+  __DATA.__objc_selrefs: 0x720
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1cc0
+  __DATA.__data: 0x1ce0
   __DATA.__common: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2971
-  Symbols:   1276
-  CStrings:  593
+  Functions: 2984
+  Symbols:   1285
+  CStrings:  598
 
Symbols:
+ _$s11WorkflowKit26AppIntentsInitialIndexGateO12waitForReady_7timeoutyAA0cD17IndexingReadiness_p_s8DurationVtYaKFZ
+ _$s11WorkflowKit26AppIntentsInitialIndexGateO12waitForReady_7timeoutyAA0cD17IndexingReadiness_p_s8DurationVtYaKFZTu
+ _$s11WorkflowKit27AppIntentsIndexingReadinessMp
+ _$sS2cEycfC
+ _$sScEMa
+ _$sScEs5ErrorsMc
+ _$ss8DurationV7secondsyABSdFZ
+ _$ss8DurationVMn
+ _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "AppIntents initial-index gate failed/timed out; deferring index (retriable): %@"
+ "AppIntentsInitialIndexGate"
+ "appIntentsReadiness"
+ "gateTimeout"
+ "toolKitDaemonInitialIndexGateTimeout"
```

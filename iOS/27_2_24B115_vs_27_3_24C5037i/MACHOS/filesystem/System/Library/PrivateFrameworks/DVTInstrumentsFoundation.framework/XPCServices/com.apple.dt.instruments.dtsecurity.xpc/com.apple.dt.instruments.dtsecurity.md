## com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-64578.209.1.0.0
-  __TEXT.__text: 0x11b58
-  __TEXT.__auth_stubs: 0x1740
+64579.9.1.0.0
+  __TEXT.__text: 0x12254
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__objc_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x5c0
-  __TEXT.__const: 0x492
+  __TEXT.__objc_methlist: 0x5b8
+  __TEXT.__const: 0x4c2
   __TEXT.__oslogstring: 0x136c
-  __TEXT.__cstring: 0x1326
+  __TEXT.__cstring: 0x12e6
   __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methtype: 0x2c1
+  __TEXT.__objc_methtype: 0x2d0
   __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__objc_methname: 0x1415
-  __TEXT.__constg_swiftt: 0x140
-  __TEXT.__swift5_typeref: 0xa0
-  __TEXT.__swift5_reflstr: 0x2c4
-  __TEXT.__swift5_fieldmd: 0x23c
+  __TEXT.__objc_methname: 0x13b5
+  __TEXT.__swift5_typeref: 0xda
+  __TEXT.__constg_swiftt: 0x180
+  __TEXT.__swift5_reflstr: 0x2f4
+  __TEXT.__swift5_fieldmd: 0x274
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x648
-  __TEXT.__eh_frame: 0x160
-  __DATA_CONST.__const: 0xec0
+  __TEXT.__unwind_info: 0x678
+  __TEXT.__eh_frame: 0x1f0
+  __DATA_CONST.__const: 0xf40
   __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xbb8
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0xd8
-  __DATA.__objc_const: 0xec0
-  __DATA.__objc_selrefs: 0x5b8
+  __DATA_CONST.__auth_got: 0xbe8
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_ptr: 0xf0
+  __DATA.__objc_const: 0xe40
+  __DATA.__objc_selrefs: 0x5b0
   __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0x508
-  __DATA.__data: 0x280
+  __DATA.__objc_data: 0x4d8
+  __DATA.__data: 0x310
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 398
-  Symbols:   465
-  CStrings:  600
+  Functions: 409
+  Symbols:   477
+  CStrings:  595
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_release_x25
+ _swift_retain_x23
+ _swift_storeEnumTagSinglePayloadGeneric
- _swift_release_x24
- _swift_updateClassMetadata2
CStrings:
+ "B32@0:8@16^@24"
+ "lockedState"
+ "startRecordingWithConfiguration:error:"
- "com_apple_dt_instruments_dtsecurity.ProcessorTraceRecorder"
- "configuration"
- "currentLiveRecording"
- "initWithConfiguration:"
- "logger"
- "signposter"
- "startRecordingAndReturnError:"
- "state"
```

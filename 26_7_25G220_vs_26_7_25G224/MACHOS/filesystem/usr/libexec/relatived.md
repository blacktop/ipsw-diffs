## relatived

> `usr/libexec/relatived`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

 333.3.1.0.0
-  __TEXT.__text: 0x17748
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x10e8
-  __TEXT.__const: 0x306
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__cstring: 0x1209
-  __TEXT.__objc_classname: 0x414
-  __TEXT.__objc_methname: 0x387b
-  __TEXT.__objc_methtype: 0x8c4
-  __TEXT.__oslogstring: 0x26a6
-  __TEXT.__constg_swiftt: 0x84
-  __TEXT.__swift5_typeref: 0x1a
-  __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x730
-  __DATA_CONST.__auth_got: 0x498
+  __TEXT.__text: 0x16cc8
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_stubs: 0x2fc0
+  __TEXT.__objc_methlist: 0x1088
+  __TEXT.__const: 0x2ba
+  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__cstring: 0x11a8
+  __TEXT.__objc_classname: 0x3ba
+  __TEXT.__objc_methname: 0x379f
+  __TEXT.__objc_methtype: 0x89d
+  __TEXT.__oslogstring: 0x2567
+  __TEXT.__unwind_info: 0x6f8
+  __DATA_CONST.__auth_got: 0x490
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xcd0
-  __DATA_CONST.__cfstring: 0xa60
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__const: 0xc50
+  __DATA_CONST.__cfstring: 0xa00
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2ac0
-  __DATA.__objc_selrefs: 0xd20
-  __DATA.__objc_ivar: 0x234
-  __DATA.__objc_data: 0x910
-  __DATA.__data: 0x3f0
+  __DATA.__objc_const: 0x2980
+  __DATA.__objc_selrefs: 0xcf8
+  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_data: 0x780
+  __DATA.__data: 0x3a0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 647
-  Symbols:   265
-  CStrings:  1096
+  Functions: 619
+  Symbols:   263
+  CStrings:  1072
 
Symbols:
- _$sBOWV
- _objc_opt_self
CStrings:
- "@\"_TtC9relatived19RMPerceptionSession\""
- "EKAnchoredTracking"
- "Feeding perception data: %{public}@"
- "Keeping existing RMPerceptionSession"
- "Not stopping RMPerceptionSession because new session is using it"
- "ObjectDetection"
- "Perception supported: %{public}d, perception enabled: %{public}d, verbose logging: %{public}d"
- "Perception update %{public}@"
- "Starting RMPerceptionSession"
- "Stopping RMPerceptionSession"
- "TempestEnablePerception"
- "TempestEnablePerceptionVerboseLogging"
- "_TtC9relatived19RMPerceptionSession"
- "_TtC9relatived23RMPerceptionSessionBase"
- "_feedEntityKitData:timestamp:"
- "_perceptionEnabled"
- "_perceptionSession"
- "_perceptionSessionRunning"
- "_perceptionSessionStartCounter"
- "_perceptionVerboseLoggingEnabled"
- "isAvailable"
- "startWithHandler:"
- "stop"
- "supportsEKAnchoredTracking"
```

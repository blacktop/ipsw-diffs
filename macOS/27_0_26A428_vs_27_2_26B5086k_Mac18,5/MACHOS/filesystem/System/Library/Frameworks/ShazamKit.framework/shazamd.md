## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-427.0.48.0.0
-  __TEXT.__text: 0x5ff84
+427.2.4.0.0
+  __TEXT.__text: 0x602bc
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0xd000
-  __TEXT.__objc_methlist: 0x628c
+  __TEXT.__objc_stubs: 0xd100
+  __TEXT.__objc_methlist: 0x629c
   __TEXT.__const: 0x744
-  __TEXT.__cstring: 0x2c67
-  __TEXT.__oslogstring: 0x550b
+  __TEXT.__cstring: 0x2c97
+  __TEXT.__oslogstring: 0x555b
   __TEXT.__gcc_except_tab: 0xb08
-  __TEXT.__objc_methname: 0x10e4f
+  __TEXT.__objc_methname: 0x10f0f
   __TEXT.__objc_classname: 0x14eb
   __TEXT.__objc_methtype: 0x31b1
   __TEXT.__swift5_typeref: 0x280

   __TEXT.__unwind_info: 0x1e80
   __TEXT.__eh_frame: 0xb48
   __DATA_CONST.__const: 0x1f60
-  __DATA_CONST.__cfstring: 0x25e0
+  __DATA_CONST.__cfstring: 0x2620
   __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258

   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x968
+  __DATA_CONST.__got: 0x980
   __DATA_CONST.__auth_ptr: 0x1d0
   __DATA.__objc_const: 0xd200
-  __DATA.__objc_selrefs: 0x3b40
+  __DATA.__objc_selrefs: 0x3b80
   __DATA.__objc_ivar: 0x5d4
   __DATA.__objc_data: 0x31b8
   __DATA.__data: 0x1ba0

   - /System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices
   - /System/Library/PrivateFrameworks/MediaServices.framework/Versions/A/MediaServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/ShazamCore.framework/Versions/A/ShazamCore
   - /System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/Versions/A/VoiceShortcutClient

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2170
-  Symbols:   568
-  CStrings:  3982
+  Functions: 2171
+  Symbols:   571
+  CStrings:  3993
 
Symbols:
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessState
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
CStrings:
+ "Could not fetch process states for Siri audio daemons due to error: %@"
+ "com.apple.corespeechd"
+ "com.apple.sirittsd"
+ "descriptor"
+ "initSystemTapWithFormat:excludePIDs:"
+ "numberWithInt:"
+ "pid"
+ "predicateMatchingAnyPredicate:"
+ "predicateMatchingJobLabel:"
+ "process"
+ "siriAudioProcessIdentifiers"
+ "statesForPredicate:withDescriptor:error:"
- "initSystemTapWithFormat:"
```

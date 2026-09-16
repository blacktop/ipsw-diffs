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
-  __TEXT.__text: 0x5a89c
+427.2.4.0.0
+  __TEXT.__text: 0x5ab9c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_stubs: 0xd2c0
-  __TEXT.__objc_methlist: 0x62d4
+  __TEXT.__objc_stubs: 0xd3c0
+  __TEXT.__objc_methlist: 0x62e4
   __TEXT.__const: 0x724
   __TEXT.__gcc_except_tab: 0xbe0
-  __TEXT.__oslogstring: 0x565b
-  __TEXT.__objc_methname: 0x1115f
-  __TEXT.__cstring: 0x2d07
+  __TEXT.__oslogstring: 0x569b
+  __TEXT.__objc_methname: 0x111ef
+  __TEXT.__cstring: 0x2d37
   __TEXT.__objc_classname: 0x14eb
   __TEXT.__objc_methtype: 0x31b1
   __TEXT.__swift5_typeref: 0x280

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e08
+  __TEXT.__unwind_info: 0x1e10
   __TEXT.__eh_frame: 0xb48
   __DATA_CONST.__const: 0x1cc8
-  __DATA_CONST.__cfstring: 0x2680
+  __DATA_CONST.__cfstring: 0x26c0
   __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258

   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__auth_got: 0x798
-  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x1d0
   __DATA.__objc_const: 0xd200
-  __DATA.__objc_selrefs: 0x3b88
+  __DATA.__objc_selrefs: 0x3bc8
   __DATA.__objc_ivar: 0x5d4
   __DATA.__objc_data: 0x31b8
   __DATA.__data: 0x1ba0

   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2130
-  Symbols:   599
-  CStrings:  3996
+  Functions: 2131
+  Symbols:   602
+  CStrings:  4007
 
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

## softposreaderd

> `/usr/libexec/softposreaderd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-50.31.1.0.0
-  __TEXT.__text: 0x4236c4
-  __TEXT.__auth_stubs: 0x4280
-  __TEXT.__objc_stubs: 0x20a0
+50.32.1.0.0
+  __TEXT.__text: 0x4239a8
+  __TEXT.__auth_stubs: 0x4290
+  __TEXT.__objc_stubs: 0x2080
   __TEXT.__objc_methlist: 0xe7c
-  __TEXT.__const: 0x88320
+  __TEXT.__const: 0x88340
   __TEXT.__swift5_typeref: 0x24cc
-  __TEXT.__cstring: 0x119bb
-  __TEXT.__objc_methtype: 0x1535
-  __TEXT.__oslogstring: 0xce1e
+  __TEXT.__cstring: 0x119ab
+  __TEXT.__objc_methtype: 0x1525
+  __TEXT.__oslogstring: 0xce4e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x794c
+  __TEXT.__constg_swiftt: 0x795c
   __TEXT.__swift5_proto: 0xcdc
   __TEXT.__swift5_types: 0x52c
   __TEXT.__objc_classname: 0x1a13
-  __TEXT.__objc_methname: 0x42dd
+  __TEXT.__objc_methname: 0x42cd
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x188
   __TEXT.__swift_as_cont: 0x3b0
   __TEXT.__swift5_protos: 0x138
-  __TEXT.__unwind_info: 0x4e48
-  __TEXT.__eh_frame: 0xcab4
-  __DATA_CONST.__const: 0x18280
+  __TEXT.__unwind_info: 0x4e40
+  __TEXT.__eh_frame: 0xca8c
+  __DATA_CONST.__const: 0x182d0
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__auth_got: 0x2148
+  __DATA_CONST.__auth_got: 0x2150
   __DATA_CONST.__got: 0xde0
   __DATA_CONST.__auth_ptr: 0xe40
   __DATA.__objc_const: 0x9190
-  __DATA.__objc_selrefs: 0xb18
+  __DATA.__objc_selrefs: 0xb10
   __DATA.__objc_data: 0x21f8
   __DATA.__data: 0xc7e8
   __DATA.__common: 0x8c0

   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SPRCore.framework/SPRCore
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSCLM.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6165
+  Functions: 6163
   Symbols:   1688
-  CStrings:  3581
+  CStrings:  3582
 
Symbols:
+ _BYSetupAssistantNeedsToRun
- _OBJC_CLASS_$_NFSession
CStrings:
+ "Failed to refresh UniversalSecureChannel: %@"
+ "dynamicSEUISheet.present failed: %@"
+ "isBuddyFlow"
- "setSessionTimeLimit:"
- "waiting for NFSecureElementManagerSession..."
```

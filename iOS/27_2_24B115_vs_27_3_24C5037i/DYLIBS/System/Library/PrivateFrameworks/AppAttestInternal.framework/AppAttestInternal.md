## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-158.0.0.0.0
-  __TEXT.__text: 0x68594
-  __TEXT.__objc_methlist: 0x6c4
+162.1.0.0.0
+  __TEXT.__text: 0x68724
+  __TEXT.__objc_methlist: 0x6cc
   __TEXT.__const: 0x4550
-  __TEXT.__cstring: 0x65be
-  __TEXT.__oslogstring: 0x386a
+  __TEXT.__cstring: 0x65ce
+  __TEXT.__oslogstring: 0x38ba
   __TEXT.__gcc_except_tab: 0x724
   __TEXT.__swift5_typeref: 0xb06
   __TEXT.__swift5_reflstr: 0x127d

   __TEXT.__swift_as_cont: 0x38
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x250
-  __TEXT.__unwind_info: 0x1418
+  __TEXT.__unwind_info: 0x1420
   __TEXT.__eh_frame: 0x1030
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xf8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1489
-  Symbols:   1168
-  CStrings:  830
+  Functions: 1491
+  Symbols:   1171
+  CStrings:  832
 
Symbols:
+ +[FeatureFlagsManager isKeyRotationEnabled]
+ ___43+[FeatureFlagsManager isKeyRotationEnabled]_block_invoke
+ _isKeyRotationEnabled.onceToken
CStrings:
+ "%25s:%-5d DeviceCheck Key Rotation feature flag enabled { enabled=%d }."
+ "AppAttest (%@-162.1) - %@"
+ "keyRotation"
- "AppAttest (%@-158) - %@"
```

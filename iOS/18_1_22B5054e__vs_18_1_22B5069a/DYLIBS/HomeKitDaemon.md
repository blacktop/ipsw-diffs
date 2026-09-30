## HomeKitDaemon

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon`

```diff

-1215.2.12.0.0
-  __TEXT.__text: 0xd78de8
+1215.2.15.1.2
+  __TEXT.__text: 0xd79a78
   __TEXT.__auth_stubs: 0x5610
-  __TEXT.__objc_methlist: 0x818c8
-  __TEXT.__cstring: 0x68fdb
+  __TEXT.__objc_methlist: 0x818f8
+  __TEXT.__cstring: 0x68fd7
   __TEXT.__swift5_typeref: 0x4114
   __TEXT.__const: 0x18b8c
   __TEXT.__constg_swiftt: 0x40f0

   __TEXT.__swift5_types: 0x370
   __TEXT.__swift5_capture: 0x148c
   __TEXT.__swift5_protos: 0xd8
-  __TEXT.__oslogstring: 0x11d3df
+  __TEXT.__oslogstring: 0x11d682
   __TEXT.__swift5_mpenum: 0xb0
   __TEXT.__gcc_except_tab: 0x28be0
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x29900
+  __TEXT.__unwind_info: 0x29910
   __TEXT.__eh_frame: 0xfef0
-  __TEXT.__objc_classname: 0x18aa3
-  __TEXT.__objc_methname: 0x14b75f
+  __TEXT.__objc_classname: 0x18acc
+  __TEXT.__objc_methname: 0x14b770
   __TEXT.__objc_methtype: 0x2befb
-  __TEXT.__objc_stubs: 0xb7360
-  __DATA_CONST.__got: 0x6580
-  __DATA_CONST.__const: 0x1b030
-  __DATA_CONST.__objc_classlist: 0x46b0
+  __TEXT.__objc_stubs: 0xb73a0
+  __DATA_CONST.__got: 0x6598
+  __DATA_CONST.__const: 0x1b0d0
+  __DATA_CONST.__objc_classlist: 0x46b8
   __DATA_CONST.__objc_catlist: 0x2d0
   __DATA_CONST.__objc_protolist: 0x1e38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37610
+  __DATA_CONST.__objc_selrefs: 0x37620
   __DATA_CONST.__objc_protorefs: 0x570
   __DATA_CONST.__objc_superrefs: 0x3550
   __DATA_CONST.__objc_arraydata: 0x32e8
   __AUTH_CONST.__auth_got: 0x2b20
-  __AUTH_CONST.__auth_ptr: 0x1438
-  __AUTH_CONST.__const: 0x1b138
+  __AUTH_CONST.__auth_ptr: 0x1898
+  __AUTH_CONST.__const: 0x1b158
   __AUTH_CONST.__cfstring: 0x5c100
-  __AUTH_CONST.__objc_const: 0x131a78
+  __AUTH_CONST.__objc_const: 0x131b08
   __AUTH_CONST.__objc_intobj: 0x36a8
   __AUTH_CONST.__objc_arrayobj: 0x900
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x2080
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1b4d8
+  __AUTH.__objc_data: 0x1b528
   __AUTH.__data: 0x3348
   __DATA.__objc_ivar: 0x95b8
   __DATA.__data: 0x19e28

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 57392
-  Symbols:   55344
-  CStrings:  81196
+  Functions: 57402
+  Symbols:   55358
+  CStrings:  81207
 
Symbols:
+ _HMHomeResetMatterStorageCorruptionOptionBadCert
+ _HMHomeResetMatterStorageCorruptionOptionEmpty
+ _HMHomeResetMatterStorageCorruptionOptionKey
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "%!{(MISSING)public}@Bad-cert option for resetting Matter storage is not supported in current configuration"
+ "%!{(MISSING)public}@Cannot generate bad fabric data when fabric isn't created yet"
+ "%!{(MISSING)public}@Cleared and left CHIP storage as empty"
+ "%!{(MISSING)public}@Empty storage option for resetting Matter storage is not supported in current configuration - option is ignored"
+ "%!{(MISSING)public}@Failed to generate bad fabric data into Matter storage: %!@(MISSING)"
+ "%!{(MISSING)public}@Failed to remove value for '%!@(MISSING)': %!@(MISSING)"
+ "%!{(MISSING)public}@Failed to save new value for '%!@(MISSING)': %!@(MISSING)"
+ "%!{(MISSING)public}@Failed to update value for '%!@(MISSING)': %!@(MISSING)"
+ "%!{(MISSING)public}@Found value for '%!@(MISSING)': %!@(MISSING)"
+ "%!{(MISSING)public}@Handling request to reset Matter storage with corruption option: %!@(MISSING)"
+ "%!{(MISSING)public}@Regenerating cert when handling commissioning cert request"
+ "%!{(MISSING)public}@Replaced Matter storage with bad fabric data"
+ "%!{(MISSING)public}@Successfully removed value for '%!@(MISSING)'"
+ "%!{(MISSING)public}@Successfully saved new value for '%!@(MISSING)'"
+ "%!{(MISSING)public}@Successfully updated value for '%!@(MISSING)'"
+ "HMDCoreDataCloudTransformableLocalEvents"
+ "HMHomeAutoSelectedPreferredResidents"
+ "HMHomeUserSelectedPreferredResident"
+ "createNewFabricIdentityWithCompletion:"
+ "nocSigner"
+ "operationalKeyPair"
+ "setNocSigner:"
- "%!{(MISSING)public}@Failed to remove '%!@(MISSING)': %!@(MISSING)"
- "%!{(MISSING)public}@Failed to save '%!@(MISSING)': %!@(MISSING)"
- "%!{(MISSING)public}@Found value for '%!@(MISSING)'"
- "%!{(MISSING)public}@Handling request to reset Matter storage"
- "%!{(MISSING)public}@Successfully removed '%!@(MISSING)'"
- "%!{(MISSING)public}@Successfully saved '%!@(MISSING)'"
- "%!{(MISSING)public}@Value for '%!@(MISSING)': %!@(MISSING)"
- "HMHomeAutoSelectedPreferredIdentifiers"
- "HMHomeUserSelectedPreferredIdentifier"
- "autoSelectedPreferredIdentifiers"
- "userSelectedPreferredIdentifier"

```

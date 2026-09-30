## HomeKitDaemonLegacy

> `/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy`

```diff

-1215.2.12.0.0
-  __TEXT.__text: 0xad9ae0
+1215.2.15.1.2
+  __TEXT.__text: 0xada630
   __TEXT.__auth_stubs: 0x3c50
   __TEXT.__objc_methlist: 0x6e254
   __TEXT.__const: 0x1132c

   __TEXT.__swift5_fieldmd: 0x7b8
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__oslogstring: 0xf44b1
+  __TEXT.__oslogstring: 0xf46e1
   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0x80
   __TEXT.__swift5_protos: 0x28

   __TEXT.__gcc_except_tab: 0x2664c
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x1f9f0
+  __TEXT.__unwind_info: 0x1fa08
   __TEXT.__eh_frame: 0x17d8
   __TEXT.__objc_classname: 0x12377
-  __TEXT.__objc_methname: 0x11b09f
+  __TEXT.__objc_methname: 0x11b0f0
   __TEXT.__objc_methtype: 0x251f0
-  __TEXT.__objc_stubs: 0xa1400
-  __DATA_CONST.__got: 0x5880
-  __DATA_CONST.__const: 0x154c0
+  __TEXT.__objc_stubs: 0xa1480
+  __DATA_CONST.__got: 0x5898
+  __DATA_CONST.__const: 0x15560
   __DATA_CONST.__objc_classlist: 0x35a8
   __DATA_CONST.__objc_catlist: 0x250
   __DATA_CONST.__objc_protolist: 0x1398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fb20
+  __DATA_CONST.__objc_selrefs: 0x2fb40
   __DATA_CONST.__objc_protorefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0x2d10
   __DATA_CONST.__objc_arraydata: 0x2838
   __AUTH_CONST.__auth_got: 0x1e40
   __AUTH_CONST.__auth_ptr: 0x388
-  __AUTH_CONST.__const: 0x12438
+  __AUTH_CONST.__const: 0x12458
   __AUTH_CONST.__cfstring: 0x4fe60
   __AUTH_CONST.__objc_const: 0xe6960
   __AUTH_CONST.__objc_arrayobj: 0x870

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
-  Functions: 44602
-  Symbols:   47300
-  CStrings:  69584
+  Functions: 44609
+  Symbols:   47311
+  CStrings:  69595
 
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
+ "%!{(MISSING)public}@Handling request to reset Matter storage with corruption option: %!@(MISSING)"
+ "%!{(MISSING)public}@Regenerating cert when handling commissioning cert request"
+ "%!{(MISSING)public}@Replaced Matter storage with bad fabric data"
+ "T@\"HMDResidentDevice\",R,V_userSelectedPreferredResident"
+ "T@\"NSArray\",R,C,V_autoSelectedPreferredResidents"
+ "_autoSelectedPreferredResidents"
+ "_userSelectedPreferredResident"
+ "autoSelectedPreferredResidents"
+ "createNewFabricIdentityWithCompletion:"
+ "nocSigner"
+ "operationalKeyPair"
+ "setNocSigner:"
+ "userSelectedPreferredResident"
- "%!{(MISSING)public}@Handling request to reset Matter storage"
- "T@\"NSArray\",R,C,V_autoSelectedPreferredIdentifiers"
- "T@\"NSUUID\",R,V_userSelectedPreferredIdentifier"
- "_autoSelectedPreferredIdentifiers"
- "_userSelectedPreferredIdentifier"
- "autoSelectedPreferredIdentifiers"
- "userSelectedPreferredIdentifier"

```

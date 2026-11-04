## homeeventsd

> `/System/Library/PrivateFrameworks/HomeKitEvents.framework/Support/homeeventsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-1520.2.7.1.3
-  __TEXT.__text: 0x85bc8
-  __TEXT.__auth_stubs: 0x1fb0
-  __TEXT.__objc_stubs: 0x1220
+1535.0.0.0.2
+  __TEXT.__text: 0x86f24
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0x3404
+  __TEXT.__const: 0x3434
   __TEXT.__objc_classname: 0x516
-  __TEXT.__objc_methname: 0x1b04
+  __TEXT.__objc_methname: 0x1b14
   __TEXT.__objc_methtype: 0x73e
-  __TEXT.__constg_swiftt: 0x10e0
-  __TEXT.__swift5_typeref: 0x153e
+  __TEXT.__constg_swiftt: 0x10e8
+  __TEXT.__swift5_typeref: 0x154a
   __TEXT.__swift5_reflstr: 0xe39
   __TEXT.__swift5_fieldmd: 0xd88
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__oslogstring: 0x3d4a
+  __TEXT.__oslogstring: 0x3eba
   __TEXT.__cstring: 0x1233
   __TEXT.__swift5_capture: 0xed0
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0x1dc
   __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift_as_entry: 0x214
-  __TEXT.__swift_as_ret: 0x294
-  __TEXT.__swift_as_cont: 0x588
+  __TEXT.__swift_as_entry: 0x210
+  __TEXT.__swift_as_ret: 0x290
+  __TEXT.__swift_as_cont: 0x598
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2228
-  __TEXT.__eh_frame: 0x6560
+  __TEXT.__unwind_info: 0x2260
+  __TEXT.__eh_frame: 0x6640
   __DATA_CONST.__const: 0x3438
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__auth_got: 0xfe0
-  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__auth_got: 0xff0
+  __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x5e0
   __DATA.__objc_const: 0x1a30
-  __DATA.__objc_selrefs: 0x628
-  __DATA.__objc_data: 0xa48
+  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_data: 0xa50
   __DATA.__data: 0x1c80
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1902
-  Symbols:   871
-  CStrings:  764
+  Functions: 1910
+  Symbols:   874
+  CStrings:  769
 
Symbols:
+ _$s13HomeKitEvents0abC5ErrorO18accountUnavailableyA2CmFWC
+ _$s13HomeKitEvents13ConfigurationC19isAcceptedEventDate_3now15acceptedOffsetsSb10Foundation0H0V_AISNySdGSgtFZ
+ _$s13HomeKitEvents13ConfigurationC24acceptedEventDateOffsetsSNySdGvgZ
+ _$s13HomeKitEvents18EncryptionKeyQueryV8database14homeIdentifier011targetCloudB4Zone05queryI012resultsLimit16qualityOfServiceAcA21DatabaseConfigurationO_10Foundation4UUIDVAA0T0C06TargetkbL0OANSiSgSo09NSQualityqR0VSgtcfC
- _$s13HomeKitEvents18EncryptionKeyQueryV8database14homeIdentifier011targetCloudB4Zone05queryI012resultsLimit12dateInterval16qualityOfServiceAcA21DatabaseConfigurationO_10Foundation4UUIDVAA0V0C06TargetkbL0OAOSiSgAM04DateQ0VSgSo09NSQualitysT0VSgtcfC
CStrings:
+ "CloudKit account is restricted, not accepting events"
+ "Dropped %{public}ld event(s) dated %{public}fs...%{public}fs from now, outside the accepted range %{public}fs...%{public}fs"
+ "Dropping event dated %{public}fs from now, outside the accepted range %{public}fs...%{public}fs"
+ "MainDriver unexpectedly nil when checking whether events can be accepted"
+ "cloudKitLoggedInState"
+ "removeObserver:name:object:"
- "isCloudKitLoggedIn"
```

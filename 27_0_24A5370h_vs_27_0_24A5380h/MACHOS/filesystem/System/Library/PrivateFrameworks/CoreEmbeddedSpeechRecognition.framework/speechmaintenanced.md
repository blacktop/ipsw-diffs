## speechmaintenanced

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/speechmaintenanced`

```diff

-  __TEXT.__text: 0x3d848
-  __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__text: 0x3ee2c
+  __TEXT.__auth_stubs: 0x1780
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x260
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x82b
-  __TEXT.__const: 0xbf8
+  __TEXT.__const: 0xc00
   __TEXT.__objc_classname: 0x2c7
-  __TEXT.__objc_methname: 0xde1
+  __TEXT.__objc_methname: 0xdf1
   __TEXT.__objc_methtype: 0x331
   __TEXT.__swift5_fieldmd: 0x4c8
-  __TEXT.__constg_swiftt: 0x4d0
+  __TEXT.__constg_swiftt: 0x4d8
   __TEXT.__swift5_reflstr: 0x67c
-  __TEXT.__swift5_capture: 0x40c
-  __TEXT.__oslogstring: 0x224e
+  __TEXT.__swift5_capture: 0x470
+  __TEXT.__oslogstring: 0x247e
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x44
-  __TEXT.__swift_as_entry: 0x98
-  __TEXT.__swift_as_ret: 0xb4
-  __TEXT.__swift_as_cont: 0x150
-  __TEXT.__cstring: 0x3d5
-  __TEXT.__unwind_info: 0xa10
-  __TEXT.__eh_frame: 0x20e0
-  __DATA_CONST.__const: 0xf58
+  __TEXT.__swift_as_entry: 0x9c
+  __TEXT.__swift_as_ret: 0xb8
+  __TEXT.__swift_as_cont: 0x154
+  __TEXT.__cstring: 0x3b5
+  __TEXT.__unwind_info: 0xa20
+  __TEXT.__eh_frame: 0x2140
+  __DATA_CONST.__const: 0xfa8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x1c0
   __DATA.__objc_const: 0xc30
-  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_selrefs: 0x368
   __DATA.__objc_data: 0xb0
   __DATA.__data: 0xd80
   __DATA.__bss: 0x580

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 638
-  Symbols:   547
-  CStrings:  366
+  Functions: 644
+  Symbols:   545
+  CStrings:  375
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _$s10Foundation6LocaleV10identifierACSS_tcfC
+ _$s10Foundation6LocaleVMa
+ _$s6Speech12NCBVQProfileC12isCompatible25withCurrentAssetForLocaleSb10Foundation0I0V_tKFTj
+ _SFDeviceSupportsIFP
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _os_transaction_create
+ _swift_retain_x28
- _$sSS18_fromUTF8RepairingySS6result_Sb11repairsMadetSRys5UInt8VGFZ
- _$sSSSTsWP
- _$sSSs25LosslessStringConvertiblesWP
- _$sSSySSxcs25LosslessStringConvertibleRzSTRzSJ7ElementSTRtzlufC
- _$sSa28_allocateBufferUninitialized15minimumCapacitys06_ArrayB0VyxGSi_tFZ
- _$ss4Int8VN
- _confstr
- _realpath$DARWIN_EXTSN
- _swift_retain_x9
- _swift_willThrowTypedImpl
CStrings:
+ "%s entity allocation cancelled."
+ "Allocation was cancelled."
+ "Asset has changed since last NCBVQ profile build; triggering full rebuild."
+ "Failed to check asset compatibility, defaulting to full rebuild: %@"
+ "Failed to perform daily NCBVQ profile maintenance: %@"
+ "Full NCBVQ profile rebuild skipped: device does not support IFP."
+ "Full NCBVQ profile rebuild skipped: feature flag is disabled."
+ "Ranking was cancelled."
+ "Task cancelled before entity tagger build. Skipping ASR and NL tagger configuration."
+ "com.apple.siri.bg_system_task.daily-ncbvq-profile-maintenance"
+ "ncbvqCascadeSetChangeListener"
+ "temporaryDirectory"
- "Sandbox: confstr(_CS_DARWIN_USER_TEMP_DIR) failed"
- "cascadeSetChangeListener"
- "com.apple.speechmaintenanced"

```

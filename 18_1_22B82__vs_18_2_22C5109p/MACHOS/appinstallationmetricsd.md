## appinstallationmetricsd

> `/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd`

```diff

-2.1.10.0.0
-  __TEXT.__text: 0x2b4e0
-  __TEXT.__auth_stubs: 0x1540
+2.2.4.0.0
+  __TEXT.__text: 0x28b10
+  __TEXT.__auth_stubs: 0x1420
   __TEXT.__objc_methlist: 0xd0
-  __TEXT.__const: 0x1304
+  __TEXT.__const: 0x12e4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x1061
-  __TEXT.__constg_swiftt: 0x848
-  __TEXT.__swift5_typeref: 0x85b
-  __TEXT.__swift5_reflstr: 0x3e9
-  __TEXT.__swift5_fieldmd: 0x560
+  __TEXT.__cstring: 0xf71
+  __TEXT.__constg_swiftt: 0x810
+  __TEXT.__swift5_typeref: 0x819
+  __TEXT.__swift5_reflstr: 0x3d9
+  __TEXT.__swift5_fieldmd: 0x554
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__objc_methname: 0x8e8
-  __TEXT.__oslogstring: 0x980
+  __TEXT.__objc_methname: 0x8c1
+  __TEXT.__oslogstring: 0x9b0
   __TEXT.__swift5_proto: 0xd8
   __TEXT.__swift5_types: 0x84
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0x1b4
-  __TEXT.__swift5_capture: 0x214
   __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_capture: 0x190
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0xb88
-  __TEXT.__eh_frame: 0x1ef0
-  __DATA_CONST.__auth_got: 0xaa0
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__auth_ptr: 0x410
-  __DATA_CONST.__const: 0x1368
+  __TEXT.__unwind_info: 0xae8
+  __TEXT.__eh_frame: 0x1c58
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__auth_ptr: 0x3f0
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1128
-  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_const: 0x1108
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0x3f8
-  __DATA.__data: 0x11a0
+  __DATA.__data: 0x10e0
   __DATA.__bss: 0x1a40
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 766
-  Symbols:   573
-  CStrings:  328
+  Functions: 732
+  Symbols:   547
+  CStrings:  319
 
Symbols:
+ _$s22AppInstallationMetrics0B5EventV10jwtGSTokenSSSgvg
+ _$s22AppInstallationMetrics0B5EventV7altDsid4dsid17billingStorefront8bundleID06clientK011countryCode12eventVersion4evid11installDate0R4Type6isBeta04itemK002osP08platform6source10storefront5token9webDomain010postTargetS07gsToken10jwtGSTokenACSSSg_s5Int64VSgAYS2SAYSSA0_10Foundation0S0VSSSbA0_S3SA3YA3_A2YtcfC
- _$s10Foundation19PropertyListDecoderC6decode_4fromxxm_AA4DataVtKSeRzlFTj
- _$s10Foundation19PropertyListDecoderCACycfc
- _$s10Foundation19PropertyListDecoderCMa
- _$s10Foundation19PropertyListEncoderC6encodeyAA4DataVxKSERzlFTj
- _$s10Foundation19PropertyListEncoderCACycfc
- _$s10Foundation19PropertyListEncoderCMa
- _$s10Foundation3URLV13DirectoryHintO13inferFromPathyA2EmFWC
- _$s10Foundation3URLV13DirectoryHintOMa
- _$s10Foundation3URLV4pathSSvg
- _$s10Foundation3URLV9appending9component13directoryHintACx_AC09DirectoryF0OtSyRzlF
- _$s10Foundation4DataV10contentsOf7optionsAcA3URLVh_So20NSDataReadingOptionsVtKcfC
- _$s10Foundation4DataV5write2to7optionsyAA3URLV_So20NSDataWritingOptionsVtKF
- _$s22AppInstallationMetrics0B5EventV7altDsid4dsid17billingStorefront8bundleID06clientK011countryCode12eventVersion4evid11installDate0R4Type6isBeta04itemK002osP08platform6source10storefront5token9webDomain010postTargetS07gsTokenACSSSg_s5Int64VSgAXS2SAXSSA_10Foundation0S0VSSSbA_S3SA3XA2_AXtcfC
- _$s22AppInstallationMetrics0B5EventVSEAAMc
- _$s22AppInstallationMetrics0B5EventVSeAAMc
- _$sBbWV
- _$sSSSysMc
- _$sSayxGSEsSERzlMc
- _$sSayxGSesSeRzlMc
- _OBJC_CLASS_$_NSUserDefaults
- _objc_retain_x27
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_task_isCurrentExecutor
- _swift_task_reportUnexpectedExecutor
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
CStrings:
+ "Clearing events no longer supported"
+ "Installation Events no longer supported"
+ "Post no longer supported"
+ "[%!@(MISSING)] Failed to generate an AMS metrics event"
+ "[%!@(MISSING)] GS lookup failed due to account lookup error: %!{(MISSING)public}@"
+ "[%!@(MISSING)] GS lookup failed due to missing account"
+ "[%!@(MISSING)] GS lookup failed due to missing accountID"
+ "[%!@(MISSING)] GS lookup failed while getting grandSlamJWT token due to error: %!{(MISSING)public}@"
+ "[%!@(MISSING)]GS lookup failed while getting grandSlam token due to error: %!{(MISSING)public}@"
+ "[DailyWakeupTask] Wakeup flush complete"
+ "com.apple.gs.ctf.metering"
+ "piu-config/include-gsToken"
- "AppInstallationMetricsDaemon/InstallationEventManager.swift"
- "Clearing events"
- "Division by zero"
- "Division results in an overflow"
- "Failed to load ledger from url: %!{(MISSING)private}s error: %!{(MISSING)public}@"
- "Get installation events"
- "Loading installation events"
- "Loading installation events from: %!{(MISSING)private}s"
- "Swift/IntegerTypes.swift"
- "UnsafeMutablePointer.initialize with negative count"
- "[%!@(MISSING)] Failed to clear installation events due to error: %!{(MISSING)public}@"
- "[%!@(MISSING)] Failed to record installation event due to error: %!{(MISSING)public}@"
- "[%!@(MISSING)] Saving installation events to: %!{(MISSING)private}s"
- "[%!@(MISSING)] Skipping immediate post of event for: %!{(MISSING)public}s"
- "[DailyWakeupTask] Flush complete"
- "events"
- "fileExistsAtPath:"
- "post complete"
- "skipImmediatePosting"
- "standardUserDefaults"

```

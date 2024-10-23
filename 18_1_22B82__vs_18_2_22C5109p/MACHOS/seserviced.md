## seserviced

> `/usr/libexec/seserviced`

```diff

-51.11.0.0.0
-  __TEXT.__text: 0x359ca0
-  __TEXT.__auth_stubs: 0x3990
-  __TEXT.__objc_stubs: 0x8ba0
-  __TEXT.__objc_methlist: 0x40f8
-  __TEXT.__const: 0x9380
-  __TEXT.__gcc_except_tab: 0x29dc
-  __TEXT.__objc_methname: 0x11dc1
-  __TEXT.__oslogstring: 0x1527f
-  __TEXT.__cstring: 0x2c3d1
-  __TEXT.__objc_classname: 0x118c
-  __TEXT.__objc_methtype: 0x6053
-  __TEXT.__swift5_typeref: 0x3ae6
+52.6.2.0.0
+  __TEXT.__text: 0x35c894
+  __TEXT.__auth_stubs: 0x39f0
+  __TEXT.__objc_stubs: 0x8bc0
+  __TEXT.__objc_methlist: 0x4120
+  __TEXT.__const: 0x93c0
+  __TEXT.__gcc_except_tab: 0x2a08
+  __TEXT.__objc_methname: 0x11e63
+  __TEXT.__oslogstring: 0x1535f
+  __TEXT.__cstring: 0x2c4c8
+  __TEXT.__objc_classname: 0x1189
+  __TEXT.__objc_methtype: 0x609d
+  __TEXT.__swift5_typeref: 0x3aac
   __TEXT.__constg_swiftt: 0x3c98
-  __TEXT.__swift5_reflstr: 0x3eea
-  __TEXT.__swift5_fieldmd: 0x40c4
+  __TEXT.__swift5_reflstr: 0x3efa
+  __TEXT.__swift5_fieldmd: 0x40dc
   __TEXT.__swift5_builtin: 0x2bc
   __TEXT.__swift5_assocty: 0x588
-  __TEXT.__swift5_capture: 0x2080
+  __TEXT.__swift5_capture: 0x1e78
   __TEXT.__swift5_proto: 0x64c
   __TEXT.__swift5_types: 0x41c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__unwind_info: 0x84f8
-  __TEXT.__eh_frame: 0xfdfc
-  __DATA_CONST.__auth_got: 0x1cd8
-  __DATA_CONST.__got: 0xfb8
-  __DATA_CONST.__auth_ptr: 0xb60
-  __DATA_CONST.__const: 0xf230
-  __DATA_CONST.__cfstring: 0x11ae0
+  __TEXT.__unwind_info: 0x8548
+  __TEXT.__eh_frame: 0xfecc
+  __DATA_CONST.__auth_got: 0x1d08
+  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__auth_ptr: 0xb78
+  __DATA_CONST.__const: 0xf0e0
+  __DATA_CONST.__cfstring: 0x11b20
   __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x408

   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x8d0
-  __DATA.__objc_const: 0x18468
-  __DATA.__objc_selrefs: 0x36d0
-  __DATA.__objc_ivar: 0xbf8
+  __DATA.__objc_const: 0x184e8
+  __DATA.__objc_selrefs: 0x36d8
+  __DATA.__objc_ivar: 0xbfc
   __DATA.__objc_data: 0x6150
-  __DATA.__data: 0xa078
+  __DATA.__data: 0xa088
   __DATA.__bss: 0xb898
   __DATA.__common: 0x58a
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10133
-  Symbols:   1594
-  CStrings:  9905
+  Functions: 10132
+  Symbols:   1602
+  CStrings:  9916
 
Symbols:
+ _$s9SEService13StateInternalO6lockedyACSayAA012InstanceInfoC0CG_tcACmFWC
+ _$s9SEService20InstanceInfoInternalC11instanceAID07packageF006moduleF0014securityDomainF00ij3KeyC014lifeCycleStateAC10Foundation4DataV_A4LSgALtcfCTj
+ _$s9SEService20InstanceInfoInternalC14LifeCycleStateV11descriptionSSvg
+ _$s9SEService20InstanceInfoInternalC14LifeCycleStateV4fromAE10Foundation4DataV_tcfC
+ _$s9SEService20InstanceInfoInternalC14LifeCycleStateV6lockedAEvgZ
+ _$s9SEService20InstanceInfoInternalC14LifeCycleStateVMa
+ _$s9SEService20InstanceInfoInternalC14LifeCycleStateVs10SetAlgebraAAMc
+ _$s9SEService20InstanceInfoInternalC14lifeCycleState10Foundation4DataVvg
+ _$s9SEService20InstanceInfoInternalC32instanceLifeCycleStateTerminateds5UInt8VvgZ
+ _$ss10SetAlgebraP10isSuperset2ofSbx_tFTj
+ _PRGetChipInfoAsync
- _$s8Dispatch1poiyAA0A4TimeVAD_AA0aB8IntervalOtF
- _$s9SEService20InstanceInfoInternalC11instanceAID07packageF006moduleF0014securityDomainF00ij3KeyC014lifeCycleStateAC10Foundation4DataV_A5LtcfCTj
- _PRGetChipInfo
CStrings:
+ "00001111-2222-3333-4444-55556666FFF8"
+ "00001111-2222-3333-4444-55556666FFF9"
+ "AID %!s(MISSING) lifecycle %!s(MISSING)"
+ "Computing %!l(MISSING)d scan rules"
+ "Couldn't retrieve SEID?"
+ "Credential %!s(MISSING) transitioned into locked state"
+ "FailedProximityChipQuery"
+ "Failure retrieving proximity chip information"
+ "Getting SE for reason %!{(MISSING)public}@ with token %!{(MISSING)public}@"
+ "Got SE (w/ token) for %!{(MISSING)public}@"
+ "Got SE (w/ transceiver) for %!@(MISSING)"
+ "Got tokened SE session for %!{(MISSING)public}@ - success %!{(MISSING)public}d error %!{(MISSING)public}@"
+ "KeyServiceAvailable proxy %!{(MISSING)public}d token %!{(MISSING)public}d"
+ "LyonBLE is not running, updateBLEConfigStatus called"
+ "LyonExpress is already running"
+ "LyonExpress is not running"
+ "LyonPower is already running"
+ "LyonUWB isRunning: %!{(MISSING)bool}d or could not cast as LyonPeer"
+ "Queuing SE request with transceiver %!{(MISSING)public}d handoffToken %!{(MISSING)public}d for %!{(MISSING)public}@"
+ "Retrieving proximity chip information"
+ "SLAMInstallFTAExtLocked"
+ "SLAMInstallPersonalizeLockDummy9"
+ "Tokened session for %!{(MISSING)public}@ finished, releasing session"
+ "UWB sessionID is not cached, cannot pause ranging"
+ "Unable to get SecureElementInfo"
+ "Vv48@0:8@\"NSData\"16@\"NSNumber\"24@\"NSData\"32@?<v@?@\"NSError\">40"
+ "_onDealloc"
+ "_session"
+ "cacheProximityChipData:completion:"
+ "designateKey:designation:handoffToken:completion:"
+ "getSecureElementWithReason:handoffToken:completion:"
+ "iOS (18.2) - SecureElementService-52.6.2"
+ "isProduction"
+ "keyOperation:handoffToken:keyData:reason:reply:"
+ "keyServiceAvailable:handoffToken:reason:reply:"
+ "legacyKeyServiceAvailable proxy %!{(MISSING)public}d"
+ "maxBTScanRules"
+ "setDesignation:designation:handoffToken:completion:"
+ "v16@?0@\"PRChipInfo\"8"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"<SecureElementTransceiver>\"@\"NSError\">32"
+ "v48@0:8@16q24@32@?40"
- "\x01)"
- "@\"NearFieldManager\""
- "Computing %!l(MISSING)d scan filters"
- "Created new peripheral for %!s(MISSING)"
- "Deleting existing peripheral %!s(MISSING) with tags %!s(MISSING) for %!s(MISSING)"
- "Failed to create peripheral for %!s(MISSING)"
- "Failed to retrieve SEID during init %!{(MISSING)public}@"
- "Failed to retrieve proximity chip type %!l(MISSING)d information missing %!d(MISSING)"
- "Got SE for %!@(MISSING)"
- "Got SEID %!{(MISSING)public}d error %!{(MISSING)public}@"
- "INVALIDATE_CARKEY_DEVICE"
- "Ignoring scan filters due to max exceeded %!l(MISSING)d"
- "Lyon onConnection"
- "Missing SEID"
- "Missing SEID -> retrying"
- "Queuing SE request with transceiver %!{(MISSING)public}d for %!{(MISSING)public}@"
- "Started ranging when device is not in correct state? %!s(MISSING)"
- "Vv40@0:8@\"NSData\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "We should have cached the sessionID while parsing M1"
- "_manager"
- "cacheProximityChipData"
- "cacheProximityChipData:"
- "designateKey:designation:completion:"
- "embedded"
- "getInformation"
- "getTags"
- "iOS (18.1) - SecureElementService-51.11"
- "maxBTScanFilters"
- "setDesignation:designation:completion:"
- "v40@0:8@16q24@?32"

```

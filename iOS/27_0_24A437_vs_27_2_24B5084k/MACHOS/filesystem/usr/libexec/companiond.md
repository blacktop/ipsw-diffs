## companiond

> `/usr/libexec/companiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__cstring`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-524.0.56.0.0
-  __TEXT.__text: 0x860e4
-  __TEXT.__auth_stubs: 0x2d70
-  __TEXT.__objc_stubs: 0x43e0
+524.10.88.0.0
+  __TEXT.__text: 0x85c58
+  __TEXT.__auth_stubs: 0x2d40
+  __TEXT.__objc_stubs: 0x4460
   __TEXT.__objc_methlist: 0x2b60
-  __TEXT.__objc_methname: 0x6155
+  __TEXT.__objc_methname: 0x61a5
   __TEXT.__swift5_typeref: 0xcbb
   __TEXT.__swift5_fieldmd: 0x820
   __TEXT.__objc_classname: 0xb48
-  __TEXT.__objc_methtype: 0x1588
-  __TEXT.__const: 0x20b6
+  __TEXT.__objc_methtype: 0x159b
+  __TEXT.__const: 0x20d6
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_reflstr: 0x832
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift_as_cont: 0x3a8
   __TEXT.__oslogstring: 0x4142
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x1ab0
+  __TEXT.__gcc_except_tab: 0x1ad0
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x26e8
-  __TEXT.__eh_frame: 0x4ed0
-  __DATA_CONST.__const: 0x2560
-  __DATA_CONST.__cfstring: 0x1b80
+  __TEXT.__unwind_info: 0x2b40
+  __TEXT.__eh_frame: 0x4eb8
+  __DATA_CONST.__const: 0x2538
+  __DATA_CONST.__cfstring: 0x1ba0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x16c8
-  __DATA_CONST.__got: 0xd08
-  __DATA_CONST.__auth_ptr: 0x558
-  __DATA.__objc_const: 0x7548
-  __DATA.__objc_selrefs: 0x1540
-  __DATA.__objc_ivar: 0x410
+  __DATA_CONST.__auth_got: 0x16b0
+  __DATA_CONST.__got: 0xd00
+  __DATA_CONST.__auth_ptr: 0x560
+  __DATA.__objc_const: 0x7568
+  __DATA.__objc_selrefs: 0x1560
+  __DATA.__objc_ivar: 0x414
   __DATA.__objc_data: 0x18e0
   __DATA.__data: 0x1e10
   __DATA.__common: 0xe8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
-  Functions: 2296
-  Symbols:   1273
-  CStrings:  1950
+  Functions: 2295
+  Symbols:   1270
+  CStrings:  1956
 
Symbols:
+ _$s12FindMyLocate12ClientTargetVMa
+ _$s12FindMyLocate12ClientTargetVMn
+ _$s12FindMyLocate13RequestOriginV_12clientTargetAcA06ClientE0O_AA0hG0VSgtcfC
+ _$s14CoreUtilsSwift15CUEventReporterP20eventMonitorCanceled2idys6UInt64V_tFTq
+ _$s14CoreUtilsSwift15CUEventReporterPAAE20eventMonitorCanceled2idys6UInt64V_tF
+ _$s17CompanionServices32CPSResponderUseCaseConfigurationV09responderF009requesterF0ACSgAA012CPSRequesterdeF0V_tFZ
+ _$s18AppIntentsServices0bC0O15localDispatcher11clientLabel6source11environment7optionsAA0A17IntentDispatching_pSS_So24LNTranscriptActionSourceVAA0aK11Environment_pAC14OptionsBuilderVy_AC0eQ0VGdtFZ
+ _OBJC_CLASS_$_CUXPCSubscriber
- _$s12FindMyLocate13RequestOriginVyAcA06ClientE0OcfC
- _$s17CompanionServices32CPSRequesterUseCaseConfigurationV0dE0OSHAAMc
- _$s17CompanionServices32CPSResponderUseCaseConfigurationV8useCasesSDyAA012CPSRequesterdeF0V0dE0OACGvgZ
- _$s18AppIntentsServices0bC0O14InterfaceIdiomO23defaultForCurrentDeviceAESgvgZ
- _$s18AppIntentsServices0bC0O14InterfaceIdiomOMn
- _$s18AppIntentsServices0bC0O14PayloadPrivacyO7defaultyA2EmFWC
- _$s18AppIntentsServices0bC0O14PayloadPrivacyOMa
- _$s18AppIntentsServices0bC0O15localDispatcher11clientLabel6source11environment7optionsAA0A17IntentDispatching_pSS_So24LNTranscriptActionSourceVAA0aK11Environment_pAC0E7OptionsVtFZ
- _$s18AppIntentsServices0bC0O17DispatcherOptionsV14interfaceIdiom14payloadPrivacyAeC09InterfaceG0OSg_AC07PayloadI0OtcfC
- _$s18AppIntentsServices0bC0O17DispatcherOptionsVMa
- _$sSH13_rawHashValue4seedS2i_tFTj
CStrings:
+ "@\"CUXPCSubscriber\""
+ "_xpcSubscriber"
+ "initWithStreamName:dispatchQueue:mock:"
+ "setEventHandler:"
+ "start"
+ "stop"
```

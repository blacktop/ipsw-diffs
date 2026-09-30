## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2005.0.13.0.0
-  __TEXT.__text: 0x37e24
+2005.0.31.0.0
+  __TEXT.__text: 0x38038
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x3938
-  __TEXT.__const: 0x2d4
+  __TEXT.__objc_methlist: 0x3958
+  __TEXT.__const: 0x2e4
   __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__cstring: 0x19f7
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2aef
+  __TEXT.__oslogstring: 0x2b30
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1370
+  __TEXT.__unwind_info: 0x1378
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xa7e
-  __TEXT.__objc_methname: 0x734a
-  __TEXT.__objc_methtype: 0x1db7
-  __TEXT.__objc_stubs: 0x4d20
+  __TEXT.__objc_methname: 0x7399
+  __TEXT.__objc_methtype: 0x1dc8
+  __TEXT.__objc_stubs: 0x4d60
   __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x1d18
+  __DATA_CONST.__const: 0x1cd0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce8
+  __DATA_CONST.__objc_selrefs: 0x1d00
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x568
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x19e0
   __AUTH_CONST.__objc_const: 0x8b58
-  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_intobj: 0x210
   __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0xc48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: 38745A15-ED4D-32B0-86C8-6894FC01A63F
-  Functions: 1519
-  Symbols:   5441
-  CStrings:  2329
+  UUID: 8D832CC3-299F-3899-B6A1-48F895186BC2
+  Functions: 1522
+  Symbols:   5440
+  CStrings:  2334
 
Symbols:
+ -[LAContext evaluateBoolOption:options:property:]
+ -[LAContext optionRedactErrors]
+ -[LAContext setOptionRedactErrors:]
+ ___36-[LAContext credentialOfType:reply:]_block_invoke.93
+ ___36-[LAContext credentialOfType:reply:]_block_invoke.93.cold.1
+ ___55-[LAContext _setCredential:type:options:log:cid:reply:]_block_invoke.92
+ ___66-[LAContext setCredential:forProcessedEvent:credentialType:reply:]_block_invoke.84
+ ___block_descriptor_76_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_84_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.89
+ ___block_literal_global.97
+ _objc_msgSend$evaluateBoolOption:options:property:
+ _objc_msgSend$optionRedactErrors
- ___36-[LAContext credentialOfType:reply:]_block_invoke.91
- ___36-[LAContext credentialOfType:reply:]_block_invoke.91.cold.1
- ___55-[LAContext _setCredential:type:options:log:cid:reply:]_block_invoke.90
- ___66-[LAContext setCredential:forProcessedEvent:credentialType:reply:]_block_invoke.82
- ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_68_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_68_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.87
- ___block_literal_global.93
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_LocalAuthentication
CStrings:
+ "B40@0:8q16@24@32"
+ "Discrepancy between option %d value (%d) and property value (%d)"
+ "evaluateBoolOption:options:property:"
+ "optionRedactErrors"
+ "setOptionRedactErrors:"

```

## rtcreportingd

> `/usr/libexec/rtcreportingd`

```diff

-142.9.0.0.0
-  __TEXT.__text: 0x6f120
-  __TEXT.__auth_stubs: 0x2170
+160.1.0.0.0
+  __TEXT.__text: 0x67ccc
+  __TEXT.__auth_stubs: 0x20d0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x48e2
-  __TEXT.__cstring: 0x25f7
-  __TEXT.__constg_swiftt: 0x166c
-  __TEXT.__swift5_typeref: 0x11a4
-  __TEXT.__swift5_reflstr: 0xe55
-  __TEXT.__swift5_fieldmd: 0x1a14
-  __TEXT.__objc_methname: 0x585
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0x1a0
+  __TEXT.__const: 0x3ef2
+  __TEXT.__cstring: 0x24c7
+  __TEXT.__constg_swiftt: 0x1508
+  __TEXT.__swift5_typeref: 0xfca
+  __TEXT.__swift5_reflstr: 0xd15
+  __TEXT.__swift5_fieldmd: 0x16f4
+  __TEXT.__objc_methname: 0x4ff
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0x158
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_proto: 0x398
-  __TEXT.__swift5_types: 0x1c4
+  __TEXT.__swift5_proto: 0x310
+  __TEXT.__swift5_types: 0x198
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift_as_entry: 0x18c
-  __TEXT.__swift_as_ret: 0x1d0
-  __TEXT.__oslogstring: 0x1a16
-  __TEXT.__swift5_capture: 0x2fc
-  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x1c8
+  __TEXT.__oslogstring: 0x19a6
+  __TEXT.__swift5_capture: 0x2e4
+  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x22f8
-  __TEXT.__eh_frame: 0x6120
-  __DATA_CONST.__auth_got: 0x10b8
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__auth_ptr: 0x530
-  __DATA_CONST.__const: 0x3cb0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x2130
+  __TEXT.__eh_frame: 0x5e48
+  __DATA_CONST.__auth_got: 0x1068
+  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__auth_ptr: 0x510
+  __DATA_CONST.__const: 0x3528
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1b88
-  __DATA.__objc_selrefs: 0x208
+  __DATA.__objc_const: 0x1a30
+  __DATA.__objc_selrefs: 0x1d8
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x2a10
-  __DATA.__bss: 0x6500
-  __DATA.__common: 0x1f0
+  __DATA.__data: 0x2810
+  __DATA.__bss: 0x5480
+  __DATA.__common: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DE6EFDDF-33B8-3380-972B-DEF14394154B
-  Functions: 2942
-  Symbols:   812
-  CStrings:  475
+  UUID: A764620D-D05C-35B4-89BF-24278B9D5F9A
+  Functions: 2707
+  Symbols:   800
+  CStrings:  451
 
Symbols:
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
- _$s10Foundation4UUIDV19_bridgeToObjectiveCSo6NSUUIDCyF
- _$sSD10FoundationE26_forceBridgeFromObjectiveC_6resultySo12NSDictionaryC_SDyxq_GSgztFZ
- _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
- _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
- _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
- _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
- _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
- _$ss22KeyedDecodingContainerV6decode_6forKeys4Int8VAFm_xtKF
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSObject
- _objc_release_x9
- _swift_dynamicCastObjCClassUnconditional
- _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ "hierarchySessionID"
+ "parentSessionID"
- "TTR rule \"%{public}s\" processed event with status: %{bool,public}d"
- "_TtC13rtcreportingd10BackendTTR"
- "b64_jsc"
- "decision_server_url"
- "frameworkObj"
- "handleEvent:sender:ruleConfig:withReplyBlock:"
- "hierarchyID"
- "initWithBool:"
- "initWithChar:"
- "initWithDouble:"
- "initWithLongLong:"
- "initWithUnsignedLongLong:"
- "library"
- "local TTR backend for "
- "radar_component_id"
- "radar_keyword_ids"
- "radar_title"
- "required_libraries"
- "rule"
- "rules"
- "running TTR rule \"%{public}s\""
- "sender"
- "shared value does not conform to any expected type"
- "v12@?0B8"
- "var"
- "version"

```

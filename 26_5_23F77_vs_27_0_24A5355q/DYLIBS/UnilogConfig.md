## UnilogConfig

> `/System/Library/PrivateFrameworks/UnilogConfig.framework/UnilogConfig`

```diff

-6.7.0.0.0
-  __TEXT.__text: 0xf6e8
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__const: 0x1358
-  __TEXT.__swift5_typeref: 0x42a
-  __TEXT.__swift5_fieldmd: 0x248
-  __TEXT.__constg_swiftt: 0x51c
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift_as_entry: 0x6c
-  __TEXT.__swift_as_ret: 0x78
-  __TEXT.__cstring: 0x239
-  __TEXT.__swift5_reflstr: 0xbe
+7.5.0.0.0
+  __TEXT.__text: 0x12304
+  __TEXT.__const: 0x1598
+  __TEXT.__swift5_typeref: 0x50c
+  __TEXT.__swift5_fieldmd: 0x2b4
+  __TEXT.__constg_swiftt: 0x594
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift_as_entry: 0x80
+  __TEXT.__swift_as_ret: 0x8c
+  __TEXT.__swift_as_cont: 0xd0
+  __TEXT.__cstring: 0x269
+  __TEXT.__swift5_reflstr: 0x10e
   __TEXT.__swift5_assocty: 0x38
-  __TEXT.__swift5_proto: 0xf4
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_types: 0x44
   __TEXT.__swift5_acfuncs: 0x78
   __TEXT.__oslogstring: 0x40
-  __TEXT.__unwind_info: 0x668
-  __TEXT.__eh_frame: 0x10c8
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x24
-  __TEXT.__objc_methtype: 0x1
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__eh_frame: 0x13f8
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x558
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x618
   __AUTH_CONST.__objc_const: 0x140
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x290
-  __DATA.__data: 0x588
+  __AUTH.__data: 0x328
+  __DATA.__data: 0x6a8
   __DATA.__common: 0x10
-  __DATA.__bss: 0x1e80
+  __DATA.__bss: 0x2180
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite
   - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/UnilogCommonLibrary
+  - /System/Library/PrivateFrameworks/UnilogPlatformLibrary.framework/UnilogPlatformLibrary
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E066C518-589B-3E30-9124-030F980EEB95
-  Functions: 575
-  Symbols:   505
-  CStrings:  20
+  UUID: B9B4A832-019E-3811-B73B-754E91FB2389
+  Functions: 647
+  Symbols:   558
+  CStrings:  15
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_memcpy8_8
+ __swiftEmptyDictionarySingleton
+ _associated conformance 12UnilogConfig0B12ManagerErrorO10Foundation09LocalizedD0AAs0D0
+ _associated conformance 21UnilogPlatformLibrary7VersionVSL0A6ConfigSQ
+ _swift_arrayInitWithCopy
+ _swift_getTupleTypeMetadata3
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x21
+ _swift_retain_x22
+ _symbolic $s12UnilogConfig07ManagedB5AssetP
+ _symbolic SS______t 12UnilogConfig015SchemaRedactionB0O
+ _symbolic Shy_____G 8Dendrite12ProtoTagPathV
+ _symbolic _____ 12UnilogConfig015SchemaRedactionB0O
+ _symbolic _____ 12UnilogConfig0B12ManagerErrorO
+ _symbolic _____ 21UnilogPlatformLibrary7VersionV
+ _symbolic _____Sg 21UnilogPlatformLibrary13MessageConfigV
+ _symbolic _____Sg 21UnilogPlatformLibrary13MessageConfigV0E5UnionO
+ _symbolic ___________ypXmTt 12UnilogConfig12AssetRequestV 10Foundation4DataV
+ _symbolic ___________ypXpt 12UnilogConfig12AssetRequestV 10Foundation4DataV
+ _symbolic _____ySS_____G s17_NativeDictionaryV 12UnilogConfig015SchemaRedactionD0O
+ _symbolic _____ySS_____G s18_DictionaryStorageC 12UnilogConfig015SchemaRedactionD0O
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 12UnilogConfig015SchemaRedactionE0O
+ _symbolic _____y_____G 12UnilogConfig14VersionedAssetV 10Foundation4DataV
+ _symbolic ypXmT
+ _type_layout_string 12UnilogConfig015SchemaRedactionB0O
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_67
CStrings:
+ "$s12UnilogConfig01$B15ServiceProtocolC11getURLAsset3forAA13AssetResponseOy10Foundation3URLVGAA0H7RequestV_tYaKFTE"
+ "$s12UnilogConfig01$B15ServiceProtocolC12getDataAsset3forAA0G8ResponseOy10Foundation0F0VGAA0G7RequestV_tYaKFTE"
+ "getDataAsset(for:)"
+ "getURLAsset(for:)"
+ "lastMileRedactionConfig"
- "$defaultActor"
- "$s12UnilogConfig01$B15ServiceProtocolC11getAssetURL3forAA0F8ResponseOy10Foundation0G0VGAA0F7RequestV_tYaKFTE"
- "$s12UnilogConfig01$B15ServiceProtocolC12getAssetData3forAA0F8ResponseOy10Foundation0G0VGAA0F7RequestV_tYaKFTE"
- "_TtC12UnilogConfig13ConfigManager"
- "_TtC12UnilogConfig22$ConfigServiceProtocol"
- "actorSystem"
- "getAssetData(for:)"
- "getAssetURL(for:)"
- "id"
- "logger"

```

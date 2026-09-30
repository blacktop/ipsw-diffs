## StreamingAppleTrace

> `/System/Library/PrivateFrameworks/StreamingAppleTrace.framework/Versions/A/StreamingAppleTrace`

```diff

-  __TEXT.__text: 0x25764
+  __TEXT.__text: 0x29328
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x1ac0
-  __TEXT.__constg_swiftt: 0xa08
-  __TEXT.__swift5_typeref: 0x6d4
-  __TEXT.__swift5_fieldmd: 0x808
+  __TEXT.__const: 0x1ca0
+  __TEXT.__constg_swiftt: 0xac0
+  __TEXT.__swift5_typeref: 0x7be
+  __TEXT.__swift5_fieldmd: 0x890
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x46b
-  __TEXT.__swift5_types: 0x94
+  __TEXT.__swift5_reflstr: 0x4b0
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__cstring: 0x5ad
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x13c
+  __TEXT.__swift5_proto: 0x14c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x224
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_capture: 0x22c
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift_as_cont: 0x5c
-  __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x980
-  __TEXT.__eh_frame: 0x17e8
+  __TEXT.__swift_as_cont: 0x54
+  __TEXT.__oslogstring: 0x40
+  __TEXT.__unwind_info: 0xa30
+  __TEXT.__eh_frame: 0x1890
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x120
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1748
-  __AUTH_CONST.__objc_const: 0xcb8
-  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__const: 0x1830
+  __AUTH_CONST.__objc_const: 0xcd8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH.__objc_data: 0x2a8
-  __AUTH.__data: 0xb38
-  __DATA.__data: 0x4f0
-  __DATA.__bss: 0x2400
+  __AUTH.__data: 0xbd8
+  __DATA.__data: 0x5f0
+  __DATA.__bss: 0x2590
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 728
-  Symbols:   417
-  CStrings:  71
+  Functions: 785
+  Symbols:   450
+  CStrings:  72
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy48_8
+ __os_log_impl
+ __swift_closure_destructor.101Tm
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 19StreamingAppleTrace13AgentInstanceVSHAASQ
+ _associated conformance 19StreamingAppleTrace13FrameMetadataV6StreamVSHAASQ
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _os_log_type_enabled
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getGenericMetadata
+ _swift_getKeyPath
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s19StreamingAppleTrace20FrameHandlerDelegateP
+ _symbolic SDy__________G 19StreamingAppleTrace13FrameMetadataV6StreamV s6UInt64V
+ _symbolic Ss
+ _symbolic Ss_S2st
+ _symbolic _____ 19StreamingAppleTrace12FrameHandlerV
+ _symbolic _____ 19StreamingAppleTrace13FrameMetadataV6StreamV
+ _symbolic _____ 19StreamingAppleTrace27LoggingFrameHandlerDelegateV
+ _symbolic _____ s6UInt64V
+ _symbolic _____ySs_S2stG 17_StringProcessing5RegexV
+ _symbolic _____ySs_S2st_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_S2st_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____y_____G 19StreamingAppleTrace12FrameHandlerV AA07LoggingdE8DelegateV
+ _symbolic _____y_____GSg 19StreamingAppleTrace12FrameHandlerV AA07LoggingdE8DelegateV
+ _symbolic _____y_____Gz_Xx 19StreamingAppleTrace12FrameHandlerV AA07LoggingdE8DelegateV
+ _symbolic _____y__________G s18_DictionaryStorageC 19StreamingAppleTrace13FrameMetadataV6StreamV s6UInt64V
+ _symbolic x
+ _type_layout_string 19StreamingAppleTrace13FrameMetadataV6StreamV
- __swift_closure_destructor.89Tm
CStrings:
+ "/^traceportr(\\d+)p(\\d+)$/"
+ "Trace loss [frame: %llu, expected: %llu] for %s"
- "Record(platform="

```

## SpeechTranslation

> `/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x24cc4
+365.8.0.0.0
+  __TEXT.__text: 0x254b0
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__objc_methlist: 0x1254
   __TEXT.__const: 0x6dc
   __TEXT.__cstring: 0xaaa
-  __TEXT.__oslogstring: 0x2605
+  __TEXT.__oslogstring: 0x2615
   __TEXT.__gcc_except_tab: 0x340
   __TEXT.__constg_swiftt: 0x340
   __TEXT.__swift5_typeref: 0x43f

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xa68
   __TEXT.__eh_frame: 0xa20
   __TEXT.__objc_classname: 0x451
-  __TEXT.__objc_methname: 0x2c03
+  __TEXT.__objc_methname: 0x2c83
   __TEXT.__objc_methtype: 0xb4b
-  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_stubs: 0x2340
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f0
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x5b8
   __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x22a8
+  __AUTH_CONST.__objc_const: 0x22e8
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x5b8
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x920
+  __DATA.__data: 0x930
   __DATA.__bss: 0x320
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5065772E-C992-39A0-9B6E-1ACE11DCC545
-  Functions: 761
-  Symbols:   1726
-  CStrings:  834
+  UUID: 909A62A7-0874-3416-A105-91E0E50ABE8D
+  Functions: 773
+  Symbols:   1739
+  CStrings:  841
 
Symbols:
+ -[_STSELFLoggingSession sessionID]
+ -[_STSpeechTranslatorClientList setLoggingSessionID:]
+ GCC_except_table16
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table9
+ __PROTOCOLS_STTranscriptionResult.18
+ __PROTOCOLS_STTranslationResult.22
+ ___53-[_STSpeechTranslatorClientList setLoggingSessionID:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ _keypath_get_selector_logIdentifier
+ _objc_msgSend$logIdentifier
+ _objc_msgSend$sessionID
+ _objc_msgSend$setLogIdentifier:
+ _objc_msgSend$setLoggingSessionID:
+ _objectdestroy.48Tm
- GCC_except_table20
- __PROTOCOLS_STTranscriptionResult.16
- __PROTOCOLS_STTranslationResult.20
- _objectdestroy.46Tm
CStrings:
+ "T@\"NSUUID\",N,C"
+ "T@\"NSUUID\",R,N,V_sessionID"
+ "_logIdentifier"
+ "client: %{public}@ received producedTranslation: %{sensitive}@, delegate: %p responds: %{BOOL}d"
+ "clientList: %{public}@ received callback producedSpeechResult: %{sensitive}@"
+ "clientList: %{public}@ received callback producedTranslationResult: %{sensitive}@"
+ "logIdentifier"
+ "sessionID"
+ "setLogIdentifier:"
+ "setLoggingSessionID:"
- "client: %{public}@ received producedTranslation: %{public}@, delegate: %p responds: %{BOOL}d"
- "clientList: %{public}@ received callback producedSpeechResult: %{public}@"
- "clientList: %{public}@ received callback producedTranslationResult: %{public}@"

```

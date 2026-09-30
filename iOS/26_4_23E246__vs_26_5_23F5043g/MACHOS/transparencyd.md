## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1547.100.136.0.0
-  __TEXT.__text: 0x2d5190
-  __TEXT.__auth_stubs: 0x3750
-  __TEXT.__objc_stubs: 0x1dbc0
+1547.120.12.0.0
+  __TEXT.__text: 0x2e1dfc
+  __TEXT.__auth_stubs: 0x37d0
+  __TEXT.__objc_stubs: 0x1dba0
   __TEXT.__objc_methlist: 0x15920
-  __TEXT.__cstring: 0x111b3
+  __TEXT.__cstring: 0x113b3
   __TEXT.__objc_classname: 0x3e64
   __TEXT.__objc_methname: 0x24f32
-  __TEXT.__const: 0x10608
+  __TEXT.__const: 0x114b8
   __TEXT.__gcc_except_tab: 0x51d4
-  __TEXT.__oslogstring: 0x12108
+  __TEXT.__oslogstring: 0x122a8
   __TEXT.__objc_methtype: 0x82f1
-  __TEXT.__swift5_typeref: 0x3826
+  __TEXT.__swift5_typeref: 0x3990
   __TEXT.__swift5_capture: 0x1690
-  __TEXT.__constg_swiftt: 0x4728
-  __TEXT.__swift5_reflstr: 0x249e
-  __TEXT.__swift5_fieldmd: 0x366c
-  __TEXT.__swift5_proto: 0xb28
-  __TEXT.__swift5_types: 0x374
-  __TEXT.__swift5_assocty: 0x618
+  __TEXT.__constg_swiftt: 0x48a4
+  __TEXT.__swift5_reflstr: 0x263e
+  __TEXT.__swift5_fieldmd: 0x38e4
+  __TEXT.__swift5_proto: 0xbf0
+  __TEXT.__swift5_types: 0x394
+  __TEXT.__swift5_assocty: 0x660
   __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0x1d8
   __TEXT.__swift_as_ret: 0x188
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xb9f8
-  __TEXT.__eh_frame: 0x7cd8
-  __DATA_CONST.__auth_got: 0x1bb8
+  __TEXT.__unwind_info: 0xbce8
+  __TEXT.__eh_frame: 0x80a0
+  __DATA_CONST.__auth_got: 0x1bf8
   __DATA_CONST.__got: 0x1128
-  __DATA_CONST.__auth_ptr: 0x988
-  __DATA_CONST.__const: 0x18520
+  __DATA_CONST.__auth_ptr: 0x998
+  __DATA_CONST.__const: 0x186f0
   __DATA_CONST.__cfstring: 0xe380
   __DATA_CONST.__objc_classlist: 0xd60
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_arraydata: 0x1b8
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x318b0
+  __DATA.__objc_const: 0x318d0
   __DATA.__objc_selrefs: 0x88e0
   __DATA.__objc_ivar: 0x1128
   __DATA.__objc_data: 0x9eb0
-  __DATA.__data: 0xcfa0
+  __DATA.__data: 0xd540
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x17780
-  __DATA.__common: 0x8b8
+  __DATA.__bss: 0x19130
+  __DATA.__common: 0x978
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D5DD77CC-3AD8-3E4A-9BA8-FD10C6DB0E30
-  Functions: 18352
-  Symbols:   1653
-  CStrings:  13766
+  UUID: 90BD8AE2-DF91-384A-BF24-3751C4E57415
+  Functions: 18667
+  Symbols:   1662
+  CStrings:  13789
 
Symbols:
+ _$s16CoreTransparency11CTConfigBagV06deviceD0AA014CTDeviceClientD0Vvg
+ _$s16CoreTransparency17CTDeviceClientBagV12ckvRestQuerySSvg
+ _$s16CoreTransparency17CTDeviceClientBagV17ckvRestBatchQuerySSvg
+ _$s16CoreTransparency17CTDeviceClientBagV17ckvRestPublicKeysSSvg
+ _$s16CoreTransparency17CTDeviceClientBagV20ckvRestReportToAppleSSvg
+ _$s16CoreTransparency17CTDeviceClientBagV23ckvRestConsistencyProofSSvg
+ _$s16CoreTransparency17CTDeviceClientBagV32ckvRestRevisionLogInclusionProofSSvg
+ _$s16CoreTransparency17CTDeviceClientBagVMa
+ _$s16CoreTransparency23DeviceClientBagProtocolP16dtRestPublicKeysSSvgTq
+ _$s16CoreTransparency23DeviceClientBagProtocolP22dtRestConsistencyProofSSvgTq
+ _$s16CoreTransparency23DeviceClientBagProtocolP23dtRestLogInclusionProofSSvgTq
- _$s10Foundation11JSONDecoderCMn
- _$s10Foundation11JSONEncoderCMn
CStrings:
+ "AetEventsRequest"
+ "AetEventsRequest.LogRevision"
+ "AetEventsResponse"
+ "AetEventsResponse.LogConsistencyResponse"
+ "AetInsertRequest"
+ "AetInsertResponse"
+ "Failed to decode config bag from source %s: %@"
+ "Failed to fetch fresh config bag: %@ [%s]"
+ "Failed to read config bag from disk: %@ [%s]"
+ "Failed to verify new config bag from source %s: %@ [%s]"
+ "Failed to write new config bag to disk: %@ [%s]"
+ "Found issues with new config bag from source %s: %s [%s]"
+ "Validated and updated config bag from source %s. [%s]"
+ "Validated new config bag from source %s which expires in %fms. Need to check bag values. [%s]"
+ "_dtRestConsistencyProof"
+ "_dtRestLogInclusionProof"
+ "_dtRestPublicKeys"
+ "ckvRestBatchQuery is empty"
+ "ckvRestConsistencyProof is empty"
+ "ckvRestPublicKeys is empty"
+ "ckvRestReportToApple is empty"
+ "ckvRestRevisionLogInclusionProof is empty"
+ "com.apple.transparency.ConfigBagManagerError.Source"
+ "fileSystem"
+ "inMemory"
+ "source description "
- "Validated and updated new config bag which expires in %fms [%s]"
- "jsonDecoder"
- "jsonEncoder"

```

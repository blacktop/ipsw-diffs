## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation`

```diff

-  __TEXT.__text: 0x38dc0
+  __TEXT.__text: 0x38df4
   __TEXT.__objc_methlist: 0x2ae4
   __TEXT.__const: 0x23a
-  __TEXT.__cstring: 0x50bd
+  __TEXT.__cstring: 0x50dd
   __TEXT.__oslogstring: 0x350d
   __TEXT.__gcc_except_tab: 0xe44
   __TEXT.__dlopen_cstrs: 0x2d4

   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x18f8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_arraydata: 0x13f8
+  __DATA_CONST.__objc_arraydata: 0x1408
   __DATA_CONST.__got: 0x388
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x59e0
+  __AUTH_CONST.__cfstring: 0x5a00
   __AUTH_CONST.__objc_const: 0x6d30
-  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__auth_got: 0x650

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1276
-  Symbols:   3392
-  CStrings:  1800
+  Functions: 1275
+  Symbols:   3391
+  CStrings:  1802
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
- _BMServiceDomainOverrideLookupFromConfigurationForSet
Functions:
~ -[BMAccessControlPolicy allowsAccessToStream:withMode:] : 696 -> 708
~ -[BMAccessControlPolicy allowsAccessToDatabase:withMode:] : 240 -> 244
~ -[BMAccessControlPolicy allowsAccessToView:withMode:] : 240 -> 244
~ -[BMAccessControlPolicy allowsAccessToSet:withMode:] : 616 -> 636
~ -[BMAccessControlPolicy allowsAccessToAllSetsWithMode:] : 188 -> 200
~ -[BMAccessControlPolicy allowsComputePublisherAccessToStreams:] : 656 -> 672
~ -[BMAccessControlPolicy allowsComputeSourceAccessToStream:] : 328 -> 344
~ -[BMAccessControlPolicy allowsAccessToClientCompute:] : 228 -> 236
~ +[BMAccessControlPolicy process:canActOnBehalfOfProcess:] : 320 -> 352
~ -[BMAccessControlPolicy(WriteService) allowsConnectionToWriteService] : 252 -> 264
~ -[BMAccessControlPolicy(WriteService) allowsAccessToWriteServiceForStream:ofUser:] : 232 -> 240
~ -[BMAccessControlPolicy(DaemonToAgent) allowsAccessToBiomeAgentForUser:] : 588 -> 600
- _BMServiceDomainOverrideLookupFromConfigurationForSet
+ _BMResourceDescriptorsLookupFromConfigurationForSet
- _BMResourceSyncPolicyLookupFromConfigurationForSet
CStrings:
+ "com.apple.intelligencetasksd"

```

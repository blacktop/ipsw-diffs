## BiomeStreams

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams`

```diff

-200.1.0.0.0
-  __TEXT.__text: 0x40f364
+200.4.0.2.0
+  __TEXT.__text: 0x40fa9c
   __TEXT.__auth_stubs: 0x23f0
   __TEXT.__objc_methlist: 0x15124
   __TEXT.__const: 0xabf84
-  __TEXT.__cstring: 0x35119
-  __TEXT.__gcc_except_tab: 0x14d8
-  __TEXT.__oslogstring: 0xbae0
+  __TEXT.__cstring: 0x35169
+  __TEXT.__gcc_except_tab: 0x1520
+  __TEXT.__oslogstring: 0xbce0
   __TEXT.__dlopen_cstrs: 0x632
   __TEXT.__constg_swiftt: 0xb2b8
   __TEXT.__swift5_typeref: 0x55b2

   __TEXT.__swift5_types: 0x844
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0xc2a8
+  __TEXT.__unwind_info: 0xc2b8
   __TEXT.__eh_frame: 0xde80
   __TEXT.__objc_classname: 0x26cd
-  __TEXT.__objc_methname: 0x1cf75
-  __TEXT.__objc_methtype: 0x3c99
-  __TEXT.__objc_stubs: 0x117c0
+  __TEXT.__objc_methname: 0x1cfa5
+  __TEXT.__objc_methtype: 0x3c9c
+  __TEXT.__objc_stubs: 0x117e0
   __DATA_CONST.__got: 0x10a8
   __DATA_CONST.__const: 0x2a7f8
   __DATA_CONST.__objc_classlist: 0xea0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6060
+  __DATA_CONST.__objc_selrefs: 0x6068
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x990
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x1208
-  __AUTH_CONST.__const: 0x12b10
+  __AUTH_CONST.__const: 0x12b50
   __AUTH_CONST.__cfstring: 0x90e0
   __AUTH_CONST.__objc_const: 0x4de88
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EBF3EF05-4DA7-3C3B-BE5D-D44C3AFF7298
-  Functions: 21841
-  Symbols:   74839
-  CStrings:  16590
+  UUID: 7F581FBC-6703-3789-90F0-0B4DA77A6095
+  Functions: 21845
+  Symbols:   74852
+  CStrings:  16602
 
Symbols:
+ +[BMDaemon(Pruning) pruneRestrictedStreamsInDomain:account:activity:protectionClass:]
+ +[BMDaemon(Pruning) pruneRestrictedStreamsInDomain:account:activity:protectionClass:].cold.1
+ +[BMDaemon(Pruning) pruneRestrictedStreamsWithActivity:protectionClass:]
+ ___33+[BMDaemon registerXPCActivities]_block_invoke.66
+ ___33+[BMDaemon registerXPCActivities]_block_invoke.71
+ ___33+[BMDaemon registerXPCActivities]_block_invoke.75
+ ___33+[BMDaemon registerXPCActivities]_block_invoke_2.69
+ ___33+[BMDaemon registerXPCActivities]_block_invoke_2.74
+ ___33+[BMDaemon registerXPCActivities]_block_invoke_2.76
+ ___block_literal_global.68
+ ___block_literal_global.73
+ ___block_literal_global.80
+ _objc_msgSend$protectionClass
+ _objc_msgSend$pruneRestrictedStreamsInDomain:account:activity:protectionClass:
+ _objc_msgSend$pruneRestrictedStreamsWithActivity:protectionClass:
- +[BMDaemon(Pruning) pruneRestrictedStreamsInDomain:account:activity:]
- +[BMDaemon(Pruning) pruneRestrictedStreamsInDomain:account:activity:].cold.1
- +[BMDaemon(Pruning) pruneRestrictedStreamsWithActivity:]
- ___33+[BMDaemon registerXPCActivities]_block_invoke.65
- ___33+[BMDaemon registerXPCActivities]_block_invoke_2.66
- ___block_literal_global.70
- _objc_msgSend$pruneRestrictedStreamsInDomain:account:activity:
- _objc_msgSend$pruneRestrictedStreamsWithActivity:
CStrings:
+ "Ignoring %@ since it is class %tu and we are pruning A or B"
+ "Ignoring %@ since it is class %tu which is handled by a separate job"
+ "Ignoring %@ since it is not a library stream and we are pruning class A or B"
+ "Pruning library stream: %{public}@"
+ "Pruning non-library stream: %{public}@"
+ "Started pruning restricted streams in directory: %{public}@ protectionClass: %tu"
+ "com.apple.biome.prune-expired-events.A"
+ "com.apple.biome.prune-expired-events.B"
+ "com.apple.biome.prune-expired-events.C"
+ "protectionClass"
+ "pruneRestrictedStreamsInDomain:account:activity:protectionClass:"
+ "pruneRestrictedStreamsWithActivity:protectionClass:"
+ "running activity \"com.apple.biome.prune-expired-events.A\""
+ "running activity \"com.apple.biome.prune-expired-events.B\""
+ "running activity \"com.apple.biome.prune-expired-events.C\""
+ "v48@0:8Q16@24@32Q40"
- "Started pruning restricted streams in directory: %{public}@"
- "com.apple.biome.prune-expired-events"
- "pruneRestrictedStreamsInDomain:account:activity:"
- "pruneRestrictedStreamsWithActivity:"
- "running activity \"com.apple.biome.prune-expired-events\""
- "v40@0:8Q16@24@32"

```

## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.60.20.0.0
-  __TEXT.__text: 0x4b2b8
+1547.80.7.0.0
+  __TEXT.__text: 0x4b09c
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x446c
+  __TEXT.__objc_methlist: 0x4484
   __TEXT.__cstring: 0x27fe
   __TEXT.__const: 0x12c0
   __TEXT.__gcc_except_tab: 0x508
-  __TEXT.__oslogstring: 0x1bbd
+  __TEXT.__oslogstring: 0x1bc7
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__constg_swiftt: 0x2f0
   __TEXT.__swift5_reflstr: 0x4e9

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x19b8
+  __TEXT.__unwind_info: 0x19a8
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_classname: 0x724
-  __TEXT.__objc_methname: 0x75ef
-  __TEXT.__objc_methtype: 0x1f31
-  __TEXT.__objc_stubs: 0x5a00
+  __TEXT.__objc_methname: 0x7644
+  __TEXT.__objc_methtype: 0x1f3e
+  __TEXT.__objc_stubs: 0x5a20
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1548
+  __DATA_CONST.__const: 0x1570
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e08
+  __DATA_CONST.__objc_selrefs: 0x1e18
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x2800
+  __AUTH_CONST.__const: 0x27e0
   __AUTH_CONST.__cfstring: 0x38c0
   __AUTH_CONST.__objc_const: 0x75a8
   __AUTH_CONST.__objc_intobj: 0x1b0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 3D51488E-7F7C-329B-B097-7598110D72D0
-  Functions: 2491
-  Symbols:   6747
-  CStrings:  2777
+  UUID: 6922A9FE-F5E0-3FA0-8B33-B6973241331D
+  Functions: 2489
+  Symbols:   6744
+  CStrings:  2779
 
Symbols:
+ -[TransparencyDaemon ktQuery:application:queryOptions:complete:]
+ -[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]
+ -[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.667
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.674
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.cold.1
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke_2
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.652
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.cold.1
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.654
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.661
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.671
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.664
+ ___block_descriptor_64_e8_32s40s48s56bs_e46_v24?0"<transparencyd_protocol>"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.670
+ _objc_msgSend$networkKTQuery:application:traceUUID:complete:
+ _objc_msgSend$validateURIs:queryOptions:traceUUID:complete:
- -[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.670
- ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke
- ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.677
- ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.cold.1
- ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke_2
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.652
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.cold.1
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.654
- ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.664
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.661
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.cold.1
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke_2
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.674
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.667
- ___block_literal_global.669
- ___block_literal_global.676
- _objc_msgSend$validateURIs:queryOptions:complete:
CStrings:
+ "Sending validateURIs:queryOptions:traceUUID:complete:"
+ "ktQuery:application:queryOptions:complete:"
+ "networkKTQuery:application:traceUUID:complete:"
+ "v48@0:8@\"NSDictionary\"16@\"KTQueryOptions\"24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "validateURIs:queryOptions:traceUUID:complete:"
- "Sending validateURIs:queryOptions:complete:"
- "networkKTQuery:application:trace:timeout:complete:"
- "v40@0:8@\"NSDictionary\"16@\"KTQueryOptions\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"

```

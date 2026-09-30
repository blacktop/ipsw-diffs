## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.0.17.0.2
-  __TEXT.__text: 0x40958
+737.0.29.0.2
+  __TEXT.__text: 0x40d98
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x4a24
+  __TEXT.__objc_methlist: 0x4a54
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0xde0
-  __TEXT.__oslogstring: 0x3092
-  __TEXT.__cstring: 0x42ef
+  __TEXT.__gcc_except_tab: 0xd74
+  __TEXT.__oslogstring: 0x30db
+  __TEXT.__cstring: 0x432f
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x1320
+  __TEXT.__unwind_info: 0x12f8
   __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_classname: 0x8e7
-  __TEXT.__objc_methname: 0x9a6c
+  __TEXT.__objc_classname: 0x8e9
+  __TEXT.__objc_methname: 0x9af2
   __TEXT.__objc_methtype: 0x32db
-  __TEXT.__objc_stubs: 0x5720
+  __TEXT.__objc_stubs: 0x57a0
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1360
+  __DATA_CONST.__const: 0x13b0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2490
+  __DATA_CONST.__objc_selrefs: 0x24b0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x7e90
+  __AUTH_CONST.__cfstring: 0x2340
+  __AUTH_CONST.__objc_const: 0x7f20
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1040
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x498
+  __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0xf48
   __DATA.__bss: 0x320
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 114AC186-A5EB-3F7F-876F-C4AC79259104
-  Functions: 2001
-  Symbols:   6360
-  CStrings:  3327
+  UUID: 8D8AFCB2-94C4-3842-B0F1-0035742D51B1
+  Functions: 2012
+  Symbols:   6386
+  CStrings:  3341
 
Symbols:
+ -[FSMessageConnection queue]
+ -[FSMessageConnection(Private) completedLocked:replyHandler:]
+ -[FSMessageConnection(Private) connect:].cold.4
+ -[FSModuleIdentity teamID]
+ -[FSModuleVolume useMetaDataIO]
+ GCC_except_table24
+ GCC_except_table5
+ GCC_except_table61
+ GCC_except_table90
+ _OBJC_IVAR_$_FSMessageConnection._queue
+ _OBJC_IVAR_$_FSModuleIdentity._teamID
+ _OBJC_IVAR_$_FSModuleVolume._useMetaDataIO
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.427
+ ___40-[FSMessageConnection(Private) connect:]_block_invoke.78
+ ___40-[FSMessageConnection(Private) connect:]_block_invoke.78.cold.1
+ ___40-[FSMessageConnection(Private) connect:]_block_invoke_3
+ ___44-[FSMessageConnection getLocalizationSetup:]_block_invoke_2
+ ___44-[FSMessageConnection getLocalizationSetup:]_block_invoke_2.cold.1
+ ___52-[FSMessageConnection(Private) prompt:replyHandler:]_block_invoke_2
+ ___52-[FSMessageConnection(Private) prompt:replyHandler:]_block_invoke_2.cold.1
+ ___52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke.407
+ ___53-[FSAgentClientDelegate instanceExited:instanceUUID:]_block_invoke
+ ___57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.418
+ ___61-[FSMessageConnection(Private) completedLocked:replyHandler:]_block_invoke
+ ___61-[FSMessageConnection(Private) completedLocked:replyHandler:]_block_invoke.80
+ ___61-[FSMessageConnection(Private) completedLocked:replyHandler:]_block_invoke.cold.1
+ ___61-[FSMessageConnection(Private) promptTrueFalse:replyHandler:]_block_invoke_2
+ ___61-[FSMessageConnection(Private) promptTrueFalse:replyHandler:]_block_invoke_2.cold.1
+ ___63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.413
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.403
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_2.404
+ ___67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke.410
+ ___71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke.298
+ ___71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke.301
+ ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke.408
+ ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.416
+ ___73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke.409
+ ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.396
+ ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.397
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.394
+ ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.406
+ ___82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.405
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.414
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.415
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.422
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s104l8s88l8s96l8
+ ___block_descriptor_56_e8_32s40r48r_e42_v32?0"NSLocale"8"NSArray"16"NSError"24lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.77
+ _objc_msgSend$completedLocked:replyHandler:
+ _objc_msgSend$queue
+ _objc_msgSend$teamIdentifier
+ _objc_msgSend$useMetaDataIO
- GCC_except_table22
- GCC_except_table30
- GCC_except_table33
- GCC_except_table74
- GCC_except_table89
- ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.423
- ___40-[FSMessageConnection(Private) connect:]_block_invoke.73
- ___40-[FSMessageConnection(Private) connect:]_block_invoke.73.cold.1
- ___44-[FSMessageConnection getLocalizationSetup:]_block_invoke.cold.1
- ___52-[FSMessageConnection(Private) prompt:replyHandler:]_block_invoke.cold.1
- ___52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke.403
- ___55-[FSMessageConnection(Private) completed:replyHandler:]_block_invoke.75
- ___55-[FSMessageConnection(Private) completed:replyHandler:]_block_invoke.cold.1
- ___57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.414
- ___61-[FSMessageConnection(Private) promptTrueFalse:replyHandler:]_block_invoke.cold.1
- ___63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.409
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.395
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_2.400
- ___67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke.406
- ___71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke.294
- ___71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke.297
- ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke.404
- ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.412
- ___73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke.405
- ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.392
- ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.393
- ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.390
- ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.402
- ___82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.401
- ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.410
- ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.411
- ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.418
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104bs112r_e5_v8?0ls32l8s40l8r112l8s48l8s56l8s64l8s72l8s80l8s104l8s88l8s96l8
- ___block_descriptor_48_e8_32r40r_e42_v32?0"NSLocale"8"NSArray"16"NSError"24lr32l8r40l8
- ___block_literal_global.71
CStrings:
+ "%s: Volume has KOIO and metadata IO disabled."
+ "%s: getLocalizationSetup didn't reply after 10seconds"
+ "MIteam"
+ "T@\"NSString\",R,V_teamID"
+ "TB,R,V_useMetaDataIO"
+ "_teamID"
+ "_useMetaDataIO"
+ "checkWithOptions: encountered on connect error!"
+ "com.apple.fskit.fsmessageconnection"
+ "com.apple.fskit3p."
+ "completedLocked:replyHandler:"
+ "teamID"
+ "teamIdentifier"
+ "useMetaDataIO"
- "%s: Volume has KOIO disabled."
- "checkWithOptions: encountered connect error!"

```

## StoreBookkeeperClient

> `/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient`

```diff

-4025.100.105.0.0
-  __TEXT.__text: 0x2824
-  __TEXT.__auth_stubs: 0x250
+4025.500.37.0.0
+  __TEXT.__text: 0x2a10
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_methlist: 0x690
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__cstring: 0x2f5
   __TEXT.__oslogstring: 0x2f9
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x148
   __TEXT.__objc_classname: 0x1b0
   __TEXT.__objc_methname: 0x1152
   __TEXT.__objc_methtype: 0x30d

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0xd18
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24720D30-88A5-39C0-BB72-E9AC99B493A1
+  UUID: 96789BA7-5740-3A7F-93F8-5BCBC32237D3
   Functions: 99
-  Symbols:   475
+  Symbols:   469
   CStrings:  311
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ ___73-[SBCPlaybackPositionService pushPlaybackPositionEntity:completionBlock:]_block_invoke : 444 -> 448
~ ___73-[SBCPlaybackPositionService pullPlaybackPositionEntity:completionBlock:]_block_invoke : 444 -> 448
~ -[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:] : 300 -> 308
~ ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke : 564 -> 568
~ ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke.7 : 88 -> 92
~ -[SBCPlaybackPositionService synchronizeImmediatelyWithCompletionHandler:] : 216 -> 236
~ -[SBCPlaybackPositionService updateForeignDatabaseWithValuesFromPlaybackPositionEntity:] : 124 -> 132
~ -[SBCPlaybackPositionService deletePlaybackPositionEntities] : 128 -> 140
~ -[SBCPlaybackPositionService deletePlaybackPositionEntity:] : 124 -> 132
~ ___89-[SBCPlaybackPositionService persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke : 368 -> 372
~ -[SBCPlaybackPositionEntity copyWithZone:] : 124 -> 120
~ -[SBCPlaybackPositionEntity initWithCoder:] : 408 -> 420
~ -[SBCPlaybackPositionEntity encodeWithCoder:] : 308 -> 316
~ -[SBCPlaybackPositionEntity iTunesCloudEntity] : 572 -> 608
~ _SBCPathWithScrubbedMount : 124 -> 136
~ ___46-[SBCPlaybackPositionEntity iTunesCloudEntity]_block_invoke : 176 -> 196
~ -[ICPlaybackPositionEntity(SBCPrivate) sbcEntity] : 708 -> 760
~ ___49-[ICPlaybackPositionEntity(SBCPrivate) sbcEntity]_block_invoke : 184 -> 204
~ -[SBCXPCService setXpcConnection:] : 12 -> 64
~ -[SBCXPCService initWithClientConfiguration:] : 148 -> 140
~ +[SBCXPCService XPCInterfaceDebugDescription] : 212 -> 236
~ +[SBCXPCService XPCServiceInterfaceClass] : 168 -> 180
~ +[SBCXPCServiceInterface serviceClientInterface] : 172 -> 184
~ +[SBCXPCServiceInterface serviceInterface] : 172 -> 184
~ +[SBCXPCServiceInterface serviceName] : 172 -> 184
~ +[SBCXPCServiceInterface newListener] : 72 -> 76
~ -[SBCXPCServiceInterface newServiceConnection] : 164 -> 176
~ -[SBCClientConfiguration initWithCoder:] : 84 -> 88
~ -[SBCClientConfiguration description] : 148 -> 156
~ -[SBCClientConfiguration initWithPlaybackPositionDomain:] : 116 -> 108
~ -[SBCPlaybackPositionDomain setUbiquitousDatabasePath:] : 12 -> 64
~ -[SBCPlaybackPositionDomain copyWithZone:] : 4 -> 40
~ -[SBCPlaybackPositionDomain initWithCoder:] : 208 -> 224
~ -[SBCPlaybackPositionDomain encodeWithCoder:] : 148 -> 156
~ -[SBCPlaybackPositionDomain description] : 240 -> 252

```

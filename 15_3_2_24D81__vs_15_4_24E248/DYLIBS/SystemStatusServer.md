## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Versions/A/SystemStatusServer`

```diff

-210.3.2.0.0
-  __TEXT.__text: 0xe7fc
+210.4.13.0.0
+  __TEXT.__text: 0xe820
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x70c
+  __TEXT.__objc_methlist: 0xa78
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x532
   __TEXT.__gcc_except_tab: 0x98

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x768
+  __DATA_CONST.__objc_selrefs: 0x7f8
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x850
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x1f70
+  __AUTH_CONST.__objc_const: 0x1968
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C72DC29-34C0-3049-BE30-29B85D9478C8
+  UUID: AD788F41-F4A5-381F-9B04-D21460C57DB7
   Functions: 275
   Symbols:   962
   CStrings:  507
Functions:
~ -[STStatusServer init] : 200 -> 208
~ -[STLocalStatusServer descriptionBuilderWithMultilinePrefix:] : 248 -> 244
~ ___122-[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:inDataChangeRecord:applyBlock:completion:]_block_invoke : 268 -> 284
~ ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke_2 : 196 -> 200
~ -[STAttributedEntityResolver resolveEntity:] : 5084 -> 5080
~ __STExecutableIdentityResolvedIdentityForIdentity : 1500 -> 1488
~ ___89-[STStatusDomainPublisherXPCClientHandle replaceDataChangeRecord:discardingOnExit:reply:]_block_invoke : 692 -> 696
~ ___105-[STStatusDomainPublisherXPCClientHandle publishData:forDomain:withChangeContext:discardingOnExit:reply:]_block_invoke : 456 -> 464
~ ___119-[STStatusDomainPublisherXPCClientHandle publishDiff:forDomain:withChangeContext:replacingData:discardingOnExit:reply:]_block_invoke : 928 -> 944

```

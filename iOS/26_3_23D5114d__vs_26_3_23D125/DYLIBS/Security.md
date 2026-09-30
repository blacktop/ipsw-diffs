## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61901.80.24.0.0
-  __TEXT.__text: 0x17c578
+61901.80.25.0.0
+  __TEXT.__text: 0x17c57c
   __TEXT.__auth_stubs: 0x4000
   __TEXT.__delay_helper: 0x340
   __TEXT.__objc_methlist: 0x6304

   __TEXT.__dof_security_: 0x325
   __TEXT.__unwind_info: 0x5ff8
   __TEXT.__objc_classname: 0xb0f
-  __TEXT.__objc_methname: 0xc145
+  __TEXT.__objc_methname: 0xc131
   __TEXT.__objc_methtype: 0x371e
   __TEXT.__objc_stubs: 0x8e20
   __DATA_CONST.__got: 0x788

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4E2E5319-4917-35B8-8A8C-D6B62424F002
+  UUID: 1BF94A50-C9C2-38B8-B0CE-EF932B04F2F8
   Functions: 6990
   Symbols:   20760
   CStrings:  11192
Symbols:
+ -[OTControl clearCliqueFromAccount:resetReason:isDBRv2:reply:]
+ -[OTControl performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:]
+ -[OTControl resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:]
+ ___136-[OTControl resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:]_block_invoke
+ ___62-[OTControl clearCliqueFromAccount:resetReason:isDBRv2:reply:]_block_invoke
+ ___83-[OTControl performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:]_block_invoke
+ _objc_msgSend$clearCliqueFromAccount:resetReason:isDBRv2:reply:
+ _objc_msgSend$performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:
+ _objc_msgSend$resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:
- -[OTControl clearCliqueFromAccount:resetReason:isGuitarfish:reply:]
- -[OTControl performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:]
- -[OTControl resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:]
- ___141-[OTControl resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:]_block_invoke
- ___67-[OTControl clearCliqueFromAccount:resetReason:isGuitarfish:reply:]_block_invoke
- ___88-[OTControl performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:]_block_invoke
- _objc_msgSend$clearCliqueFromAccount:resetReason:isGuitarfish:reply:
- _objc_msgSend$performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:
- _objc_msgSend$resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:
Functions:
~ +[OTClique resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:] : 5032 -> 5036
CStrings:
+ "clearCliqueFromAccount:resetReason:isDBRv2:reply:"
+ "performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:"
+ "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:"
+ "resetAndEstablish:resetReason:isDBRv2:accountIsW:reply:"
- "clearCliqueFromAccount:resetReason:isGuitarfish:reply:"
- "performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:"
- "resetAndEstablish:resetReason:isGuitarfish:accountIsW:reply:"

```

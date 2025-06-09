## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

```diff

-938.120.13.0.0
-  __TEXT.__text: 0xb220
+1045.0.1.0.1
+  __TEXT.__text: 0xb26c
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1426
-  __TEXT.__oslogstring: 0xbc7
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__cstring: 0x14ac
+  __TEXT.__oslogstring: 0xbf0
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__unwind_info: 0x330
   __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x920
+  __TEXT.__objc_methname: 0x97f
   __TEXT.__objc_methtype: 0x349
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x7f8
+  __TEXT.__objc_stubs: 0xa40
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0x658
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0xc0
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E29C41DF-137B-3636-ACBE-2EE1AE19769F
-  Functions: 249
-  Symbols:   862
-  CStrings:  472
+  UUID: F83F1753-B7B0-3374-A0F0-967EA5F6F1EB
+  Functions: 250
+  Symbols:   866
+  CStrings:  478
 
Symbols:
+ -[AMFIConnection removeTrustforTeamID:]
+ -[AMFIConnection setTrustForTeamID:withSignature:withSignType:]
+ GCC_except_table2
+ GCC_except_table4
+ GCC_except_table7
+ _AMFIProfileRemoveTeamIDTrust
+ _AMFIProfileRemoveTeamIDTrust.cold.1
+ _AMFIProfileRemoveTeamIDTrust.cold.2
+ _AMFIProfileRequiresReboot.cold.3
+ _AMFIProfileRequiresReboot.cold.4
+ _AMFIProfileSetTeamIDTrustWithOptions
+ _AMFIProfileSetTeamIDTrustWithOptions.cold.1
+ _AMFIProfileSetTeamIDTrustWithOptions.cold.2
+ _AMFIProfileSetTeamIDTrustWithOptions.cold.3
+ _AMFIProfileSetTeamIDTrustWithOptions.cold.4
+ _OBJC_CLASS_$_MISProfileDBClient
+ ___39-[AMFIConnection removeTrustforTeamID:]_block_invoke
+ ___39-[AMFIConnection removeTrustforTeamID:]_block_invoke.44
+ ___39-[AMFIConnection removeTrustforTeamID:]_block_invoke.cold.1
+ ___63-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke
+ ___63-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke.43
+ ___63-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke.cold.1
+ _iCloudForceHardeningEntitlements
+ _objc_msgSend$auxiliarySignatureWithTeamID:
+ _objc_msgSend$removeTrustforTeamID:
+ _objc_msgSend$removeTrustforTeamID:withReply:
+ _objc_msgSend$setTrustForTeamID:withSignature:withSignType:
+ _objc_msgSend$setTrustForTeamID:withSignature:withSignType:withReply:
+ _objc_msgSend$teamIDSupportsAuxiliarySignature:
+ _objc_msgSend$teamIDWithProfileUUID:
+ _tccForceHardeningEntitlements
- -[AMFIConnection removeTrustforUuid:]
- -[AMFIConnection setTrustForUuid:withSignature:withSignType:]
- GCC_except_table5
- _AMFIProfileRemoveTrust.cold.1
- _AMFIProfileRemoveTrust.cold.2
- _AMFIProfileSetTrustWithOptions.cold.1
- _AMFIProfileSetTrustWithOptions.cold.2
- _AMFIProfileSetTrustWithOptions.cold.3
- _AMFIProfileSetTrustWithOptions.cold.4
- ___37-[AMFIConnection removeTrustforUuid:]_block_invoke
- ___37-[AMFIConnection removeTrustforUuid:]_block_invoke.44
- ___37-[AMFIConnection removeTrustforUuid:]_block_invoke.cold.1
- ___61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke
- ___61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke.43
- ___61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke.cold.1
- __getProfileAuxiliarySignature
- __getProfileAuxiliarySignature.cold.1
- __getProfileAuxiliarySignature.cold.2
- _forceRuntimeAndLVEntitlements
- _objc_msgSend$removeTrustforUuid:
- _objc_msgSend$removeTrustforUuid:withReply:
- _objc_msgSend$setTrustForUuid:withSignature:withSignType:
- _objc_msgSend$setTrustForUuid:withSignature:withSignType:withReply:
CStrings:
+ "-[AMFIConnection removeTrustforTeamID:]_block_invoke"
+ "-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke"
+ "AMFIProfileRemoveTeamIDTrust"
+ "AMFIProfileSetTeamIDTrustWithOptions"
+ "[%s] attempting to remove trust for team ID: %@"
+ "[%s] attempting to set trust for team ID: %@ | %u"
+ "[%s] team ID must be provided"
+ "[%s] unable to remove trust for team ID: %@"
+ "[%s] unable to set trust for team ID: %@"
+ "_getTeamIDAuxiliarySignature"
+ "auxiliarySignatureWithTeamID:"
+ "com.apple.private.codesignkit.signer-source-host"
+ "com.apple.private.icloud-account-access"
+ "removeTrustforTeamID:"
+ "removeTrustforTeamID:withReply:"
+ "setTrustForTeamID:withSignature:withSignType:"
+ "setTrustForTeamID:withSignature:withSignType:withReply:"
+ "teamIDSupportsAuxiliarySignature:"
+ "teamIDWithProfileUUID:"
- "-[AMFIConnection removeTrustforUuid:]_block_invoke"
- "-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke"
- "AMFIProfileRemoveTrust"
- "AMFIProfileSetTrustWithOptions"
- "[%s] attempting to remove trust: %@"
- "[%s] attempting to set trust: %@ | %u"
- "[%s] unable to copy profile: %@ | %d"
- "[%s] unable to remove trust: %@"
- "[%s] unable to set trust: %@"
- "removeTrustforUuid:"
- "removeTrustforUuid:withReply:"
- "setTrustForUuid:withSignature:withSignType:"
- "setTrustForUuid:withSignature:withSignType:withReply:"

```

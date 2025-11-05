## CSExattrCrypto

> `/System/Library/PrivateFrameworks/CSExattrCrypto.framework/Versions/A/CSExattrCrypto`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x90e8
+2333.22.13.7.0
+  __TEXT.__text: 0x9090
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x2b8
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0xa59
+  __TEXT.__objc_methlist: 0x328
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0xa58
   __TEXT.__oslogstring: 0x19f
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methname: 0xcd8
   __TEXT.__objc_methtype: 0x4b8

   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__cfstring: 0x860
-  __AUTH_CONST.__objc_const: 0x408
+  __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41B567C5-DF77-3041-A3AC-A4B6D4ECC558
-  Functions: 168
-  Symbols:   625
+  UUID: D6626411-E618-35BE-A05A-79EE003C23A0
+  Functions: 176
+  Symbols:   635
   CStrings:  377
 
Symbols:
+ +[MDPrivateXattrServices defaultServices].cold.1
+ -[MDPrivateXattrServices extractDecryptedDataWith:cryptoCallback:decryptableXids:intoDict:keyRing:xid:].cold.1
+ -[MDPrivateXattrServices updatePrivateXattrParams:flags:forFileDescriptor:mergeCallback:completionHandler:].cold.1
+ -[_MDLabel _cfTypeID].cold.1
+ MDCopyDecodedXattrFromData.cold.1
+ MDLabelGetTypeID.cold.1
+ _MDItemSetPrivateAttributesForURL.cold.1
+ _MDPrivateXattrUUIDsGetter.cold.1
+ copyUpdatedData.cold.3
+ storePrivateMDAttributeData.cold.1
CStrings:
+ "ptr != ((void*)0)"
- "ptr != ((void *)0)"

```

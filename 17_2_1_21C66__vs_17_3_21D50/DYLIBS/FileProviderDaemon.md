## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-1703.62.4.0.0
-  __TEXT.__text: 0xb9f38
+1703.80.16.0.0
+  __TEXT.__text: 0xb9efc
   __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0x4a44
+  __TEXT.__objc_methlist: 0x4a5c
   __TEXT.__cstring: 0xae18
-  __TEXT.__oslogstring: 0xc062
+  __TEXT.__oslogstring: 0xc038
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0xbf0c
   __TEXT.__ustring: 0x1796
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x33f8
+  __TEXT.__unwind_info: 0x3408
   __TEXT.__objc_classname: 0x867
-  __TEXT.__objc_methname: 0x12aaf
-  __TEXT.__objc_methtype: 0x49c5
-  __TEXT.__objc_stubs: 0xcaa0
+  __TEXT.__objc_methname: 0x12b0b
+  __TEXT.__objc_methtype: 0x49d7
+  __TEXT.__objc_stubs: 0xcae0
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x34d0
   __DATA_CONST.__objc_classlist: 0x200

   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xef60
-  __DATA_CONST.__objc_selrefs: 0x3c00
+  __DATA_CONST.__objc_selrefs: 0x3c10
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__cfstring: 0x4c20
   __AUTH_CONST.__const: 0x9a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   Functions: 3815
-  Symbols:   12077
-  CStrings:  5238
+  Symbols:   12079
+  CStrings:  5240
 
Symbols:
+ -[FPDExtensionManager domainFromItemID:checkInvalidation:reason:]
+ -[FPDExtensionManager providerWithIdentifier:checkInvalidation:reason:]
+ ___block_literal_global.224
+ _objc_msgSend$domainFromItemID:checkInvalidation:reason:
+ _objc_msgSend$providerWithIdentifier:checkInvalidation:reason:
- ___40-[FPDProvider materializeRootForDomain:]_block_invoke.cold.1
- ___block_literal_global.221
CStrings:
+ "@36@0:8@16B24^Q28"
+ "[INFO] [Mat] Materialized root %{public}@ with error: %@"
+ "[INFO] [Mat] Will try to materialize root %{public}@"
+ "domainFromItemID:checkInvalidation:reason:"
+ "providerWithIdentifier:checkInvalidation:reason:"
- "[ERROR] [Mat] Tried to materialize nil root for domain %@"
- "[INFO] [Mat] Materialized root %@ with error: %@"
- "[INFO] [Mat] Will try to materialize root %@"

```

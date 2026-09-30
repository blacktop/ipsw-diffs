## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2424.0.0.0.0
-  __TEXT.__text: 0xf842c
+2425.0.0.0.0
+  __TEXT.__text: 0xf8558
   __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_methlist: 0xb164
+  __TEXT.__objc_methlist: 0xb17c
   __TEXT.__const: 0x13a4
-  __TEXT.__cstring: 0x17cc3
+  __TEXT.__cstring: 0x17c6c
   __TEXT.__oslogstring: 0x8f7c
   __TEXT.__gcc_except_tab: 0x10c4
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x3118
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1e05c
+  __TEXT.__objc_methname: 0x1e09f
   __TEXT.__objc_methtype: 0x236f
-  __TEXT.__objc_stubs: 0xdb60
+  __TEXT.__objc_stubs: 0xdbc0
   __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x4d30
+  __DATA_CONST.__const: 0x4d28
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ca8
+  __DATA_CONST.__objc_selrefs: 0x5cb8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0xbb8
-  __AUTH_CONST.__const: 0x2070
-  __AUTH_CONST.__cfstring: 0x192a0
+  __AUTH_CONST.__const: 0x2090
+  __AUTH_CONST.__cfstring: 0x19260
   __AUTH_CONST.__objc_const: 0xd6a8
   __AUTH_CONST.__objc_intobj: 0x420
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0x980
   __DATA.__data: 0xc20
-  __DATA.__bss: 0xc49
+  __DATA.__bss: 0xc59
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x208

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C8A2F94-FCCA-39A4-9426-E6D0AC2903E8
-  Functions: 5627
-  Symbols:   17336
-  CStrings:  12209
+  UUID: F8C277EA-C9E7-3F74-A122-56845650FA8C
+  Functions: 5631
+  Symbols:   17349
+  CStrings:  12207
 
Symbols:
+ +[MCRestrictionsPayload _ephemeralMultiUserOnlyKeysFilter]
+ +[MCRestrictionsPayload _ephemeralMultiUserOnlyKeysFilter].cold.1
+ -[NSMutableDictionary(MCUtilities) MCFilterOutRestrictionPayloadKeys:]
+ -[NSMutableDictionary(MCUtilities) _MCFilterRestrictionPayloadKeys:filterOut:]
+ GCC_except_table280
+ ___58+[MCRestrictionsPayload _ephemeralMultiUserOnlyKeysFilter]_block_invoke
+ ___78-[NSMutableDictionary(MCUtilities) _MCFilterRestrictionPayloadKeys:filterOut:]_block_invoke
+ ___block_descriptor_49_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_literal_global.564
+ ___block_literal_global.656
+ ___block_literal_global.673
+ ___block_literal_global.693
+ ___block_literal_global.742
+ ___block_literal_global.778
+ ___block_literal_global.783
+ ___block_literal_global.788
+ ___block_literal_global.793
+ ___block_literal_global.798
+ __ephemeralMultiUserOnlyKeysFilter.dict
+ __ephemeralMultiUserOnlyKeysFilter.onceToken
+ _objc_msgSend$MCFilterOutRestrictionPayloadKeys:
+ _objc_msgSend$_MCFilterRestrictionPayloadKeys:filterOut:
+ _objc_msgSend$_ephemeralMultiUserOnlyKeysFilter
- -[MCProfileConnection(Misc) isDeprecatedWebKitSynchronousXHRLoadsAllowed]
- GCC_except_table281
- _MCFeatureDeprecatedWebKitSynchronousXHRLoads
- ___67-[NSMutableDictionary(MCUtilities) MCFilterRestrictionPayloadKeys:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
- ___block_literal_global.559
- ___block_literal_global.654
- ___block_literal_global.671
- ___block_literal_global.691
- ___block_literal_global.740
- ___block_literal_global.775
- ___block_literal_global.780
- ___block_literal_global.785
- ___block_literal_global.790
- ___block_literal_global.795
CStrings:
+ "MCFilterOutRestrictionPayloadKeys:"
+ "_MCFilterRestrictionPayloadKeys:filterOut:"
+ "_ephemeralMultiUserOnlyKeysFilter"
- "FEATURE_WEBKIT_DEPRECATED_SYNCHRONOUSXHRLOADS"
- "allowDeprecatedWebKitSynchronousXHRLoads"
- "isDeprecatedWebKitSynchronousXHRLoadsAllowed"

```

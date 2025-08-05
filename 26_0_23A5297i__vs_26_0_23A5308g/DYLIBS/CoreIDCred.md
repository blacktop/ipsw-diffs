## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.40.1.0.0
-  __TEXT.__text: 0x48454
-  __TEXT.__auth_stubs: 0xdf0
+8.42.2.0.0
+  __TEXT.__text: 0x48a94
+  __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0x206c
-  __TEXT.__const: 0x3708
+  __TEXT.__const: 0x3778
   __TEXT.__cstring: 0x2046
   __TEXT.__oslogstring: 0x3a3c
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__constg_swiftt: 0x900
-  __TEXT.__swift5_typeref: 0xe52
+  __TEXT.__swift5_typeref: 0xe70
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x5a6
-  __TEXT.__swift5_fieldmd: 0x790
+  __TEXT.__swift5_reflstr: 0x746
+  __TEXT.__swift5_fieldmd: 0x7f0
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x2c8
+  __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_capture: 0x590
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__unwind_info: 0x18f0
+  __TEXT.__unwind_info: 0x1908
   __TEXT.__eh_frame: 0x2380
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x41d2
-  __TEXT.__objc_methtype: 0xecf
+  __TEXT.__objc_methname: 0x41f0
+  __TEXT.__objc_methtype: 0xf08
   __TEXT.__objc_stubs: 0x1a20
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc40
+  __DATA_CONST.__objc_selrefs: 0xc50
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0x23a8
   __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x3768
   __AUTH.__objc_data: 0x2a8
   __AUTH.__data: 0x1b8
   __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0xcc8
-  __DATA.__bss: 0x5980
+  __DATA.__data: 0xcf8
+  __DATA.__bss: 0x5a00
   __DATA_DIRTY.__objc_data: 0x708
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0F13CB25-ECA0-3F40-A932-8756578D06FC
-  Functions: 2386
-  Symbols:   3339
-  CStrings:  1456
+  UUID: B2CC0D8E-1A2F-3604-B29A-1AED1D232BCA
+  Functions: 2392
+  Symbols:   3341
+  CStrings:  1459
 
Symbols:
+ -[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]
+ -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]
+ -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:].cold.1
+ ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke
+ ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke.31
+ ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke.cold.1
+ ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke
+ ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2
+ ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2.cold.1
+ ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2.cold.2
+ _associated conformance 10CoreIDCred8DIPErrorV10Foundation26_ObjectiveCBridgeableErrorAAs0G0
+ _objc_msgSend$updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:
+ _symbolic SDySSSDySSSaySay_____GGGG 10CoreIDCred15DocumentRequestV11DataElementV
+ _symbolic SDySSSaySay_____GGG 10CoreIDCred15DocumentRequestV11DataElementV
+ _symbolic SaySay_____GG 10CoreIDCred15DocumentRequestV11DataElementV
- -[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:data:completion:]
- -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:]
- -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:].cold.1
- ___79-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke
- ___79-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke.31
- ___79-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke.cold.1
- ___85-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke
- ___85-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2
- ___85-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2.cold.1
- ___85-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2.cold.2
- _objc_msgSend$updateDataInSyncableKeyStoreForIdentifier:data:completion:
- _symbolic SDySSSDySSSay_____GGG 10CoreIDCred15DocumentRequestV11DataElementV
- _symbolic SDySSSay_____GG 10CoreIDCred15DocumentRequestV11DataElementV
CStrings:
+ "domain"
+ "updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:"
+ "userInfo"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "updateDataInSyncableKeyStoreForIdentifier:data:completion:"

```

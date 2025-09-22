## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1924.1.2.0.0
-  __TEXT.__text: 0x194130
+1924.5.0.0.0
+  __TEXT.__text: 0x194ca0
   __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x11614
-  __TEXT.__cstring: 0x157c4
-  __TEXT.__const: 0x5a8
-  __TEXT.__oslogstring: 0x186b2
-  __TEXT.__gcc_except_tab: 0x7f70
+  __TEXT.__objc_methlist: 0x1161c
+  __TEXT.__cstring: 0x1586b
+  __TEXT.__const: 0x5b8
+  __TEXT.__oslogstring: 0x18a5b
+  __TEXT.__gcc_except_tab: 0x7fd4
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x5398
+  __TEXT.__unwind_info: 0x53b0
   __TEXT.__objc_classname: 0x2c27
-  __TEXT.__objc_methname: 0x25a2e
+  __TEXT.__objc_methname: 0x25ac7
   __TEXT.__objc_methtype: 0x61e3
-  __TEXT.__objc_stubs: 0x17020
-  __DATA_CONST.__got: 0x1190
+  __TEXT.__objc_stubs: 0x17080
+  __DATA_CONST.__got: 0x1198
   __DATA_CONST.__const: 0x3c08
   __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7fd0
+  __DATA_CONST.__objc_selrefs: 0x7ff0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x6e8
   __AUTH_CONST.__auth_got: 0xa70
   __AUTH_CONST.__const: 0x1ac0
-  __AUTH_CONST.__cfstring: 0x12be0
+  __AUTH_CONST.__cfstring: 0x12cc0
   __AUTH_CONST.__objc_const: 0x22d70
   __AUTH_CONST.__objc_intobj: 0x2298
   __AUTH_CONST.__objc_doubleobj: 0x50

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C311A660-458E-3CCA-A287-6FF2A78D2D1D
-  Functions: 8619
-  Symbols:   27411
-  CStrings:  14162
+  UUID: AF48388C-76A9-37D5-A0D6-8C9478A2DC3F
+  Functions: 8624
+  Symbols:   27428
+  CStrings:  14191
 
Symbols:
+ -[_CDInteractionStore migrateIMessageDomainIdentifiers]
+ _OBJC_CLASS_$_NSBatchUpdateRequest
+ ___55-[_CDInteractionStore migrateIMessageDomainIdentifiers]_block_invoke
+ ___55-[_CDInteractionStore migrateIMessageDomainIdentifiers]_block_invoke.cold.1
+ ___55-[_CDInteractionStore migrateIMessageDomainIdentifiers]_block_invoke.cold.2
+ ___block_literal_global.343
+ _objc_msgSend$batchUpdateRequestWithEntityName:
+ _objc_msgSend$setPropertiesToUpdate:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
- ___block_literal_global.318
CStrings:
+ "any;"
+ "batchUpdateRequestWithEntityName:"
+ "domainIdentifier = %@"
+ "domainIdentifier BEGINSWITH %@"
+ "iMessage;"
+ "migrateIMessageDomainIdentifiers"
+ "migrateIMessageDomainIdentifiers Begin"
+ "migrateIMessageDomainIdentifiers End"
+ "migrateIMessageDomainIdentifiers End (Already completed)"
+ "migrateIMessageDomainIdentifiers Failed to query for '%{public}@'-prefixed domain identifiers (error was %{public}@): %{public}td %{private}@"
+ "migrateIMessageDomainIdentifiers Marking successful migration"
+ "migrateIMessageDomainIdentifiers Migration was not successful"
+ "migrateIMessageDomainIdentifiers No '%{public}@'-prefixed domain identifiers remaining"
+ "migrateIMessageDomainIdentifiers Unexpectedly updated 0 entities from %{private}@ to %{private}@; aborting (predicate was %{private}@)"
+ "migrateIMessageDomainIdentifiers Updated %{public}@ entities from %{private}@ to %{private}@"
+ "migrateIMessageDomainIdentifiers Updating %{private}@ to %{private}@ (interaction: %{private}@)"
+ "migrateIMessageDomainIdentifiers failed to update domainIdentifier %{private}@ (error was %{public}@): %{public}td %{private}@"
+ "noindex(bundleId) in %@ OR noindex(targetBundleId) in %@"
+ "not null"
+ "setPropertiesToUpdate:"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"

```

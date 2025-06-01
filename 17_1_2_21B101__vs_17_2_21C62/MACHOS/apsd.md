## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-971.200.71.2.2
-  __TEXT.__text: 0xbc848
+971.300.71.0.0
+  __TEXT.__text: 0xbcf28
   __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0xfac0
+  __TEXT.__objc_stubs: 0xfb20
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x9aa8
-  __TEXT.__objc_methname: 0x19107
+  __TEXT.__objc_methlist: 0x9af0
+  __TEXT.__objc_methname: 0x19229
   __TEXT.__objc_classname: 0xf4e
   __TEXT.__objc_methtype: 0x4201
-  __TEXT.__cstring: 0x8d72
+  __TEXT.__cstring: 0x8d82
   __TEXT.__const: 0x69a
-  __TEXT.__oslogstring: 0x10472
-  __TEXT.__gcc_except_tab: 0x1bb0
+  __TEXT.__oslogstring: 0x1059b
+  __TEXT.__gcc_except_tab: 0x1bc0
   __TEXT.__dlopen_cstrs: 0xaa
   __TEXT.__constg_swiftt: 0x238
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_reflstr: 0x199
   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x2ffc
+  __TEXT.__unwind_info: 0x3010
   __TEXT.__eh_frame: 0x118
   __DATA_CONST.__auth_got: 0xfa8
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x3880
-  __DATA_CONST.__cfstring: 0x7ce0
+  __DATA_CONST.__cfstring: 0x7d00
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1cca8
-  __DATA.__objc_selrefs: 0x50f0
+  __DATA.__objc_const: 0x1ccd8
+  __DATA.__objc_selrefs: 0x5120
   __DATA.__objc_protorefs: 0x60
   __DATA.__objc_classrefs: 0x600
   __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0xc9c
+  __DATA.__objc_ivar: 0xca0
   __DATA.__objc_data: 0x2d38
   __DATA.__data: 0x1828
   __DATA.__bss: 0x3c8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 82C6B18A-CCEE-3A31-9766-7FBB4C936FB5
-  Functions: 4596
+  UUID: 7CD6B639-AEF8-3891-99F8-23EBEF147B8F
+  Functions: 4602
   Symbols:   751
-  CStrings:  8037
+  CStrings:  8051
 
CStrings:
+ "%@: Migrating tokens to the keychain"
+ "%@: SecItemAdd()/SecItemUpdate() failed: %ld - setTokenForDomain"
+ "%@: SecItemCopyMatching() failed for persistenRef %@ with error: %ld - copyAppSpecificTokensWithDomain %@"
+ "%@: SecItemCopyMatching() failed: %ld - copyAppSpecificTokensWithDomain %@"
+ "%@: SecItemCopyMatching() failed: %ld - copyTokenForDomain"
+ "%@: SecItemCopyMatching() failed: %ld - isAppSpecificTokenValid"
+ "%@: SecItemCopyMatching() returned no items found."
+ "%@: SecItemDelete() failed: %ld - deleteAppSpecificTokens"
+ "%@: SecItemDelete() failed: %ld - deleteAppSpecificTokensWithArray persistentRef %@"
+ "%@: SecItemDelete() failed: %ld - setTokenForDomain"
+ "%@: SecResult shows duplicate item, trying to update it. setTokenForDomain %@ appSpecificIdentifier %@  token %@"
+ "%@: Sending acknowledgement message with response %ld"
+ "%@: Tokens can only be saved with a system token attached!"
+ "%@: copyAppSpecificTokensWithDomain %@ %@ %@"
+ "%@: copyAppSpecificTokensWithDomain - %@ for topic %@ account %@"
+ "%@: copyTokenForDomain %@ %@ %@"
+ "%@: deleteAppSpecificTokens - %@ for topic %@"
+ "%@: deleteAppSpecificTokens - domain %@ tokenServiceSuffix %@"
+ "%@: dropping cache {user: %@, service: %@}"
+ "%@: isAppSpecificTokenValid %@ %@ %@"
+ "%@: isAppSpecificTokenValid %@ %@ %@ - using cache {count: %llu}"
+ "%@: isAppSpecificTokenValid? %@ found cached token %@"
+ "%@: setTokenForDomain %@ token %@ appSpecificIdentifier %@"
+ "%@: storing cache {user: %@, service: %@, count: %llu}"
+ "<%@:%p; %@>"
+ "T@\"NSMutableDictionary\",&,N,V_perAppTokensByUserThenService"
+ "_cacheTokens:forUser:andService:"
+ "_cachedTokensForUser:andService:"
+ "_clearCacheForUser:andService:"
+ "_perAppTokensByUserThenService"
+ "initWithEnvironment:allowInMemoryCache:"
+ "perAppTokensByUserThenService"
+ "setPerAppTokensByUserThenService:"
- "Migrating tokens to the keychain"
- "SecItemAdd()/SecItemUpdate() failed: %ld - setTokenForDomain"
- "SecItemCopyMatching() failed for persistenRef %@ with error: %ld - copyAppSpecificTokensWithDomain %@"
- "SecItemCopyMatching() failed: %ld - copyAppSpecificTokensWithDomain %@"
- "SecItemCopyMatching() failed: %ld - copyTokenForDomain"
- "SecItemCopyMatching() failed: %ld - isAppSpecificTokenValid"
- "SecItemCopyMatching() returned no items found."
- "SecItemDelete() failed: %ld - deleteAppSpecificTokens"
- "SecItemDelete() failed: %ld - deleteAppSpecificTokensWithArray persistentRef %@"
- "SecItemDelete() failed: %ld - setTokenForDomain"
- "SecResult shows duplicate item, trying to update it. setTokenForDomain %@ appSpecificIdentifier %@  token %@"
- "Tokens can only be saved with a system token attached!"
- "copyAppSpecificTokensWithDomain %@ %@ %@"
- "copyAppSpecificTokensWithDomain - %@ for topic %@ account %@"
- "copyTokenForDomain %@ %@ %@"
- "deleteAppSpecificTokens - %@ for topic %@"
- "deleteAppSpecificTokens - domain %@ tokenServiceSuffix %@"
- "isAppSpecificTokenValid %@ %@ %@"
- "isAppSpecificTokenValid? %@ found cached token %@"
- "setTokenForDomain %@ token %@ appSpecificIdentifier %@"

```

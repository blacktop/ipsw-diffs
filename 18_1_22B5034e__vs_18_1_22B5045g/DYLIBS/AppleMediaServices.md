## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-8.1.6.0.0
-  __TEXT.__text: 0x6efa18
-  __TEXT.__auth_stubs: 0x41d0
-  __TEXT.__objc_methlist: 0x1d500
-  __TEXT.__cstring: 0x259c6
-  __TEXT.__const: 0x55fb4
+8.1.8.2.1
+  __TEXT.__text: 0x6dfbb0
+  __TEXT.__auth_stubs: 0x41e0
+  __TEXT.__objc_methlist: 0x1d550
+  __TEXT.__cstring: 0x25c3b
+  __TEXT.__const: 0x566a4
   __TEXT.__swift5_typeref: 0x32bb
   __TEXT.__swift5_reflstr: 0x1974
   __TEXT.__swift5_assocty: 0x7e0

   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__oslogstring: 0x2c601
-  __TEXT.__gcc_except_tab: 0x16c48
+  __TEXT.__gcc_except_tab: 0x16e30
   __TEXT.__dlopen_cstrs: 0x8d3
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x108b8
+  __TEXT.__unwind_info: 0x10938
   __TEXT.__eh_frame: 0xa664
   __TEXT.__objc_classname: 0x3945
-  __TEXT.__objc_methname: 0x3ddea
+  __TEXT.__objc_methname: 0x3ded3
   __TEXT.__objc_methtype: 0x6c3f
-  __TEXT.__objc_stubs: 0x2b3e0
-  __DATA_CONST.__got: 0x16b0
-  __DATA_CONST.__const: 0xb4b0
+  __TEXT.__objc_stubs: 0x2b480
+  __DATA_CONST.__got: 0x16c8
+  __DATA_CONST.__const: 0xb428
   __DATA_CONST.__objc_classlist: 0x1158
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda68
+  __DATA_CONST.__objc_selrefs: 0xda98
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0xba0
   __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__auth_got: 0x2100
-  __AUTH_CONST.__auth_ptr: 0x9b0
-  __AUTH_CONST.__const: 0x23808
-  __AUTH_CONST.__cfstring: 0x1fce0
-  __AUTH_CONST.__objc_const: 0x38030
+  __AUTH_CONST.__auth_got: 0x2108
+  __AUTH_CONST.__auth_ptr: 0x9a8
+  __AUTH_CONST.__const: 0x23ac0
+  __AUTH_CONST.__cfstring: 0x1fd20
+  __AUTH_CONST.__objc_const: 0x380c0
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x118

   __AUTH.__data: 0xde8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x5
-  __DATA.__objc_ivar: 0x16d0
+  __DATA.__objc_ivar: 0x16dc
   __DATA.__data: 0x4de8
-  __DATA.__bss: 0x7921
+  __DATA.__bss: 0x7b01
   __DATA.__common: 0xaa0
   __DATA_DIRTY.__objc_ivar: 0x63c
   __DATA_DIRTY.__objc_data: 0x5208
   __DATA_DIRTY.__data: 0x1988
-  __DATA_DIRTY.__bss: 0x3380
+  __DATA_DIRTY.__bss: 0x3370
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20316
-  Symbols:   18245
-  CStrings:  19435
+  Functions: 20352
+  Symbols:   18281
+  CStrings:  19453
 
Symbols:
+ _NSFileSystemSize
+ _NSFileSystemFreeSize
+ __ZTINSt3__14__fs10filesystem16filesystem_errorE
+ __ZNSt3__14__fs10filesystem8__removeERKNS1_4pathEPNS_10error_codeE
CStrings:
+ ":responseBody"
+ "regexForPattern:fromCache:"
+ "URL mismatch in cached response."
+ "A local account cannot be made active."
+ "HTTP method mismatch in cached response."
+ "Failed to delete cached bag responses: "
+ "setRegexCache:"
+ "Failed to delete legacy HTTPCache file. error = "
+ "CREATE TABLE IF NOT EXISTS \"HTTPCache\" (\"accountIdentifier\" TEXT NOT NULL,\"key\" TEXT NOT NULL,\"url\" TEXT NOT NULL,\"method\" TEXT NOT NULL,\"requestBody\" BLOB NOT NULL,\"headers\" BLOB NOT NULL,\"responseBody\" BLOB NOT NULL,\"createdAt\" INTEGER NOT NULL,PRIMARY KEY (\"key\", \"accountIdentifier\"))"
+ "attributesOfFileSystemForPath:error:"
+ "Device storage has %!f(MISSING)% free (%!@(MISSING) free out of %!@(MISSING))"
+ "_regexCache"
+ "databaseError"
+ "%!@(MISSING). Log key: %!@(MISSING). %!@(MISSING)."
+ "matchEvent:toFilter:withCache:"
+ "REPLACE INTO \"HTTPCache\" (\"accountIdentifier\", \"key\", \"url\", \"method\", \"requestBody\", \"headers\", \"responseBody\", \"createdAt\")VALUES (:accountIdentifier, :key, :url, :method, :requestBody, :headers, :responseBody, :createdAt)"
+ "Failed to set bag cache current platform version: "
+ "Unable to determine free storage space, error: %!@(MISSING)"
+ "regexCache"
+ "requestBody"
+ "_deviceStorageDetails"
+ "stringFromValue:"
+ "T@\"NSMutableDictionary\",R,N,V_regexCache"
+ "AMSBagCacheProviderCurrentPlatformVersion"
+ ":requestBody"
+ "bag-anonymous-account"
+ "Legacy HTTPCache file was deleted."
+ "T@\"NSMutableDictionary\",&,N,V_regexCache"
+ "HTTPCache2"
+ "SELECT \"accountIdentifier\", \"url\", \"method\", \"requestBody\", \"headers\", \"responseBody\", \"createdAt\"FROM \"HTTPCache\"WHERE (\"key\" IS :key AND \"accountIdentifier\" IS :accountIdentifier)"
+ "Request body mismatch in cached response."
- "iBooks/"
- "; arm64"
- "REPLACE INTO \"HTTPCache\" (\"accountIdentifier\", \"key\", \"url\", \"headers\", \"response\", \"createdAt\")VALUES (:accountIdentifier, :key, :url, :headers, :response, :createdAt)"
- ":response"
- "SELECT \"accountIdentifier\", \"url\", \"headers\", \"response\", \"createdAt\"FROM \"HTTPCache\"WHERE (\"key\" IS :key AND \"accountIdentifier\" IS :accountIdentifier)"
- ") "
- "; x64"
- "Configurator/"
- "matchEvent:toFilter:"
- "(Windows "
- "%!@(MISSING). Log key: %!@(MISSING)"
- "MacAppStore/3.0 "
- "CREATE TABLE IF NOT EXISTS \"HTTPCache\" (\"accountIdentifier\" TEXT NOT NULL,\"key\" TEXT NOT NULL,\"url\" TEXT NOT NULL,\"headers\" BLOB NOT NULL,\"response\" BLOB NOT NULL,\"createdAt\" INTEGER NOT NULL,PRIMARY KEY (\"key\", \"accountIdentifier\"))"
- "AppleWebKit/"

```

## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-710.1.103.0.0
-  __TEXT.__text: 0xbd6c8
+710.7.140.0.0
+  __TEXT.__text: 0xbdb74
   __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x6390
+  __TEXT.__objc_methlist: 0x63d8
   __TEXT.__const: 0x223
   __TEXT.__gcc_except_tab: 0x2604
-  __TEXT.__cstring: 0x9d2e
-  __TEXT.__oslogstring: 0xe519
+  __TEXT.__cstring: 0x9dc3
+  __TEXT.__oslogstring: 0xe564
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x27f0
+  __TEXT.__unwind_info: 0x2808
   __TEXT.__objc_classname: 0x800
-  __TEXT.__objc_methname: 0x123b5
-  __TEXT.__objc_methtype: 0x41c5
-  __TEXT.__objc_stubs: 0xc340
+  __TEXT.__objc_methname: 0x124b5
+  __TEXT.__objc_methtype: 0x421e
+  __TEXT.__objc_stubs: 0xc3c0
   __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x2080
+  __DATA_CONST.__const: 0x2090
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bc8
+  __DATA_CONST.__objc_selrefs: 0x3bf8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c0
   __AUTH_CONST.__auth_got: 0x7e0
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x7d80
-  __AUTH_CONST.__objc_const: 0xa528
+  __AUTH_CONST.__cfstring: 0x7de0
+  __AUTH_CONST.__objc_const: 0xa598
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x64c
+  __DATA.__objc_ivar: 0x650
   __DATA.__data: 0xaa0
   __DATA.__bss: 0x228
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3250
-  Symbols:   4050
-  CStrings:  5181
+  Functions: 3258
+  Symbols:   4060
+  CStrings:  5196
 
Symbols:
+ _kMSASClientOrgKey
+ _kMSASModelSetClientOrgKeyForAlbumWithGUIDFn
CStrings:
+ "\x1e"
+ " client org key: %!@(MISSING)"
+ "%!{(MISSING)public}@: Could not add clientOrgKey column to Albums. Error: %!{(MISSING)public}s"
+ "B80@0:8@16^@24^@32^@40^@48^@56^@64^@72"
+ "T@\"NSString\",&,N,V_clientOrgKey"
+ "_clientOrgKey"
+ "alter table Albums add column clientOrgKey text"
+ "clientOrgKey"
+ "clientOrgKey"
+ "dbQueueAlbumWithGUID:outObject:outName:outCtag:outForeignCtag:outURLString:outUserInfoData:outClientOrgKey:"
+ "insert or replace into Albums (GUID, name, ctag, foreignCtag, obj, url, userInfo, clientOrgKey) values (?, ?, ?, ?, ?, ?, ?, ?);"
+ "modelSetClientOrgKeyForAlbumWithGUID"
+ "select obj, name, ctag, foreignCtag, url, userInfo, clientOrgKey from Albums where GUID = ?;"
+ "setClientOrgKey:"
+ "setClientOrgKey:forAlbumWithGUID:"
+ "setClientOrgKey:forAlbumWithGUID:info:"
+ "setClientOrgKey:forAlbumWithGUID:personID:"
+ "setClientOrgKey:forAlbumWithGUID:personID:info:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
- "\x1d"
- "B72@0:8@16^@24^@32^@40^@48^@56^@64"
- "dbQueueAlbumWithGUID:outObject:outName:outCtag:outForeignCtag:outURLString:outUserInfoData:"
- "insert or replace into Albums (GUID, name, ctag, foreignCtag, obj, url, userInfo) values (?, ?, ?, ?, ?, ?, ?);"
- "select obj, name, ctag, foreignCtag, url, userInfo from Albums where GUID = ?;"

```

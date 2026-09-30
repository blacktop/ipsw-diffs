## smbclientd

> `/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd`

```diff

-219.100.3.0.0
-  __TEXT.__text: 0x635d8
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x5160
-  __TEXT.__objc_methlist: 0x2070
+231.0.0.0.0
+  __TEXT.__text: 0x64670
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0x2138
   __TEXT.__const: 0x2bc
-  __TEXT.__cstring: 0x1360
-  __TEXT.__oslogstring: 0xe181
-  __TEXT.__objc_classname: 0x191
-  __TEXT.__objc_methname: 0x63cb
-  __TEXT.__objc_methtype: 0x1f9a
-  __TEXT.__gcc_except_tab: 0x2930
+  __TEXT.__cstring: 0x143c
+  __TEXT.__oslogstring: 0xe26d
+  __TEXT.__objc_classname: 0x1ca
+  __TEXT.__objc_methname: 0x65fa
+  __TEXT.__objc_methtype: 0x2011
+  __TEXT.__gcc_except_tab: 0x2a00
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1370
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x2270
-  __DATA_CONST.__cfstring: 0xb00
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x28
+  __TEXT.__unwind_info: 0x13d8
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x22e8
+  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2db8
-  __DATA.__objc_selrefs: 0x1978
-  __DATA.__objc_ivar: 0x2c4
-  __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x234
+  __DATA.__objc_const: 0x2f40
+  __DATA.__objc_selrefs: 0x1a08
+  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_data: 0x640
+  __DATA.__data: 0x294
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper
   - /System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine
   - /System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BDFF90E-9DEB-3266-8A19-9FF43BC72B33
-  Functions: 2262
-  Symbols:   229
-  CStrings:  2619
+  UUID: 276E3672-D3BC-3808-953D-A99280707352
+  Functions: 2285
+  Symbols:   239
+  CStrings:  2657
 
Symbols:
+ OBJC_IVAR_$_LiveFSMountClient.conn
+ OBJC_IVAR_$_LiveFSMountClient.helper
+ OBJC_IVAR_$_LiveFSMountClient.provider
+ _OBJC_CLASS_$_NSFileProviderDomain
+ _OBJC_CLASS_$_NSFileProviderManager
+ _OBJC_CLASS_$_SOAuthorization
+ _OBJC_METACLASS_$_LiveFSMountClient
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _livefs_std_log
- _OBJC_CLASS_$_LiveFSFPMountClient
CStrings:
+ "%s: addDomain returned error: %@"
+ "%s: name(%@), displayName(%@), providerName(%@)"
+ "%s: removeDomain returned error: %@"
+ "%s:setConnected:completionHandler: returned %@"
+ "-[SMBMounterClientHelper createDomain:displayName:how:storageName:reply:]"
+ "-[SMBMounterClientHelper createDomain:displayName:how:storageName:reply:]_block_invoke"
+ "-[SMBMounterClientHelper destroyDomain:]_block_invoke"
+ "@44@0:8@16@24@32i40"
+ "LIMakeSymLink: fatal, no memory for smbfattr"
+ "LiveFSMounterClient"
+ "SMBFPClient"
+ "SMBMounterClientHelper"
+ "T@\"NSString\",&,V_providerName"
+ "T@\"smbNode\",R,W,V_dnp"
+ "_initWithProviderIdentifier:"
+ "_initWithProviderIdentifier:domain:"
+ "_providerName"
+ "addDomain:completionHandler:"
+ "createDomain:displayName:how:reply:"
+ "createDomain:displayName:how:storageName:reply:"
+ "createDomain:how:reply:"
+ "destroyDomain:"
+ "fillNextEntry: _dnp is nil"
+ "fixupConnectionFor:"
+ "initWithIdentifier:displayName:pathRelativeToDocumentStorage:"
+ "initWithIdentifier:displayName:pathRelativeToDocumentStorage:hidden:"
+ "initWithProvider:"
+ "nil"
+ "providerName"
+ "realms"
+ "removeDomain:completionHandler:"
+ "setConnected:completionHandler:"
+ "setErasable:"
+ "setProviderName:"
+ "setReadOnly:"
+ "v28@?0i8^{_LIStatfsResult=QQQQQQQ}12Q20"
+ "v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\">28"
+ "v44@0:8@\"NSString\"16@\"NSString\"24i32@?<v@?@\"NSError\">36"
- "T@\"smbNode\",R,V_dnp"
- "v28@?0i8^{_LIStatfsResult=QQQQQQ}12Q20"

```

## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-355.3.0.0.0
-  __TEXT.__text: 0x27354
+355.4.0.0.0
+  __TEXT.__text: 0x2776c
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x1eec
+  __TEXT.__objc_methlist: 0x1f94
   __TEXT.__const: 0x1d8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__cstring: 0x3f7b
+  __TEXT.__cstring: 0x3f76
   __TEXT.__oslogstring: 0x1a4f
   __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__objc_classname: 0x35e
-  __TEXT.__objc_methname: 0x42ea
-  __TEXT.__objc_methtype: 0xa24
-  __TEXT.__objc_stubs: 0x26c0
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__objc_classname: 0x380
+  __TEXT.__objc_methname: 0x4409
+  __TEXT.__objc_methtype: 0xa41
+  __TEXT.__objc_stubs: 0x2720
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x828
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_selrefs: 0x1288
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x3e8
   __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x3868
+  __AUTH_CONST.__objc_const: 0x39d0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x210
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x3d0
   __DATA.__bss: 0x8
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 682
-  Symbols:   2426
-  CStrings:  1819
+  Functions: 695
+  Symbols:   2467
+  CStrings:  1833
 
Symbols:
+ -[NFXPCConnectionUserInfoDictionary .cxx_destruct]
+ -[NFXPCConnectionUserInfoDictionary clientName]
+ -[NFXPCConnectionUserInfoDictionary initWithServiceWhitelist:clientName:]
+ -[NFXPCConnectionUserInfoDictionary modifyObjectForKey:handler:]
+ -[NFXPCConnectionUserInfoDictionary objectForKey:]
+ -[NFXPCConnectionUserInfoDictionary objectForKeyedSubscript:]
+ -[NFXPCConnectionUserInfoDictionary objectsForKeys:notFoundMarker:]
+ -[NFXPCConnectionUserInfoDictionary removeObjectForKey:]
+ -[NFXPCConnectionUserInfoDictionary serviceWhitelist]
+ -[NFXPCConnectionUserInfoDictionary setObject:forKey:]
+ -[NFXPCConnectionUserInfoDictionary setObject:forKeyedSubscript:]
+ -[NSXPCConnection(NFUserInfo) NF_clientName]
+ -[NSXPCConnection(NFUserInfo) NF_serviceType]
+ _OBJC_CLASS_$_NFXPCConnectionUserInfoDictionary
+ _OBJC_IVAR_$_NFXPCConnectionUserInfoDictionary._clientName
+ _OBJC_IVAR_$_NFXPCConnectionUserInfoDictionary._data
+ _OBJC_IVAR_$_NFXPCConnectionUserInfoDictionary._dataLock
+ _OBJC_IVAR_$_NFXPCConnectionUserInfoDictionary._serviceWhitelist
+ _OBJC_METACLASS_$_NFXPCConnectionUserInfoDictionary
+ __OBJC_$_INSTANCE_METHODS_NFXPCConnectionUserInfoDictionary
+ __OBJC_$_INSTANCE_VARIABLES_NFXPCConnectionUserInfoDictionary
+ __OBJC_$_PROP_LIST_NFXPCConnectionUserInfoDictionary
+ __OBJC_$_PROP_LIST_NSXPCConnection_$_NFUserInfo
+ __OBJC_CLASS_RO_$_NFXPCConnectionUserInfoDictionary
+ __OBJC_METACLASS_RO_$_NFXPCConnectionUserInfoDictionary
+ _objc_msgSend$clientName
+ _objc_msgSend$objectsForKeys:notFoundMarker:
+ _objc_msgSend$serviceWhitelist
CStrings:
+ "@\"NFServiceWhitelistChecker\""
+ "NFXPCConnectionUserInfoDictionary"
+ "NF_clientName"
+ "NF_serviceType"
+ "T@\"NFServiceWhitelistChecker\",R,N,V_serviceWhitelist"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_clientName"
+ "_dataLock"
+ "_serviceWhitelist"
+ "initWithServiceWhitelist:clientName:"
+ "modifyObjectForKey:handler:"
+ "objectsForKeys:notFoundMarker:"
+ "serviceType"
+ "serviceWhitelist"
- "ServiceWhitelist"

```

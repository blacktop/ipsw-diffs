## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-833.40.18.0.1
-  __TEXT.__text: 0x106c14
-  __TEXT.__objc_methlist: 0xb634
+833.60.4.0.1
+  __TEXT.__text: 0x10771c
+  __TEXT.__objc_methlist: 0xb694
   __TEXT.__const: 0x1620
-  __TEXT.__cstring: 0xa13c
+  __TEXT.__cstring: 0xa1f2
   __TEXT.__swift5_typeref: 0x889
   __TEXT.__oslogstring: 0x10329
   __TEXT.__constg_swiftt: 0x7b0

   __TEXT.__swift5_protos: 0x18
   __TEXT.__gcc_except_tab: 0x255c
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x3f08
+  __TEXT.__unwind_info: 0x3f28
   __TEXT.__eh_frame: 0xa74
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a28
+  __DATA_CONST.__objc_selrefs: 0x3a48
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x2e8
   __DATA_CONST.__got: 0x548
   __AUTH_CONST.__const: 0x15c0
-  __AUTH_CONST.__cfstring: 0x4e60
-  __AUTH_CONST.__objc_const: 0x17da0
+  __AUTH_CONST.__cfstring: 0x4e80
+  __AUTH_CONST.__objc_const: 0x17e28
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__auth_got: 0x1448
   __AUTH.__objc_data: 0xea8
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0xc5c
-  __DATA.__data: 0x3db0
+  __DATA.__objc_ivar: 0xc60
+  __DATA.__data: 0x3dc0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x3198

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3932
-  Symbols:   7095
-  CStrings:  2154
+  Functions: 3939
+  Symbols:   7099
+  CStrings:  2159
 
Symbols:
+ -[MCMContainerCacheEntry adoptCreatorFromMetadata:]
+ -[MCMContainerCacheEntry creator]
+ -[MCMContainerCacheEntry initWithIdentifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:creator:metadata:userIdentityCache:]
+ -[MCMContainerCacheEntry setCreator:]
+ -[MCMContainerClassCache _concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:creator:metadata:]
+ GCC_except_table3042
+ _OBJC_IVAR_$_MCMContainerCacheEntry._creator
- -[MCMContainerCacheEntry initWithIdentifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:userIdentityCache:]
- -[MCMContainerClassCache _concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:]
- GCC_except_table3039
CStrings:
+ "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, posixOwnership = %@, fsNode = %@, instanceUUID = %@, creator = %@%s%s>"
+ "Identity record creator field is unterminated"
+ "Identity record creator is not an acceptable "
+ "Identity record creator is not valid UTF-8"
+ "MobileContainerManager-833.60.4.0.1~339"
+ "creator"
+ "creator: "
+ "\xa1"
- "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, posixOwnership = %@, fsNode = %@, instanceUUID = %@%s%s>"
- "MobileContainerManager-833.40.18.0.1~91"
- "\x91"
```

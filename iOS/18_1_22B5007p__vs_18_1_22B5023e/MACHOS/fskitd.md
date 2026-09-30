## fskitd

> `/usr/libexec/fskitd`

```diff

-445.0.0.0.0
-  __TEXT.__text: 0x3e510
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0x44a0
-  __TEXT.__objc_methlist: 0x1628
+467.0.0.0.0
+  __TEXT.__text: 0x3ec64
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_stubs: 0x4520
+  __TEXT.__objc_methlist: 0x1660
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1e4c
-  __TEXT.__cstring: 0x269b
-  __TEXT.__oslogstring: 0x3142
+  __TEXT.__gcc_except_tab: 0x1e50
+  __TEXT.__cstring: 0x2670
+  __TEXT.__oslogstring: 0x3169
   __TEXT.__objc_classname: 0x1f8
-  __TEXT.__objc_methname: 0x511d
-  __TEXT.__objc_methtype: 0x1e59
-  __TEXT.__unwind_info: 0xe98
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1dc0
-  __DATA_CONST.__cfstring: 0x9a0
+  __TEXT.__objc_methname: 0x51d0
+  __TEXT.__objc_methtype: 0x1f14
+  __TEXT.__unwind_info: 0xea8
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x1d78
+  __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x28f0
-  __DATA.__objc_selrefs: 0x13d8
+  __DATA.__objc_const: 0x2930
+  __DATA.__objc_selrefs: 0x1400
   __DATA.__objc_ivar: 0x154
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x370

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1179
-  Symbols:   275
-  CStrings:  1672
+  Functions: 1185
+  Symbols:   280
+  CStrings:  1679
 
Symbols:
+ _FSModuleIdentityAttributeShortName
+ _FSModuleIdentityAttributeSupportsBlockResources
+ _FSModuleIdentityAttributeSupportsKOIO
+ _FSModuleIdentityAttributeSupportsServerURLs
+ _OBJC_CLASS_$_FSGenericURLResource
+ _objc_retain_x9
- _OBJC_CLASS_$_FSPathURLResource
CStrings:
+ "%!s(MISSING): Attempt to start disabled extension %!@(MISSING)"
+ "B16@?0@\"FSTaskDescription\"8"
+ "BSDName"
+ "Could not allocate root filesystem"
+ "Could not allocate root filesystem"
+ "Could not initialize the fskitd's root memory filesystem."
+ "Could not initialize the fskitd's root memory filesystem. error = %!{(MISSING)public}@"
+ "Creating the root (FPnfsMemFS) filesystem"
+ "Mount the root filesystem (FPnfsMemFS"
+ "Mounting filesystem on port %!@(MISSING) with rootfh = %!s(MISSING)"
+ "addBundleToEnableModules:"
+ "applyResource starting with resource %!@(MISSING) kind %!l(MISSING)d"
+ "initWithProxy:"
+ "isEnabled"
+ "isWritable"
+ "moduleForBundleID:"
+ "newWithProxy:"
+ "openWithBSDName:writable:auditToken:replyHandler:"
+ "removeBundleFromEnabledModules:"
+ "revoke"
+ "setEnabledStateForIdentifier:newState:replyHandler:"
+ "setEnabledStateForToken:identifier:newState:replyHandler:"
+ "v20@?0i8@\"FSStatFSResult\"12"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?i@\"NSData\"@\"NSData\">32"
+ "v44@0:8@16@24B32@?36"
+ "v52@0:8@\"NSString\"16@\"FSFileName\"24I32Q36@?<v@?ii@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">44"
+ "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"
+ "v68@0:8{?=[8I]}16@\"NSString\"48B56@?<v@?@\"NSError\">60"
+ "v68@0:8{?=[8I]}16@48B56@?60"
+ "v72@?0i8i12@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@\"NSData\"56@\"NSData\"64"
+ "v72@?0i8i12@\"NSString\"16@\"NSData\"24@\"NSString\"32@\"NSData\"40@\"NSString\"48@\"NSData\"56@\"NSData\"64"
- "Could not allocate root file system"
- "Could not allocate root file system"
- "Could not initialize the fskitd's root memory file system."
- "Could not initialize the fskitd's root memory file system. error = %!{(MISSING)public}@"
- "Creating the root (FPnfsMemFS) file system"
- "FSShortName"
- "FSSupportsBlockResources"
- "FSSupportsKernelOffloadedIO"
- "Mount the root file system (FPnfsMemFS"
- "Mounting file system on port %!@(MISSING) with rootfh = %!s(MISSING)"
- "applyResource starting with resource %!@(MISSING) kind %!d(MISSING)"
- "bsdName"
- "containerIdentifier"
- "nameWithString:"
- "openWithBSDName:writeable:auditToken:replyHandler:"
- "revoke:"
- "terminate:"
- "v20@?0i8@\"FSKitStatfsResult\"12"
- "v28@?0i8@\"FSFileName\"12@\"NSData\"20"
- "v32@?0i8@\"NSData\"12I20@\"NSData\"24"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"FSFileName\"@\"NSData\">32"
- "v48@?0i8@\"NSData\"12@\"NSData\"20@\"NSString\"28@\"NSData\"36I44"
- "v48@?0i8@\"NSString\"12@\"NSData\"20@\"NSString\"28@\"NSData\"36I44"
- "v52@0:8@\"NSString\"16@\"FSFileName\"24I32Q36@?<v@?i@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\"I>44"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"I@\"NSData\">56"
- "writable"

```

## configd

> `/usr/libexec/configd`

```diff

-1405.120.5.0.0
-  __TEXT.__text: 0x68c00
-  __TEXT.__auth_stubs: 0x24b0
+1434.0.0.502.1
+  __TEXT.__text: 0x68bc0
+  __TEXT.__auth_stubs: 0x24f0
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x2fc1
-  __TEXT.__oslogstring: 0x55fd
+  __TEXT.__cstring: 0x3026
+  __TEXT.__oslogstring: 0x55f2
   __TEXT.__objc_methname: 0x1a6b
-  __TEXT.__objc_classname: 0x5d
+  __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methtype: 0x501
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0xad0
-  __DATA_CONST.__auth_got: 0x1268
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__auth_ptr: 0x108
+  __TEXT.__unwind_info: 0xa38
   __DATA_CONST.__const: 0x19d0
-  __DATA_CONST.__cfstring: 0x25a0
+  __DATA_CONST.__cfstring: 0x25c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__auth_got: 0x1288
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0xc48
   __DATA.__objc_selrefs: 0x738
   __DATA.__objc_ivar: 0x90

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F3C6F98-1986-3E2B-AA0C-E74E9D94ABC9
-  Functions: 954
-  Symbols:   817
-  CStrings:  1970
+  UUID: 165947A8-C9A6-326D-AE61-8909C9C691C8
+  Functions: 957
+  Symbols:   820
+  CStrings:  1977
 
Symbols:
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
- _kSCPropNetDNSEncryptedServerServicePriority
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s: %@ removing NAT64 request"
+ "%s: nat64 prefix list %s"
+ "%s: will configure %@"
+ "/AppleVirtIONetwork/"
+ "NO"
+ "YES"
+ "cleared"
+ "copyAutoConfigurableInterfaceList"
+ "currentSetExists"
+ "updated"
- "%@ %s: no active NAT64 request"
- "%s %s: removing NAT64 request"
- "%s: nat64 prefix%s updated"
- "es"

```

## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

```diff

-912.0.0.0.0
-  __TEXT.__text: 0x164d8
+917.0.0.0.0
+  __TEXT.__text: 0x168c8
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_methlist: 0xe84
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x13f7
-  __TEXT.__oslogstring: 0x2175
+  __TEXT.__cstring: 0x1429
+  __TEXT.__oslogstring: 0x222e
   __TEXT.__unwind_info: 0x360
   __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x2d17
+  __TEXT.__objc_methname: 0x2d36
   __TEXT.__objc_methtype: 0x1464
-  __TEXT.__objc_stubs: 0x2500
+  __TEXT.__objc_stubs: 0x2520
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x2300
+  __AUTH_CONST.__cfstring: 0x2340
   __AUTH_CONST.__objc_const: 0x2698
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1C2E45EF-2855-34AB-83CD-BC515DBC8251
+  UUID: 3155603B-C589-3A07-A5B3-EBB020DDEAB6
   Functions: 300
-  Symbols:   1454
-  CStrings:  1501
+  Symbols:   1455
+  CStrings:  1509
 
Symbols:
+ ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.422
+ _listxattr
+ _objc_msgSend$initWithBytes:length:encoding:
- ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.421
- _objc_retain_x28
Functions:
~ -[PCCJob packageLog:forRouting:info:options:] : 888 -> 1556
~ -[PCCGroupJob initWithID:forTarget:options:] : 1452 -> 1448
~ -[PCCProxyingDevice handleFile:from:metadata:] : 3168 -> 3512
CStrings:
+ "Adding xattr %@: %@"
+ "com.apple.dataprotection.policy.exception-applied-by"
+ "failed to decode xattr value for key: %@"
+ "failed to get xattr list size for file: %s"
+ "failed to get xattr value for key: %s"
+ "failed to get xattr value size for key: %s"
+ "initWithBytes:length:encoding:"
+ "xattr_list"
- "1"
- "DnUOverride"

```

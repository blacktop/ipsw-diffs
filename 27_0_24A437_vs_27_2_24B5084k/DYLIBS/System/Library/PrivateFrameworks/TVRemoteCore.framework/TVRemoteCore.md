## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-627.0.28.0.0
-  __TEXT.__text: 0x470d4
+627.10.45.0.0
+  __TEXT.__text: 0x47270
   __TEXT.__lazy_helpers: 0x580
-  __TEXT.__objc_methlist: 0x64d0
-  __TEXT.__const: 0x240
-  __TEXT.__oslogstring: 0x6b90
-  __TEXT.__cstring: 0x372c
+  __TEXT.__objc_methlist: 0x6528
+  __TEXT.__const: 0x250
+  __TEXT.__oslogstring: 0x6bd5
+  __TEXT.__cstring: 0x3738
   __TEXT.__gcc_except_tab: 0xb14
-  __TEXT.__unwind_info: 0x1860
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3090
+  __DATA_CONST.__objc_selrefs: 0x3100
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x4a60
-  __AUTH_CONST.__objc_const: 0x9f88
+  __AUTH_CONST.__cfstring: 0x4a80
+  __AUTH_CONST.__objc_const: 0x9fe0
   __AUTH_CONST.__lazy_load_got: 0x80
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1860
-  __DATA.__objc_ivar: 0x698
+  __DATA.__objc_ivar: 0x69c
   __DATA.__data: 0xa34
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x170

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2139
-  Symbols:   4765
-  CStrings:  1299
+  Functions: 2142
+  Symbols:   4780
+  CStrings:  1300
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper _updateFindMyRemoteSupport]
+ -[TVRCSiriRemoteInfo productID]
+ -[TVRCSiriRemoteInfo setProductID:]
+ GCC_except_table104
+ GCC_except_table114
+ GCC_except_table119
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table141
+ GCC_except_table146
+ GCC_except_table15
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table98
+ _GestaltGetDeviceClass
+ _OBJC_IVAR_$_TVRCSiriRemoteInfo._productID
+ _objc_msgSend$_updateFindMyRemoteSupport
+ _objc_msgSend$appendUnsignedInteger:withName:format:
+ _objc_msgSend$deletionCount
+ _objc_msgSend$forwardDeletionCount
+ _objc_msgSend$insertionText
+ _objc_msgSend$keyboardOutput
+ _objc_msgSend$productID
+ _objc_msgSend$setProductID:
+ _objc_msgSend$textOperations
- GCC_except_table103
- GCC_except_table113
- GCC_except_table118
- GCC_except_table123
- GCC_except_table129
- GCC_except_table133
- GCC_except_table140
- GCC_except_table145
- GCC_except_table31
- GCC_except_table35
- GCC_except_table40
- GCC_except_table43
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table87
- GCC_except_table90
- GCC_except_table93
- GCC_except_table95
- GCC_except_table97
CStrings:
+ "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d, paired remote productID: %@"
+ "Keyboard RemoteTextInput send operation - insert length:%lu deleteBackward:%lu forwardDelete:%lu"
+ "productID"
- "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d"
- "Keyboard RemoteTextInput send payload string length: %lu"
```

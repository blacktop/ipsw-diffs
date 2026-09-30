## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

```diff

-627.0.28.0.0
-  __TEXT.__text: 0x4a550
-  __TEXT.__objc_methlist: 0x63a8
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x3627
+627.10.45.0.0
+  __TEXT.__text: 0x4a710
+  __TEXT.__objc_methlist: 0x63f8
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0x3633
   __TEXT.__gcc_except_tab: 0xb1c
-  __TEXT.__oslogstring: 0x6697
-  __TEXT.__unwind_info: 0x1888
+  __TEXT.__oslogstring: 0x66dc
+  __TEXT.__unwind_info: 0x1890
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f90
+  __DATA_CONST.__objc_selrefs: 0x2ff8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x1300
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x9d90
+  __AUTH_CONST.__cfstring: 0x49c0
+  __AUTH_CONST.__objc_const: 0x9de0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1860
-  __DATA.__objc_ivar: 0x690
+  __DATA.__objc_ivar: 0x694
   __DATA.__data: 0x9d0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x160

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2154
-  Symbols:   4739
-  CStrings:  1266
+  Functions: 2157
+  Symbols:   4751
+  CStrings:  1267
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper _updateFindMyRemoteSupport]
+ -[TVRCSiriRemoteInfo productID]
+ -[TVRCSiriRemoteInfo setProductID:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table121
+ GCC_except_table131
+ GCC_except_table136
+ GCC_except_table141
+ GCC_except_table147
+ GCC_except_table153
+ GCC_except_table160
+ GCC_except_table167
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table48
+ GCC_except_table97
+ GCC_except_table99
+ OBJC_IVAR_$_TVRCSiriRemoteInfo._productID
+ _GestaltGetDeviceClass
+ _objc_msgSend$_updateFindMyRemoteSupport
+ _objc_msgSend$appendUnsignedInteger:withName:format:
+ _objc_msgSend$deletionCount
+ _objc_msgSend$forwardDeletionCount
+ _objc_msgSend$insertionText
+ _objc_msgSend$keyboardOutput
+ _objc_msgSend$productID
+ _objc_msgSend$setProductID:
+ _objc_msgSend$textOperations
- GCC_except_table100
- GCC_except_table102
- GCC_except_table104
- GCC_except_table107
- GCC_except_table110
- GCC_except_table112
- GCC_except_table114
- GCC_except_table120
- GCC_except_table130
- GCC_except_table135
- GCC_except_table140
- GCC_except_table146
- GCC_except_table152
- GCC_except_table159
- GCC_except_table16
- GCC_except_table166
- GCC_except_table37
- GCC_except_table42
- GCC_except_table47
- GCC_except_table50
- GCC_except_table96
- GCC_except_table98
CStrings:
+ "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d, paired remote productID: %@"
+ "Keyboard RemoteTextInput send operation - insert length:%lu deleteBackward:%lu forwardDelete:%lu"
+ "productID"
- "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d"
- "Keyboard RemoteTextInput send payload string length: %lu"
```

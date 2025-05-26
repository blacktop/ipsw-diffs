## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-542.1.0.0.0
-  __TEXT.__text: 0x76590
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_methlist: 0x7850
+550.8.1.0.0
+  __TEXT.__text: 0x7668c
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x7880
   __TEXT.__const: 0x1cbf
-  __TEXT.__cstring: 0x12cf9
+  __TEXT.__cstring: 0x12cc8
   __TEXT.__gcc_except_tab: 0xfd8
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x1970
+  __TEXT.__unwind_info: 0x1954
   __TEXT.__objc_classname: 0x9ad
-  __TEXT.__objc_methname: 0xf4f0
-  __TEXT.__objc_methtype: 0x27be
-  __TEXT.__objc_stubs: 0x83a0
+  __TEXT.__objc_methname: 0xf5b2
+  __TEXT.__objc_methtype: 0x27cf
+  __TEXT.__objc_stubs: 0x83e0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x2280
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xed38
-  __DATA_CONST.__objc_selrefs: 0x33e8
+  __DATA_CONST.__objc_const: 0xed98
+  __DATA_CONST.__objc_selrefs: 0x3418
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_classrefs: 0x268
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__objc_const: 0x5a0
+  __AUTH_CONST.__objc_const: 0x3a8
   __AUTH_CONST.__cfstring: 0x4740
-  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x8a8
+  __AUTH_CONST.__auth_got: 0x8b0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1074
+  __DATA.__objc_ivar: 0x107c
   __DATA.__data: 0x1928
   __DATA.__bss: 0x118
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x360
-  __DATA_DIRTY.__objc_const: 0x17e0
+  __DATA_DIRTY.__const: 0x400
+  __DATA_DIRTY.__objc_const: 0x19d8
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x1a8
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3142
-  Symbols:   9843
-  CStrings:  5837
+  Functions: 3146
+  Symbols:   9856
+  CStrings:  5848
 
Symbols:
+ -[RPConnection cloudDaemon]
+ -[RPConnection setCloudDaemon:]
+ -[RPIdentity disabledUntilTicks]
+ -[RPIdentity setDisabledUntilTicks:]
+ _OBJC_IVAR_$_RPConnection._cloudDaemon
+ _OBJC_IVAR_$_RPIdentity._disabledUntilTicks
+ _SecondsToUpTicks
+ ___block_literal_global.1284
+ _objc_msgSend$idsDeviceIDSelf
+ _objc_msgSend$reconfirm
+ _objc_msgSend$setDisabledUntilTicks:
- ___block_literal_global.1274
- _objc_msgSend$setDisabled:
CStrings:
+ "### Rejecting connection to self"
+ "$\x12\"\x11\x13\x11\x11!\"\x11\xbb\x18\x1f\r\x13"
+ "550.8.1"
+ "@\"RPCloudDaemon\""
+ "Rejected connection"
+ "T@\"RPCloudDaemon\",&,N,V_cloudDaemon"
+ "TQ,N,V_disabledUntilTicks"
+ "_cloudDaemon"
+ "_disabledUntilTicks"
+ "cloudDaemon"
+ "disabledUntilTicks"
+ "idsDeviceIDSelf"
+ "reconfirm"
+ "setCloudDaemon:"
+ "setDisabledUntilTicks:"
- "$\x12\"\x11\x13\x11\x11!\"\x11\xbb\x17\x1f\r\x13"
- "542.1"
- "Paired peer removed authentication, invalidating\n"
- "SharedHome peer removed authentication, invalidating\n"

```

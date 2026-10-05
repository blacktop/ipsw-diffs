## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1219.40.7.0.0
-  __TEXT.__text: 0x26d8c
-  __TEXT.__objc_methlist: 0x19cc
+1219.40.10.502.1
+  __TEXT.__text: 0x26e1c
+  __TEXT.__objc_methlist: 0x19e4
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x3dbf
+  __TEXT.__cstring: 0x3e08
   __TEXT.__oslogstring: 0x4235
   __TEXT.__gcc_except_tab: 0x820
   __TEXT.__ustring: 0xa

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2058
+  __DATA_CONST.__const: 0x2078
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf60
+  __DATA_CONST.__objc_selrefs: 0xf70
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x3c00
-  __AUTH_CONST.__objc_const: 0x2370
+  __AUTH_CONST.__cfstring: 0x3c40
+  __AUTH_CONST.__objc_const: 0x23a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x760
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 837
-  Symbols:   1906
-  CStrings:  883
+  Functions: 839
+  Symbols:   1912
+  CStrings:  885
 
Symbols:
+ -[_ACCExternalAccessoryInfo ppidVersionUID]
+ -[_ACCExternalAccessoryInfo setPpidVersionUID:]
+ GCC_except_table58
+ GCC_except_table97
+ _OBJC_IVAR_$__ACCExternalAccessoryInfo._ppidVersionUID
+ _kACCExternalAccessoryPPIDVersionUIDKey
+ _kACCInfo_PPIDVersionUID
+ _kCFACCExternalAccessoryPPIDVersionUIDKey
+ _kCFACCInfo_PPIDVersionUID
- GCC_except_table38
- GCC_except_table42
- GCC_except_table51
Functions:
~ -[_ACCExternalAccessoryInfo initWithAccessoryInfoDictionary:] : 596 -> 632
~ -[_ACCExternalAccessoryInfo description] : 308 -> 340
~ -[_ACCExternalAccessoryInfo updateAccessoryInfo:] : 700 -> 744
+ -[_ACCExternalAccessoryInfo productID]
+ -[_ACCExternalAccessoryInfo setDestinationSharingOptions:]
~ -[_ACCExternalAccessoryInfo .cxx_destruct] : 200 -> 212
CStrings:
+ "<_ACCExternalAccessoryInfo>[%@ name='%@' manu='%@' model='%@' serial='%@' fw(active)='%@', fw(pending)='%@', hw='%@' ppid='%@' ppidVersionUID='%@']"
+ "ACCExternalAccessoryPPIDVersionUIDKey"
+ "PPIDVersionUID"
- "<_ACCExternalAccessoryInfo>[%@ name='%@' manu='%@' model='%@' serial='%@' fw(active)='%@', fw(pending)='%@', hw='%@' ppid='%@']"
```

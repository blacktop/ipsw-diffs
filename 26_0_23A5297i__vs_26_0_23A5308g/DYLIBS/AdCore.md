## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/AdCore`

```diff

-637.1.7.0.0
-  __TEXT.__text: 0x2ca98
+637.1.11.0.0
+  __TEXT.__text: 0x2cc80
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x3de4
+  __TEXT.__objc_methlist: 0x3e0c
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x3d07
+  __TEXT.__cstring: 0x3d93
   __TEXT.__gcc_except_tab: 0x44c
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xb78
+  __TEXT.__unwind_info: 0xb80
   __TEXT.__objc_classname: 0x3a2
-  __TEXT.__objc_methname: 0x70ce
+  __TEXT.__objc_methname: 0x711b
   __TEXT.__objc_methtype: 0xab7
-  __TEXT.__objc_stubs: 0x3ec0
+  __TEXT.__objc_stubs: 0x3f20
   __DATA_CONST.__got: 0x330
   __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ef8
+  __DATA_CONST.__objc_selrefs: 0x1f10
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x4a80
-  __AUTH_CONST.__objc_const: 0x5820
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x5860
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_ivar: 0x3c8
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F75FF731-91E8-3758-A9F8-FCF106CE69D6
-  Functions: 1361
-  Symbols:   4251
-  CStrings:  2786
+  UUID: E920F6F2-D8D0-3369-BC1E-6AF1C4F15F60
+  Functions: 1364
+  Symbols:   4261
+  CStrings:  2799
 
Symbols:
+ -[ADCoreSettings isProtoTeenState]
+ -[DSIDRecord isProtoTeen]
+ -[DSIDRecord setIsProtoTeen:]
+ _OBJC_IVAR_$_DSIDRecord._isProtoTeen
+ ___block_literal_global.280
+ _objc_msgSend$isProtoTeen
+ _objc_msgSend$isProtoTeenState
+ _objc_msgSend$setIsProtoTeen:
- ___block_literal_global.276
Functions:
~ -[DSIDRecord _parseItunesFlags] : 1084 -> 1144
~ -[ADIDManager(AdCore) loadFakeRecord:] : 1648 -> 1760
~ -[DSIDRecord initWithDSID:serializedRecord:version:] : 1500 -> 1536
~ -[DSIDRecord copyWithZone:] : 660 -> 680
~ -[DSIDRecord dictionaryRepresentation] : 1560 -> 1616
~ -[DSIDRecord isRestrictedByApple] : 176 -> 220
+ -[DSIDRecord setActualBirthYear:]
+ -[DSIDRecord iAdIDBeforeReset]
+ -[ADCoreSettings isProtoTeenState]
~ -[ADCoreSettings isAccountRestricted] : 260 -> 300
CStrings:
+ "ProtoAccount"
+ "TB,N,V_isProtoTeen"
+ "This is a fake record but Proto Teen is TRUE. Setting Enabled Proto Teen State"
+ "_isProtoTeen"
+ "isProtoTeen"
+ "isProtoTeenState"
+ "kADDSIDRecord_AccountIsProtoTeenKey"
+ "setIsProtoTeen:"
+ "\x86"
- "v"

```

## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-1394.82.1.0.0
-  __TEXT.__text: 0xd284
+1394.100.151.0.1
+  __TEXT.__text: 0xd3e4
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_methlist: 0xe8c
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x1d4
   __TEXT.__cstring: 0xa43
-  __TEXT.__oslogstring: 0xccd
+  __TEXT.__oslogstring: 0xd11
   __TEXT.__unwind_info: 0x470
-  __TEXT.__objc_classname: 0x1f7
-  __TEXT.__objc_methname: 0x2eae
-  __TEXT.__objc_methtype: 0x8e0
-  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_classname: 0x20a
+  __TEXT.__objc_methname: 0x2ec6
+  __TEXT.__objc_methtype: 0x8f1
+  __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1f50
-  __DATA_CONST.__objc_selrefs: 0xae8
+  __DATA_CONST.__objc_const: 0x2788
+  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_const: 0x5e8

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0x68
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x300
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA308E96-99C2-36A9-B5BB-7DC1DC55D216
-  Functions: 369
-  Symbols:   1453
-  CStrings:  943
+  UUID: 613C5991-D4D5-3243-8C5C-5EAB7F20BEAA
+  Functions: 371
+  Symbols:   1478
+  CStrings:  946
 
Symbols:
+ -[MechanismKofN initWithK:ofSubmechanisms:serial:request:].cold.1
+ -[RemoteUIActivator _sbHandleWithDefinition:configurationContext:].cold.1
+ _OBJC_IVAR_$_MechanismKofN.AND
+ _OBJC_IVAR_$_MechanismKofN.OR
+ _OBJC_IVAR_$_MechanismKofN.k
+ _OBJC_IVAR_$_MechanismKofN.n
+ _OBJC_IVAR_$_MechanismKofN.submechanisms
+ __OBJC_$_PROP_LIST_MechanismComposite
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MechanismComposite
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MechanismComposite
+ __OBJC_$_PROTOCOL_REFS_MechanismComposite
+ __OBJC_CLASS_PROTOCOLS_$_MechanismKofN
+ __OBJC_LABEL_PROTOCOL_$_MechanismComposite
+ __OBJC_PROTOCOL_$_MechanismComposite
+ __OBJC_PROTOCOL_REFERENCE_$_MechanismComposite
+ ___42-[_RemoteUIManager connectRemoteUI:reply:]_block_invoke.128
+ ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.103
+ ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.110
+ ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke_2.111
+ ___block_literal_global.105
+ _objc_msgSend$conformsToProtocol:
- _OBJC_IVAR_$_MechanismKofN._AND
- _OBJC_IVAR_$_MechanismKofN._OR
- _OBJC_IVAR_$_MechanismKofN._k
- _OBJC_IVAR_$_MechanismKofN._n
- _OBJC_IVAR_$_MechanismKofN._submechanisms
- ___42-[_RemoteUIManager connectRemoteUI:reply:]_block_invoke.127
- ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.102
- ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.109
- ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke_2.110
- ___block_literal_global.104
CStrings:
+ "@\"NSArray\"16@0:8"
+ "Failed to create remote alert handle with %{public}@ and %{public}@"
+ "MechanismComposite"
+ "T@\"NSArray\",R,N,Vsubmechanisms"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,GisAND"
+ "TB,R,N,GisAND,VAND"
+ "TB,R,N,GisOR"
+ "TB,R,N,GisOR,VOR"
+ "TQ,R,N"
+ "TQ,R,N,Vk"
+ "TQ,R,N,Vn"
- "T@\"NSArray\",R,N,V_submechanisms"
- "TB,R,N,GisAND,V_AND"
- "TB,R,N,GisOR,V_OR"
- "TQ,R,N,V_k"
- "TQ,R,N,V_n"
- "_AND"
- "_OR"
- "_n"
- "_submechanisms"

```

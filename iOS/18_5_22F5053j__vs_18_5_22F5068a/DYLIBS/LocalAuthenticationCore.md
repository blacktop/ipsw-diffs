## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1656.120.5.0.0
-  __TEXT.__text: 0xcda78
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_methlist: 0x7c48
-  __TEXT.__const: 0x3bb4
-  __TEXT.__cstring: 0xaffb
+1656.120.6.0.0
+  __TEXT.__text: 0xce2b4
+  __TEXT.__auth_stubs: 0x2020
+  __TEXT.__objc_methlist: 0x7cc8
+  __TEXT.__const: 0x3c04
+  __TEXT.__cstring: 0xb14b
   __TEXT.__oslogstring: 0x5029
   __TEXT.__gcc_except_tab: 0x1468
   __TEXT.__dlopen_cstrs: 0x3ac

   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_ret: 0xd4
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3940
+  __TEXT.__unwind_info: 0x3960
   __TEXT.__eh_frame: 0x20e8
-  __TEXT.__objc_classname: 0x1da2
-  __TEXT.__objc_methname: 0xc87c
-  __TEXT.__objc_methtype: 0x3651
-  __TEXT.__objc_stubs: 0x8d60
+  __TEXT.__objc_classname: 0x1dbc
+  __TEXT.__objc_methname: 0xc923
+  __TEXT.__objc_methtype: 0x36bf
+  __TEXT.__objc_stubs: 0x8de0
   __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x3df8
-  __DATA_CONST.__objc_classlist: 0x708
+  __DATA_CONST.__const: 0x3f98
+  __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ff0
+  __DATA_CONST.__objc_selrefs: 0x3030
   __DATA_CONST.__objc_protorefs: 0x208
-  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1008
-  __AUTH_CONST.__auth_ptr: 0x400
+  __AUTH_CONST.__auth_got: 0x1020
+  __AUTH_CONST.__auth_ptr: 0x3f8
   __AUTH_CONST.__const: 0x3118
-  __AUTH_CONST.__cfstring: 0x4e40
-  __AUTH_CONST.__objc_const: 0x31200
+  __AUTH_CONST.__cfstring: 0x5600
+  __AUTH_CONST.__objc_const: 0x31300
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x988
+  __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x734
+  __DATA.__objc_ivar: 0x73c
   __DATA.__data: 0x42f8
   __DATA.__bss: 0x1fa9
   __DATA.__common: 0x40

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5255
-  Symbols:   18553
-  CStrings:  4886
+  Functions: 5266
+  Symbols:   18651
+  CStrings:  4961
 
Symbols:
+ +[LACAccessControl _checkConstraints:contain:]
+ +[LACAccessControl checkACL:hasConstraint:forOperation:]
+ +[LACAccessControl constraintsFromACL:]
+ +[LACAccessControl denyAllACL]
+ +[LACAccessControl deserializeACL:]
+ +[LACAccessControl serializeACL:]
+ -[LACAccessControlOperation .cxx_destruct]
+ -[LACAccessControlOperation initWithTypeErasedOperation:]
+ -[LACAccessControlOperation keyOp]
+ -[LACAccessControlOperation rawValue]
+ _CFDictionaryCreateCopy
+ _LACAccessControlOperationRawValueACL
+ _LACAccessControlOperationRawValueAKS
+ _LACAccessControlOperationRawValueCreateItem
+ _LACAccessControlOperationRawValueCreateKey
+ _LACAccessControlOperationRawValueUseItem
+ _LACAccessControlOperationRawValueUseKeyDecrypt
+ _LACAccessControlOperationRawValueUseKeyKeyExchange
+ _LACAccessControlOperationRawValueUseKeySign
+ _LACPolicyOptionPushButtonUseMaxPreArmAge
+ _NSStringFromLACAccessControlOperationRawValue
+ _OBJC_CLASS_$_LACAccessControlOperation
+ _OBJC_IVAR_$_LACAccessControlOperation._aksOp
+ _OBJC_IVAR_$_LACAccessControlOperation._rawValue
+ _OBJC_METACLASS_$_LACAccessControlOperation
+ _SecAccessControlCreate
+ _SecAccessControlSetConstraints
+ __OBJC_$_INSTANCE_METHODS_LACAccessControlOperation
+ __OBJC_$_INSTANCE_VARIABLES_LACAccessControlOperation
+ __OBJC_$_PROP_LIST_LACAccessControlOperation
+ __OBJC_CLASS_RO_$_LACAccessControlOperation
+ __OBJC_METACLASS_RO_$_LACAccessControlOperation
+ _kAKSKeyACMHandle
+ _kAKSKeyAccessGroups
+ _kAKSKeyAcl
+ _kAKSKeyAclConstraintAccessGroups
+ _kAKSKeyAclConstraintBio
+ _kAKSKeyAclConstraintKofN
+ _kAKSKeyAclConstraintOpBool
+ _kAKSKeyAclConstraintPolicy
+ _kAKSKeyAclConstraintUserPasscode
+ _kAKSKeyAclParamCredentialMaxAge
+ _kAKSKeyAclParamKofN
+ _kAKSKeyAclParamRequirePasscode
+ _kAKSKeyAuthData
+ _kAKSKeyBagId
+ _kAKSKeyData
+ _kAKSKeyExternalData
+ _kAKSKeyFlags
+ _kAKSKeyIterations
+ _kAKSKeyKeybagClass
+ _kAKSKeyKeybagHandle
+ _kAKSKeyOpAttest
+ _kAKSKeyOpComputeKey
+ _kAKSKeyOpCreate
+ _kAKSKeyOpDecrypt
+ _kAKSKeyOpDefaultAcl
+ _kAKSKeyOpDelete
+ _kAKSKeyOpECIESDecrypt
+ _kAKSKeyOpECIESEncrypt
+ _kAKSKeyOpECIESTranscode
+ _kAKSKeyOpEncrpyt
+ _kAKSKeyOpEncrypt
+ _kAKSKeyOpKEMDecapsulate
+ _kAKSKeyOpKEMEncapsulate
+ _kAKSKeyOpSetKeyClass
+ _kAKSKeyOpSign
+ _kAKSKeyOpSync
+ _kAKSKeyOpTranscrypt
+ _kAKSKeyOpUnwrap
+ _kAKSKeyOpWrap
+ _kAKSKeyOperation
+ _kAKSKeyPad
+ _kAKSKeyPasscode
+ _kAKSKeyProtectedData
+ _kAKSKeyPublicKey
+ _kAKSKeyRefKey
+ _kAKSKeyRefKeyMac
+ _kAKSKeySalt
+ _kAKSKeyTag
+ _kAKSKeyType
+ _kAKSKeyUUID
+ _kAKSKeyVersion
+ _kAKSKeyWrappedKey
+ _objc_msgSend$_checkConstraints:contain:
+ _objc_msgSend$constraintsFromACL:
+ _objc_msgSend$deserializeACL:
+ _objc_msgSend$keyOp
CStrings:
+ "@24@0:8^{__SecAccessControl=}16"
+ "ACL"
+ "AKS"
+ "B40@0:8@16@24@32"
+ "Could not initialize trivial ACL (%@)"
+ "Could note deserialize ACL (%@)"
+ "CreateItem"
+ "CreateKey"
+ "LACAccessControlOperation"
+ "UseItem"
+ "UseKeyDecrypt"
+ "UseKeyKeyExchange"
+ "UseKeySign"
+ "^{__SecAccessControl=}16@0:8"
+ "^{__SecAccessControl=}24@0:8@16"
+ "_aksOp"
+ "_checkConstraints:contain:"
+ "acmh"
+ "ad"
+ "ag"
+ "bc"
+ "bh"
+ "bid"
+ "cag"
+ "cbio"
+ "checkACL:hasConstraint:forOperation:"
+ "ckon"
+ "cob"
+ "constraintsFromACL:"
+ "cpo"
+ "cup"
+ "dacl"
+ "denyAllACL"
+ "deserializeACL:"
+ "ed"
+ "f"
+ "initWithTypeErasedOperation:"
+ "iter"
+ "keyOp"
+ "kid"
+ "kt"
+ "kv"
+ "o"
+ "oa"
+ "oacl"
+ "oc"
+ "ock"
+ "od"
+ "odel"
+ "oe"
+ "oecd"
+ "oece"
+ "oect"
+ "okd"
+ "oke"
+ "orwk"
+ "os"
+ "osgn"
+ "oskc"
+ "ouw"
+ "ow"
+ "p"
+ "pad"
+ "pcma"
+ "pd"
+ "pkofn"
+ "prp"
+ "pub"
+ "rk"
+ "rkm"
+ "salt"
+ "serializeACL:"
+ "tag"
+ "wk"

```

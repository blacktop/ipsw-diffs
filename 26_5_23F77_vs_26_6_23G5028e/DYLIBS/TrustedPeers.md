## TrustedPeers

> `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers`

```diff

-61901.120.67.0.0
-  __TEXT.__text: 0x34030
+61901.160.29.0.0
+  __TEXT.__text: 0x343cc
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x3834
+  __TEXT.__objc_methlist: 0x3874
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0xa14
-  __TEXT.__cstring: 0xd5d
+  __TEXT.__cstring: 0xd72
   __TEXT.__oslogstring: 0x1973
   __TEXT.__unwind_info: 0xe20
   __TEXT.__objc_classname: 0x510
-  __TEXT.__objc_methname: 0x6753
-  __TEXT.__objc_methtype: 0xd14
-  __TEXT.__objc_stubs: 0x45e0
+  __TEXT.__objc_methname: 0x6811
+  __TEXT.__objc_methtype: 0xd34
+  __TEXT.__objc_stubs: 0x4620
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d0
+  __DATA_CONST.__objc_selrefs: 0x18f0
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1b20
-  __AUTH_CONST.__objc_const: 0x4e60
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__objc_const: 0x4eb0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x2e4
+  __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x2c0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07BC15B0-689B-333A-B7B1-DEE896A09A11
-  Functions: 1211
-  Symbols:   3784
-  CStrings:  1889
+  UUID: 1AFE30F7-8D77-3A1B-BE92-FE0F56A4F0AE
+  Functions: 1216
+  Symbols:   3797
+  CStrings:  1897
 
Symbols:
+ -[TPModel createStableInfoWithFrozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:]
+ -[TPPBPeerStableInfo hasSupportsTLKOwnership]
+ -[TPPBPeerStableInfo setHasSupportsTLKOwnership:]
+ -[TPPBPeerStableInfo setSupportsTLKOwnership:]
+ -[TPPBPeerStableInfo supportsTLKOwnership]
+ -[TPPeerStableInfo initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:]
+ -[TPPeerStableInfo supportsTLKOwnership]
+ GCC_except_table1166
+ GCC_except_table1174
+ OBJC_IVAR_$_TPPBPeerStableInfo._supportsTLKOwnership
+ ___304-[TPPeerStableInfo initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:]_block_invoke
+ ___Block_byref_object_copy_.3082
+ ___Block_byref_object_dispose_.3083
+ ___block_literal_global.1206
+ ___block_literal_global.1417
+ ___block_literal_global.3091
+ _objc_msgSend$initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:
+ _objc_msgSend$setSupportsTLKOwnership:
+ _objc_msgSend$supportsTLKOwnership
- -[TPModel createStableInfoWithFrozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:]
- -[TPPeerStableInfo initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:]
- GCC_except_table1161
- GCC_except_table1169
- ___283-[TPPeerStableInfo initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:]_block_invoke
- ___Block_byref_object_copy_.3073
- ___Block_byref_object_dispose_.3074
- ___block_literal_global.1208
- ___block_literal_global.1419
- ___block_literal_global.3082
- _objc_msgSend$initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:
CStrings:
+ "@132@0:8@16@24@32i40@44@52@60@68@76@84@92@100@108B116B120^@124"
+ "@140@0:8Q16@24@32@40i48@52@60@68@76@84@92@100@108@116B124B128^@132"
+ "TB,N,V_supportsTLKOwnership"
+ "_supportsTLKOwnership"
+ "createStableInfoWithFrozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:"
+ "hasSupportsTLKOwnership"
+ "initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:supportsTLKOwnership:error:"
+ "setHasSupportsTLKOwnership:"
+ "setSupportsTLKOwnership:"
+ "supportsTLKOwnership"
+ "{?=\"clock\"b1\"flexiblePolicyVersion\"b1\"frozenPolicyVersion\"b1\"userControllableViewStatus\"b1\"isInheritedAccount\"b1\"supportsRepudiation\"b1\"supportsTLKOwnership\"b1}"
- "@128@0:8@16@24@32i40@44@52@60@68@76@84@92@100@108B116^@120"
- "@136@0:8Q16@24@32@40i48@52@60@68@76@84@92@100@108@116B124^@128"
- "createStableInfoWithFrozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:"
- "initWithClock:frozenPolicyVersion:flexiblePolicyVersion:policySecrets:syncUserControllableViews:secureElementIdentity:walrusSetting:webAccess:deviceName:serialNumber:osVersion:signingKeyPair:recoverySigningPubKey:recoveryEncryptionPubKey:isInheritedAccount:error:"
- "{?=\"clock\"b1\"flexiblePolicyVersion\"b1\"frozenPolicyVersion\"b1\"userControllableViewStatus\"b1\"isInheritedAccount\"b1\"supportsRepudiation\"b1}"

```

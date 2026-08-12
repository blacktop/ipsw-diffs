## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-70.37.0.0.0
-  __TEXT.__text: 0x3ab0c
-  __TEXT.__objc_methlist: 0x2c1c
+70.39.1.0.0
+  __TEXT.__text: 0x3ae60
+  __TEXT.__objc_methlist: 0x2c64
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x8bc2
-  __TEXT.__oslogstring: 0x23fe
+  __TEXT.__cstring: 0x8d46
+  __TEXT.__oslogstring: 0x249c
   __TEXT.__gcc_except_tab: 0x1208
-  __TEXT.__unwind_info: 0xe18
+  __TEXT.__unwind_info: 0xe28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1618
+  __DATA_CONST.__objc_selrefs: 0x1648
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x250
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x2c60
+  __AUTH_CONST.__cfstring: 0x2ce0
   __AUTH_CONST.__objc_const: 0x4ef0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1098
-  Symbols:   2328
-  CStrings:  1000
+  Functions: 1104
+  Symbols:   2343
+  CStrings:  1008
 
Symbols:
+ -[DAKeyManagementSession deleteKey:reason:completionHandler:]
+ -[DAKeyManagementSession localDeleteKey:reason:completionHandler:]
+ -[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:deviceTransfer:ourBindingAttestation:config:completionHandler:]
+ -[KmlSettingsManager creationBlockParamsForStrategy:threshold:windowInDays:]
+ -[KmlSettingsManager ignorePendingPairingCreationBlock]
+ -[KmlSettingsManager pendingPairingCreationBlockStrategy]
+ GCC_except_table102
+ GCC_except_table14
+ GCC_except_table20
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table9
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ ___148-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:deviceTransfer:ourBindingAttestation:config:completionHandler:]_block_invoke
+ ___61-[DAKeyManagementSession deleteKey:reason:completionHandler:]_block_invoke
+ ___66-[DAKeyManagementSession localDeleteKey:reason:completionHandler:]_block_invoke
+ _objc_msgSend$createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:deviceTransfer:ourBindingAttestation:config:completionHandler:
+ _objc_msgSend$deleteKey:reason:callback:
+ _objc_msgSend$deleteKey:reason:completionHandler:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$localDeleteKey:reason:callback:
+ _objc_msgSend$localDeleteKey:reason:completionHandler:
- GCC_except_table100
- GCC_except_table11
- GCC_except_table28
- GCC_except_table37
- GCC_except_table40
- GCC_except_table43
- GCC_except_table47
- GCC_except_table50
- GCC_except_table59
- GCC_except_table62
- GCC_except_table65
- GCC_except_table68
- GCC_except_table73
- GCC_except_table74
- GCC_except_table76
- GCC_except_table77
- GCC_except_table79
- GCC_except_table80
- GCC_except_table82
- GCC_except_table83
- GCC_except_table85
- GCC_except_table86
- GCC_except_table88
- GCC_except_table89
- GCC_except_table91
- GCC_except_table92
- GCC_except_table94
- GCC_except_table95
- GCC_except_table97
- GCC_except_table98
- ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke
- ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke
- ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke
- _objc_msgSend$deleteKey:callback:
- _objc_msgSend$localDeleteKey:callback:
- _objc_msgSend$unsignedIntegerValue
CStrings:
+ "%s : %i : Invalid pending pairing creation block strategy %ld; using default (10-in-14)"
+ "%s : %i : Using pending pairing creation block strategy override: %ld"
+ "-[DAKeyManagementSession deleteKey:reason:completionHandler:]"
+ "-[DAKeyManagementSession deleteKey:reason:completionHandler:]_block_invoke"
+ "-[DAKeyManagementSession localDeleteKey:reason:completionHandler:]"
+ "-[DAKeyManagementSession localDeleteKey:reason:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:deviceTransfer:ourBindingAttestation:config:completionHandler:]"
+ "-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:deviceTransfer:ourBindingAttestation:config:completionHandler:]_block_invoke"
+ "-[KmlSettingsManager pendingPairingCreationBlockStrategy]"
+ "PendingPairingCreationBlockStrategy"
+ "Unspecified"
+ "debug.IgnorePendingPairingCreationBlock"
+ "debug.pendingPairingCreationBlockStrategyOverride"
- "-[DAKeyManagementSession deleteKey:completionHandler:]"
- "-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke"
- "-[DAKeyManagementSession localDeleteKey:completionHandler:]"
- "-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke"
- "-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke"
```

## KerberosHelper

> `/System/Library/PrivateFrameworks/KerberosHelper.framework/Versions/A/KerberosHelper`

```diff

-163.0.1.0.0
-  __TEXT.__text: 0x97b8
+163.100.1.0.0
+  __TEXT.__text: 0x9530
   __TEXT.__auth_stubs: 0xb90
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0xc93
   __TEXT.__oslogstring: 0xc61
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x188
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x730
   __AUTH_CONST.__auth_got: 0x5c8

   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
-  UUID: 5EE727F5-3CF7-3DE0-B2D2-D38BE844135C
-  Functions: 132
-  Symbols:   447
+  UUID: 1DD364BF-AFF2-388A-95BB-9C5AEF1F1EBB
+  Functions: 137
+  Symbols:   488
   CStrings:  350
 
Symbols:
+ CredChange.cold.1
+ CredChange.cold.2
+ CredChange.cold.3
+ NAHAddReferenceAndLabel.cold.1
+ NAHCreate.cold.1
+ NAHCreate.cold.10
+ NAHCreate.cold.11
+ NAHCreate.cold.12
+ NAHCreate.cold.2
+ NAHCreate.cold.3
+ NAHCreate.cold.4
+ NAHCreate.cold.5
+ NAHCreate.cold.6
+ NAHCreate.cold.7
+ NAHCreate.cold.8
+ NAHCreate.cold.9
+ NAHFindByLabelAndRelease.cold.1
+ NAHSelectionAcquireCredential.cold.1
+ NAHSelectionAcquireCredential.cold.10
+ NAHSelectionAcquireCredential.cold.11
+ NAHSelectionAcquireCredential.cold.12
+ NAHSelectionAcquireCredential.cold.13
+ NAHSelectionAcquireCredential.cold.14
+ NAHSelectionAcquireCredential.cold.15
+ NAHSelectionAcquireCredential.cold.16
+ NAHSelectionAcquireCredential.cold.17
+ NAHSelectionAcquireCredential.cold.2
+ NAHSelectionAcquireCredential.cold.3
+ NAHSelectionAcquireCredential.cold.4
+ NAHSelectionAcquireCredential.cold.5
+ NAHSelectionAcquireCredential.cold.6
+ NAHSelectionAcquireCredential.cold.7
+ NAHSelectionAcquireCredential.cold.8
+ NAHSelectionAcquireCredential.cold.9
+ __NAHFindByLabelAndRelease_block_invoke.cold.1
+ addSecItem.cold.1
+ addSelection.cold.1
+ addSelection.cold.2
+ updateError.cold.1
+ use_existing_principals.cold.1
+ use_existing_principals.cold.2
Functions:
~ _KRBCreateSessionInfo : 3892 -> 3824
~ _is_local_hostname : 128 -> 132
~ _KRBDecodeNegTokenInit : 760 -> 724
~ __CFNetServiceDeconstructServiceName : 1132 -> 1128
~ _ConvertDomainLabelToCString_withescape : 140 -> 144
~ _NAHCreate : 4744 -> 4548
~ _addSecItem : 460 -> 444
~ _NAHSelectionAcquireCredential : 4344 -> 4056
~ _updateError : 328 -> 312
~ _NAHSelectionGetInfoForKey : 528 -> 516
~ _NAHAddReferenceAndLabel : 304 -> 288
~ _CredChange : 1028 -> 980
~ _NAHFindByLabelAndRelease : 320 -> 304
~ ___NAHFindByLabelAndRelease_block_invoke : 292 -> 276
~ _NAHSelectionGetGSSMech : 60 -> 56
~ _name2oid : 100 -> 96
~ _use_existing_principals : 1148 -> 1124
~ _addSelection : 792 -> 756
~ _add_realms : 260 -> 264

```

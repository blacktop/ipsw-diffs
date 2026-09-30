## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-398.106.0.0.0
-  __TEXT.__text: 0x72868
+398.109.0.0.0
+  __TEXT.__text: 0x728c8
   __TEXT.__auth_stubs: 0x1110
   __TEXT.__objc_methlist: 0xc28
-  __TEXT.__gcc_except_tab: 0xac98
+  __TEXT.__gcc_except_tab: 0xacc8
   __TEXT.__const: 0xc20
   __TEXT.__cstring: 0x4f36
   __TEXT.__oslogstring: 0x4e7a

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE0733CB-1C3D-379E-B2D7-FBBAFAC90A41
+  UUID: 42306953-5AD3-30E4-BA11-3D1E5FE0B708
   Functions: 1661
-  Symbols:   5752
+  Symbols:   5754
   CStrings:  1582
 
Symbols:
+ __ZN4avas6server20LegacySessionManager20PrivateRemoveSessionERN5caulk10sync_guardINS0_17SessionCollectionENS2_4mach11unfair_lockEEEjRKNS0_15ProcessIdentityEP19NSMutableDictionary.cold.4
Functions:
~ __ZZNK4avas6server20LegacySessionManager33FindSessionAndVerifyOwnershipPrivINS0_17SessionCollection25SessionPresentingIteratorEEET_S5_S5_jRKNS0_15ProcessIdentityERKNSt3__18optionalINS1_24EntitlementExceptionTypeEEEENKUlRKS5_E_clINS9_4pairIjNS9_10shared_ptrINS0_18ISessionPresentingEEEEEEEDaSG_ : 524 -> 480
~ __ZN4avas6server20LegacySessionManager20PrivateRemoveSessionERN5caulk10sync_guardINS0_17SessionCollectionENS2_4mach11unfair_lockEEEjRKNS0_15ProcessIdentityEP19NSMutableDictionary : 3904 -> 4088
~ __ZZNK4avas6server20LegacySessionManager33FindSessionAndVerifyOwnershipPrivINSt3__120__map_const_iteratorINS3_21__tree_const_iteratorINS3_12__value_typeIjNS3_10shared_ptrINS0_16AudioSessionInfoEEEEEPNS3_11__tree_nodeISA_PvEElEEEEEET_SH_SH_jRKNS0_15ProcessIdentityERKNS3_8optionalINS1_24EntitlementExceptionTypeEEEENKUlRKSH_E_clINS3_4pairIKjS9_EEEEDaSR_ : 524 -> 480

```

## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-319.122.4.0.0
-  __TEXT.__text: 0x39c4
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x5b8
-  __TEXT.__cstring: 0x45f7
+417.0.0.502.1
+  __TEXT.__text: 0x41a4
+  __TEXT.__const: 0x768
+  __TEXT.__cstring: 0x57e1
   __TEXT.__oslogstring: 0x39b
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xbb8
-  __AUTH_CONST.__auth_got: 0x140
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 763091CF-262F-38A9-B971-006BEECD3B5F
-  Functions: 25
-  Symbols:   86
-  CStrings:  440
+  UUID: EBFD0321-0578-3D58-B7B9-D43AF4F4A6DB
+  Functions: 28
+  Symbols:   87
+  CStrings:  549
 
Symbols:
+ ___block_descriptor_tmp.508
+ _os_eligibility_bring_up_daemon_4_migration
+ _os_eligibility_bring_up_daemon_4_secure_erase
+ _os_eligibility_diff_mobile_asset
- ___block_descriptor_tmp.400
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "OS_ELIGIBILITY_DOMAIN_ADALIA"
+ "OS_ELIGIBILITY_DOMAIN_ADULT_AGE_VERIFICATION_STATUS_REQUIRED_SPYGLASS"
+ "OS_ELIGIBILITY_DOMAIN_AGONUM"
+ "OS_ELIGIBILITY_DOMAIN_AGRILUS"
+ "OS_ELIGIBILITY_DOMAIN_AGRIOTES"
+ "OS_ELIGIBILITY_DOMAIN_AMARA"
+ "OS_ELIGIBILITY_DOMAIN_ANATIS"
+ "OS_ELIGIBILITY_DOMAIN_ANTHOCHARIS"
+ "OS_ELIGIBILITY_DOMAIN_BEMBIDION"
+ "OS_ELIGIBILITY_DOMAIN_BUPRESTIS"
+ "OS_ELIGIBILITY_DOMAIN_CALOSOMA"
+ "OS_ELIGIBILITY_DOMAIN_CALVIA"
+ "OS_ELIGIBILITY_DOMAIN_CARABUS"
+ "OS_ELIGIBILITY_DOMAIN_CELASTRINA"
+ "OS_ELIGIBILITY_DOMAIN_CHLAENIUS"
+ "OS_ELIGIBILITY_DOMAIN_CHRYSOBOTHRIS"
+ "OS_ELIGIBILITY_DOMAIN_CICINDELA"
+ "OS_ELIGIBILITY_DOMAIN_COCCINELLA"
+ "OS_ELIGIBILITY_DOMAIN_COLIAS"
+ "OS_ELIGIBILITY_DOMAIN_CTENICERA"
+ "OS_ELIGIBILITY_DOMAIN_CURCULIO"
+ "OS_ELIGIBILITY_DOMAIN_DICERCA"
+ "OS_ELIGIBILITY_DOMAIN_ELAPHRUS"
+ "OS_ELIGIBILITY_DOMAIN_ELATER"
+ "OS_ELIGIBILITY_DOMAIN_ERGATES"
+ "OS_ELIGIBILITY_DOMAIN_EUCHLOE"
+ "OS_ELIGIBILITY_DOMAIN_GLAUCOPSYCHE"
+ "OS_ELIGIBILITY_DOMAIN_HARPALUS"
+ "OS_ELIGIBILITY_DOMAIN_HYLOBIUS"
+ "OS_ELIGIBILITY_DOMAIN_LEBIA"
+ "OS_ELIGIBILITY_DOMAIN_LIMONIUS"
+ "OS_ELIGIBILITY_DOMAIN_LISTRONOTUS"
+ "OS_ELIGIBILITY_DOMAIN_LYCAENA"
+ "OS_ELIGIBILITY_DOMAIN_MELANOPHILA"
+ "OS_ELIGIBILITY_DOMAIN_MELANOTUS"
+ "OS_ELIGIBILITY_DOMAIN_MONOCHAMUS"
+ "OS_ELIGIBILITY_DOMAIN_NEOPHASIA"
+ "OS_ELIGIBILITY_DOMAIN_NOTIOPHILUS"
+ "OS_ELIGIBILITY_DOMAIN_OTIORHYNCHUS"
+ "OS_ELIGIBILITY_DOMAIN_PAPILIO"
+ "OS_ELIGIBILITY_DOMAIN_PARNASSIUS"
+ "OS_ELIGIBILITY_DOMAIN_PISSODES"
+ "OS_ELIGIBILITY_DOMAIN_PLEBEJUS"
+ "OS_ELIGIBILITY_DOMAIN_PRIONUS"
+ "OS_ELIGIBILITY_DOMAIN_PSYLLOBORA"
+ "OS_ELIGIBILITY_DOMAIN_PTEROSTICHUS"
+ "OS_ELIGIBILITY_DOMAIN_SCAPHINOTUS"
+ "OS_ELIGIBILITY_DOMAIN_SITONA"
+ "OS_ELIGIBILITY_DOMAIN_TACHYS"
+ "OS_ELIGIBILITY_DOMAIN_TRECHUS"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_BACKGROUND_RESTRICTION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_BACKGROUND_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "OS_ELIGIBILITY_DOMAIN_XYLOTRECHUS"
+ "OS_ELIGIBILITY_INPUT_DEVICE_SIRI_MODE"
+ "OS_ELIGIBILITY_INPUT_HAS_LINWOOD"
+ "com.apple.os-eligibility-domain.change.adalia"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-status-required-spyglass"
+ "com.apple.os-eligibility-domain.change.agonum"
+ "com.apple.os-eligibility-domain.change.agrilus"
+ "com.apple.os-eligibility-domain.change.agriotes"
+ "com.apple.os-eligibility-domain.change.amara"
+ "com.apple.os-eligibility-domain.change.anatis"
+ "com.apple.os-eligibility-domain.change.anthocharis"
+ "com.apple.os-eligibility-domain.change.bembidion"
+ "com.apple.os-eligibility-domain.change.buprestis"
+ "com.apple.os-eligibility-domain.change.calosoma"
+ "com.apple.os-eligibility-domain.change.calvia"
+ "com.apple.os-eligibility-domain.change.carabus"
+ "com.apple.os-eligibility-domain.change.celastrina"
+ "com.apple.os-eligibility-domain.change.chlaenius"
+ "com.apple.os-eligibility-domain.change.chrysobothris"
+ "com.apple.os-eligibility-domain.change.cicindela"
+ "com.apple.os-eligibility-domain.change.coccinella"
+ "com.apple.os-eligibility-domain.change.colias"
+ "com.apple.os-eligibility-domain.change.ctenicera"
+ "com.apple.os-eligibility-domain.change.curculio"
+ "com.apple.os-eligibility-domain.change.dicerca"
+ "com.apple.os-eligibility-domain.change.elaphrus"
+ "com.apple.os-eligibility-domain.change.elater"
+ "com.apple.os-eligibility-domain.change.ergates"
+ "com.apple.os-eligibility-domain.change.euchloe"
+ "com.apple.os-eligibility-domain.change.glaucopsyche"
+ "com.apple.os-eligibility-domain.change.harpalus"
+ "com.apple.os-eligibility-domain.change.hylobius"
+ "com.apple.os-eligibility-domain.change.lebia"
+ "com.apple.os-eligibility-domain.change.limonius"
+ "com.apple.os-eligibility-domain.change.listronotus"
+ "com.apple.os-eligibility-domain.change.lycaena"
+ "com.apple.os-eligibility-domain.change.melanophila"
+ "com.apple.os-eligibility-domain.change.melanotus"
+ "com.apple.os-eligibility-domain.change.monochamus"
+ "com.apple.os-eligibility-domain.change.neophasia"
+ "com.apple.os-eligibility-domain.change.notiophilus"
+ "com.apple.os-eligibility-domain.change.otiorhynchus"
+ "com.apple.os-eligibility-domain.change.papilio"
+ "com.apple.os-eligibility-domain.change.parnassius"
+ "com.apple.os-eligibility-domain.change.pissodes"
+ "com.apple.os-eligibility-domain.change.plebejus"
+ "com.apple.os-eligibility-domain.change.prionus"
+ "com.apple.os-eligibility-domain.change.psyllobora"
+ "com.apple.os-eligibility-domain.change.pterostichus"
+ "com.apple.os-eligibility-domain.change.scaphinotus"
+ "com.apple.os-eligibility-domain.change.sitona"
+ "com.apple.os-eligibility-domain.change.tachys"
+ "com.apple.os-eligibility-domain.change.trechus"
+ "com.apple.os-eligibility-domain.change.unverified-adult-background-restriction-required"
+ "com.apple.os-eligibility-domain.change.unverified-adult-background-restriction-required-mini-buddy"
+ "com.apple.os-eligibility-domain.change.xylotrechus"
+ "mobileAssetDiffDictionary"

```

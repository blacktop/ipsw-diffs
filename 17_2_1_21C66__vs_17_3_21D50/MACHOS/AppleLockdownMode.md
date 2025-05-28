## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

 65.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x43a9
-  __TEXT_EXEC.__text: 0x13a24
+  __TEXT.__cstring: 0x446f
+  __TEXT_EXEC.__text: 0x13bb0
   __TEXT_EXEC.__auth_stubs: 0x230
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1360
+  __DATA_CONST.__kalloc_var: 0x1400
   Functions: 168
-  Symbols:   604
-  CStrings:  462
+  Symbols:   606
+  CStrings:  466
 
Symbols:
+ Util_AllocRequirement.kalloc_type_view_383
+ Util_DeallocRequirement.kalloc_type_view_577
CStrings:
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
+ "requirement->type == kACMRequirementTypeRatchet"
+ "site.ACMRequirement.ACMRequirementDataRatchet"

```

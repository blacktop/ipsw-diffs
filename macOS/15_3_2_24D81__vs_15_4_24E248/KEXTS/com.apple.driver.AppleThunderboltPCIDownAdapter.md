## com.apple.driver.AppleThunderboltPCIDownAdapter

> `com.apple.driver.AppleThunderboltPCIDownAdapter`

```diff

-437.0.0.0.0
-  __TEXT.__cstring: 0x106e
-  __TEXT_EXEC.__text: 0x5368
+438.0.0.0.0
+  __TEXT.__cstring: 0x127e
+  __TEXT_EXEC.__text: 0x5654
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x18a0
+  __DATA_CONST.__const: 0x18c0
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 0B9D73C5-B4E8-3DED-98EE-7259F0B894AD
-  Functions: 73
-  Symbols:   492
-  CStrings:  61
+  UUID: 7AFC4204-DC27-3FA5-B64B-B2549EE47850
+  Functions: 75
+  Symbols:   494
+  CStrings:  66
 
Symbols:
+ __ZN30AppleThunderboltPCIDownAdapter25activateSetLegacyPropertyEv
+ __ZN30AppleThunderboltPCIDownAdapter30deactivateRemoveLegacyPropertyEv
CStrings:
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - fCorrelatedPCIDevice = %p, fProviderPort = %p\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - switch needs extended link training, add legacy property to correlated PCI\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - the_switch = %p\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::deactivateRemoveLegacyProperty - remove legacy property from correlated PCI\n"
+ "PCI-Thunderbolt-Legacy"

```

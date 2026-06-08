## com.apple.driver.AppleInterruptControllerV3

> `com.apple.driver.AppleInterruptControllerV3`

```diff

-94.0.0.0.0
-  __TEXT.__cstring: 0xae8
-  __TEXT_EXEC.__text: 0x4328
+98.0.0.0.0
+  __TEXT.__cstring: 0xb75
+  __TEXT_EXEC.__text: 0x4470
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xfd8
   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 669CABD9-A35E-3D09-A776-850840565522
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x68
+  UUID: 38DF8CD2-0395-3C1B-8B5E-71D1C81C7C1D
   Functions: 122
   Symbols:   0
-  CStrings:  70
+  CStrings:  72
 
Functions:
~ __ZN26AppleInterruptControllerV35startEP9IOService -> sub_fffffe0008ff9210 : 2704 -> 2912
~ sub_fffffe0008d22bc8 -> sub_fffffe0008ff9f98 : 724 -> 808
~ __ZN26AppleInterruptControllerV315handleInterruptEPvP9IOServicei -> sub_fffffe0008ffaab4 : 660 -> 696
CStrings:
+ "\"Interrupt storm: last int %d total int fired %lld times, iack=%x, vector=%p,storm_debug=%p, index=%lld\" @%s:%d"
+ "1211111212221212111111222222222222222222222111111111112221121111111212121212122111211211211211211211211211211211211211211211211211211211211211211211211211211"
+ "AppleInterruptControllerV3::_aicPlatformQuiesceActions: Unmask %u interrupts required in SLP_MEDIA\n"
+ "sleep-unmasked-interrupts"
- "\"Interrupt storm: last int %d total int fired %lld times, iack=%x, vector=%p,storm_debug=%p\" @%s:%d"
- "1211111212221212111111222222222222222222221111111111222111111111212121212122111211211211211211211211211211211211211211211211211211211211211211211211211211"

```

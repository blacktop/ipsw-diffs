## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x19274 sha256:2ebbd066d6a5cc6e8278b3ac0f8904d78089b0692f2cc1228f45d92d83bfe743
-  __TEXT.__auth_stubs: 0x7c0 sha256:d1aa19f1a83f23da3fc6544f17098db02b194e8394aac03252938a344f226343
-  __TEXT.__const: 0x130 sha256:c58ec6472e7fb3bf8660de07b898bb20a22532db30149c91bb52afe354b0ad6e
-  __TEXT.__cstring: 0x2e37 sha256:873cd6e4414657ae46596a15e231a39f846e801374248e0baaca33835a1c4182
-  __TEXT.__oslogstring: 0x257d sha256:e72e9d50068301b0d2f61e8faa0f1fff9daa043acafdfb4d4cbc847937759686
-  __TEXT.__unwind_info: 0x258 sha256:d339786081b6e9d7eb0889e6a660f9fd578dce16def0cc8d00eab3657cc048e9
-  __DATA_CONST.__got: 0x70 sha256:b5fdab78d8947eacc864bfeecb4d2100780e5afe1cd8efafb124887913ac49fa
-  __DATA_CONST.__const: 0x268 sha256:d3ace2b7cd1a513c34ee504fa51fe2ed216e86dcd6c9c0cf88ffcbe4ef7e46f9
-  __AUTH_CONST.__auth_got: 0x3e0 sha256:5f51d9e57c051cc516388346d860976bff3531da9561f6570c19b2ca2da48eab
-  __AUTH_CONST.__const: 0x100 sha256:1a41bf91dc917d19cc8df0d5b884d37f83ea0296b6ab68a30521d97a0690cb0d
-  __AUTH_CONST.__cfstring: 0x380 sha256:33b572e2a8d6d527a3a4023ed6868fca7eda2e4775de7cf270dc1b971493dd1a
-  __DATA_DIRTY.__data: 0x1 sha256:4bf5122f344554c53bde2ebb8cd2b7e3d1600ad631c385a5d7cce23c7785459a
+370.33.1.0.0
+  __TEXT.__text: 0x180a0 sha256:facaf5555d1a528e8cbf11a4ccc277e8bdb3986d5b0c236c018fde501acc725e
+  __TEXT.__const: 0x120 sha256:66fa1225fe3ff2707b7c03e30c7f4eeced25f80403ea8e7fec10f1a58f0cda39
+  __TEXT.__cstring: 0x2e33 sha256:a16b9ee56e283199109eb9b0bca0d470462f839e9df51fbd4af5fd1318163baf
+  __TEXT.__oslogstring: 0x2570 sha256:eef610a3f7aef7fa7e5831287631307f6dc1f503fc210ed4ce089113c33d7366
+  __TEXT.__unwind_info: 0x250 sha256:ce8e56facdb5b9e417c7f7a172a2c2477cb5ca738ed2142d19a8fbc2f6a2a2c8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x268 sha256:68a708e58215ab68233547e3d8ba8137d841a779348bf892ee58a31621c33fab
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x100 sha256:1642c72a87b2b8ce55feafba943d4b91c4eca77ce03d82a2bb4f9e6e87c721d8
+  __AUTH_CONST.__cfstring: 0x360 sha256:ec1e960f69fb2be7b770f7f30503d18821946863dcf23338b919b1fddf20bc16
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA_DIRTY.__data: 0x2 sha256:9dcf97a184f32623d11a73124ceb99a5709b083721e878a16d78f596718ba7b2
   __DATA_DIRTY.__bss: 0x248 sha256:62ec1707572ac5078d31a687a5d23de0c6d2a58d3462efb7039957548a7986cc
   __DATA_DIRTY.__common: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 93AF3F23-E5B9-37D4-A4D4-03630F9D2800
-  Functions: 180
-  Symbols:   275
-  CStrings:  674
+  UUID: 4F7610C1-9281-3BAF-983F-158A631B4D0C
+  Functions: 178
+  Symbols:   273
+  CStrings:  676
 
Symbols:
+ _NFHardwareGPIOSetPowerToggle
+ _NFHardwareInterfaceSetPowerToggle
+ _postAnalyticsResetTimingEvent
- _NFHardwareInterfaceIsHammerfestAlive
- _NFHardwareInterfaceRead
- _NFHardwareInterfaceReadAbort
- _NFHardwareInterfaceWrite
- _NFHardwareSerialIsHammerfestAlive
CStrings:
+ "%s:%i enable toggle=%llu"
+ "%{public}s:%i enable toggle=%llu"
+ "NFHardwareGPIOSetPowerToggle"
+ "_phTmlNfc_PowerToggle"
+ "download_mode"
+ "download_mode_no_ven"
+ "normal_mode"
+ "normal_mode_no_ven"
+ "power_off"
+ "spmi_follower_reset"
- "%s:%i Using blocking socket for relay"
- "%{public}s:%i Using blocking socket for relay"
- "NFHardwareInterfaceRead"
- "NFHardwareSerialIsHammerfestAlive"
- "hammerfest-data-available-event"
- "nfc,secondary,spmi"
- "phTmlNfc_ConfigureTestParams"

```

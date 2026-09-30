## libVinylUpdater.dylib

> `/usr/lib/updaters/libVinylUpdater.dylib`

```diff

-143.0.0.0.0
-  __TEXT.__text: 0x35fe0
+144.0.0.0.0
+  __TEXT.__text: 0x35ea4
   __TEXT.__auth_stubs: 0x16a0
   __TEXT.__init_offsets: 0x38
-  __TEXT.__gcc_except_tab: 0x309c
-  __TEXT.__cstring: 0x7dfe
+  __TEXT.__gcc_except_tab: 0x308c
+  __TEXT.__cstring: 0x7d7c
   __TEXT.__const: 0x3661
   __TEXT.__oslogstring: 0x7c
   __TEXT.__unwind_info: 0x13d0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 214571E7-6CC7-3BDE-A6C7-565536A666DD
+  UUID: 763F5CB8-7CE9-3C3B-B82F-1867B39BA040
   Functions: 924
   Symbols:   2916
-  CStrings:  1222
+  CStrings:  1218
 
Symbols:
+ ___cxx_global_var_init.22
- ___cxx_global_var_init.25
Functions:
~ __ZN5eUICC12VinylFactory8GetValveEPvibNSt3__110shared_ptrIvEE : 520 -> 196
~ __ZN5eUICC6isLETOERNSt3__110unique_ptrINS_15eUICCVinylValveENS0_14default_deleteIS2_EEEE -> __ZN5eUICC20getPairingIdentifierEPPK14__CFDictionary : 52 -> 320
~ __ZN5eUICC20getPairingIdentifierEPPK14__CFDictionary -> __ZN5eUICC6getEIDEPPK14__CFDictionaryRNSt3__110unique_ptrINS_15eUICCVinylValveENS4_14default_deleteIS6_EEEE : 320 -> 936
~ __ZN5eUICC6getEIDEPPK14__CFDictionaryRNSt3__110unique_ptrINS_15eUICCVinylValveENS4_14default_deleteIS6_EEEE -> __ZN5eUICC11checkEOSDevEPbRNSt3__110unique_ptrINS_15eUICCVinylValveENS1_14default_deleteIS3_EEEE : 936 -> 556
~ __ZN5eUICC11checkEOSDevEPbRNSt3__110unique_ptrINS_15eUICCVinylValveENS1_14default_deleteIS3_EEEE -> __ZN5eUICC6isLETOERNSt3__110unique_ptrINS_15eUICCVinylValveENS0_14default_deleteIS2_EEEE : 556 -> 52
~ ____ZN5eUICC18eUICCVinylMAVValve15HardwareHasESIMERh_block_invoke : 304 -> 312
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B3UxugAk1tQWl3hWAkQfz4mygpcDOieBK7HPtNw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "VinylRestore-144~127"
- "/AppleInternal/Library/BuildRoots/4~B2AGugBZ_np8VItXFRjcq-chWqq1BBFvNVQRNIk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "GetValve"
- "LETO-capable device detected! Attempt to enable eUICC.\n"
- "VinylRestore-143~561"
- "eUICC enabled, mux switch success!\n"
- "eUICC not enabled, aborted!\n"

```

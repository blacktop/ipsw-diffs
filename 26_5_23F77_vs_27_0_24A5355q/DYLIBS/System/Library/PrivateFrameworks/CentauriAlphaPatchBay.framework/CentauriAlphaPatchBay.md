## CentauriAlphaPatchBay

> `/System/Library/PrivateFrameworks/CentauriAlphaPatchBay.framework/CentauriAlphaPatchBay`

```diff

-72.129.725.0.0
-  __TEXT.__text: 0xf34 sha256:7ab824ec9166427b8fee9cd2b91c59666758dfae4fa28b47a1aace385ba23438
-  __TEXT.__auth_stubs: 0x100 sha256:066f8aa2eb914fcfccaa988cc1a0c2a02d584791cf60ce33904b3bb8385c24a4
-  __TEXT.__const: 0x10 sha256:59f2921ddd453068345a7e49e971e7f67ff13e666d0dfaf5665a22df4204d43d
-  __TEXT.__cstring: 0x12e sha256:2bfe3afc4c0fc56489db21bf946ef966715b1d46d64c796b891bae794bc5ef95
-  __TEXT.__oslogstring: 0x1cf sha256:75fbad4e77eb0191cd35d6f331b9233561700016ba3dd29780c3ada1f0acace4
-  __TEXT.__unwind_info: 0x78 sha256:2388b21441d863cbcf932d0a68dbe38f801344e1507892e93d1bc516bfe44c16
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
-  __AUTH_CONST.__auth_got: 0x80 sha256:38723a2e5e8a17aa7950dc008209944e898f69a7bd10a23c839d341e935fd5ca
-  __AUTH_CONST.__cfstring: 0x100 sha256:e7f2c811f35004ffcd0d6632721ad9487c6d24fb9d28d7ab8d360be9f1a8a12d
+91.58.1.0.0
+  __TEXT.__text: 0x12ac sha256:ef4388ffe183c5fb6eb7e0ac5bc695efb724b63c46d8c32c8e238a2af1db1ffc
+  __TEXT.__const: 0x18 sha256:6b233b3549281d28decf50dbd511aa98f26f1e0182e14d3bc75ecb4a7aa3df8e
+  __TEXT.__oslogstring: 0x33d sha256:bd394629e7c29c553650e00e2d191f26b90d4b6e951001604eb01ee2c328df0f
+  __TEXT.__cstring: 0x160 sha256:919c59d19efb75cd828dff02fd07c994671dcf50ca51c28b1fc8f8b1941acba1
+  __TEXT.__unwind_info: 0x78 sha256:18e17c9510e16844055c0b53a117f795af96019df7f75dad80a6ab8ca1a4a358
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x180 sha256:9fb2cce2a93ab3c0895541caa23ae3a3a6d8b4af7ece45429794656cb1281851
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 3CB79A57-D969-388C-A272-461A11D3ECC8
-  Functions: 26
-  Symbols:   72
-  CStrings:  35
+  UUID: 0B5D8763-4E04-3879-A06C-0F8BD42D4D4B
+  Functions: 27
+  Symbols:   78
+  CStrings:  53
 
Symbols:
+ _AddPatchbayItem
+ _CFStringHasSuffix
+ _CentauriAlphaPatchBayCopyData.cold.3
+ _CentauriAlphaPatchBayCopyData.cold.4
+ _MGCopyAnswer
+ _arc4random
+ _memcpy
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
CStrings:
+ "%s: CentauriAlphaPatchBayCopyData"
+ "%s: adding patchbay item. item_type 0x%x, size 0x%x, cur_item offset 0x%x"
+ "%s: cannot add patchbay item. item_type 0x%x, size 0x%x, cur_item offset 0x%x"
+ "%s: failed to get HWModelStr; assuming AP"
+ "%s: failed to load all PPM data"
+ "%s: getUint8FromIOReg"
+ "%s: ppm EDT read success"
+ "%s: setting board type to AP"
+ "%s: setting board type to DEV"
+ "AddPatchbayItem"
+ "DEV"
+ "HWModelStr"
+ "dev"
+ "ppm-alert-conf"

```

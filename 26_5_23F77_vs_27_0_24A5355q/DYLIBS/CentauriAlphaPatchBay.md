## CentauriAlphaPatchBay

> `/System/Library/PrivateFrameworks/CentauriAlphaPatchBay.framework/CentauriAlphaPatchBay`

```diff

-72.129.725.0.0
-  __TEXT.__text: 0xf34
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x12e
-  __TEXT.__oslogstring: 0x1cf
+91.58.1.0.0
+  __TEXT.__text: 0x12ac
+  __TEXT.__const: 0x18
+  __TEXT.__oslogstring: 0x33d
+  __TEXT.__cstring: 0x160
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__got: 0x20
-  __AUTH_CONST.__auth_got: 0x80
-  __AUTH_CONST.__cfstring: 0x100
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x180
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

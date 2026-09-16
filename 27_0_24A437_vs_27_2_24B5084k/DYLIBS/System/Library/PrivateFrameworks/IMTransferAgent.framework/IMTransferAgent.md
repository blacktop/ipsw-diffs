## IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent`

```diff

-1491.100.1.2.25
-  __TEXT.__text: 0x169c4
+1491.200.63.2.1
+  __TEXT.__text: 0x16abc
   __TEXT.__objc_methlist: 0xa84
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1720
+  __TEXT.__gcc_except_tab: 0x1748
   __TEXT.__cstring: 0xbb3
-  __TEXT.__oslogstring: 0x2a69
+  __TEXT.__oslogstring: 0x2a99
   __TEXT.__unwind_info: 0x5f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd70
+  __DATA_CONST.__objc_selrefs: 0xd80
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x390

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 250
-  Symbols:   263
-  CStrings:  352
+  Symbols:   264
+  CStrings:  353
 
Symbols:
+ _IMStringFromCommSafetyEnablementGroup
Functions:
~ sub_283c0f31c -> sub_2893e131c : 2476 -> 2644
~ sub_283c0fdcc -> sub_2893e1e74 : 1184 -> 1192
~ sub_283c1026c -> sub_2893e231c : 532 -> 536
~ sub_283c12898 -> sub_2893e494c : 1056 -> 1064
~ sub_283c197f8 -> sub_2893eb8b4 : 5536 -> 5596
CStrings:
+ "About to construct the nickname with contentSafetyEnablementGroup: %@"
+ "Avatar image safety check was skipped, comm safety check group setting: %@. Creating IMNicknameAvatarImage."
+ "Download %@ file size %llu -> request priority %ld"
+ "Wallpaper safety check was skipped, comm safety check group setting: %@. Creating IMWallpaper."
- "About to construct the nickname with contentSafetyEnablementGroup: %ld"
- "Avatar image safety check was skipped, comm safety check group setting: %ld. Creating IMNicknameAvatarImage."
- "Wallpaper safety check was skipped, comm safety check group setting: %ld. Creating IMWallpaper."
```

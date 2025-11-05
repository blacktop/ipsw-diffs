## Radius

> `/System/Library/SystemConfiguration/PPPController.bundle/Contents/PlugIns/Radius.ppp/Contents/MacOS/Radius`

```diff

 1016.0.0.0.0
-  __TEXT.__text: 0x3d88
+  __TEXT.__text: 0x3d28
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x1b
   __TEXT.__cstring: 0xf11

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: 7233D205-E5FE-3C52-89CA-116AD3C27E44
+  UUID: 1F745E78-64AC-32E2-A6B8-588101B0025B
   Functions: 50
   Symbols:   143
   CStrings:  161
Functions:
~ sub_2e84 -> sub_81c : 2156 -> 2132
~ _radius_decryptmppekey : 368 -> 364
~ sub_3a48 -> sub_13c4 : 2288 -> 2304
~ _rad_add_server : 380 -> 352
~ _rad_config : 1316 -> 1332
~ _rad_continue_send_request : 1860 -> 1836
~ _rad_create_request : 160 -> 156
~ _rad_get_attr : 156 -> 148
~ _rad_init_send_request : 480 -> 460
~ _rad_auth_open : 152 -> 148
~ _rad_put_attr : 456 -> 452
~ _rad_put_vendor_attr : 288 -> 284
~ sub_64dc -> sub_3e18 : 1616 -> 1612

```

## ACCAppLinksIconService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCAppLinksIconService.xpc/ACCAppLinksIconService`

```diff

-1139.82.1.0.0
-  __TEXT.__text: 0xf58
-  __TEXT.__auth_stubs: 0x220
+1147.100.12.0.0
+  __TEXT.__text: 0xf90
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x28

   __TEXT.__objc_methname: 0x38b
   __TEXT.__objc_methtype: 0x130
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x10

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFB5CDEA-57A1-31FC-842B-981501F40CAF
+  UUID: 53932AFD-FE5D-3ED9-87C9-8D62EF176BCC
   Functions: 17
-  Symbols:   271
+  Symbols:   268
   CStrings:  104
 
Symbols:
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/ACCAppLinksIconService.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/NSData+Hash.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_core_accessories.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_signposts.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_wrapper.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/ACCAppLinksIconService/
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Sources/CoreAccessories/Common/Common_C/
+ /Library/Caches/com.apple.xbs/F5A9EB88-27AF-4280-BB72-BB9A63BAB9AE/TemporaryDirectory.0jPZEO/Sources/CoreAccessories/Common/Common_ObjC/
+ _objc_retainAutoreleasedReturnValue
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/ACCAppLinksIconService.o
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/NSData+Hash.o
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_core_accessories.o
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_signposts.o
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/logging_wrapper.o
- /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCAppLinksIconService.build/Objects-normal/arm64e/main.o
- /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/
- /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/Accessory_Frameworks/CoreAccessories/ACCAppLinksIconService/
- /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_C/
- /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_ObjC/
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ -[NSData(Hash) SHA1] : 172 -> 176
~ -[NSData(Hash) SHA256_16] : 168 -> 172
~ -[NSData(Hash) SHA256] : 168 -> 172
~ -[ServiceDelegate listener:shouldAcceptNewConnection:] : 144 -> 148
~ _main : 96 -> 100
~ +[ACCAppLinksIconService iconImageFromUnmaskedImage:] : 440 -> 456
~ -[ACCAppLinksIconService getIconDataForBundleID:forIconSize:withReply:] : 212 -> 204
~ -[ACCAppLinksIconService _getIconDataForBundleID:forIconSize:withReply:] : 704 -> 732

```

## ApplePayDiagnostics

> `/System/Library/Frameworks/PassKit.framework/PlugIns/ApplePayDiagnostics.appex/ApplePayDiagnostics`

```diff

-1642.6.5.0.0
-  __TEXT.__text: 0x60c
-  __TEXT.__auth_stubs: 0x1c0
+1677.4.0.0.0
+  __TEXT.__text: 0x5d8
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__cstring: 0x54
   __TEXT.__objc_methname: 0x18c
   __TEXT.__oslogstring: 0x145
   __TEXT.__objc_classname: 0x1d
   __TEXT.__objc_methtype: 0x13
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x80
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 276096FE-60CA-36E4-9108-CBE7C7519CE4
+  UUID: D3BA1FD9-22DC-306B-AB86-1FF060C2BAB6
   Functions: 6
-  Symbols:   47
+  Symbols:   46
   CStrings:  29
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retain_x2
+ _objc_storeStrong
- _objc_release_x20
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x24
Functions:
~ sub_100000bf0 : 1348 -> 1312
~ sub_10000114c -> sub_100001128 : 112 -> 96

```

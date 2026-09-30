## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61901.80.25.0.0
-  __TEXT.__text: 0x3c98
+61901.100.267.0.2
+  __TEXT.__text: 0x3e2c
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xd0
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methname: 0x411
   __TEXT.__objc_methtype: 0x17e

   __DATA.__objc_selrefs: 0x190
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AFDE0F72-CD73-32A1-90BD-6A2A13A809BB
+  UUID: 11B9771E-6524-36B0-A3C7-9613173FB9E7
   Functions: 34
   Symbols:   175
   CStrings:  309
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ sub_100000d98 : 724 -> 760
~ sub_1000010dc -> sub_100001100 : 444 -> 464
~ sub_100001344 -> sub_10000137c : 6344 -> 6620
~ sub_100002c0c -> sub_100002d58 : 480 -> 516
~ sub_100002dec -> sub_100002f5c : 176 -> 180
~ sub_100002e9c -> sub_100003010 : 708 -> 728
~ sub_100003160 -> sub_1000032e8 : 100 -> 104
~ sub_1000031c4 -> sub_100003350 : 104 -> 108
~ sub_10000322c -> sub_1000033bc : 732 -> 724
~ sub_100003cbc -> sub_100003e44 : 436 -> 448

```

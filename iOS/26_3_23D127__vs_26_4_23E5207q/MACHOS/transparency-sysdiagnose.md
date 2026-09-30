## transparency-sysdiagnose

> `/usr/libexec/transparency-sysdiagnose`

```diff

-1547.80.8.0.0
-  __TEXT.__text: 0xfa4
+1547.100.130.0.0
+  __TEXT.__text: 0x1008
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x1b4

   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82300145-C356-3B78-BF4D-4D9E5A55445A
+  UUID: DB0A73F3-C9DF-3166-8EB6-AAFE7630DC19
   Functions: 21
   Symbols:   71
   CStrings:  112
Symbols:
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_release_x26
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ sub_100000be0 : 940 -> 956
~ sub_100000fec -> sub_100000ffc : 712 -> 716
~ sub_10000133c -> sub_100001350 : 512 -> 540
~ sub_100001584 -> sub_1000015b4 : 516 -> 524
~ sub_100001788 -> sub_1000017c0 : 112 -> 120
~ sub_1000017f8 -> sub_100001838 : 140 -> 148
~ sub_100001884 -> sub_1000018cc : 180 -> 192
~ sub_100001938 -> sub_10000198c : 148 -> 152
~ sub_100001a64 -> sub_100001abc : 104 -> 112
~ sub_100001acc -> sub_100001b2c : 124 -> 128

```

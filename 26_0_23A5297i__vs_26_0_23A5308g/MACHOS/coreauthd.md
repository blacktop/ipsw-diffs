## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.0.49.0.0
-  __TEXT.__text: 0x3adc0
+2005.0.60.0.0
+  __TEXT.__text: 0x3af6c
   __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_stubs: 0x3420
   __TEXT.__objc_methlist: 0x1954

   __TEXT.__objc_classname: 0x6c9
   __TEXT.__objc_methtype: 0x1f07
   __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__oslogstring: 0x15de
-  __TEXT.__unwind_info: 0xc68
+  __TEXT.__oslogstring: 0x162b
+  __TEXT.__unwind_info: 0xc70
   __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x2130
   __DATA_CONST.__cfstring: 0xdc0

   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_intobj: 0xf0
   __DATA.__objc_const: 0x7908
   __DATA.__objc_selrefs: 0x10b8
   __DATA.__objc_ivar: 0x178

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3A011D6-06F7-361C-A6DE-AAB71597A8F5
+  UUID: 3989EF34-9C6E-3BF4-B65A-5885E484FD2B
   Functions: 1435
-  Symbols:   390
-  CStrings:  1888
+  Symbols:   393
+  CStrings:  1890
 
Symbols:
+ _LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet
+ _LACPolicyOptionNotInteractive
+ _LACPolicyOptionTimeout
Functions:
~ sub_100011de8 : 236 -> 664
CStrings:
+ "Injecting LAOptionTimeout = %d"
+ "Updated options from %{public}@ to %{public}@"

```

## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1341.0.0.0.0
-  __TEXT.__text: 0x42384
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x7be0
-  __TEXT.__objc_methlist: 0x3590
+1347.0.0.0.0
+  __TEXT.__text: 0x425b4
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_stubs: 0x7c60
+  __TEXT.__objc_methlist: 0x3580
   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x1054
   __TEXT.__cstring: 0x28ba
-  __TEXT.__objc_methname: 0xc4d2
-  __TEXT.__oslogstring: 0x9bb6
+  __TEXT.__objc_methname: 0xc547
+  __TEXT.__oslogstring: 0x9c0c
   __TEXT.__objc_classname: 0x6c3
-  __TEXT.__objc_methtype: 0x3665
+  __TEXT.__objc_methtype: 0x3606
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0xe78
   __DATA_CONST.__const: 0x1f48

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x6e8
-  __DATA.__objc_const: 0x5c28
-  __DATA.__objc_selrefs: 0x28a8
+  __DATA.__objc_const: 0x5c20
+  __DATA.__objc_selrefs: 0x28c8
   __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1155
-  Symbols:   449
-  CStrings:  2742
+  Symbols:   450
+  CStrings:  2746
 
Symbols:
+ _NPKPairedOrPairingDeviceSupportsSEPassRelevancy
Functions:
~ sub_100013b1c : 1172 -> 1636
~ sub_100013fb0 -> sub_100014180 : 176 -> 208
~ sub_100018648 -> sub_100018838 : 512 -> 576
CStrings:
+ "Notice: Device does not support SE pass relevancy; suppressing relevancy for pass: %@"
+ "arrayWithCapacity:"
+ "npkRelevancyReasonText"
+ "passByPreservingDeviceOwnedSettingsFromExisting:onIncoming:"
+ "setReasonText:"
- "v36@0:8B16@\"PKAddCarKeyPassConfiguration\"20@?<v@?B@\"PKCarUnlockSupportedTerminal\"@\"NSError\">28"
```

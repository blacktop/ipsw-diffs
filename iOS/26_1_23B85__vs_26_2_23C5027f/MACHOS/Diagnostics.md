## Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

-1066.42.1.0.0
-  __TEXT.__text: 0x156364
+1066.60.12.0.0
+  __TEXT.__text: 0x1563b8
   __TEXT.__auth_stubs: 0x41a0
   __TEXT.__objc_stubs: 0x6780
   __TEXT.__objc_methlist: 0x68dc

   __DATA_CONST.__auth_got: 0x20e0
   __DATA_CONST.__got: 0x11e0
   __DATA_CONST.__auth_ptr: 0x1278
-  __DATA_CONST.__const: 0xd250
+  __DATA_CONST.__const: 0xd258
   __DATA_CONST.__cfstring: 0x1d40
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D72717ED-3BC9-3DE9-B663-F2D3EEF22996
+  UUID: 615D522C-A5F6-36D2-827D-C286F77CC2D6
   Functions: 6996
   Symbols:   1966
   CStrings:  4993
Functions:
~ sub_10000ef2c : 232 -> 224
~ sub_10003e6c8 -> sub_10003e6c0 : 2856 -> 2884
~ sub_100040b28 -> sub_100040b3c : 2152 -> 2168
~ sub_100043700 -> sub_100043724 : 880 -> 936
~ sub_100061f78 -> sub_100061fd4 : 3968 -> 3988
~ sub_1000b30bc -> sub_1000b312c : 3800 -> 3772
CStrings:
+ "Unsupported watch case size %d. Omitting case size from device info"
- "Unsupported watch case size %d. Falling back to default size"

```
